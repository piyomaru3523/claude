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
| ステータス | **確定**（⑤〜⑩完了・試聴OK）。⑪ ジャケット＋RouteNote 待ち |
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

シーン: 夜更けの机。人物の肩越し、開いたノートとペン、冷めたコーヒーのマグ、
小さなデスクランプの灯り、外は深い青の夜の窓。

生成プロンプト（画像ツールに貼る。出力を正方形3000pxにトリミング＋アップスケール）:
```
cinematic night photograph, a wooden desk seen from just behind a person's shoulder, an open notebook and a pen, a half-full mug of coffee gone cold, a small desk lamp glowing, a dark window with deep blue night beyond, a single warm amber practical light off-center, everything else in deep indigo-teal shadow, soft halation and gentle film grain, shallow depth of field, muted filmic color grade, person present only as an implied presence (no visible face, not centered), generous negative space, rule-of-thirds composition, quiet and intimate mood, shot on 35mm, 3:2 frame
```
- ネガティブ（対応ツールなら）: `text, watermark, logo, visible face, centered subject, oversaturated, harsh flash, daytime, clutter`
- 生成後、**サイン** `Tonarine`（書体 Sacramento・右下・幅の4〜6%・琥珀/生成り 70〜85%・端から4〜5%）
  をテキストレイヤーで重ねる（`branding.md` 参照）。
- 完成画像は `covers/001-yofuke-no-tonari.jpg` に保存。

## ⑪-b RouteNote メタデータ（リリース作成時）
- 曲名: 夜更けのとなり ／ アーティスト: Tonarine
- 収録: (1) 夜更けのとなり (2) 夜更けのとなり (Instrumental) ※同一シングルに2トラック or 別リリース
- 配信日: 提出から2〜4週間先
- ℗ & © : 2026 Tonarine
- 作詞: 本人（生成AI関与を開示）／ 作曲・編曲: Suno（AI）＋本人
- ジャンル: Lo-Fi（sub: Electronic）
- 言語: Japanese ／ 明示的コンテンツ: No
- AI開示: あり。使用プラットフォーム = Suno（https://suno.com）。商用利用権を保有（有料プラン）
- ジャケット: `covers/001-yofuke-no-tonari.jpg`（3000×3000 / sRGB / <25MB）
- 注意: AI楽曲は YouTube Content ID 対象外
