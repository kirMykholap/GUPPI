## Case 678 — The Insight on one judgment in two copies is answered again

> **context:**
> `insight-harness-one-rule-implemented-twice-drifts` says that one judgment of the pipeline lives in two copies of code, which drift apart under a green suite. Case 360 answered it with `rule-one-judgment-one-implementation`, whose text stands in `CLAUDE.md`, and set it `actioned`. The synthesis of session 1343 reopened it: it added the lesson `lesson-orchestration-defer-supersedes-a-parent-without-its-sub-cases`, where the Spec hook read a `{supersedes:case N}` mark as N with its sub-cases, and `prespec` and `materialize` read it as N alone. Case 660 closed that drift as the rule asks: `materialize.in_family` is now the one reading, and `prespec.retired_by` imports it. So the page is open, with severity 1, only for a cause that is already fixed, and it stands in the backlog. The person agreed to set it `actioned` again, and chose that `addressed_by` names the Decision of this Case, the latest, as `rule-insights-schema` asks and as case 611 did for `insight-case-form-chat-form-read-by-no-script`. The History line names case 360 and case 660.
> The frame. `rule-one-judgment-one-implementation` does not change: its Purpose says that it actions this Insight (case 360), and that stays true. Its one Estimate, `estimate-one-judgment-one-implementation-followed`, stands `passed` from its reading of 2026-09-29. The reopening lesson, of 2026-10-05, records a later breach of its Criterion: two readings of one mark, where the Criterion asks that the predicate live in one module and both sides import it. Case 660 closed that breach by `materialize.in_family`, which `prespec.retired_by` imports, so the Criterion holds again of the code. This Case changes no code and no promise, so it does not take that reading again, and the Estimate stands. The cascade of `generate` archives the `clustered` child of an `actioned` Insight, which `estimate-generate-cascades` checks; `guppi backlog` lists only an `open` Insight, which `estimate-backlog-renders` checks. Their Criteria speak of this change and stay true, so they stand and check this Case; the Case creates no Estimate. A Grep `insight-harness-one-rule-implemented-twice-drifts` over `vault/wiki/` printed 5 files: `vault/wiki/backlog.md`, `vault/wiki/log.md`, `vault/wiki/estimates/estimate-synthesis-clusters.md`, `vault/wiki/lessons/lesson-orchestration-defer-supersedes-a-parent-without-its-sub-cases.md` and `vault/wiki/rules/rule-one-judgment-one-implementation.md`. `guppi backlog` writes `backlog.md` again, and `log.md` is history, so these two were not read. The hit in `estimate-synthesis-clusters` is in its Result, a past reading, and it stays true. The lesson keeps its `insight` field, and the cascade archives it. The rule's Purpose stays true, as said above.

> **problem:**
> The Insight stays open in the backlog, but the rule in `CLAUDE.md` answers its pattern, and a fix that followed the rule has already closed the drift of its new lesson.

> **recommend:**
> - **Which decision should the Insight name as its answer?**
>   - Recommended: (a) this Case, the latest decision, with its History line naming the rule and the fix.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: the pre-spec report found that the Case did not name `estimate-one-judgment-one-implementation-followed`, the Estimate of the rule that answers the Insight; the person agreed to its fix.
>   - Taken: `context` names that Estimate and says why it stands: case 660 fixed the later breach, and this Case does not take its reading again.

> **given:**
> `insight-harness-one-rule-implemented-twice-drifts`: the Insight that this Case sets `actioned`.
> **＋** `rule-insights-schema`: the shape of an Insight, which asks for one `addressed_by`, the latest.
> **＋** `rule-one-judgment-one-implementation`: the rule in `CLAUDE.md` that answers the pattern.
> **＋** `lesson-orchestration-defer-supersedes-a-parent-without-its-sub-cases`: the `clustered` child that reopened the Insight.
> **＋** `rule-page-generation`: the rule of `guppi generate` and its cascade.
> **＋** `vault/wiki/backlog.md`: the backlog, which lists each `open` Insight.

> **when:**
> `guppi generate` of `rule-page-generation` applies the decision of this Case and runs its cascade, and `guppi backlog` writes `vault/wiki/backlog.md`.

> **then:**
> `insight-harness-one-rule-implemented-twice-drifts` stands `actioned`, and its `addressed_by` names the Decision of this Case.
> **＋** `lesson-orchestration-defer-supersedes-a-parent-without-its-sub-cases` becomes `archived` by the cascade.
> **＋** `vault/wiki/backlog.md` no longer lists the Insight under `## Deferred`.
> **－** `rule-one-judgment-one-implementation` does not change.

> **tasks:**
> - [ ] update `insight-harness-one-rule-implemented-twice-drifts`
>   - set:
>     ```
>     {status: actioned, addressed_by: decision-case-678}
>     ```
>   - change: `actioned: rule-one-judgment-one-implementation in CLAUDE.md answers the pattern (case 360), and materialize.in_family, the one reading of a supersedes mark that prespec imports, closed the drift of the reopening lesson (case 660) (case 678)`

> **ratification:**
> ```
> - decision[case 678][update][insight-harness-one-rule-implemented-twice-drifts]{ref:insight-harness-one-rule-implemented-twice-drifts}
> ```
