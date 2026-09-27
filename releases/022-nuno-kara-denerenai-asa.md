# Release 022 — 布団から出られない朝

| 項目 | 値 |
|---|---|
| 配信タイトル | （タイトル未定・歌詞確定後に決定） |
| slug | futon-kara-denerenai-asa |
| テーマ | 一人でも朝は辛いけど、キミがいると布団の中が安心になる |
| 主張（論法） | 布団の温度→寝ぐせ→キミの体温→抽象（帰納法） |
| 情景 | 冬の朝、暗い部屋、布団から出たくない時間 |
| Style | 案A（ウォーム・ロウファイ） |
| ステータス | 歌詞検証済み（③禁則違反なし）。Style/Exclude確定後、Suno生成へ |

## Suno 入力

### Style欄
```
A soft morning haze wrapped in quilted warmth — a mellow lo-fi beat opens like eyes half-closing again, gentle and hesitant. Warm synth pads drift beneath a young Japanese female voice, breathy and drowsy, half-whispers the melody as if not quite awake, close and private. No sharp edges: rounded keys, a soft room reverb, analog pad haze, a quiet noise floor. A gentle boom-bap kick and brushed swung hi-hats hold an unhurried 105 BPM; a soft round bass walks beneath. The arrangement breathes in slow tides — hushed verses where every word feels like a confession whispered under quilts, a chorus that lifts only enough to acknowledge the day outside, a bridge that thins to one voice and held pad, then eases back into warmth. Everything sits back in the mix, calm and repeatable, a loop to drift beside.
```

### Exclude Styles欄
```
vinyl crackle, tape hiss, hissy noise floor, pop brightness, overly upbeat progressions, energetic morning vibes, EDM festival bombast, big-room drops, aggressive techno, trap percussion cliches, loud belted vocals, excessive autotune, harsh compression, brittle sibilant highs, plastic synth textures, sterile digital reverb, predictable four-chord loops, busy crowded arrangement
```

### 歌詞欄（かな。外来語のみカタカナ。③検証済み・禁則違反なし）
```
[Intro]

[Verse1]
あさのアラーム
またなるのかと
ふとんのなかは
あたたかい
まどはまだくらい
ひとりでもこの
じかんはあつい
けどキミがいると
もっとあつい

[PreChorus]
おきなきゃいけない
そうだけどな
あと五ふんでいい
あと五ふんくらい

[Chorus]
ふとんをぬけられない
あさなのに
キミのぬくもり
もう手放したくない
これでいいんだ
そのまま
ここにいようよ

[Verse2]
キミのねぐせ
あたまのはし
ほっぺたあたりが
むずむずしてる
まどのそとでは
ひかりがふえて
でんしゃがなって
ばたばた
でも

[Chorus]
ふとんをぬけられない
あさなのに
キミのぬくもり
もう手放したくない
きょうだって
あしただって
ここがいいんだ

[Bridge]
あたたかいから
あんしんだから
ひとりじゃない
ここにいるよ

[Chorus]
ふとんをぬけられない
あさなのに
キミのぬくもり
もう手放したくない
これからも
ずっと
ここにいようよ

[Outro]
あさの
ふとんの
なかで
```

---

## ステップ完了
- ①テーマ分析: 完了（テーマ・主張・情景確定）
- ②歌詞執筆: 完了
- ③歌詞検証: 完了（禁則違反なし）
- ④～⑩（Suno生成〜マスタリング）: 生成前

## ⑪-a ジャケット（`branding.md` テンプレ準拠）
シーン: 冬の朝、布団の膨らみだけ。カーテンの隙間から青い薄明かり。
```
soft hand-drawn illustration, anime-adjacent, warm muted palette, a lump of a person asleep under a thick quilt on a low bed, early winter dawn, faint blue light through a gap in the curtains, a small mug on the bedside table, a glowing warm light as the single light source off-center, deep indigo-navy shadows with warm amber light, gentle linework, grainy textured shading, cozy and quiet, no visible face, generous empty space, square, no text
```
ネガティブ: `text, watermark, signature, harsh outlines, bright daylight, oversaturated, chibi, busy background, faces`
生成後にサイン合成: `python scripts/add_signature.py covers/022-nuno-kara-denerenai-asa_bg.jpg covers/022-nuno-kara-denerenai-asa.jpg`（背景は `_bg.jpg` で保存）。
