#!/usr/bin/env python3
"""Rebuild data/yc_recent_batches.csv from the public YC company directory.

Source: https://github.com/yc-oss/api (a daily mirror of ycombinator.com/companies).
The theme of each company is NOT in the source. It comes from
data/yc_bracket_assignments.csv, which was labelled by hand.

Usage:  python3 scripts/fetch_yc.py
Standard library only. Companies that have no assignment yet are written with
bracket_id "UNASSIGNED" and listed on stderr so they can be labelled.
"""
import csv
import json
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE_URL = "https://yc-oss.github.io/api/companies/all.json"
BATCHES = ["Fall 2025", "Winter 2026", "Spring 2026", "Summer 2026", "Fall 2026"]


def region(company):
    regions = company.get("regions") or []
    if "India" in regions:
        return "India"
    if "United States of America" in regions:
        return "USA"
    return "Other"


def main():
    with urllib.request.urlopen(SOURCE_URL, timeout=120) as resp:
        companies = json.load(resp)
    with open(ROOT / "data" / "yc_bracket_assignments.csv", newline="") as f:
        assigned = {row["yc_slug"]: row["bracket_id"] for row in csv.DictReader(f)}

    rows = [c for c in companies if c["batch"] in BATCHES]
    rows.sort(key=lambda c: (BATCHES.index(c["batch"]), c["name"].lower()))
    missing = []
    out = ROOT / "data" / "yc_recent_batches.csv"
    with open(out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["bracket_id", "startup", "yc_one_liner", "batch", "region", "location",
                    "team_size", "yc_industry", "tags", "website", "yc_url", "yc_slug",
                    "yc_long_description"])
        for c in rows:
            bracket = assigned.get(c["slug"], "UNASSIGNED")
            if bracket == "UNASSIGNED":
                missing.append(c["slug"])
            w.writerow([bracket, c["name"], (c["one_liner"] or "").strip(), c["batch"], region(c),
                        c.get("all_locations") or "", c.get("team_size") or "",
                        c.get("subindustry") or "", "; ".join(c.get("tags") or []),
                        c.get("website") or "", c["url"], c["slug"],
                        " ".join((c.get("long_description") or "").split())])
    print(f"wrote {len(rows)} companies to {out.relative_to(ROOT)}")
    if missing:
        print(f"{len(missing)} without a bracket: {', '.join(missing)}", file=sys.stderr)


if __name__ == "__main__":
    main()
