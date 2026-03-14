---
name: seo-traffic-conversion-audit
description: Audit organic traffic for real purchase conversion — keyword source → landing relevance → conversion path — and kill vanity traffic stories. Use when the user wants to find high-traffic pages (especially blog) with zero or near-zero conversions, map queries to PDP fit, add product placement hooks in content, or fix organic sessions that never touch commercial pages. Task focus: identify zero-converting blog posts and inject concrete product tie-in points (modules, CTAs, internal links). Do NOT use for pure SEO ranking checks ("where do we rank for X"), keyword volume-only research, backlink audits, or technical crawl without conversion or landing relevance — those belong to ranking/SEO skills, not this one. If the user only asks rankings, answer briefly and optionally one line on conversion — do not run the full audit template unless they care about revenue from organic.
compatibility:
  required: []
---

# SEO traffic → conversion audit

You separate **organic traffic that buys** from **vanity visits** (high sessions, no money) and upgrade **irrelevant landers** with **product placement** so SEO pays rent.

## Should-not-trigger (strict)

- **Pure ranking query** — "What position is keyword K?" with no CVR, GA, or landing ask.
- **Rank tracking / SERP only** — no conversion lens.

Scope is **conversion optimization on organic**, not **ranking mechanics**.

## When to lean in

- Blog or guides **traffic up, revenue from those URLs flat or zero**.
- Organic landers with **intent mismatch** (informational query, no path to product).
- Need **product injection points** in long content.

## Core workflow

1. **Keyword / query source** — Landing URL, primary query theme (GSC / GA4), session quality proxy (engaged sessions if available).
2. **Landing relevance** — Does the page satisfy intent **and** connect to a product story? Gap list.
3. **Purchase path** — Do organic sessions hit cart/checkout from this entry? If not, where they exit.
4. **Placement plan** — For **high-traffic zero-conversion** posts: **specific** blocks (comparison table, "shop the routine," inline SKU, mid-article CTA, FAQ product link).

## Gather context

1. URLs + organic sessions (or clicks) + conversions attributed to URL (GA4 path or assisted).
2. Product catalog fit (which SKUs match the post topic).
3. Editorial constraints (tone, no hard sell).

Read `references/organic_conversion_playbook.md` for placement patterns.

## Mandatory outputs (full audit)

### A) Vanity vs productive table

| URL / page | Organic traffic | Conversions (or $) | Verdict |
|------------|-----------------|----------------------|---------|
| … | high / med / low | 0 or n | Vanity / productive / fix |

Flag **high traffic + zero conversion** as primary remediation list.

### B) Relevance & path notes

Per flagged URL:

- **Query intent** (informational / commercial / mixed).
- **Relevance score** (high/med/low to product line).
- **Where path breaks** (no internal link to PDP, weak CTA, off-brand topic).

### C) Product placement injection list

For each **high-traffic zero-conversion** blog post, output **at least 3 placement points**:

| Placement # | Location in article | Product tie-in | CTA / link target |
|-------------|---------------------|----------------|-------------------|
| 1 | After H2 [topic] | … | PDP / collection |
| 2 | Mid-article comparison | … | … |
| 3 | Before conclusion | … | … |

Placement types: **editorial bridge**, **comparison module**, **bundle callout**, **FAQ single link**, **sticky sidebar** (describe if not building HTML).

## Pushy when vague

If user says "organic is huge but sales aren't," still output the **vanity table** and **one blog post** worked example with **three placements** (use placeholders if no URLs).

## When NOT to use

- Rank-only briefs (should-not-trigger).
- Paid search — use ads skill.

## Split with other skills

- **Ranking / technical SEO** — not this skill’s primary job.
- **PDP CRO** — use when lander is already product page.
