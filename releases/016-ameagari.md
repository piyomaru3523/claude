# Release 016 — Ameagari / 雨あがり

| 項目 | 値 |
|---|---|
| 配信タイトル | Ameagari ／ 日本語ローカライズ: 雨あがり |
| slug | ameagari |
| テーマ | 濡れた傘を片付けるだけの動作にも、キミといる日常のありがたさが宿る |
| 主張（論法） | しずく・湿った匂い・玄関の明かりという具体を積み重ねる（帰納法） |
| 情景 | 雨あがりの夜、傘の雫を拭きながら玄関に入る |
| Style | 案B（メロウlo-fi） |
| ステータス | 歌詞検証済み（③禁則違反なし）。Style/Exclude確定。ジャケット・RouteNote入稿待ち |

## Suno 入力

### Style欄
```
A soft synth motif opens like a door closing softly out of the rain, three warm notes shaking off the last drops. Mellow lo-fi pop meets late-night city-pop calm - a study-playlist steadiness with a pop ballad's quiet ache, chords leaning major but shaded with a wistful seventh. A young Japanese female voice, breathy and close, half-whispers the melody, close and private, recorded with pristine clarity. In the gaps a brief muted electric-piano phrase answers her. Production stays low, warm and pristine: rounded electric piano, clean analog pads, a soft room reverb, crystal-clear, nothing sharp or forward. A gentle boom-bap kick and brushed hi-hats hold an unhurried 118 BPM; a soft round bass walks beneath. The arrangement breathes in slow tides - hushed verses, a chorus that lifts only a little, a bridge that thins to one voice and a held pad, then eases back. Everything sits back in the mix, calm and repeatable, a loop to work beside.
```

### Exclude Styles欄
```
vinyl crackle, tape hiss, static, hum, background noise, muddy low end, hazy production, low fidelity, pop brightness, overly upbeat progressions, EDM festival bombast, big-room drops, aggressive techno, trap percussion cliches, loud belted vocals, excessive autotune, harsh compression, brittle sibilant highs, plastic synth textures, sterile digital reverb, predictable four-chord loops
```

### 歌詞欄
`work/lyrics_016_ameagari_suno.txt`（かな・③検証済み）
（work/ は Git 管理外なので下にも収録）:
```
[Intro]

[Verse1]
あめがやんでかさをたたむ
しずくがゆかにこぼれてく
げんかんさきのつめたさよ
くつをぬぐおとがひびく
キミがタオルをくれたんだ
かみをふいてわらいあう
なんでもないこのじかんが
とてもたいせつにおもえる

[PreChorus]
あめあとのしめったにおい
それすらもすきになってく
キミとふたりのげんかんで
それだけでじゅうぶんなんだ

[Chorus]
なんでもないそのしぐさに
かさをたたむだけのじかん
キミといればとくべつだ
ぬれたかさもわるくないね
あめやんだよるのげんかん
ふたりだけのひととき

[Verse2]
かさのしずくをふきとって
たてかけておくすみっこに
キミのかみもぬれている
それをみてまたわらった
とくにはなさなくてもいい
おなじじかんがすぎるだけ
あしたのてんきわからない
でもこんやはこれでいいや

[Chorus]
なんでもないそのしぐさに
かさをたたむだけのじかん
キミといればとくべつだ
ぬれたかさもわるくないね
あめやんだよるのげんかん
ふたりだけのひととき

[Bridge]
かさをひろげたあのひを
いつかわらってはなそうか
こんやのままでいさせて
そっとおぼえておこうか

[Chorus]
あめがあがったよるのこと
きっとわすれずにいるはず
かさをたたんだあのよるも
キミといたからよかった
なんでもないひがかわる
かわるじゅもんはキミのこえ

[Outro]
かさをしまう
キミがわらってる
おやすみ
```


## ⑤〜⑩
`python scripts/run_audio.py --input input/ameagari_stems --name "雨あがり" --instrumental`

## ⑪-a ジャケット
シーン: 雨あがりの夜、玄関で濡れた傘のしずくを拭う後ろ姿。玄関の小さな灯りだけが光源。
```
Soft painterly illustration, hand-painted book cover style, thick soft brushstrokes with visible canvas grain texture, muted desaturated warm brown-amber color palette. Extremely dark, moody, low-key lighting. A young woman with dark hair in a loose messy bun, seen from a three-quarter angle from behind, crouched at a genkan wiping raindrops from a folded umbrella, a single small entryway light the only source in the dark hall. Soft dark silhouette, face deep in shadow, no visible features, solid opaque clothing with no transparency. Square format, figure off-center, generous dark negative space. No text.
```
右下に `Tonarine` サイン。`covers/016-ameagari.jpg`。

## ⑪-b RouteNote
`_routenote_template.md` どおり。Title `Ameagari` / `Ameagari (Instrumental)` / 日本語 `雨あがり`。
Audio: `output/雨あがり.flac` / `output/雨あがり (Instrumental).flac`。
