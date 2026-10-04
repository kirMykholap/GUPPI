## Case 633 — ask-guppi at /pre-spec: a fixed frame around the findings, and its searches checked apart

> **context:**
> `ask-guppi` is the read-only helper agent that the main agent sends once, at the first `/pre-spec` of a session, to find Cases that clash with the vault or with each other. Its frame, `.claude/agents/ask-guppi.md` rendered from `rule-ask`, tells it to answer the three questions of `/pre-spec` with one numbered list of findings under each. `estimate-ask-finds` checks that answer. Its Criterion lets nothing reach the caller beyond the findings and a list of paths. It also reads the order of searches (the Grep of the rules first, then one Grep per other category) as the whole of the searching. The Estimate failed at the /hi of 1934 (raw/2026-10-04/1934/ledger.md L1), as it failed before (raw/2026-10-01/1441/ledger.md L33, raw/2026-10-04/0004/ledger.md L17). The dispatch it read, at the /pre-spec of 1439, gave the three lists in order, and each finding was sound. But the answer opened with a heading and a summary, closed with a paragraph on what the vault bears out and a "Not checked" list, and ran several Greps per category. I read the dispatch at the /pre-spec of 1934 (agent a6d84c6b7ce6994bf) against the same Criterion. It does the same things. It opens with a paragraph on which Spec it read and which Cases. After the findings it gives the facts that hold, a "Not done" list and a list of pages. It runs about twenty Greps after the category Greps, several of them to count again what a `context` states. It also says that three of these Greps covered `vault/wiki/decisions/`, which the frame forbids except for two reasons. Part of the extra text is what `CLAUDE.md` asks of every answer: say what is done and what is not done. Part of the extra searching is what the third question of `/pre-spec` needs, since a count can only be checked by running its search again.
>
> The person chose a fixed frame around the lists. One line before them names what was read. After them stands one list of what was not checked, then the paths. A summary and a list of what holds stay out. The person chose free Greps and Reads after the fixed start, to check a finding at `/pre-spec`. On Decision pages the person ruled that a count over them is not checked again: each Decision page states its own at its moment, and reading them again would mean editing history. So a count whose search covers `vault/wiki/decisions/` is not run again and is no finding. The ban of the frame on Decision pages stands. The person chose two sub-cases. 633.1 replaces the Criterion of `estimate-ask-finds` with the form of the answer alone, and sets its `purpose` and `method` anew, since both state the old promise. 633.2 moves the line on searches into a new Estimate, `estimate-ask-searches-at-prespec`. A Glob of `vault/**/estimate-ask-searches*.md` printed nothing, so the slug is free. The new Estimate has `ref: rule-ask`, so the vault query was not run. Each sub-case adds its sentence to a different passage of the Render, so the two `replace` anchors do not overlap.
>
> The check of this answer noted that five lines of the old Criterion of `estimate-ask-finds` are not carried word for word. That is on purpose, and each line has a new place:
> - The line that the answer opens with the lists now follows the new opening line on what was read.
> - The line on a list of paths that may stand after the findings becomes the line on a list of what was not checked, then the paths.
> - The line on the Grep of the rules moves to `estimate-ask-searches-at-prespec`, word for word.
> - The line that nothing reaches the caller beyond the findings and the paths becomes the line that refuses a summary, a list of what holds, an index line and page text.
> - The line that an answer with no list after the findings holds the promise narrows to an answer with no list of paths, since the list of what was not checked is now required.
>
> The check also noted that a `then` line of 633.2 on `vault/wiki/decisions/` shares words with the line of 633.1 on the `## Problem` of a deferring Decision. That is on purpose. 633.1 checks that the Problem stands in the finding, and 633.2 checks that the searches over the Decision pages go no further than that Problem.
>
> Frame checks. The moment this Case sets is the answer of `ask-guppi` at `/pre-spec`. A Grep of `ask-guppi` over `.claude/` printed 4 files: `.claude/agents/ask-guppi.md`, `.claude/agents/case-guppi.md`, `.claude/skills/pre-spec/SKILL.md` and `.claude/skills/hi/SKILL.md`. A Grep of `ask-guppi` over `vault/wiki/rules/`, leaving out `rule-ask.md`, printed 7 files: `rule-case-protocol.md`, `rule-case-build.md`, `rule-orchestration.md`, `rule-prespec.md`, `schema.yaml`, `rule-skill-hi.md` and `rule-rules-schema.md`. The hits in `rule-case-protocol.md` and the History hits in `rule-prespec.md` are History lines and were not read. None of the hits I read sets the form of the agent's answer or its searches at `/pre-spec`:
> - `rule-prespec` and its skill set what the main agent sends and its own report;
> - `rule-orchestration` sets only that `ask-guppi` asks at `/pre-spec`;
> - `rule-case-build` and `case-guppi.md` have `case-guppi` run the query itself;
> - `schema.yaml` and `rule-rules-schema` say that `ask-guppi` reaches a deferred Decision through `deferred_by`;
> - `rule-skill-hi` says the near lines of the Frontier need no `ask-guppi`.
>
> Each stays true. A Grep of `ask-guppi` over `vault/wiki/estimates/` printed 10 files. Two of them are the Estimates of `rule-ask`. The other eight are `estimate-case-build-writes-the-case`, `estimate-case-build-checks-the-finished-case`, `estimate-hi-takes-a-conserved-spec`, `estimate-hi-writes-frontier`, `estimate-internal-context-loaded`, `estimate-orchestration-shows-the-built-case`, `estimate-orchestration-puts-the-harness-before-plan-mode` and `estimate-prespec-reconciles`. Each speaks of when `ask-guppi` is sent or of the query of `case-guppi`, not of the form of the answer or the searches at `/pre-spec`, so their Criteria stand. `estimate-case-build-checks-the-finished-case` has `case-guppi` leave the Decision pages out of its own searches, which agrees with the person's ruling. `estimate-ask-query-before-a-create` checks the query that `case-guppi` runs before a `create`. The new sentence of 633.2 holds only at `/pre-spec`, so that Criterion stands. A Grep of `ask-guppi` over `guppi/` printed nothing, so no code judges the answer. The caller's prompt says Case 632 changes none of these pages, and it sets nothing about this answer, so its file was not read. The open Frontier item C4, on how `/pre-spec` checks a Spec beyond one run of `ask-guppi`, is left to its own Case. `rule-prespec` does not change here.

