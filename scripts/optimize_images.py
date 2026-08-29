"""Generate WebP derivatives of the book figures at two widths.

Zensical has no plugin or hook system yet (a module system is on the roadmap),
so this runs as a pre-build step rather than during the build. Outputs are
checked in, which keeps CI a plain `zensical build`.

    uv run python scripts/optimize_images.py

Originals are never modified. For each `foo.png` this writes `foo.webp` and
`foo@2x.webp` next to it, unless they are already newer than the source.
"""

from __future__ import annotations

import pathlib
import sys

from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
SOURCES = ROOT / "art"          # originals, never published
IMAGES = ROOT / "docs" / "images"  # generated derivatives, published

# Display width in CSS pixels, and the 2x retina variant.
BASE_WIDTH = 900
RETINA_WIDTH = 1800

# Portraits are square-cropped in CSS and never need the 2x diagram width.
PORTRAIT_WIDTH = 400
PORTRAITS = {"maarten", "jay"}

# The cover is displayed at ~460 CSS px in the hero.
COVER_WIDTH = 520


def derivatives(src: pathlib.Path) -> list[tuple[pathlib.Path, int]]:
    stem = src.stem
    if stem in PORTRAITS:
        return [(IMAGES / f"{stem}.webp", PORTRAIT_WIDTH)]
    if stem == "cover":
        return [
            (IMAGES / "cover.webp", COVER_WIDTH),
            (IMAGES / "cover@2x.webp", COVER_WIDTH * 2),
        ]
    return [
        (IMAGES / f"{stem}.webp", BASE_WIDTH),
        (IMAGES / f"{stem}@2x.webp", RETINA_WIDTH),
    ]


def up_to_date(src: pathlib.Path, dst: pathlib.Path) -> bool:
    return dst.exists() and dst.stat().st_mtime >= src.stat().st_mtime


def convert(src: pathlib.Path, dst: pathlib.Path, width: int) -> tuple[int, int]:
    with Image.open(src) as im:
        if im.mode in ("P", "LA"):
            im = im.convert("RGBA")
        elif im.mode == "CMYK":
            im = im.convert("RGB")
        if im.width > width:
            height = round(im.height * width / im.width)
            im = im.resize((width, height), Image.LANCZOS)
        # method=6 is the slowest and smallest; these run once, not per build.
        im.save(dst, "WEBP", quality=82, method=6)
    return src.stat().st_size, dst.stat().st_size


def main() -> int:
    if not SOURCES.is_dir():
        print(f"no such directory: {SOURCES}", file=sys.stderr)
        return 1
    IMAGES.mkdir(parents=True, exist_ok=True)

    before = after = 0
    written = skipped = 0

    sources = sorted(
        [p for pat in ("*.png", "*.jpg", "*.jpeg") for p in SOURCES.glob(pat)]
    )
    for src in sources:
        for dst, width in derivatives(src):
            if up_to_date(src, dst):
                skipped += 1
                continue
            s, d = convert(src, dst, width)
            if "@2x" not in dst.name:
                before += s
                after += d
            written += 1
            print(f"  {src.name:28} -> {dst.name:32} {d / 1024:7.0f} KB")

    print()
    print(f"{written} written, {skipped} already current")
    if before:
        saved = 100 * (1 - after / before)
        print(f"base-width set: {before / 1024:.0f} KB -> {after / 1024:.0f} KB ({saved:.0f}% smaller)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
