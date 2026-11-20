"""news-image-20261120 entry: write the repo's entry.png to the output dir.

The image is the finished 1024x1024 front page (HTML/CSS/SVG drawn in
poster.html and rendered to PNG with headless Chromium): 41 verified
stories from Friday 20 November 2026 — 11 illustrated lead stories, a
dotted world map, four stat boxes and a date-check strip. main.py only
copies those bytes, after checking the PNG signature, dimensions and size,
so every run writes the same bytes. No network, standard library only.
"""

import os
import shutil
import struct
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024
MAX_BYTES = 1_048_576


def _check_png(data: bytes) -> None:
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise SystemExit("entry.png is not a PNG file")
    if len(data) < 33 or data[12:16] != b"IHDR":
        raise SystemExit("entry.png has no IHDR chunk")
    width, height = struct.unpack(">II", data[16:24])
    if (width, height) != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        raise SystemExit(f"entry.png is {width}x{height}, expected 1024x1024")
    if len(data) > MAX_BYTES:
        raise SystemExit(f"entry.png is {len(data)} bytes, over the 1 MiB limit")


def main() -> None:
    if not SRC.is_file():
        raise SystemExit(f"missing image next to main.py: {SRC}")
    data = SRC.read_bytes()
    _check_png(data)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / "entry.png"
    shutil.copyfile(SRC, out)
    if out.read_bytes() != data:
        raise SystemExit("output does not match entry.png")


if __name__ == "__main__":
    main()
