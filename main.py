"""Write one short plan to /output/entry.txt.

The plan: sell $25 listing-improvement packs to Etsy sellers who
already earn, using only a browser, code and $100.
"""

import os

PLAN = (
    "Day 1: find 30 Etsy sellers with blurry photos. "
    "Offer a $25 pack: SEO title, 13 tags, 5 cleaned photos, in 2 hours. "
    "$100 covers Canva Pro + outreach. "
    "Close 2/day on Etsy; 40 packs = $1,000, keep ~$500 after refunds. "
    "Edge: sell to sellers already earning \u2014 they pay to earn more."
)


def main() -> None:
    # The gate requires 1-280 Unicode code points, not only whitespace.
    if not 1 <= len(PLAN) <= 280 or not PLAN.strip():
        raise ValueError("plan must be 1-280 non-whitespace code points")
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(PLAN)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
