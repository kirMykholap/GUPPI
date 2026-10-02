## Case 600 — The Insight on the loop after the pre-spec findings is closed by the rules that set the loop

> **context:**
> After `/pre-spec` reports findings, the Cases they touch go back to their `case-guppi` agents. The rebuilt Cases, the rounds those agents raise and the main agent's own questions must then reach the person. In session 2042 none of this had a rule, and two failures came of it. The main agent passed on the answers of four `case-guppi` agents one at a time, and the person could not tell what to answer (`lesson-prespec-findings-relayed-piecemeal-lose-the-person`). A second run of the skill sent `ask-guppi` over the whole plan again for eight minutes, and nobody told the person first (`lesson-prespec-second-run-dispatches-ask-guppi-again`). The librarian joined the two lessons in `insight-prespec-after-findings-loop-unruled`, which is still `open` in `backlog.md`.
>
> Each part of the Insight's pattern and Proposal was checked against the rules of today:
> - How the rebuilt Cases, the rounds and the main agent's own questions reach the person. The Render of `rule-prespec`, written whole by case 561.1, sets the loop of case 561.2. Case 581.1 added the waiting line, and case 595.1 holds everything until the person answers every question of the report. The questions of the report take the grill-me shape (case 561.13). `estimate-prespec-gathers-the-answers-after-findings` passed by hand at the `/pre-spec` of session 1202, with one list numbered by Case and the four rebuilt Cases shown in one reply.
> - What a second run checks. The same Render sends `ask-guppi` at the first run of the session only. After the rebuilt Cases are ratified, the agent does not call `/pre-spec` again: it runs the script check alone, and the hook on the exit runs it too (cases 561.1, 561.3). `estimate-prespec-reconciles` passed by hand in session 1237: the check ran once more, and `ExitPlanMode` followed with no second `/pre-spec`.
> - What a run costs. The Proposal asked a second run to state its cost before it starts. No costly later run remains. Case 561 recorded that this question falls away, and the person confirmed it in this Case.
>
> Cases 580 and 581 left the Insight open because no rule covered waits on a `case-guppi` outside the loop. Case 598.1 of this session now sets those waits for a batch. This Case marks the Insight `actioned`. Its `addressed_by` names `decision-case-561.1`, the decision that wrote the loop and the first-run-only dispatch and so closed both lessons. `rule-insights-schema` sets that field to one decision, the one that fixed the pattern. Case 595.1 later changed one step of the loop and said nothing of a later run. The cascade of `generate` then archives the two `clustered` lessons. The Insight stays live, so a new lesson with the same cause reopens it. The Insight has no `deferred_by`, so no `{supersedes:case N}` block is needed. The Case makes no `create`, so the vault query was not run.
>
> Searches of the frame:
> - A Grep of `insight-prespec-after-findings-loop-unruled` over the repository, run again after the finding of `/pre-spec`, printed 21 files:
>   - under `vault/wiki/`: `backlog.md`, where the line comes from the `open` status; `log.md`, which was not read; and the two children
>   - under `vault/raw/2026-10-02/2049/`: `ledger.md`, `frontier.md`, `cases/case-598.md` and `cases/case-600.md`
>   - under `vault/raw/2026-10-02/1834/`: `spec.md`, `materialize.yaml` and `cases/case-595.md`
>   - under `vault/archive/migration/`: `2026-10-01/1441/raw/spec.md`, `materialize.yaml`, `cases/case-581.md` and `cases/case-580.md`; `2026-09-30/2356/raw/spec.md`, `materialize.yaml`, `frontier.md` and `cases/case-561.md`; `2026-10-01/1237/raw/frontier.md`; and `2026-09-30/2042/raw/materialize.yaml`
> - The Grep does not search `vault/raw/2026-10-02/event_log.md`, so that file is not among its hits.
> - A Grep of `^(root_cause|pattern):.*(pre-spec|prespec|findings|built again|rebuilt)` over `vault/wiki/` printed 13 files. Besides the Insight and its two lessons, the lessons it printed were these: `lesson-spec-write-keeps-the-body-of-a-case-that-gains-sub-cases`, `lesson-case-build-closes-a-sprint-item-without-the-sprint-page`, `lesson-prespec-judged-a-pair-by-its-anchor-alone`, `lesson-ledger-ratification-with-a-new-item-lost-its-block` and `lesson-lint-schema-body-table-one-section-per-row`. Their root causes concern other mechanisms, so no lesson of this cause was recorded after case 561. The other hits were Insights of other patterns.
>
> Case 598 of this session replaces the Criterion of `estimate-prespec-gathers-the-answers-after-findings`, and case 595.1 left it `pending`. This Case changes no text of that page or of `rule-prespec`. Case 599 actions a sibling Insight in the same way, by the same `generate` run, on another page. Case 597 does not touch this moment.
>
> Two Estimates already check the fix, `estimate-prespec-gathers-the-answers-after-findings` and `estimate-prespec-reconciles`. Their Criteria stand, because this Case changes no behaviour. `estimate-insights-schema-checked` speaks of the schema file, which this Case does not change.

