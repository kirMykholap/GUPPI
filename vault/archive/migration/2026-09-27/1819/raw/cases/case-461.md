## Case 461 — A defer reply in Plan Mode ends with the Frontier and the question of what comes next

> **context:**
> When the person asks to put off an item, the main agent writes the short Case and its `LEDGER` line in one reply. The `Stop` hook of `rule-spec-write` then writes the short Case under `## Deferred`. `estimate-case-protocol-defers-in-one-reply` promises that in Plan Mode "the reply ends with the Frontier". It failed on the reading of session 1745 and failed again on the reading of session 1255. In 1255, the defer reply for Cases 454–456 was right in every other part. But the defers came at the close of Plan Mode, when no line was open, and a paragraph that proposed `/pre-spec` with a question followed the Frontier. The edit of the plan file seen in 1745 is now refused by the hook of Case 445.1.
> The Render of `rule-case-protocol` says only that the agent "asks nothing about it", meaning the defer. The acknowledging reply ends with "the question which item is next". So the defer reply is the only reply that must end with no question, even when `/pre-spec` is the only next step. In the rounds the person chose these points. The promise changes, not the reply: the defer reply ends as the acknowledging reply does, and no hook is added. `rule-orchestration` stays in `backlog.md` as it stands. The acknowledging reply is not changed. It has the same gap when the Case closes the last open line, and that is left not done: its reading (Frontier W8) can show whether it matters.
> Of the other Estimates of the rule, `estimate-case-protocol-loaded` promises only that the file equals the Render (case 378.5). `estimate-case-protocol-shows-the-built-case` speaks of the short form only as written by the main agent in English. `estimate-case-protocol-acknowledging-reply` speaks of the acknowledging reply. None of them is touched. The `replace` pair of this Case is in the paragraph "The short form — deferred decisions". The pairs of Case 458 are in "Who builds a Case" and "Language", so the anchors do not meet. No `create`, so no vault query ran.

> **problem:**
> The Criterion forbids any text after the Frontier in a defer reply. At the close of Plan Mode no line is open, and the person needs to know what comes next. So the agent writes a question after the Frontier, and the Estimate fails on a reply that did what the person needed. The wording that fails is the promise, and a stricter Render would fail again for the same reason.

> **recommend:**
> Make the defer reply in Plan Mode end with the Frontier and then a question. The question asks which open item is next or, when no line under `## Cases` is open, whether to run `/pre-spec`, and no text follows it. Replace the Criterion of `estimate-case-protocol-defers-in-one-reply` whole to hold this, and keep its method. This matches the reply to its sibling, the acknowledging reply. The rejected option is a `Stop` hook that refuses text after the Frontier. It stays for later, in case the text rule fails again.

> **given:**
> `rule-case-protocol` — its Render, the paragraph "The short form — deferred decisions", where the defer reply is described
> **＋** `vault/wiki/case-schema.md` — the file rendered from `rule-case-protocol`
> **＋** `estimate-case-protocol-defers-in-one-reply` — the promise of the defer reply, its Criterion replaced whole
> **＋** `rule-spec-write` — the `Stop` hook that writes the short Case into the plan file and `spec.md`
> **＋** `raw/<date>/<hi HHMM>/frontier.md` — the Frontier whose line the defer reply closes
> **＋** `rule-prespec` — `/pre-spec`, the next step when no line under `## Cases` is open

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
>   - old: `` in Plan Mode then the Frontier with the line closed `[-] … · defer case N` — and asks nothing about it; ``
>   - new: `` in Plan Mode then the Frontier with the line closed `[-] … · defer case N` and, last, a question — which open item is next or, when no line under `## Cases` is open, whether to run `/pre-spec` — with no text after it; it asks nothing about the defer itself (case 461); ``
>   - change: `the defer reply in Plan Mode ends with the Frontier and a question of what comes next, the open item or /pre-spec (case 461)`
> - [ ] update `estimate-case-protocol-defers-in-one-reply`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — in Plan Mode a question of what comes next follows the Frontier and ends the defer reply (case 461)`
> - [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
> - [ ] read `estimate-case-protocol-defers-in-one-reply` — by hand, the first defer the person asks for after the render

> **ratification:**
> ```
> - decision[case 461][update][rule-case-protocol]{ref:rule-case-protocol}
> - decision[case 461][update][estimate-case-protocol-defers-in-one-reply]{ref:estimate-case-protocol-defers-in-one-reply}
> ```
