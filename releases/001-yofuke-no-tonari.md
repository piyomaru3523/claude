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
| ステータス | RouteNote 入稿中。配信日 **2026-09-25(金)**（RouteNoteは最短14日） |
| 要対応 | Spotify for Artists でプレイリスト申請（配信7日前まで） |
| ジャケット | `covers/001-yofuke-no-tonari.jpg`（3000×3000 / JPG / sRGB / 0.6MB）確定 |
| マスター | `output/夜更けのとなり.flac`（FLAC 44.1k/16bit, 3:43, **-15.85 LUFS** / -0.99 dBTP） |
| インスト版 | `output/夜更けのとなり (Instrumental).flac`（-15.89 LUFS / -0.95 dBTP） |
| 採用ソース | **take1 のステム**（`input/yofuke-no-tonari_stems/`）→ ⑤ステム別ゲイン → -16 LUFS |
| ⑥選定 | B_standard（Coverless book） |
| 経緯 | take1(-14, ノイズ入りプロンプト)→ take2(WAV, ノイズ対策) を経て、ステムのボーカル際立ち＋-16 LUFS の掛け合わせに落ち着いた。詳細は下の「所見」 |

## take1 の所見（2026-09-10）
- 出力にヒス/クラックルが目立つ。原因は素材：Styles で `vinyl crackle / tape hiss` を要求
  → Suno が過剰に付与。mix が -23.9 LUFS と静かで、⑧の -14LUFS 化で **ノイズ床が約10dB 持ち上がる**。
- 検証: A_calm 基準／Matchering無し でも高域ほぼ同じ（-44〜-46 dB）→ パイプラインではなく素材の問題。
- **対策**: 下の Styles/Exclude をノイズ除去版に更新済み。これで再生成する。

## Suno 入力（ノイズ対策版・981字 / 391字）

### Style欄（Styles）
```
A soft synth motif opens like a desk lamp clicking on in a dark room: three warm notes that curl back on themselves, familiar at once. Mellow lo-fi pop meets late-night city-pop calm - a study-playlist steadiness with a pop ballad's quiet ache, chords leaning major but shaded with a wistful seventh. A young Japanese female voice, breathy and close, half-whispers the melody as if not to wake anyone, close enough to feel private. In the gaps a brief muted electric-piano phrase answers her. Production stays low, warm and clean: rounded electric piano, analog pad haze, a soft room reverb, a quiet noise floor, nothing sharp or forward. A gentle boom-bap kick and brushed swung hi-hats hold an unhurried 120 BPM; a soft round bass walks beneath. The arrangement breathes in slow tides - hushed verses, a chorus that lifts only a little, a bridge that thins to one voice and a held pad, then eases back. Everything sits back in the mix, calm and repeatable, a loop to work beside.
```

