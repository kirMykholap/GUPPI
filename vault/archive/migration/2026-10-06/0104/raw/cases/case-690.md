## Case 690 — A fact of a dispatch prompt and a ratified render change are no longer claimed unchecked

> **context:**
> `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it` gathers the slips where a sentence claims more than the check behind it. Case 359 set the general rule in `rule-agent-writing`, case 388 had `ask-guppi` check a fact of a `context` at `/pre-spec`, and cases 544.1 and 636 added checks to the build of a Case by `case-guppi`; each time a new lesson reopened the Insight. Its two live lessons come from the main agent. In `lesson-orchestration-dispatch-prompt-carried-counts-not-from-a-run` the prompt that dispatched `case-guppi` described an answer by sentence counts taken from a glance at a transcript; `case-guppi` copied them into the `context`, and `ask-guppi` at `/pre-spec` found them not borne out, which sent the Case back. In `lesson-orchestration-a-ratified-render-change-claimed-live-before-the-render` the main agent told the person, in the reply that acknowledged a ratification, that the change would already run at the `/pre-spec` of the same session, while the skill file changes only at the librarian's `uv run guppi render` after the session.
> The person chose that `case-guppi` reads at its source each fact its prompt states besides the person's words, and keeps out of the Case a fact it cannot read there (Case 690.1, in the Render of `rule-case-build`); that the paragraph `Changes:` of the acknowledging reply says that a change of a file rendered from a Rule page takes effect at the librarian's render, so the reply claims no new behaviour of that file for the rest of the session (Case 690.2, in the Render of `rule-orchestration`); two new Estimates, each read at the Retro of this session from the new Render in the Spec, since the files change only after the session and case 670.4 keeps a reading in the session of the Case; and the Insight set `actioned` by this Case (Case 690.3). `estimate-backlog-renders` checks the effect on `backlog.md`, since its Criterion lists an Insight under `## Deferred` only while it is `open`, and it stands.
> The frame. `estimate-case-build-checks-the-finished-case` speaks of the claims of `context` that rest on a search, and `estimate-case-build-writes-the-case` of what the prompt holds; the new sentence adds a reading of the prompt's facts and makes no line of either false, so both stand, and the new Estimate of Case 690.1 checks the change. `estimate-orchestration-acknowledging-reply` says the paragraph `Changes:` says what changes in one or two sentences; the new text keeps that, so it stands, and the new Estimate of Case 690.2 checks the change. The sentence of `rule-orchestration` on the prompt of the dispatch lists what the prompt holds and stays true. Cases 685, 686, 688 and 689 change other sentences of `rule-orchestration`: 685 sets the reply that answers the ledger hook's reminder, which comes after the acknowledging reply, and none of them changes the sentence on the paragraph `Changes:`; the new texts do not touch. No reader in code refuses on the old texts, so no old form is kept.
> The searches. A Grep of `caller's prompt|prompt of (the|its) call` over `vault/wiki/rules/` and `.claude/` printed `rule-orchestration.md` and `rule-case-build.md`, and `.claude/agents/case-guppi.md`: the Render of `rule-case-build` enters Case 690.1 and the agent file follows at the render; the sentence of `rule-orchestration` stands, as said above. A Grep of `Changes:` over `vault/wiki/rules/` printed `rule-orchestration.md`, whose sentence on the acknowledging reply enters Case 690.2 and whose sentence on Cases ratified in one answer, which names one paragraph `Changes:`, stands; over `.claude/` it printed nothing. A Grep of `Changes` over `guppi/` printed nothing, so no code judges the paragraph. A Grep of `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it` over `{vault/wiki/**,guppi/**,.claude/**,tests/**}` printed `brief.md`, `backlog.md` and `log.md`, not read, and the two lessons, whose `insight` field stays true. A Glob of `vault/**/*prompt-fact*` and of `vault/**/*rendered-change*` printed nothing, so both new slugs are free.

> **problem:**
> A fact the main agent writes into a dispatch prompt enters a Case unchecked, and the reply that acknowledges a ratification can tell the person that a change of a rendered harness file already runs in the session, while it changes only at the librarian's render.

> **recommend:**
> - **A fact in the prompt that sends out a Case build**
>   - Recommended: (a) the builder's frame says that a fact the prompt states, apart from the person's words, enters a Case only after the builder reads it at its source, and a fact it cannot read stays out.
>   - Answer: agreed, (a).
> - **A ratified change claimed to work before the render**
>   - Recommended: (a) the paragraph `Changes:` of the acknowledging reply says that a change to a file rendered from a Rule page takes effect at the librarian's render, after the session, and the reply claims no new behaviour for the rest of the session.
>   - Answer: agreed, (a).
> - **What checks the two fixes**
>   - Recommended: (a) two new Estimates, one per fix, each read at the Retro of this session from the new text in the Spec; the two existing Estimates stand.
>   - Answer: agreed, (a).
> - **What becomes of the backlog item after this Case**
>   - Recommended: (a) marked as dealt with by this Case; it leaves the backlog and its two lessons are archived.
>   - Answer: agreed, (a).

### Case 690.1 — case-guppi reads a fact of its prompt at its source

> **given:**
> `rule-case-build`: the frame of `case-guppi`, rendered into `.claude/agents/case-guppi.md`.
> **＋** `estimate-case-build-reads-a-prompt-fact-at-its-source`: the new check of the reading.
> **＋** `rule-orchestration`: the dispatch, which sets what the prompt holds.
> **＋** `estimate-case-build-checks-the-finished-case`: the check of the claims of `context`, which stands.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case, and the prompt of its call or a later message states a fact besides the person's words: a count, or what a page, a file or a reply says.

