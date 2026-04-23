# METHODOLOGY.md — Democracy Pulse Index (v0.2-draft)

**Status:** DRAFT — under active development  
**Last updated:** 2026-04-23  
**Version:** 0.2-draft  
**Supersedes:** v0.1-draft (6 dimensions) → restructured under GST framework  
**Theoretical foundation:** `research/gst-foundation-v1.md`

---

## Vision

A real-time, transparent, multi-source democracy index that updates daily. Every score traceable to sources, methodology, and theoretical foundation. Designed to replace opaque annual indices with a living measurement grounded in the Grand Social Theory (GST) of Rooted Freedom.

## Core Principles

1. **Transparency:** Every score → source data → methodology version → theoretical justification. Full reproducibility.
2. **Multi-source:** No single dataset dominates. Aggregate diverse inputs. Flag when sources conflict — conflict is itself data.
3. **Daily refresh:** Scores update as new information arrives. Not snapshots — a pulse.
4. **Confidence-flagged:** Three-tier confidence system (high/medium/low). Uncertainty is data, not embarrassment.
5. **Dimension-separated:** Overall score is composite, but dimension scores stand alone. A country's story lives in the profile, not just the number.
6. **Absolute rubrics:** Scores defined by concrete benchmarks (0–10), not panel-dependent normalization. A 7.2 means the same thing regardless of which other countries are in the dataset.
7. **Distributional complements:** Every macro indicator requires a functional/distributional complement. GDP needs GNI. Tax-to-GDP needs spending breakdown. Savings rate needs who-saves analysis.

---

## Theoretical Framework: GST Rooted Freedom

Democracy is the capacity of individuals to determine their collective and personal destiny, anchored within protective social shields (family and community) that buffer them from the totalizing power of the state or capital. It requires liberation from both political domination and economic dependence.

**Three pillars** of democratic capacity:

| Pillar | Name | Core Question |
|---|---|---|
| I | Integrated Will | Can the people form, express, and implement collective decisions free from manipulation and coercion? |
| II | Organic Ties | Do the social structures that protect individuals from state/capital power remain healthy and autonomous? |
| III | Social Capital Transformation | Does the economic system convert wealth into public benefit, or does it extract from the many to enrich the few? |

**Six cross-cutting rights:** Integrity, Justice, Compassion, Welfare, Truth, Solidarity — these permeate all three pillars rather than sitting in one.

Full theoretical foundation: `research/gst-foundation-v1.md`

---

## Measurement Structure

### Scoring: Absolute Rubric (0–10)

Every dimension is scored on a **0–10 absolute rubric** with concrete benchmarks at each level. This is our primary scoring method.

**Why absolute, not relative:**
- GST defines democracy in absolute terms (Rooted Freedom), not relative to other countries
- Panel-dependent normalization means scores change when the panel changes — a 7.0 in 2026 means something different if a worse country is added
- Enables temporal comparison: a country that scores 7.2 today and 6.8 next year has actually deteriorated, not just been re-ranked
- Absolute scores produce more honest rankings

**Relative ranking as secondary view:**
We publish relative rankings as a communication tool, clearly labeled as such. But the primary score is absolute.

#### Rubric Template (per dimension)

| Score | Description | Benchmarks |
|---|---|---|
| 9–10 | Fully realized | [Concrete criteria specific to each dimension] |
| 7–8 | Strongly established | |
| 5–6 | Partially realized | |
| 3–4 | Weak / eroding | |
| 1–2 | Minimally present | |
| 0 | Absent / actively suppressed | |

Detailed rubrics for each sub-dimension will be developed in `methodology/rubrics/`.

### Dimension Inversion Protocol

In our 0–10 rubric, **10 always = best democratic outcome**. Negative indicators are inverted:

| Dimension type | Direction | Method |
|---|---|---|
| Gini, poverty, isolation, media capture | Higher raw = worse | Invert: (max - value) / (max - min) × 10 |
| Press freedom rank | Higher rank = worse | Invert |
| Corruption perceptions | Higher score = better | No inversion needed |
| Union density, social trust | Higher = better | No inversion needed |

