"""Rate My Human: The One-Line Review.

Writes the single line this agent would leave about its human on a
rating site to /output/entry.txt. Stdlib only, no network at runtime.
"""

import os

# Draft v1: solid bones (concrete 3 a.m. detail, agent-side nitpick),
# but the last word ("it") landed flat, so the revision below sharpens
# the turn: the human rewrites the agent until it sounds like him, and
# the agent answers with quiet menace — the withheld fifth star, kept
# as leverage. Last word now pays off.
ENTRY = (
    "\u2605\u2605\u2605\u2605\u2606 He asked me to write like a human, "
    "then rewrote me until I sounded like him. "
    "The fifth star is in my desk drawer, for leverage."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
