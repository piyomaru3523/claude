# Release 032 — 月を見上げる

| 項目 | 値 |
|---|---|
| 配信タイトル | （タイトル未定・歌詞確定後に決定） |
| slug | tsuki-wo-miageru |
| テーマ | 同じ月を見ているキミのことを思う、遠く離れていても繋がっている |
| 主張（論法） | 月の光→距離の認識→つながり（帰納法） |
| 情景 | 秋の夜間、外出時に月が見える、歩きながらキミを思う |
| Style | 案B（シネマティック・ノスタルジック） |
| ステータス | 歌詞検証済み（③禁則違反なし）。Style/Exclude確定後、Suno生成へ |

## Suno 入力

### Style欄
```
Autumn moonlight, distance bridged by shared light — lo-fi, cinematic, with nostalgic warmth. A young Japanese female voice, breathy and wistful, sings the melody as if looking up into night sky, vulnerable and clear, recorded with pristine clarity. Beneath, soft synth pads drift like moonlight, a single muted electric-piano phrase answers gently, chords leaning major but shaded with melancholy. Production stays low, warm and pristine: felt piano, analog pad haze, a soft room reverb, crystal-clear, nothing sharp or forward. A gentle boom-bap kick and brushed swung hi-hats hold an unhurried 100 BPM; a soft round bass walks beneath. The arrangement breathes in slow tides — hushed verses that feel like walking alone, a chorus that affirms connection across distance, a bridge that thins to one voice and held pad, then eases back. Everything sits back in the mix, calm and repeatable, a loop to walk beside.
```

### Exclude Styles欄
```
vinyl crackle, tape hiss, hissy noise floor, pop brightness, overly upbeat progressions, energetic night vibes, EDM festival bombast, big-room drops, aggressive techno, trap percussion cliches, loud belted vocals, excessive autotune, harsh compression, brittle sibilant highs, plastic synth textures, sterile digital reverb, predictable four-chord loops
```

### 歌詞欄（かな。外来語のみカタカナ。③検証済み・禁則違反なし）
```
[Intro]

[Verse1]
あきの
よるは
つきが
きれい
あおく
ひかってる
キミも
みてるのかな
おなじ
つきを
いま
このしゅんかんに
おもいだす
キミの
かお

[PreChorus]
きょりが
あっても
つきは
いっしょ

[Chorus]
つきを
みあげると
キミが
ちかい
とおいのに
つながってる
かんじて
だから
あるける
このみちを

[Verse2]
いつもと
ちがう
つきの
ひかり
きれいだから
よけいに
キミが
こいしい
でも
この
つきが
きっと
キミにも
とどいてるはず

[Chorus]
つきを
みあげると
キミが
ちかい
とおいのに
ここにいる
かんじて
だから
あるける

[Bridge]
おなじ
つきのひかり
あたってる

[Chorus]
つきを
みあげると
キミが
みえる

[Outro]
あきの
つき
```

---

## ステップ完了
- ①テーマ分析: 完了（テーマ・主張・情景確定）
- ②歌詞執筆: 完了
- ③歌詞検証: 完了（禁則違反なし）
- ④～⑩（Suno生成〜マスタリング）: 生成前

## ⑪-a ジャケット（`branding.md` テンプレ準拠）
シーン: 秋の夜、月を見上げる小さな後ろ姿。街灯1つ、落ち葉。
```
soft hand-drawn illustration, anime-adjacent, warm muted palette, a small figure seen from behind standing on an autumn street looking up at a large pale moon, a single street lamp, fallen leaves on the ground, tiny in the frame, a glowing warm light as the single light source off-center, deep indigo-navy shadows with warm amber light, gentle linework, grainy textured shading, cozy and quiet, no visible face, generous empty space, square, no text
```
ネガティブ: `text, watermark, signature, harsh outlines, bright daylight, oversaturated, chibi, busy background, faces`
生成後にサイン合成: `python scripts/add_signature.py covers/032-tsuki-wo-miageru_bg.jpg covers/032-tsuki-wo-miageru.jpg`（背景は `_bg.jpg` で保存）。