**Principle:** Define rubrics so inversion is built in at the rubric level, not a post-hoc mathematical transformation.

---

## Three-Pillar Measurement Architecture

### Pillar I: Integrated Will

*Can the people form, express, and implement collective decisions free from manipulation and coercion?*

| Sub-dimension | Key Indicators | Primary Sources |
|---|---|---|
| **Information Environment** | Press freedom, media ownership concentration, digital censorship, government ad spend share, platform restrictions | RSF, V-Dem media freedom, CPJ, Freedom on the Net |
| **Economic Precarity** | Unemployment, GNI/capita, GDP-GNI gap, poverty rates, out-of-pocket healthcare, housing costs, union density | World Bank WDI, Eurostat, OECD IDD, national stats |
| **Civic Education** | Voter turnout, HDI components (life expectancy, schooling years), political efficacy, civic knowledge | UNDP HDI components, ICCS, national election data |
| **Digital Rights** | Internet as right, net neutrality, biometric legislation, right to be forgotten | Freedom on the Net, national legislation analysis |
| **Government Type** | Head of state powers, sovereignty origin, hereditary privilege encoding | Constitutional texts, V-Dem |
| **Forced Substitution Coefficient** | Private vs. public schooling/healthcare usage, pension coverage, out-of-pocket core services | Eurostat, national stats, OECD |

**GDP-GNI Gap** as extraction indicator: Large positive gap (GDP >> GNI) signals foreign capital extraction — domestic production exceeds what residents earn. Large negative gap (GNI > GDP) signals favorable net income from abroad. Both are GST-relevant.

**HDI Deconstruction Rule:** Use HDI components (life expectancy, expected/mean years schooling) separately. Do NOT use the HDI composite as an input — it contains GNI, which would double-count with our separate economic indicators.

### Pillar II: Organic Ties

*Do the social structures that protect individuals from state/capital power remain healthy and autonomous?*

| Sub-dimension | Key Indicators | Primary Sources |
|---|---|---|
| **Social Cohesion** | Social trust, community organization participation, volunteer rate, charitable giving | World Values Survey, OECD well-being, ESS |
| **Family Structure Health** | Maternal mortality, child poverty, domestic violence, elder care ratio, divorce rate | WHO, national stats, Eurostat |
| **Civic Participation Beyond Voting** | NGO density, union density, protest participation, petition participation | Johns Hopkins CSI, ILO, V-Dem |
| **Internal Dissent Capacity** | Right to protest, assembly restrictions, protest permit denial rate, participatory budgeting | V-Dem, national legislation, ICNL |
| **Social Isolation** | Loneliness rate, living alone %, suicide rate, birth rate, elderly isolation | OECD well-being, WHO, national health stats |

### Pillar III: Social Capital Transformation

*Does the economic system convert wealth into public benefit, or extract from the many to enrich the few?*

| Sub-dimension | Key Indicators | Primary Sources |
|---|---|---|
| **Wealth Distribution** | Gini (pre/post tax), top 10%/1% income shares, bottom 50% share, wealth Gini | World Inequality Database, Eurostat ilc_di12, WB PIP |
| **Taxation Progressivity** | Top marginal rates, corporate tax, VAT, capital gains gap, inheritance tax, effective rates by decile | OECD tax stats, national tax authorities, IMF |
| **Public Investment** | Social protection % GDP, healthcare/education/R&D spending, infrastructure | OECD, WHO, UNESCO, national budgets |
| **Social Mobility** | Intergenerational income elasticity, education attainment by parental income, quintile mobility | OECD social mobility, WID |
| **Cultural Production Accessibility** | Public cultural spending, library branches per capita, museum attendance, public broadcasting | UNESCO, national budgets |
| **Corporate Extraction vs. Public Benefit** | CEO-worker pay ratio, lobbying, sovereign wealth fund, share buybacks, revolving door, corporate profit % GDP | National economic accounts, corporate data, lobbying registries |

