# Findings

Research date: 2026-10-13. First pass. Numbers come from the files in `data/`.
Anything marked "my reading" is an interpretation, not a fact from a source.

## 1. What was looked at

- **Y Combinator:** all 900 companies from the last 5 batches (Fall 2025 to Fall 2026),
  each sorted by hand into one of 22 themes. Fall 2026 is still filling up (134 listed so far).
- **Nine other programs:** a16z Speedrun (SR007), Peak XV Surge 12, Accel Atoms AI Cohort 2026,
  Antler India, Antler US, WTFund, Thiel Fellowship 2026, Emergent Ventures India,
  Google for Startups Accelerator India 2026.
- **22 programs compared** on money, equity, and whether founders in India can apply
  (`data/incubators.csv`).

## 2. What YC funds now

Counts per batch. "Share" compares the two full batches that are furthest apart.

| Theme | Fall 25 | Winter 26 | Spring 26 | Summer 26 | Share Fall 25 | Share Summer 26 |
|---|---|---|---|---|---|---|
| Manufacturing, hardware, chips, energy | 3 | 10 | 11 | 30 | 2.1% | 13.0% |
| AI-native service companies | 4 | 8 | 9 | 20 | 2.8% | 8.7% |
| Robotics | 6 | 8 | 9 | 18 | 4.1% | 7.8% |
| Training data for AI | 5 | 8 | 5 | 17 | 3.4% | 7.4% |
| Fintech and markets | 7 | 11 | 13 | 15 | 4.8% | 6.5% |
| Infrastructure for AI agents | 7 | 13 | 9 | 14 | 4.8% | 6.1% |
| Enterprise AI workers | 12 | 9 | 17 | 14 | 8.3% | 6.1% |
| AI for traditional industries | 10 | 13 | 11 | 13 | 6.9% | 5.7% |
| Defense and space | 5 | 9 | 7 | 11 | 3.4% | 4.8% |
| Coding and developer tools | 14 | 14 | 16 | 10 | 9.7% | 4.3% |
| Sales and marketing AI | 11 | 12 | 18 | 8 | 7.6% | 3.5% |
| Healthcare AI | 8 | 11 | 10 | 8 | 5.5% | 3.5% |
| Consumer apps | 11 | 8 | 8 | 7 | 7.6% | 3.0% |
| Finance back-office AI | 8 | 12 | 6 | 5 | 5.5% | 2.2% |
| Creative tools | 7 | 3 | 1 | 2 | 4.8% | 0.9% |
| Voice AI | 3 | 2 | 3 | 1 | 2.1% | 0.4% |

What stands out:

1. **Physical-world companies went from 10% to 26% of the batch.** Robotics + defense +
   industrial hardware was 14 of 145 in Fall 2025 and 59 of 230 in Summer 2026.
   TechCrunch's nine Summer 2026 demo-day picks were all hardware, robotics or deep tech (nuclear data centers at sea,
   AI chips, robots, strike drones).
2. **"Be the firm, don't sell to the firm."** AI-native service companies went from 4 to 20.
   These are law firms, accounting firms, insurance brokers, freight brokers, debt collectors
   and clinics that use AI inside and sell the finished work.
3. **Selling data to AI labs became a category.** 17 companies in Summer 2026 sell training
   data, robot data or practice environments. Several report revenue within weeks.
4. **Crowded software themes are shrinking as a share:** coding tools, sales and marketing AI,
   consumer apps, creative tools, voice AI.
5. **Almost everything is AI and B2B.** Consumer apps are 38 of 900.

## 3. India and YC

- **Only 9 of 900 YC companies are based in India (1%).** 769 are based in the US (85%).
- A newsletter's community estimate says Indian-origin founders were **about 20% of the
  Summer 2026 batch** (90+ of about 470 founders). Not verified by the newsletter itself.
- So Indian founders do get in, but mostly with a US-based company. YC needs a parent company
  in the US, Canada, Singapore or Cayman, and the batch is in person in San Francisco.
- The 9 India-based companies: Bolna AI (voice AI for Indian businesses), Redapto, Perseus,
  Cardboard (AI video editor), Ressl AI, BentoLabs AI, Waybill (Gurugram, parts buying for
  hardware teams), Markov (computer-use data for AI labs), Kailash Labs (small video AI models).
  **All 9 sell to businesses; none is a consumer app.** Only Bolna describes itself as built
  for the Indian market.
- A close example: **ByteAsk** (YC Fall 2026). Two IIT Delhi computer science graduates, an
  earlier legal-AI startup that was acquired, now an AI coding agent for C and C++.
  $1M pre-seed led by YC with Entrepreneur First.

## 4. What India-side programs fund

