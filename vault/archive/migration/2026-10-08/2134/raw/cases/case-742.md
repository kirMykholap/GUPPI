## Case 742 — The Insight on a ratified line never withdrawn is closed

> **context:**
> The ledger only grows, so the decision line of a first ratification is never withdrawn. A Case built again with a target dropped or renamed, or in another shape, needs a new number whose line supersedes the old one. `insight-ledger-ratified-line-never-withdrawn` records that only the Spec hook found such a build. Case 671.1 set it `actioned`: the check of the file of a Case sends back a ratified Case built again without the item of one of its lines, with the new number and the marks, and `estimate-case-check-sends-back-a-ratified-case-without-a-target` checks it. The check also sends back a ratified Case built again in another shape under its old number (case 610.1), and `estimate-case-check-sends-back-a-ratified-case-in-another-shape` checks it. The Insight was opened again on 2026-10-07 by its one live child, `lesson-case-build-splits-a-ratified-leaf-case`: asked to add a second behaviour to ratified Case 713, which had no sub-cases, `case-guppi` split it, undid the split and built Case 719 to supersede it. The root cause of that lesson is that `rule-case-build` set no step for such a fix. Case 725.1, in session 2114 of 2026-10-07, after that lesson, added the step: such a fix is built as a new top-level Case beside the ratified one, and `estimate-case-build-writes-the-case`, read `passed` on 2026-10-08, checks it in its Criterion. Its Criterion stands, since this Case changes no behaviour. A Grep of `^root_cause:.*(ratified|new number|supersed|rebuil|built again|decision line)` over `vault/wiki/lessons/` printed 13 files. Read by their `root_cause` lines, only `lesson-case-build-splits-a-ratified-leaf-case` records a ratified Case built again with a target dropped, renamed or added under its old number. `lesson-case-build-emptied-the-file-of-a-ratified-case` records the file left behind by such a build, an instruction that case 725.1 changed too. `lesson-case-check-refuses-a-rebuild-under-a-new-number`, `lesson-case-check-store-keeps-sub-cases-a-rebuild-dropped` and `lesson-prespec-parent-of-superseded-sub-cases` are children of the Insight that Case 740 actions. The others record other causes. So no lesson with this root cause has come since case 725.1. The person chose to set the Insight `actioned`, with `addressed_by` naming `decision-case-725.1`, the latest decision that fixed the pattern, as `rule-insights-schema` asks. That Decision page exists, so the field takes the quoted wikilink, as Case 740 of this session writes it for its own Insight. `estimate-insights-schema-checked` checks that an `actioned` Insight carries one `addressed_by`, and its Criterion stands. When the Insight is `actioned`, the cascade of `uv run guppi generate` archives its `clustered` lesson. Case 739 of this session notes an `update` of a page this cascade archives; this Case updates no lesson. Cases 740 and 741 of this session action two other Insights and touch no page of this Case. A Grep of `insight-ledger-ratified-line-never-withdrawn` over `vault/wiki/` printed `vault/wiki/backlog.md`, `vault/wiki/log.md` and `vault/wiki/lessons/lesson-case-build-splits-a-ratified-leaf-case.md`; over `guppi/` it printed nothing. `backlog.md` is written again by `uv run guppi backlog`, which lists only an `open` Insight. The `insight` field of the lesson still names the Insight, and the cascade archives the lesson. `log.md` is not read.

> **problem:**
> The Insight stands `open` in the backlog, though each way a ratified Case can come back changed now has a fix, and the Estimates of those fixes have passed.

> **recommend:**
> - **What happens to the Insight?**
>   - Recommended: (a) mark it `actioned`: one `update` sets the status and names the fix in `addressed_by`, the cascade archives its lesson, and the Insight stays live until the close of the sprint.
>   - Answer: agreed, (a).
> - **Which decision does the Insight name as its fix?**
>   - Recommended: (a) `decision-case-725.1`, the decision that added the step for a second behaviour and closed the cause of the last lesson.
>   - Answer: agreed, (a).

> **given:**
> `insight-ledger-ratified-line-never-withdrawn`: the Insight that is set `actioned`.
> **＋** `rule-insights-schema`: the rule that sets `addressed_by` of an `actioned` Insight to the latest decision that fixed it.
> **＋** `lesson-case-build-splits-a-ratified-leaf-case`: the `clustered` child of the Insight.
> **＋** `decision-case-725.1`: the Decision page of the latest fix of the pattern, which `addressed_by` names.
> **＋** `vault/wiki/backlog.md`: the list of open items, written by `uv run guppi backlog`.

> **when:**
> The librarian runs `uv run guppi generate` over the Spec of the session, then `uv run guppi backlog`.

> **then:**
> `insight-ledger-ratified-line-never-withdrawn` stands `actioned`, and its `addressed_by` names `decision-case-725.1`.
> **＋** The cascade of `uv run guppi generate` archives `lesson-case-build-splits-a-ratified-leaf-case`.
> **＋** `vault/wiki/backlog.md` no longer lists the Insight.
> **－** The `## Pattern` and `## Proposal` of the Insight do not change.

> **tasks:**
> - [ ] update `insight-ledger-ratified-line-never-withdrawn`
>   - set: `{status: actioned, addressed_by: "[[decision-case-725.1]]"}`
>   - change: `actioned: a ratified Case built again without one of its targets or in another shape goes back with a new number, and a second behaviour of a ratified Case with no sub-cases is built as a new Case beside it (cases 610.1, 671.1, 725.1)`

> **ratification:**
> ```
> - decision[case 742][update][insight-ledger-ratified-line-never-withdrawn]{ref:insight-ledger-ratified-line-never-withdrawn}
> ```