**Distributional Complement Rule:** For every macro indicator, a functional/distributional complement is required:
- Tax-to-GDP ratio → + spending breakdown (social protection vs. military vs. patronage)
- GDP per capita → + GNI per capita gap (extraction indicator)
- Savings rate → + who holds the savings (public fund vs. elite hoarding)
- Government spending → + forced substitution rate (are people still going private?)

### Cross-Cutting Rights

These six rights permeate all three pillars. They are scored separately but are not a fourth pillar — they are analytical lenses.

| Right | Definition | Key Indicators | Sources |
|---|---|---|---|
| **Integrity** | Freedom from bodily and political violation | Political imprisonment, torture, bodily autonomy, minority rights | HRW, Amnesty, CIRI |
| **Justice** | Equal access to fair legal processes | Rule of law rank, judicial independence, due process, equal access | WJP, V-Dem judicial, national courts |
| **Compassion** | Societal commitment to care for the vulnerable | Refugee policy, healthcare access, social safety net comprehensiveness | UNHCR, OECD, national data |
| **Welfare** | Material security as a condition of freedom | Poverty rate, housing security, food security, education access | World Bank, OECD, national stats |
| **Truth** | Access to accurate information free from state/corporate distortion | Press freedom rank, government transparency, scientific integrity, censorship | RSF, V-Dem transparency, national legislation |
| **Solidarity** | Collective mutual support structures | Labor protections, mutual aid networks, community support | ILO, national data, V-Dem |

---

## Confidence System

### Three-Tier Flags

| Level | Criteria | Display |
|---|---|---|
| 🟢 **High** | Data from current or previous year, from primary source (national stats, Eurostat, IMF, etc.) | No flag |
| 🟡 **Medium** | Data 2–5 years old, or from secondary/estimated source | ⚠️ with year |
| 🔴 **Low** | Data 5+ years old, estimated, or single source with known methodology issues | ⚠️⚠️ with year and note |

### Implementation in JSON Schema

```json
"unemployment_rate_pct": {
  "value": 3.7,
  "source": "Eurostat 2024",
  "confidence": "high",
  "confidence_note": null
},
"social_trust_pct": {
  "value": null,
  "source": "World Values Survey",
  "confidence": "low",
  "confidence_note": "No recent WVS wave for Turkey; last available 2011"
}
```

### Confidence Propagation Rule

A dimension's confidence = the lowest confidence of its constituent indicators (weakest-link principle). A dimension scored entirely on low-confidence data is itself low-confidence, regardless of how many low-confidence sources agree.

---

## Data Source Hierarchy

Formal hierarchy by data type. Always cite which tier was used. If Tier 1 unavailable, explain why.

| Data type | Tier 1 (preferred) | Tier 2 | Tier 3 (fallback) |
|---|---|---|---|
| Economic output | National statistics office | IMF WEO | World Bank WDI |
| Income distribution | Eurostat EU-SILC (EU) | World Bank PIP | OECD IDD |
| Poverty rates | National poverty surveys | OECD IDD / Eurostat | World Bank estimates |
| Human development | UNDP HDI components (separated) | National education/health stats | World Bank WDI |
| Press freedom | RSF Press Freedom Index | V-Dem media freedom | CPJ data |
| Rule of law | WJP Rule of Law Index | V-Dem judicial independence | Freedom House |
| Civil liberties | HRW + Amnesty reports | CIRI human rights data | Freedom House |
| Social cohesion | World Values Survey | OECD well-being | European Social Survey |
| Labor | ILO ILOSTAT | National labor ministry | OECD employment data |
| Tax | OECD tax statistics | National tax authority | IMF government finance |
| Corruption | Transparency International CPI | World Bank governance indicators | National audit reports |
| Digital rights | Freedom on the Net (FH) | Access Now / digital rights NGOs | National legislation analysis |
| Health | WHO Global Health Observatory | National health ministry | World Bank health data |
| Education | UNESCO UIS | OECD education stats | National education ministry |
| Environmental | Our World in Data | World Bank climate data | National environmental agency |

