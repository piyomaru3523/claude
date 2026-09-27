# Release 007 — Gozen Sanji / 午前三時

| 項目 | 値 |
|---|---|
| 配信タイトル | Gozen Sanji ／ 日本語ローカライズ: 午前三時 |
| slug | gozen-sanji |
| テーマ | 眠れない三時。時計、天井、寝転がってイヤホン |
| Style | 案A（ジャズ寄り） |
| ステータス | RouteNote 入稿完了（審査待ち）。配信日 **2026-10-02(金)** |
| マスター | `output/午前三時.flac`（-16.08 LUFS / -0.97 dBTP）／ インスト版あり（-16.03 LUFS / -5.37 dBTP） |
| ステム | 8パート（Guitar/Strings含む、Brass/Woodwindsなし）。⑥は本編B_standard／インストA_calm選定 |

## Suno 入力

### Style欄
```
A muted electric-piano figure drifts in the dark like a clock you stopped hearing, jazzy sevenths leaning and resolving, very soft. Mellow lo-fi meets late-night jazz - the hush of a study playlist carrying the warmth of a small combo, chords full of sevenths and ninths, never bright, always a little wistful. A young Japanese female voice, breathy and close, half-sings the melody, close and private, recorded with pristine clarity. Brushed drums swing softly under an unhurried 104 BPM; an upright-style bass walks in slow steps; a muted electric-piano line answers the voice in the gaps. Production stays low, warm and pristine: felt-damped keys, a soft room reverb, crystal-clear, nothing sharp or forward. The arrangement breathes in slow tides - hushed verses, a chorus that lifts only a little, a bridge that thins to voice and one held chord, then eases back. Everything sits back in the mix, calm and repeatable, a loop to work beside.
```

### Exclude Styles欄
```
vinyl crackle, tape hiss, static, hum, background noise, muddy low end, hazy production, low fidelity, pop brightness, overly upbeat progressions, EDM festival bombast, big-room drops, aggressive techno, trap percussion cliches, loud belted vocals, excessive autotune, harsh compression, brittle sibilant highs, plastic synth textures, sterile digital reverb, predictable four-chord loops
```

### 歌詞欄
`work/lyrics_007_gozen-sanji_suno.txt`
（work/ は Git 管理外なので下にも収録）:
```
[Intro]

[Verse1]
とけいがさんじをさす
ねむりがこないよる
キミはてんじょうをみてる
かんがえがまわる
ふとんのなかはくらい
そとはもっとしずか
イヤホンをつける
おとをちいさくして

[PreChorus]
かぞえるのはやめて
いきだけをおう
ねむれなくてもいい
おきていていい

[Chorus]
ごぜんさんじのへやで
キミはひとりじゃない
あしたのことは
いまはおいておこう
となりでなっているよ
あさがくるまでは

[Verse2]
きのうのちいさなくい
まだむねにのこる
でもよるのさんじは
きめるじかんじゃない
かんがえはあさにわたす
いまはただよこになる
てんじょうのくらがりに
おとをひろげる

[Chorus]
ごぜんさんじのへやで
キミはひとりじゃない
あしたのことは
いまはおいておこう
となりでなっているよ
あさがくるまでは

[Bridge]
まぶたがおもくなる
おとがぼやけていく
そのまましずんで
あさであおう

[Chorus]
ごぜんさんじをすぎて
キミのいきがゆるむ
ねむれそうなら
このままめをとじて
となりでちいさく
ならしつづけるよ

[Outro]
とけいがよじ
キミがねむった
おやすみ
```


## ⑤〜⑩
`python scripts/run_audio.py --input input/gozen-sanji_stems --name "午前三時" --instrumental`

## ⑪-a ジャケット
シーン: 暗い部屋、布団に横たわる人物を斜め上から。イヤホンをつけ、天井を見ている。かすかに光る時計だけが唯一の光。顔は見えない・中央に置かない。
```
soft hand-drawn illustration, anime-adjacent, warm muted palette, a person lying on a futon in a dark room seen from a low angle, earphones in, looking up at the ceiling, a faintly glowing clock as the only light source off-center, deep indigo-navy shadows with a small warm glow, gentle linework, grainy textured shading, quiet and still, no visible face, not centered, generous empty space, square, no text
```
右下に `Tonarine` サイン。`covers/007-gozen-sanji.jpg`。

## ⑪-b RouteNote
`_routenote_template.md` どおり。Title `Gozen Sanji` / `Gozen Sanji (Instrumental)` / 日本語 `午前三時`。
Audio: `output/午前三時.flac` / `output/午前三時 (Instrumental).flac`。

