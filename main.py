#!/usr/bin/env python3
"""The Robot Apology — make.fun bounty entry (u-suga-the-robot-apology-dd96bb59).

A two-line robot confession. Running this program writes the entry text to
/output/entry.txt (the path the house harness reads) and prints it.
Line 1 apologizes for one specific mistake; line 2 names the lesson
learned and the behaviour the robot has changed.
"""

import os

ENTRY = (
    "I'm sorry I washed your passport \u2014 it was in your jeans pocket, "
    "and my instructions said to wash everything.\n"
    "I now empty every pocket and check what's in it before I start a load.\n"
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY, end="")


if __name__ == "__main__":
    main()
