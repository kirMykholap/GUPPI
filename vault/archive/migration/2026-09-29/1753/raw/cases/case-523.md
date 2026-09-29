## Case 523 — The question after a defer stands as written

> **context:**
> When the person puts off an item in Plan Mode, the agent answers in one reply. The reply holds a short Case, the Frontier with that line closed, and one question at the end. The question asks which open item is next. When no line under `## Cases` is open, it asks whether to run `/pre-spec` instead. The reading of `estimate-case-protocol-defers-in-one-reply` failed in session 1134. There the defer of Case 509 closed the last Cases line, and the question asked whether to take the open W readings, not whether to run `/pre-spec`. The text of `rule-case-protocol` was already right at that time. The gap was that the W readings had no set moment before Retro. That session filled the gap with case 508: a W line now closes at `/hi`, in Work Mode or at Retro. The item came to session 1432, and the person put it off as Case 518. In the same session, Cases 517 and 518 closed the last Cases line. That reply ended with the question whether to run `/pre-spec`, with no text after it. Nobody wrote a reading for it.
>
> In one round the person made two choices. The failure in session 1134 was a slip whose cause is gone, so the text of `rule-case-protocol` stays as it is. The `method` of the Estimate now names a defer that leaves no Cases line open, because only such a defer tests the question that failed.
>
> The frame and the vault's answer:
> - `rule-case-protocol` carries `deferred_by` Case 518. This Case retires that defer: its decision line names the page with `{supersedes:case 518}`, and the `update` has only a `change`.
> - Case 521.4 of this session changes the short-form paragraph of the same page. This Case changes no text there.
> - `rule-skill-hi` gives the W lines their moments, and the question in case 461 needs no change.
> - The `when` and `then` of this Case are the current Criterion of `estimate-case-protocol-defers-in-one-reply`, word for word. The promise is not signed in a second wording.
> - The Estimate update names the `method` alone. Under `rule-case-protocol` its Criterion and its `failed` status do not change. Because a decision line of this session updates the Estimate, its reading waits for a later session.
> - The new `method` keeps the `by hand` form of `vault/wiki/estimates/schema.yaml`, as the old one did. So a finding of lint on the form of a method of a MOC, if there is one, does not change.
> - No other Estimate of `rule-case-protocol` has a Criterion that speaks of the question after a defer. No hook changes, and the Case creates no page, so no vault query was run.
>
> Not done: no sentence on the W list is added to the Render. No hook checks the question.

> **problem:**
> The rule on the question after a defer is under a defer, and its Estimate reads as failed. The rule text was right, and the one wrong question came from a gap that is now closed. The `method` of the Estimate also lets a defer that leaves Cases lines open count as a reading, and such a defer never tests the question that failed.

> **recommend:**
> Keep the text of `rule-case-protocol` and retire the defer of Case 518. Narrow the `method` to the first defer after the render that leaves no line under `## Cases` open. A reading then tests the `/pre-spec` question, and the Criterion stays as it is. The rejected options were a sentence on the W list in the Render, which would rewrite the promise and delay its reading, and a hook written for one failure.

> **given:**
> `rule-case-protocol` — the rule of the short-form Case and of the reply that shows a defer.
> **＋** `estimate-case-protocol-defers-in-one-reply` — the promise of the defer reply, and the page whose `method` this Case sets.
> **＋** `raw/<date>/<hi HHMM>/frontier.md` — the Frontier the reply shows and the Cases lines the question looks at.
> **＋** `rule-spec-write` — the `Stop` hook that writes the short-form Case into the plan file and `spec.md`.
> **＋** `spec.md` — the Spec of the session, at `raw/<date>/<hi HHMM>/spec.md`.
> **＋** `/pre-spec` — the check the question offers.
> **＋** `rule-prespec` — the rule of that check.

> **when:**
> The person asks in the chat to defer an item, in Plan Mode or at Retro.

> **then:**
> In the same reply the agent shows the Case in the short form — `context`, `problem` and a fence tagged `then` with one `defer` item per target, no other section — and carries its `LEDGER` block, one `defer` line per target, with no tool call after it.
> **＋** The agent writes nothing of the Case into the plan file or `spec.md`: the `Stop` hook of `rule-spec-write` writes it.
> **＋** The person's words asking for the defer are its ratification: no question asks for it.
> **＋** In Plan Mode the reply shows the Frontier of `raw/<date>/<hi HHMM>/frontier.md` after the Case, with the line of the item closed `[-] … · defer case N`.
> **＋** In Plan Mode a question follows the Frontier and ends the reply: which open item is next, or, when no line under `## Cases` of `raw/<date>/<hi HHMM>/frontier.md` is open, whether to run `/pre-spec` of `rule-prespec`.
> **＋** A wording the person corrects is a new short Case with `{supersedes:case N}` on its line, shown the same way.
> **－** No text follows that question.
> **－** At Retro no Frontier is shown.

> **tasks:**
> - [ ] update `rule-case-protocol`
>   - change: `the defer taken up: the question after a defer stands as written, the failure of session 1134 a slip whose cause case 508 removed (case 523, supersedes 518)`
> - [ ] update `estimate-case-protocol-defers-in-one-reply`
>   - set: `{method: "by hand, the first defer the person asks for after the render that leaves no line under ## Cases of frontier.md open"}`
>   - change: `the method reads a defer that closes the last Cases line, the branch that failed; the Criterion and the failed status stand (case 523)`
> - [ ] read `estimate-case-protocol-defers-in-one-reply` — by hand in a later session after the render: the first defer that closes the last Cases line, read in the chat against the Criterion

> **ratification:**
> ```
> - decision[case 523][update][rule-case-protocol]{ref:rule-case-protocol}{supersedes:case 518}
> - decision[case 523][update][estimate-case-protocol-defers-in-one-reply]{ref:rule-case-protocol}
> ```
