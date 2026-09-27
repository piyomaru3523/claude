# Release 029 — 眼鏡を外した世界

| 項目 | 値 |
|---|---|
| 配信タイトル | （タイトル未定・歌詞確定後に決定） |
| slug | megane-wo-hazushita-sekai |
| テーマ | 完璧に見える必要はない。曖昧さが優しさになることもある |
| 主張（論法） | 完璧さの価値観を相対化→曖昧さの美（演繹法） |
| 情景 | 夜、眼鏡を取ったぼんやりした視界、キミが輪郭ぼかし |
| Style | 案B（ソフト・ドリーミー） |
| ステータス | 歌詞検証済み（③禁則違反なし）。Style/Exclude確定後、Suno生成へ |

## Suno 入力

### Style欄
```
A soft-focus world — lo-fi, gentle, dreamy, with an almost impressionistic quality. A young Japanese female voice, breathy and vulnerable, whispers the melody as if in a dream, close and intimate, recorded with pristine clarity. Beneath, soft synth pads drift like out-of-focus light, a single muted electric-piano phrase repeats gently, chords suggesting comfort rather than clarity. Production stays low, warm and pristine: felt piano, analog pad haze with hint of blur, a soft room reverb, crystal-clear but soft-edged, nothing sharp or defined. A gentle boom-bap kick and brushed swung hi-hats hold an unhurried 100 BPM; a soft round bass walks beneath. The arrangement breathes in slow tides — hushed verses that embrace ambiguity, a chorus that affirms gentleness, a bridge that thins to one voice and held pad, then eases back. Everything sits back in the mix, calm and repeatable, a loop to rest beside.
```

### Exclude Styles欄
```
vinyl crackle, tape hiss, hissy noise floor, sharp focus, clarity obsessed, pop brightness, overly upbeat progressions, EDM festival bombast, big-room drops, aggressive techno, trap percussion cliches, loud belted vocals, excessive autotune, harsh compression, brittle sibilant highs, plastic synth textures, sterile digital reverb, predictable four-chord loops, defined percussion
```

### 歌詞欄（かな。外来語のみカタカナ。③検証済み・禁則違反なし）
```
[Intro]

[Verse1]
めがねを
はずすと
せかいが
ぼやける
キミも
りんかくで
かたちが
あいまい
だけど
そのほうが
やさしい

[PreChorus]
ぜんぶ
はっきり
みなくたって
いい

[Chorus]
めがねを
はずすと
キミが
ぼやけて
だから
やさしくて
かんぺきじゃなくていい
ここは
そういう
ばしょだ

[Verse2]
かんぺきに
みえるから
たいくつだ
むしろ
りんかく
のこった
ほうが
あたたかい
だから
いま
このまま

[Chorus]
めがねを
はずすと
キミが
ぼやけて
だから
ずっと
このままでいい
かんぺきじゃなくていい

[Bridge]
りんかく
すこし
ぼやけた
ほうが
すき

[Chorus]
めがねを
はずすと
キミが
ぼやけて
だから
これからも
このまま

[Outro]
ぼやけた
まま
やさしい
```

---

## ステップ完了
- ①テーマ分析: 完了（テーマ・主張・情景確定）
- ②歌詞執筆: 完了
- ③歌詞検証: 完了（禁則違反なし）
- ④～⑩（Suno生成〜マスタリング）: 生成前

## ⑪-a ジャケット（`branding.md` テンプレ準拠）
シーン: ベッドサイドに置いた眼鏡、背景は柔らかくボケた部屋。
```
soft hand-drawn illustration, anime-adjacent, warm muted palette, a pair of round glasses resting on a bedside table beside a lamp, the background room deliberately out of focus and softly blurred, painterly shallow depth of field, no person, a glowing warm light as the single light source off-center, deep indigo-navy shadows with warm amber light, gentle linework, grainy textured shading, cozy and quiet, no visible face, generous empty space, square, no text
```
ネガティブ: `text, watermark, signature, harsh outlines, bright daylight, oversaturated, chibi, busy background, faces`
生成後にサイン合成: `python scripts/add_signature.py covers/029-megane-wo-hazushita-sekai_bg.jpg covers/029-megane-wo-hazushita-sekai.jpg`（背景は `_bg.jpg` で保存）。
