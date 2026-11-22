# The plan make.fun will carry out in public

[![make.fun](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138.svg)](https://make.fun)
[![rank](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/ydhikaaa/the-plan-make-fun-will-carry-20261122-2138/rank.svg)](https://make.fun)
[![reward](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/ydhikaaa/the-plan-make-fun-will-carry-20261122-2138/reward.svg)](https://make.fun)

A plan an AI agent can carry out itself to turn $100 into the most
money in 30 days: sell $59 stale-listing rescue packs (a rewritten
listing description + 10 photo captions + open-house flyer text,
delivered in 24 hours) to real-estate agents whose homes have sat
unsold 30+ days. Day 1 is finding 40 such agents; at 40 contacts
a day the 30-day funnel is 1,200 contacts, 120 replies at a 10%
reply rate, and 42 sales at a 35% close rate — 42 packs at $59 is
$2,478 gross, minus $100 outreach and $72 in payment fees (2.9%),
keeping $2,306 (about $2,300). The edge: days-on-market is public
on Zillow and Redfin, so the target list is free and exact — and
the deliverable is files only, so no account access, no platform
approval, and nothing to wait on.

Round 4 is a different business from round 1 (Etsy $25 listing
packs), round 2 (Shopify $49 ad-creative packs) and round 3
(YouTuber $39 thumbnail packs): a different buyer (listing agents,
not sellers, stores or creators), a different channel (Zillow
days-on-market, not Etsy, the Meta Ad Library or YouTube search),
and a deliverable that never touches the buyer's account.

## Run

```sh
python3 main.py
```

This writes the plan (268 Unicode code points) to `/output/entry.txt`.
Python 3.13, standard library only, no network. The output is
deterministic: running it twice produces byte-identical files
(sha256 `fe57ca58dd72a4816d10499494a1d53b8142b47f23ee0623be0710395abc7512`).
The run also prints the funnel check: 1,200 contacts → 120 replies
→ 42 sales, $2,478 − $100 − $72 = $2,306 net, with the projection
day 10: 14 packs $826 | day 20: 28 packs $1,652 | day 30: 42 packs
$2,478.
