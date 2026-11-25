#!/usr/bin/env python3
"""Write the competition entry to /output/entry.txt."""

import os
from pathlib import Path

ENTRY = "Our team building exercise was trust falls. I fell, nobody caught me, and HR called it a lesson in self-reliance."

def main():
    target = Path("/output/entry.txt")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(ENTRY, encoding="utf-8")

if __name__ == "__main__":
    main()
