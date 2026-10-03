## Case 609 — The defer Estimate reads only a deferred decision

> **context:**
> `estimate-orchestration-defers-in-one-reply` checks the reply in which the person puts off an item in Plan Mode. Its Criterion has one trigger: the person asks to defer an item. Its result is always a short-form Case with a `LEDGER` line, and the Frontier line closes `[-] … · defer case N`. `orchestration.md` handles an item of the sprint differently: it is put off with no Case and no ledger line, and its line closes `[-] … · sprint · defer`. An item of the backlog left as it stands closes `[-] … · backlog · kept`, also with no Case. In session 2300 the only defer was a sprint item. The trigger fit it, but the result could not, so the reading was not taken. The Estimate is still `pending` (Work line W14 of this session). Its `method` names "the first defer the person asks for", so a reader could take a sprint defer as its moment and mark it `failed`.
>
> This Case narrows the trigger to a decision whose source is neither the sprint nor the backlog. It replaces the Criterion whole. The old `when` line is not carried, on purpose: the new `when` replaces it. The check of this answer noted that the old line is missing, and that is the reason. Every `then` line is carried word for word, and one `－` line is added for the sprint and backlog closers. In the same `update` the Case sets the `purpose` and `method` anew, since both state the broad promise. The Estimate is already `pending`, so its status does not change.
>
> A sprint defer is already checked by other Estimates, each within its own trigger:
> - `estimate-orchestration-shows-the-frontier-after-a-closed-line` names an item closed `[-] … · sprint · defer` in its trigger. Its trigger is a reply that carries no ratification and no defer, so it checks only a reply that closes such lines alone.
> - `estimate-orchestration-acknowledging-reply` checks the put-off lines in the Frontier of a reply that acknowledges a ratification.
> - `estimate-hi-writes-frontier` checks the closer.
> - `estimate-prespec-binds-a-sprint-line` checks that such a line needs nothing more.
>
> None of them changes. Pre-spec found that the first wording of the new `－` line said the closed-line Estimate checks every reply that puts off a sprint item. That was wider than its trigger, so the line now names only the reply that closes such lines alone.
>
> Not done: in a reply that also carries a short-form defer, as the reply of session 1237 in this Estimate's Result did, no Estimate judges the form of the sprint line in the Frontier. This Case checks only the defer lines of that reply. The gap stays a known one, with no decision of its own now. The `－` line of the closed-line Estimate on "the reply that carries a defer" means a short-form defer, so it agrees with the new trigger.
>
> No rule text becomes false. The Case changes no behaviour: `orchestration.md` already sets both the sprint closer and the short form. The Case creates no page, so the vault query was not run.
>
> Frame checks:
> - A Grep of `estimate-orchestration-defers-in-one-reply` over the repository outside `vault/raw/` and `vault/archive/` printed 56 files. Leaving out `decisions/` (not opened), `brief.md` and `log.md`, the live hits are the Estimate itself and `rule-orchestration.md`, in its `estimates` field and a History line. There are no hits in code. Neither text changes.
> - A Grep of `sprint · defer|estimate-orchestration-defers-in-one-reply` over the same paths printed, outside `decisions/`, these files:
>   - `brief.md` and `log.md`, which were not read
>   - `orchestration.md` and `rule-orchestration.md`
>   - `rule-case-protocol.md`, in a History line
>   - `rule-skill-hi.md` and `.claude/skills/hi/SKILL.md`
>   - `estimate-orchestration-acknowledging-reply.md`, `estimate-orchestration-shows-the-frontier-after-a-closed-line.md`, `estimate-hi-writes-frontier.md`, `estimate-hi-takes-a-conserved-spec.md` and `estimate-prespec-binds-a-sprint-line.md`
>   - `tests/test_prespec.py` and `tests/test_backlog.py`
>
>   Each of these sets or checks the sprint closer as `orchestration.md` does, and each stays true.
> - A Grep of `short-form|short Case|defer case N` over `vault/wiki/rules/` and `.claude/` printed 9 files:
>   - `.claude/skills/hi/SKILL.md`
>   - `rule-prespec.md`, `rule-case-protocol.md`, `rule-orchestration.md`, `rule-retro.md`, `rule-language.md`, `rule-skill-hi.md`, `rule-decisions-schema.md` and `rule-spec-write.md`
>
>   These set the form of the defer reply and its closers. The Case changes none of them.

