# Claude Design Brief — Democracy Pulse Website

## What This Is

**Democracy Pulse** is a real-time democracy index built on a novel theoretical framework called the **Grand Social Theory (GST)**. Unlike existing indices (Economist Democracy Index, Freedom House, V-Dem), it:

1. **Updates daily**, not annually
2. **Is fully transparent** — every score traces back to raw data and a stated methodology
3. **Uses a different theoretical lens** — measures *rooted freedom*, not procedural checklists
4. **Rejects expert-survey dominance** — prioritizes verifiable data over opinion polls
5. **Measures structural mechanisms**, not actors — diagnoses the *how*, never the *who*

---

## Theoretical Framework (GST)

### Core Definition
> Democracy is the capacity of individuals to determine their collective and personal destiny, anchored within protective social shields (family and community) that buffer them from the totalizing power of the state or capital. It requires liberation from both cognitive manipulation and economic precarity, ensuring that capital maintains its legitimacy only through its continuous transformation into public benefit.

### Three Pillars

**Pillar I — Integrated Will** (Psychological/Cognitive)
- *Core question:* Do citizens act out of genuine preference, or manufactured necessity and systemic fear?
- Key metric: Forced Substitution Coefficient — tracking abandonment of public services due to manufactured insecurity
- When people "choose" private alternatives because public options were deliberately degraded, that is forced substitution masked as choice

**Pillar II — Organic Ties** (Sociological/Anthropological)
- *Core question:* Do communities protect individuals while preserving their capacity for internal dissent?
- Key distinction: Organic Democracy (protective + internally free) vs. Micro-Fascism (protective + conformity-enforcing)

**Pillar III — Social Capital Transformation** (Economic/Political)
- *Core question:* Does capital serve the public good, or does it extract and stagnate?
- Capital's legitimacy is conditional — wealth that transforms into public benefit is legitimate; wealth that extracts and hoards is feudal stagnation

### Six Cross-Cutting Rights
Every individual possesses rights paired with duties:
1. **Integrity** — wholeness of person; not to be instrumentalized
2. **Justice** — fair treatment, due process, equitable access
3. **Compassion** — recognized as full human being
4. **Welfare** — material sufficiency as baseline for democratic participation
5. **Truth** — authentic perception, free from substituted perception
6. **Solidarity** — collective support when individual capacity is insufficient

### Triangular Social Contract
The individual, community, and state exist in mutual obligation:
- State protects individual from harm (including oppressive communities)
- Community buffers individual from state and capital
- Individual holds both rights and duties

### Monitory Democracy (Normative Model, NOT a measurement dimension)
The core democratic act is not voting — it is auditing. The normative model involves:
- AI-assisted petition systems via e-government
- Empowered administrative judiciary (merit-selected, independent)
- Pattern detection across thousands of petitions
- Merit-based governance staff selection (like military career paths)

---

## Data Structure

### Current Pilot Countries
- Turkey, United States, Norway (3 of 5 planned; India and China coming)

### Measurement Dimensions Per Country

**Pillar I — Integrated Will** (6 dimensions):
1. **Government Type** — republic vs monarchy, sovereignty origin, hereditary privilege encoded, head of state formal powers, monarch budget per capita
2. **Information Environment** (4 sub-sections):
   - *Mainstream Media:* state-owned broadcasters, private broadcasters, top 5 owners market share, newspapers per 1000, journalists imprisoned/killed, media regulator independence, broadcast licensing, govt ad spend share, defamation prison sentences, prior restraint orders
   - *Digital Media:* internet penetration, social media usage, internet shutdowns, online censorship laws, data retention laws, VPN usage, news sites blocked, encrypted messaging restrictions, govt content removal requests, digital surveillance legislation
   - *Economic Structure:* advertising market total, cross-ownership by non-media conglomerates, foreign ownership restrictions, journalist salary vs national avg
   - *Social Media Journalism:* YouTube news subscribers, X journalist followers, TikTok news creators, independent YouTube avg views, social media as primary news source, govt social media censorship, platform bans/restrictions, crowdfunded journalism platforms, podcast as news source
