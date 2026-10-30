## Case 923 — The main agent states what a subagent did only from its transcript

> **context:**
> The main agent sometimes writes a fact that a source already holds from its own reading or impression, not from the source. `insight-orchestration-writes-from-its-own-reading` clusters two such slips. In `lesson-orchestration-claimed-a-reading-before-taking-it` the main agent said that no "modified since read" refusal came in the session, from its impression of the summaries of `case-guppi`, which do not show their tool errors, and read the transcripts only later. In `lesson-orchestration-retyped-a-ratification-line` it retyped a ledger line of a showing from its own reading of the defers, with the wrong `{supersedes:...}` mark, where the summary held the right one.
>
> The second slip is already covered. The Render of `rule-orchestration` says that the `ratification` of a showing holds the ledger lines as the summary holds them, `estimate-orchestration-shows-the-built-case` promises it, and the `Stop` check of `rule-case-check` refuses a showing that differs from the stored text, which is how that slip was caught. The Proposal of the Insight asks for such a check, and it already stands. The first slip broke only the general sentence of `rule-agent-writing` that a claim is no wider than the output it rests on. No text says where a fact about a subagent's tool calls comes from, and no check caught that slip. The person chose one sentence in the Render of `rule-orchestration`, placed after the sentence on the short form written with no dispatch, and a new Estimate on it. The Insight is set `actioned` by this Case, with the bare slug `decision-case-923` in `addressed_by`, as `rule-insights-schema` sets it. The existing Estimates of `rule-orchestration` speak of other promises, so their Criteria stand.
>
> A Grep for `written with no dispatch` over `vault/wiki/` printed `vault/wiki/orchestration.md` and `vault/wiki/rules/rule-orchestration.md`, so the anchor of the pair falls once on the Rule page. A Grep for `transcript` over the `*.md` files of `.claude/` printed only `.claude/skills/hi/SKILL.md`, whose readings at `/hi` read no transcript of an earlier session. The new sentence speaks only of a subagent of the session, so it does not cover that moment. The report of `.claude/skills/pre-spec/SKILL.md` gives the list of what the `ask-guppi` run did not check, and by `.claude/agents/ask-guppi.md` the last lines of that list name each rule a search of `ask-guppi` broke. That is a subagent's own report of its calls, which the new sentence lets the main agent pass on marked as that report, so the report of `/pre-spec` stands as it is. A Grep for `orchestration` over `.guppi/tests/` printed `test_orchestration.py`, `test_casecheck.py`, `test_onward.py` and `test_ratified.py`. Only `test_orchestration.py` reads `vault/wiki/orchestration.md` live, and its functions `example`, `store_of_showing` and `defer_records` read only the blocks tagged `showing` and `defer`, which the new sentence does not touch. A Grep for the slug of the Insight over `vault/wiki/`, `.guppi/` and `.claude/` printed `brief.md`, `backlog.md`, `log.md` and the two lesson pages. The lesson pages name the Insight in their `insight` field, which stays true. A Glob `vault/wiki/**/estimate-orchestration-states-*.md` printed nothing, so the new slug is free. The ledger of the session holds no `lesson[error]` line and no `{addresses:` mark, so this Case closes no lesson of this session.

> **problem:**
> No text says that a fact about what a subagent did comes from its transcript. The main agent stated such a fact from the subagents' summaries, which do not show their tool errors.

> **recommend:**
> - **What the Case does with the Insight**
>   - Recommended: (b) add one sentence to `orchestration.md`: a fact about what a subagent did is stated only after the main agent reads it in that subagent's transcript, and mark the Insight as dealt with.
>   - Answer: agreed, (b).
> - **Which Estimate checks the new sentence**
>   - Recommended: (a) a new Estimate, `estimate-orchestration-states-a-subagent-fact-from-its-transcript`, read by hand at the Retro of this session and after the first reply under the new Render that states such a fact.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: after a finding of `/pre-spec`, the person chose that the sentence tells two cases apart: a fact the main agent states as its own of what a subagent did needs that subagent's transcript, and what a subagent reports of its own calls the main agent may pass on with no transcript, marked as that subagent's report; the report of `/pre-spec` stays as it is.
>   - Taken: the new sentence, the `then` and the `purpose` of the new Estimate now tell the two cases apart.

> **given:**
> `rule-orchestration`: the rule of the main agent's work, rendered into `vault/wiki/orchestration.md`.
> **＋** `vault/wiki/orchestration.md`: the file the main agent loads at `/hi`.
> **＋** `estimate-orchestration-states-a-subagent-fact-from-its-transcript`: the new Estimate of the sentence.
> **＋** `insight-orchestration-writes-from-its-own-reading`: the Insight this Case actions.

> **when:**
> The main agent, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`, states in a reply what a subagent of the session did: a tool call it made, a tool error it met, or a hook that refused its call.

> **then:**
> Before a reply that states such a fact as its own, the main agent has read that fact in the transcript of that subagent.
> **＋** The reply states no such fact as its own from the summary of the subagent alone.
> **－** What a subagent reports of its own calls, such as the rules a search of `ask-guppi` broke, the main agent may pass on with no transcript, marked as the report of that subagent.
> **－** A ledger line of a showing is still copied from the summary of `case-guppi`, as `vault/wiki/orchestration.md` sets it.

> **tasks:**
> - [ ] update `rule-orchestration`
>   - old: `A deferred decision in the short form is the agent's own, written with no dispatch (case 419.1).`
>   - new: `` A deferred decision in the short form is the agent's own, written with no dispatch (case 419.1). A fact of what a subagent of the session did — a tool call it made, a tool error it met, a hook that refused its call — the main agent states as its own only after it reads that fact in the transcript of that subagent, never from its summary alone, since a summary does not show its tool errors; what a subagent reports of its own calls the main agent may pass on with no transcript, marked as the report of that subagent, such as by the words of `ask-guppi` (as set in case 923). ``
>   - change: `the main agent states what a subagent did only after it reads the fact in its transcript (case 923)`
> - [ ] `uv run --project .guppi guppi render`: `vault/wiki/orchestration.md`
> - [ ] create `estimate-orchestration-states-a-subagent-fact-from-its-transcript`
>   - ref: `rule-orchestration`
>   - kind: `QA`
>   - purpose: `Whether the main agent states as its own what a subagent of the session did only after it reads the fact in the transcript of that subagent, and passes on a subagent's report of its own calls marked as that report`
>   - method: `by hand at the Retro of the session that changes it: the new Render of rule-orchestration in the Spec read against the Criterion; after the first reply of the main agent under that Render that states what a subagent did: that reply and the tool calls of the main agent before it read against the Criterion, recorded in the estimate line`
>   - tags: `[session, workflow, orchestration]`
> - [ ] read `estimate-orchestration-states-a-subagent-fact-from-its-transcript`
> - [ ] update `insight-orchestration-writes-from-its-own-reading`
>   - set:
>     ```
>     status: actioned
>     addressed_by: decision-case-923
>     ```
>   - change: `actioned: the main agent states what a subagent did only after it reads the fact in its transcript, in rule-orchestration; the ratification lines of a showing were already copied from the summary and checked by rule-case-check (case 923)`

> **ratification:**
> ```
> - decision[case 923][update][rule-orchestration]{ref:rule-orchestration}
> - decision[case 923][create][estimate-orchestration-states-a-subagent-fact-from-its-transcript]{ref:rule-orchestration}{tags:session,workflow,orchestration}
> - decision[case 923][update][insight-orchestration-writes-from-its-own-reading]{ref:insight-orchestration-writes-from-its-own-reading}
> ```
