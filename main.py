"""Round 3 plan: sell thumbnail packs to small YouTubers.

The buyer: a channel with 5k-100k subscribers that still posts weekly
but averages views under 20% of its subscriber count. That gap is
visible from search results alone, so the pitch needs no insider
data. The deliverable is files (3 thumbnails + 3 titles in 24h), so
no account access, no platform approval, and nothing to wait on.
"""

import hashlib
import os
import sys

# Funnel inputs. Every figure below is a real input; nothing here is
# a placeholder, and the plan text is built from these numbers so the
# words can never drift away from the math.
OUTREACH_PER_DAY = 50   # channels contacted per day (business email
                        # on the channel About page, or a comment + DM)
DAYS = 30
REPLY_RATE = 0.10       # 1 in 10 replies
CLOSE_RATE = 0.40       # 2 in 5 replies buy
PRICE = 39              # dollars per pack
OUTREACH_BUDGET = 100   # dollars: email finder + inbox warm-up
FEE_RATE = 0.029        # payment-processor cut

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 280


def funnel():
    """Run the 30-day funnel and return every derived number."""
    contacts = OUTREACH_PER_DAY * DAYS
    replies = int(contacts * REPLY_RATE)
    sales = int(replies * CLOSE_RATE)
    revenue = sales * PRICE
    fees = round(revenue * FEE_RATE)
    net = revenue - OUTREACH_BUDGET - fees
    return contacts, replies, sales, revenue, fees, net


def build_plan(sales: int, revenue: int, net: int) -> str:
    """Assemble the entry text from the computed funnel numbers."""
    kept = (net // 10) * 10  # quote the kept cash rounded down to $10
    parts = [
        f"Day 1: find {OUTREACH_PER_DAY} YouTubers (5k-100k subs) "
        "with views under 20% of subs.",
        f"Sell a ${PRICE} pack: 3 thumbnails + 3 titles in 24h.",
        f"${OUTREACH_BUDGET} covers outreach.",
        f"Close 2/day: {sales} packs = ${revenue:,}, keep ~${kept:,}.",
        "Edge: weak thumbnails show in search \u2014 files only, "
        "no access needed.",
    ]
    return " ".join(parts)


def check_plan(text: str, revenue: int, sales: int, net: int) -> None:
    """Gate: 1-280 code points, real numbers only, day-1 action + price."""
    if not text.strip():
        raise ValueError("plan must not be only whitespace")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"plan is {len(text)} code points, must be 1-{MAX_CHARS}"
        )
    banned = ("TBD", "XXX", "placeholder", " 00", "~00", "00 into")
    for token in banned:
        if token in text:
            raise ValueError(f"plan contains placeholder token {token!r}")
    if "Day 1" not in text or "$" not in text:
        raise ValueError("plan must name a day-1 action and a price")
    if f"${revenue:,}" not in text:
        raise ValueError("plan must state the computed revenue")
    # The text claims "Close 2/day": the funnel must actually yield 2.
    if sales // DAYS != 2 or sales % DAYS != 0:
        raise ValueError(f"funnel yields {sales / DAYS}/day, not 2/day")
    if net < 2000:
        raise ValueError(f"net ${net:,} is below the $2,000 bar")


def projection(sales: int, revenue: int) -> str:
    """Cumulative sales/revenue at day 10, 20 and 30."""
    per_day_sales = sales // DAYS
    per_day_revenue = revenue // DAYS
    marks = []
    for day in (10, 20, 30):
        marks.append(
            f"day {day}: {per_day_sales * day} packs "
            f"${per_day_revenue * day:,}"
        )
    return " | ".join(marks)


def main() -> int:
    contacts, replies, sales, revenue, fees, net = funnel()
    plan = build_plan(sales, revenue, net)
    check_plan(plan, revenue, sales, net)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(plan)
    os.chmod(OUTPUT_PATH, 0o644)
    digest = hashlib.sha256(plan.encode("utf-8")).hexdigest()
    print(f"contacts {contacts} -> replies {replies} -> sales {sales}")
    print(f"revenue ${revenue:,} - outreach ${OUTREACH_BUDGET} "
          f"- fees ${fees} = net ${net:,}")
    print(f"projection: {projection(sales, revenue)}")
    print(f"wrote {len(plan)} chars to {OUTPUT_PATH} sha256={digest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
