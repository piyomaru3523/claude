"""⑤〜⑩ を1曲分まとめて実行するオーケストレータ。

  ⑤ ステム調整/ミックスダウン → ⑥ リファレンス選定 → ⑦ Matchering →
  ⑧ loudnorm → ⑨ QC（不合格なら ⑧ をより保守的な TP でリトライ）→ ⑩ 書き出し

使い方:
  # 完成ミックス1本
  python scripts/run_audio.py --input input/song.wav --name "Focus Rain"
  # ステム一式（フォルダ）
  python scripts/run_audio.py --input input/song_stems --name "Focus Rain"
  # ステムから本編＋インスト版を両方
  python scripts/run_audio.py --input input/song_stems --name "Focus Rain" --instrumental
"""
from __future__ import annotations

import argparse
import json as _json
import subprocess
import sys
from pathlib import Path

from common import ROOT, die, log, step  # noqa: E402
from step8_loudnorm import loudnorm  # noqa: E402
from step9_qc import judge, measure  # noqa: E402
from step10_export import safe_name  # noqa: E402

import config  # noqa: E402

SCRIPTS = ROOT / "scripts"


def sh(script: str, *args: str) -> None:
    cmd = [sys.executable, str(SCRIPTS / script), *args]
    proc = subprocess.run(cmd, cwd=str(ROOT))
    if proc.returncode != 0:
        die(f"{script} が失敗しました (exit {proc.returncode})")


def process(input_path: Path, name: str, keep_going: bool, instrumental: bool) -> bool:
    """1曲分の ⑤〜⑩。QC 合格なら True。"""
    slug = safe_name(name).replace(" ", "_").replace("　", "_")
    w = config.WORK_DIR
    mix = w / f"{slug}_mix.wav"
    ref_json = w / f"{slug}_ref.json"
    master = w / f"{slug}_master.wav"
    ln = w / f"{slug}_ln.wav"
    qc_json = w / f"{slug}_qc.json"

    step(f"▶ {name}  ({input_path})")

    step5_args = ["--input", str(input_path), "--out", str(mix)]
    if instrumental:
        step5_args.append("--instrumental")
    sh("step5_mix_stems.py", *step5_args)
    sh("step6_pick_reference.py", "--input", str(mix), "--json", str(ref_json))
    sh("step7_master_matchering.py", "--input", str(mix), "--ref-json", str(ref_json),
       "--out", str(master))

    passed = False
    m = v = None
    for attempt in range(config.QC_MAX_RETRY + 1):
        tp = config.TARGET_TP - 0.5 * attempt
        if attempt:
            log(f"QCリトライ {attempt}/{config.QC_MAX_RETRY}：TP目標を {tp} dBTP に引き締めて再調整")
        loudnorm(master, ln, target_tp=tp)
        m = measure(ln)
        v = judge(m)
        log(f"QC: {m['lufs']:.2f} LUFS / {m['true_peak_dbtp']:.2f} dBTP → "
            + ("合格" if v["passed"] else "不合格"))
        if v["passed"]:
            passed = True
            break

    qc_json.write_text(_json.dumps({**m, **v}, ensure_ascii=False, indent=2), encoding="utf-8")

    if not passed and not keep_going:
        die("QCが最後まで合格しませんでした。--keep-going で強制続行できますが、値を確認してください。")
    if not passed:
        log("WARN: QC未合格。--keep-going 指定のため⑩へ進みます。")

    sh("step10_export.py", "--input", str(ln), "--name", name)
    return passed


def main() -> int:
    ap = argparse.ArgumentParser(description="⑤〜⑩ 一括実行")
    ap.add_argument("--input", type=Path, required=True, help="Sunoからのダウンロード（ファイル or ステムのフォルダ）")
    ap.add_argument("--name", required=True, help="曲名")
    ap.add_argument("--keep-going", action="store_true",
                    help="QCが最後まで通らなくても⑩まで進める（既定は中断）")
    ap.add_argument("--instrumental", action="store_true",
                    help="本編に加えてボーカル抜きのインスト版も書き出す（ステム入力時のみ）")
    args = ap.parse_args()
    if not args.input.exists():
        die(f"入力が見つかりません: {args.input}")

    want_inst = args.instrumental and args.input.is_dir()
    if args.instrumental and not args.input.is_dir():
        log("WARN: --instrumental はステムのフォルダ入力時のみ。インスト版はスキップします。")

    ok = process(args.input, args.name, args.keep_going, instrumental=False)
    if want_inst:
        ok = process(args.input, f"{args.name} (Instrumental)", args.keep_going,
                     instrumental=True) and ok

    step("完了")
    log(f"配信用ファイルは {config.OUTPUT_DIR} を確認してください。")
    log("⑪ 人が試聴 → RouteNote へアップロード（AI関与の開示 / 商用利用権の確認を忘れずに）")
    return 0 if ok else 2


if __name__ == "__main__":
    sys.exit(main())
