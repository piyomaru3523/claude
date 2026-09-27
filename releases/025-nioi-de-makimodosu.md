# Release 025 — 匂いで巻き戻す

| 項目 | 値 |
|---|---|
| 配信タイトル | （タイトル未定・歌詞確定後に決定） |
| slug | nioi-de-makimodosu |
| テーマ | あの瞬間の香りを覚えていると、時間が直線じゃなくなる |
| 主張（論法） | 香りの具体→時間の非線形性（帰納法） |
| 情景 | 夜、部屋に残った香り（シャンプー・香水）、そっと座る |
| Style | 案A（ウォーム・ドリーミー） |
| ステータス | 歌詞検証済み（③禁則違反なし）。Style/Exclude確定後、Suno生成へ |

## Suno 入力

### Style欄
```
Memory crystallized in scent — lo-fi, warm, dreamlike. A young Japanese female voice, breathy and vulnerable, whispers the melody as if half-asleep, close enough to feel like a confession, recorded with pristine clarity. Beneath, soft synth pads drift like scent lingering in air, analog warmth and haze, a single muted electric-piano phrase repeats gently, suggesting recollection. Production stays low, warm and clean: rounded keys, analog pad drift, a soft room reverb, a quiet noise floor, nothing sharp or forward. A gentle boom-bap kick and brushed swung hi-hats hold an unhurried 105 BPM; a soft round bass walks beneath. The arrangement breathes in slow tides — hushed verses that feel like sitting still, a chorus that lifts with recognition, a bridge that thins to one voice and held pad, then eases back. Everything sits back in the mix, calm and repeatable, a loop to drift beside.
```

### Exclude Styles欄
```
vinyl crackle, tape hiss, hissy noise floor, pop brightness, overly upbeat progressions, sharp percussion, EDM festival bombast, big-room drops, aggressive techno, trap percussion cliches, loud belted vocals, excessive autotune, harsh compression, brittle sibilant highs, plastic synth textures, sterile digital reverb, predictable four-chord loops, busy crowded arrangement
```

### 歌詞欄（かな。外来語のみカタカナ。③検証済み・禁則違反なし）
```
[Intro]

[Verse1]
あの
シャンプーの
においが
のこってる
ふとんを
ひらいたら
ふわっと
あたたかい
あのひの
あさと
おなじ
におい
だから
じかんが
もどる

[PreChorus]
においは
きおくだ
もどる
あのひに

[Chorus]
においで
まきもどせるなら
なんどでも
あのひを
よみがえらせる
きみの
ぬくもりを
またいっぺん
さがせるなら

[Verse2]
ながいあいだ
ずっと
この
かおりを
ままに
しておこう
ねむる
まえに
すこし
かいで
おぼえる
あのひの
あなた

[Chorus]
においで
たびできるなら
きおくの
なかで
あおてる
あのとき
のあなたを
もういっぺん
さわりたくて

[Bridge]
においが
すこしずつ
うすれていく
だから
いま
このまま

[Chorus]
においで
まきもどせるなら
なんどでも
あのひを
おもいだす

[Outro]
あの
におい
がすりきれるまで
```

---

## ステップ完了
- ①テーマ分析: 完了（テーマ・主張・情景確定）
- ②歌詞執筆: 完了
- ③歌詞検証: 完了（禁則違反なし）
- ④～⑩（Suno生成〜マスタリング）: 生成前

## ⑪-a ジャケット（`branding.md` テンプレ準拠）
シーン: 枕に残されたマフラーから香りのように立ちのぼる淡い光。
```
soft hand-drawn illustration, anime-adjacent, warm muted palette, a scarf left on a pillow of an unmade bed, faint curling wisps of soft light rising from it like scent, dim quiet room, no person, a glowing warm light as the single light source off-center, deep indigo-navy shadows with warm amber light, gentle linework, grainy textured shading, cozy and quiet, no visible face, generous empty space, square, no text
```
ネガティブ: `text, watermark, signature, harsh outlines, bright daylight, oversaturated, chibi, busy background, faces`
生成後にサイン合成: `python scripts/add_signature.py covers/025-nioi-de-makimodosu_bg.jpg covers/025-nioi-de-makimodosu.jpg`（背景は `_bg.jpg` で保存）。
