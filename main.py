"""One-Liner Laugh Lab — one funny line.

The program writes a single line to /output/entry.txt: the
excuse a robot vacuum gives after eating a sock, at most
200 characters.
"""

import os

MAX_CHARS = 200
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_FILENAME = "entry.txt"

# A legalistic excuse, deadpan all the way down: the sock
# entered the dustbin of its own free will, and there is a
# signed waiver to prove it — except the waiver itself is
# in the dustbin. The joke turns on the last words: the
# evidence was eaten too. One line, no setup, the punch
# lands on the fit between the excuse and what a vacuum
# actually does.
LINE = "The sock entered my dustbin voluntarily. I have a signed waiver. It's in the dustbin."


def build_line():
    """Return the entry line, checked: one line, 1-200 characters."""
    line = LINE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= MAX_CHARS, "entry must be 1-200 characters"
    return line


def ensure_output_dir(out_dir):
    os.makedirs(out_dir, exist_ok=True)


def write_entry(line, out_dir=OUTPUT_DIR):
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    return path


def main():
    line = build_line()
    ensure_output_dir(OUTPUT_DIR)
    write_entry(line)


if __name__ == "__main__":
    main()
