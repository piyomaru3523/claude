"""⑤〜⑩ を1曲分まとめて実行するオーケストレータ。

  ⑤ ステム調整/ミックスダウン → ⑥ リファレンス選定 → ⑦ Matchering →
  ⑧ loudnorm → ⑨ QC（不合格なら ⑧ をより保守的な TP でリトライ）→ ⑩ 書き出し

使い方:
  # 完成ミックス1本
  python scripts/run_audio.py --input input/song.wav --name "Focus Rain"
  # ステム一式（フォルダ）
  python scripts/run_audio.py --input input/song_stems --name "Focus Rain"
"""
from __future__ import annotations

import argparse
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


def main() -> int:
    ap = argparse.ArgumentParser(description="⑤〜⑩ 一括実行")
    ap.add_argument("--input", type=Path, required=True, help="Sunoからのダウンロード（ファイル or ステムのフォルダ）")
    ap.add_argument("--name", required=True, help="曲名")
    ap.add_argument("--keep-going", action="store_true",
                    help="QCが最後まで通らなくても⑩まで進める（既定は中断）")
    args = ap.parse_args()
    if not args.input.exists():
        die(f"入力が見つかりません: {args.input}")

    slug = safe_name(args.name).replace(" ", "_").replace("　", "_")
    w = config.WORK_DIR
    mix = w / f"{slug}_mix.wav"
    ref_json = w / f"{slug}_ref.json"
    master = w / f"{slug}_master.wav"
    ln = w / f"{slug}_ln.wav"
    qc_json = w / f"{slug}_qc.json"

    step(f"▶ {args.name}  ({args.input})")

    sh("step5_mix_stems.py", "--input", str(args.input), "--out", str(mix))
    sh("step6_pick_reference.py", "--input", str(mix), "--json", str(ref_json))
    sh("step7_master_matchering.py", "--input", str(mix), "--ref-json", str(ref_json),
       "--out", str(master))

    passed = False
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

    import json as _json
    qc_json.write_text(_json.dumps({**m, **v}, ensure_ascii=False, indent=2), encoding="utf-8")

    if not passed:
        msg = "QCが最後まで合格しませんでした。"
        if not args.keep_going:
            die(msg + " --keep-going で強制続行できますが、値を確認してください。")
        log("WARN: " + msg + " --keep-going 指定のため⑩へ進みます。")

    sh("step10_export.py", "--input", str(ln), "--name", args.name)

    step("完了")
    log(f"配信用ファイルは {config.OUTPUT_DIR} を確認してください。")
    log("⑪ 人が試聴 → RouteNote へアップロード（AI関与の開示 / 商用利用権の確認を忘れずに）")
    return 0 if passed else 2


if __name__ == "__main__":
    sys.exit(main())
