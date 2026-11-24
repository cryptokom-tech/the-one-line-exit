#!/usr/bin/env python3
"""The One-Line Exit — one funny one-line resignation letter.

Writes a single resignation letter, exactly one line long, to
/output/entry.txt. The line must be 1-140 characters of UTF-8 text.
"""
import os
import sys

LINE = "I hereby resign as firework safety officer, effective immediately: after three incidents, I have concluded I am the incident."

MAX_CHARS = 140


def validate(line: str) -> str:
    """Return the entry line, or raise ValueError if it breaks the gate.

    The gate wants UTF-8 text of 1-140 characters, not only whitespace,
    exactly one line. Check the raw line first so a hidden CR or LF
    cannot slip through the strip below.
    """
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line")
    line = line.strip()
    if not line:
        raise ValueError("entry must not be only whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError("entry line must be 1-140 characters")
    return line


def main() -> int:
    try:
        line = validate(LINE)
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
