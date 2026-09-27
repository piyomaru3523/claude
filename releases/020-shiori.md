# Release 020 — Shiori / 栞

| 項目 | 値 |
|---|---|
| 配信タイトル | Shiori ／ 日本語ローカライズ: 栞 |
| slug | shiori |
| テーマ | 途中でやめることは終わりじゃない、続きがあるから栞を挟む |
| 主張（論法） | 栞の位置・閉じた本の重み・また明日読む約束という具体を積み重ねる（帰納法） |
| 情景 | 読みかけの本を閉じて栞を挟む夜 |
| Style | 案C（シネマティック） |
| ステータス | 歌詞検証済み（③禁則違反なし）。Style/Exclude確定。ジャケット・RouteNote入稿待ち |

## Suno 入力

### Style欄
```
A soft synth motif opens like a book closing softly at the page's edge, three warm notes settling into private quiet. A lo-fi beat under a wide cinematic haze - felt piano and long-tail reverb pads, chords drifting between major and a wistful seventh. A young Japanese female voice, breathy and close, half-whispers the melody, close and private, recorded with pristine clarity. Underneath, a distant field-recording texture (a page turning, room tone) moves quietly beneath the beat. Production stays low, warm and pristine: felt piano, long reverb tails, a soft room ambience, crystal-clear, nothing sharp or forward. A gentle boom-bap kick and brushed hi-hats hold an unhurried 110 BPM; a soft round bass walks beneath. The arrangement breathes in slow tides - hushed verses, a chorus that lifts only a little, a bridge that thins to one voice and a held pad, then eases back. Everything sits back in the mix, calm and repeatable, a loop to work beside.
```

### Exclude Styles欄
```
vinyl crackle, tape hiss, static, hum, background noise, muddy low end, hazy production, low fidelity, pop brightness, overly upbeat progressions, EDM festival bombast, big-room drops, aggressive techno, trap percussion cliches, loud belted vocals, excessive autotune, harsh compression, brittle sibilant highs, plastic synth textures, sterile digital reverb, predictable four-chord loops
```

### 歌詞欄
`work/lyrics_020_shiori_suno.txt`（かな・③検証済み）
（work/ は Git 管理外なので下にも収録）:
```
[Intro]

[Verse1]
よみかけのほんをとじる
しおりをそっとはさみこむ
つづきはまたあしたにね
でんきをけしてめをとじる
キミもとなりでねむってる
ほんのおもみがてにのこる
なんでもないこのじかんが
なぜかとくべつにかんじる

[PreChorus]
とちゅうでやめることだって
おわりじゃないよわかってる
しおりがあるかぎりきっと
つづきはちゃんとまっている

[Chorus]
しおりをはさむそのしぐさ
あしたへのやくそくがある
とちゅうでもいいんだそれで
まだつづきがあるから
キミとのじかんもおなじさ
またあしたからはじめよう

[Verse2]
ほんだなにほんをもどして
でんきをけすまえひとこと
キミにおやすみをつぶやく
へんじはねむたそうなこえ
それでもうれしくなるんだ
なんでもないやりとりでも
しおりのいちをおぼえとく
あしたのじぶんのために

[Chorus]
しおりをはさむそのしぐさ
あしたへのやくそくがある
とちゅうでもいいんだそれで
まだつづきがあるから
キミとのじかんもおなじさ
またあしたからはじめよう

[Bridge]
とじたほんのしずけさよ
ちいさなためいきひとつ
つづきをまつじかんも
わるくないとおもえるんだ

[Chorus]
しおりをはさんだページで
あしたのじぶんがまってる
とちゅうでやめてもいいんだ
つづきはちゃんとそこにある
キミとのひびもおなじだね
またつづけていけばいい

[Outro]
ほんをとじる
キミがねむってる
おやすみ
```


## ⑤〜⑩
`python scripts/run_audio.py --input input/shiori_stems --name "栞" --instrumental`

## ⑪-a ジャケット
シーン: ベッドサイドで読みかけの本を閉じて栞を挟む後ろ姿。枕元のランプだけが光源。
```
Soft painterly illustration, hand-painted book cover style, thick soft brushstrokes with visible canvas grain texture, muted desaturated warm brown-amber color palette. Extremely dark, moody, low-key lighting. A young woman with dark hair in a loose messy bun, seen from a three-quarter angle from behind, sitting up in bed closing a book and slipping a bookmark inside, a single small bedside lamp the only light source in the dark room. Soft dark silhouette, face deep in shadow, no visible features, solid opaque clothing with no transparency. Square format, figure off-center, generous dark negative space. No text.
```
右下に `Tonarine` サイン。`covers/020-shiori.jpg`。

## ⑪-b RouteNote
`_routenote_template.md` どおり。Title `Shiori` / `Shiori (Instrumental)` / 日本語 `栞`。
Audio: `output/栞.flac` / `output/栞 (Instrumental).flac`。
