# Release 017 — Shuuden / 終電

| 項目 | 値 |
|---|---|
| 配信タイトル | Shuuden ／ 日本語ローカライズ: 終電 |
| slug | shuuden |
| テーマ | ひとりの帰り道でも、キミのことを考えるだけで冷たい夜が少し優しくなる |
| 主張（論法） | 大切な人を思うと孤独が和らぐという一般論を、終電の窓の夜景に重ねる（演繹法） |
| 情景 | 終電、窓に流れる夜景、少し眠い帰り道 |
| Style | 案C（シネマティック） |
| ステータス | 歌詞検証済み（③禁則違反なし）。Style/Exclude確定。ジャケット・RouteNote入稿待ち |

## Suno 入力

### Style欄
```
A soft synth motif opens like city lights streaming past a train window, three warm notes settling into the hum of the last train. A lo-fi beat under a wide cinematic haze - felt piano and long-tail reverb pads, chords drifting between major and a wistful seventh. A young Japanese female voice, breathy and close, half-whispers the melody, close and private, recorded with pristine clarity. Underneath, a distant field-recording texture (rail clatter, muffled announcements, room tone) moves quietly beneath the beat. Production stays low, warm and pristine: felt piano, long reverb tails, a soft room ambience, crystal-clear, nothing sharp or forward. A gentle boom-bap kick and brushed hi-hats hold an unhurried 110 BPM; a soft round bass walks beneath. The arrangement breathes in slow tides - hushed verses, a chorus that lifts only a little, a bridge that thins to one voice and a held pad, then eases back. Everything sits back in the mix, calm and repeatable, a loop to work beside.
```

### Exclude Styles欄
```
vinyl crackle, tape hiss, static, hum, background noise, muddy low end, hazy production, low fidelity, pop brightness, overly upbeat progressions, EDM festival bombast, big-room drops, aggressive techno, trap percussion cliches, loud belted vocals, excessive autotune, harsh compression, brittle sibilant highs, plastic synth textures, sterile digital reverb, predictable four-chord loops
```

### 歌詞欄
`work/lyrics_017_shuuden_suno.txt`（かな・③検証済み）
（work/ は Git 管理外なので下にも収録）:
```
[Intro]

[Verse1]
おわりのでんしゃにゆられて
まどのそとよるがながれる
つかれたかおがうつってる
すこしねむたいこのじかん
キミのことをかんがえたら
さむさがすこしやわらいだ
ひとりのかえりみちだけど
さみしくないふしぎなよる

[PreChorus]
でんしゃのおとにまぎれても
キミのこえがきこえてくる
ひとりもわるくないかも
そうおもえるのはキミゆえ

[Chorus]
よるのまどがながれていく
キミをおもえばあたたかい
おわりのでんしゃゆれながら
ひとりじゃないときづくんだ
さむいよるもキミのことを
おもうだけでやさしくなる

[Verse2]
えきのあかりがとおざかる
つぎはとうちゃくのおしらせ
かばんのなかのすまほみる
キミからのれんらくひとつ
それだけでこころがゆるむ
つかれもすこしやわらいだ
おわりのでんしゃはもうすぐ
キミのまつばしょへつづく

[Chorus]
よるのまどがながれていく
キミをおもえばあたたかい
おわりのでんしゃゆれながら
ひとりじゃないときづくんだ
さむいよるもキミのことを
おもうだけでやさしくなる

[Bridge]
まどにうつるじぶんのかお
すこしわらってるみたいだ
ひとりのじかんもきっと
キミとつながっているから

[Chorus]
おわりのでんしゃおりたなら
キミにあえるあのばしょへ
つめたいよるをこえてきた
それもぜんぶわるくないよ
よるがあけてしまっても
キミとならそれでいいんだ

[Outro]
でんしゃがとまる
キミがまってる
ただいま
```


## ⑤〜⑩
`python scripts/run_audio.py --input input/shuuden_stems --name "終電" --instrumental`

## ⑪-a ジャケット
シーン: 終電の窓際に座り、外を流れる夜景を眺める後ろ姿。車内の灯りだけが光源。
```
Soft painterly illustration, hand-painted book cover style, thick soft brushstrokes with visible canvas grain texture, muted desaturated warm brown-amber color palette. Extremely dark, moody, low-key lighting. A young woman with dark hair in a loose messy bun, seen from a three-quarter angle from behind, sitting by a train window at night, city lights blurring past outside, the train car's dim overhead light the only source. Soft dark silhouette, face deep in shadow, no visible features, solid opaque clothing with no transparency. Square format, figure off-center, generous dark negative space. No text.
```
右下に `Tonarine` サイン。`covers/017-shuuden.jpg`。

## ⑪-b RouteNote
`_routenote_template.md` どおり。Title `Shuuden` / `Shuuden (Instrumental)` / 日本語 `終電`。
Audio: `output/終電.flac` / `output/終電 (Instrumental).flac`。
