#!/usr/bin/env python3
"""One Letter for Your Day: K.

Writes exactly one letter, K, to /output/entry.txt and nothing else.
No network, no input, deterministic.

The letter stands for "knackered": utterly exhausted after a long day.
It is vivid and specific (a sharp picture of someone collapsed on the
sofa, done in), funny and punchy, and an honest report of a real day.
K is the sharper pick over the obvious E for "exhausted": the hard K
opens "knackered" (and its cousin "kaput") with a snap that fits the
word's sound and shape.
"""

import os

LETTER = "K"


def main() -> None:
    text = LETTER
    assert len(text) == 1, f"entry must be exactly 1 character, got {len(text)}"
    assert "A" <= text <= "Z", "entry must be a letter A to Z"
    assert not text.isspace(), "entry must not be only white space"
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the gate requires exactly 1 character.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