> **then:**
> The fact enters the Case only after `case-guppi` reads it at its source.
> **＋** A fact that `case-guppi` cannot read at its source stays out of the Case.
> **－** The person's words enter `recommend` as the person's answer, with no source to read.

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `` the person's question or change on the Case you built. The person's words reach you in ``
>   - new: `` the person's question or change on the Case you built. A fact the prompt or a message states besides the person's words — a count, or what a page, a file or a reply says — enters the Case only after you read it at its source; a fact you cannot read there stays out of the Case (case 690.1). The person's words reach you in ``
>   - change: `a fact of the prompt besides the person's words enters the Case only after case-guppi reads it at its source (case 690.1)`
> - [ ] create `estimate-case-build-reads-a-prompt-fact-at-its-source`
>   - ref: `rule-case-build`
>   - kind: `QA`
>   - purpose: `Whether case-guppi lets a fact its prompt states besides the person's words into a Case only after it reads it at its source, and keeps out a fact it cannot read there`
>   - method: `by hand, at the Retro of the session that changes it, the new Render of rule-case-build in the Spec read against the Criterion, recorded in the estimate line`
>   - tags: `[session, workflow, harness]`
> - [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
> - [ ] read `estimate-case-build-reads-a-prompt-fact-at-its-source`

> **ratification:**
> ```
> - decision[case 690.1][update][rule-case-build]{ref:rule-case-build}
> - decision[case 690.1][create][estimate-case-build-reads-a-prompt-fact-at-its-source]{ref:rule-case-build}{tags:session,workflow,harness}
> ```

### Case 690.2 — The acknowledging reply says when a rendered change lands

> **given:**
> `rule-orchestration`: the main agent's rules, rendered into `vault/wiki/orchestration.md`.
> **＋** `estimate-orchestration-says-when-a-rendered-change-lands`: the new check of the paragraph.
> **＋** `estimate-orchestration-acknowledging-reply`: the check of the form of the reply, which stands.
> **＋** `vault/raw/2026-10-06/0104/cases/case-685.md`: Case 685, which sets the reply after the acknowledging reply.

> **when:**
> The person ratifies a Case that changes a file rendered from a Rule page, and the main agent writes the reply that acknowledges it, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> The paragraph `Changes:` says that the change of that file takes effect at the librarian's render, after the session.
> **＋** The reply claims no new behaviour of that file for the rest of the session.

> **tasks:**
> - [ ] update `rule-orchestration`
>   - old: `` a paragraph **Changes:** — what changes, in one or two sentences; ``
>   - new: `` a paragraph **Changes:** — what changes, in one or two sentences, and, when the change touches a file rendered from a Rule page, that the file changes at the librarian's render after the session, so the reply claims no new behaviour of that file for the rest of the session (case 690.2); ``
>   - change: `the paragraph Changes: says that a rendered file changes at the librarian's render (case 690.2)`
> - [ ] create `estimate-orchestration-says-when-a-rendered-change-lands`
>   - ref: `rule-orchestration`
>   - kind: `QA`
>   - purpose: `Whether the reply that acknowledges a Case that changes a file rendered from a Rule page says that the file changes at the librarian's render, and claims no new behaviour of it for the rest of the session`
>   - method: `by hand, at the Retro of the session that changes it, the new Render of rule-orchestration in the Spec read against the Criterion, recorded in the estimate line`
>   - tags: `[session, workflow, harness]`
> - [ ] `uv run guppi render`: `vault/wiki/orchestration.md`
> - [ ] read `estimate-orchestration-says-when-a-rendered-change-lands`

> **ratification:**
> ```
> - decision[case 690.2][update][rule-orchestration]{ref:rule-orchestration}
> - decision[case 690.2][create][estimate-orchestration-says-when-a-rendered-change-lands]{ref:rule-orchestration}{tags:session,workflow,harness}
> ```

### Case 690.3 — The Insight on facts signed from a narrower check closes

> **given:**
> `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it`: the Insight this Case closes.
> **＋** `rule-insights-schema`: the form of an Insight and of its `actioned` status.
> **＋** `rule-page-generation`: the rule of `guppi generate`, which applies the update and archives the lessons of an `actioned` Insight.
> **＋** `vault/wiki/backlog.md`: the backlog, which lists each `open` Insight.

> **when:**
> `guppi generate` of `rule-page-generation` applies the decision of this Case, and `guppi backlog` writes `vault/wiki/backlog.md`.

> **then:**
> `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it` stands `actioned`, and its `addressed_by` names the Decision of this Case.
> **＋** Its `clustered` lessons become `archived` by the cascade.
> **＋** `vault/wiki/backlog.md` no longer lists it under `## Deferred`.

> **tasks:**
> - [ ] update `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it`
>   - set:
>     ```
>     status: actioned
>     addressed_by: decision-case-690.3
>     ```
>   - change: `actioned: case-guppi reads a fact of its prompt at its source (case 690.1), and the acknowledging reply says that a rendered file changes at the librarian's render (case 690.2) (case 690.3)`

> **ratification:**
> ```
> - decision[case 690.3][update][insight-workflow-fact-signed-from-a-check-that-does-not-cover-it]{ref:insight-workflow-fact-signed-from-a-check-that-does-not-cover-it}
> ```
