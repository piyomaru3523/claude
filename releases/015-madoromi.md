# Release 015 — Madoromi / まどろみ

| 項目 | 値 |
|---|---|
| 配信タイトル | Madoromi ／ 日本語ローカライズ: まどろみ |
| slug | madoromi |
| テーマ | 起きなきゃいけないとわかっていても、あと少しだけこの時間にいたい |
| 主張（論法） | あたたかい布団・キミの寝息・まだ暗い窓という具体を積み重ねる（帰納法） |
| 情景 | 早朝、目覚まし前のまどろみ、まだ薄暗い寝室 |
| Style | 案A（ジャズ寄り） |
| ステータス | 歌詞検証済み（③禁則違反なし）。Style/Exclude確定。ジャケット・RouteNote入稿待ち |

## Suno 入力

### Style欄
```
A muted electric-piano phrase drifts in like the first light through a curtain, three jazzy chords that lean and resolve like a slow, sleepy breath. Mellow lo-fi meets late-night jazz - the hush of a study playlist carrying the warmth of a small combo, chords full of sevenths and ninths, never bright, always a little wistful. A young Japanese female voice, breathy and close, half-sings the melody, close and private, recorded with pristine clarity. Brushed drums swing softly under an unhurried 104 BPM; an upright-style bass walks in slow steps; a muted electric-piano line answers the voice in the gaps. Production stays low, warm and pristine: felt-damped keys, a soft room reverb, crystal-clear, nothing sharp or forward. The arrangement breathes in slow tides - hushed verses, a chorus that lifts only a little, a bridge that thins to voice and one held chord, then eases back. Everything sits back in the mix, calm and repeatable, a loop to work beside.
```

### Exclude Styles欄
```
vinyl crackle, tape hiss, static, hum, background noise, muddy low end, hazy production, low fidelity, pop brightness, overly upbeat progressions, EDM festival bombast, big-room drops, aggressive techno, trap percussion cliches, loud belted vocals, excessive autotune, harsh compression, brittle sibilant highs, plastic synth textures, sterile digital reverb, predictable four-chord loops
```

### 歌詞欄
`work/lyrics_015_madoromi_suno.txt`（かな・③検証済み）
（work/ は Git 管理外なので下にも収録）:
```
[Intro]

[Verse1]
めざましがまだなってない
まどのそとはまだくらい
ふとんのなかあたたかくて
うごきたくないこのじかん
となりでねいきがきこえる
すこしだけゆっくりしよう
めをとじたままてをのばす
キミのぬくもりたしかめる

[PreChorus]
おきなきゃいけないけど
まだこのままでいたいんだ
まぶたのうらのあたたかさ
もうすこしだけこのままで

[Chorus]
おきなくていいこのままで
キミのねいきがきこえてる
まだくらいあさがくるまで
じかんはゆっくりでいいよ
このぬくもりをはなさない
もうすこしだけまどろもう

[Verse2]
まくらのしわがきになる
うごくのがもったいなくて
とけいのおとがちかくなる
それでもまだうごけないよ
キミのてがふれるかんしょく
それだけでじゅうぶんだった
そとのひかりがすこしずつ
へやをやさしくそめていく

[Chorus]
おきなくていいこのままで
キミのねいきがきこえてる
まだくらいあさがくるまで
じかんはゆっくりでいいよ
このぬくもりをはなさない
もうすこしだけまどろもう

[Bridge]
めざましがなったなら
しずかにめをあけようか
それでもいまはこのままで
キミのそばでゆめのつづき

[Chorus]
めざましがなってしまった
キミがいればそれでいい
おきてもぬくもりはのこる
またあしたもここでねよう
まどろみのじかんはおわる
またこんやもここでねよう

[Outro]
めをあける
キミがわらってる
おはよう
```


## ⑤〜⑩
`python scripts/run_audio.py --input input/madoromi_stems --name "まどろみ" --instrumental`

## ⑪-a ジャケット
シーン: 早朝、まだ薄暗い寝室でベッドに横たわり、隣で眠るキミの気配を感じながらまどろむ後ろ姿。窓のカーテンの隙間からわずかな朝の光。
```
Soft painterly illustration, hand-painted book cover style, thick soft brushstrokes with visible canvas grain texture, muted desaturated warm brown-amber color palette. Extremely dark, moody, low-key lighting. A young woman with dark hair loose over the pillow, seen from a three-quarter angle from behind, lying in bed under a blanket, one hand resting near the pillow, the faint gray light of dawn barely visible through a gap in the curtains, the room still mostly dark. Soft dark silhouette, face deep in shadow, no visible features, solid opaque clothing with no transparency. Square format, figure off-center, generous dark negative space. No text.
```
右下に `Tonarine` サイン。`covers/015-madoromi.jpg`。

## ⑪-b RouteNote
`_routenote_template.md` どおり。Title `Madoromi` / `Madoromi (Instrumental)` / 日本語 `まどろみ`。
Audio: `output/まどろみ.flac` / `output/まどろみ (Instrumental).flac`。