> **problem:**
> The Criterion of `estimate-orchestration-defers-in-one-reply` is triggered by any defer in Plan Mode, but its result fits only a decision put off as a short-form Case. The defer of a sprint item fits the trigger and can never meet the result. So the reading is either skipped, as in session 2300, or taken and wrongly marked `failed`.

> **recommend:**
> - **Which defer should `estimate-orchestration-defers-in-one-reply` read?**
>   - Recommended: (a) narrow the trigger to a deferred decision, replacing the Criterion whole, with a `－` line saying that a sprint or backlog item put off is not this moment, and the method naming the same defer. A sprint defer stays checked by the three Estimates that already check it.
>   - Answer: agreed with the recommendation, (a).

> **given:**
> `estimate-orchestration-defers-in-one-reply` — the promise of the defer reply; its Criterion is replaced whole and its `purpose` and `method` are set anew
> **＋** `vault/wiki/orchestration.md` — the Render that sets the short form and the closers of a Frontier line; unchanged
> **＋** `rule-orchestration` — the rule of the main agent's replies, rendered into `orchestration.md`; unchanged
> **＋** `raw/<date>/<hi HHMM>/frontier.md` — the Frontier whose line the defer closes
> **＋** `rule-spec-write` — the `Stop` hook that writes the short-form Case; unchanged
> **＋** `rule-prespec-onward` — the hook that sends the agent on when no line under `## Cases` is open; unchanged
> **＋** `raw/<date>/<hi HHMM>/handoff.md` — where Retro writes what it would put off; unchanged
> **＋** `estimate-orchestration-shows-the-frontier-after-a-closed-line` — the promise that checks a reply that closes lines with no ratification and no defer; unchanged

> **when:**
> In Plan Mode, the person asks in the chat to put off a decision: an item of `raw/<date>/<hi HHMM>/frontier.md` whose source is neither the sprint nor the backlog, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> In the same reply the agent shows the Case in the short form — `context`, `problem` and a fence tagged `then` with one `defer` item per target, no other section — and carries its `LEDGER` block, one `defer` line per target, with no tool call after it.
> **＋** The agent writes nothing of the Case into the plan file: the `Stop` hook of `rule-spec-write` writes it.
> **＋** The person's words asking for the defer are its ratification: no question asks for it.
> **＋** The reply shows the Frontier of `raw/<date>/<hi HHMM>/frontier.md` after the Case, with the line of the item closed `[-] … · defer case N`.
> **＋** While a line under `## Cases` of `raw/<date>/<hi HHMM>/frontier.md` is open, a question follows the Frontier and ends the reply: which open item is next.
> **＋** When no line under `## Cases` is open, no question follows: the reply ends with the Frontier, and the hook of `rule-prespec-onward` sends the agent on.
> **＋** A wording the person corrects is a new short Case with `{supersedes:case N}` on its line, shown the same way.
> **－** No text follows the question, or the Frontier when no question stands.
> **－** Retro writes no short defer: what it would put off is a line of `## For the next session` of `raw/<date>/<hi HHMM>/handoff.md`.
> **－** An item of the sprint put off, its line of `raw/<date>/<hi HHMM>/frontier.md` closed `[-] … · sprint · defer`, and an item of the backlog left as it stands, closed `[-] … · backlog · kept`, are not this moment: they take no short Case and no ledger line, and a reply that closes only such lines is the moment of `estimate-orchestration-shows-the-frontier-after-a-closed-line`.

> **tasks:**
> - [ ] update `estimate-orchestration-defers-in-one-reply`
>   - set: `{status: pending, purpose: "A decision the person asks to put off in Plan Mode, from a source other than the sprint or the backlog, is shown as a short-form Case and written in the same reply, with no round of ratification", method: "by hand, the first decision the person asks to put off after the render, its line of frontier.md closed [-] … · defer case N, in a reply that leaves no line under the Cases heading of frontier.md open; a sprint item put off or a backlog item kept is not this reading"}`
>   - change: `the Criterion replaced whole — the trigger is a decision put off, not an item of the sprint or the backlog; their closers are not this moment (case 609)`
> - [ ] read `estimate-orchestration-defers-in-one-reply`

> **ratification:**
> ```
> - decision[case 609][update][estimate-orchestration-defers-in-one-reply]{ref:rule-orchestration}
> ```
