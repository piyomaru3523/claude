# Release 010 — Teiden / 停電

| 項目 | 値 |
|---|---|
| 配信タイトル | Teiden ／ 日本語ローカライズ: 停電 |
| slug | teiden |
| テーマ | 不便な夜ほど、普段気づかない小さなことがかけがえなく見える |
| 主張（論法） | 消えたもの（テレビ・スマホの充電）を積み重ねることで、残ったもの（灯り・キミ）の価値が際立つ（帰納法） |
| 情景 | 突然の停電、ろうそく一本の夜 |
| Style | 案A（ジャズ寄り） |
| ステータス | RouteNote: Album Details/Artwork/Manage Stores/日本語ローカライズ(アルバムレベル)完了。UPC 5064115276007。配信日2026-10-05。Track(Add Audio)は音楽アップロードを後でまとめて行うため未着手 — その際にTrack1/2のローカライズも要追加 |

## Suno 入力

### Style欄
```
A muted electric-piano figure flickers like a candle flame in the dark, jazzy sevenths leaning and resolving, very soft. Mellow lo-fi meets late-night jazz - the hush of a study playlist carrying the warmth of a small combo, chords full of sevenths and ninths, never bright, always a little wistful. A young Japanese female voice, breathy and close, half-sings the melody, close and private, recorded with pristine clarity. Brushed drums swing softly under an unhurried 104 BPM; an upright-style bass walks in slow steps; a muted electric-piano line answers the voice in the gaps. Production stays low, warm and pristine: felt-damped keys, a soft room reverb, crystal-clear, nothing sharp or forward. The arrangement breathes in slow tides - hushed verses, a chorus that lifts only a little, a bridge that thins to voice and one held chord, then eases back. Everything sits back in the mix, calm and repeatable, a loop to work beside.
```

### Exclude Styles欄
```
vinyl crackle, tape hiss, static, hum, background noise, muddy low end, hazy production, low fidelity, pop brightness, overly upbeat progressions, EDM festival bombast, big-room drops, aggressive techno, trap percussion cliches, loud belted vocals, excessive autotune, harsh compression, brittle sibilant highs, plastic synth textures, sterile digital reverb, predictable four-chord loops
```

### 歌詞欄
`work/lyrics_010_teiden_suno.txt`（かな・③検証済み）
（work/ は Git 管理外なので下にも収録）:
```
[Intro]

[Verse1]
てれびのおとがきえて
へやがきゅうにしずか
すまほのじゅうでんさえも
もったいなくてけす
いつものおとがきえたら
なにもかもがきわだつ
まっちをすったおとさえ
やけにおおきくきこえる

[PreChorus]
あかりがひとつともる
ろうそくのあわいひかり
キミのかおだけみえる
それだけでじゅうぶん

[Chorus]
きえたものよりのこるもの
そのほうがずっとまぶしい
あかりがきえたよるだから
きづけたちいさなしあわせ
キミがそばにいることが
いちばんのあかりだよ

[Verse2]
ほのおをはさんですわって
とくにはなさなくても
しずかなじかんがながれる
それだけでみたされる
でんきがなくてもへいき
そうおもえたこんやだった
このしずけさもきっと
わるくないとおもえた

[Chorus]
きえたものよりのこるもの
そのほうがずっとまぶしい
あかりがきえたよるだから
きづけたちいさなしあわせ
キミがそばにいることが
いちばんのあかりだよ

[Bridge]
あかりがもどってきても
このじかんはわすれない
ていでんのよるのことを
いつかふたりでわらおう

[Chorus]
あかりがもどるよるでも
あのしずけさをおぼえてる
ほのおのとなりでわらった
キミのかおのこと
とくべつじゃないじかんが
とくべつになったよる

[Outro]
でんきがついた
キミがわらってる
おかえり
```


## ⑤〜⑩
`python scripts/run_audio.py --input input/teiden_stems --name "停電" --instrumental`

## ⑪-a ジャケット
シーン: 停電した部屋、後ろ姿の人物がろうそく一本の炎を見つめている。壁に伸びる影、いつもと違う静けさ。
```
Soft painterly illustration, hand-painted book cover style, thick soft brushstrokes with visible canvas grain texture, muted desaturated warm brown-amber color palette. Extremely dark, moody, low-key lighting. A young woman with dark hair in a loose messy bun, seen from a three-quarter angle from behind, sitting close to a single lit candle in an otherwise powerless, pitch-dark room, the candle flame the only warm light source, a long soft shadow on the wall behind her. Soft dark silhouette, face deep in shadow, no visible features, solid opaque clothing with no transparency. Square format, figure off-center, generous dark negative space. No text.
```
右下に `Tonarine` サイン。`covers/010-teiden.jpg`。

## ⑪-b RouteNote
`_routenote_template.md` どおり。Title `Teiden` / `Teiden (Instrumental)` / 日本語 `停電`。
Audio: `output/停電.flac` / `output/停電 (Instrumental).flac`。
