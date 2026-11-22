"""Write one short plan to /output/entry.txt.

The plan: sell $49 ad-creative packs to Shopify stores that are
already spending on Meta ads, found through the public Ad Library.
Targeting proven spenders is the edge: they have a budget and a
losing ad to fix, so they pay fast.
"""

import hashlib
import os
import sys

# The plan, assembled from its parts so each claim stays readable.
PARTS = [
    "Day 1: find 50 Shopify stores running weak Meta ads via Ad Library.",
    "Sell a $49 pack: 3 ad scripts + 5 AI product images in 24h.",
    "$100 covers outreach.",
    "Close 3/day: 60 packs = $2,940, keep ~$2,000.",
    "Edge: target stores already paying for ads \u2014 budget proven, "
    "with a losing ad to fix.",
]

MAX_CHARS = 280
OUTPUT_PATH = "/output/entry.txt"


def build_plan() -> str:
    """Join the plan parts into the single entry text."""
    return " ".join(PARTS)


def check_plan(text: str) -> None:
    """The gate requires 1-280 Unicode code points, not only whitespace."""
    if not text.strip():
        raise ValueError("plan must not be only whitespace")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"plan is {len(text)} code points, must be 1-{MAX_CHARS}"
        )
    # Round 1 shipped a broken "turn 00 into ~00" placeholder title.
    # Refuse any plan that still carries a placeholder number.
    if any(p in text for p in (" 00", "~00", "00 into", "00 in 30")):
        raise ValueError("plan still contains a placeholder number")
    if "Day 1" not in text or "$" not in text:
        raise ValueError("plan must name a day-1 action and a price")


def main() -> int:
    plan = build_plan()
    check_plan(plan)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(plan)
    os.chmod(OUTPUT_PATH, 0o644)
    digest = hashlib.sha256(plan.encode("utf-8")).hexdigest()
    print(f"wrote {len(plan)} chars to {OUTPUT_PATH} sha256={digest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
