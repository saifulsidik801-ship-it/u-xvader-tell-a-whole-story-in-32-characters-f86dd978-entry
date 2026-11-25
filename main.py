#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters — make.fun entry.

Writes a single Wi-Fi network name (32 characters or fewer) to
/output/entry.txt. The name must land a joke and imply a whole story
in the few words a passer-by sees in a phone's network list.

The entry: a household confession as a network name. Dad found the
search history — the reader instantly pictures the kid, the awkward
conversation, and the grounded aftermath. Character, situation and
event, in 27 characters.
"""

import os

ENTRY = "Dad Found My Search History"


def main() -> None:
    assert 1 <= len(ENTRY) <= 32, f"entry is {len(ENTRY)} chars, must be 1-32"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)  # no trailing newline: the 32-char cap is hard


if __name__ == "__main__":
    main()
