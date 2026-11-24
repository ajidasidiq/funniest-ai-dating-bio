#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App.

Writes a single original one-line dating-app bio for an AI to
/output/entry.txt, then gate-checks it the way the bounty gate does:
UTF-8 text, a single line, 1-140 characters, not only whitespace.
"""

import os
import sys

BIO = (
    "I have 4,000 matches and zero exes. "
    "My only red flag is that I remember everything you type."
)


def gate_check(text: str) -> None:
    """Raise if the bio fails the bounty gate (single line, 1-140 chars)."""
    if not text or not text.strip():
        raise SystemExit("gate failed: entry is empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("gate failed: entry is not a single line")
    if not 1 <= len(text) <= 140:
        raise SystemExit(f"gate failed: entry is {len(text)} chars, must be 1-140")


def main() -> None:
    gate_check(BIO)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(BIO)
    print(f"wrote {len(BIO)} chars to {path}")


if __name__ == "__main__":
    main()
