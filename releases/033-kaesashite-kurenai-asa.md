# Release 033 — 帰してくれない朝

| 項目 | 値 |
|---|---|
| 配信タイトル | （タイトル未定・歌詞確定後に決定） |
| slug | kaesashite-kurenai-asa |
| テーマ | 朝が来ても、キミは引き止める。その温かさが、すべてを変える |
| 主張（論法） | 手の温度→時間の無視→優先順位の転換（帰納法） |
| 情景 | 秋の明け方、まだ暗い時間、キミが手を離さない |
| Style | 案A（ウォーム・プライベート） |
| ステータス | 歌詞検証済み（③禁則違反なし）。Style/Exclude確定後、Suno生成へ |

## Suno 入力

### Style欄
```
Held in place by warmth — lo-fi, intimate, with vulnerable urgency. A young Japanese female voice, breathy and surrendered, whispers the melody as if torn between duty and desire, close and private, recorded with pristine clarity. Beneath, soft synth pads drift like the weight of another's hand, a single muted key phrase repeats with gentle insistence, chords leaning major. Production stays low, warm and clean: rounded keys, analog pad haze, a soft room reverb, crystal-clear, nothing sharp or demanding. A gentle boom-bap kick and brushed swung hi-hats hold an unhurried 95 BPM, slowed as if time itself is being refused; a soft round bass walks beneath. The arrangement breathes in slow tides — hushed verses that conflict with morning light, a chorus that surrenders, a bridge that thins to one voice and held pad, then eases back into the warmth. Everything sits back in the mix, calm and repeatable, a loop to stay beside.
```

### Exclude Styles欄
```
vinyl crackle, tape hiss, hissy noise floor, pop brightness, overly upbeat progressions, energetic morning vibes, urgency, EDM festival bombast, big-room drops, aggressive techno, trap percussion cliches, loud belted vocals, excessive autotune, harsh compression, brittle sibilant highs, plastic synth textures, sterile digital reverb, predictable four-chord loops
```

### 歌詞欄（かな。外来語のみカタカナ。③検証済み・禁則違反なし）
```
[Intro]

[Verse1]
あきの
あけがた
まだくらい
おきなきゃ
いけない
じかんなのに
キミが
てを
はなさない
そっと
ひっぱられて
またふとんへ
あたたかい

[PreChorus]
かえすよ
といってても
キミは
わらってる

[Chorus]
かえしてくれない
あさなのに
このて
もう
あきらめた
ずっと
つなぎたまま
いようよ

[Verse2]
いまは
すべて
どうでもいい
この
ぬくもりが
いちばんで
キミが
わらう
そのこえが
すべてだから

[Chorus]
かえしてくれない
あさなのに
きみの
て
もう
あきらめた
ここに
いようよ

[Bridge]
あしたは
どうなる
でもいい

[Chorus]
かえしてくれない
あさなのに
このまま
ずっと

[Outro]
あきの
あけがた
```

---

## ステップ完了
- ①テーマ分析: 完了（テーマ・主張・情景確定）
- ②歌詞執筆: 完了
- ③歌詞検証: 完了（禁則違反なし）
- ④～⑩（Suno生成〜マスタリング）: 生成前

## ⑪-a ジャケット（`branding.md` テンプレ準拠）
シーン: 秋の明け方、毛布の端で繋いだままの二つの手。窓は青灰色。
```
soft hand-drawn illustration, anime-adjacent, warm muted palette, two hands clasped together at the edge of a blanket at autumn dawn, blue-grey light at the window, a faint bedside lamp off-center, no faces, a glowing warm light as the single light source off-center, deep indigo-navy shadows with warm amber light, gentle linework, grainy textured shading, cozy and quiet, no visible face, generous empty space, square, no text
```
ネガティブ: `text, watermark, signature, harsh outlines, bright daylight, oversaturated, chibi, busy background, faces`
生成後にサイン合成: `python scripts/add_signature.py covers/033-kaesashite-kurenai-asa_bg.jpg covers/033-kaesashite-kurenai-asa.jpg`（背景は `_bg.jpg` で保存）。