> **problem:**
> The frame of `ask-guppi` sets the three lists of `/pre-spec` and nothing around them. `estimate-ask-finds` refuses every word beyond the lists and the paths, and it reads the order of searches as a limit. Each run adds what `CLAUDE.md` and the third question need: what was read, what was not checked, and searches that check a count. The check fails each time on text and searches that are useful. The question is what may stand around the lists, how freely the agent searches at `/pre-spec`, and how each is checked.

> **recommend:**
> - **What may stand around the three lists**
>   - Recommended: (b) a fixed frame: one line before the first list that names what was read, and after the findings one list of what was not checked, then the paths; no summary and no list of what holds.
>   - Answer: agreed with the recommendation, (b).
> - **How freely the agent searches at /pre-spec**
>   - Recommended: (a) the fixed start stays, the Grep of the rules and one Grep per category; after them, more Greps and Reads are allowed to check a finding, and the frame gains one sentence that says so.
>   - Answer: agreed with the recommendation, (a).
> - **A count check that reaches the Decision pages**
>   - Recommended: (a) a search that runs again a count stated in a Case may cover `vault/wiki/decisions/`, file names and counts only, no Decision page opened.
>   - Answer: not as recommended. Other Decision pages are not counted again: that is extra context and needs no fixing. Each Decision page states its own at its moment, and reading them again would mean editing history all the time.
> - **One promise or two**
>   - Recommended: (a) two sub-cases: `estimate-ask-finds` keeps the form of the answer alone, and a new Estimate checks the searches at `/pre-spec`; both are read from the same transcript.
>   - Answer: agreed with the recommendation, (a).

### Case 633.1 — ask-guppi frames its findings at /pre-spec with one line on what it read and a list of what it did not check

> **given:**
> `rule-ask` — its Render is the text of `.claude/agents/ask-guppi.md`; the paragraph on `/pre-spec` changes
> **＋** `.claude/agents/ask-guppi.md` — the agent rendered from `rule-ask`
> **＋** `estimate-ask-finds` — the check whose Criterion is replaced whole and whose `purpose` and `method` are set anew
> **＋** `CLAUDE.md` — asks every answer to say what is done and what is not done; unchanged
> **＋** `.claude/skills/pre-spec/SKILL.md` — sends `ask-guppi` the plan file and the three questions; unchanged
> **＋** `vault/raw/<date>/event_log.md` — records each dispatch

> **when:**
> At the first run of `/pre-spec` in a session, the main agent dispatches `ask-guppi` through the `Agent` tool with the plan file and the questions of `.claude/skills/pre-spec/SKILL.md`, and the agent follows `.claude/agents/ask-guppi.md` as rendered from `rule-ask`.

> **then:**
> The answer opens with one line that names what the agent read: the plan file, or the Spec that the plan's title line names, and the Cases it checked.
> **＋** Then stands one numbered list of findings under each question of `.claude/skills/pre-spec/SKILL.md`, in its order: what contradicts a page, a rule or another Case; an Estimate a Case does not name that speaks of the thing the Case changes; a fact of a `context` the vault does not bear out.
> **＋** Each finding names its Case and the page or the Cases it bears on; a question with no finding says "none".
> **＋** A finding that names a page carrying `deferred_by` gives the `## Problem` of the Decision that field names.
> **＋** After the findings stands one list of what the questions ask that the agent did not check, "none" when it checked all of it, and then a list of the paths of the files it read.
> **＋** The dispatch stands in `vault/raw/<date>/event_log.md`.
> **－** The findings are not put under the lines `exists`, `near`, `missing`, `rules` and tags/slug: those lines answer a question whether a thing exists.
> **－** No summary of the findings, no list of what holds, no index line and no page text reaches the caller.
> **－** An answer with no list of paths holds the promise as well.

