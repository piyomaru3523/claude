"""⑧ ラウドネス最終調整【自動】

FFmpeg の loudnorm フィルタを2パスで適用し、統合ラウドネスを config.TARGET_LUFS、
True Peak を config.TARGET_TP に合わせる。出力は 24bit / 44.1kHz wav。

使い方:
  python scripts/step8_loudnorm.py --input work/song_master.wav --out work/song_ln.wav
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from common import die, ffmpeg_bin, log, run, step  # noqa: E402

import config  # noqa: E402

SR = 44100


def _measure(src: Path, tp: float, lufs: float) -> dict:
    af = (f"loudnorm=I={lufs}:TP={tp}:"
          f"LRA={config.TARGET_LRA}:print_format=json")
    proc = run([ffmpeg_bin(), "-hide_banner", "-i", str(src), "-af", af,
                "-f", "null", "-"])
    blob = proc.stderr + proc.stdout
    m = re.search(r"\{[^{}]*\"input_i\"[^{}]*\}", blob, re.S)
    if not m:
        die("loudnorm の測定結果(JSON)を解析できませんでした。")
    return json.loads(m.group(0))


def loudnorm(src: Path, out: Path, target_tp: float | None = None,
             target_lufs: float | None = None) -> dict:
    tp = config.TARGET_TP if target_tp is None else target_tp
    lufs = config.TARGET_LUFS if target_lufs is None else target_lufs
    step("⑧ ラウドネス最終調整（2パス loudnorm）")
    log(f"目標 I={lufs} LUFS / TP={tp} dBTP")
    log("1パス目: 測定")
    stats = _measure(src, tp, lufs)
    log(f"  入力 I={stats['input_i']} LUFS / TP={stats['input_tp']} dBTP / LRA={stats['input_lra']}")

    af = (
        f"loudnorm=I={lufs}:TP={tp}:LRA={config.TARGET_LRA}:"
        f"measured_I={stats['input_i']}:measured_TP={stats['input_tp']}:"
        f"measured_LRA={stats['input_lra']}:measured_thresh={stats['input_thresh']}:"
        f"offset={stats['target_offset']}:linear=true:print_format=summary"
    )
    log("2パス目: 適用")
    out.parent.mkdir(parents=True, exist_ok=True)
    run([ffmpeg_bin(), "-hide_banner", "-y", "-i", str(src), "-af", af,
         "-ar", str(SR), "-c:a", "pcm_s24le", str(out)])
    return stats


def main() -> int:
    ap = argparse.ArgumentParser(description="⑧ FFmpeg loudnorm 2パス")
    ap.add_argument("--input", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--target-tp", type=float, help="True Peak 目標の上書き（QC不合格時のリトライ用）")
    ap.add_argument("--target-lufs", type=float, help="統合ラウドネス目標の上書き")
    args = ap.parse_args()
    if not args.input.exists():
        die(f"入力が見つかりません: {args.input}")

    loudnorm(args.input, args.out, args.target_tp, args.target_lufs)
    step("結果")
    log(f"出力: {args.out}  （目標 {config.TARGET_LUFS} LUFS / {config.TARGET_TP} dBTP）")
    log("→ ⑨ step9_qc.py で測定・合否判定してください。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
