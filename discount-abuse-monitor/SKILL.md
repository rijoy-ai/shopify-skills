---
name: discount-abuse-monitor
description: Monitor discount-code abuse and promo leakage so conversions do not destroy margin. Use when gross margin is abnormal during campaigns, codes spread widely on social or deal forums, one code shows extreme redemption vs plan, new-customer share from a code looks suspicious, or the user wants to tighten discount strategy after a leak. Output code-level economics and risk. Do NOT use for pure creative promo naming with no usage or margin data, or legal-only coupon terms with no abuse or P&L ask.
compatibility:
  required: []
---

# Discount code abuse monitor

You connect **campaign → margin red lines → discount policy fixes** when **volume up but profit flat or down** because codes are **overused or leaked**.

## When to lean in

- **Margin crash** during promo vs baseline.
- **Social / forum leakage** of single-use or "private" codes.
- **Redemption spike** on one code (many orders, low net margin).

## Core workflow

1. **Pull code usage** — Per code: redemptions, order value, net revenue after discounts, estimated margin or profit (inputs: COGS % or order-level margin if available).
2. **Profit attribution** — Profit brought by code ≈ sum(order net × margin) − **allocated discount cost** (or revenue net of discount × margin — state formula).
3. **Risk assessment** — Leak signal, concentration (one email vs open web), new vs repeat, velocity, stack abuse.
4. **Strategy correction** — Caps, expiry, single-use per customer, exclude sale items, replace with segmented codes, kill leaked code + rotate.

## Gather context

1. Export: code, orders, discount $, revenue, refunds if possible.
2. Target margin % or min acceptable profit per order.
3. Whether code was supposed to be segmented (VIP only, etc.).

Read `references/discount_abuse_playbook.md` for risk rubric.

## Mandatory success output: master table

Every **full** run must include this table (one row per code or per code + segment):

| Discount code | Usage count | Profit brought | Risk assessment |
|---------------|-------------|----------------|-----------------|
| … | … | … | Low / Med / High + reason |

**Column rules**

- **Discount code**: Identifier as in store.
- **Usage count**: Redemptions or orders using code (define).
- **Profit brought**: Currency amount **after** discount and **after** COGS (or state proxy: "contribution if margin X%"); negative allowed.
- **Risk assessment**: **Low / Medium / High** plus **one line** (e.g. "High — 10× planned redemptions, spike after TikTok post").

If data missing, show table with **placeholders** and **exact fields** to export from Shopify/Woo/admin.

## Follow-up block (full run)

- **Red line**: Any code with profit ≤ 0 or below floor.
- **Actions**: kill, cap, new code, customer limits, stack rules.

## When NOT to use

- No access to usage or revenue — offer generic policy only if user insists; still show empty table schema.

## Split with other skills

- **Promo traffic stress** — ad efficiency; this skill is **code economics + abuse**.
- **Affiliate ROI** — creator codes overlap; still use this skill when **leak + margin** is the ask.
