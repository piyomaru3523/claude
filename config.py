"""パイプライン全体の設定値。音楽的な判断が必要な値はここに集約してある。"""
from pathlib import Path

# ------------------------------------------------------------------
# パス
# ------------------------------------------------------------------
ROOT = Path(__file__).resolve().parent
INPUT_DIR = ROOT / "input"            # ④ Sunoからダウンロードした曲 / ステムを置く
WORK_DIR = ROOT / "work"              # 中間ファイル
OUTPUT_DIR = ROOT / "output"          # 最終成果物
REF_DIR = ROOT / "references"         # ⑥ リファレンス音源（バケット別）
REF_INDEX = REF_DIR / "references.json"  # analyze_references.py が生成する特徴量インデックス

for _d in (INPUT_DIR, WORK_DIR, OUTPUT_DIR):
    _d.mkdir(exist_ok=True)

# ------------------------------------------------------------------
# ⑥ リファレンスのムードバケット
#   analyze_references.py が各フォルダの音源を解析し REF_INDEX に特徴量を書き出す。
#   1バケットにつき wav/flac/mp3 を1曲以上入れておく（複数入れると平均を取る）。
# ------------------------------------------------------------------
BUCKETS = {
    "A_calm":     {"label": "落ち着き系",  "bpm_hint": 88},   # 〜95BPM  マイナー寄り・メロウ
    "B_standard": {"label": "標準系",      "bpm_hint": 108},  # 95〜120BPM 長調寄り・軽やか
    "C_drive":    {"label": "推進系",      "bpm_hint": 128},  # 120BPM〜 steady groove
}

# ⑥ マッチングの重み付け（合計1.0）。聴感上いちばん効くのがBPMなので最優先。
MATCH_WEIGHTS = {
    "bpm": 0.5,               # BPM一致度
    "spectral_centroid": 0.3,  # 明るさ（音の硬さ/柔らかさ）
    "rms": 0.2,              # エネルギー感
}

# ------------------------------------------------------------------
# ⑧ ⑨ マスタリング目標値（主要配信サービスで概ね安全な一般値）
# ------------------------------------------------------------------
TARGET_LUFS = -14.0          # 統合ラウドネス
TARGET_TP = -1.0             # True Peak 上限 (dBTP)
TARGET_LRA = 11.0            # ラウドネスレンジ（loudnorm 用の目安）

# ⑨ QC 許容誤差（測定値がこの範囲を外れたら ⑧ をリトライ）
QC_TOLERANCE_LUFS = 1.0      # ±1.0 LU
QC_TP_CEILING = -1.0         # これを超えたら不合格 (dBTP)
QC_MAX_RETRY = 3

# ------------------------------------------------------------------
# ⑩ 書き出しフォーマット
#   配信先は RouteNote 確定。要求は FLAC または MP3(320kbps)/16bit/44.1kHz。
#   WAV は不可。デフォルトは FLAC。
#   併せて output/masters/ に 24bit マスターも保存（アーカイブ用）。
# ------------------------------------------------------------------
EXPORT_PRESET = "flac"       # "flac" | "mp3_320" | "wav_24"(アーカイブ用途のみ)
EXPORT_PRESETS = {
    "flac":    {"ext": "flac", "codec": "flac",      "sample_rate": 44100, "sample_fmt": "s16"},
    "mp3_320": {"ext": "mp3",  "codec": "libmp3lame", "sample_rate": 44100, "bitrate": "320k"},
    "wav_24":  {"ext": "wav",  "codec": "pcm_s24le",  "sample_rate": 44100},
}
KEEP_24BIT_MASTER = True     # output/masters/ に 24bit マスターを別途残す

# ------------------------------------------------------------------
# ⑤ ステムのデフォルト処理（Suno のパート別ダウンロードを想定）
#   ファイル名にこのキーワードが含まれるステムに、対応するゲイン(dB)を適用。
#   小文字化して部分一致で判定。該当なしは 0dB。
# ------------------------------------------------------------------
STEM_GAIN_DB = {
    "vocal": -1.0,   # ボーカルは主張しすぎない（作業用BGM棚の趣旨）
    "voice": -1.0,
    "drum": -0.5,
    "bass": 0.0,
    "guitar": -1.5,
    "piano": -1.0,
    "synth": -1.5,
    "other": -1.5,
    "instrument": 0.0,
}
# ⑤ ミックスバス（ステム合算後）にかける軽い整音。控えめ固定。
MIX_BUS_HIGHPASS_HZ = 30
MIX_BUS_COMP = {"threshold_db": -18.0, "ratio": 1.8, "attack_ms": 15, "release_ms": 200}

# ------------------------------------------------------------------
# ③ 歌詞検証（仕様書の禁則ルール）
# ------------------------------------------------------------------
LYRICS_MAX_MORA_PER_LINE = 12       # 1行12モーラ超えを違反として検出
LYRICS_MAX_CONSECUTIVE_YOON = 2     # 拗音3連続以上を違反として検出（許容は2まで）
LYRICS_MAX_CONSECUTIVE_N_ENDING = 1  # 「ん」終わりが2行連続以上を違反として検出
LYRICS_MORA_TOLERANCE = 1           # --target 指定時、目標モーラ数に対する行ごと許容差
LYRICS_TARGET_DURATION_SEC = 170    # 尺の目安 2分50秒
LYRICS_SUBJECT = "キミ"             # 歌詞の主語（固定）
