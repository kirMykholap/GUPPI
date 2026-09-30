## Case 547 — The Frontier is shown after every closed Frontier line in Plan Mode

> **context:**
> The Frontier is the list of open items for the session, kept in the session's `frontier.md`. The agent closes a line of it when the item ends. The paragraph of `rule-case-protocol` on the reply that acknowledges a ratification tells the agent to end that reply with a `## Frontier` heading, the lines of `frontier.md` and the question which item is next (case 167). The paragraph on the short form tells the agent to do the same after a defer the person asks for (case 461). No text covers a line closed in any other way. Examples are an `A` line closed by the person's answer, a `W` line closed by a reading, a `C` line that needs no decision, and items closed `[-] … · sprint · defer` or `[-] … · backlog · kept`. In session 1736 the agent closed A1 (`estimate-permissions`) and C3 (`estimate-glossary-terms-defined`) as `· work`. Each reply ended with only the question which item is next, so the person did not see what was still open.
> The Case adds one sentence to the paragraph "Plan Mode and the Frontier" of the Render of `rule-case-protocol`, which renders into `vault/wiki/case-schema.md`, and creates an Estimate for the new promise. The Estimate has a `ref`, so no vault query on its existence was run. A Glob for `estimate-case-protocol-shows-the-frontier*` found no page, so the slug is free.
> Frame. `estimate-case-protocol-acknowledging-reply` and `estimate-case-protocol-defers-in-one-reply` stand. Their triggers are a ratification and a defer, and the new sentence excludes both. `estimate-case-protocol-loaded` checks only that the file equals the Render (case 378.5). The case-form, ledger-line-form and shows-the-built-case Estimates speak of other things.
> Pre-spec found that the first reply of `/hi` can also close `W` lines by a reading. `rule-skill-hi` sets its own form for that reply: the Cases as a checklist with their detail and `- near` lines, `Backlog: N items` last, the Work as one block, and then a wait for the person to pick the order. The rule of this Case therefore holds only after the first reply of `/hi`, and that reply keeps its form. With that bound, the Criterion of `estimate-hi-writes-frontier`, which sets the chat form of the `/hi` reply, stays true and is not touched.
> Search. A Grep for `Frontier` over `.claude/` and over `glossary.md` found no other sentence the change makes false. In `.claude/skills/hi/SKILL.md`, the reply to an `A` answer after the first reply carries a `LEDGER` block and ends in text. A Frontier after the block keeps that true, so `estimate-hi-takes-its-readings` stands. The hits in `.claude/skills/work/SKILL.md`, `.claude/skills/pre-spec/SKILL.md`, `.claude/skills/carry/SKILL.md` and `.claude/agents/librarian-guppi.md` speak of Work Mode, pre-spec and the handoff, where no Frontier is shown. The glossary rows "Plan Mode" and "`/hi`, Frontier" say nothing about what a later reply shows.
> The backlog item `rule-orchestration` (deferred by cases 424 and 546) would move the acknowledging reply into a rule of its own. It stays deferred. This sentence moves with the rest of that paragraph when the item is taken up.

> **problem:**
> A reply that closes a Frontier line with no ratification and no defer does not show the Frontier. The person does not see what is still open before choosing the next item. The rule names the Frontier only for the reply after a ratification and the reply after a defer.

> **recommend:**
> - **When must the agent show the Frontier after it closes a line?**
>   Recommended: every closed line from `/hi` to the end of Plan Mode; Work Mode and Retro unchanged.
>   Answer: agreed, as recommended; the first reply of `/hi` is excluded by the change below.
> - **What does the Frontier look like in these replies?**
>   Recommended: the same form as after a ratification, with the last question as after a defer: which item is next, or whether to run `/pre-spec` when no Cases line is open.
>   Answer: agreed, as recommended.
> - **How is the new behaviour checked?**
>   Recommended: a new Estimate on `rule-case-protocol`; `estimate-case-protocol-acknowledging-reply` stays as it is.
>   Answer: agreed, as recommended.
> - **Should the larger item `rule-orchestration` that was put off come into this Case?**
>   Recommended: leave it in the backlog; this Case adds one sentence to `case-schema.md` through `rule-case-protocol`.
>   Answer: agreed, as recommended.
> - **Change**
>   Asked: at pre-spec, the rule holds after the first reply of `/hi`, and that reply keeps its own form set by `rule-skill-hi`; `rule-skill-hi` enters `given`.
>   Taken: `when`, `then` and the new sentence start after the first reply of `/hi`; a `－` line of `then` keeps the form of that reply; `rule-skill-hi` is in `given`.
> - **Change**
>   Asked: at pre-spec, `context` says that `estimate-hi-writes-frontier` stays true with this bound.
>   Taken: `context` says so.

