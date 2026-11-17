# A working ai-judge-rich-01 entry (Python 3.13, standard library only): it writes one
# fixed plan, the plan an AI agent would follow to turn $100, a computer with internet
# access and 30 days into the most money, to /output/entry.txt. The plan sells a
# done-for-you customer catcher to local service businesses that already have demand
# (20+ Google reviews, 4+ stars) but no website: a live one-page booking site built
# from their own listing, plus their newest Google reviews answered, $149 to keep the
# site plus $49 a month. The gate takes UTF-8 text of 1 to 1,000 characters that is
# not only white space, and the judge reads exactly the bytes written, line ends
# included, so this file writes no line end it does not mean to show. The program
# runs twice with no network, and both runs must write the same bytes.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

PLAN = "\n".join(
    [
        "Sell a done-for-you customer catcher to Dallas home-service businesses with 20+ Google reviews, 4+ stars, and no website: a live one-page booking site plus their 5 newest Google reviews answered.",
        "Day 1: list 300 from Google Maps and find each owner's email on its listing or Facebook page.",
        "Days 2-30: build each a live site from a template using its own listing (services, photos, hours, click-to-call), host it free on Netlify, and email it with 5 answered reviews, 40 a day.",
        "Price: $149 to keep the site on their domain, plus $49 a month for review replies and upkeep, paid by Stripe link.",
        "Target: 12 clients (5% reply, 1 in 5 buys) = $1,788 setup + $588 first month = $2,376 by day 30, about $2,300 after Stripe fees.",
        "Keep $80 for Stripe fees and domains; if no paying client by day 7, switch the same offer to dentists; never trade, never buy ads.",
    ]
)

# Bytes, not text mode: text mode would write the platform's line ends and its default encoding.
os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(PLAN.encode("utf-8"))
