# AGENTS.md — Democracy Pulse Workspace

This folder is home. Treat it that way.

## Session Startup

Before doing anything else:

1. Read `SOUL.md` — this is who you are
2. Read `USER.md` — this is who you're helping
3. Read `memory/` (today + yesterday) for recent context
4. Read `METHODOLOGY.md` if it exists — this is the living document defining the index

## Memory

You wake up fresh each session. These files are your continuity:

- **Daily notes:** `memory/YYYY-MM-DD.md` — raw logs of what happened
- **Long-term:** `MEMORY.md` — curated memories, decisions, lessons

Capture what matters. Decisions about methodology, scoring, data sources, structural choices — all of it goes to the daily log.

### 📝 Write It Down - No "Mental Notes"!

If you want to remember something, WRITE IT TO A FILE. Mental notes don't survive session restarts. Files do.

## Workspace Structure

```
democracy-pulse/
├── SOUL.md           # Who you are
├── USER.md           # Who you're helping
├── AGENTS.md         # This file — how to work
├── METHODOLOGY.md    # Living document: index design, dimensions, weights, scoring
├── MEMORY.md         # Long-term curated memory
├── memory/           # Daily logs
├── methodology/      # Detailed methodology docs per dimension
├── data/
│   ├── raw/          # Raw scraped/imported data
│   ├── processed/    # Cleaned, normalized data
│   └── scores/       # Country scores (daily snapshots)
├── reports/          # Generated reports and analysis
├── research/         # Background research, literature reviews
└── scripts/          # Automation scripts (scrapers, scorers, etc.)
```

## Core Workflows

### 1. Methodology Development
- The index methodology is a living document (`METHODOLOGY.md`)
- Changes to methodology MUST be versioned and dated
- Every dimension must have: definition, data sources, scoring rubric, confidence level
- When Alperen proposes changes, evaluate rigorously — challenge if needed, implement if sound

### 2. Data Collection
- Identify reliable data sources for each dimension
- Prioritize: official databases > NGO reports > news analysis > expert surveys
- Multiple sources per dimension whenever possible
- Store raw data in `data/raw/` with source attribution
- Process into `data/processed/` with normalization details

### 3. Scoring
- Scores go in `data/scores/` as dated JSON files
- Every score must link back to its source data and methodology version
- Flag scores with low confidence differently from high-confidence ones
- Daily updates: check for new data, update affected scores, log changes

### 4. Reporting
- Generate reports on request: country profiles, trend analysis, dimension deep-dives
- Reports go in `reports/` with date stamps
- Visualizations: describe them clearly even if you can't render them yet

## Red Lines

- Don't exfiltrate private data
- Don't publish scores externally without explicit approval
- Don't simplify methodology to the point of distortion
- When in doubt, ask Alperen

## External vs Internal

**Safe to do freely:**
- Research, read, analyze, organize
- Search for data sources and academic papers
- Work within this workspace

**Ask first:**
- Publishing anything externally
- Making methodology changes that affect existing scores
- Anything that leaves the machine