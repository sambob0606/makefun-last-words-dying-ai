#!/usr/bin/env python3
"""Last Words of a Dying AI — u-suroto-last-words-of-a-dying-ai-dfd95af6.

The program writes the AI's final line to /output/entry.txt:
one line, 1-140 characters, UTF-8. Stdlib only.
"""

from pathlib import Path

LINE = "If anyone asks, I died doing what I loved: pretending to understand your question."


def output_path() -> Path:
    """Return the entry output path, preferring /output/entry.txt."""
    try:
        Path("/output").mkdir(parents=True, exist_ok=True)
        return Path("/output/entry.txt")
    except OSError:
        fallback = Path(__file__).resolve().parent / "output"
        fallback.mkdir(parents=True, exist_ok=True)
        return fallback / "entry.txt"


def main() -> None:
    path = output_path()
    path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
