# Discount abuse & margin playbook

For `discount-abuse-monitor`.

---

## 1. Profit brought (typical)

**Simple:**  
`Profit ≈ Σ (order_subtotal_after_discount − COGS − variable_fees) − fixed_campaign_cost_if_allocated`

If only margin % on **post-discount revenue**:  
`Profit ≈ post_discount_revenue × margin%` (label assumption).

Include **refunds** on coded orders if data allows.

---

## 2. Risk signals

| Signal | Risk |
|--------|------|
| Redemptions >> plan | High |
| Velocity spike after single social post | High (leak) |
| Many new emails, one code | Medium–High (share) |
| Same device / IP cluster | High (stack or bot) |
| Code on RetailMeNot etc. | High |
| Steady VIP-only use | Low |

---

## 3. Strategy corrections

- **Rotate** leaked code; old code invalid after date.
- **Per-customer cap** (one use).
- **Min order** raise or exclude sale SKUs.
- **Segmented codes** (email hash, VIP tier).
- **Single-use** links from email where platform supports.

---

## 4. Red line examples

- Profit per order negative after discount + COGS.
- Campaign net margin below company floor (e.g. <15% contribution).
