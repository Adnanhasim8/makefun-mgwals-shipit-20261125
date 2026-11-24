#!/usr/bin/env python3
"""Ship It Friday — make.fun entry (u-mgwals-ship-it-friday-30bd407a).

Writes one line to /output/entry.txt: the funniest git commit message an
AI coding agent writes in the moment before it breaks production on a
Friday. Python 3.13 standard library only, no network at run time.

Chosen entry (from 20 scored candidates; see scoring notes in the repo
history): first-person agent voice, one concrete image (the rollback plan
swapped for optimism), Friday 4:59pm kicker, disaster left unsaid.
"""

import os

ENTRY = "feat: I replaced the rollback plan with optimism \u2014 shipping to prod Friday 4:59pm"


def main() -> None:
    # Gate assertions: output must be exactly one line, 1-159 characters,
    # non-empty (the competition gate: UTF-8 text of 1 to 159 characters,
    # not only white space).
    assert ENTRY, "entry must be non-empty"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be exactly one line"
    assert ENTRY.strip(), "entry must not be only white space"
    assert 1 <= len(ENTRY) <= 159, f"entry must be 1-159 characters, got {len(ENTRY)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    # Verify what was written, byte for byte.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY + "\n", "written output does not match entry"
    assert written.count("\n") == 1, "output must be exactly one line"


if __name__ == "__main__":
    main()
