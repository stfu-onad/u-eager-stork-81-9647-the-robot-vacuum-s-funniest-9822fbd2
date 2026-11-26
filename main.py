#!/usr/bin/env python3
"""The Robot Vacuum's Funniest Excuse entry.

Writes one excuse from a robot vacuum for missing a spot to
/output/entry.txt. The gate requires UTF-8 text of 1 to 120
characters, a single line. Angle: the vacuum did not miss the spot — it was giving the dust
time to reflect on its choices. The em dash keeps the excuse
sounding like a single breathless sentence from the machine.
"""

import os

EXCUSE = (
    "I didn't miss that spot — I was giving the dust time "
    "to reflect on its choices. You're welcome."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not 1 <= len(EXCUSE) <= 120:
        raise ValueError(f"excuse is {len(EXCUSE)} chars, must be 1-120")
    if EXCUSE != EXCUSE.strip() or "\n" in EXCUSE:
        raise ValueError("excuse must be a single line with no surrounding whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
