---
name: shopify-retention-playbooks
description: Create merchant-operator retention and repeat-purchase playbooks for Shopify stores (no specific apps required). Use when the user mentions Shopify operations, increasing repeat purchase rate, retention, LTV, subscription retention, replenishment, win-back, post-purchase strategy, loyalty strategy, customer lifecycle, cohort retention, or asks “how do I improve repeat purchases on my Shopify store?”.
---

# Shopify Retention Playbooks (Merchant Ops)

为 Shopify 独立站商家输出“可执行”的复购/留存打法，不依赖特定 App。重点是：**复购机制选择 + 生命周期触达 + 实验与指标**。

## 先收集输入（缺失就追问）

最少问清这些（用简短问句）：

1. **品类与复购周期**：消耗品/补货？订阅？复购间隔（典型 7/21/30/45/60/90 天）
2. **毛利与折扣空间**：能不能做券/积分？最高折扣/赠品成本上限
3. **客单价与主渠道**：Paid/SEO/Influencer/Email/SMS
4. **现状指标**（没有就让用户给区间/估计）：AOV、repeat purchase rate、30/60/90-day repeat、退款率
5. **触达能力**：Email/SMS/WhatsApp/DM 现状；是否能做自动化（Klaviyo/Shopify Email/其他）
6. **限制与偏好**：是否能承受弹窗、是否重视品牌调性、地区/语言

## 输出格式（必须按此结构交付）

```markdown
## 1) Retention diagnosis (what’s likely broken)
- ...

## 2) Playbooks (choose 3–6 to start)
### Playbook: <name>
- Goal:
- Best for:
- Offer/mechanism:
- Trigger/timing:
- Audience rules:
- Creative angles:
- KPIs:
- Failure modes + mitigations:

## 3) 30-day execution calendar
Week 1:
Week 2:
Week 3:
Week 4:

## 4) Metrics dashboard (definitions)
- ...

## 5) Experiments (A/B)
- ...
```

## 1) 复购机制选择（先选对“杠杆”）

按商家类型选默认杠杆（必要时组合）：

- **补货/耗材**：replenishment reminder + post-purchase education + subscribe & save upsell
- **订阅**：renewal-save offer + skip/pause education + usage-based content
- **高客单/低频**：community + VIP access + referral + UGC reassurance
- **强口碑**：review/UGC capture → reuse in lifecycle messages

## 2) Playbooks 清单（从这里挑 3–6 个落地）

至少从以下类别里覆盖：

- **Post-purchase onboarding**（降低后悔/退款，抬高第二单概率）
- **Replenishment / re-order reminders**（按复购周期触发）
- **Win-back**（沉默用户唤醒：价值点而不是一上来就打折）
- **Cross-sell to 2nd order**（用“下一步”产品组合而不是泛推荐）
- **Subscription save**（续费前/失败支付/取消意向）
- **VIP / loyalty-lite**（不用强积分体系也能做：早鸟、专属内容、优先补货）

## 3) KPI 定义（让 AI 不输出空方案）

必须给出清晰口径：

- **Repeat purchase rate (RPR)**：在观察窗内下第 2 单的客户占比（说明 30/60/90 天）
- **Time to 2nd order**：第 1 单到第 2 单的中位数天数
- **Cohort retention**：按首购周/月 cohort 的复购曲线
- **Contribution margin**：折扣/赠品后的毛利（约束每个活动）

## 4) 典型陷阱（输出时要主动规避）

- “所有人同一条 win-back” → 必须分层：高价值/低价值、最近购买时间、品类
- “靠折扣拉复购” → 如果毛利薄，优先教育内容/补货提醒/捆绑包
- “没事件没口径” → 先定义事件与指标，再谈自动化

