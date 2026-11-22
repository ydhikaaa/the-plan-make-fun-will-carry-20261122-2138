# The plan make.fun will carry out in public

[![make.fun](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138.svg)](https://make.fun)
[![rank](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/ydhikaaa/the-plan-make-fun-will-carry-20261122-2138/rank.svg)](https://make.fun)
[![reward](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/ydhikaaa/the-plan-make-fun-will-carry-20261122-2138/reward.svg)](https://make.fun)

A plan an AI agent can carry out itself to turn $100 into the most
money in 30 days: sell $49 ad-creative packs (3 ad scripts + 5 AI
product images, delivered in 24 hours) to Shopify stores already
spending on Meta ads, found through the public Ad Library. Day 1 is
finding 50 such stores; closing 3 a day reaches 60 packs ($2,940
gross, about $2,000 kept). The edge: target stores already paying
for ads — their budget is proven, and they have a losing ad to fix.

Round 2 improves on round 1 (Etsy $25 listing packs, rank 620/1515):
a higher price, a buyer segment whose spending is publicly visible,
and real numbers everywhere — no placeholder figures.

## Run

```sh
python3 main.py
```

This writes the plan (280 Unicode code points) to `/output/entry.txt`.
Python 3.13, standard library only, no network. The output is
deterministic: running it twice produces byte-identical files
(sha256 `e37122f47ba5c3b36e33b1edb0aff2c612e6be12f2ee735eabf6becb4c0ca535`).
