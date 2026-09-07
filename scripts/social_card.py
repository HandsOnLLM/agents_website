"""Render the 1200x630 social card used in link previews.

Zensical can generate social cards per page, but the one that matters most is
the site-wide card people see when the book is shared on LinkedIn or X, so it
is drawn here from the real cover and checked in.

    uv run python scripts/social_card.py
"""

from __future__ import annotations

import pathlib
import sys

from PIL import Image, ImageDraw, ImageFont

ROOT = pathlib.Path(__file__).resolve().parent.parent
COVER = ROOT / "art" / "cover.jpg"
OUT = ROOT / "docs" / "images" / "social-card.png"

W, H = 1200, 630
PAD = 64

# Sampled from docs/stylesheets/theme.css — keep in step with --ag-* tokens.
INK = (12, 18, 27)
INK_SOFT = (176, 191, 208)
DOLPHIN = (127, 178, 226)
AGENT = (217, 162, 212)
RULE = (38, 49, 63)

# Windows ships these; fall back to Pillow's default if absent.
FONT_CANDIDATES = {
    "bold": ["C:/Windows/Fonts/segoeuib.ttf", "/System/Library/Fonts/Supplemental/Arial Bold.ttf"],
    "regular": ["C:/Windows/Fonts/segoeui.ttf", "/System/Library/Fonts/Supplemental/Arial.ttf"],
    "mono": ["C:/Windows/Fonts/consola.ttf", "/System/Library/Fonts/Menlo.ttc"],
}


def font(kind: str, size: int) -> ImageFont.FreeTypeFont:
    for path in FONT_CANDIDATES[kind]:
        if pathlib.Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default(size)


def main() -> int:
    if not COVER.exists():
        print(f"missing cover: {COVER}", file=sys.stderr)
        return 1

    card = Image.new("RGB", (W, H), INK)
    draw = ImageDraw.Draw(card)

    # Cover on the right, full-bleed to the top and bottom padding.
    with Image.open(COVER) as cover:
        cover = cover.convert("RGB")
        target_h = H - PAD * 2
        target_w = round(cover.width * target_h / cover.height)
        cover = cover.resize((target_w, target_h), Image.LANCZOS)
        cover_x = W - PAD - target_w
        card.paste(cover, (cover_x, PAD))

    text_right = cover_x - 48
    x = PAD

    # Eyebrow
    f_eyebrow = font("mono", 20)
    draw.text((x, PAD + 6), "300+ CUSTOM ILLUSTRATIONS", font=f_eyebrow, fill=DOLPHIN)

    # Title
    f_title = font("bold", 62)
    y = PAD + 58
    for line, colour in (
        ("An Illustrated", (232, 239, 247)),
        ("Guide to", (232, 239, 247)),
        ("AI Agents", DOLPHIN),
    ):
        draw.text((x, y), line, font=f_title, fill=colour)
        y += 70

    # Rule
    y += 18
    draw.line([(x, y), (min(x + 300, text_right), y)], fill=RULE, width=2)
    y += 26

    # Standfirst
    f_body = font("regular", 27)
    for line in ("Explore the fundamentals", "of AI agents!"):
        draw.text((x, y), line, font=f_body, fill=INK_SOFT)
        y += 36

    # Byline, pinned to the bottom
    f_by = font("regular", 23)
    draw.text((x, H - PAD - 30), "Maarten Grootendorst  &  Jay Alammar", font=f_by, fill=AGENT)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    card.save(OUT, "PNG", optimize=True)
    print(f"wrote {OUT.relative_to(ROOT)}  ({OUT.stat().st_size / 1024:.0f} KB, {W}x{H})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
