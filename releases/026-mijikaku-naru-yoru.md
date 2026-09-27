# Release 026 — 短くなる夜

| 項目 | 値 |
|---|---|
| 配信タイトル | （タイトル未定・歳詞確定後に決定） |
| slug | mijikaku-naru-yoru |
| テーマ | 時間が短いほど、濃くなる。だから毎晩が必死だ |
| 主張（論法） | 毎日短くなる夜→その中の濃さ（帰納法） |
| 情景 | 初夏、日が長くなり始めて、夜が短い季節 |
| Style | 案B（アップテンポ・キリッとしたロウファイ） |
| ステータス | 歌詞検証済み（③禁則違反なし）。Style/Exclude確定後、Suno生成へ |

## Suno 入力

### Style欄
```
The night is shrinking — lo-fi, urgent but contained, with subtle momentum. A young Japanese female voice, warm and focused, sings with quiet intensity, breathy and close, recorded with pristine clarity. Beneath, crisp synth pads and a single bright muted key phrase that repeats with gentle insistence, chords suggesting urgency without panic. Production stays low, warm and pristine: bright keys, analog pad haze, a soft room reverb, crystal-clear, nothing harsh or forward. A subtle boom-bap kick and crisp brushed hi-hats hold a steady 115 BPM with just enough momentum to feel the time passing; a soft round bass walks with purpose. The arrangement builds through verses into a chorus that affirms the intensity of now, a bridge that thins to one voice and held pad, then eases back. Everything sits back in the mix, repeatable, a loop to work beside with quiet urgency.
```

### Exclude Styles欄
```
vinyl crackle, tape hiss, hissy noise floor, pop brightness, overly upbeat progressions, lazy production, drowsy tempo, EDM festival bombast, big-room drops, aggressive techno, trap percussion cliches, loud belted vocals, excessive autotune, harsh compression, brittle sibilant highs, plastic synth textures, sterile digital reverb, predictable four-chord loops
```

### 歌詞欄（かな。外来語のみカタカナ。③検証済み・禁則違反なし）
```
[Intro]

[Verse1]
しょしょきの
よるは
みじかい
きのうより
もっと
みじかくなる
あした
もっともっと
みじかくなる
だから
ここにいる
ぼくらは
ひっし

[PreChorus]
じかんが
へっていく
だから
こいから
ぬける

[Chorus]
ここにいるじかんが
みじかいから
もっと
こい
もっと
きらきら
するんだ
だから
まいばん
ひっしだ

[Verse2]
あい
にんげんは
じかんが
へるほど
あわてる
きみの
こえが
ちいさく
きこえるから
もっと
ちかい

[Chorus]
ここにいるじかんが
みじかいから
ぎゅっと
いまを
つかんで
はなさない
だから
まいばん
ひっしだ

[Bridge]
よが
きえていく
だから
ああ

[Chorus]
ここにいるじかんが
みじかいから
もっともっと
きらきら
する

[Outro]
よが
みじかいから
```

---

## ステップ完了
- ①テーマ分析: 完了（テーマ・主張・情景確定）
- ②歌詞執筆: 完了
- ③歌詞検証: 完了（禁則違反なし）
- ④～⑩（Suno生成〜マスタリング）: 生成前

## ⑪-a ジャケット（`branding.md` テンプレ準拠）
シーン: 初夏、もう白み始める窓とまだ点いているデスクランプ、氷の溶けかけたグラス。
```
soft hand-drawn illustration, anime-adjacent, warm muted palette, an open window with a pale dawn already on the horizon in early summer, a desk lamp still lit, a half-finished glass of iced tea and a small clock on the desk, person only as a small back view or none, a glowing warm light as the single light source off-center, deep indigo-navy shadows with warm amber light, gentle linework, grainy textured shading, cozy and quiet, no visible face, generous empty space, square, no text
```
ネガティブ: `text, watermark, signature, harsh outlines, bright daylight, oversaturated, chibi, busy background, faces`
生成後にサイン合成: `python scripts/add_signature.py covers/026-mijikaku-naru-yoru_bg.jpg covers/026-mijikaku-naru-yoru.jpg`（背景は `_bg.jpg` で保存）。
