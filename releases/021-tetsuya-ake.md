# Release 021 — Tetsuya Ake / 徹夜明け

| 項目 | 値 |
|---|---|
| 配信タイトル | Tetsuya Ake ／ 日本語ローカライズ: 徹夜明け |
| slug | tetsuya-ake |
| テーマ | 眠れなかった夜も、キミと迎える朝ならそれでよかったと思える |
| 主張（論法） | 差し込む朝日・疲れた目・キミの笑い声という具体を積み重ねる（帰納法） |
| 情景 | 夜通し起きていた朝、カーテンの隙間から朝日が差し込む |
| Style | 案B（メロウlo-fi） |
| ステータス | 歌詞検証済み（③禁則違反なし）。Style/Exclude確定。ジャケット・RouteNote入稿待ち |

## Suno 入力

### Style欄
```
A soft synth motif opens like morning light slipping through a gap in the curtains, three warm notes waking slowly after a sleepless night. Mellow lo-fi pop meets late-night city-pop calm - a study-playlist steadiness with a pop ballad's quiet ache, chords leaning major but shaded with a wistful seventh. A young Japanese female voice, breathy and close, half-whispers the melody, close and private, recorded with pristine clarity. In the gaps a brief muted electric-piano phrase answers her. Production stays low, warm and pristine: rounded electric piano, clean analog pads, a soft room reverb, crystal-clear, nothing sharp or forward. A gentle boom-bap kick and brushed hi-hats hold an unhurried 118 BPM; a soft round bass walks beneath. The arrangement breathes in slow tides - hushed verses, a chorus that lifts only a little, a bridge that thins to one voice and a held pad, then eases back. Everything sits back in the mix, calm and repeatable, a loop to work beside.
```

### Exclude Styles欄
```
vinyl crackle, tape hiss, static, hum, background noise, muddy low end, hazy production, low fidelity, pop brightness, overly upbeat progressions, EDM festival bombast, big-room drops, aggressive techno, trap percussion cliches, loud belted vocals, excessive autotune, harsh compression, brittle sibilant highs, plastic synth textures, sterile digital reverb, predictable four-chord loops
```

### 歌詞欄
`work/lyrics_021_tetsuya-ake_suno.txt`（かな・③検証済み）
（work/ は Git 管理外なので下にも収録）:
```
[Intro]

[Verse1]
いちやづけがおわったころ
まどのそとがしろんでくる
つかれためをこすりながら
かーてんのすきまみつめる
キミがコーヒーくれるんだ
ふたりでのむあさのじかん
ねむれなかったよるだけど
わるくはなかったとおもう

[PreChorus]
ねむくたってしあわせだ
あさひがへやをそめていく
これがきっとごほうびだ
キミのえがおがそこにある

[Chorus]
ねむれなかったよるだけど
キミとむかえるあさがいい
かーてんのすきまのひが
つかれたこころをてらすよ
ねむらなかったよるもいい
キミがそばにいたから

[Verse2]
コーヒーのゆげがゆれる
キミのあくびがうつってく
もうすぐねむれるはずだよ
そのまえにあさをみよう
がんばったねとキミがいう
そのひとことでむくわれる
ねむいめにうつるあさひ
いつもよりまぶしくみえる

[Chorus]
ねむれなかったよるだけど
キミとむかえるあさがいい
かーてんのすきまのひが
つかれたこころをてらすよ
ねむらなかったよるもいい
キミがそばにいたから

[Bridge]
てつやのあさはとくべつだ
いつもとちがうあさのいろ
つかれてるのにわらってる
キミがそばにいてくれる

[Chorus]
ねむれなかったよるのあと
キミとならそれでいいんだ
かーてんごしのあさひが
ふたりのあさをてらしだす
そのよるがあったから
このあさがもっとまぶしい

[Outro]
めをとじる
キミのとなりで
おやすみ
```


## ⑤〜⑩
`python scripts/run_audio.py --input input/tetsuya-ake_stems --name "徹夜明け" --instrumental`

## ⑪-a ジャケット
シーン: 徹夜明けの朝、机に向かったまま、カーテンの隙間から差し込む朝日を浴びる後ろ姿。
```
Soft painterly illustration, hand-painted book cover style, thick soft brushstrokes with visible canvas grain texture, muted desaturated warm brown-amber color palette. Extremely dark, moody, low-key lighting. A young woman with dark hair in a loose messy bun, seen from a three-quarter angle from behind, slumped tiredly at a desk, a thin beam of early morning sunlight cutting through a gap in the curtains across the dim room. Soft dark silhouette, face deep in shadow, no visible features, solid opaque clothing with no transparency. Square format, figure off-center, generous dark negative space. No text.
```
右下に `Tonarine` サイン。`covers/021-tetsuya-ake.jpg`。

## ⑪-b RouteNote
`_routenote_template.md` どおり。Title `Tetsuya Ake` / `Tetsuya Ake (Instrumental)` / 日本語 `徹夜明け`。
Audio: `output/徹夜明け.flac` / `output/徹夜明け (Instrumental).flac`。
