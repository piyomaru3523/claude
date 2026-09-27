# Release 009 — Shimekiri / しめきり

| 項目 | 値 |
|---|---|
| 配信タイトル | Shimekiri ／ 日本語ローカライズ: しめきり |
| slug | shimekiri |
| テーマ | 焦って進めるより、キミのペースの方が結局早い |
| 主張（論法） | 無理に急ぐと集中力が落ちてミスが増えるという一般論を、今夜の作業に当てはめる（演繹法） |
| 情景 | 深夜、資料が積まれた机、締め切り前夜 |
| Style | 案C（シネマティック） |
| ステータス | RouteNote: Album Details/Artwork/Manage Stores/日本語ローカライズ(アルバムレベル)完了。UPC 5064115416649。配信日2026-10-05。Track(Add Audio)は音楽アップロードを後でまとめて行うため未着手 — その際にTrack1/2のローカライズも要追加 |

## Suno 入力

### Style欄
```
A soft synth motif opens like a desk lamp burning late into the night, three warm notes that hold steady under pressure. A lo-fi beat under a wide cinematic haze - felt piano and long-tail reverb pads, chords drifting between major and a wistful seventh. A young Japanese female voice, breathy and close, half-whispers the melody, close and private, recorded with pristine clarity. Underneath, a distant field-recording texture (soft rain, room tone) moves quietly beneath the beat. Production stays low, warm and pristine: felt piano, long reverb tails, a soft room ambience, crystal-clear, nothing sharp or forward. A gentle boom-bap kick and brushed hi-hats hold an unhurried 110 BPM; a soft round bass walks beneath. The arrangement breathes in slow tides - hushed verses, a chorus that lifts only a little, a bridge that thins to one voice and a held pad, then eases back. Everything sits back in the mix, calm and repeatable, a loop to work beside.
```

### Exclude Styles欄
```
vinyl crackle, tape hiss, static, hum, background noise, muddy low end, hazy production, low fidelity, pop brightness, overly upbeat progressions, EDM festival bombast, big-room drops, aggressive techno, trap percussion cliches, loud belted vocals, excessive autotune, harsh compression, brittle sibilant highs, plastic synth textures, sterile digital reverb, predictable four-chord loops
```

### 歌詞欄
`work/lyrics_009_shimekiri_suno.txt`（かな・③検証済み）
（work/ は Git 管理外なので下にも収録）:
```
[Intro]

[Verse1]
いそいでかいたもじが
すこしゆがんでいく
けしごむでけしてまた
おなじところをかく
とけいばかりみてしまう
てがとまってしまう
あせるほどとおくなる
しめきりのもじすう

[PreChorus]
いちどてをとめてみる
しんこきゅうをひとつ
それだけでみえてくる
つぎにすすむみちが

[Chorus]
いそがなくていいんだよ
キミのぺーすがちかみち
ひとつずつでいいんだよ
あせらなくていいんだよ
すこしずつでもすすめば
ちゃんとあさがくるから

[Verse2]
いちぎょうずつよみかえす
あせったときよりきれいだ
いちどたちどまるほうが
けっきょくはやくすすむ
キミのてもとをみていて
そうきづいたよこんや
だからいそがなくていい
それがいちばんのちかみち

[Chorus]
いそがなくていいんだよ
キミのぺーすがちかみち
ひとつずつでいいんだよ
あせらなくていいんだよ
すこしずつでもすすめば
ちゃんとあさがくるから

[Bridge]
ぺんをおいてすこしだけ
かたのちからをぬこう
いそがなくてもいいから
またすこしずつすすもう

[Chorus]
ひとつずつつみあげてきた
そのさきにあさがくる
あせらなくてよかったね
キミのぺーすでよかった
しめきりをこえたそのさき
となりでみていたよ

[Outro]
ぺんをおくおと
キミがいきをつく
おつかれさま
```


## ⑤〜⑩
`python scripts/run_audio.py --input input/shimekiri_stems --name "しめきり" --instrumental`

## ⑪-a ジャケット
シーン: 後ろ姿の人物が資料の積まれた机に向かう。デスクランプ一つ、窓の外は暗い。集中と少しの疲れが同居する夜。
```
Soft painterly illustration, hand-painted book cover style, thick soft brushstrokes with visible canvas grain texture, muted desaturated warm brown-amber color palette. Extremely dark, moody, low-key lighting. A young woman with dark hair in a loose messy bun, seen from a three-quarter angle from behind, sitting at a desk piled with papers and books late at night, a small desk lamp the only warm light source. Soft dark silhouette, face deep in shadow, no visible features, solid opaque clothing with no transparency. Square format, figure off-center, generous dark negative space. No text.
```
右下に `Tonarine` サイン。`covers/009-shimekiri.jpg`。

## ⑪-b RouteNote
`_routenote_template.md` どおり。Title `Shimekiri` / `Shimekiri (Instrumental)` / 日本語 `しめきり`。
Audio: `output/しめきり.flac` / `output/しめきり (Instrumental).flac`。
