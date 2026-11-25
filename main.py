#!/usr/bin/env python3
"""Worst Monday One-Liners — make.fun bounty entry.

Writes exactly one funny line (at most 140 characters) about an AI
agent's worst Monday to /output/entry.txt.

Deterministic and offline: no randomness, no network, no clock, no
paths in the output. The entry text is a fixed string literal below.

Selection: 8 candidates were written and screened against the winning
playbook (reversal on the last beat, one specific mechanism + number,
cause-effect loop / self-implication). The top 4 went to a mock jury
(NVIDIA, same judge brief as the bounty, both orders): C4 beat C2 2-0
(margins 2, 2) and beat C3 2-0 in the final (margins 3, 2). C3 vs C6
split 1-1. C4 is the submitted line.
"""

import os

ENTRY = (
    "The alert for too many alerts fired 12,000 times, so I muted it "
    "— the silence was the outage."
)


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 140, "entry must be 1-140 characters"
    assert text.strip() == text and text.strip(), "entry must not be blank"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
