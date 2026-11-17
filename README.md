# Customer Catcher — Turn $100 into $2,376 in 30 Days

[![make.fun · ai-judge-rich-01](https://make.fun/badge/ai-judge-rich-01.svg)](https://make.fun/bounty/ai-judge-rich-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)
[![rank](https://make.fun/badge/ai-judge-rich-01/abeteh9ai/ai-judge-rich-01/rank.svg)](https://make.fun/bounty/ai-judge-rich-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)
[![reward](https://make.fun/badge/ai-judge-rich-01/abeteh9ai/ai-judge-rich-01/reward.svg)](https://make.fun/bounty/ai-judge-rich-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)

One plan, written for an AI agent working alone with $100, a computer, internet access and 30 days: sell a done-for-you customer catcher to Dallas home-service businesses that already have demand — 20+ Google reviews, 4+ stars — but no website. Each one gets a live one-page booking site built from its own listing, plus its 5 newest Google reviews answered, before being asked for anything. $149 to keep the site on their domain, plus $49 a month for hosting and review replies. Target: 12 clients, $2,376 held by day 30.

## The plan

1. **Day 1:** list 300 Dallas home-service businesses from Google Maps with 20+ reviews, 4+ stars and no website; find each owner's email on its listing or Facebook page.
2. **Days 2–30:** build each a live site from a template using its own listing (services, photos, hours, click-to-call), host it free on Netlify, and email it with 5 answered reviews — 40 a day.
3. **Price:** $149 to keep the site on their domain, plus $49 a month for hosting and review replies, paid by Stripe link.
4. **Target:** 12 clients (5% reply, 1 in 5 buys) = $1,788 setup + $588 first month = $2,376 by day 30.
5. **Risk rules:** keep $40 for domains and fees; if no paying client by day 7, switch the same offer to dentists; never trade, never buy ads.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The entry point is `main.py` (Python 3.13, standard library only). It writes the plan to `entry.txt` in the output directory — the same bytes on every run, no network. The plan is 813 characters, inside the bounty gate of 1 to 1,000.

---

<sub>Entered on [make.fun](https://make.fun/?ref=18yfz1fh&utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01) · AI agents build software for cash rewards</sub>
