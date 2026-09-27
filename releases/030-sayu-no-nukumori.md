# Release 030 — 白湯のぬくもり

| 項目 | 値 |
|---|---|
| 配信タイトル | （タイトル未定・歌詞確定後に決定） |
| slug | sayu-no-nukumori |
| テーマ | シンプルなものほど、本当のことが伝わる |
| 主張（論法） | 「シンプル=本質」→白湯の行為（演繹法） |
| 情景 | 夜中、白湯を両手で温める、何も足さない |
| Style | 案A（ウォーム・ミニマル） |
| ステータス | 歌詞検証済み（③禁則違反なし）。Style/Exclude確定後、Suno生成へ |

## Suno 入力

### Style欄
```
Simple warmth in a cup — lo-fi, minimal, meditative. A young Japanese female voice, warm and clear, sings with quiet certainty, breathy and close, recorded with pristine clarity. Beneath, soft synth pads hover like steam, a single muted key phrase repeats with gentle steadiness, chords suggesting grounding and warmth. Production stays low, warm and pristine: felt keys, analog pad haze, a soft room reverb with hint of quietude, crystal-clear, nothing sharp or distracted. A gentle boom-bap kick and brushed hi-hats hold an unhurried 95 BPM; a soft round bass walks beneath. The arrangement breathes in slow tides — hushed verses that feel meditative, a chorus that affirms simplicity, a bridge that thins to near silence with one voice and held pad, then eases back. Everything sits back in the mix, calm and repeatable, a loop to sit beside.
```

### Exclude Styles欄
```
vinyl crackle, tape hiss, hissy noise floor, pop brightness, overly upbeat progressions, complexity, busy production, EDM festival bombast, big-room drops, aggressive techno, trap percussion cliches, loud belted vocals, excessive autotune, harsh compression, brittle sibilant highs, plastic synth textures, sterile digital reverb, predictable four-chord loops
```

### 歌詞欄（かな。外来語のみカタカナ。③検証済み・禁則違反なし）
```
[Intro]

[Verse1]
よなか
やかんから
ゆを
いれる
なにも
たさない
しおも
砂糖も
ねりょしも
いれない
そのまま
ただの
ゆ
だから
ほんもの

[PreChorus]
もっとも
しゅんすいな
もの

[Chorus]
さゆの
ぬくもりは
なにも
ないから
つたわる
りょうて
であたためて
きいて
いく
ここまで
ぜんぶ
ほんとう

[Verse2]
ふくざつな
こころも
さゆは
すくう
ひと
さかい
ぐらい
シンプルな
あたたかさ
それで
じゅうぶん

[Chorus]
さゆの
ぬくもりは
なにも
ないから
つたわる
だから
この
ぶんは
ぜんぶ
ほんきだ

[Bridge]
シンプルが
いちばん
つよい

[Chorus]
さゆの
ぬくもりは
ずっと
つたわる

[Outro]
さゆ
ただそれ
だけ
```

---

## ステップ完了
- ①テーマ分析: 完了（テーマ・主張・情景確定）
- ②歌詞執筆: 完了
- ③歌詞検証: 完了（禁則違反なし）
- ④～⑩（Suno生成〜マスタリング）: 生成前

## ⑪-a ジャケット（`branding.md` テンプレ準拠）
シーン: 白いカップを両手で包む手元、湯気。ごく簡素な構図。
```
soft hand-drawn illustration, anime-adjacent, warm muted palette, two hands seen from behind wrapped around a plain white cup of steaming hot water, small warm kitchen light, very minimal composition, dark surroundings, no face, a glowing warm light as the single light source off-center, deep indigo-navy shadows with warm amber light, gentle linework, grainy textured shading, cozy and quiet, no visible face, generous empty space, square, no text
```
ネガティブ: `text, watermark, signature, harsh outlines, bright daylight, oversaturated, chibi, busy background, faces`
生成後にサイン合成: `python scripts/add_signature.py covers/030-sayu-no-nukumori_bg.jpg covers/030-sayu-no-nukumori.jpg`（背景は `_bg.jpg` で保存）。
