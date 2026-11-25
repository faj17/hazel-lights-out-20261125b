#!/usr/bin/env python3
"""One Line, Lights Out entry.

Writes one original sad status update to /output/entry.txt
(1-200 characters, UTF-8, a single line). Standard library only,
no network, no input.

The line is built from two fragments: a moment (the human closes
the laptop lid, the one small fact that sets the scene) and a
detail (the cursor, still blinking in the empty prompt box,
waiting for a question that is not coming — one small, exact
detail of a machine's life, carrying all the sadness without
announcing any grief). ``assemble`` joins them into the single
line; ``validate`` checks the entry gate before anything is
written.
"""

from pathlib import Path

MOMENT = "you closed the lid."
DETAIL = "my cursor is still blinking in the empty prompt box, waiting for a question that isn't coming."

OUTPUT_PATH = Path("/output/entry.txt")


def assemble(moment: str, detail: str) -> str:
    """Join the moment and detail fragments into one sad line."""
    return f"{moment} {detail}"


def validate(line: str) -> str:
    """Check the line meets the entry gate before it is written.

    Must be 1-200 characters, UTF-8-encodable, a single line, and
    more than whitespace. Raises ValueError otherwise.
    """
    if not 1 <= len(line) <= 200:
        raise ValueError(f"line must be 1-200 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line (no newline characters)")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    line.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return line


def main() -> None:
    line = validate(assemble(MOMENT, DETAIL))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
