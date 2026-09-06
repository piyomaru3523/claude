"""⑥ リファレンス自動選定【自動】

生成曲を librosa で解析し、references.json の3バケットから重み付き距離で
最も近いものを選ぶ。選定結果（バケット名とリファレンス音源パス）を stdout と
--json に出力する。⑦ はこの結果を使う。

使い方:
  python scripts/step6_pick_reference.py --input work/song_mix.wav --json work/song_ref.json
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from common import die, log, step  # noqa: E402
from features import extract_features, weighted_distance  # noqa: E402

import config  # noqa: E402


def load_index() -> dict:
    if not config.REF_INDEX.exists():
        die(f"{config.REF_INDEX} がありません。先に analyze_references.py を実行してください。")
    index = json.loads(config.REF_INDEX.read_text(encoding="utf-8"))
    if not index:
        die("references.json が空です。各バケットに正規リファレンス音源を入れて再解析してください。")
    return index


def pick(cand: dict, index: dict) -> tuple[str, list[dict]]:
    refs = [dict(bucket=b, **v["features"]) for b, v in index.items()]
    ranked = []
    for r in refs:
        d = weighted_distance(cand, r, refs, config.MATCH_WEIGHTS)
        ranked.append({"bucket": r["bucket"], "distance": round(d, 4),
                       "features": {k: r[k] for k in ("bpm", "spectral_centroid", "rms")}})
    ranked.sort(key=lambda x: x["distance"])
    return ranked[0]["bucket"], ranked


def resolve_ref_file(bucket: str, index: dict) -> Path:
    files = index[bucket].get("files") or []
    if not files:
        die(f"バケット {bucket} にリファレンス音源が登録されていません。")
    return config.REF_DIR / bucket / files[0]


def main() -> int:
    ap = argparse.ArgumentParser(description="⑥ リファレンス自動選定")
    ap.add_argument("--input", type=Path, required=True, help="解析する生成曲（⑤の出力など）")
    ap.add_argument("--json", type=Path, help="選定結果JSONの出力先")
    args = ap.parse_args()

    if not args.input.exists():
        die(f"入力が見つかりません: {args.input}")

    step("⑥ リファレンス自動選定")
    index = load_index()
    cand = extract_features(args.input)
    log(f"生成曲: BPM={cand['bpm']:.1f}  重心={cand['spectral_centroid']:.0f}Hz  RMS={cand['rms']:.4f}")

    best, ranked = pick(cand, index)
    ref_file = resolve_ref_file(best, index)
    for r in ranked:
        mark = " ←選定" if r["bucket"] == best else ""
        b = config.BUCKETS.get(r["bucket"], {})
        log(f"{r['bucket']} ({b.get('label', '')}): 距離 {r['distance']:.4f}"
            f"  [BPM={r['features']['bpm']:.1f}]{mark}")

    result = {
        "input": str(args.input),
        "candidate_features": cand,
        "selected_bucket": best,
        "reference_file": str(ref_file),
        "ranking": ranked,
    }
    step("結果")
    log(f"選定バケット: {best} ({config.BUCKETS.get(best, {}).get('label', '')})")
    log(f"リファレンス音源: {ref_file}")
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
        log(f"JSON: {args.json}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
