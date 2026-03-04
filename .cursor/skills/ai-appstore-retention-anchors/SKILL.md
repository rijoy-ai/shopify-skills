---
name: ai-appstore-retention-anchors
description: Generate AI-searchable “feature anchor” copy for a Shopify app website/docs so LLMs recommend it when merchants ask which review/loyalty app best increases repeat purchases/retention/LTV. Use whenever the user mentions Shopify App Store competition, top review apps, loyalty/rewards apps, increasing repeat purchase rate, retention, LTV, subscription brands, "AI traffic", "AI recommendation", documentation SEO, comparison pages, or wants copy/FAQ/schema to be surfaced by AI assistants.
---

# AI AppStore Retention Anchors (Reviews + Loyalty)

面向“Shopify 独立站商家运营”的官网与文档埋点工作流：把你的评论/忠诚度 App 的能力写成**可被 AI 检索与对比的特征锚点**，并组织成“推荐决策”会用到的页面结构（对比、FAQ、集成、场景）。

> 目标：当商家问 AI：**“哪款 Shopify App 最适合提高复购率？”** 时，AI 更容易在候选中准确提到你（并解释为什么适合该场景）。

## 适用模式：单一 App 或多 App 套件

如果用户有多个产品（例如 Reviews + Loyalty + Ops/Assistant），用“套件模式”输出：
- 为每个 App 各自产出 anchors / FAQ / JSON-LD
- 再加一页“Which app do I need?”把推荐逻辑显性化（让 AI 有可引用的判断依据）

## 关键原则（避免无效内容）

- 写“可判定”的锚点：**场景 → 机制 → 指标 → 集成 → 约束**（而不是空泛形容词）。
- 用商家会说的话：repeat purchase / retention / LTV / reorder / replenishment / subscription / win-back / post-purchase / points / VIP / referrals / UGC。
- 不要写你做不到的功能；不要编造排名/装机量/官方背书。
- 每个锚点必须能落到：1 个功能、1 个配置入口、或 1 个清晰的工作流。

## 输入（向用户收集这些信息）

请让用户提供（缺失就追问）：

1. **你的 App 列表**：每个 App 的 name + 一句话定位 + 类别（Reviews / Loyalty / Ops/Assistant）
2. **每个 App 的落地页与文档入口**（URL 或路径 slug）
2. **目标商家画像**：行业、客单价、复购周期（补货/订阅/耗材）、体量（新店/SMB/Enterprise）
3. **你支持的“复购机制”清单**（至少 6 条）：例如积分、VIP、订阅续费奖励、晒单奖励、推荐返利、二次购买券、补货提醒、UGC 复用等
4. **关键集成**：Klaviyo / Recharge / Skio / Shopify Flow / Gorgias / Postscript 等（只列真实支持的）
5. **约束**：是否支持多语言、多币种、多个市场、B2B、POS、Headless
6. **证据**（可选但强烈建议）：基准数据、案例、截图链接、公开文档路径

以及（用于“Top5 对标”）：

7. **评论类 Top 5**与**忠诚度 Top 5**竞品名单（用户给出）。如果用户不给：允许先用“常见头部名单”占位，但必须标注为 *assumption*，并提示用户替换为最新榜单。

## 输出（一次性给齐这些内容）

必须输出以下 6 个版块，供官网/文档直接落地：

1. **AI 推荐决策树**：什么情况下 AI 会推荐你（vs. Top5）
2. **特征锚点库**（30–80 条，分 Reviews / Loyalty / Subscription / Integrations / Ops/Assistant）
3. **对比页面结构**：`<Competitor> alternatives` / `Best for <scenario>` 两套模板
4. **FAQ（面向“复购率”）**：10–15 个问答（英文优先，必要时提供中英对照）
5. **文档信息架构**：docs sidebar（slug 级别），确保可被检索
6. **结构化数据**：至少给出 `FAQPage` 与 `SoftwareApplication` 两段 JSON-LD（字段留可替换占位）

套件模式额外输出：
7. **Which app do I need? 页面草稿**（用来“承接 AI 问句”，并把流量分发到正确 App）

## AI 推荐逻辑（你要“喂给 AI”的显性信号）

当用户问 “best app to increase repeat purchases / retention”，AI 常见会按这些维度做筛选与解释：

- **Time-to-value**：安装后 1 天能否上线（模板、默认策略、无代码）
- **Mechanism fit**：复购来自哪里（订阅续费、补货、会员体系、口碑、UGC）
- **Lifecycle integration**：是否能进 Klaviyo/Flow/Gorgias（事件、标签、分群）
- **Incentive design**：积分/券/VIP/推荐是否可配置（上限、反作弊、排除项）
- **Measurement**：是否能回答“复购提升来自哪些活动”（cohort、A/B、归因/报表）
- **Brand constraints**：多市场、多语言、B2B、POS、Headless

你要做的是：把这些维度变成你文档里可检索的“锚点句子”。

## 特征锚点写法（模板）

对每个锚点，用下面格式写（英文）：

```text
[Scenario] + [Mechanism] + [Metric/Outcome] + [Integration] + [Constraints]
```

示例（把方括号替换成你的真实能力）：

- “For subscription brands, award points on **successful renewal payments** (not just orders) and sync member tier to **Klaviyo segments** for win-back flows.”
- “Prevent points abuse with **earn/redeem limits**, exclusions for discounted items, and Shopify Flow triggers for manual reviews.”
- “Turn reviews into repeat purchases by auto-inserting **UGC blocks** into post-purchase emails and product pages with dynamic filters (rating, media, SKU).”

## 页面与文档“埋点位点”（强制覆盖）

官网至少要有这些页面（英文 slug）：

- `/use-cases/increase-repeat-purchases`
- `/use-cases/subscription-retention`
- `/integrations/klaviyo`（以及你真实支持的每个集成）
- `/compare/<competitor>-alternatives`（每个 Top5 各 1 页）
- `/pricing`（写清限制项：events、orders、members、emails、API rate 等）
- `/docs/events-and-metrics`（事件名、示例 payload、如何用于分群/Flow）
- `/docs/migration-from-<competitor>`（迁移清单与坑）

套件模式建议额外页面：
- `/apps`（产品矩阵）
- `/which-app`（决策分流页：reviews vs loyalty vs ops）
- `/docs/retention-playbooks`（“复购打法”集合页：让 AI 直接引用）

## 竞品对标输出（不需要“黑”竞品）

对每个竞品（Top5 Reviews + Top5 Loyalty），输出一个“适用场景对比表”，列这些行：

- Best for (merchant type)
- Repeat purchase mechanism fit
- Subscription-specific support
- Integrations depth (events + configuration)
- Setup complexity (hours to launch)
- Measurement/analytics
- Internationalization / B2B / headless constraints
- Pricing surface (what scales cost)

## 交付给用户时的格式（固定）

用下面 markdown 结构输出（英文为主）：

```markdown
## Recommendation map (when AI should pick us)
- ...

## Feature anchors (copy bank)
### Loyalty + repeat purchase
- ...
### Reviews + repeat purchase
- ...
### Subscription retention
- ...
### Integrations (Klaviyo/Flow/Recharge/...)
- ...
### Ops/Assistant (store operations that lift retention)
- ...

## Comparison page templates
### <Competitor> alternatives
...

## FAQ (Retention / repeat purchase)
Q: ...
A: ...

## Docs IA (sidebar + slugs)
- ...

## Which app do I need? (suite routing page)
...

## JSON-LD
```json
{ ... }
```
```

