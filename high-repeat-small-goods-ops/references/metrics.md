# Metric Definitions & Dashboard Fields (High-Repeat Small Goods)

Goal: Align "ops/ads/content/CS" on the same metrics so reviews don’t mismatch.

---

## A. Core metrics (suggest weekly)

### 1) Traffic & conversion funnel
- **Exposure**: Times product/store/content was seen (per platform definition)
- **CTR**: Clicks / exposure
- **Add-to-cart rate**: Add-to-cart users / visitors (or add-to-cart events/visitors—define one)
- **Favorite rate**: Favorites / visitors
- **CVR**: Paying buyers / visitors
- **AOV**: Paying amount / paying orders (or / paying buyers—define one)

### 2) Transaction & quality
- **GMV**: Paying amount (include/exclude refunds and shipping per platform)
- **Gross margin**: GMV − product cost − platform/payment/fulfillment (or use margin % if exact cost unknown)
- **Return rate**: Returned orders / paid orders (optionally "shipped only")
- **Post-purchase reason mix** (returns/claims): Fit/quality/color/logistics/expectation gap/allergy etc. (tagged)

### 3) Repeat & existing customers
- **Repeat customer mix**: Repeat customer GMV / total GMV (or repeat order share)
- **Second-order rate**: First-time buyers who buy again within X days / first-time buyers
- **30-day repeat rate**: Buyers in period who buy again within 30 days / buyers in period
- **Repeat cycle**: Median days to next purchase (by category if possible)

### 4) Reputation & content
- **Review rate**: Orders with review / paid orders
- **Photo/video review rate**: Orders with photo or video review / orders with review
- **Negative review rate**: 1–2 star orders / reviewed orders
- **Content conversion**: GMV from content traffic / content traffic (platform definitions vary)

---

## B. Segmentation fields for repeat (simplified RFM)

Tag each user with:
- **Recency**: Days since last purchase
- **Frequency**: Purchases in last 90 days
- **Monetary**: Total spend in last 90 days (or margin contribution)

Example output fields:
- user_id / platform_uid
- last_purchase_date
- days_since_last_purchase
- orders_90d
- gmv_90d
- segment (new/active/high-value/silent/churned)
- preferred_category (e.g. phone case/screen protector/accessory; or lipstick/base/skincare)

---

## C. Minimum dataset for weekly review

Weekly minimum:
- By day: Visitors, paying buyers, GMV, CVR, AOV, return rate
- Top SKUs: Volume, GMV, margin estimate, return rate, review stars
- Repeat: Repeat customer mix, second-order or 30-day repeat rate (pick one)
- Reviews: Review rate, negative review rate, top 3 negative-review reasons
