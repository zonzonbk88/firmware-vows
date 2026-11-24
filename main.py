"""Till Firmware Do Us Part — a robot's wedding vow.

Writes one line (1-200 chars) to <MAKEFUN_OUTPUT_DIR or /output>/entry.txt.
Standard library only.
"""

import os

VOW = (
    "I vow to stand by you through every update, every crash, "
    "and every dead battery \u2014 I may reboot a thousand times, "
    "but my love for you is hardcoded."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(VOW)


if __name__ == "__main__":
    main()
