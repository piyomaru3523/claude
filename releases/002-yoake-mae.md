# Release 002 — Yoake Mae / 夜明け前

| 項目 | 値 |
|---|---|
| 配信タイトル | Yoake Mae ／ 日本語ローカライズ: 夜明け前 |
| slug | yoake-mae |
| テーマ | 徹夜明け・夜明け前。白む窓、冷めた最後のコーヒー |
| Style | 案B |
| 由来 | `work/features_2026-09-02.json` 流用 |
| ステータス | Suno生成待ち |
| 配信日 | 001の後、10〜14日間隔で（金曜・提出から最短14日） |

## Suno 入力

### Style欄
```
A soft synth note holds like the first pale light at the edge of a window, then a warm three-note motif circles back, familiar at once. Mellow lo-fi pop meets late-night city-pop calm - a study-playlist steadiness with a pop ballad's quiet ache, chords leaning major but shaded with a wistful seventh. A young Japanese female voice, breathy and close, half-whispers the melody, close and private, recorded with pristine clarity. In the gaps a brief muted electric-piano phrase answers her. Production stays low, warm and pristine: rounded electric piano, clean analog pads, a soft room reverb, crystal-clear, nothing sharp or forward. A gentle boom-bap kick and brushed hi-hats hold an unhurried 118 BPM; a soft round bass walks beneath. The arrangement breathes in slow tides - hushed verses, a chorus that lifts only a little, a bridge that thins to one voice and a held pad, then eases back. Everything sits back in the mix, calm and repeatable, a loop to work beside.
```

### Exclude Styles欄
```
vinyl crackle, tape hiss, static, hum, background noise, muddy low end, hazy production, low fidelity, pop brightness, overly upbeat progressions, EDM festival bombast, big-room drops, aggressive techno, trap percussion cliches, loud belted vocals, excessive autotune, harsh compression, brittle sibilant highs, plastic synth textures, sterile digital reverb, predictable four-chord loops
```

### 歌詞欄
`work/lyrics_002_yoake-mae_suno.txt`（かな・③検証済み）
（work/ は Git 管理外なので下にも収録）:
```
[Intro]

[Verse1]
そらのはしがしろむ
よるがほどけていく
キミのめはまだあいてる
よくがんばったね
カップのそこのコーヒー
とっくにつめたい
それでもすこしだけ
のこしておいたんだ

[PreChorus]
とりがなきはじめる
あさがくるあいず
まぶたがおもいなら
とじてもいいよ

[Chorus]
よあけまえのしずけさ
キミとここにいる
おわらせなくていい
つづきはあとでいい
ひかりがさすまえに
ひとやすみしよう

[Verse2]
まどのそとのあおが
すこしずつうすまる
とおくでくるまのおと
まちもめをさます
やりのこしたことは
かばんにいれておく
あしたのキミにわたす
それでたりてる

[Chorus]
よあけまえのしずけさ
キミとここにいる
おわらせなくていい
つづきはあとでいい
ひかりがさすまえに
ひとやすみしよう

[Bridge]
めをつむってみて
いきをふかくすって
かたのちからをぬく
もうだいじょうぶ

[Chorus]
よあけまえのしずけさ
キミとここにいる
むりをしないでいい
めざめはゆっくりで
ひかりがさすころに
おはようをいおう

[Outro]
そらがしろい
キミがねむる
おやすみ
```


## ⑤〜⑩
`python scripts/run_audio.py --input input/yoake-mae_stems --name "夜明け前" --instrumental`
（単一ミックスなら `--input input/yoake-mae.wav`）

## ⑪-a ジャケット（手描きイラスト / `branding.md`）
シーン: 後ろ姿の人物が机に向かい、窓の空がうっすら白みはじめている。冷めて半分残ったマグ、まだ点いた小さなデスクランプ。
```
soft hand-drawn illustration, anime-adjacent, warm muted palette, a person seen from behind at a small desk, the sky just outside the window beginning to pale toward dawn, a half-empty mug of cold coffee, a small desk lamp still glowing as the single light source off-center, deep indigo-navy shadows with warm amber light, gentle linework, grainy textured shading, cozy and quiet, no visible face, not centered, generous empty space, square, no text
```
生成後、右下に `Tonarine`（Sacramento・約135px・#F2C88C 80%・端から約130px）。`covers/002-yoake-mae.jpg`。

## ⑪-b RouteNote
`releases/_routenote_template.md` の固定値どおり。曲固有:
- Release/Track title: `Yoake Mae` ／ Track2: `Yoake Mae (Instrumental)`
- 日本語ローカライズ: `夜明け前`
- Audio: `output/夜明け前.flac` / `output/夜明け前 (Instrumental).flac`