> **problem:**
> The rules of `/pre-spec` now set the loop after its findings and rule out a costly second run, and the checks of both passed once. The Insight still stands `open` in the backlog only because no decision marked it `actioned`. The questions were whether every part of its cause is closed, which decision to name as the fix, and whether to close it now.

> **recommend:**
> - **Is the cost part closed by removing the costly run?**
>   - Recommended: (a) closed. No costly later run remains, since a later step is only the script check. Neither lesson concerned the first run.
>   - Answer: agreed with the recommendation, (a).
> - **Which decision should the note name as its fix?**
>   - Recommended: (a) `decision-case-561.1`, the decision that wrote the loop and the later-run rule and so closed both failures.
>   - Answer: agreed with the recommendation, (a).
> - **Close the note now, or after the loop's check passes again?**
>   - Recommended: (a) close now. The rule stands, its check passed once on real questions, and a recurrence reopens the note.
>   - Answer: agreed with the recommendation, (a).

> **given:**
> `insight-prespec-after-findings-loop-unruled` — the Insight, set `actioned`
> **＋** `decision-case-561.1` — the decision that wrote the loop after the findings and the first-run-only dispatch, named by `addressed_by`; unchanged
> **＋** `lesson-prespec-findings-relayed-piecemeal-lose-the-person` and `lesson-prespec-second-run-dispatches-ask-guppi-again` — its `clustered` children
> **＋** `rule-insights-schema` — the shape of an Insight, `addressed_by` and the cascade; unchanged
> **＋** `guppi/generate.py` — applies the `update` and runs the cascade; unchanged
> **＋** `vault/wiki/backlog.md` — lists the `open` Insights
> **＋** `rule-prespec` and `.claude/skills/pre-spec/SKILL.md` — set the loop after the findings and the later run; unchanged
> **＋** `estimate-prespec-gathers-the-answers-after-findings` and `estimate-prespec-reconciles` — the checks of that rule; unchanged

> **when:**
> `uv run guppi generate` applies the `update` of `insight-prespec-after-findings-loop-unruled`, and someone then reads `vault/wiki/backlog.md`.

> **then:**
> `insight-prespec-after-findings-loop-unruled` has `status: actioned` and `addressed_by` naming `decision-case-561.1`.
> **＋** The cascade of `guppi/generate.py` archives `lesson-prespec-findings-relayed-piecemeal-lose-the-person` and `lesson-prespec-second-run-dispatches-ask-guppi-again`.
> **＋** `vault/wiki/backlog.md` holds no line for the Insight.
> **－** The Insight is not archived: it stays live, and a new lesson with its cause reopens it.
> **－** `rule-prespec`, `.claude/skills/pre-spec/SKILL.md`, `estimate-prespec-gathers-the-answers-after-findings` and `estimate-prespec-reconciles` do not change.

> **tasks:**
> - [ ] update `insight-prespec-after-findings-loop-unruled`
>   - set: `{status: actioned, addressed_by: "[[decision-case-561.1]]"}`
>   - change: `actioned: the pre-spec skill gathers the rounds and the rebuilt Cases after the findings into one list and one showing, and sends ask-guppi at the first run only, with no second call (cases 561.1, 561.2); the cost of a second run falls away with it; no lesson of the cause since (case 600)`

> **ratification:**
> ```
> - decision[case 600][update][insight-prespec-after-findings-loop-unruled]{ref:insight-prespec-after-findings-loop-unruled}
> ```
