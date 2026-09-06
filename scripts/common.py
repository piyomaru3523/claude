"""スクリプト共通のヘルパー。"""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

# Windows のコンソール(cp932)でも日本語・記号を化けさせず出力する
for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

AUDIO_EXTS = {".wav", ".flac", ".mp3", ".aiff", ".aif", ".ogg", ".m4a"}


def log(msg: str) -> None:
    print(f"  {msg}", flush=True)


def step(msg: str) -> None:
    print(f"\n=== {msg} ===", flush=True)


def die(msg: str, code: int = 1) -> "None":
    print(f"ERROR: {msg}", file=sys.stderr, flush=True)
    raise SystemExit(code)


def ffmpeg_bin(name: str = "ffmpeg") -> str:
    """ffmpeg / ffprobe の実行パスを返す。PATH 優先、無ければ die。"""
    found = shutil.which(name)
    if not found:
        die(f"{name} が見つかりません。PATH を確認してください。")
    return found


def run(cmd: list[str], **kw) -> subprocess.CompletedProcess:
    """コマンドを実行し、失敗時は stderr を表示して die。"""
    proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", **kw)
    if proc.returncode != 0:
        sys.stderr.write(proc.stdout or "")
        sys.stderr.write(proc.stderr or "")
        die(f"コマンド失敗 (exit {proc.returncode}): {' '.join(cmd[:3])} ...")
    return proc


def find_audio(path: Path) -> list[Path]:
    """ファイルならそれ自身、ディレクトリなら直下の音声ファイル一覧を返す。"""
    if path.is_file():
        return [path]
    if path.is_dir():
        return sorted(p for p in path.iterdir() if p.suffix.lower() in AUDIO_EXTS)
    die(f"入力が見つかりません: {path}")
    return []


def ffprobe_json(src: Path) -> dict:
    import json

    proc = run([
        ffmpeg_bin("ffprobe"), "-v", "quiet", "-print_format", "json",
        "-show_format", "-show_streams", str(src),
    ])
    return json.loads(proc.stdout)