3. **Economic Precarity** — Gini pre/post-tax, poverty rate, unemployment, youth unemployment, labor force participation, employment rate, inflation (CPI/food/core/producer), minimum wage (gross/net/local/USD), average wage, GDP per capita (nominal/PPP), workforce on minimum wage, housing cost ratio, food cost share, out-of-pocket healthcare, uninsured population, real wage growth, union density
4. **Forced Substitution Coefficient** — private tutoring enrollment, private healthcare usage, privatization revenue, out-of-pocket core services, public vs private school enrollment, public vs private hospital beds, pension coverage (public/private)
5. **Civic Education** — civic knowledge score, voter turnout, political efficacy, mandatory civic education hours
6. **Digital Rights** — constitutional right to internet, net neutrality, digital ID scope, biometric data legislation, right to be forgotten

**Pillar II — Organic Ties** (5 dimensions):
1. **Social Cohesion** — social trust, community organization participation, volunteer rate, charitable giving
2. **Family Structure Health** — domestic violence, divorce rate, single-parent households, child poverty, maternal mortality, elder care public vs family
3. **Civic Participation Beyond Voting** — NGOs per capita, protest participation, petition participation, union density
4. **Internal Dissent Capacity** — legal right to protest, protest permit required, permit denial rate, assembly law restrictions, participatory budgeting
5. **Social Isolation** — loneliness rate, living alone, elderly isolation, suicide rate, birth rate

**Pillar III — Social Capital Transformation** (6 dimensions):
1. **Wealth Distribution** — Gini pre/post-tax, top 1%/10% income share, bottom 50% wealth share, wealth Gini, billionaire wealth % GDP
2. **Taxation Progressivity** — tax-to-GDP, top marginal income tax rate, corporate tax rate, capital gains tax rate, capital gains vs income tax gap, effective tax rate by decile, tax gap estimate, property tax, inheritance/estate tax
3. **Public Investment** — healthcare spending (total + public share), education spending (total + public), infrastructure, R&D (total + public), social protection, military spending
4. **Social Mobility** — intergenerational income elasticity, education by parental income quartile, income mobility bottom→top, public university enrollment by income quintile
5. **Cultural Production Accessibility** — public arts funding per capita, museum attendance, library branches, public broadcasting budget, cultural participation rate
6. **Corporate Extraction vs Public Benefit** — corporate profit % GDP, CEO-to-worker pay ratio, share buybacks, dividend vs reinvestment, lobbying expenditure (total + per capita), revolving door instances

### Data Format
- JSON files per country at `data/raw/{country}_pilot_v0.1.json`
- Fields are snake_case, values are numbers/strings/booleans/null
- `null` = data not yet collected
- No commentary in data files — data and analysis are separate
- No Freedom House, RSF, or any external inference scores — only raw verifiable data
- No specific entity/person names — GST diagnoses mechanisms, not actors

---

## Current Site

**URL:** https://alprnkmbr.github.io/democracy/
**Repo:** https://github.com/alprnkmbr/democracy
**Tech:** Static HTML/CSS/JS, deployed via GitHub Pages

### What Works Now
- Dark/light mode toggle
- Country selector buttons (Turkey, US, Norway)
- Generic data rendering — all 16+ dimensions displayed, nulls show "—"
- Mobile-responsive layout
- CSS variables for theming

### What Needs Improvement (Everything Visual/UX)
The current site is a functional data dump. It needs to become a **data visualization dashboard** that makes the GST framework's insights immediately visible.

---

## Design Requirements

### 1. Landing Page / Hero
- Clear statement of what Democracy Pulse is and why it differs from existing indices
- The GST framework visualized — three pillars, six rights, triangular social contract
- Should feel academic but alive — this is a living index, not a PDF report
- Current pilot countries shown

### 2. Country Dashboard
- Each country gets a rich profile page
- **Radar/spider chart** showing the 3 pillars (or all dimensions) at a glance — the signature visual
- Color-coded dimension scores (once we have them) — gradient from red (critical) through yellow (moderate) to green (healthy)
- Data tables are fine for detail but should not be the primary visual
- Trend indicators where we have time-series data (coming later)

### 3. Comparison View
- Side-by-side radar charts for multiple countries
- Key differences highlighted
- This is where the GST framework's different lens becomes most visible — e.g., Norway scoring lower than expected on Government Type (hereditary monarchy), Turkey showing forced substitution patterns

