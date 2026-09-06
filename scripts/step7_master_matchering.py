"""⑦ マスタリング【自動】

Matchering で ⑥ が選定したリファレンスに EQ/ラウドネス/ダイナミクスを寄せる。
リファレンスの音声そのものはコピーされず、周波数・音量特性の解析結果だけが使われる。

使い方:
  python scripts/step7_master_matchering.py --input work/song_mix.wav \
      --ref-json work/song_ref.json --out work/song_master.wav
  # リファレンスを直接指定することも可能:
  python scripts/step7_master_matchering.py --input work/song_mix.wav \
      --reference references/B_standard/ref.wav --out work/song_master.wav
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from common import die, log, step  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser(description="⑦ Matchering マスタリング")
    ap.add_argument("--input", type=Path, required=True, help="マスタリング対象（⑤の出力）")
    ap.add_argument("--out", type=Path, required=True, help="出力 wav（24bit, work/ 配下想定）")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--ref-json", type=Path, help="⑥ step6 の選定結果JSON")
    g.add_argument("--reference", type=Path, help="リファレンス音源を直接指定")
    args = ap.parse_args()

    if not args.input.exists():
        die(f"入力が見つかりません: {args.input}")

    if args.reference:
        reference = args.reference
    else:
        if not args.ref_json.exists():
            die(f"--ref-json が見つかりません: {args.ref_json}")
        reference = Path(json.loads(args.ref_json.read_text(encoding="utf-8"))["reference_file"])
    if not reference.exists():
        die(f"リファレンス音源が見つかりません: {reference}")

    step("⑦ Matchering マスタリング")
    log(f"対象      : {args.input.name}")
    log(f"リファレンス: {reference}")

    import matchering as mg

    mg.log(info_handler=log, warning_handler=lambda m: log(f"WARN: {m}"))

    args.out.parent.mkdir(parents=True, exist_ok=True)
    mg.process(
        target=str(args.input),
        reference=str(reference),
        results=[mg.pcm24(str(args.out))],
    )

    step("結果")
    log(f"出力: {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
