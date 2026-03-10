# Evals (skill-creator convention)

This skill’s test cases and assertions follow the [skill-creator](https://github.com/anthropics/skills) convention for "with skill / without skill" comparison and quantitative assertion scoring.

## evals.json structure

- **skill_name**: `fitness-plan-flows`
- **evals**: Array; each item includes
  - **id**: Sequence number (1-based)
  - **prompt**: User task description (real scenario)
  - **expected_output**: Summary of expected output
  - **files**: List of input files (usually empty)
  - **assertions**: Array of objectively verifiable assertions; each has `name`, `description` for grader to pass/fail and fill `evidence`

## Assertion design

- Each assertion can be judged independently: whether the output contains a given structure/field/wording.
- Align with SKILL output format: Flow map, flow specs (Goal/Trigger/Exit/Timeline/plan type/Messages/KPIs), plan content list, implementation mapping.
- Grading uses `text` (for description), `passed` (true/false), `evidence` (quote from output).

## Workspace and iterations

Eval results live in **sibling to the skill**: `fitness-plan-flows-workspace/`, organized by iteration:

- `iteration-1/<eval_name>/`: First run; `eval_name` matches the descriptive name for each eval (see `eval_metadata.json` in workspace).
- After each run, that directory gets `with_skill/outputs/`, `without_skill/outputs/`, and optionally `grading.json`, `timing.json`.
- Aggregation and viewer generation are described in the workspace `README.md`.
