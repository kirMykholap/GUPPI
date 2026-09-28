## Case 465 — The method of estimate-carry-over-writes names the render check and a reading by hand

> **context:**
> The carry skill `.claude/skills/carry/SKILL.md` is the Render of `rule-carry-over`. It is a prompt. After the person chooses "conserve" at the fork of `ExitPlanMode`, the agent reads the tree, rewrites the brief, writes `carry.md`, runs `guppi backlog` and commits. The `method` of `estimate-carry-over-writes` says "pytest over the skill's render, plus one live reading of a carried-over session". No test covers the skill: `pytest tests/test_render.py -k skill` deselects all 26 tests (brief of session 1819). What the Estimate promises is what the agent does after it reads the prompt, and pytest cannot run that.
> The Estimate is `pending`. Case 451.9 replaced its Criterion, and the live reading of that Criterion is still owed. `render --check` covers the `－` line "SKILL.md equals the Render". `tests/test_backlog.py` and `tests/test_materialize.py` cover the code that reads `carry.md`, under their own Estimates. `estimate-skill-grill-me-asks-in-rounds` gives a prompt skill the same kind of method: "uv run guppi render --check; by hand, …".
> In the frame I found no contradiction. `check_method` in `guppi/lint.py` passes a method that holds `by hand`. The `method` description in `vault/wiki/estimates/schema.yaml` asks for where and when a reading is taken, and the new text says both. The Criterion of `estimate-lint-checks-the-method` is about lint's behaviour, and this Case does not change lint. This Case changes only the `method` field. The Criterion and the status stay, so no other Estimate of `rule-carry-over` is touched. `rule-spec-box` stays out of the frame: nothing here makes a sentence of it false.
> In the round, the person agreed to: change the method and write no test; the proposed wording; change only `method`; keep `rule-spec-box` out.

> **problem:**
> The method of `estimate-carry-over-writes` names a pytest that does not exist and cannot check the promise. A reader who follows the method finds nothing to run. The reading stays owed, and the Estimate cannot be read as its method says.

> **recommend:**
> Set the `method` to `uv run guppi render --check` plus one reading by hand of the first `/carry` after the fork, and name what the reading checks. The render check covers the file, and the reading covers the behaviour. A test in `tests/test_render.py` would only repeat `render --check` or match sentences of the prompt. It would not check what the agent does, so I rejected it.

> **given:**
> `estimate-carry-over-writes` — the promise of the carry skill, whose `method` changes
> **＋** `rule-carry-over` — the rule whose Render the Estimate checks
> **＋** `.claude/skills/carry/SKILL.md` — the rendered skill that `render --check` compares
> **＋** `vault/wiki/brief.md` — the brief the carry skill rewrites
> **＋** `vault/wiki/backlog.md` — the backlog that `guppi backlog` writes during a carry
> **＋** `tests/` — the test folder, where no test covers the carry skill
> **＋** `guppi/lint.py` — `check_method` classifies the `method` of an Estimate
> **＋** `vault/wiki/estimates/schema.yaml` — the description of the `method` field

> **when:**
> A reader takes the reading of `estimate-carry-over-writes` by its `method`.
> **＋** `uv run guppi lint` reads the `method` of `estimate-carry-over-writes`.

> **then:**
> The `method` names `uv run guppi render --check`, and one reading by hand of the first `/carry` after the fork of `ExitPlanMode`: the tree, `vault/wiki/brief.md`, `carry.md`, `vault/wiki/backlog.md` and the commit.
> **＋** `check_method` gives `estimate-carry-over-writes` no `method` finding.
> **－** The `method` names no pytest and no file under `tests/`.
> **－** The Criterion and the `pending` status of `estimate-carry-over-writes` stay as they are.

> **tasks:**
> - [ ] update `estimate-carry-over-writes`
>   - set: `{method: "uv run guppi render --check; by hand, the first /carry after the fork of ExitPlanMode — the tree, vault/wiki/brief.md, carry.md, vault/wiki/backlog.md and the commit read"}`
>   - change: `the method names render --check and a reading by hand; no test targets the carry skill (case 465)`

> **ratification:**
> ```
> - decision[case 465][update][estimate-carry-over-writes]{ref:estimate-carry-over-writes}
> ```
