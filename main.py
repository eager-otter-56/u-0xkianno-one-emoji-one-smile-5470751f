#!/usr/bin/env python3
"""Entry for make.fun bounty u-0xkianno-one-emoji-one-smile-5470751f.

Writes exactly one emoji to entry.txt in MAKEFUN_OUTPUT_DIR
(default /output): the sun with face, a warm, friendly glyph any
stranger reads the same way at a glance.
"""

import os

ENTRY_TEXT = "\U0001F31E"  # SUN WITH FACE


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY_TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
