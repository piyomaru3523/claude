"""librosa による音響特徴抽出（⑥ リファレンス選定 / analyze_references 共通）。"""
from __future__ import annotations

from pathlib import Path

import numpy as np


def extract_features(path: Path, sr: int = 22050) -> dict:
    """BPM・スペクトル重心（明るさ）・RMS（エネルギー感）を抽出する。"""
    import librosa

    y, _ = librosa.load(str(path), sr=sr, mono=True)
    if y.size == 0:
        raise ValueError(f"音声が空です: {path}")

    # BPM: librosa のバージョン差を吸収
    tempo_fn = getattr(librosa.feature, "tempo", None)
    if tempo_fn is None:
        import librosa.feature.rhythm as _rhythm  # librosa 一部バージョン
        tempo_fn = _rhythm.tempo
    bpm = float(np.atleast_1d(tempo_fn(y=y, sr=sr))[0])

    centroid = float(np.mean(librosa.feature.spectral_centroid(y=y, sr=sr)))
    rms = float(np.mean(librosa.feature.rms(y=y)))
    return {
        "bpm": round(bpm, 2),
        "spectral_centroid": round(centroid, 2),
        "rms": round(rms, 6),
        "duration_sec": round(len(y) / sr, 2),
    }


_KEYS = ("bpm", "spectral_centroid", "rms")


def weighted_distance(cand: dict, ref: dict, others: list[dict], weights: dict) -> float:
    """cand と ref の重み付きユークリッド距離。
    others（全バケット + cand）で各特徴を min-max 正規化してからスケールを揃える。"""
    pool = others + [cand]
    dist_sq = 0.0
    for k in _KEYS:
        vals = [d[k] for d in pool]
        lo, hi = min(vals), max(vals)
        span = (hi - lo) or 1.0
        nc = (cand[k] - lo) / span
        nr = (ref[k] - lo) / span
        dist_sq += weights[k] * (nc - nr) ** 2
    return dist_sq ** 0.5
