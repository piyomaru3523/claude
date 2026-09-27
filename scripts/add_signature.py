"""ジャケット背景画像に Tonarine のサイン（署名）を合成する。
branding.md の仕様: Sacramento フォント、高さ約135px（3000px基準）、
色 #F2C88C、不透明度80%、右下に約130pxインセット。
"""
import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
FONT_PATH = ROOT / "covers" / "fonts" / "Sacramento-Regular.ttf"

SIGNATURE_TEXT = "Tonarine"
SIGNATURE_COLOR = (0xF2, 0xC8, 0x8C)
SIGNATURE_OPACITY = 0.80
SIGNATURE_HEIGHT_RATIO = 135 / 3000
INSET_RATIO = 130 / 3000
CANVAS_SIZE = 3000


def add_signature(input_path: Path, output_path: Path) -> None:
    img = Image.open(input_path).convert("RGB")
    if img.size != (CANVAS_SIZE, CANVAS_SIZE):
        img = img.resize((CANVAS_SIZE, CANVAS_SIZE), Image.LANCZOS)

    target_h = int(CANVAS_SIZE * SIGNATURE_HEIGHT_RATIO)
    inset = int(CANVAS_SIZE * INSET_RATIO)

    # フォントサイズをキャップハイト基準で目標高さに合わせる（反復調整）
    font_size = target_h
    font = ImageFont.truetype(str(FONT_PATH), font_size)
    bbox = font.getbbox(SIGNATURE_TEXT)
    text_h = bbox[3] - bbox[1]
    if text_h > 0:
        font_size = int(font_size * target_h / text_h)
        font = ImageFont.truetype(str(FONT_PATH), font_size)
        bbox = font.getbbox(SIGNATURE_TEXT)

    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]

    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    x = CANVAS_SIZE - inset - text_w - bbox[0]
    y = CANVAS_SIZE - inset - text_h - bbox[1]
    alpha = int(255 * SIGNATURE_OPACITY)
    draw.text((x, y), SIGNATURE_TEXT, font=font, fill=(*SIGNATURE_COLOR, alpha))

    composited = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    composited.save(output_path, "JPEG", quality=95)
    print(f"font_size={font_size}px  text_w={text_w}px  -> {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    add_signature(args.input, args.output)
