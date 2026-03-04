---
name: shopify-lifecycle-flows
description: Design Shopify merchant lifecycle messaging flows (email/SMS) that improve repeat purchases and retention without depending on a specific tool. Use when the user mentions Klaviyo/Shopify Email/SMS, post-purchase flows, replenishment reminders, win-back, subscription churn, segmentation, or asks for flow diagrams, message copy, timing, and KPIs.
---

# Shopify Lifecycle Flows (Email/SMS)

为 Shopify 商家输出可直接搭建的生命周期自动化：**触发条件、分群规则、时间线、消息文案框架、与 KPI**。不绑定任何具体 App/ESP，但会给“实现映射”（Klaviyo / Shopify Email / 其他）。

## 先收集输入（缺失就追问）

1. **渠道**：Email / SMS / WhatsApp（有哪些）
2. **ESP/工具**：Klaviyo？Shopify Email？其他？
3. **产品复购周期**：7/21/30/45/60/90 天？是否订阅
4. **品牌调性**：强促销 vs 强内容
5. **限制**：短信频次、合规（地区）、折扣上限

## 输出格式（必须按此结构）

```markdown
## Flow map (high level)
- ...

## Flow specs (build-ready)
### Flow: <name>
- Goal:
- Trigger:
- Exit rules:
- Segments:
- Timeline (T+):
- Messages (Email/SMS):
  - Subject / Hook:
  - Body structure:
  - CTA:
- KPIs:
- Notes (deliverability, compliance, edge cases):

## Implementation mapping
- Klaviyo:
- Shopify Email:
```

## 默认应产出的 6 条核心 Flow（可按需要裁剪）

1. **Post-purchase onboarding**（T+0 到 T+7）：使用指南、FAQ、预期管理、降低退款
2. **Review / UGC capture**（在“体验窗口”后）：收集口碑，反哺转化与复购
3. **Replenishment reminder**（按复购周期）：T+X、T+X+3、T+X+7
4. **Cross-sell to 2nd order**（第 1 单后 10–21 天）：组合装/配件/补充装
5. **Win-back**（沉默 45/60/90 天分层）：内容价值 → 轻激励 → 强激励（可选）
6. **Subscription save**（如果有订阅）：续费前提醒、支付失败、取消意向挽回

## 规则（让方案更“可执行”）

- **所有 flow 必须有 exit rules**：一旦下单/订阅恢复/已评价，就退出或转支线
- **必须分层**：至少按 AOV/LTV 或订单数分层（高价值人群避免过度打折）
- **短信要少而准**：短信只用于“时效性强、价值明确”的节点（补货/续费/支付失败）

