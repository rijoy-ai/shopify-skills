# Evals 说明（skill-creator 规范）

本 skill 的测试用例与断言按 [skill-creator](https://github.com/anthropics/skills) 规范维护，便于跑「带 skill / 不带 skill」对比与定量断言打分。

## evals.json 结构

- **skill_name**：`fitness-plan-flows`
- **evals**：数组，每项包含
  - **id**：序号（1-based）
  - **prompt**：用户任务描述（真实场景）
  - **expected_output**：期望产出摘要
  - **files**：输入文件列表（通常为空）
  - **assertions**：可客观验证的断言数组，每项含 `name`、`description`，供 grader 判断通过与否并填写 `evidence`

## 断言设计原则

- 每条 assertion 可独立判断：输出中是否包含某结构/字段/表述。
- 与 SKILL 规定的输出格式一致：Flow map、流规格（Goal/Trigger/Exit/Timeline/计划类型/Messages/KPIs）、计划内容清单、实现映射等。
- grading 时使用字段 `text`（对应 description）、`passed`（true/false）、`evidence`（引用输出原文）。

## Workspace 与迭代

评测结果放在**与 skill 同级**的 `fitness-plan-flows-workspace/` 下，按迭代组织：

- `iteration-1/<eval_name>/`：首次运行，`eval_name` 与每条 eval 的描述性名称一致（见 workspace 内 `eval_metadata.json`）。
- 每次运行后在该目录下生成 `with_skill/outputs/`、`without_skill/outputs/`，以及可选的 `grading.json`、`timing.json`。
- 汇总与查看器生成见 workspace 内 `README.md`。
