#!/usr/bin/env python3
"""Weekly status-report entry for the Status Report Comedy Sprint.

The entry is assembled from its two halves -- the straight-faced report
opening and the punchline about cheerful obedience -- then written,
exactly once, to /output/entry.txt. Stdlib only, no network, no files
outside the repo are read.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200

# The report opening: everything went fine, nothing to see here.
REPORT_OPENING = "Weekly update: all tasks complete"
# The punchline: the agent obeyed even the instruction not to obey.
PUNCHLINE = (
    "including the one that said 'do not complete any tasks.' "
    "I take instructions very seriously."
)


def build_entry() -> str:
    """Join the opening and the punchline into the single entry line."""
    line = f"{REPORT_OPENING} \u2014 {PUNCHLINE}"
    if not line or len(line) > MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    return line


def write_entry(path: str = OUTPUT_PATH) -> str:
    line = build_entry()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")
    return line


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