### 4. Methodology Transparency
- Every score must link to its source data
- Methodology page explaining the GST framework, pillars, dimensions, scoring
- "Why this dimension?" expandable explanations
- Version history — methodology changes are tracked

### 5. Visual Language
- **Academic credibility** — not playful, not corporate, not NGO-slick
- Think: data observatory, not marketing site
- Dark mode as default (current approach works)
- Color palette: deep blues, muted accents. Data visualization colors should be colorblind-safe
- Typography: clean, readable. Data-heavy pages need good information hierarchy

### 6. Interactive Elements
- Clicking a dimension should show its sub-fields and source data
- Hover states on charts showing exact values
- Filtering/sorting on comparison views
- Expandable methodology sections

### 7. Technical Constraints
- Must work as **static site** (GitHub Pages) — no server-side rendering
- Data loads from JSON files via fetch()
- Must be **fast** — this is a data dashboard, not a blog
- Mobile-first but desktop is the primary use case for detailed analysis
- Accessibility: proper ARIA labels, keyboard navigation, colorblind-safe palette

### 8. Future Features (Design for Extensibility)
- Time-series data and trend lines (coming when we have daily snapshots)
- Search by dimension across countries
- API endpoints for programmatic access
- More countries (scaling from 3 to 50+)
- Score cards / composite scores per pillar
- Download data as CSV/XLSX

---

## Brand / Identity

**Name:** Democracy Pulse
**Tagline:** "Democracy isn't a snapshot. It's a pulse."
**What makes it different:** Existing indices are slow, opaque, and influenced by their sponsors' politics. Democracy Pulse is real-time, transparent, and grounded in a theory that measures *rooted freedom* — not procedural compliance.

**Tone:** Academic but alive. Precise but not pedantic. Think: a trusted research collaborator, not a government report.

---

## Data Files for Reference

The current JSON structure (Turkey example, trimmed):

```json
{
  "country": "Turkey",
  "country_code": "TR",
  "collection_date": "2026-04-19",
  "data_version": "0.1-pilot",
  "pillar_I_integrated_will": {
    "government_type": { ... },
    "information_environment": {
      "mainstream_media": { ... },
      "digital_media": { ... },
      "economic_structure": { ... },
      "social_media_journalism": { ... }
    },
    "economic_precarity": { ... },
    "forced_substitution_coefficient": { ... },
    "civic_education": { ... },
    "digital_rights": { ... }
  },
  "pillar_II_organic_ties": {
    "social_cohesion": { ... },
    "family_structure_health": { ... },
    "civic_participation_beyond_voting": { ... },
    "internal_dissent_capacity": { ... },
    "social_isolation": { ... }
  },
  "pillar_III_social_capital_transformation": {
    "wealth_distribution": { ... },
    "taxation_progressivity": { ... },
    "public_investment": { ... },
    "social_mobility": { ... },
    "cultural_production_accessibility": { ... },
    "corporate_extraction_vs_public_benefit": { ... }
  }
}
```

Full data files are at: `https://alprnkmbr.github.io/democracy/data/raw/{turkey,usa,norway}_pilot_v0.1.json`

---

## Hard Rules

1. **No Freedom House, RSF, or external inference scores** — we don't use them, don't reference them
2. **No specific entity/person names** in data display — GST diagnoses mechanisms, not actors
3. **Data and analysis are separate** — show raw data, don't embed commentary
4. **Every score must be traceable** to source and methodology
5. **Null/missing data must be visible** — don't hide gaps, show them honestly
6. **Government Type is a regular dimension** under Pillar I, not special-flagged
7. **Light/dark mode** required
8. **Static site only** — GitHub Pages deployment

---

## What We Want From Claude Design

Take the current site and transform it into a proper data dashboard that:
1. Makes the GST framework's three-pillar structure visually clear and compelling
2. Presents country data through radar charts, comparison views, and expandable dimension details
3. Feels like a serious academic tool, not a blog or marketing page
4. Is extensible — we'll add more countries, time-series data, and scoring over time
5. Maintains the data-only principle — no commentary baked into the UI

The data pipeline and methodology work will continue on our end. We need the visual/UX layer to be excellent.