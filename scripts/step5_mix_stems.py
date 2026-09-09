"""⑤ ステムバランス調整【自動】

Suno のパート別（ステム）ダウンロードがある場合、パートごとに config.STEM_GAIN_DB の
ゲインと軽いハイパスをかけて合算し、ミックスバスに控えめな整音をしてミックスダウンする。

入力が単一ファイル（完成ミックス）の場合は処理せずフォーマット標準化のみ行う。

使い方:
  python scripts/step5_mix_stems.py --input input/song_stems --out work/song_mix.wav
  python scripts/step5_mix_stems.py --input input/song.wav   --out work/song_mix.wav
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np

from common import AUDIO_EXTS, die, find_audio, log, step  # noqa: E402

import config  # noqa: E402

TARGET_SR = 44100
MIX_PEAK_DBFS = -6.0          # マスタリング前のヘッドルーム確保


def _read_stereo(path: Path, sr: int) -> np.ndarray:
    """(2, n) float32 で読み込む。サンプルレートを揃え、モノはステレオ複製。"""
    from pedalboard.io import AudioFile

    with AudioFile(str(path)).resampled_to(sr) as f:
        audio = f.read(f.frames)
    if audio.ndim == 1:
        audio = audio[np.newaxis, :]
    if audio.shape[0] == 1:
        audio = np.repeat(audio, 2, axis=0)
    elif audio.shape[0] > 2:
        audio = audio[:2, :]
    return audio.astype(np.float32)


def _write(path: Path, audio: np.ndarray, sr: int) -> None:
    from pedalboard.io import AudioFile

    path.parent.mkdir(parents=True, exist_ok=True)
    with AudioFile(str(path), "w", samplerate=sr, num_channels=audio.shape[0], bit_depth=24) as f:
        f.write(audio)


def _gain_for(name: str) -> float:
    low = name.lower()
    for kw, g in config.STEM_GAIN_DB.items():
        if kw in low:
            return g
    return 0.0


def mix_stems(stems: list[Path], out: Path) -> None:
    from pedalboard import Compressor, Gain, HighpassFilter, Pedalboard

    layers = []
    for s in stems:
        audio = _read_stereo(s, TARGET_SR)
        g = _gain_for(s.name)
        board = Pedalboard([HighpassFilter(cutoff_frequency_hz=25), Gain(gain_db=g)])
        layers.append(board(audio, TARGET_SR))
        log(f"stem: {s.name}  gain {g:+.1f} dB")

    n = max(l.shape[1] for l in layers)
    mix = np.zeros((2, n), dtype=np.float32)
    for l in layers:
        mix[:, : l.shape[1]] += l

    c = config.MIX_BUS_COMP
    bus = Pedalboard([
        HighpassFilter(cutoff_frequency_hz=config.MIX_BUS_HIGHPASS_HZ),
        Compressor(threshold_db=c["threshold_db"], ratio=c["ratio"],
                   attack_ms=c["attack_ms"], release_ms=c["release_ms"]),
    ])
    mix = bus(mix, TARGET_SR)

    peak = float(np.max(np.abs(mix))) or 1.0
    target = 10 ** (MIX_PEAK_DBFS / 20)
    mix *= target / peak
    log(f"ミックスバス整音 + ピーク {MIX_PEAK_DBFS:.1f} dBFS 正規化")
    _write(out, mix, TARGET_SR)


def standardize(src: Path, out: Path) -> None:
    audio = _read_stereo(src, TARGET_SR)
    peak = float(np.max(np.abs(audio)))
    if peak > 10 ** (MIX_PEAK_DBFS / 20):
        audio *= (10 ** (MIX_PEAK_DBFS / 20)) / peak
        log(f"ピークが高いため {MIX_PEAK_DBFS:.1f} dBFS に抑制")
    _write(out, audio, TARGET_SR)


VOCAL_KEYWORDS = ("vocal", "voice", "vox")


def main() -> int:
    ap = argparse.ArgumentParser(description="⑤ ステムバランス調整 / ミックスダウン")
    ap.add_argument("--input", type=Path, required=True, help="ステムのディレクトリ または 完成ミックスのファイル")
    ap.add_argument("--out", type=Path, required=True, help="出力 wav（work/ 配下想定）")
    ap.add_argument("--instrumental", action="store_true",
                    help="ボーカル系ステム（vocal/voice/vox）を除外してインスト版を作る")
    ap.add_argument("--exclude", default="",
                    help="除外するステム名キーワード（カンマ区切り、部分一致・小文字）")
    args = ap.parse_args()

    drop = [k.strip().lower() for k in args.exclude.split(",") if k.strip()]
    if args.instrumental:
        drop += list(VOCAL_KEYWORDS)

    step("⑤ ステムバランス調整" + ("（インスト）" if args.instrumental else ""))
    if args.input.is_dir():
        stems = [p for p in find_audio(args.input) if p.suffix.lower() in AUDIO_EXTS]
        if not stems:
            die(f"ステムが見つかりません: {args.input}")
        if drop:
            kept = [p for p in stems if not any(k in p.name.lower() for k in drop)]
            for p in stems:
                if p not in kept:
                    log(f"除外: {p.name}")
            stems = kept
            if not stems:
                die("除外の結果ステムが0本になりました。")
        if len(stems) == 1:
            log("ステム1本のみ → 標準化のみ実施")
            standardize(stems[0], args.out)
        else:
            log(f"ステム {len(stems)} 本をミックスダウン")
            mix_stems(stems, args.out)
    else:
        if not args.input.exists():
            die(f"入力が見つかりません: {args.input}")
        log("単一ファイル入力 → フォーマット標準化のみ（ステム処理なし）")
        standardize(args.input, args.out)

    step("結果")
    log(f"出力: {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
