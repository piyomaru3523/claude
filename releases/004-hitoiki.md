# Release 004 — Hitoiki / ひといき

| 項目 | 値 |
|---|---|
| 配信タイトル | Hitoiki ／ 日本語ローカライズ: ひといき |
| slug | hitoiki |
| テーマ | 休憩。やかんの音、温かいお茶、伸び、肩にかけた毛布 |
| Style | 案B |
| ステータス | RouteNote 入稿完了（審査待ち）。配信日 **2026-10-02(金)** |
| マスター | `output/ひといき.flac`（-15.89 LUFS / -0.98 dBTP）／ インスト版あり |

## Suno 入力

### Style欄
```
A warm three-note motif rises like steam from a mug, curling back on itself, familiar at once. Mellow lo-fi pop meets late-night city-pop calm - a study-playlist steadiness with a pop ballad's quiet ache, chords leaning major but shaded with a wistful seventh. A young Japanese female voice, breathy and close, half-whispers the melody, close and private, recorded with pristine clarity. In the gaps a brief muted electric-piano phrase answers her. Production stays low, warm and pristine: rounded electric piano, clean analog pads, a soft room reverb, crystal-clear, nothing sharp or forward. A gentle boom-bap kick and brushed hi-hats hold an unhurried 118 BPM; a soft round bass walks beneath. The arrangement breathes in slow tides - hushed verses, a chorus that lifts only a little, a bridge that thins to one voice and a held pad, then eases back. Everything sits back in the mix, calm and repeatable, a loop to work beside.
```

### Exclude Styles欄
```
vinyl crackle, tape hiss, static, hum, background noise, muddy low end, hazy production, low fidelity, pop brightness, overly upbeat progressions, EDM festival bombast, big-room drops, aggressive techno, trap percussion cliches, loud belted vocals, excessive autotune, harsh compression, brittle sibilant highs, plastic synth textures, sterile digital reverb, predictable four-chord loops
```

### 歌詞欄
`work/lyrics_004_hitoiki_suno.txt`
（work/ は Git 管理外なので下にも収録）:
```
[Intro]

[Verse1]
やかんがなった
キミのてがとまる
おちゃをいれるじかんだ
すこしだけやすもう
ゆげがゆっくりのぼる
まどにまるくにじむ
がめんからめをはなす
それだけでいい

[PreChorus]
せのびをひとつ
かたがかるくなる
いそぐよるじゃない
すわっていよう

[Chorus]
ひといきつこう
キミのペースでいい
てをとめるのは
サボりじゃないよ
となりであたたかい
ゆげをみている

[Verse2]
もうふをかたにかけて
あしをすこしのばす
とけいのおとがやさしい
いまはいそがない
やることはきえない
でもにげもしない
もどればまっている
あわてなくていい

[Chorus]
ひといきつこう
キミのペースでいい
てをとめるのは
サボりじゃないよ
となりであたたかい
ゆげをみている

[Bridge]
おちゃをひとくち
のどがゆるんでいく
まだよるはながい
ゆっくりでいい

[Chorus]
ひといきついた
キミのめがやわらぐ
そろそろもどろうか
でもいまじゃなくていい
となりでみているよ
ゆげがきえるまで

[Outro]
カップがからになる
キミがたちあがる
おかえり
```


## ⑤〜⑩
`python scripts/run_audio.py --input input/hitoiki_stems --name "ひといき" --instrumental`

## ⑪-a ジャケット
シーン: 後ろ姿の人物が机から少し身を引き、湯気の立つマグを両手で持つ。肩に毛布、暖色のランプ。
```
soft hand-drawn illustration, anime-adjacent, warm muted palette, a person seen from behind leaning back from a small desk, holding a steaming mug in both hands, a blanket over their shoulders, a small warm desk lamp as the single light source off-center, deep indigo-navy shadows with warm amber light, gentle linework, grainy textured shading, cozy and quiet, no visible face, not centered, generous empty space, square, no text
```
右下に `Tonarine` サイン。`covers/004-hitoiki.jpg`。

## ⑪-b RouteNote
`_routenote_template.md` どおり。Title `Hitoiki` / `Hitoiki (Instrumental)` / 日本語 `ひといき`。
Audio: `output/ひといき.flac` / `output/ひといき (Instrumental).flac`。

