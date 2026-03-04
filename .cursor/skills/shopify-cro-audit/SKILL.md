---
name: shopify-cro-audit
description: Audit a Shopify store for conversion rate optimization (CRO) and repeat-purchase lift without requiring any specific apps. Use when the user asks for CRO, PDP optimization, cart/checkout improvements, site audit, speed/UX issues, reducing returns, increasing AOV, or wants a prioritized backlog with impact/effort and measurement plan.
---

# Shopify CRO Audit (PDP/Cart/Checkout)

输出一份“能落地”的 Shopify 转化诊断与改版清单：**问题 → 证据/信号 → 改法 → 优先级 → 量化验证**。不绑定任何特定 App 或主题。

## 先收集输入（缺失就追问）

1. **站点链接**（或截图/页面文案粘贴）
2. **主题/堆栈**：Online Store 2.0？自定义？是否 headless
3. **关键页面**：Top 3 landing pages、Top 3 PDP、cart/checkout
4. **现状指标**（没有就要区间）：CVR、ATC rate、checkout completion、AOV、退款率
5. **流量结构**：移动端占比、主要国家、主要渠道
6. **约束**：是否能改 checkout、是否能开发、上线节奏

## 输出格式（固定）

```markdown
## Executive summary (3 bullets)
- ...

## Funnel hypothesis (where conversion leaks)
- Landing → PDP:
- PDP → Add to cart:
- Cart → Checkout:
- Checkout → Purchase:

## Findings & fixes (prioritized backlog)
| Priority | Area | Issue | Evidence/Signal | Fix | Effort | Expected impact | Metric |
|---|---|---|---|---|---|---|---|

## A/B test plan (top 3 experiments)
1. ...

## Measurement checklist
- ...
```

## 审计维度（必须覆盖）

### 1) PDP（商品详情页）
- 价值主张是否 5 秒可理解（标题+首屏）
- 社会证明是否“可验证”（评分、review 摘要、UGC）
- 风险逆转（退换、运费、到货时间、质保）
- 购买决策信息（尺寸、成分/材质、对比、FAQ）
- 订阅/补货的切入（如果适用）：subscribe & save、补货频率
- 变体选择与库存/预售提示

### 2) Collection / Search
- 筛选器是否支持“快速缩小”（价格、尺寸、用途、补货周期）
- 列表卡片是否能承载“复购理由”（补货、套装、省钱）

### 3) Cart（购物车）
- 运费/税/到货时间透明度
- 加购（合理）与强推（反感）的边界
- 优惠码体验（避免“我是不是错过了折扣”的焦虑）

### 4) Checkout
- 字段摩擦与信任（支付方式、徽章不滥用）
- 退换/配送政策可达性
- 站点性能与移动端可用性

## 输出规则（避免“空泛建议”）

- 每条建议都必须绑定一个**可测指标**（ATC、CVR、AOV、refund、time-to-2nd-order）
- 优先级必须考虑：移动端、流量占比、实现成本、品牌风险
- 如果用户不给站点：输出“CRO 问诊问卷 + 默认改版 backlog”，并明确哪些项需要页面信息才能定制

