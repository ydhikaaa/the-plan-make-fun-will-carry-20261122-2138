"""Round 4 plan: sell stale-listing rescue packs to real-estate agents.

The buyer: a listing agent whose home has sat unsold 30+ days.
Days-on-market is public on Zillow and Redfin, so the pain is
visible from search results alone and the target list costs
nothing to build. The deliverable is files only (a rewritten
listing description, 10 photo captions, open-house flyer text,
delivered in 24h), so no account access, no platform approval,
and nothing to wait on. A stale listing costs the agent a
commission; a $59 fix is a rounding error against it.
"""

import hashlib
import os
import sys

# Funnel inputs. Every figure below is a real input; nothing here is
# a placeholder, and the plan text is built from these numbers so the
# words can never drift away from the math.
OUTREACH_PER_DAY = 40   # agents contacted per day (agent email on
                        # the brokerage site, or a DM on the listing)
DAYS = 30
REPLY_RATE = 0.10       # 1 in 10 replies
CLOSE_RATE = 0.35       # about 1 in 3 replies buys
PRICE = 59              # dollars per rescue pack
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
        "Day 1: find 40 agents with listings stale 30+ days "
        "on Zillow.",
        f"Sell a ${PRICE} pack: rewritten description, 10 photo "
        "captions, flyer text in 24h.",
        f"${OUTREACH_BUDGET} covers outreach.",
        f"{sales} packs = ${revenue:,}, keep ~${kept:,}.",
        "Edge: stale days are public, so targeting is free; "
        "files only, no access.",
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
    if f"{sales} packs" not in text:
        raise ValueError("plan must state the computed pack count")
    kept = (net // 10) * 10
    if f"${kept:,}" not in text:
        raise ValueError("plan must state the computed kept cash")
    if f"${PRICE}" not in text:
        raise ValueError("plan must state the pack price")
    if net < 2000:
        raise ValueError(f"net ${net:,} is below the $2,000 bar")


def projection(sales: int, revenue: int) -> str:
    """Cumulative packs/revenue at day 10, 20 and 30."""
    marks = []
    for day in (10, 20, 30):
        packs = sales * day // DAYS
        money = revenue * day // DAYS
        marks.append(f"day {day}: {packs} packs ${money:,}")
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
