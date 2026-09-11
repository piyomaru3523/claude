# Release 003 — Ame no Yoru / 雨の夜

| 項目 | 値 |
|---|---|
| 配信タイトル | Ame no Yoru ／ 日本語ローカライズ: 雨の夜 |
| slug | ame-no-yoru |
| テーマ | 雨の夜の作業。窓を伝う雨、玄関に立てた濡れた傘 |
| Style | 案A（ジャズ寄り） |
| ステータス | Suno生成待ち |

## Suno 入力

### Style欄
```
An electric-piano phrase falls in time with rain on the glass, three jazzy chords that lean and resolve like someone thinking out loud. Mellow lo-fi meets late-night jazz - the hush of a study playlist carrying the warmth of a small combo, chords full of sevenths and ninths, never bright, always a little wistful. A young Japanese female voice, breathy and close, half-sings the melody, close and private, recorded with pristine clarity. Brushed drums swing softly under an unhurried 104 BPM; an upright-style bass walks in slow steps; a muted electric-piano line answers the voice in the gaps. Production stays low, warm and pristine: felt-damped keys, a soft room reverb, crystal-clear, nothing sharp or forward. The arrangement breathes in slow tides - hushed verses, a chorus that lifts only a little, a bridge that thins to voice and one held chord, then eases back. Everything sits back in the mix, calm and repeatable, a loop to work beside.
```

### Exclude Styles欄
```
vinyl crackle, tape hiss, static, hum, background noise, muddy low end, hazy production, low fidelity, pop brightness, overly upbeat progressions, EDM festival bombast, big-room drops, aggressive techno, trap percussion cliches, loud belted vocals, excessive autotune, harsh compression, brittle sibilant highs, plastic synth textures, sterile digital reverb, predictable four-chord loops
```

### 歌詞欄
`work/lyrics_003_ame-no-yoru_suno.txt`
（work/ は Git 管理外なので下にも収録）:
```
[Intro]

[Verse1]
まどをつたうあめ
ほそいせんをひく
キミのペンもとまらない
おなじリズムで
かさはかわかないまま
げんかんにたてた
へやはあたたかい
それでじゅうぶん

[PreChorus]
のきしたのみずおと
ひくくつづいてる
いそがなくていい
あめもまってる

[Chorus]
あめのよるのなかで
キミのてがうごく
ぬれたまちをみてる
まどのうちがわから
となりにすわるよ
おとがやむまでは

[Verse2]
ノートのすみに
ちいさなしみがひとつ
あめのせいにしておく
きにしなくていい
かんがえごとがおおいよる
そとはあらわれてく
キミのあたまのなかも
すこしずつはれる

[Chorus]
あめのよるのなかで
キミのてがうごく
ぬれたまちをみてる
まどのうちがわから
となりにすわるよ
おとがやむまでは

[Bridge]
かさのおとをきいて
かたをすこしおとす
ゆびをあたためて
またかきだそう

[Chorus]
あめのよるのなかで
キミのてがうごく
あせらなくていいよ
じかんはまだある
となりにすわるよ
あさがくるまでは

[Outro]
あめがほそくなる
キミがいきをつく
もうすこし
```


## ⑤〜⑩
`python scripts/run_audio.py --input input/ame-no-yoru_stems --name "雨の夜" --instrumental`

## ⑪-a ジャケット
シーン: 後ろ姿の人物が机に向かい、暗い窓を雨がいく筋も伝う。暖色のデスクランプ、ドアのそばに閉じた傘。
```
soft hand-drawn illustration, anime-adjacent, warm muted palette, a person seen from behind at a small desk, rain streaking down a dark window beside them, a closed umbrella leaning by the door, a small warm desk lamp as the single light source off-center, deep indigo-navy shadows with warm amber light, gentle linework, grainy textured shading, cozy and quiet, no visible face, not centered, generous empty space, square, no text
```
右下に `Tonarine` サイン。`covers/003-ame-no-yoru.jpg`。

## ⑪-b RouteNote
`_routenote_template.md` どおり。Title `Ame no Yoru` / `Ame no Yoru (Instrumental)` / 日本語 `雨の夜`。
Audio: `output/雨の夜.flac` / `output/雨の夜 (Instrumental).flac`。

