# ③ 歌詞生成 + 自動検証

## 入力
- `work/style_<日付>.md`（②で選んだ案）
- ①の共通特徴（歌詞の主語・語りかけの傾向）

## 手順
1. アシスタントが構成タグ付きで歌詞を生成する：
   - `[Intro] [Verse1] [PreChorus] [Chorus] [Verse2] [Bridge] [Chorus] [Outro]` など
   - 尺の目安 **2分50秒**（`config.LYRICS_TARGET_DURATION_SEC`）
   - 主語は **「キミ」** で固定（`config.LYRICS_SUBJECT`）
   - 各行に**かな読みを併記**（`表記 | かなよみ`）— モーラ検証の精度確保のため
   - `templates/lyrics.example.txt` の書式で `work/lyrics_<曲名>.txt` に保存
2. 自動検証を実行：
   ```
   python scripts/step3_validate_lyrics.py work/lyrics_<曲名>.txt --json work/lyrics_qc_<曲名>.json
   ```
   検出される禁則（`config.py` で調整可能）：
   - 1行 **12モーラ超え**
   - **拗音3連続**
   - **「ん」終わりが2行連続**
   - `--target targets.txt`（1行1整数）を渡すと、行ごとの目標モーラ数 ±1 のズレも検出
3. 違反行を修正して 2 を再実行。違反ゼロになったら④へ。

## 出力
- `work/lyrics_<曲名>.txt`（④で Suno の歌詞欄に貼る）
- `work/lyrics_qc_<曲名>.json`（検証ログ）
