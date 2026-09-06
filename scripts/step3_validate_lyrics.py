"""③ 歌詞のモーラ数カウント・禁則チェックを自動実行する。

仕様書の禁則ルール:
  - 1行 12 モーラ超えを検出
  - 拗音 3 連続を検出
  - 「ん」終わりが 2 行連続を検出
  - （--target 指定時）目標モーラ数から ±LYRICS_MORA_TOLERANCE を超える行を検出

入力ファイルの書式（1行1要素）:
  [Verse1]              ← 角括弧だけの行はセクションタグ（カウント対象外）
  (空行)                ← 無視
  遠くの空を見てる        ← 表記のみ。よみは pykakasi で自動推定
  遠くの空 | とおくのそら  ← "表記 | よみ" または "表記<TAB>よみ" で明示（推奨・精度が上がる）

使い方:
  python scripts/step3_validate_lyrics.py path/to/lyrics.txt
  python scripts/step3_validate_lyrics.py lyrics.txt --target targets.txt --json work/lyrics_qc.json
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from common import ROOT, die, log, step  # noqa: E402

import config  # noqa: E402

SMALL_MERGE = set("ゃゅょぁぃぅぇぉゎ")   # 直前の音に合体して独立モーラにならない小書き仮名
CHOON = "ー"
HATSUON = "ん"


def to_hiragana(s: str) -> str:
    out = []
    for ch in s:
        o = ord(ch)
        if 0x30A1 <= o <= 0x30F6:          # カタカナ → ひらがな
            out.append(chr(o - 0x60))
        else:
            out.append(ch)
    return "".join(out)


def has_kanji(s: str) -> bool:
    return any(0x4E00 <= ord(ch) <= 0x9FFF for ch in s)


_KKS = None


def auto_reading(surface: str) -> str | None:
    """pykakasi で表記→ひらがな読みを推定。使えない場合は None。"""
    global _KKS
    if _KKS is None:
        try:
            import pykakasi

            _KKS = pykakasi.kakasi()
        except Exception:
            _KKS = False
    if not _KKS:
        return None
    try:
        return "".join(item["hira"] for item in _KKS.convert(surface))
    except Exception:
        return None


def split_moras(reading: str) -> list[str]:
    """ひらがな読み文字列をモーラ単位に分割する。仮名以外（句読点・空白・漢字）は無視。"""
    hira = to_hiragana(reading)
    moras: list[str] = []
    for ch in hira:
        if ch in SMALL_MERGE:
            if moras:
                moras[-1] += ch                # 直前モーラに合体（拗音・外来音）
            else:
                moras.append(ch)               # 行頭に小書き仮名（禁則側で拾う）
        elif ch == CHOON or 0x3041 <= ord(ch) <= 0x3096:
            moras.append(ch)                   # 基本仮名 / 促音っ / 撥音ん / 長音ー
        # それ以外（漢字・ローマ字・記号・空白）はスキップ
    return moras


def is_yoon(mora: str) -> bool:
    return len(mora) > 1 and mora[-1] in SMALL_MERGE


def max_run(flags: list[bool]) -> int:
    best = cur = 0
    for f in flags:
        cur = cur + 1 if f else 0
        best = max(best, cur)
    return best


def parse_lyrics(path: Path) -> list[dict]:
    rows: list[dict] = []
    for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        text = raw.strip()
        if not text or text.startswith("#"):
            continue
        if text.startswith("[") and text.endswith("]"):
            rows.append({"lineno": lineno, "kind": "section", "section": text})
            continue
        if "|" in text:
            surface, reading = (p.strip() for p in text.split("|", 1))
        elif "\t" in text:
            surface, reading = (p.strip() for p in text.split("\t", 1))
        else:
            surface, reading = text, ""
        rows.append({
            "lineno": lineno, "kind": "lyric",
            "surface": surface, "reading_given": reading,
        })
    return rows


def load_targets(path: Path) -> list[int]:
    vals: list[int] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        t = raw.strip()
        if not t or t.startswith("#"):
            continue
        vals.append(int(t))
    return vals


def analyze(rows: list[dict], targets: list[int] | None) -> dict:
    warnings: list[str] = []
    results: list[dict] = []
    prev_ends_n = False
    ti = 0

    for row in rows:
        if row["kind"] == "section":
            results.append(row | {"section_break": True})
            prev_ends_n = False               # セクションをまたぐ「ん」連続は数えない
            continue

        surface = row["surface"]
        reading = row["reading_given"]
        source = "given"
        if not reading:
            auto = auto_reading(surface)
            if auto is not None:
                reading, source = auto, "pykakasi"
            else:
                reading, source = surface, "surface"
        if has_kanji(reading):
            warnings.append(
                f"L{row['lineno']}: 読みに漢字が残っています（モーラ数が不正確）: 「{surface}」"
                f" — 『表記 | よみ』形式でかな読みを併記してください"
            )

        moras = split_moras(reading)
        n = len(moras)
        yoon_flags = [is_yoon(m) for m in moras]
        yoon_run = max_run(yoon_flags)
        ends_n = bool(moras) and moras[-1] == HATSUON

        flags: list[str] = []
        if n > config.LYRICS_MAX_MORA_PER_LINE:
            flags.append(f"{n}モーラ（{config.LYRICS_MAX_MORA_PER_LINE}超え）")
        if yoon_run > config.LYRICS_MAX_CONSECUTIVE_YOON:
            flags.append(f"拗音{yoon_run}連続")
        if ends_n and prev_ends_n:
            flags.append("「ん」終わり2行連続")

        target = None
        if targets is not None:
            if ti < len(targets):
                target = targets[ti]
                if abs(n - target) > config.LYRICS_MORA_TOLERANCE:
                    flags.append(f"目標{target}±{config.LYRICS_MORA_TOLERANCE}から外れ（{n}）")
            ti += 1

        results.append({
            "lineno": row["lineno"], "kind": "lyric", "surface": surface,
            "reading": reading, "reading_source": source,
            "moras": n, "mora_list": moras, "yoon_run": yoon_run,
            "ends_with_n": ends_n, "target": target, "violations": flags,
        })
        prev_ends_n = ends_n

    if targets is not None and ti != len(targets):
        warnings.append(
            f"--target の行数({len(targets)})と歌詞行数({ti})が一致しません"
        )

    violations = [r for r in results if r.get("violations")]
    return {"results": results, "warnings": warnings, "violation_count": len(violations)}


def print_report(report: dict) -> None:
    step("③ 歌詞検証レポート")
    header = f"{'L':>4}  {'モーラ':>5}  {'拗連':>4}  {'ん末':>4}  歌詞 / 読み"
    print(header)
    print("-" * max(len(header), 60))
    for r in report["results"]:
        if r.get("section_break"):
            print(f"\n{r['section']}")
            continue
        mark = "  ×" if r["violations"] else "   "
        end_n = "ん" if r["ends_with_n"] else "・"
        print(f"{r['lineno']:>4}  {r['moras']:>5}  {r['yoon_run']:>4}  {end_n:>4} {mark} "
              f"{r['surface']}  ／  {r['reading']}"
              + (f"  [{r['reading_source']}]" if r["reading_source"] != "given" else ""))
        for v in r["violations"]:
            print(f"{'':>22}  → {v}")

    if report["warnings"]:
        step("警告")
        for w in report["warnings"]:
            log(w)

    step("結果")
    if report["violation_count"] == 0:
        log("禁則違反なし。④ Suno へ進めます。")
    else:
        log(f"禁則違反 {report['violation_count']} 行。上記 × の行を修正して再実行してください。")


def main() -> int:
    ap = argparse.ArgumentParser(description="③ 歌詞のモーラ数・禁則チェック")
    ap.add_argument("lyrics", type=Path, help="歌詞ファイル（表記のみ / '表記 | よみ'）")
    ap.add_argument("--target", type=Path, help="行ごとの目標モーラ数ファイル（1行1整数）")
    ap.add_argument("--json", type=Path, help="レポートJSONの出力先")
    args = ap.parse_args()

    if not args.lyrics.exists():
        die(f"歌詞ファイルが見つかりません: {args.lyrics}")

    rows = parse_lyrics(args.lyrics)
    if not any(r["kind"] == "lyric" for r in rows):
        die("歌詞行が1行もありません。")

    targets = load_targets(args.target) if args.target else None
    if args.target and not args.target.exists():
        die(f"--target ファイルが見つかりません: {args.target}")

    report = analyze(rows, targets)
    print_report(report)

    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
        log(f"JSON: {args.json}")

    return 1 if report["violation_count"] else 0


if __name__ == "__main__":
    sys.exit(main())
