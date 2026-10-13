# Startup Research Ideas

Research by Nikshay Yadav and Akshit Arora on one question:

> Which pre-seed startup ideas are incubators and accelerators funding right now,
> and which of those programs can two founders from India get into?

## Read this first

| If you want | Open |
|---|---|
| The spreadsheet (one tab per theme) | [`output/startup-idea-research.xlsx`](output/startup-idea-research.xlsx) |
| The conclusions in plain words | [`research/findings.md`](research/findings.md) |
| What is still unknown | [`research/open-questions.md`](research/open-questions.md) |
| Where every fact came from | [`research/sources.md`](research/sources.md) |

## What is inside (as of 2026-10-13)

- **374 funded startups** with the idea in one plain sentence, from 10 programs:
  Y Combinator, a16z Speedrun, Peak XV Surge, Accel Atoms, Antler India, Antler US, WTFund,
  Thiel Fellowship, Emergent Ventures India, Google for Startups Accelerator India.
- **All 900 YC companies** from Fall 2025 to Fall 2026, each sorted into one of 22 themes.
- **22 programs compared:** money, equity, who can apply, timing.

## Layout

```
data/
  brackets.csv                 the 22 themes
  funded_startups.csv          main table, one row per funded startup
  incubators.csv               one row per program
  yc_bracket_assignments.csv   hand-made theme label for each YC company
  yc_recent_batches.csv        generated: all 900 YC companies
output/
  startup-idea-research.xlsx   generated from data/
research/
  findings.md                  what the data says
  sources.md                   source log
  open-questions.md            gaps and next steps
scripts/
  fetch_yc.py                  refreshes the YC table from the public directory
  build_workbook.py            builds the spreadsheet from data/
```

The CSV files are the source of truth. The spreadsheet is rebuilt from them:

```
python3 scripts/fetch_yc.py
uv run --with openpyxl python3 scripts/build_workbook.py
```

AI agents: read [`AGENTS.md`](AGENTS.md) before changing anything.
