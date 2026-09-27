# Release 031 — 朝日が差し込む

| 項目 | 値 |
|---|---|
| 配信タイトル | （タイトル未定・歌詞確定後に決定） |
| slug | asahi-ga-sashikomu |
| テーマ | 現実より、この時間を選ぶ。優先順位が変わった |
| 主張（論法） | 朝日・床・キミの寝顔→選択の転換（帰納法） |
| 情景 | 初夏の寝坊した朝、床に流れる朝日、キミとまた寝ることにする |
| Style | 案C（シネマティック・ウォーム） |
| ステータス | 歌詞検証済み（③禁則違反なし）。Style/Exclude確定後、Suno生成へ |

## Suno 入力

### Style欄
```
Morning light, a choice unmade — lo-fi, cinematic, with warm orchestral undertones. A young Japanese female voice, breathy and tender, whispers the melody as if making a private decision, close and intimate, recorded with pristine clarity. Beneath, felt piano and long reverb tails, soft strings that suggest morning light without stating it, chords drifting between major and wistful. Production stays low, warm and pristine: felt piano, analog pad haze, a soft room ambience, crystal-clear, nothing sharp or demanding. A gentle boom-bap kick and brushed hi-hats hold an unhurried 105 BPM; a soft round bass walks beneath. The arrangement breathes in slow tides — hushed verses that feel like waking, a chorus that affirms the choice to stay, a bridge that thins to one voice and held pad, then eases back. Everything sits back in the mix, calm and repeatable, a loop to rest beside.
```

### Exclude Styles欄
```
vinyl crackle, tape hiss, hissy noise floor, energetic morning vibes, pop brightness, overly upbeat progressions, urgent tempo, EDM festival bombast, big-room drops, aggressive techno, trap percussion cliches, loud belted vocals, excessive autotune, harsh compression, brittle sibilant highs, plastic synth textures, sterile digital reverb, predictable four-chord loops
```

### 歌詞欄（かな。外来語のみカタカナ。③検証済み・禁則違反なし）
```
[Intro]

[Verse1]
あさひが
ゆかに
ながれこむ
きょうも
ねぼうした
ほんとうは
いそがなきゃ
いけない
でも
きみの
ねがおが
きらきら
しててさ
ぼくは
ここに
いたい

[PreChorus]
よのなか
よりも
このじかんが
だいじ

[Chorus]
あさひが
さすなか
もういっぺん
ねよう
げんじつより
ここが
だいじ
だから
もう
おきない

[Verse2]
しごとも
ようじも
ぜんぶ
あとだ
キミの
ねぐせ
あたまのあたり
ひかりが
ふれて
きみが
きらきら
してる

[Chorus]
あさひが
さすなか
もういっぺん
ねよう
せかいより
ここが
だいじだ
だから
このまま
ずっと

[Bridge]
ゆうせんじゅいが
かわった
あさひのなかで

[Chorus]
あさひが
さすなか
もういっぺん
ねよう
これからも
ここが
いちばん

[Outro]
あさひ
だけど
ねてる
```

---

## ステップ完了
- ①テーマ分析: 完了（テーマ・主張・情景確定）
- ②歌詞執筆: 完了
- ③歌詞検証: 完了（禁則違反なし）
- ④～⑩（Suno生成〜マスタリング）: 生成前

## ⑪-a ジャケット（`branding.md` テンプレ準拠）
シーン: 初夏の朝、床に流れる朝日と二人分の枕、布団の膨らみ。光源は朝日1つ。
```
soft hand-drawn illustration, anime-adjacent, warm muted palette, a warm patch of morning sunlight spilling across a wooden floor toward an unmade bed with two pillows and a mound of blanket, early summer morning, sunbeam as the single light source, no face, a glowing warm light as the single light source off-center, deep indigo-navy shadows with warm amber light, gentle linework, grainy textured shading, cozy and quiet, no visible face, generous empty space, square, no text
```
ネガティブ: `text, watermark, signature, harsh outlines, bright daylight, oversaturated, chibi, busy background, faces`
生成後にサイン合成: `python scripts/add_signature.py covers/031-asahi-ga-sashikomu_bg.jpg covers/031-asahi-ga-sashikomu.jpg`（背景は `_bg.jpg` で保存）。
