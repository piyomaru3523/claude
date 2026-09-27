# Release 008 — Zankyou / 残響

| 項目 | 値 |
|---|---|
| 配信タイトル | Zankyou ／ 日本語ローカライズ: 残響 |
| slug | zankyou |
| テーマ | 電話が切れても、声の温もりはすぐには消えない |
| 主張（論法） | 声のトーン・間合い・話した内容という具体的な記憶が積み重なって残るから（帰納法） |
| 情景 | 夜、電話を切った直後の自室〜そのまま眠りにつくまで |
| Style | 案B |
| ステータス | RouteNote入稿完了（審査待ち）。配信日 **2026-10-05(月)**（10/2・10/3は入稿から最短14日規定により選択不可のため） |

`lyrics_methodology.md` の工程（テーマ→主張→論法→5W1H→想起ワード）を適用した1曲目。

## Suno 入力

### Style欄
```
A soft synth motif fades like a phone screen going dark, three warm notes that linger after the call ends. Mellow lo-fi pop meets late-night city-pop calm - a study-playlist steadiness with a pop ballad's quiet ache, chords leaning major but shaded with a wistful seventh. A young Japanese female voice, breathy and close, half-whispers the melody, close and private, recorded with pristine clarity. In the gaps a brief muted electric-piano phrase answers her. Production stays low, warm and pristine: rounded electric piano, clean analog pads, a soft room reverb, crystal-clear, nothing sharp or forward. A gentle boom-bap kick and brushed hi-hats hold an unhurried 118 BPM; a soft round bass walks beneath. The arrangement breathes in slow tides - hushed verses, a chorus that lifts only a little, a bridge that thins to one voice and a held pad, then eases back. Everything sits back in the mix, calm and repeatable, a loop to work beside.
```

### Exclude Styles欄
```
vinyl crackle, tape hiss, static, hum, background noise, muddy low end, hazy production, low fidelity, pop brightness, overly upbeat progressions, EDM festival bombast, big-room drops, aggressive techno, trap percussion cliches, loud belted vocals, excessive autotune, harsh compression, brittle sibilant highs, plastic synth textures, sterile digital reverb, predictable four-chord loops
```

### 歌詞欄
`work/lyrics_008_zankyou_suno.txt`（かな・③検証済み）
（work/ は Git 管理外なので下にも収録）:
```
[Intro]

[Verse1]
でんわをきったおとが
まだみみにのこってる
わらったこえのとーんが
すこしかすれていたね
なにげないあいづちさえ
おぼえていたいとおもう
がめんはもうくらいのに
あたまのなかでつづいてる

[PreChorus]
まだなにかいいたそうで
とちゅうでおわったはなし
それでもじゅうぶんだった
つづきはまたこんど

[Chorus]
みみのおくにこえがある
むねのおくにまだのこる
でんわはもうきれたのに
ぬくもりはきえないまま
こんやだけのきおくでも
ちゃんとそばにかんじてる

[Verse2]
あしたはなすやくそくも
ちゃんとおぼえているよ
わらったひょうしにきれた
そのつづきもしってるよ
こえだけのじかんでも
ちゃんとつみかさなってく
だからこんやもねむれる
あかりをけしてねむろう

[Chorus]
みみのおくにこえがある
むねのおくにまだのこる
でんわはもうきれたのに
ぬくもりはきえないまま
こんやだけのきおくでも
ちゃんとそばにかんじてる

[Bridge]
つもったきおくがぜんぶ
キミのささえになる
でんわのむこうのこえも
ぜんぶおぼえているよ

[Chorus]
こえはいつかうすれても
きおくだけはきえないよ
つみかさねたじかんだけ
ちゃんととなりにいるから
おやすみをいうまでは
まだそばではなしてよ

[Outro]
きおくがひとつのこる
キミがそっとねむる
おやすみ
```


## ⑤〜⑩
`python scripts/run_audio.py --input input/zankyou_stems --name "残響" --instrumental`

## ⑪-a ジャケット
シーン: 後ろ姿の人物がベッドの端に座り、電話を切ったあとスマホの画面がゆっくり暗くなっていく。部屋は暗く、画面の光だけが唯一の光源。
```
Soft painterly illustration, hand-painted book cover style, thick soft brushstrokes with visible canvas grain texture, muted desaturated warm brown-amber color palette. Extremely dark, moody, low-key lighting. A young woman with dark hair in a loose messy bun, seen from a three-quarter angle from behind, sitting on the edge of a bed at night, phone still in her hand, the screen's fading glow the only light in the dark room. Soft dark silhouette, face deep in shadow, no visible features, solid opaque clothing with no transparency. Square format, figure off-center, generous dark negative space. No text.
```
右下に `Tonarine` サイン。`covers/008-zankyou.jpg`。

## ⑪-b RouteNote
`_routenote_template.md` どおり。Title `Zankyou` / `Zankyou (Instrumental)` / 日本語 `残響`。
Audio: `output/残響.flac` / `output/残響 (Instrumental).flac`。
