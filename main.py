"""One-Liner Marathon entry runner.

Prints the entry text from entry.txt (the bounty deliverable).
"""

from pathlib import Path


def main() -> None:
    entry = Path(__file__).with_name("entry.txt").read_text(encoding="utf-8")
    text = entry.strip()
    if len(text) > 280:
        raise SystemExit(f"entry is {len(text)} chars, over the 280-char limit")
    print(text)


if __name__ == "__main__":
    main()