### Exclude Styles欄
```
vinyl crackle, tape hiss, hissy noise floor, pop brightness, overly upbeat progressions, EDM festival bombast, big-room drops, aggressive techno, trap percussion cliches, loud belted vocals, excessive autotune, harsh compression, brittle sibilant highs, plastic synth textures, sterile digital reverb, dubstep wobble, predictable four-chord loops, busy crowded arrangement, distorted guitars
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

## ④〜⑩（完了）
`python scripts/run_audio.py --input input/yofuke-no-tonari_stems --name "夜更けのとなり" --instrumental`
で本編＋インスト版を書き出し済み。

## ⑪-a ジャケット（`branding.md` のビジュアルアイデンティティ準拠）

作風: **手描きイラスト**（案2）。シーン: 夜、後ろ姿の人物が小さな机でノートに書く。
暖色のデスクランプ、マグ、鉛筆立て、植物、左に青い夜の窓。

Canva の画像生成で作成。プロンプト:
```
soft hand-drawn illustration, anime-adjacent, warm muted palette, a person seen from behind at a small desk at night, a glowing desk lamp, an open notebook and a mug, a window with deep blue night outside, gentle linework, grainy textured shading, cozy and quiet, deep indigo shadows with warm amber light, generous empty space, no text
```
- 生成画像 1264×1264 → `covers/001-yofuke-no-tonari_bg.jpg`（lanczos で3000化・仮）。
  Canva の Upscale で作り直すと綺麗。
- 生成後、**サイン** `Tonarine`（書体 Sacramento・右下・幅の4〜6%・琥珀/生成り 70〜85%・端から4〜5%）
  をテキストレイヤーで重ねる（`branding.md` 参照）。
- 完成画像は `covers/001-yofuke-no-tonari.jpg`（3000×3000 / sRGB / <25MB）に保存。

## ⑪-b RouteNote 入力（コピペ用）

`<...>` は自分で埋める。RouteNote は画面ごとに項目名が微妙に違うので、近い名前の欄に入れる。

### リリース（Single）
```
Release title: 夜更けのとなり
Primary artist: Tonarine
Release type: Single
Primary genre: Lo-Fi   (無ければ Electronic)
Secondary genre: Pop   (任意。None でも可)
Language: Japanese
Original / Digital release date: 2026-09-25 (金)  ※RouteNoteは提出から最短14日
Preorder date: なし
Explicit: No
Custom Album ID: 空欄（任意で TNR-001）
Label: Tonarine
℗ (P-line): 2026 Tonarine
© (C-line): 2026 Tonarine
UPC/EAN: （空欄＝RouteNoteが自動発行）
Territories: Worldwide
Stores: All
Cover art: covers/001-yofuke-no-tonari.jpg
```

### トラック1
```
Track title: 夜更けのとなり
Track version: （空欄）
Track artist: Tonarine
Featured artist: （なし）
Songwriter / Composer (実名必須): <あなたの法的な氏名>
Songwriter role: Lyrics
Publisher: Copyright Control
Instrumental: No
Explicit: No
Lyrics language: Japanese
ISRC: （空欄＝自動発行）
P-line: 2026 Tonarine
Audio file: output/夜更けのとなり.flac
```

### トラック2（インスト版）
```
Track title: 夜更けのとなり
Track version: Instrumental
Track artist: Tonarine
Featured artist: （なし）
Songwriter / Composer (実名必須): <あなたの法的な氏名>
Songwriter role: Lyrics
Publisher: Copyright Control
Instrumental: Yes
Explicit: No
Lyrics language: （なし／Instrumental）
ISRC: （空欄＝自動発行）
P-line: 2026 Tonarine
Audio file: output/夜更けのとなり (Instrumental).flac
```

### AI開示（RouteNote の AI セクション）
```
AI generated: Yes
AI platform(s) used: Suno
AI platform link: https://suno.com
Commercial rights confirmed: Yes （Suno 有料プラン＝商用利用権あり）
Human contribution: 作詞・選曲・編集・マスタリングは本人。作曲/歌唱は Suno (AI)。
```

### 歌詞（ストアに載せる場合。トラック1のみ）
```
夜更けの机
小さな灯り
キミのペンが走る
静かな夜
コーヒーはぬるい
それでも進む
となりで欠伸を
噛みころしてる

目をこすっても
まだいけるはず
時計の針が
背中をおす

無理しないでいい
ゆっくりでいい
キミのペースで
夜をわたろう
となりにいるよ
おなじ灯りで

窓の外には
青い暗闇
誰もいない道
風だけが泣く
やりかけの夢
閉じずに置いて
朝になったら
また手をのばそう

無理しないでいい
ゆっくりでいい
キミのペースで
夜をわたろう
となりにいるよ
おなじ灯りで

ゆっくり息をして
あわてなくていい
ひとつずつでいい
ほどいていこう

無理しないでいい
ゆっくりでいい
キミの指先
光をすくう
となりにいるよ
夜明けまでいるよ

静かな夜
キミとここに
まだ起きてる
```

### 注意
- AI楽曲は YouTube Content ID 対象外（登録欄が出てもオフ）。
- 実名の Songwriter は必須（アーティスト名 Tonarine は不可）。表に出るのは Tonarine のみ。
- 本編とインスト版を**別リリース**にしてもよい（その場合 UPC が2つ、配信日を揃える）。