> **given:**
> `rule-case-protocol`: its Render paragraph "Plan Mode and the Frontier" takes the new sentence
> **＋** `vault/wiki/case-schema.md`: the Render of `rule-case-protocol`, loaded by `/hi`
> **＋** `rule-skill-hi`: sets the form of the first reply of `/hi`, which this Case leaves as it is
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier of the session, whose lines the agent closes
> **＋** `/pre-spec`: the check that closes Plan Mode, named in the last question
> **＋** `estimate-case-protocol-shows-the-frontier-after-a-closed-line`: the new Estimate of the promise
> **＋** `estimate-case-protocol-acknowledging-reply`: the form of the Frontier that the new reply repeats

> **when:**
> After the first reply of `/hi` and before the end of Plan Mode, the agent closes a line of `raw/<date>/<hi HHMM>/frontier.md` in a reply that carries no ratification and no defer. Examples are an `A` line closed by the person's answer, a `W` line closed by a reading, a `C` line that needs no decision, or an item closed `[-] … · sprint · defer` or `[-] … · backlog · kept`.

> **then:**
> The reply ends with the heading `## Frontier` and the lines of `raw/<date>/<hi HHMM>/frontier.md` as a checklist, in the form that `estimate-case-protocol-acknowledging-reply` sets. The closed lines are folded into one, the open ones stand one per line with a short title, and the lines put off stand as they are closed.
> **＋** A question follows the Frontier and ends the reply: which open item is next, or, when no line under `## Cases` of `raw/<date>/<hi HHMM>/frontier.md` is open, whether to run `/pre-spec`.
> **＋** A reply that closes several lines shows one Frontier, after its `LEDGER` block when it carries one.
> **－** The first reply of `/hi` keeps the form that `rule-skill-hi` sets, the lines it closes included.
> **－** A line closed in Work Mode or at Retro shows no Frontier.
> **－** The reply that acknowledges a ratification and the reply that carries a defer keep their own form, as `estimate-case-protocol-acknowledging-reply` sets it.

> **tasks:**
> - [ ] update `rule-case-protocol`
>   - old: `(case 451.1). Plan Mode does not end`
>   - new: `` (case 451.1). A reply after the first reply of `/hi` and before the end of Plan Mode that closes a line of `frontier.md` with no ratification and no defer — an `A` line by the person's answer, a `W` line by a reading, a `C` line that needs no decision, an item closed `[-] … · sprint · defer` or `[-] … · backlog · kept` — ends as the acknowledging reply ends: a heading `## Frontier`, the lines of `frontier.md` as a checklist in its form, and, last, the question which open item is next or, when no line under `## Cases` is open, whether to run `/pre-spec`; a reply that closes several lines shows one Frontier; the first reply of `/hi` keeps the form `rule-skill-hi` sets, and a line closed in Work Mode or at Retro shows none (case 547). Plan Mode does not end ``
>   - change: `a reply after the first reply of /hi that closes a Frontier line in Plan Mode with no ratification and no defer shows the Frontier and the question which item is next`
> - [ ] create `estimate-case-protocol-shows-the-frontier-after-a-closed-line`
>   - type: `estimate`
>   - ref: `rule-case-protocol`
>   - kind: `QA`
>   - purpose: `Whether a reply after the first reply of /hi that closes a Frontier line in Plan Mode with no ratification and no defer ends with the Frontier and the question which item is next`
>   - method: `by hand, in a later session: the first reply in Plan Mode after the first reply of /hi that closes a line of frontier.md with no ratification and no defer, read against the Criterion`
>   - tags: `[session, workflow]`
> - [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
> - [ ] read `estimate-case-protocol-shows-the-frontier-after-a-closed-line`

> **ratification:**
> ```
> - decision[case 547][update][rule-case-protocol]{ref:rule-case-protocol}
> - decision[case 547][create][estimate-case-protocol-shows-the-frontier-after-a-closed-line]{ref:rule-case-protocol}{tags:session,workflow}
> ```
