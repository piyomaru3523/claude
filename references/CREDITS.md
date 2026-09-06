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

補足: 当初 A/B を入れ替えて配置した。`analyze_references.py` の実測テンポ（Tokyo Cafe が
ハーフタイムで約72、Coverless book が約81）に合わせ、体感テンポが A<B<C になるようにした。
3曲とも同じ「チル系lofi」帯なので分離は緩め。将来もっと明確に分けたい場合は、A にもっと
遅い曲、C にもっと速い曲（125BPM前後の soft house/house）を差し替えるとよい。
