# Release 011 — Yashoku / 夜食

| 項目 | 値 |
|---|---|
| 配信タイトル | Yashoku ／ 日本語ローカライズ: 夜食 |
| slug | yashoku |
| テーマ | 誰にも見せない時間ほど、二人だけの宝物になる |
| 主張（論法） | 半分こしたおにぎり、ご飯粒を見て笑う、誰にも言わない秘密――小さな具体を積み重ねる（帰納法） |
| 情景 | 深夜二時、冷蔵庫の灯りだけの台所 |
| Style | 案B |
| ステータス | RouteNote: Album Details/Artwork/Manage Stores/日本語ローカライズ(アルバムレベル)完了。UPC 5063941679242。配信日2026-10-05。Track(Add Audio)は音楽アップロードを後でまとめて行うため未着手 — その際にTrack1/2のローカライズも要追加 |

## Suno 入力

### Style欄
```
A soft synth motif glows like a fridge door opening in a dark kitchen, three warm notes settling into a hush. Mellow lo-fi pop meets late-night city-pop calm - a study-playlist steadiness with a pop ballad's quiet ache, chords leaning major but shaded with a wistful seventh. A young Japanese female voice, breathy and close, half-whispers the melody, close and private, recorded with pristine clarity. In the gaps a brief muted electric-piano phrase answers her. Production stays low, warm and pristine: rounded electric piano, clean analog pads, a soft room reverb, crystal-clear, nothing sharp or forward. A gentle boom-bap kick and brushed hi-hats hold an unhurried 118 BPM; a soft round bass walks beneath. The arrangement breathes in slow tides - hushed verses, a chorus that lifts only a little, a bridge that thins to one voice and a held pad, then eases back. Everything sits back in the mix, calm and repeatable, a loop to work beside.
```

### Exclude Styles欄
```
vinyl crackle, tape hiss, static, hum, background noise, muddy low end, hazy production, low fidelity, pop brightness, overly upbeat progressions, EDM festival bombast, big-room drops, aggressive techno, trap percussion cliches, loud belted vocals, excessive autotune, harsh compression, brittle sibilant highs, plastic synth textures, sterile digital reverb, predictable four-chord loops
```

### 歌詞欄
`work/lyrics_011_yashoku_suno.txt`（かな・③検証済み）
（work/ は Git 管理外なので下にも収録）:
```
[Intro]

[Verse1]
おなかがちいさくなる
とけいはしんやにじ
れいぞうこのとをあけて
しろいひかりがこぼれる
のこりもののおにぎりを
キミとはんぶんこする
だれもしらないじかんが
しずかにはじまってく

[PreChorus]
こえをひそめてわらう
だれにもいえないひみつ
あかりはれいぞうこだけ
それでじゅうぶんだね

[Chorus]
だれにもみせないじかんが
ふたりだけのたからもの
つめたいひかりのしたで
キミとわけあうやしょく
おなかがあったまったら
またねむってしまおう

[Verse2]
れいぞうこがまたうなって
しずかなおとだけひびく
キミのほおにごはんつぶ
それをみてわらった
だれにもいわないひみつが
またひとつふえていく
あしたのことはあしたの
キミにまかせよう

[Chorus]
だれにもみせないじかんが
ふたりだけのたからもの
つめたいひかりのしたで
キミとわけあうやしょく
おなかがあったまったら
またねむってしまおう

[Bridge]
とをしめるおとが
へやをまたくらくする
でもおなかはあたたかい
それだけでいいよるだ

[Chorus]
れいぞうこのあかりだけの
ちいさなやしょくかいだった
だれにもみせないじかんが
ふたりだけのたからものに
またおなかがすいたら
よんでねとなりで

[Outro]
とがしまる
キミがまたねむる
おやすみ
```


## ⑤〜⑩
`python scripts/run_audio.py --input input/yashoku_stems --name "夜食" --instrumental`

## ⑪-a ジャケット
シーン: 真夜中の台所、後ろ姿の人物が開けた冷蔵庫の前にしゃがんでいる。庫内灯だけが唯一の光源。
```
Soft painterly illustration, hand-painted book cover style, thick soft brushstrokes with visible canvas grain texture, muted desaturated cool-white and warm brown color palette. Extremely dark, moody, low-key lighting. A young woman with dark hair in a loose messy bun, seen from a three-quarter angle from behind, crouching in front of an open refrigerator in a dark midnight kitchen, the fridge's white interior light the only light source spilling onto her. Soft dark silhouette, face deep in shadow, no visible features, solid opaque clothing with no transparency. Square format, figure off-center, generous dark negative space. No text.
```
右下に `Tonarine` サイン。`covers/011-yashoku.jpg`。

## ⑪-b RouteNote
`_routenote_template.md` どおり。Title `Yashoku` / `Yashoku (Instrumental)` / 日本語 `夜食`。
Audio: `output/夜食.flac` / `output/夜食 (Instrumental).flac`。
