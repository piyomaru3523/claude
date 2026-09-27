# Release 024 — 季節のはじまり

| 項目 | 値 |
|---|---|
| 配信タイトル | （タイトル未定・歌詞確定後に決定） |
| slug | kisetsuno-hajimari |
| テーマ | 季節が変わっても、キミとの約束は変わらない |
| 主張（論法） | 肌で感じる温度変化→永遠性（帰納法） |
| 情景 | 初春、上着を脱ぎ始める夜、風が変わった感覚 |
| Style | 案C（トランジション・シネマティック） |
| ステータス | 歌詞検証済み（③禁則違反なし）。Style/Exclude確定後、Suno生成へ |

## Suno 入力

### Style欄
```
Spring arrives in a breath of warm wind — lo-fi, cinematic, with subtle orchestral undertones. A young Japanese female voice, warm and clear, sings the melody with quiet certainty, breathy and close, recorded with pristine clarity. Beneath, felt piano and long reverb tails, soft strings that suggest rather than state, chords drifting between major and a wistful seventh. Production stays low, warm and pristine: felt piano, analog pad haze, a soft room ambience, crystal-clear, nothing sharp or forward. A gentle boom-bap kick and brushed hi-hats hold an unhurried 110 BPM; a soft round bass walks beneath. The arrangement breathes in slow tides — hushed verses where warmth builds, a chorus that affirms like watching buds open, a bridge that thins to one voice and held pad, then eases back. Everything sits back in the mix, calm and repeatable, a loop to work beside.
```

### Exclude Styles欄
```
vinyl crackle, tape hiss, static, hum, background noise, cold production, winter atmosphere, pop brightness, overly upbeat progressions, EDM festival bombast, big-room drops, aggressive techno, trap percussion cliches, loud belted vocals, excessive autotune, harsh compression, brittle sibilant highs, plastic synth textures, sterile digital reverb, predictable four-chord loops
```

### 歌詞欄（かな。外来語のみカタカナ。③検証済み・禁則違反なし）
```
[Intro]

[Verse1]
はるの
かぜが
ふくように
なった
きのう
きょう
あさって
どんどん
あたたかく
なってく
うわぎを
ぬいで
みたら
かんじる
ひかりの
ちゅういが
あたたかい

[PreChorus]
すべてが
かわっていく
でも

[Chorus]
キミとの
やくそくだけは
かわらない
きせつが
いくつ
すぎても
これは
ずっと

[Verse2]
くうきが
かわる
ころ
こころも
かわるのかな
でも
キミをみると
あの
さくらが
さいてた
ひに
もどる

[Chorus]
キミとの
やくそくだけは
かわらない
はるになっても
なつになっても
これは
ずっと

[Bridge]
かぜが
かわった
でも
ここが
あたたい

[Chorus]
キミとの
やくそくだけは
かわらない
ずっと
ずっと

[Outro]
はるのかぜ
でも
あたたかい
```

---

## ステップ完了
- ①テーマ分析: 完了（テーマ・主張・情景確定）
- ②歌詞執筆: 完了
- ③歌詞検証: 完了（禁則違反なし）
- ④～⑩（Suno生成〜マスタリング）: 生成前

## ⑪-a ジャケット（`branding.md` テンプレ準拠）
シーン: 初春の夜、少し開いた窓と椅子に掛けた上着、桜の枝。
```
soft hand-drawn illustration, anime-adjacent, warm muted palette, a window left slightly open on an early spring night, a curtain lifting in the breeze, a coat draped over a chair, a single cherry blossom sprig in a glass on the desk, no person, a glowing warm light as the single light source off-center, deep indigo-navy shadows with warm amber light, gentle linework, grainy textured shading, cozy and quiet, no visible face, generous empty space, square, no text
```
ネガティブ: `text, watermark, signature, harsh outlines, bright daylight, oversaturated, chibi, busy background, faces`
生成後にサイン合成: `python scripts/add_signature.py covers/024-kisetsuno-hajimari_bg.jpg covers/024-kisetsuno-hajimari.jpg`（背景は `_bg.jpg` で保存）。