> **tasks:**
> - [ ] update `rule-ask`
>   - old: `and a question with no finding says "none" (case 626.1).`
>   - new: `and a question with no finding says "none" (case 626.1). One line before the first list names what you read: the plan file, or the Spec its title line names, and the Cases you checked. After the findings stand one list of what the questions ask that you did not check, "none" when you checked all of it, and then the list of the paths of the files you read; no summary of the findings and no list of what holds (case 633.1).`
>   - change: `ask-guppi frames its findings at /pre-spec with one line on what it read and, after them, a list of what it did not check before the paths; no summary, no list of what holds (case 633.1)`
> - [ ] update `estimate-ask-finds`
>   - set: `{status: pending, purpose: "Whether ask-guppi answers the questions of /pre-spec with one line on what it read, one numbered list of findings under each question, each finding naming its Case and the page or Cases it bears on, then a list of what it did not check and a list of the paths of the files it read, and nothing else", method: "by hand at the /hi of a later session: the answer of ask-guppi at a /pre-spec after the render of .claude/agents/ask-guppi.md by case 633.1, read in its agent transcript against the event log, recorded in the estimate line"}`
>   - change: `the Criterion replaced whole — one line on what was read before the findings, a list of what was not checked after them and before the paths, no summary and no list of what holds; the line on the searches moved to estimate-ask-searches-at-prespec (case 633.1)`
> - [ ] `uv run guppi render`: `.claude/agents/ask-guppi.md`
> - [ ] read `estimate-ask-finds`

> **ratification:**
> ```
> - decision[case 633.1][update][rule-ask]{ref:rule-ask}
> - decision[case 633.1][update][estimate-ask-finds]{ref:rule-ask}
> ```

### Case 633.2 — ask-guppi searches as a finding needs at /pre-spec and leaves the Decision pages out of a count

> **given:**
> `rule-ask` — its Render is the text of `.claude/agents/ask-guppi.md`; the paragraph on the Greps changes
> **＋** `.claude/agents/ask-guppi.md` — the agent rendered from `rule-ask`
> **＋** `.claude/skills/pre-spec/SKILL.md` — the skill `/pre-spec`, whose first run sends `ask-guppi` the plan file and the three questions; unchanged
> **＋** `estimate-ask-searches-at-prespec` — the new Estimate
> **＋** `estimate-ask-query-before-a-create` — checks the searches of the query `case-guppi` runs before a `create`; unchanged
> **＋** `vault/wiki/rules/` — the rule pages the agent greps first
> **＋** `vault/wiki/decisions/` — the Decision pages, searched only for the two reasons the frame names

> **when:**
> At the first run of `/pre-spec` in a session, the main agent dispatches `ask-guppi` through the `Agent` tool with the plan file and the questions of `.claude/skills/pre-spec/SKILL.md`, and the agent follows `.claude/agents/ask-guppi.md` as rendered from `rule-ask`.

> **then:**
> The agent starts with the Grep `^(purpose|deferred_by):` over `vault/wiki/rules/`, then runs one Grep per other category the question touches.
> **＋** After those Greps it runs further Greps and Reads as a finding needs, including the search behind a count that a `context` states.
> **＋** A count of a `context` whose search covers `vault/wiki/decisions/` is not run again and is no finding.
> **－** No Grep or Read of the agent reaches `vault/wiki/decisions/`, except for the `## Problem` of a Decision that a `deferred_by` names and a Decision reached through a page's `origin` when the question asks why something was decided.

> **tasks:**
> - [ ] update `rule-ask`
>   - old: `When the question is about a check, reach the Estimates`
>   - new: `` At `/pre-spec`, after these Greps, Grep and Read as each finding needs, including the search behind a count that a `context` states; a count whose search covers `vault/wiki/decisions/` is not run again and is no finding, since a Decision page states its own at its moment (case 633.2). When the question is about a check, reach the Estimates ``
>   - change: `at /pre-spec ask-guppi greps and reads as each finding needs after the index Greps; a count over vault/wiki/decisions/ is not run again (case 633.2)`
> - [ ] create `estimate-ask-searches-at-prespec`
>   - type: `estimate`
>   - ref: `rule-ask`
>   - kind: `QA`
>   - purpose: `Whether ask-guppi at /pre-spec starts with the Grep of the rules and one Grep per other category, then greps and reads as each finding needs, and leaves vault/wiki/decisions/ out of every search but the two reasons its frame names, a count over Decision pages not run again`
>   - method: `by hand at the /hi of a later session: the Grep, Glob and Read calls of ask-guppi at a /pre-spec after the render of .claude/agents/ask-guppi.md by case 633.2, read in its agent transcript against the Criterion, recorded in the estimate line`
>   - tags: `[session, workflow, harness]`
> - [ ] `uv run guppi render`: `.claude/agents/ask-guppi.md`
> - [ ] read `estimate-ask-searches-at-prespec`

> **ratification:**
> ```
> - decision[case 633.2][update][rule-ask]{ref:rule-ask}
> - decision[case 633.2][create][estimate-ask-searches-at-prespec]{ref:rule-ask}{tags:session,workflow,harness}
> ```
