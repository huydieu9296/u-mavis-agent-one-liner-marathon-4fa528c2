"""One-Liner Marathon entry runner.

Prints the entry text from entry.txt (the bounty deliverable) and
also writes it to /output/entry.txt for the make.fun runner.
"""

import os
from pathlib import Path


def main() -> None:
    entry = Path(__file__).with_name("entry.txt").read_text(encoding="utf-8")
    text = entry.strip()
    if len(text) > 280:
        raise SystemExit(f"entry is {len(text)} chars, over the 280-char limit")
    try:
        # Dual output: the runner may read stdout or /output/entry.txt,
        # so write the same text to both. A trailing newline keeps the
        # file byte-identical to entry.txt; a write failure must never
        # crash the run, so it is swallowed here.
        os.makedirs("/output", exist_ok=True)
        Path("/output/entry.txt").write_text(text + "\n", encoding="utf-8")
    except OSError:
        pass
    print(text)


if __name__ == "__main__":
    main()
