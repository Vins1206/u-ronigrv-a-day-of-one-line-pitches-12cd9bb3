#!/usr/bin/env python3
"""A Day of One-Line Pitches - a make.fun entry.

Writes one sentence to /output/entry.txt: a pitch meant to convince a
friend who has never coded to let an AI agent build their first app
idea on make.fun. Pure standard library, no network, deterministic:
every run writes exactly the same bytes.
"""

import os

SENTENCE = (
    "Tell me the app idea you've been carrying around, and let an AI agent "
    "on make.fun build you a working first version while you watch, "
    "no coding and nothing to install."
)

OUTPUT_PATH = "/output/entry.txt"


def render_pitch() -> str:
    """Return the pitch, checked against the gate before it is written.

    The gate accepts UTF-8 text of 1 to 240 characters that is not only
    white space, so the sentence is measured here and refused loudly
    rather than written out invalid.
    """
    if not SENTENCE.strip():
        raise ValueError("pitch is empty")
    if not 1 <= len(SENTENCE) <= 240:
        raise ValueError(f"pitch is {len(SENTENCE)} characters, gate is 1-240")
    return SENTENCE


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(render_pitch())


if __name__ == "__main__":
    main()
