# Release 006 — Kaerimichi / 帰り道

| 項目 | 値 |
|---|---|
| 配信タイトル | Kaerimichi ／ 日本語ローカライズ: 帰り道 |
| slug | kaerimichi |
| テーマ | 終電後の帰り道→机。誰もいない道、帰宅して灯りをつける |
| Style | 案B |
| ステータス | ⑤〜⑩完了。⑪ 試聴確認待ち |
| マスター | `output/帰り道.flac`（-16.05 LUFS / -0.98 dBTP）／ インスト版あり（-0.93 dBTP） |

## Suno 入力

### Style欄
```
A soft synth motif clicks on like a lamp in an empty room, three warm notes that circle back, familiar at once. Mellow lo-fi pop meets late-night city-pop calm - a study-playlist steadiness with a pop ballad's quiet ache, chords leaning major but shaded with a wistful seventh. A young Japanese female voice, breathy and close, half-whispers the melody, close and private, recorded with pristine clarity. In the gaps a brief muted electric-piano phrase answers her. Production stays low, warm and pristine: rounded electric piano, clean analog pads, a soft room reverb, crystal-clear, nothing sharp or forward. A gentle boom-bap kick and brushed hi-hats hold an unhurried 118 BPM; a soft round bass walks beneath. The arrangement breathes in slow tides - hushed verses, a chorus that lifts only a little, a bridge that thins to one voice and a held pad, then eases back. Everything sits back in the mix, calm and repeatable, a loop to work beside.
```

### Exclude Styles欄
```
vinyl crackle, tape hiss, static, hum, background noise, muddy low end, hazy production, low fidelity, pop brightness, overly upbeat progressions, EDM festival bombast, big-room drops, aggressive techno, trap percussion cliches, loud belted vocals, excessive autotune, harsh compression, brittle sibilant highs, plastic synth textures, sterile digital reverb, predictable four-chord loops
```

### 歌詞欄
`work/lyrics_006_kaerimichi_suno.txt`
（work/ は Git 管理外なので下にも収録）:
```
[Intro]

[Verse1]
しゅうでんがいった
ホームにのこるキミ
ひとつさきまであるく
よるのくうきはうすい
じはんきのあかり
みちをぼんやりてらす
あしおとだけがつづく
それでもすすむ

[PreChorus]
かぎをまわすおと
へやがキミをまつ
うわぎをかけて
あかりをつける

[Chorus]
かえりみちのはてに
ちいさなつくえがある
おそくなっても
もどれるばしょがある
となりにすわるよ
つくえにつくまで

[Verse2]
まどのそとはしずか
とおくでいぬがなく
いちにちのおもさを
いすにおろす
やりのこしはあるけど
きょうはここまででいい
つづきはつくえのうえで
あしたまたあおう

[Chorus]
かえりみちのはてに
ちいさなつくえがある
おそくなっても
もどれるばしょがある
となりにすわるよ
つくえにつくまで

[Bridge]
くつをそろえておく
いきをひとつはく
きょうもよくやった
もうやすもう

[Chorus]
かえりみちはながい
でもひとりじゃない
キミがつくころに
あかりをつけておく
となりでまってるよ
おかえりをいう

[Outro]
かぎがかかる
キミがすわる
ただいま
```


## ⑤〜⑩
`python scripts/run_audio.py --input input/kaerimichi_stems --name "帰り道" --instrumental`

## ⑪-a ジャケット
シーン: カーテンの隙間から、後ろ姿の人物が窓越しに誰もいない夜道を見ている。濡れた路面に街灯の光が反射。001に絵柄を揃えるため、001と同系統のプロンプトでCanva生成。
```
Soft painterly illustration, hand-painted book cover style, thick soft brushstrokes with visible canvas grain texture, muted desaturated warm brown-amber-olive color palette. Extremely dark, moody, low-key lighting. A young woman with dark hair in a loose messy bun, seen from behind, small in the frame and off-center, standing near a window at night, looking out. Soft dark silhouette, face deep in shadow, no visible features. Solid opaque cardigan, no transparency. Through the window, a quiet empty night street: wet asphalt reflecting warm amber streetlamp light, bare trees, no people. Square format, generous dark negative space. No text.
```
右下に `Tonarine` サイン。`covers/006-kaerimichi.jpg`。

## ⑪-b RouteNote
`_routenote_template.md` どおり。Title `Kaerimichi` / `Kaerimichi (Instrumental)` / 日本語 `帰り道`。
Audio: `output/帰り道.flac` / `output/帰り道 (Instrumental).flac`。

