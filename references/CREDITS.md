# リファレンス音源の出典

すべて **Pixabay Content License**（商用可・クレジット表記義務なし・無料）。
実制作曲（AI生成ではない）・インスト。マスタリングの音の基準としてのみ使用し、
再配布・単体販売はしない。

| バケット | ファイル | 曲 / 作者 | 取得元 | 実測(参考) |
|---|---|---|---|---|
| A_calm     | `tvari-tvari-tokyo-cafe-159065.mp3`                 | TVARI – Tokyo Cafe / TVARI                 | https://pixabay.com/music/beats-tvari-tokyo-cafe-159065/ | ~72 BPM / 暗め |
| B_standard | `ambientaudiovision-coverless-book-lofi-186307.mp3` | Coverless book (Lofi) / AmbientAUDIOVISION | https://pixabay.com/music/beats-coverless-book-lofi-186307/ | ~81 BPM / 中庸 |
| C_drive    | `bransboynd-fresh-457883.mp3`                       | Fresh / Bransboynd                         | https://pixabay.com/music/soft-house-fresh-457883/ | ~112 BPM / 明るい・推進 |

取得日: 2026-09-07

補足1: 当初 A/B を入れ替えて配置した。`analyze_references.py` の実測テンポ（Tokyo Cafe が
ハーフタイムで約72、Coverless book が約81）に合わせ、体感テンポが A<B<C になるようにした。

補足2: ⑥ の routing は各リファレンスの実測BPMではなく、`config.BUCKETS` の `bpm_hint`
（設計テンポ A=80 / B=104 / C=128）を使う。3曲が 72〜112 に固まっていて実測だと
「C_drive＝速い曲」というラベルが機能しないため。リファレンス音声そのものは⑦の音色
マッチングでそのまま使う（routing と音作りを分離）。将来、C に本当に速い曲（125BPM前後の
house）、A にもっと遅い曲を入れれば実測ベースに戻してもよい。
