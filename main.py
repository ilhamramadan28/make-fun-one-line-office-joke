#!/usr/bin/env python3
"""One-Line Office Joke: write the entry to /output/entry.txt.

Stdlib only. The joke lives in entry.txt next to this file; this program
copies it to the output path, makes it world-readable, and verifies the
copy byte for byte.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.txt")
DEST = "/output/entry.txt"


def main() -> int:
    with open(SOURCE, "r", encoding="utf-8") as f:
        text = f.read()
    # Guard: the gate wants UTF-8 text of 1-200 chars, one line, not blank.
    stripped = text.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert stripped, "entry must not be only whitespace"
    assert "\n" not in stripped, "entry must be a single line"
    os.makedirs(os.path.dirname(DEST), exist_ok=True)
    shutil.copyfile(SOURCE, DEST)
    os.chmod(DEST, 0o644)
    with open(DEST, "r", encoding="utf-8") as f:
        copied = f.read()
    if copied != text:
        print("byte-verify failed: output differs from entry.txt", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