- **Peak XV Surge 12** (15 named, 7 in India): consumer and health are much bigger here than
  in YC. Pediatric clinics, AI health assistant, beauty at home, personal finance, music,
  defence satellites. Cheques are seed-sized (up to $5M), so most had raised before.
- **Antler India** (12 listed on its page): defence and space (counter-drone, satellite servicing,
  amphibious aircraft), voice AI, cross-border payments, hydrogen engines, kirana supply.
- **Accel Atoms 2026** (5 of 4,000+ applicants): AI co-scientist, ERP agents, voice AI for
  call centres, AI entertainment, factory automation.
- **WTFund 2026** (8 startups, founders under 25, ₹20 lakh grant, no equity): mostly health
  hardware (oral cancer test, pathology microscope AI, stroke rehab robot) and AI
  infrastructure (payments for AI agents, AI security).
- **Google's India accelerator 2026** (20): later-stage, equity-free, no cash.

## 5. Ideas that show up in several programs at once

When unrelated investors fund the same idea, it is a stronger signal than one batch.

| Idea | Where it appears |
|---|---|
| Payments or cards for AI agents | YC (Locus, Agentcard, Maven, Orthogonal, Sponge), WTFund (Prava), Antler US (Parleo) |
| Insurance for risks created by AI agents | YC (Klaimee, Mount, Valgo, PRINCEPS, Risklytics), a16z Speedrun (Keythorn) |
| AI-native law firm | YC (General Legal, Moritz, Vector Legal, LegalOS), a16z Speedrun (Athena, OneGC) |
| Voice AI for businesses | YC (Bolna, Samora, Callab), Antler India (Infer.so, Navana.ai), Accel Atoms (Persistence Labs) |
| Counter-drone and defence drones | YC (9 Mothers, Isengard, Milliray), Antler India (Armory), Antler US (TAV Drones) |
| Robot and human-movement training data | YC (Asimov, Praxis, Hemlock, Cortex), a16z Speedrun (Munari, Vound) |
| Simulated customers or users | YC (Expected Parrot, Foresight, Auxos, Studio), a16z Speedrun (Primitive Labs, Tenera) |
| AI for freight forwarders and logistics | YC (Peer, TrueMile, Burt), a16z Speedrun (Nimble, Rumbo, Sotant) |
| AI for ERP systems | YC (Trope, Assemble), Accel Atoms + Antler India (Dodge.ai) |
| AI copilot for mechanical engineers | YC (Aurorin CAD, REV1), Antler US (Tandem) |
| Testing and monitoring voice or AI agents | YC (Lemma, Sentrial, BentoLabs), Surge (Reinforce Labs), Google India (SuperBryn) |
| AI devices: earbuds, rings, glasses | YC (antimattr, E1O, Button Computer, Vexo), WTFund (Antimattr) |

## 6. Programs: what is realistic for two founders in India

Full table: `data/incubators.csv`. Short version, my reading:

| Goal | Programs | Why |
|---|---|---|
| No-strings money while still students | WTFund (₹20 lakh grant), Emergent Ventures India (grant), Z Fellows ($10K) | No or little equity. Does not block a later accelerator. Antimattr went WTFund then YC. |
| First real cheque in India | Antler India (₹4 Cr for 11%), AJVC (₹1.5 Cr for 9%), 100X.VC (₹1.25 Cr for 15%), Campus Fund (₹1-8 Cr, student founders), gradCapital ($40K for 4%) | Open to India-based teams. Antler takes pre-product teams and decides in 3 weeks. |
| Indian founders building for the world | Accel Atoms (up to $2M), South Park Commons (up to $1M, Bengaluru bootcamp, no idea needed) | Built for this exact case, but very selective. |
| The big global shot | Y Combinator ($500K for 7%), a16z Speedrun (up to $1M for 10%) | Any country can apply to YC. Needs a US-style parent company and 3 months in San Francisco. Next YC deadline reported as 2026-11-02. |
| Later, not first | Peak XV Surge (up to $5M), Google accelerator (no cash) | Both expect a product and usually earlier funding. |

## 7. Paths worth copying

- **Antimattr:** WTFund grant (India, under 25) then YC Fall 2026.
- **Dodge.ai:** Antler India then Accel Atoms AI Cohort 2026.
- **Dodo Payments:** Antler India then Google's India accelerator 2026.
- **ByteAsk:** earlier startup acquired, then YC Fall 2026 with Entrepreneur First.
- **Waybill, Markov, Bolna:** stayed in India and still got into YC.

## 8. Limits of this first pass

- Funding for most rows is the program's standard cheque. Startup-specific rounds are
  mostly not public.
- Speedrun and Antler US company lists come from third-party pages, not the firms themselves.
- "Indian founders?" is only filled where a source said so. Most YC rows are `unknown`.
- Themes were assigned by one reader from short descriptions. Some companies fit two themes.
- See `research/open-questions.md` for what to do next.
