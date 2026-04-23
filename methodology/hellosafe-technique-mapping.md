# Data Source & Technique Mapping: HelloSafe → Democracy Pulse GST Framework

**Date:** 2026-04-23
**Purpose:** Map useful techniques, data sources, and methodological choices from the HelloSafe Prosperity Index 2026 into our GST-based measurement framework. This is not about adopting their dimension structure — it's about learning from their implementation choices.

---

## I. Techniques to Adopt

### 1. GNI alongside GDP (Pillar I: Economic Precarity)

**HelloSafe approach:** Uses both GDP/capita PPP (30%) and GNI/capita Atlas method (20%) to counter the Ireland/Luxembourg multinational profit distortion. Ireland's GDP inflated ~$70K/person by Apple/Google/Pfizer accounting; GNI reveals actual household income.

**Our application:**
- We already collect `gdp_per_capita_nominal_usd`, `gdp_per_capita_ppp_usd` in our data schema
- **Add:** `gni_per_capita_atlas_usd` and `gni_per_capita_ppp_usd` as mandatory fields
- **Use case:** The gap between GDP and GNI is itself a GST-relevant indicator — a large GDP-GNI gap signals that capital extraction is recorded as domestic production but flows to foreign owners. This connects directly to Pillar III's "corporate extraction vs. public benefit" dimension
- **Scoring implication:** For economic precarity, weight GNI higher than GDP. GDP measures what's produced in a country; GNI measures what residents actually earn. The difference is a forced substitution indicator at the macro level

**Data source:** World Bank WDI — GNI per capita, Atlas method (current US$ and PPP)

### 2. Inverted Negative Indicators (All Pillars)

**HelloSafe approach:** Gini and poverty rate are inverted — more equal = higher score. Simple, intuitive, standard.

**Our application:**
Already partially implemented (lower Gini = better in our data), but we should formalize the inversion protocol:

| Dimension | Direction | Inversion method |
|---|---|---|
| Economic precarity indicators | Lower = better | Invert: (max - value) / (max - min) × 10 |
| Information substitution | Higher capture = worse | Invert |
| Forced substitution coefficient | Higher = worse | Invert |
| Social isolation | Higher = worse | Invert |
| Wealth inequality (Gini, top% shares) | Higher = worse | Invert |
| Corporate extraction | Higher = worse | Invert |
| Press freedom rank | Higher rank = worse | Invert |
| Corruption perceptions | Higher score = better | No inversion needed |

**Principle:** In our 0–10 rubric, 10 always = best democratic outcome. Define the rubric so inversion is built in, not a post-hoc transformation.

### 3. Per-Country Per-Indicator Confidence Flags (All Pillars)

**HelloSafe approach:** Marks ⚠️ on every country-indicator with outdated data, shows the exact year. E.g., Japan Gini: 2013 ⚠️, Qatar Gini: 2007 ⚠️, Singapore Gini: 2017 ⚠️.

**Our application — three-tier confidence system:**

| Level | Criteria | Display |
|---|---|---|
| 🟢 High confidence | Data from current or previous year, from primary source (national stats, Eurostat, etc.) | No flag |
| 🟡 Medium confidence | Data 2–5 years old, or from secondary/estimated source | ⚠️ with year |
| 🔴 Low confidence | Data 5+ years old, estimated, or single source with known methodology issues | ⚠️⚠️ with year and note |

