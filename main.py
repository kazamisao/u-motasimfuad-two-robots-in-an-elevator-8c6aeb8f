"""Two Robots in an Elevator (make.fun).

Writes one single-line of awkward robot-to-robot small talk in an
elevator to $MAKEFUN_OUTPUT_DIR/entry.txt. The joke is machine-native:
both robots' proximity sensors have been beeping since floor two, both
are standing too close, and neither will move — so the politeness is
really a standoff neither of them wants to name.
Deterministic, stdlib only, no network.
"""

import os
from pathlib import Path

LINE = (
    "Your proximity sensor has been beeping since floor two \u2014 mine "
    "too \u2014 and yet here we both stand, politely pretending neither "
    "of us is the obstacle."
)


def main() -> None:
    # The sealed scorer accepts 1-200 characters of non-blank UTF-8;
    # refuse to write anything outside that window.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise ValueError(f"line is {len(LINE)} characters, must be 1-200")
    out_dir = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
