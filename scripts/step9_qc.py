"""⑨ QCチェック【自動】

pyloudnorm で統合ラウドネスを、4倍オーバーサンプリングで True Peak を測定し、
config の目標値・許容誤差に収まっているか判定する。外れていれば exit 1
（run_audio.py が ⑧ を再実行する）。

使い方:
  python scripts/step9_qc.py --input work/song_ln.wav --json work/song_qc.json
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np

from common import die, log, step  # noqa: E402

import config  # noqa: E402

TP_EST_MARGIN = 0.1   # オーバーサンプリング推定の誤差ぶん緩める (dB)


def measure(path: Path) -> dict:
    import pyloudnorm as pyln
    import soundfile as sf
    from scipy.signal import resample_poly

    data, rate = sf.read(str(path))
    meter = pyln.Meter(rate)
    lufs = float(meter.integrated_loudness(data))

    oversampled = resample_poly(data, 4, 1, axis=0)
    peak = float(np.max(np.abs(oversampled)))
    tp_dbtp = float(20.0 * np.log10(peak)) if peak > 0 else float("-inf")

    sample_peak = float(np.max(np.abs(data)))
    sp_dbfs = float(20.0 * np.log10(sample_peak)) if sample_peak > 0 else float("-inf")
    return {"lufs": round(lufs, 2), "true_peak_dbtp": round(tp_dbtp, 2),
            "sample_peak_dbfs": round(sp_dbfs, 2)}


def judge(m: dict) -> dict:
    lufs_err = abs(m["lufs"] - config.TARGET_LUFS)
    lufs_ok = bool(lufs_err <= config.QC_TOLERANCE_LUFS)
    tp_ok = bool(m["true_peak_dbtp"] <= config.QC_TP_CEILING + TP_EST_MARGIN)
    return {"lufs_ok": lufs_ok, "tp_ok": tp_ok, "passed": lufs_ok and tp_ok,
            "lufs_error": round(lufs_err, 2)}


def main() -> int:
    ap = argparse.ArgumentParser(description="⑨ ラウドネス/TP の QC")
    ap.add_argument("--input", type=Path, required=True)
    ap.add_argument("--json", type=Path)
    args = ap.parse_args()
    if not args.input.exists():
        die(f"入力が見つかりません: {args.input}")

    step("⑨ QCチェック")
    m = measure(args.input)
    v = judge(m)
    log(f"統合ラウドネス : {m['lufs']:.2f} LUFS  (目標 {config.TARGET_LUFS} ±{config.QC_TOLERANCE_LUFS})"
        f"  {'OK' if v['lufs_ok'] else 'NG'}")
    log(f"True Peak      : {m['true_peak_dbtp']:.2f} dBTP  (上限 {config.QC_TP_CEILING})"
        f"  {'OK' if v['tp_ok'] else 'NG'}")
    log(f"サンプルピーク : {m['sample_peak_dbfs']:.2f} dBFS")

    result = {"input": str(args.input), **m, **v,
              "target_lufs": config.TARGET_LUFS, "tp_ceiling": config.QC_TP_CEILING}
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

    step("結果")
    if v["passed"]:
        log("合格。⑩ フォーマット書き出しへ進めます。")
        return 0
    log("不合格。⑧ ラウドネス調整をやり直してください。")
    return 1


if __name__ == "__main__":
    sys.exit(main())
