# Release 014 — Mimi wo Fusaide / 耳をふさいで

| 項目 | 値 |
|---|---|
| 配信タイトル | Mimi wo Fusaide ／ 日本語ローカライズ: 耳をふさいで |
| slug | mimi-wo-fusaide |
| テーマ | 全部の音を遮断しても、キミの声だけは選んで届く |
| 主張（論法） | 「外の音は消える／でもキミの声はとどく」という対比を積み重ねる（帰納法） |
| 情景 | 一日の終わり、ヘッドホンをつける部屋 |
| Style | 案C（シネマティック） |
| ステータス | RouteNote: Album Details/Artwork/Manage Stores/日本語ローカライズ(アルバムレベル)完了。UPC 5064140115425。配信日2026-10-05。Track(Add Audio)は音楽アップロードを後でまとめて行うため未着手 — その際にTrack1/2のローカライズも要追加 |

## Suno 入力

### Style欄
```
A soft synth motif opens like sound fading behind a pair of headphones, three warm notes settling into private quiet. A lo-fi beat under a wide cinematic haze - felt piano and long-tail reverb pads, chords drifting between major and a wistful seventh. A young Japanese female voice, breathy and close, half-whispers the melody, close and private, recorded with pristine clarity. Underneath, a distant field-recording texture (muffled city noise, room tone) moves quietly beneath the beat. Production stays low, warm and pristine: felt piano, long reverb tails, a soft room ambience, crystal-clear, nothing sharp or forward. A gentle boom-bap kick and brushed hi-hats hold an unhurried 110 BPM; a soft round bass walks beneath. The arrangement breathes in slow tides - hushed verses, a chorus that lifts only a little, a bridge that thins to one voice and a held pad, then eases back. Everything sits back in the mix, calm and repeatable, a loop to work beside.
```

### Exclude Styles欄
```
vinyl crackle, tape hiss, static, hum, background noise, muddy low end, hazy production, low fidelity, pop brightness, overly upbeat progressions, EDM festival bombast, big-room drops, aggressive techno, trap percussion cliches, loud belted vocals, excessive autotune, harsh compression, brittle sibilant highs, plastic synth textures, sterile digital reverb, predictable four-chord loops
```

### 歌詞欄
`work/lyrics_014_mimiwofusaide_suno.txt`（かな・③検証済み）
（work/ は Git 管理外なので下にも収録）:
```
[Intro]

[Verse1]
いやほんをとりだして
かたほうだけつけてみる
せかいのおとがとおくなる
じぶんだけのじかんになる
ちいさならんぷのあかりが
へやをしずかにてらす
うるさいいちにちのあとで
そっとめをとじてみる

[PreChorus]
かたほうだけのおんがくが
もうかたほうはキミのため
そとのおとはきえても
キミのこえだけとどく

[Chorus]
みみをふさいでしまっても
キミのこえだけとどくよ
せかいがうるさいままでも
となりはいつもしずかだ
おんがくのすきまから
キミがそっとのぞくんだ

[Verse2]
こーどのむこうから
キミのこえがとどく
かたほうだけのせかいでも
キミとふたりぶんになる
そうおんはとおざかるのに
ひつようなおとだけのこる
らんぷのあかりもいっしょに
きょうもいちにちおわった

[Chorus]
みみをふさいでしまっても
キミのこえだけとどくよ
せかいがうるさいままでも
となりはいつもしずかだ
おんがくのすきまから
キミがそっとのぞくんだ

[Bridge]
いやほんをはずすころ
キミもねむくなる
もうふにつつまれたまま
そのままふたりでねむろう

[Chorus]
みみをふさいでいても
キミだけはとくべつだ
せかいがうるさいままでも
となりはあたたかいまま
おんがくがおわってからも
キミのこえをきいていたい

[Outro]
いやほんをはずす
キミのねいきがきこえる
おやすみ
```


## ⑤〜⑩
`python scripts/run_audio.py --input input/mimi-wo-fusaide_stems --name "耳をふさいで" --instrumental`

## ⑪-a ジャケット
シーン: 後ろ姿の人物がヘッドホンをつけて世界の音を遮断する瞬間。間接照明ひとつだけの静かな部屋。
```
Soft painterly illustration, hand-painted book cover style, thick soft brushstrokes with visible canvas grain texture, muted desaturated warm brown-amber color palette. Extremely dark, moody, low-key lighting. A young woman with dark hair in a loose messy bun, seen from a three-quarter angle from behind, sitting quietly with headphones just placed over her ears, a single small warm lamp the only light source in the dark room. Soft dark silhouette, face deep in shadow, no visible features, solid opaque clothing with no transparency. Square format, figure off-center, generous dark negative space. No text.
```
右下に `Tonarine` サイン。`covers/014-mimi-wo-fusaide.jpg`。

## ⑪-b RouteNote
`_routenote_template.md` どおり。Title `Mimi wo Fusaide` / `Mimi wo Fusaide (Instrumental)` / 日本語 `耳をふさいで`。
Audio: `output/耳をふさいで.flac` / `output/耳をふさいで (Instrumental).flac`。
