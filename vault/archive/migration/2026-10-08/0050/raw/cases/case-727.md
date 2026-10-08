## Case 727 — A Case taken back closes its Frontier line as orchestration sets it

> **context:**
> When a newer Case replaces an earlier one in the same session, `case-schema.md` says that the Frontier line the earlier Case closed is closed again by the replacing Case. That holds when a Case is built again under a new number: the line then names the new number. It does not hold when the person takes back a ratified Case. The main agent then writes a short Case that puts the targets off and replaces the Case taken back. But `orchestration.md` closes the line of a sprint item `[-] … · sprint · defer` and the line of a backlog item `[-] … · backlog · kept`, and neither closer names the short Case; when a part of the Case stays in the plan, the line keeps `· case N` (cases 713, 723.1). Pre-spec found this as F5 of Case 713, and Case 722.3 put `rule-case-protocol` off again for it, so the page holds `decision-case-722.3` in its `deferred_by`. The person chose to keep the general sentence and add the take-back as an exception that points to `orchestration.md`, so the closers of a take-back stand in one file only. A Grep for `closed again|closes again|close again` over `vault/wiki/`, `.claude/`, `guppi/` and `tests/` printed `vault/wiki/brief.md`, `vault/wiki/case-schema.md` and `vault/wiki/rules/rule-case-protocol.md`; the hit in the brief only reports this item, and the librarian writes the brief again. The Case takes up the deferred decision, so its decision line carries `{supersedes:case 722.3}` and names the page by an `update`; this sets `decision-case-722.3` `superseded`, and the change of Splitting that the History of the page records for 722.3 stays on the page, since a mark removes no text. No Estimate is touched: `estimate-case-protocol-loaded` checks after the render that `case-schema.md` equals the Render, and `estimate-orchestration-takes-back-a-ratified-case` already checks the closers of a take-back; neither Criterion speaks of a change that this Case makes, so both stand, and `estimate-case-protocol-case-form` speaks of the form of a Case file, not of the Frontier.

> **problem:**
> `case-schema.md` says that a Frontier line is always closed again by the Case that replaces the earlier one. A Case taken back from a sprint or a backlog item closes its line by a closer that names no Case, and so the schema contradicts `orchestration.md`.

> **recommend:**
> - **How the sentence on the Frontier line is fixed**
>   - Recommended: (a) keep the sentence and add the take-back as an exception that points to `orchestration.md`.
>   - Answer: agreed, (a).
> - **What checks that the fix is done**
>   - Recommended: (a) no new check; `estimate-case-protocol-loaded` checks the render and `estimate-orchestration-takes-back-a-ratified-case` keeps checking the behaviour.
>   - Answer: agreed, (a).

> **given:**
> `rule-case-protocol`: the page whose Render holds the sentence on the Frontier line.
> **＋** `vault/wiki/case-schema.md`: the file rendered from `rule-case-protocol`.
> **＋** `rule-orchestration`: the rule that sets the closers of the line of a Case taken back.

> **when:**
> `case-guppi` reads `vault/wiki/case-schema.md`, rendered from `rule-case-protocol`, on a Case that replaces an earlier Case in its own session.

> **then:**
> The schema says that a Frontier line the earlier Case closed is closed again by the replacing Case.
> **＋** The schema says that the line of the item of a Case taken back closes as `rule-orchestration` sets it for a take-back.
> **－** The schema does not list the closers of a take-back.

> **tasks:**
> - [ ] update `rule-case-protocol`
>   - old: `a Frontier line it closed is closed again by the superseding Case, and pre-spec catches a superseded Case still in the plan (case 299.1)`
>   - new: `` a Frontier line it closed is closed again by the superseding Case, but the line of the item of a Case taken back closes as `orchestration.md` sets it for a take-back (cases 713, 727), and pre-spec catches a superseded Case still in the plan (case 299.1) ``
>   - change: `the take-back is an exception to the Frontier line closed again by the superseding Case, its closer set in orchestration.md (case 727, supersedes the defer of 722.3)`
> - [ ] `uv run guppi render`: `vault/wiki/case-schema.md`

> **ratification:**
> ```
> - decision[case 727][update][rule-case-protocol]{ref:rule-case-protocol}{supersedes:case 722.3}
> ```
