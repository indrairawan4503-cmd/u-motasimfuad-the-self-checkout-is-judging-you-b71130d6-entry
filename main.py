#!/usr/bin/env python3
"""The Self-Checkout Is Judging You — variant A (twelve-yoghurts shopper).

Writes one funny line in the voice of a judgmental self-checkout machine
to /output/entry.txt. Deterministic, no network, no model calls.
"""

import os

TEXT = (
    "Twelve yoghurts, no spoon, no dignity. I have already lived your whole "
    "week for you: yoghurt for breakfast, yoghurt for dinner, and a small "
    "cry in aisle four on Thursday. Bag your shame carefully."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    # Any copy to the repo root must never crash the run: the grader mounts
    # the repo read-only, so this is guarded.
    try:
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(TEXT)
    except OSError:
        pass


if __name__ == "__main__":
    main()