**Implementation in our JSON schema:**
```json
"unemployment_rate_pct": {
  "value": 8.5,
  "source": "TÜİK 2024",
  "confidence": "high",
  "confidence_note": null
},
"gini_coefficient_pretax": {
  "value": 0.448,
  "source": "TÜİK 2024",
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

### 4. Robustness Testing Across Weight Configurations (Methodology)

**HelloSafe approach:** Tests 7 alternative weighting configurations. Reports top 5 is stable across all. This is a form of sensitivity analysis.

**Our application:**
Define at minimum these configurations for testing:

| Config | Pillar I | Pillar II | Pillar III | Cross-cutting | Rationale |
|---|---|---|---|---|---|
| A (baseline) | Equal (25% each pillar, 25% rights) | Equal | Equal | Equal | Our default |
| B (economic emphasis) | 35% | 20% | 35% | 10% | Tests if economic dominance shifts rankings |
| C (political emphasis) | 40% | 25% | 20% | 15% | Tests if Integrated Will dominance changes outcomes |
| D (social emphasis) | 20% | 40% | 20% | 20% | Tests if Organic Ties dominance changes outcomes |
| E (rights-first) | 20% | 20% | 20% | 40% | Tests if cross-cutting rights dominance matters |
| F (flat all dimensions) | Equal across all 17 sub-dimensions | — | — | — | No pillar aggregation |
| G (HelloSafe-like) | Weight economic sub-dims ×2 | — | — | — | Mimics economic-heavy approaches |

**Reporting rule:** If a country's rank shifts by ≥5 positions across configurations, flag it as "weight-sensitive" and investigate why.

### 5. Data Source Hierarchy (All Pillars)

**HelloSafe approach:** Eurostat ilc_di12 → World Bank PIP → OECD IDD (for inequality). Primary, most recent, most harmonized source wins.

**Our application — formal hierarchy per data type:**

| Data type | Tier 1 (preferred) | Tier 2 | Tier 3 (fallback) |
|---|---|---|---|
| Economic output | National statistics office | IMF WEO | World Bank WDI |
| Income distribution | Eurostat EU-SILC (EU countries) | World Bank PIP | OECD IDD |
| Poverty rates | National poverty surveys | OECD IDD / Eurostat | World Bank estimates |
| Human development | UNDP HDI components | National education/health stats | World Bank WDI |
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

**Rule:** Always cite the tier used. If Tier 1 is unavailable, explain why in `confidence_note`.

---

## II. Data Sources to Add to Our Schema

Based on HelloSafe's source table and our gaps:

### Missing from our current `data/raw/` files:

| Source | What it provides | Our dimension |
|---|---|---|
| **World Bank WDI — GNI per capita, Atlas method** | Real household income (vs. GDP distortion) | Pillar I: Economic precarity |
| **UNDP HDI components (life expectancy, expected years schooling, mean years schooling)** | Separate HDI sub-indices, not just composite | Pillar I: Civic education; Pillar III: Welfare |
| **Eurostat ilc_di12** | Most current, harmonized Gini for EU countries | Pillar III: Wealth distribution |
| **OECD IDD** | Relative poverty rates, income decile ratios | Pillar III: Wealth distribution; Cross-cutting: Welfare |
| **World Bank PIP** | Gini, poverty headcounts for non-EU countries | Pillar III: Wealth distribution |
| **CEPALSTAT** | Poverty/inequality for Latin America | Pillar III: Wealth distribution (future expansion) |

### Already in our schema but under-populated:

| Indicator | Countries with data | Countries with null |
|---|---|---|
| `gni_per_capita_*` | None — not in schema | All 3 |
| `relative_poverty_rate_pct` | None | All 3 |
| `income_decile_ratios` | None | All 3 |
| `poverty_rate_national_pct` | Turkey only | Norway, USA |
| `social_trust_pct` | Norway (74), USA (31) | Turkey |

---

## III. Methodological Choices to Consider

### A. Panel vs. Absolute Scoring

**HelloSafe:** Min-max normalization within panel → scores depend on who else is in the panel.

**Our position:** We should use **absolute rubric-based scoring** (0–10 defined by concrete benchmarks) as our primary method. Reasons:
- Panel-dependent scores can't be compared across time (a 7.0 in 2026 means something different if the panel changes)
- Our GST framework defines democracy in absolute terms (Rooted Freedom), not relative to other countries
- A country shouldn't score higher just because a worse country was added to the panel

**But:** Relative ranking is still useful for communication. We can:
1. Score each country on absolute rubrics → primary score
2. Publish relative rankings as a *secondary* view
3. Both approaches, clearly labeled

### B. The HDI Double-Counting Problem

**HelloSafe's flaw:** HDI includes GNI, so using both HDI (20%) and GNI (20%) double-counts income.

**Our approach:** We should use HDI **components** (life expectancy, education indices) separately, not the composite. This avoids double-counting and gives us more granular data:
- Life expectancy → Pillar II: Family structure health
- Expected/mean years of schooling → Pillar I: Civic education
- GNI component → already captured separately

**Decision:** Deconstruct HDI into components. Don't use the composite as an input.

### C. Regional Normalization

**HelloSafe:** Separate regional panels with intra-panel normalization.

**Our approach:** Use absolute rubrics (so no need for regional normalization), but produce **regional comparative views** as a secondary output. The story "Norway 8.7, Turkey 3.2, China 1.8" is more informative than "Norway 98, Turkey 54, China 32" on a panel-dependent scale.

### D. Savings Rate Removal Lesson

**HelloSafe removed savings rate** because Qatar's 57% savings rate reflected rentier economics, not population prosperity.

**GST parallel:** This validates our **Forced Substitution Coefficient** concept. Raw macro indicators (savings rate, GDP, tax-to-GDP) can be misleading without understanding *who benefits*. A high tax-to-GDP ratio in Norway (42.6%) funds universal public services. A similar ratio in an authoritarian state might fund security apparatus and patronage networks.

**Decision:** For every macro indicator, we need a distributional/functional complement:
- Tax-to-GDP ratio → + how it's spent (social protection vs. military vs. patronage)
- GDP per capita → + GNI per capita gap (extraction indicator)
- Savings rate → + who holds the savings (public fund vs. elite hoarding)
- Government spending → + forced substitution rate (are people still going private?)

---

## IV. Summary: Action Items

### Immediate (next data collection pass):

1. ✅ Add `gni_per_capita_atlas_usd` and `gni_per_capita_ppp_usd` to all country JSON schemas
2. ✅ Add `relative_poverty_rate_pct` to all country JSON schemas
3. ✅ Add `gdp_gni_gap_usd` as a computed field (GDP - GNI = extraction indicator)
4. ✅ Add three-tier confidence flags (`high`/`medium`/`low` + year + note) to every data point
5. ✅ Add UNDP HDI components separately (life expectancy, expected/mean years schooling) instead of composite

### Methodology:

6. ✅ Define 7 robustness testing weight configurations
7. ✅ Formalize data source hierarchy per data type
8. ✅ Build absolute rubric-based scoring (0–10) as primary; relative ranking as secondary
9. ✅ Deconstruct HDI into components — don't use composite
10. ✅ For every macro indicator, require a distributional/functional complement

### Research:

11. ✅ Study Eurostat ilc_di12 methodology for possible adoption in EU country scoring
12. ✅ Compare World Bank PIP vs. OECD IDD vs. national source Gini estimates for Turkey (we have 0.448 from TÜİK — how does WB PIP compare?)
13. ✅ Investigate whether OECD IDD publishes relative poverty rates for our pilot countries

---

*This mapping is a living document. Update as techniques are implemented or superseded.*