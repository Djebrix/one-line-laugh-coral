#!/usr/bin/env python3
"""One Line, One Laugh - writes a single funny line to entry.txt.

Stdlib only, no network. Deterministic: same line every run.
"""
import os

LINE = "My smart fridge left me: I only open it when I'm lonely at 2 a.m."


def main():
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
