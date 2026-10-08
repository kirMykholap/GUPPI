## Case 728 — The check of the put-off reply reads the new Render at Retro

> **context:**
> When the person puts off a decision whose Frontier item comes from neither the sprint nor the backlog, the main agent shows a short Case in the same reply, carries its ledger line, closes the line `[-] … · defer case N` and asks what comes next. `estimate-orchestration-defers-in-one-reply` checks that reply, and its `method` waits for such a reply live. Case 723.2 of session 2114 replaced its Criterion; in that session only the sprint items C1 and C2 were put off, so Retro set it `failed` with the result "not read" (ledger L22 of 2114), and by the cascade `rule-orchestration` went from `built` to `draft`, though no fault was seen. `rule-retro` reads an Estimate of a rule whose Render a Case of the Spec changes from the new Render in the Spec, and a Grep for `^(method|status|checked):` over `vault/wiki/estimates/` with the glob `estimate-orchestration-*` printed the lines of 16 files: the method of `estimate-orchestration-shows-the-built-case`, `estimate-orchestration-takes-back-a-ratified-case`, `estimate-orchestration-marks-each-round-of-a-batch` and `estimate-orchestration-says-when-a-rendered-change-lands` reads that new Render at Retro, and every Estimate but this one stands `passed`. The person chose the same method for this Estimate, and chose to set it `passed` by their decision now, since `case-guppi` read the Render of `rule-orchestration` as it stands against the Criterion and found each line of the Criterion stated there: the short form, the `LEDGER` block with no tool call after it, the Frontier with its closer, the closing question, the corrected wording, the `**Waiting:**` turn of a dropped Case, no short defer at Retro, and the sprint and backlog closers. The update writes the Criterion back unchanged, so the promise stands and nothing is signed twice; `estimate-prespec-hook-reports-a-method-that-waits-for-another-session` already checks that a new `method` holds only what runs in its own session, and its Criterion stands, since this Case adds no form of method. With every live Estimate of `rule-orchestration` `passed`, the cascade of `generate` sets the rule `built`. By `rule-retro`, the Retro of this session neither reads this Estimate nor sets it `failed`, since its update sets `passed` by the person's decision.

> **problem:**
> `estimate-orchestration-defers-in-one-reply` can be read only on a live reply that puts off a decision of another source than the sprint or the backlog. A session with no such reply leaves it `failed` with no fault seen, and keeps `rule-orchestration` in `draft`.

> **recommend:**
> - **What the method reads**
>   - Recommended: (b) read the new Render of `rule-orchestration` in the Spec at Retro of the session that changes the Estimate, as sibling Estimates do.
>   - Answer: agreed, (b).
> - **How the check leaves `failed`**
>   - Recommended: (a) set it `passed` now by the person's decision, its Criterion written back unchanged, after the Render as it stands was read against the Criterion.
>   - Answer: agreed, (a).

> **given:**
> `estimate-orchestration-defers-in-one-reply`: its `method` is set and its status is set by the person's decision.
> **＋** `rule-orchestration`: the rule whose Render the method reads.
> **＋** `rule-retro`: the rule that reads at Retro the Estimates the session changes.

> **when:**
> The Retro of a session whose Spec replaces the Criterion of `estimate-orchestration-defers-in-one-reply` takes its reading.

> **then:**
> Retro reads the new Render of `rule-orchestration` in the Spec against that Criterion and writes the result in the estimate line.
> **－** The reading does not wait for a decision that the person puts off in Plan Mode.

> **tasks:**
> - [ ] update `estimate-orchestration-defers-in-one-reply`
>   - set:
>     ```
>     status: passed
>     checked: 2026-10-08
>     method: "by hand at Retro of the session that changes it: the new Render of rule-orchestration in the Spec, read against the Criterion, recorded in the estimate line"
>     ```
>   - sections.Criterion:
>     ```
>     When:
>     In Plan Mode, the person asks in the chat to put off a decision: an item of `raw/<date>/<hi HHMM>/frontier.md` whose source is neither the sprint nor the backlog, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.
>
>     Then:
>     In the same reply the agent shows the Case in the short form — `context`, `problem` and a fence tagged `then` with one `defer` item per target, no other section — and carries its `LEDGER` block, one `defer` line per target, with no tool call after it.
>     **＋** The agent writes nothing of the Case into the plan file: the `Stop` hook of `rule-spec-write` writes it.
>     **＋** The person's words asking for the defer are its ratification: no question asks for it.
>     **＋** The reply shows the Frontier of `raw/<date>/<hi HHMM>/frontier.md` after the Case, with the line of the item closed `[-] … · defer case N`.
>     **＋** While a line under `## Cases` of `raw/<date>/<hi HHMM>/frontier.md` is open, a question follows the Frontier and ends the reply: which open item is next.
>     **＋** When no line under `## Cases` is open before `/pre-spec`, the question whether to go on to `/pre-spec` follows the Frontier and ends the reply. The agent calls `/pre-spec` only after the person says to go on.
>     **＋** When no line under `## Cases` is open after `/pre-spec`, no question follows: the reply ends with the Frontier, and the hook of `rule-prespec-onward` sends the agent on with the loop after the findings.
>     **＋** A wording the person corrects is a new short Case with `{supersedes:case N}` on its line, shown the same way.
>     **＋** When the item has a Case that `case-guppi` built and that has no decision line in `raw/<date>/<hi HHMM>/ledger.md`, the drop goes to that `case-guppi` first and the turn of the person's words ends with one `**Waiting:**` line; the short Case, its `LEDGER` block and the Frontier come in the turn that the answer `**Dropped:**` opens.
>     **－** No text follows the question, or the Frontier when no question stands.
>     **－** Retro writes no short defer: what it would put off is a line of `## For the next session` of `raw/<date>/<hi HHMM>/handoff.md`.
>     **－** An item of the sprint put off, its line of `raw/<date>/<hi HHMM>/frontier.md` closed `[-] … · sprint · defer`, and an item of the backlog left as it stands, closed `[-] … · backlog · kept`, are not this moment: they take no short Case and no ledger line but for the short Case of a take-back of a ratified Case, which is the moment of `estimate-orchestration-takes-back-a-ratified-case`, and a reply that closes only such lines with no take-back is the moment of `estimate-orchestration-shows-the-frontier-after-a-closed-line`.
>     ```
>   - sections.Result:
>     ```
>     2026-10-08, the person's decision, case 728: the Render of rule-orchestration as it stands read against the Criterion; each line of the Criterion is stated in it
>     2026-10-07, Retro, not read: its method needs a decision of a source other than the sprint or the backlog put off with its line closed [-] … · defer case N; in session 2114 only the sprint items C1 and C2 were put off, closed · sprint · defer, which the method excludes
>     ```
>   - change: `the method reads the new Render of rule-orchestration in the Spec at Retro; passed by the person's decision, the Criterion written back unchanged (case 728)`

> **ratification:**
> ```
> - decision[case 728][update][estimate-orchestration-defers-in-one-reply]{ref:rule-orchestration}
> ```
