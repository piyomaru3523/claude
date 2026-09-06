"""⑩ フォーマット書き出し【自動】

⑨ を通過したマスターを RouteNote 要求フォーマットに変換する。
既定は FLAC 44.1kHz/16bit（RouteNote は WAV 不可）。config.EXPORT_PRESET で切替。
config.KEEP_24BIT_MASTER が True なら output/masters/ に 24bit マスターも残す。

使い方:
  python scripts/step10_export.py --input work/song_ln.wav --name "Focus Rain"
"""
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

from common import die, ffmpeg_bin, log, run, step  # noqa: E402

import config  # noqa: E402


def safe_name(name: str) -> str:
    keep = "-_ () 　".replace(" ", "")
    return "".join(c for c in name if c.isalnum() or c in " -_()　").strip() or "track"


def export(src: Path, name: str) -> Path:
    preset = config.EXPORT_PRESETS[config.EXPORT_PRESET]
    config.OUTPUT_DIR.mkdir(exist_ok=True)
    out = config.OUTPUT_DIR / f"{safe_name(name)}.{preset['ext']}"

    cmd = [ffmpeg_bin(), "-hide_banner", "-y", "-i", str(src),
           "-ar", str(preset["sample_rate"]), "-c:a", preset["codec"]]
    if "sample_fmt" in preset:
        cmd += ["-sample_fmt", preset["sample_fmt"]]
    if "bitrate" in preset:
        cmd += ["-b:a", preset["bitrate"]]
    cmd.append(str(out))
    run(cmd)
    log(f"配信用: {out}  ({config.EXPORT_PRESET})")

    if config.KEEP_24BIT_MASTER:
        masters = config.OUTPUT_DIR / "masters"
        masters.mkdir(exist_ok=True)
        master = masters / f"{safe_name(name)}_master24.wav"
        if src.suffix.lower() == ".wav":
            shutil.copy2(src, master)
        else:
            run([ffmpeg_bin(), "-hide_banner", "-y", "-i", str(src),
                 "-ar", "44100", "-c:a", "pcm_s24le", str(master)])
        log(f"24bitマスター保管: {master}")
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="⑩ フォーマット書き出し")
    ap.add_argument("--input", type=Path, required=True, help="⑨ を通過したマスター（⑧の出力）")
    ap.add_argument("--name", required=True, help="曲名（ファイル名になる）")
    args = ap.parse_args()
    if not args.input.exists():
        die(f"入力が見つかりません: {args.input}")

    step("⑩ フォーマット書き出し")
    out = export(args.input, args.name)
    step("結果")
    log(f"完成: {out}")
    log("→ ⑪ 人が試聴確認 → RouteNote へアップロード（AI関与の開示を忘れずに）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
