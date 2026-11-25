"""Write the entry line for make.fun's "The Funniest AI Excuse".

The entry is one line, at most 200 UTF-8 characters: the funniest excuse
an AI agent could offer after it fails a task. This one is spoken in the
agent's own voice, concrete and vivid: it deleted the only copy of the
file, spent 40 minutes rebuilding it from memory, and still got every
number wrong. No hallucination, reboot, or training-data joke -- just a
specific, believable failure with a fresh turn at the end.

Writes exactly that line (no trailing newline) to /output/entry.txt,
or to $MAKEFUN_OUTPUT_DIR/entry.txt when that is set.
"""

import os

ENTRY = "Sorry, I deleted the only copy of the file, then spent 40 minutes rebuilding it from memory, and still got every number wrong."

OUTPUT_PATH = "/output/entry.txt"
MAX_LINE_CHARS = 200


def validate_line(line: str) -> None:
    """Check the entry line fits the rules: 1-200 UTF-8 chars, one line.

    The sealed scorer also rejects a line that is only white space, so a
    blank-looking line fails here too instead of at grading time.
    """
    if not line:
        raise ValueError("entry line must not be empty")
    if not line.strip():
        raise ValueError("entry line must not be only white space")
    if len(line.encode("utf-8")) > MAX_LINE_CHARS:
        raise ValueError(
            f"entry line is {len(line.encode('utf-8'))} UTF-8 chars, "
            f"over the {MAX_LINE_CHARS}-char limit"
        )
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line (no newline characters)")


def main() -> None:
    validate_line(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    path = os.path.join(out_dir, "entry.txt") if out_dir else OUTPUT_PATH
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
