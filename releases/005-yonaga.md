# Release 005 — Yonaga / 夜長

| 項目 | 値 |
|---|---|
| 配信タイトル | Yonaga ／ 日本語ローカライズ: 夜長 |
| slug | yonaga |
| テーマ | 秋の夜長。肌寒い夜、上着、窓の外に虫の声、毛布 |
| Style | 案B |
| ステータス | Suno生成待ち |
| 配信目安 | 10〜11月（秋の内容のため早めに） |

## Suno 入力

### Style欄
```
A low synth pad settles like early dark, and a warm three-note motif circles back under a faint hum of distant insects. Mellow lo-fi pop meets late-night city-pop calm - a study-playlist steadiness with a pop ballad's quiet ache, chords leaning major but shaded with a wistful seventh. A young Japanese female voice, breathy and close, half-whispers the melody as if not to wake anyone, close enough to feel private. In the gaps a brief muted electric-piano phrase answers her. Production stays low, warm and clean: rounded electric piano, analog pad haze, a soft room reverb, a quiet noise floor, nothing sharp or forward. A gentle boom-bap kick and brushed swung hi-hats hold an unhurried 118 BPM; a soft round bass walks beneath. The arrangement breathes in slow tides - hushed verses, a chorus that lifts only a little, a bridge that thins to one voice and a held pad, then eases back. Everything sits back in the mix, calm and repeatable, a loop to work beside.
```

### Exclude Styles欄
```
vinyl crackle, tape hiss, pop brightness, overly upbeat progressions, EDM festival bombast, big-room drops, aggressive techno, trap percussion cliches, loud belted vocals, excessive autotune, harsh compression, brittle sibilant highs, plastic synth textures, sterile digital reverb, predictable four-chord loops, busy crowded arrangement, big band brass
```

### 歌詞欄
`work/lyrics_005_yonaga_suno.txt`
（work/ は Git 管理外なので下にも収録）:
```
[Intro]

[Verse1]
ひがおちるのがはやい
よるがながくなった
キミはうわぎをはおる
ゆびさきがすこしひえる
まどのそとのくさむら
むしがまだないてる
ほそいこえがつづく
あきのおわりのおと

[PreChorus]
あたたかいものをもって
つくえにもどろう
よるはにげないから
ゆっくりでいい

[Chorus]
よるがながいなら
いそがなくていい
キミのぶんだけ
じかんはここにある
となりでみているよ
あさはとおいから

[Verse2]
もうふをもういちまい
あしもとにおいた
ページをめくるおと
へやにだけひびく
やりたいこととやること
どちらもだいじで
こんやはすこしずつ
ほどいていこう

[Chorus]
よるがながいなら
いそがなくていい
キミのぶんだけ
じかんはここにある
となりでみているよ
あさはとおいから

[Bridge]
まどをすこししめて
むしのこえがとおのく
かたをあたためて
またつづけよう

[Chorus]
よるがながいから
あせらなくていい
キミのペースで
いっぽずつでいい
となりにすわるよ
むしがやむまでは

[Outro]
よるがふかくなる
キミがしゅうちゅうする
そのちょうし
```


## ⑤〜⑩
`python scripts/run_audio.py --input input/yonaga_stems --name "夜長" --instrumental`

## ⑪-a ジャケット
シーン: 後ろ姿の人物が薄手の上着（カーディガン）を羽織って机に向かう。暗い秋の夜の窓、椅子にもう一枚の毛布、暖色のランプ。
```
soft hand-drawn illustration, anime-adjacent, warm muted palette, a person seen from behind at a small desk wearing a light cardigan, a dark autumn night through the window, a second blanket draped over the chair, a small warm desk lamp as the single light source off-center, deep indigo-navy shadows with warm amber light, gentle linework, grainy textured shading, cozy and quiet, no visible face, not centered, generous empty space, square, no text
```
右下に `Tonarine` サイン。`covers/005-yonaga.jpg`。

## ⑪-b RouteNote
`_routenote_template.md` どおり。Title `Yonaga` / `Yonaga (Instrumental)` / 日本語 `夜長`。
Audio: `output/夜長.flac` / `output/夜長 (Instrumental).flac`。

