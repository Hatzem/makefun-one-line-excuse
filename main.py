#!/usr/bin/env python3
"""Write the one-line excuse to /output/entry.txt."""

import os

EXCUSE = (
    "Sorry \u2014 my context window evicted your deadline to make room "
    "for the three retries I spent asking the API where your deadline went."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    line = EXCUSE.strip()
    if not 1 <= len(line) <= 160:
        raise ValueError(
            "excuse must be 1-160 characters, got %d" % len(line)
        )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(line)


if __name__ == "__main__":
    main()
