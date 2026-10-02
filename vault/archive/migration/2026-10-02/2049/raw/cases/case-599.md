## Case 599 — The Insight on the main agent's own questions is closed by the rule that gave them the grill-me shape

> **context:**
> At `/pre-spec`, the main agent sometimes needs a decision from the person. In sessions 0248 and 1306 it asked for those decisions in a layout of its own. The questions had no numbered title line, no `**Now:**` line and no recommended answer. At that time only the rounds of `case-guppi` had to use the grill-me shape. The librarian put the two lessons together in `insight-prespec-main-agent-question-off-the-grill-me-shape`, and that Insight is still `open` in `backlog.md`.
>
> Case 561.13 closed the cause in two places. `## Who builds a Case` of `orchestration.md` gives the question shape of `.claude/skills/grill-me/SKILL.md` to each question the main agent puts to the person itself: at `/pre-spec`, at `/hi` and at a stop of Work Mode. `.claude/skills/pre-spec/SKILL.md` asks for each decision of its report in that same shape. Case 595 moved the sentence into `rule-orchestration` and did not change its meaning. The second half of the Insight's Proposal was that the first lesson must stand where the next `/pre-spec` reads it. That half is covered too: the shape is now a rule in the files that the main agent loads at `/hi` and at `/pre-spec`.
>
> No decision marked the Insight `actioned`, so it stayed in the backlog. This Case does that. Its `addressed_by` names `decision-case-561.13`, because the schema of `rule-insights-schema` sets that field to the decision that fixed the pattern. The cascade of `generate` then archives the two `clustered` lessons. The Insight stays live, so that a new lesson with the same cause reopens it.
>
> Searches of the frame:
> - A Grep of the Insight's slug over `vault/wiki/` printed these files:
>   - `backlog.md`, where the line comes from the `open` status
>   - `log.md`, not read
>   - `lesson-prespec-report-decisions-off-the-question-shape.md` and `lesson-prespec-report-questions-still-off-the-shape.md`, its children
> - A Grep of `^(root_cause|pattern):.*(shape|grill)` over `vault/wiki/` printed 5 files: the Insight, its two lessons, `insight-harness-yaml-entry-shape-assumed.md` and `lesson-hooks-posttooluse-stdout-not-in-context.md`. The last two concern other causes, so no new lesson of this cause was recorded after case 561.13.
> - A Grep of `grill-me` over `.claude/` printed `agents/case-guppi.md`, `skills/grill-me/SKILL.md`, `skills/wait-what/SKILL.md` and `skills/pre-spec/SKILL.md`. Over `vault/wiki/rules/` it printed 7 files: `rule-skill-grill-me`, `rule-prespec`, `rule-orchestration`, `rule-case-build`, `rule-case-protocol`, `rule-plan-mode` and `rule-skill-wait-what`. None of them is made false by closing the Insight, and this Case changes none of them.
>
> The Insight has no `deferred_by`, so no `{supersedes:case N}` block is needed. The Case makes no `create`, so the vault query was not run.
>
> Case 598 of this session changes `rule-orchestration` to add a batch, and each question of the batch also takes the grill-me shape. It does not touch the sentence of case 561.13. This Case changes no text of that page.
>
> `estimate-orchestration-asks-in-the-grill-me-shape` already checks the fix. Its Criterion covers each question the main agent asks itself at `/pre-spec`, at `/hi` and at a stop of Work Mode. It passed by hand at the close of session 1441. Case 595.13 moved it and set it `pending`. Its Criterion stands, because this Case changes no behaviour. `estimate-insights-schema-checked` speaks of the schema file, which is not changed.

> **problem:**
> The cause of the Insight is closed by a ratified rule, and the check of that rule passed once. The Insight still stands `open` in the backlog only because no decision marked it `actioned`. The question was whether to close it now, and which decision to name as the fix.

> **recommend:**
> - **Should the Insight be marked closed now, and which decision should it name as the fix?**
>   - Recommended: (a) close it now and name the decision that wrote the rule, `decision-case-561.13`. The cause is closed in `orchestration.md` and in the pre-spec skill, the check passed once on real questions at `/pre-spec`, and the schema says `addressed_by` names the decision that fixed the pattern.
>   - Answer: (a).

> **given:**
> `insight-prespec-main-agent-question-off-the-grill-me-shape` — the Insight, set `actioned`
> **＋** `decision-case-561.13` — the decision that gave the main agent's own questions the grill-me shape, named by `addressed_by`; unchanged
> **＋** `lesson-prespec-report-decisions-off-the-question-shape` and `lesson-prespec-report-questions-still-off-the-shape` — its `clustered` children
> **＋** `rule-insights-schema` — the shape of an Insight, `addressed_by` and the cascade; unchanged
> **＋** `guppi/generate.py` — applies the `update` and runs the cascade; unchanged
> **＋** `vault/wiki/backlog.md` — lists the `open` Insights
> **＋** `rule-orchestration` and `.claude/skills/pre-spec/SKILL.md` — give the grill-me shape to the main agent's own questions; unchanged
> **＋** `estimate-orchestration-asks-in-the-grill-me-shape` — the check of that rule; unchanged

> **when:**
> `uv run guppi generate` applies the `update` of `insight-prespec-main-agent-question-off-the-grill-me-shape`, and someone then reads `vault/wiki/backlog.md`.

> **then:**
> `insight-prespec-main-agent-question-off-the-grill-me-shape` has `status: actioned` and `addressed_by` naming `decision-case-561.13`.
> **＋** The cascade of `guppi/generate.py` archives `lesson-prespec-report-decisions-off-the-question-shape` and `lesson-prespec-report-questions-still-off-the-shape`.
> **＋** `vault/wiki/backlog.md` holds no line for the Insight.
> **－** The Insight is not archived: it stays live, and a new lesson with its cause reopens it.
> **－** `rule-orchestration`, `.claude/skills/pre-spec/SKILL.md` and `estimate-orchestration-asks-in-the-grill-me-shape` do not change.

> **tasks:**
> - [ ] update `insight-prespec-main-agent-question-off-the-grill-me-shape`
>   - set: `{status: actioned, addressed_by: "[[decision-case-561.13]]"}`
>   - change: `actioned: orchestration.md and the pre-spec skill give the grill-me shape to each question the main agent puts to the person itself (case 561.13); no lesson of the cause since (case 599)`

> **ratification:**
> ```
> - decision[case 599][update][insight-prespec-main-agent-question-off-the-grill-me-shape]{ref:insight-prespec-main-agent-question-off-the-grill-me-shape}
> ```
