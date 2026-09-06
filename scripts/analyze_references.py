"""references/<bucket>/ 内のリファレンス音源を解析し references.json を生成する。

⑥ の自動選定はこのインデックスを参照する。リファレンス音源を追加・差し替えたら
再実行すること。1バケットに複数入れると特徴量の平均を取る。
"""
from __future__ import annotations

import json
import sys

from common import find_audio, log, step  # noqa: E402
from features import extract_features  # noqa: E402

import config  # noqa: E402


def main() -> int:
    step("リファレンス解析")
    index: dict[str, dict] = {}
    missing: list[str] = []

    for bucket, meta in config.BUCKETS.items():
        folder = config.REF_DIR / bucket
        folder.mkdir(parents=True, exist_ok=True)
        files = find_audio(folder)
        if not files:
            missing.append(bucket)
            log(f"{bucket} ({meta['label']}): 音源なし — スキップ")
            continue

        feats = [extract_features(f) for f in files]
        avg = {
            k: round(sum(d[k] for d in feats) / len(feats), 6)
            for k in ("bpm", "spectral_centroid", "rms")
        }
        index[bucket] = {
            "label": meta["label"],
            "files": [f.name for f in files],
            "features": avg,
        }
        log(f"{bucket} ({meta['label']}): {len(files)}曲  "
            f"BPM={avg['bpm']:.1f}  重心={avg['spectral_centroid']:.0f}Hz  RMS={avg['rms']:.4f}")

    config.REF_INDEX.write_text(
        json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    step("結果")
    log(f"書き出し: {config.REF_INDEX}")
    if missing:
        log(f"未設定バケット: {', '.join(missing)} — 各フォルダに正規音源を1曲入れて再実行してください。")
    return 0 if len(index) == len(config.BUCKETS) else 1


if __name__ == "__main__":
    sys.exit(main())
