# Billboard JAPAN → AI作曲（Suno）→ 簡易マスタリング パイプライン

Billboard JAPAN Hot 100 の**構造的特徴（著作権で保護されない要素のみ）**を分析し、
そこから Suno 用の作曲スタイル・歌詞を組み立て、生成した曲を無料ツールだけで
配信基準（RouteNote / 作業用BGM棚）に耐えるマスターに仕上げるまでを半自動化する。

設計の正本は `docs/pipeline_spec.md`。

## セットアップ（初回のみ）

前提（このPCは導入済み）: Python 3.12 / ffmpeg / git

```bash
cd C:\Users\User\claude_local\billboard-bgm-pipeline
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

リファレンス音源を用意（詳細は `references/README.md`）:
- `references/A_calm/` `references/B_standard/` `references/C_drive/` に正規音源を1曲ずつ
- `python scripts/analyze_references.py` を実行して `references.json` を生成

## 全体フロー

| 手動/自動 | ステップ | コマンド / 実施 |
|---|---|---|
| チャット | ① チャート分析 | `prompts/step1_chart_analysis.md` → `work/features_*.json` |
| チャット | ② Styleプロンプト3案 | `prompts/step2_style_prompt.md` → `work/style_*.md` |
| チャット+CLI | ③ 歌詞生成 + 検証 | `prompts/step3_lyrics.md` / `python scripts/step3_validate_lyrics.py work/lyrics_*.txt` |
| **手動** | ④ Suno 生成・DL | Style欄/歌詞欄に貼付 → 試聴 → 曲 or ステムを `input/` に保存 |
| 自動 | ⑤〜⑩ 一括 | `python scripts/run_audio.py --input input/<曲 or ステムdir> --name "<曲名>"` |
| **手動** | ⑪ 試聴 → アップロード | `output/*.flac` を確認 → RouteNote へ（AI開示・商用利用権の確認） |

### ⑤〜⑩ の内訳（`run_audio.py` が順に実行）
1. **⑤** ステムがあれば Pedalboard でゲイン/EQ調整しミックスダウン（`step5_mix_stems.py`）
2. **⑥** librosa で BPM・明るさ・エネルギーを解析し、3バケットから重み付き距離で
   リファレンスを自動選定（BPM 0.5 / 明るさ 0.3 / エネルギー 0.2、`step6_pick_reference.py`）
3. **⑦** Matchering で選定リファレンスに合わせてマスタリング（`step7_master_matchering.py`）
4. **⑧** ffmpeg loudnorm 2パスで −14 LUFS / −1 dBTP に調整（`step8_loudnorm.py`）
5. **⑨** pyloudnorm で測定・合否判定。不合格なら ⑧ を TP を引き締めてリトライ（`step9_qc.py`）
6. **⑩** RouteNote 向け FLAC 44.1kHz/16bit に書き出し。24bit マスターも `output/masters/` に保管（`step10_export.py`）

## 個別実行

```bash
python scripts/step3_validate_lyrics.py work/lyrics_song.txt --json work/lyrics_qc.json
python scripts/step5_mix_stems.py       --input input/song_stems --out work/song_mix.wav
python scripts/step6_pick_reference.py  --input work/song_mix.wav --json work/song_ref.json
python scripts/step7_master_matchering.py --input work/song_mix.wav --ref-json work/song_ref.json --out work/song_master.wav
python scripts/step8_loudnorm.py        --input work/song_master.wav --out work/song_ln.wav
python scripts/step9_qc.py              --input work/song_ln.wav --json work/song_qc.json
python scripts/step10_export.py         --input work/song_ln.wav --name "Focus Rain"
```

## 設定

音楽的な判断が要る値は `config.py` に集約:
目標ラウドネス / True Peak、⑥ の重み付け、③ の禁則しきい値、⑤ のステム別ゲイン、
⑩ の書き出しプリセットなど。

## 重要な制約（`docs/pipeline_spec.md` 参照）

- **Suno の自動アクセス禁止** — ④（プロンプト入力・生成・DL）は完全手動。Chrome 自動操作の対象外。
- **Billboard JAPAN のスクレイピングはしない** — ① はユーザーの手動コピー&貼付のみ。
- **Matchering のリファレンスは正規音源のみ** — チャート上位曲の実音源を取得して使わない。
- **RouteNote アップロード時は AI 関与を開示**（2026年改定ポリシーで必須）。Suno は商用利用権付きの
  有料プランであること。
