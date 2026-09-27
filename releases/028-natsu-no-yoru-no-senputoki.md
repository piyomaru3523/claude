# Release 028 — 夏の夜の扇風機

| 項目 | 値 |
|---|---|
| 配信タイトル | （タイトル未定・歌詞確定後に決定） |
| slug | natsu-no-yoru-no-senputoki |
| テーマ | 機械的な音も、キミが隣にいるだけで違う |
| 主張（論法） | 扇風機の音→キミの寝息→一緒の夜（帰納法） |
| 情景 | 夏、寝苦しい夜、扇風機の音、隣を意識する |
| Style | 案A（ウォーム・ナイト） |
| ステータス | 歌詞検証済み（③禁則違反なし）。Style/Exclude確定後、Suno生成へ |

## Suno 入力

### Style欄
```
Summer night machinery transformed — lo-fi, intimate, with rhythmic warmth. A young Japanese female voice, breathy and drowsy, sings as if half-asleep, close and vulnerable, recorded with pristine clarity. Beneath, soft synth pads drift beneath the vocals, a single muted key phrase answers gently, chords leaning major but shaded. Production stays low, warm and clean: rounded keys, analog pad haze, a soft room reverb with hint of fan-noise ambience, crystal-clear, nothing harsh. A gentle boom-bap kick and subtle hi-hats hold an unhurried 105 BPM with the rhythm of breathing; a soft round bass walks beneath. The arrangement breathes in slow tides — hushed verses where you hear the fan, a chorus that affirms presence, a bridge that thins to one voice and held pad, then eases back to just the fan and breathing. Everything sits back in the mix, calm and repeatable, a loop to sleep beside.
```

### Exclude Styles欄
```
vinyl crackle, tape hiss, hissy noise floor, pop brightness, overly upbeat progressions, energetic summer vibes, EDM festival bombast, big-room drops, aggressive techno, trap percussion cliches, loud belted vocals, excessive autotune, harsh compression, brittle sibilant highs, plastic synth textures, sterile digital reverb, predictable four-chord loops
```

### 歌詞欄（かな。外来語のみカタカナ。③検証済み・禁則違反なし）
```
[Intro]

[Verse1]
なつの
よなか
せんぷうきの
おとが
ずっと
うるさい
でも
キミが
となりに
いると
その
おとも
きこえなくなる
わけじゃなくて
ちがう
きこえかたに
なる

[PreChorus]
おなじ
こくをすってる
ふたりで

[Chorus]
せんぷうきの
おとも
キミがいると
りんご
みたい
あたたかい
だから
いっしょに
ねむれなくても
いい

[Verse2]
キミの
ねいき
あたまの
そばで
かすかに
きこえて
ぼくの
こくも
きこえてるのかな
おたがいに
さあ
さあ
いってるなか
でねる

[Chorus]
せんぷうきの
おとも
キミがいると
うたってる
みたい
だから
うるさくない
ずっと
このままでいい

[Bridge]
きかいの
おと
でも
ふたりだと

[Chorus]
せんぷうきの
おとも
きこえなくなる
かわりに
キミが
きこえる

[Outro]
せんぷうきの
おとのなか
```

---

## ステップ完了
- ①テーマ分析: 完了（テーマ・主張・情景確定）
- ②歌詞執筆: 完了
- ③歌詞検証: 完了（禁則違反なし）
- ④～⑩（Suno生成〜マスタリング）: 生成前

## ⑪-a ジャケット（`branding.md` テンプレ準拠）
シーン: 夏の夜の寝室、床の扇風機と揺れるカーテン、小さな常夜灯。
```
soft hand-drawn illustration, anime-adjacent, warm muted palette, a retro electric fan on the floor of a bedroom on a summer night, its blades softly blurred, curtains stirring at an open window, a small night lamp, no person, a glowing warm light as the single light source off-center, deep indigo-navy shadows with warm amber light, gentle linework, grainy textured shading, cozy and quiet, no visible face, generous empty space, square, no text
```
ネガティブ: `text, watermark, signature, harsh outlines, bright daylight, oversaturated, chibi, busy background, faces`
生成後にサイン合成: `python scripts/add_signature.py covers/028-natsu-no-yoru-no-senputoki_bg.jpg covers/028-natsu-no-yoru-no-senputoki.jpg`（背景は `_bg.jpg` で保存）。
