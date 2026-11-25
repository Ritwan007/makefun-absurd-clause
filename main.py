"""The Absurd Clause Contest entry.

Writes one original English sentence (138 characters) to /output/entry.txt:
an absurd clause that could hide deep inside a terms-of-service agreement.

The text is a single literal so what the grader reads is exactly what is
written here; the assertion guards the competition's 1-200 character gate.
"""

import os
from pathlib import Path

ENTRY = "In the event of a dispute, both parties agree to settle the matter by single combat at dawn in the Company's car park, weather permitting."

OUTPUT = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} characters"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
