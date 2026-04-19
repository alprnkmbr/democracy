# METHODOLOGY.md — Democracy Pulse Index (v0.1-draft)

**Status:** DRAFT — under development
**Last updated:** 2026-04-19
**Version:** 0.1-draft

## Vision

A real-time, transparent, multi-source democracy index that updates daily. Every score traceable to sources and methodology. Designed to replace opaque annual indices with a living measurement.

## Core Principles

1. **Transparency:** Every score → source data → methodology version. Full reproducibility.
2. **Multi-source:** No single dataset dominates. Aggregate diverse inputs.
3. **Daily refresh:** Scores update as new information arrives. Not snapshots — a pulse.
4. **Confidence-flagged:** Low-confidence scores are marked differently. Uncertainty is data.
5. **Dimension-separated:** Overall score is composite, but dimension scores stand alone.

## Dimensions (Proposed — Subject to Revision)

### D1: Electoral Integrity
- Free and fair elections, voter access, opposition viability, election monitoring
- Sources: election observation missions, V-Dem, IDEA, domestic monitors

### D2: Institutional Checks
- Separation of powers, judicial independence, legislative oversight, constitutional constraints
- Sources: constitutional texts, judicial independence indices, V-Dem, Rule of Law Index

### D3: Civil Liberties
- Freedom of expression, assembly, religion, movement, due process
- Sources: CIRI, Freedom House, HRW reports, Amnesty, domestic NGOs

### D4: Media & Information Freedom
- Press freedom, journalist safety, internet freedom, state media capture
- Sources: RSF Press Freedom Index, Freedom on the Net, CPJ data

### D5: Participation & Representation
- Voter turnout, gender/minority representation, civic engagement, direct democracy mechanisms
- Sources: IDEA, IPU, national election data

### D6: Rule of Law & Accountability
- Corruption, legal predictability, security sector oversight, human rights enforcement
- Sources: WJP Rule of Law Index, Transparency International, national audit data

## Scoring

- Each dimension: 0–10 scale
- Overall score: weighted composite (weights TBD — likely equal initially, refined empirically)
- Daily delta: change from previous day's score, with attribution (which data source changed)
- Volatility indicator: rolling 30-day standard deviation of daily scores

## Data Pipeline (Conceptual)

```
[Raw Sources] → [Scrapers/Importers] → [data/raw/]
     ↓
[Normalization Engine] → [data/processed/]
     ↓
[Scoring Engine] → [data/scores/]
     ↓
[Reports & Alerts] → [reports/]
```

## Open Questions

- **Weights:** Equal weighting or expert-derived? Hybrid?
- **Countries:** Start with a pilot set (10-20) or go global from day one?
- **Automation level:** How much scoring can be automated vs. needs human judgment?
- **Backtesting:** Should we score historical periods to validate methodology?
- **Publication:** Where and how to publish? Website? API? Academic paper first?

---

*This document is alive. Update it as the methodology evolves. Every change must be versioned.*