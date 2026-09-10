"""③ の検証用歌詞ファイル（表記 | よみ）から Suno 貼り付け用のかな歌詞を書き出す。

- セクションタグ [Verse1] 等はそのまま
- 各行は「よみ」側だけを採用
- 外来語のひらがなを慣用のカタカナに置換
- コメント行（#）と空行のセクション内空行は除去

使い方:
  python scripts/make_suno_lyrics.py work/lyrics_002_yoake-mae.txt
    -> work/lyrics_002_yoake-mae_suno.txt
"""
from __future__ import annotations

import sys
from pathlib import Path

# 外来語のひらがな読み -> カタカナ表記
LOANWORDS = {
    "こーひー": "コーヒー", "かっぷ": "カップ", "りずむ": "リズム", "ぺん": "ペン",
    "ぺーす": "ペース", "ぺーじ": "ページ", "のーと": "ノート", "ほーむ": "ホーム",
    "いやほん": "イヤホン", "さぼり": "サボり",
}


def to_suno(reading: str) -> str:
    for h, k in LOANWORDS.items():
        reading = reading.replace(h, k)
    return reading


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: make_suno_lyrics.py <lyrics_file>", file=sys.stderr)
        return 2
    src = Path(sys.argv[1])
    out = src.with_name(src.stem + "_suno.txt")

    lines: list[str] = []
    for raw in src.read_text(encoding="utf-8").splitlines():
        t = raw.strip()
        if not t or t.startswith("#"):
            if not t and lines and lines[-1].startswith("["):
                lines.append("")  # セクション直後の空行は残す（Suno可読性）
            continue
        if t.startswith("[") and t.endswith("]"):
            if lines:
                lines.append("")
            lines.append(t)
            continue
        reading = t.split("|", 1)[1].strip() if "|" in t else t
        lines.append(to_suno(reading))

    # 連続する空行を1つに畳む
    collapsed: list[str] = []
    for ln in lines:
        if ln == "" and collapsed and collapsed[-1] == "":
            continue
        collapsed.append(ln)
    text = "\n".join(collapsed).strip() + "\n"
    out.write_text(text, encoding="utf-8")
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
