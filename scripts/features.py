"""librosa による音響特徴抽出（⑥ リファレンス選定 / analyze_references 共通）。"""
from __future__ import annotations

from pathlib import Path

import numpy as np


BPM_FOLD_LO = 70.0    # 作業用BGM/lofi/chill の体感テンポはこの帯に収まるので、
BPM_FOLD_HI = 140.0   # librosa が拾いがちな倍/半テンポをこの範囲に畳み込む


def _estimate_bpm(y, sr) -> float:
    """BPM を推定し、倍テンポ・半テンポの取り違えを [70,140) に正規化する。

    librosa.feature.tempo は倍/半テンポに飛びやすいので、より安定な
    beat_track を主に使い、失敗時のみ tempo にフォールバックする。
    """
    import librosa

    try:
        tempo, _beats = librosa.beat.beat_track(y=y, sr=sr)
    except Exception:
        tempo_fn = getattr(librosa.feature, "tempo", None)
        if tempo_fn is None:
            import librosa.feature.rhythm as _rhythm
            tempo_fn = _rhythm.tempo
        tempo = tempo_fn(y=y, sr=sr)

    bpm = float(np.atleast_1d(tempo)[0])
    while bpm >= BPM_FOLD_HI:
        bpm /= 2.0
    while 0 < bpm < BPM_FOLD_LO:
        bpm *= 2.0
    return bpm


def extract_features(path: Path, sr: int = 22050) -> dict:
    """BPM・スペクトル重心（明るさ）・RMS（エネルギー感）を抽出する。"""
    import librosa

    y, _ = librosa.load(str(path), sr=sr, mono=True)
    if y.size == 0:
        raise ValueError(f"音声が空です: {path}")

    bpm = _estimate_bpm(y, sr)

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
