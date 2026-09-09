# Release 001 — 夜更けのとなり

| 項目 | 値 |
|---|---|
| 曲名 | **夜更けのとなり** |
| ローマ字 | Yofuke no Tonari |
| アーティスト | Tonarine（`branding.md`） |
| 由来 | Billboard JAPAN Hot 100 2026-09-02 付の分析（`work/features_2026-09-02.json`）→ 案B |
| 尺の目安 | 2:50 |
| 言語 | Japanese |
| ジャンル | Lo-fi / チル（作業用BGM） |
| ステータス | Suno生成待ち（有料プラン・商用利用権） |

## Suno 入力

### Style欄（Styles）
```
A soft synth motif opens like a desk lamp clicking on in a dark room: three warm notes that curl back on themselves, familiar at once. Mellow lo-fi pop meets late-night city-pop calm - a study-playlist steadiness with a pop ballad's quiet ache, chords leaning major but shaded with a wistful seventh. A young Japanese female voice, breathy and close, half-whispers the melody as if not to wake anyone, close enough to feel private. In the gaps a brief muted electric-piano phrase answers her. Production stays low and warm: rounded electric piano, analog pad haze, faint vinyl crackle and tape hiss in a soft room reverb, nothing sharp or forward. A gentle boom-bap kick and brushed swung hi-hats hold an unhurried 120 BPM; a soft round bass walks beneath. The arrangement breathes in slow tides - hushed verses, a chorus that lifts only a little, a bridge that thins to one voice and a held pad, then eases back. Everything sits back in the mix, calm and repeatable, a loop to work beside.
```

### Exclude Styles欄
```
pop brightness, overly upbeat progressions, EDM festival bombast, big-room drops, aggressive techno, trap percussion cliches, loud belted vocals, excessive autotune, harsh compression, brittle sibilant highs, plastic synth textures, sterile digital reverb, dubstep wobble, predictable four-chord loops, busy crowded arrangement, distorted guitars, cinematic orchestral swells
```

### 歌詞欄（かな。外来語のみカタカナ。③検証済み・禁則違反なし）
```
[Intro]

[Verse1]
よふけのつくえ
ちいさなあかり
キミのペンがはしる
しずかなよる
コーヒーはぬるい
それでもすすむ
となりであくびを
かみころしてる

[PreChorus]
めをこすっても
まだいけるはず
とけいのはりが
せなかをおす

[Chorus]
むりしないでいい
ゆっくりでいい
キミのペースで
よるをわたろう
となりにいるよ
おなじあかりで

[Verse2]
まどのそとには
あおいくらやみ
だれもいないみち
かぜだけがなく
やりかけのゆめ
とじずにおいて
あさになったら
またてをのばそう

[Chorus]
むりしないでいい
ゆっくりでいい
キミのペースで
よるをわたろう
となりにいるよ
おなじあかりで

[Bridge]
ゆっくりいきをして
あわてなくていい
ひとつずつでいい
ほどいていこう

[Chorus]
むりしないでいい
ゆっくりでいい
キミのゆびさき
ひかりをすくう
となりにいるよ
よあけまでいるよ

[Outro]
しずかなよる
キミとここに
まだおきてる
```

## ④手順
1. Suno（有料）で Style / Exclude / 歌詞を貼って生成
2. 良いテイクを選ぶ → Persona でボーカルをロック（以降のリリースで使い回す）
3. 曲（可能ならステムも）を `input/yofuke-no-tonari.wav`（or `input/yofuke-no-tonari_stems/`）に置く
4. `python scripts/run_audio.py --input input/yofuke-no-tonari.wav --name "夜更けのとなり"` で ⑤〜⑩

## ⑪ RouteNote メタデータ（リリース作成時）
- 曲名: 夜更けのとなり ／ アーティスト: Tonarine
- 配信日: 提出から2〜4週間先
- ℗ & © : (year) Tonarine
- 作詞: （生成AI関与を開示）／ 作曲: Suno + 本人
- ジャンル: Lo-Fi / Electronic（要確認）
- 明示的コンテンツ: No
- AI開示: あり。使用プラットフォーム = Suno（https://suno.com）。商用利用権を保有（有料プラン）
- ジャケット: 3000×3000px JPG / RGB / 25MB未満（アートディレクション未定）
- 注意: AI楽曲は YouTube Content ID 対象外
