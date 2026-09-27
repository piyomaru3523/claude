# Release 012 — Yoru no Beranda / 夜のベランダ

| 項目 | 値 |
|---|---|
| 配信タイトル | Yoru no Beranda ／ 日本語ローカライズ: 夜のベランダ |
| slug | yoru-no-beranda |
| テーマ | 面倒な家事も、キミと一緒なら特別な時間になる |
| 主張（論法） | 洗濯バサミの音、シーツの匂いなど心地よく感じる具体を積み重ねる（帰納法） |
| 情景 | 夜のベランダ、月明かり、洗濯物 |
| Style | 案B |
| ステータス | RouteNote: Album Details/Artwork/Manage Stores/日本語ローカライズ(アルバムレベル)完了。UPC 5064140646325。配信日2026-10-05。Track(Add Audio)は音楽アップロードを後でまとめて行うため未着手 — その際にTrack1/2のローカライズも要追加 |

## Suno 入力

### Style欄
```
A soft synth motif drifts like laundry stirring in a night breeze, three warm notes that settle and sway. Mellow lo-fi pop meets late-night city-pop calm - a study-playlist steadiness with a pop ballad's quiet ache, chords leaning major but shaded with a wistful seventh. A young Japanese female voice, breathy and close, half-whispers the melody, close and private, recorded with pristine clarity. In the gaps a brief muted electric-piano phrase answers her. Production stays low, warm and pristine: rounded electric piano, clean analog pads, a soft room reverb, crystal-clear, nothing sharp or forward. A gentle boom-bap kick and brushed hi-hats hold an unhurried 118 BPM; a soft round bass walks beneath. The arrangement breathes in slow tides - hushed verses, a chorus that lifts only a little, a bridge that thins to one voice and a held pad, then eases back. Everything sits back in the mix, calm and repeatable, a loop to work beside.
```

### Exclude Styles欄
```
vinyl crackle, tape hiss, static, hum, background noise, muddy low end, hazy production, low fidelity, pop brightness, overly upbeat progressions, EDM festival bombast, big-room drops, aggressive techno, trap percussion cliches, loud belted vocals, excessive autotune, harsh compression, brittle sibilant highs, plastic synth textures, sterile digital reverb, predictable four-chord loops
```

### 歌詞欄
`work/lyrics_012_yorunoberanda_suno.txt`（かな・③検証済み）
（work/ は Git 管理外なので下にも収録）:
```
[Intro]

[Verse1]
せんたくかごをかかえて
べらんだへふたりででる
つきがやけにあかるい
かぜがすこしつめたい
めんどうなはずのかじも
キミといればわるくない
しゃつをいちまいほしたら
となりにたおるをかける

[PreChorus]
せんたくばさみのおとが
りずむをきざんでいく
ひとりならめんどうでも
ふたりならここちいい

[Chorus]
めんどうなかじのはずが
キミといればとくべつに
つきのしたふたりならんで
せんたくものがゆれる
とくにはなさなくても
それだけでいいじかん

[Verse2]
あしたははれるといいねと
そんなはなしをしながら
かわいたしーつのにおいは
キミのかみとおなじだ
ひとりでやってたはずの
かじがたのしみにかわる
キミがいるからめんどうも
わるくないとおもえた

[Chorus]
めんどうなかじのはずが
キミといればとくべつに
つきのしたふたりならんで
せんたくものがゆれる
とくにはなさなくても
それだけでいいじかん

[Bridge]
せんたくもののかげで
すこしだけかくれよう
キミのかたにあたまを
そっとあずけよう

[Chorus]
このかじもキミとならすき
とくべつなじかんになる
あしたもおなじじかんに
ここでまってるよ
ほしがまたたくよるだから
キミとならんでいたい

[Outro]
せんたくものがひとつ
つきにてらされる
おやすみ
```


## ⑤〜⑩
`python scripts/run_audio.py --input input/yoru-no-beranda_stems --name "夜のベランダ" --instrumental`

## ⑪-a ジャケット
シーン: 夜のベランダ、後ろ姿の人物が洗濯物を干している。月明かりが唯一の光源、風にゆれる洗濯物。
```
Soft painterly illustration, hand-painted book cover style, thick soft brushstrokes with visible canvas grain texture, muted desaturated cool-blue and warm amber color palette. Extremely dark, moody, low-key lighting. A young woman with dark hair in a loose messy bun, seen from a three-quarter angle from behind, standing on a small night balcony hanging laundry, moonlight the only light source, laundry gently stirring in the breeze. Soft dark silhouette, face deep in shadow, no visible features, solid opaque clothing with no transparency. Square format, figure off-center, generous dark negative space. No text.
```
右下に `Tonarine` サイン。`covers/012-yoru-no-beranda.jpg`。

## ⑪-b RouteNote
`_routenote_template.md` どおり。Title `Yoru no Beranda` / `Yoru no Beranda (Instrumental)` / 日本語 `夜のベランダ`。
Audio: `output/夜のベランダ.flac` / `output/夜のベランダ (Instrumental).flac`。
