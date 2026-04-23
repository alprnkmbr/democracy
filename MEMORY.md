# MEMORY.md — Long-Term Curated Memory

## Project: Democracy Pulse

### What It Is
A real-time, transparent, multi-source democracy index. Updates daily. Every score traceable to sources and methodology. Replaces opaque annual indices with a living measurement.

### Key Decisions
- **2026-04-19:** Equal weighting for all 6 dimensions at launch; calibrate empirically later
- **2026-04-19:** Pilot set of ~10 countries; mix of consolidated democracies, backsliding, hybrid, and autocratic regimes to stress-test dimensions
- **2026-04-19:** Aim for maximum automation; flag confidence levels (automated-high / automated-needs-review / requires-human)
- **2026-04-19:** Backtesting needed but method TBD — likely score known trajectories (e.g., Hungary 2010–2025, Turkey 2013–2025) as validity check
- **2026-04-19:** Alperen wants visual interface; proposed GitHub repo + GitHub Pages; I suggested Option B (repo + auto-deploy to Vercel/Netlify) for better interactivity; awaiting decision

### Methodology Status
- v0.1-draft: 6 dimensions defined (Electoral Integrity, Institutional Checks, Civil Liberties, Media & Info Freedom, Participation & Representation, Rule of Law & Accountability)
- Scoring: 0–10 per dimension, equal weights
- Pipeline: sketched conceptually, not built

### Pilot Countries
- Norway, USA, Turkey, India, China (5 countries for pilot)

### Methodology Status
- v0.2-draft: GST framework (3 pillars + 6 cross-cutting rights) with absolute rubric scoring, confidence system, data source hierarchy, robustness testing, distributional complement rule, HDI deconstruction rule, dimension inversion protocol
- Pipeline: 7-step daily cycle defined (ingest → flag → score → aggregate → test → log → publish)
- Pilot: Norway, Turkey, USA (v0.2 data); India, China not started

### Measurement Dimensions Structure
- Full structure in `research/gst-foundation-v1.md` Section VIII
- Pillar I: Press freedom, information environment, Forced Substitution Coefficient, economic precarity, civic education, digital rights
- Pillar II: Social cohesion, family structure health, civic participation, internal dissent capacity, social isolation
- Pillar III: Wealth distribution, taxation progressivity, public investment, social mobility, cultural production, corporate extraction
- Cross-cutting: Integrity, Justice, Compassion, Welfare, Truth, Solidarity

### Key Decisions
- Equal weights for pilot, calibrate later
- GitHub Pages for dashboard (static, JSON snapshots)
- Maximum automation aim, flag confidence levels
- Theory before methodology — GST foundation v1 written
- Monitory democracy is normative model, NOT a measurement dimension
- Existing index data categories are valid — GST reframes, doesn't reject
- Gap analysis is core methodology across all dimensions
- Absolute rubric scoring (0–10) as primary; relative ranking as secondary view
- Deconstruct HDI into components — never use composite as input
- Every macro indicator requires a distributional/functional complement
- 7 robustness weight configurations defined (A–G)
- Formal data source hierarchy per data type (3 tiers, 15 categories)
- Confidence propagation: weakest-link principle (dimension confidence = lowest indicator confidence)