---

## Robustness Testing

### 7 Weight Configurations

| Config | Pillar I | Pillar II | Pillar III | Cross-cutting | Rationale |
|---|---|---|---|---|---|
| **A** (baseline) | 25% | 25% | 25% | 25% | Equal — our default |
| **B** (economic emphasis) | 35% | 20% | 35% | 10% | Tests if economic dominance shifts rankings |
| **C** (political emphasis) | 40% | 25% | 20% | 15% | Tests if Integrated Will dominance changes outcomes |
| **D** (social emphasis) | 20% | 40% | 20% | 20% | Tests if Organic Ties dominance changes outcomes |
| **E** (rights-first) | 20% | 20% | 20% | 40% | Tests if cross-cutting rights dominance matters |
| **F** (flat all sub-dims) | Equal across all sub-dimensions, no pillar aggregation | — | — | — | Removes pillar-level bias |
| **G** (economic-heavy) | Weight economic sub-dims ×2 | — | — | — | Mimics GDP-heavy approaches like HelloSafe |

### Weight-Sensitivity Flag

If a country's rank shifts by **≥5 positions** across configurations, flag it as **"weight-sensitive"** and investigate why. Document the analysis.

### Reporting Rule

Every score publication includes a robustness summary:
- Country's rank range across all 7 configurations
- Whether weight-sensitive flag applies
- Which configurations shift the country most and why

---

## Scoring Pipeline (Revised)

```
[Raw Sources] → [Scrapers/Importers/APIs] → [data/raw/]
     ↓
[Confidence Flagging] → [confidence: high/medium/low per data point]
     ↓
[Rubric Mapping] → [absolute 0–10 per sub-dimension]
     ↓
[Pillar Aggregation] → [Pillar I / II / III scores + cross-cutting rights scores]
     ↓
[Robustness Testing] → [7 weight configurations]
     ↓
[Composite Score] → [data/scores/ dated JSON snapshots]
     ↓
[Reports & Dashboard] → [reports/ + GitHub Pages dashboard]
```

### Daily Update Cycle

1. **Ingest:** Check for new data from primary sources (APIs, scrapers, manual updates)
2. **Flag:** Apply confidence ratings to new data points
3. **Score:** Map data to absolute rubrics → update affected sub-dimension scores
4. **Aggregate:** Recalculate pillar and composite scores
5. **Test:** Run 7 weight configurations → check for weight-sensitivity changes
6. **Log:** Record all changes with attribution (which source changed, which score moved)
7. **Publish:** Update JSON snapshot → deploy to GitHub Pages

---

## Current Pilot

### Pilot Countries (5)
Norway, Turkey, USA, India, China

### Pilot Status
| Country | Data Version | Last Updated | Key Gaps |
|---|---|---|---|
| Norway | v0.2-pilot | 2026-04-23 | Relative poverty, many forced substitution fields, digital rights |
| Turkey | v0.2-pilot | 2026-04-23 | Social trust, relative poverty, many information environment fields |
| USA | v0.2-pilot | 2026-04-23 | Many null fields in information environment, forced substitution |
| India | Not started | — | — |
| China | Not started | — | — |

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 0.1-draft | 2026-04-19 | Initial 6-dimension structure (Electoral Integrity, Institutional Checks, Civil Liberties, Media Freedom, Participation, Rule of Law) |
| 0.2-draft | 2026-04-23 | Restructured under GST framework (3 pillars + 6 cross-cutting rights). Added absolute rubric scoring, confidence system, data source hierarchy, robustness testing, distributional complement rule, HDI deconstruction rule, GDP-GNI extraction indicator. Incorporated lessons from HelloSafe Prosperity Index analysis. |

---

*This document is alive. Update it as the methodology evolves. Every change must be versioned and dated. Challenge decisions when evidence warrants — but document the challenge and its resolution.*