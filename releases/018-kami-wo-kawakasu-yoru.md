# Release 018 — Kami wo Kawakasu Yoru / 髪を乾かす夜

| 項目 | 値 |
|---|---|
| 配信タイトル | Kami wo Kawakasu Yoru ／ 日本語ローカライズ: 髪を乾かす夜 |
| slug | kami-wo-kawakasu-yoru |
| テーマ | 何気ない生活音にも、キミと過ごす夜だとわかる特別さがある |
| 主張（論法） | ドライヤーの音・鏡の湯気・キミの気配という具体的な生活音を積み重ねる（帰納法） |
| 情景 | お風呂上がり、ドライヤーの音だけが響く脱衣所 |
| Style | 案B（メロウlo-fi） |
| ステータス | 歌詞検証済み（③禁則違反なし）。Style/Exclude確定。ジャケット・RouteNote入稿待ち |

## Suno 入力

### Style欄
```
A soft synth motif opens like a hairdryer humming down to silence, three warm notes settling into the quiet after. Mellow lo-fi pop meets late-night city-pop calm - a study-playlist steadiness with a pop ballad's quiet ache, chords leaning major but shaded with a wistful seventh. A young Japanese female voice, breathy and close, half-whispers the melody, close and private, recorded with pristine clarity. In the gaps a brief muted electric-piano phrase answers her. Production stays low, warm and pristine: rounded electric piano, clean analog pads, a soft room reverb, crystal-clear, nothing sharp or forward. A gentle boom-bap kick and brushed hi-hats hold an unhurried 118 BPM; a soft round bass walks beneath. The arrangement breathes in slow tides - hushed verses, a chorus that lifts only a little, a bridge that thins to one voice and a held pad, then eases back. Everything sits back in the mix, calm and repeatable, a loop to work beside.
```

### Exclude Styles欄
```
vinyl crackle, tape hiss, static, hum, background noise, muddy low end, hazy production, low fidelity, pop brightness, overly upbeat progressions, EDM festival bombast, big-room drops, aggressive techno, trap percussion cliches, loud belted vocals, excessive autotune, harsh compression, brittle sibilant highs, plastic synth textures, sterile digital reverb, predictable four-chord loops
```

### 歌詞欄
`work/lyrics_018_kami-wo-kawakasu-yoru_suno.txt`（かな・③検証済み）
（work/ は Git 管理外なので下にも収録）:
```
[Intro]

[Verse1]
おふろあがりのぬれたかみ
どらいやーのおとがひびく
キミもかみをかわかしてる
きょうのことをはなしながら
かがみにうつるキミのかお
すこしつかれたかおしてる
なんでもないこのじかんが
いちにちのおわりをつげる

[PreChorus]
あたたかいかぜがぬけてく
キミのこえもまざっていく
とくべつなことはなくても
これでじゅうぶんしあわせだ

[Chorus]
どらいやーだけがひびく
キミとすごすこのじかんが
なによりもたいせつなんだ
かわいたかみがやわらかい
きょうのつかれもきえていく
キミがいるからねむれそう

[Verse2]
くしをとってかみをとかす
キミのてがそっとふれる
ふたりだけのしずかなよる
かいわはなくてもいいんだ
かわいたかみをたばねてく
あくびをひとつこぼしてた
もうすぐねむるじかんだが
もうすこしここにいたいな

[Chorus]
どらいやーだけがひびく
キミとすごすこのじかんが
なによりもたいせつなんだ
かわいたかみがやわらかい
きょうのつかれもきえていく
キミがいるからねむれそう

[Bridge]
ねつもだんだんきえていく
へやがすこしずつしずまる
おとがきこえなくなっても
キミのぬくもりだけのこる

[Chorus]
どらいやーをとめたあとの
しずけさもきらいじゃないよ
きょうがおわっていくころ
キミがそばにいてよかった
かわいたかみをなでながら
おやすみのじゅんびをしよう

[Outro]
どらいやーがとまる
キミがあくびする
おやすみ
```


## ⑤〜⑩
`python scripts/run_audio.py --input input/kami-wo-kawakasu-yoru_stems --name "髪を乾かす夜" --instrumental`

## ⑪-a ジャケット
シーン: お風呂上がり、脱衣所の鏡の前でドライヤーを持ち髪を乾かす後ろ姿。小さな照明ひとつだけが光源。
```
Soft painterly illustration, hand-painted book cover style, thick soft brushstrokes with visible canvas grain texture, muted desaturated warm brown-amber color palette. Extremely dark, moody, low-key lighting. A young woman with dark damp hair, seen from a three-quarter angle from behind, standing before a mirror holding a hairdryer to her hair, a single small vanity light the only source in the dim room. Soft dark silhouette, face deep in shadow, no visible features, solid opaque clothing with no transparency. Square format, figure off-center, generous dark negative space. No text.
```
右下に `Tonarine` サイン。`covers/018-kami-wo-kawakasu-yoru.jpg`。

## ⑪-b RouteNote
`_routenote_template.md` どおり。Title `Kami wo Kawakasu Yoru` / `Kami wo Kawakasu Yoru (Instrumental)` / 日本語 `髪を乾かす夜`。
Audio: `output/髪を乾かす夜.flac` / `output/髪を乾かす夜 (Instrumental).flac`。
