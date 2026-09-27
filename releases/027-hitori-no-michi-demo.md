# Release 027 — 一人の道でも

| 項目 | 値 |
|---|---|
| 配信タイトル | （タイトル未定・歌詞確定後に決定） |
| slug | hitori-no-michi-demo |
| テーマ | 誰かの声が一人の夜道を、優しく照らす |
| 主張（論法） | ラジオの声→キミの記憶→温かさ（帰納法） |
| 情景 | 仕事帰り、イヤホンからラジオの声、キミのことを思い出す |
| Style | 案A（ウォーム・コンフォート） |
| ステータス | 歌詞検証済み（③禁則違反なし）。Style/Exclude確定後、Suno生成へ |

## Suno 入力

### Style欄
```
A familiar voice in the dark — lo-fi, warm, comforting like a radio late at night. A young Japanese female voice, breathy and close, hums the melody as if accompanying a broadcast, intimate and private, recorded with pristine clarity. Beneath, soft synth pads drift like voices through headphones, a single muted key phrase answers gently, chords leaning major. Production stays low, warm and clean: rounded keys, analog pad haze, a soft room reverb, crystal-clear, nothing sharp or forward. A gentle boom-bap kick and brushed swung hi-hats hold an unhurried 100 BPM; a soft round bass walks beneath. The arrangement breathes in slow tides — hushed verses where you feel alone but held, a chorus that lifts with recognition, a bridge that thins to one voice and held pad, then eases back. Everything sits back in the mix, calm and repeatable, a loop to walk beside.
```

### Exclude Styles欄
```
vinyl crackle, tape hiss, hissy noise floor, radio static, pop brightness, overly upbeat progressions, energetic beats, EDM festival bombast, big-room drops, aggressive techno, trap percussion cliches, loud belted vocals, excessive autotune, harsh compression, brittle sibilant highs, plastic synth textures, sterile digital reverb, predictable four-chord loops
```

### 歌詞欄（かな。外来語のみカタカナ。③検証済み・禁則違反なし）
```
[Intro]

[Verse1]
ひとりの
かえりみち
イヤホンから
ラジオの
こえが
とぎれとぎれに
きこえる
だれかの
こえが
してくると
あんしん
する
ひとりだけどな

[PreChorus]
その
こえを
きいてると
キミを
おもいだす

[Chorus]
だれかの
こえが
ゆりかごみたい
ひかりみたい
あったかい
だから
ひとりでも
このみちが
やさしい

[Verse2]
まっくらな
みちでも
せなか
あたたかくて
まるで
キミが
そばにいるみたい
ラジオの
パーソナリティの
こえが
キミに
きこえて
くる

[Chorus]
だれかの
こえが
ゆりかごみたい
ひかりみたい
あたたかい
だから
ひとりでも
このみちで
あるけるんだ

[Bridge]
こえが
あると
ひかりが
ある

[Chorus]
だれかの
こえが
やさしくて
ここまで
つれてきてくれる

[Outro]
ひとりの
みちでも
ひかりが
ある
```

---

## ステップ完了
- ①テーマ分析: 完了（テーマ・主張・情景確定）
- ②歌詞執筆: 完了
- ③歌詞検証: 完了（禁則違反なし）
- ④～⑩（Suno生成〜マスタリング）: 生成前

## ⑪-a ジャケット（`branding.md` テンプレ準拠）
シーン: 夜の帰り道、後ろ姿が小さく。街灯1つ、遠くに灯る窓。
```
soft hand-drawn illustration, anime-adjacent, warm muted palette, a small figure seen from behind walking an empty night street, earphone cable trailing, a single street lamp off-center, one distant lit window, tiny in the frame, a glowing warm light as the single light source off-center, deep indigo-navy shadows with warm amber light, gentle linework, grainy textured shading, cozy and quiet, no visible face, generous empty space, square, no text
```
ネガティブ: `text, watermark, signature, harsh outlines, bright daylight, oversaturated, chibi, busy background, faces`
生成後にサイン合成: `python scripts/add_signature.py covers/027-hitori-no-michi-demo_bg.jpg covers/027-hitori-no-michi-demo.jpg`（背景は `_bg.jpg` で保存）。
