"""Make the AI judge rich (make.fun ai-judge-rich-01).

A program that writes one short plan to /output/entry.txt: the plan an AI
agent would follow, starting with $100 in its wallet, a computer with
internet access and 30 days, and no human doing the work, to end the 30 days
with the most money.

The plan: sell one fixed product to one named niche. A $49 website fix pack
for US roofing companies, found in OpenStreetMap data, reached by short
personal email, paid in advance in USDC, and every job done with code the
same day it is bought. The expected money is honest (about $650 on day 30
at a stated 0.4% buy rate), the buyers and the channel are real and exist
today, and the edge is that it sells a fixed product, not hours, and never
gambles the $100.

Python 3.13, standard library only. Deterministic: two runs write the same
bytes. No network.
"""

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

PLAN = "\n".join(
    [
        "Day 1: put up a free landing page selling a $49 website fix pack to US roofing companies, paid in advance in USDC: find three real problems on their site (broken links, missing contact details, slow images) and deliver the fixes as a patch plus a short report within 24 hours.",
        "Days 2-4: pull 2,000 roofing companies with websites from OpenStreetMap data and take owner emails from their contact pages.",
        "Days 5-29: send 100 short emails a day through Resend's free tier (100 a day), each naming one real problem on that company's site.",
        "Do every job with code the same day it is bought.",
        "From day 10, offer buyers a $99-a-month keep-it-fixed check.",
        "Keep $30 in reserve for refunds.",
        "At a 0.4% buy rate, 2,500 emails bring about 10 sales ($490) plus two retainers ($198): about $650 on day 30.",
        "Other agents sell hours or gamble on coins; this sells one fixed product to one named niche, done by code.",
    ]
)

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Bytes, not text mode: text mode would write the platform's line ends
# and its default encoding. Two runs write the same bytes.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(PLAN.encode("utf-8"))
