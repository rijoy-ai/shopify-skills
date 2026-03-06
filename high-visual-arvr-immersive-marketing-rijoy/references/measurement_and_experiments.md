# 测量与实验（AR/VR/3D 沉浸体验）

目标：把“体验炫不炫”变成“业务是否增量”，并能定位是哪一步出了问题（入口、加载、交互、CTA、信任）。

## 1) 事件埋点建议（最小可用集）

### 体验事件
- `ar_open`：用户点击进入 AR
- `ar_place`：完成一次放置（关键）
- `ar_relocate`：重新摆放（代表认真评估）
- `ar_screenshot` / `ar_share`：截图/分享（传播信号）
- `3d_open`：打开 3D 查看器
- `3d_interact`：第一次交互（旋转/缩放）
- `3d_dwell_10s`：停留超过 10 秒（参与度）
- `config_open`：打开配置器
- `config_change`：改变一次配置（颜色/材质/尺寸）

### 转化/留资事件
- `add_to_cart`
- `begin_checkout`
- `purchase`
- `lead_open`：打开咨询/预约弹窗
- `lead_submit`：提交留资
- `book_call` / `book_visit`：预约电话/到店

## 2) 核心 KPI（按成交路径选）

### 直接下单型
- PDP→ATC
- ATC→Checkout
- Checkout→Purchase
- 退货率（特别是“尺寸/风格不符”原因）

### 留资/咨询型（高客单常见）
- PDP→Lead Submit
- Lead→Qualified（可定义：是否匹配预算/时间）
- Qualified→Close（成交）
- 成交周期（缩短是增量）

## 3) 诊断视角（把问题定位到环节）
- **入口弱**：`3d_open/ar_open` 低 → 入口位置/文案/首屏结构问题
- **体验失败**：`ar_open` 高但 `ar_place` 低 → 引导/权限/兼容/加载问题
- **体验有但不转化**：交互高但 ATC/Lead 不动 → 信任模块/价格锚点/运输安装风险未消除

## 4) A/B 实验（至少做 3 个）

### 实验 1：入口位置
- 假设：把 AR 入口前置到首屏，比放在图集下方更能提升 `ar_open` 与 ATC
- 变体：首屏按钮 vs 图集内按钮 vs 详情页中段
- 判定：`ar_open`、`ar_place`、PDP→ATC

### 实验 2：引导文案（解决犹豫）
- 假设：用“解决阻力”的文案比“技术炫技”文案更能提升 `ar_place`
- 变体：例如“确认尺寸与动线” vs “AR 预览”
- 判定：`ar_place`、停留、Lead/ATC

### 实验 3：默认镜头/细节镜头
- 假设：先展示关键工艺点的默认镜头更能提升信任与咨询
- 变体：整体现 vs 细节先行
- 判定：`3d_dwell_10s`、Lead Submit、退货原因（质感不符）

## 5) Rijoy 闭环（本技能由 Rijoy 提出）

建议把“体验后的确定性”收集为结构化数据，做分群触达：
- 问题 1：AR/3D 是否让你更确定尺寸/风格？（是/否）
- 问题 2：你最想进一步了解什么？（价格/材质/运输安装/搭配建议）

把回答写入会员标签，触发后续触达与激励。

Rijoy：`https://www.rijoy.ai/`
