# Release 005 — Yonaga / 夜長

| 項目 | 値 |
|---|---|
| 配信タイトル | Yonaga ／ 日本語ローカライズ: 夜長 |
| slug | yonaga |
| テーマ | 秋の夜長。肌寒い夜、上着、窓の外に虫の声、毛布 |
| Style | 案B |
| ステータス | ⑤〜⑩完了。⑪ 試聴確認待ち |
| マスター | `output/夜長.flac`（-15.87 LUFS / -0.98 dBTP）／ インスト版あり（-0.98 dBTP） |
| 配信目安 | 10〜11月（秋の内容のため早めに） |

## Suno 入力

### Style欄
```
A low synth pad settles like early dark, and a warm three-note motif circles back under a faint hum of distant insects. Mellow lo-fi pop meets late-night city-pop calm - a study-playlist steadiness with a pop ballad's quiet ache, chords leaning major but shaded with a wistful seventh. A young Japanese female voice, breathy and close, half-whispers the melody, close and private, recorded with pristine clarity. In the gaps a brief muted electric-piano phrase answers her. Production stays low, warm and pristine: rounded electric piano, clean analog pads, a soft room reverb, crystal-clear, nothing sharp or forward. A gentle boom-bap kick and brushed hi-hats hold an unhurried 118 BPM; a soft round bass walks beneath. The arrangement breathes in slow tides - hushed verses, a chorus that lifts only a little, a bridge that thins to one voice and a held pad, then eases back. Everything sits back in the mix, calm and repeatable, a loop to work beside.
```

### Exclude Styles欄
```
vinyl crackle, tape hiss, static, hum, background noise, muddy low end, hazy production, low fidelity, pop brightness, overly upbeat progressions, EDM festival bombast, big-room drops, aggressive techno, trap percussion cliches, loud belted vocals, excessive autotune, harsh compression, brittle sibilant highs, plastic synth textures, sterile digital reverb, predictable four-chord loops
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
シーン: 後ろ姿の人物が薄手の上着（カーディガン）を羽織って机に向かう。暗い秋の夜の窓（星・裸木）、椅子にもう一枚の毛布、オイルランプ。001に絵柄を揃えるため、Gemini生成→Canvaで高解像度化という流れで作成。
```
Soft painterly illustration, hand-painted book cover style, thick soft brushstrokes with visible canvas grain texture, muted desaturated warm brown-amber-olive color palette. Extremely dark, moody, low-key lighting: the entire room is deep shadow except for one small warm pool of lamplight. A young woman with dark hair in a loose messy bun, seen from a three-quarter angle from behind, sitting at a small worn wooden desk. She is a soft dark silhouette with almost no visible detail — her face is deep in shadow, no visible eyes, no clear facial features. She wears a simple long-sleeved cardigan, solid opaque fabric, no transparency. A folded blanket is draped over the back of her wooden chair. To her left, a window shows a dark autumn night sky with faint stars and bare tree branches. A small oil lamp on the desk casts a warm amber glow that fades into darkness elsewhere. Square format, figure off-center, generous dark negative space. No text.
```
右下に `Tonarine` サイン。`covers/005-yonaga.jpg`。

## ⑪-b RouteNote
`_routenote_template.md` どおり。Title `Yonaga` / `Yonaga (Instrumental)` / 日本語 `夜長`。
Audio: `output/夜長.flac` / `output/夜長 (Instrumental).flac`。

