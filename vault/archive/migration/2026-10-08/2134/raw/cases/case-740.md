## Case 740 — The Insight on Case ids that leave only by a supersedes line is closed

> **context:**
> `insight-case-check-a-case-id-leaves-only-by-a-supersedes-line` gathers three lessons with one cause: a check kept a Case id in view until a `{supersedes:case N}` mark of the ledger named it. In `lesson-prespec-parent-of-superseded-sub-cases`, a parent with no ledger lines of its own stayed a finding after each of its sub-cases was superseded. In `lesson-case-check-store-keeps-sub-cases-a-rebuild-dropped`, the store of the check of a case file kept sub-cases that a rebuild had dropped. In `lesson-case-check-refuses-a-rebuild-under-a-new-number`, a build under a new number was refused while the build it replaced stood in the plan. Each failure is fixed in the code today. The module docstring of `guppi/prespec.py` says that the plan is compared with no other file, since the ratified copy is gone (case 445.2). `other_blocks` of `guppi/casecheck.py` leaves out a stored Case that the file of its top-level Case no longer holds, by `left_by_its_file` (case 722.1), and a Case that a mark on a decision line of the answer's own file names, by `ratification_records` (case 725.2). `remove_superseded` of `guppi/ratified.py` removes a parent from the plan once marks retire each of its sub-cases, by `retired_whole` of `guppi/prespec.py` (case 722.2). Three Estimates check these fixes and all three stand `passed`: `estimate-case-check-sends-back-a-clash-with-another-case`, `estimate-case-check-leaves-out-a-case-the-file-supersedes` and `estimate-spec-write-removes-a-superseded-case`. Their Criteria stand, since this Case changes no code. The person chose to set the Insight `actioned` with `addressed_by` naming `decision-case-725.2`, the latest decision that fixed the pattern, as `rule-insights-schema` asks. That Decision page already exists, so the field takes the quoted wikilink. `estimate-insights-schema-checked` checks that an `actioned` Insight carries one `addressed_by`, and its Criterion stands. When the Insight is `actioned`, the cascade of `uv run guppi generate` archives its three `clustered` lessons. Case 739 of this session notes an `update` of a page that this cascade archives; this Case updates none of the three lessons. A Grep of `insight-case-check-a-case-id-leaves-only-by-a-supersedes-line` over `vault/wiki/` printed `vault/wiki/backlog.md`, `vault/wiki/log.md` and the three lessons; over `guppi/` it printed nothing. `backlog.md` is written again by `uv run guppi backlog`, which drops an Insight that is not `open`. The `insight` field of each lesson still names the Insight correctly, and the cascade archives the lessons. `log.md` is not read.

> **problem:**
> The Insight stands `open` in the backlog, though the code now fixes each failure it records, and the Estimates of those fixes have passed.

> **recommend:**
> - **What happens to the Insight**
>   - Recommended: (a) close it and name the last earlier fix: set it `actioned` with `addressed_by` naming `decision-case-725.2`, and change no code.
>   - Answer: agreed, (a).

> **given:**
> `insight-case-check-a-case-id-leaves-only-by-a-supersedes-line`: the Insight that is set `actioned`.
> **＋** `rule-insights-schema`: the rule that sets `addressed_by` of an `actioned` Insight to the latest decision that fixed it.
> **＋** `lesson-prespec-parent-of-superseded-sub-cases`: a `clustered` child of the Insight.
> **＋** `lesson-case-check-store-keeps-sub-cases-a-rebuild-dropped`: a `clustered` child of the Insight.
> **＋** `lesson-case-check-refuses-a-rebuild-under-a-new-number`: a `clustered` child of the Insight.
> **＋** `decision-case-725.2`: the Decision page of the latest fix of the pattern, which `addressed_by` names.
> **＋** `vault/wiki/backlog.md`: the list of open items, written by `uv run guppi backlog`.

> **when:**
> The librarian runs `uv run guppi generate` over the Spec of the session, then `uv run guppi backlog`.

> **then:**
> `insight-case-check-a-case-id-leaves-only-by-a-supersedes-line` stands `actioned`, and its `addressed_by` names `decision-case-725.2`.
> **＋** The cascade of `uv run guppi generate` archives `lesson-prespec-parent-of-superseded-sub-cases`, `lesson-case-check-store-keeps-sub-cases-a-rebuild-dropped` and `lesson-case-check-refuses-a-rebuild-under-a-new-number`.
> **＋** `vault/wiki/backlog.md` no longer lists the Insight.
> **－** The `## Pattern` and `## Proposal` of the Insight do not change.

> **tasks:**
> - [ ] update `insight-case-check-a-case-id-leaves-only-by-a-supersedes-line`
>   - set: `{status: actioned, addressed_by: "[[decision-case-725.2]]"}`
>   - change: `actioned: each check now leaves out a Case id that a rebuild dropped or that every superseded sub-case retires, without waiting for a supersedes line of the ledger (cases 445.2, 722.1, 722.2, 725.2)`

> **ratification:**
> ```
> - decision[case 740][update][insight-case-check-a-case-id-leaves-only-by-a-supersedes-line]{ref:insight-case-check-a-case-id-leaves-only-by-a-supersedes-line}
> ```
