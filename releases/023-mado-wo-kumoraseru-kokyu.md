# Release 023 — 窓を曇らせる呼吸

| 項目 | 値 |
|---|---|
| 配信タイトル | （タイトル未定・歌詞確定後に決定） |
| slug | mado-wo-kumoraseru-kokyu |
| テーマ | 外の寒さと内側の温かさが隣同士、世界が分かれている |
| 主張（論法） | 「冬の寒さ」という現実→「ここだけ温かい」という例外（演繹法） |
| 情景 | 冬の早朝、寒い窓、二人で息を吹きかける |
| Style | 案B（クール・ミニマル） |
| ステータス | 歌詞検証済み（③禁則違反なし）。Style/Exclude確定後、Suno生成へ |

## Suno 入力

### Style欄
```
A winter window frame — lo-fi, minimal, crystalline. A young Japanese female voice, breathy and close, whispers as if fogging glass, intimate and private, recorded with pristine clarity. Beneath, soft synth pads hover like breath on cold air, a single muted key phrase repeating gently. No percussion at first — just voice and pad — then a distant, almost inaudible boom-bap kick and brushed hi-hats enter at 95 BPM, so soft they feel like wind. A soft round bass walks beneath, barely present. The arrangement is spacious, minimal, breathing room between each phrase. Everything is clean, crystalline, cold but not harsh — a study in contrast: outside is frozen silence, inside is warm and private. The arrangement breathes in slow tides — hushed verses, a chorus that lifts only a little, a bridge that thins to near silence, then eases back. Repeatable, a loop to study beside.
```

### Exclude Styles欄
```
vinyl crackle, tape hiss, static, hum, background noise, warm ambience, cozy production, lo-fi fuzz, pop brightness, overly upbeat progressions, EDM festival bombast, big-room drops, aggressive techno, trap percussion cliches, loud belted vocals, excessive autotune, harsh compression, brittle sibilant highs, plastic synth textures, sterile digital reverb, predictable four-chord loops
```

### 歌詞欄（かな。外来語のみカタカナ。③検証済み・禁則違反なし）
```
[Intro]

[Verse1]
ふゆの
そとは
こおってる
ガラスもひんやり
さわると
ちぢむ
キミの
いきが
まどに
あたる
もくもく
ぼやける

[PreChorus]
そとの
せかいが
かすんで
きえるみたい

[Chorus]
ここだけ
あたたかい
まどをくもらせて
ゆびで
なんか
かいて
ふたりの
へや

[Verse2]
そとは
だれもいなくて
りんごもかたくて
きしきしいってる
でも
ここは
あなたと
あたたかくて
やさしくて
だから

[Chorus]
ここだけ
あたたかい
まどをくもらせて
ふたりで
つくった
きせき
の
へや

[Bridge]
ガラスの
こっちと
あっち
あきらかに
ちがう

[Chorus]
ここだけ
あたたかい
ずっと
ここにいようよ

[Outro]
まどの
むこうは
さむい
```

---

## ステップ完了
- ①テーマ分析: 完了（テーマ・主張・情景確定）
- ②歌詞執筆: 完了
- ③歌詞検証: 完了（禁則違反なし）
- ④～⑩（Suno生成〜マスタリング）: 生成前

## ⑪-a ジャケット（`branding.md` テンプレ準拠）
シーン: 冬の早朝、曇った窓に指で描いた線。マグ2つ。
```
soft hand-drawn illustration, anime-adjacent, warm muted palette, a fogged-up window at winter dawn seen close up, a small line drawn by a fingertip in the condensation, two mugs on the sill, deep blue-grey outside, no person, a glowing warm light as the single light source off-center, deep indigo-navy shadows with warm amber light, gentle linework, grainy textured shading, cozy and quiet, no visible face, generous empty space, square, no text
```
ネガティブ: `text, watermark, signature, harsh outlines, bright daylight, oversaturated, chibi, busy background, faces`
生成後にサイン合成: `python scripts/add_signature.py covers/023-mado-wo-kumoraseru-kokyu_bg.jpg covers/023-mado-wo-kumoraseru-kokyu.jpg`（背景は `_bg.jpg` で保存）。
