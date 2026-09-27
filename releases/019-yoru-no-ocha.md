# Release 019 — Yoru no Ocha / 夜のお茶

| 項目 | 値 |
|---|---|
| 配信タイトル | Yoru no Ocha ／ 日本語ローカライズ: 夜のお茶 |
| slug | yoru-no-ocha |
| テーマ | 冷めてしまったものも、もう一度あたためればまだ間に合う |
| 主張（論法） | 少し手をかければやり直せるという一般論を、冷めたお茶を温め直す様子に重ねる（演繹法） |
| 情景 | 冷めてしまったお茶を温め直す静かな夜 |
| Style | 案A（ジャズ寄り） |
| ステータス | 歌詞検証済み（③禁則違反なし）。Style/Exclude確定。ジャケット・RouteNote入稿待ち |

## Suno 入力

### Style欄
```
A muted electric-piano phrase rises like steam from a reheated cup, three jazzy chords that lean and resolve like a slow exhale. Mellow lo-fi meets late-night jazz - the hush of a study playlist carrying the warmth of a small combo, chords full of sevenths and ninths, never bright, always a little wistful. A young Japanese female voice, breathy and close, half-sings the melody, close and private, recorded with pristine clarity. Brushed drums swing softly under an unhurried 104 BPM; an upright-style bass walks in slow steps; a muted electric-piano line answers the voice in the gaps. Production stays low, warm and pristine: felt-damped keys, a soft room reverb, crystal-clear, nothing sharp or forward. The arrangement breathes in slow tides - hushed verses, a chorus that lifts only a little, a bridge that thins to voice and one held chord, then eases back. Everything sits back in the mix, calm and repeatable, a loop to work beside.
```

### Exclude Styles欄
```
vinyl crackle, tape hiss, static, hum, background noise, muddy low end, hazy production, low fidelity, pop brightness, overly upbeat progressions, EDM festival bombast, big-room drops, aggressive techno, trap percussion cliches, loud belted vocals, excessive autotune, harsh compression, brittle sibilant highs, plastic synth textures, sterile digital reverb, predictable four-chord loops
```

### 歌詞欄
`work/lyrics_019_yoru-no-ocha_suno.txt`（かな・③検証済み）
（work/ は Git 管理外なので下にも収録）:
```
[Intro]

[Verse1]
さめてしまったおちゃをみて
もういちどあたためよう
やかんのおとがしずかだ
よるのきっちんひとりで
キミはもうねむってるころ
おとをたてないようにする
なんでもないこのさぎょうが
なぜかここちよくかんじる

[PreChorus]
さめたものでももういちど
あたためればまにあうかな
そんなふうにおもうよるは
すこしだけやさしくなれる

[Chorus]
さめたおちゃをあたためて
それだけのことなのに
こころもすこしあたたまる
やりなおせることがある
そうおもえるだけでいい
しずかなきっちんのじかん

[Verse2]
ゆげがゆっくりたちのぼる
まどのそとはまだくらい
キミのねいきがきこえる
それをききながらのむ
きょうのことをふりかえって
わるくないひだとおもう
さめたきもちもあたためて
またあしたにつながってく

[Chorus]
さめたおちゃをあたためて
それだけのことなのに
こころもすこしあたたまる
やりなおせることがある
そうおもえるだけでいい
しずかなきっちんのじかん

[Bridge]
やかんのおとがとまるころ
キミのねがえりがきこえた
こんなしずかなじかんにも
キミがいるのがうれしいよ

[Chorus]
さめたおちゃもあたためれば
それをおしえてくれたんだ
うまくいかないひもきっと
やりなおせるよキミとなら
よるのきっちんひとりでも
キミのきはいがそばにある

[Outro]
おちゃをのむ
キミがねむってる
おやすみ
```


## ⑤〜⑩
`python scripts/run_audio.py --input input/yoru-no-ocha_stems --name "夜のお茶" --instrumental`

## ⑪-a ジャケット
シーン: 夜のキッチンでコンロの前に立ち、やかんを見つめる後ろ姿。コンロの小さな灯りだけが光源。
```
Soft painterly illustration, hand-painted book cover style, thick soft brushstrokes with visible canvas grain texture, muted desaturated warm brown-amber color palette. Extremely dark, moody, low-key lighting. A young woman with dark hair in a loose messy bun, seen from a three-quarter angle from behind, standing at a stove watching a kettle, the small blue stove flame the only light source in the dark kitchen. Soft dark silhouette, face deep in shadow, no visible features, solid opaque clothing with no transparency. Square format, figure off-center, generous dark negative space. No text.
```
右下に `Tonarine` サイン。`covers/019-yoru-no-ocha.jpg`。

## ⑪-b RouteNote
`_routenote_template.md` どおり。Title `Yoru no Ocha` / `Yoru no Ocha (Instrumental)` / 日本語 `夜のお茶`。
Audio: `output/夜のお茶.flac` / `output/夜のお茶 (Instrumental).flac`。
