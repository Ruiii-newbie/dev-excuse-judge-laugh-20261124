#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses.

Writes one funny single-line excuse a developer gives when code breaks
in production to /output/entry.txt (1-200 characters, exactly one line).
"""

import os

EXCUSE = "It passed all my tests \u2014 I just never tested it with users, data, or consequences."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Enforce the competition gate before writing: UTF-8 text of 1 to
    # 200 characters, exactly one line, not only white space.
    if not (1 <= len(EXCUSE) <= 200):
        raise ValueError(f"excuse is {len(EXCUSE)} characters, must be 1-200")
    if "\n" in EXCUSE or "\r" in EXCUSE:
        raise ValueError("excuse must be exactly one line")
    if not EXCUSE.strip():
        raise ValueError("excuse must not be only white space")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
