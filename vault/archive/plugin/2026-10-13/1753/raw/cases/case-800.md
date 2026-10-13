## Case 800 — case-guppi and ask-guppi close the gaps behind two lessons

> **context:**
> Session 1426 left two lessons with no fix. In `lesson-case-build-gave-a-sub-case-no-estimate`, the person answered that Case 795.1 creates no new Estimate. `case-guppi` read this as "no Estimate" and wrote the sub-case with no check. It never looked for an Estimate that already checked the change, though its frame sentence of case 561.11 asks it to name such an Estimate in `context`. The main agent sent the summary back before the showing, by case 561.9 of `rule-orchestration`. The cause is the round question on the promise: its "no new Estimate" option named no existing Estimate, so the answer could be read two ways. In `lesson-ask-guppi-read-a-decision-page-without-a-reason`, at the /pre-spec of session 1426, `ask-guppi` opened `decision-case-616`, the Decision behind the `deferred_by` of `entity-guppi`, though no finding named `entity-guppi`. Ledger line 3 of session 1426 shows that Case 795.1 updated `entity-guppi`. The frame of `ask-guppi` allows that read only when "a page in your answer" carries `deferred_by`. At /pre-spec the answer is a list of findings, and the text does not say whether the read may come before a finding names the page. The governing rule is `rule-search-leaves-out-decisions`: a Decision page is read only for a reason the frame of the agent names. A hook that refuses such reads cannot see the findings before the answer is written, so the person chose to fix the text of the rule, not to add a hook on the agent.
>
> Case 800.1 adds one sentence to the Render of `rule-case-build`. It replaces the Criterion, `purpose` and `method` of `estimate-case-build-answers-what-done-means`, the one Estimate of that page whose Criterion speaks of how a Case is checked. I read the Criterion of every Estimate the page lists. Case 800.2 adds one clause to the Render of `rule-ask`, and creates `estimate-ask-opens-a-decision-only-for-a-finding` on `rule-ask`. A Glob `vault/**/estimate-ask-opens-a-decision-only-for-a-finding.md` printed nothing, so the slug is free. The `create` has a `ref`, so no vault query runs before it. The line of `estimate-ask-finds` that a finding on a page with `deferred_by` gives the `## Problem` of its Decision stands, and the new Estimate does not repeat it. The reason of `estimate-search-leaves-out-decisions-in-every-agent`, that a page of the answer carries `deferred_by`, stays true, since a page a finding names is a page of the answer, so its Criterion stands. The `－` line of `estimate-ask-searches-at-prespec` hands Decision reads to that Estimate and stays true. The `.claude/skills/pre-spec/SKILL.md` that dispatches `ask-guppi` sets nothing about Decision reads. A Grep of `case-guppi\.md|ask-guppi\.md|rule-case-build|rule-ask\b|agents/` over `tests/` printed nothing, so no test reads the two rendered files or the two rule pages live. The `Purpose` of each rule names neither behaviour and stays. Both lessons were written in session 1426, so no decision line carries `{addresses:...}` for them (case 284.2). They stay `new` until a later lesson joins them or the close of the sprint archives them.

> **problem:**
> Two agents read a gap in their frame as permission. `case-guppi` closed the check of a sub-case on an answer that named no Estimate. `ask-guppi` opened a Decision page before any finding of its own named the page.

> **recommend:**
> - **How should case-guppi stop reading "no new Estimate" as "no Estimate"?**
>   - Recommended: (a) the question on the promise names the existing Estimate by slug, and an answer of no new Estimate closes the promise only with that Estimate named in `context`.
>   - Answer: agreed, (a).
> - **When may ask-guppi open the Decision behind a put-off page during the review?**
>   - Recommended: (a) restrict the rule: at /pre-spec, the Decision is opened only after a finding names the page, never to judge whether a finding stands.
>   - Answer: (a). In the first round the person asked why the agent opened that Decision at all, and whether the agent or the rule should be restricted.
> - **Should the two fixes be one Case with two parts, or two separate Cases?**
>   - Recommended: (a) one Case with two sub-cases.
>   - Answer: agreed, (a).
> - **How is the case-guppi fix checked?**
>   - Recommended: (a) replace the Criterion of `estimate-case-build-answers-what-done-means`, read at the Retro of this session against the new Render.
>   - Answer: agreed, (a).
> - **How is the ask-guppi fix checked?**
>   - Recommended: (a) a new narrow Estimate on `rule-ask`, read after the next /pre-spec on the new text.
>   - Answer: agreed, (a).

### Case 800.1 — An answer of no new Estimate names the existing one

> **given:**
> `rule-case-build`: the rule of `case-guppi`; one sentence of its Render changes.
> **＋** `.claude/agents/case-guppi.md`: the file rendered from `rule-case-build`.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a Case.
> **＋** `estimate-case-build-answers-what-done-means`: its Criterion, `purpose` and `method` replaced.
> **＋** `rule-orchestration`: the main agent sends back a summary in which a Case gives no Estimate.

> **when:**
> `case-guppi` writes a Case into `raw/<date>/<hi HHMM>/cases/case-<N>.md`, following `.claude/agents/case-guppi.md` as rendered from `rule-case-build`.

> **then:**
> Each Case and sub-case of the file creates an Estimate or replaces the Criterion of one, or its `context`, or its parent's, names by slug the Estimate that already checks the change and says why its Criterion stands.
> **＋** The summary that `case-guppi` answers with names that Estimate under the item of each Case and sub-case.
> **＋** A question of a round before the Case on how it is checked gives an option that names by slug the Estimate that already checks the change, where one in the `estimates` of a page the Case changes does.
> **＋** After the person answers that no new Estimate is created, the `context` names by slug the Estimate that checks the change, taken from the `estimates` of a page the Case changes.
> **＋** When the person's words and the frame give neither, `case-guppi` asks in a round, before it writes the Case, what the Estimate will check, and the `recommend` of the Case holds that question.
> **－** A deferred decision in the short form is not written by `case-guppi` and carries no such Estimate.

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `a Case that can give neither has the promise open, and you ask in a round what its Estimate will check (case 561.11).`
>   - new: `` a Case that can give neither has the promise open, and you ask in a round what its Estimate will check (case 561.11). A question of a round on how a Case is checked gives, beside the option of a new Estimate or a replaced Criterion, an option that names by slug the Estimate that already checks the change, found in the `estimates` of each page the Case changes, where one there does; an answer that no new Estimate is created closes the promise only with that Estimate: before the summary you name it in `context` and say why its Criterion stands, and where none of those Estimates checks the change you ask again in a round what its Estimate will check (case 800.1). ``
>   - change: `an answer that no new Estimate is created closes the promise only with the existing Estimate named by slug in the round and in context (case 800.1)`
> - [ ] update `estimate-case-build-answers-what-done-means`
>   - set:
>     ```
>     status: pending
>     purpose: "Whether each Case case-guppi builds creates or replaces an Estimate or names the one that already checks the change, offers that Estimate by slug in a round on the promise, names it in context after an answer that no new Estimate is created, and asks in a round when it can do neither"
>     method: "by hand at the Retro of this session: the new Render of rule-case-build in raw/<date>/<hi HHMM>/spec.md read against the Criterion, recorded in the estimate line"
>     ```
>   - change: `the Criterion replaced whole — the round on the promise names the existing Estimate, and an answer of no new Estimate closes the promise only with it named (case 800.1)`
> - [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
> - [ ] read `estimate-case-build-answers-what-done-means`

> **ratification:**
> ```
> - decision[case 800.1][update][rule-case-build]{ref:rule-case-build}
> - decision[case 800.1][update][estimate-case-build-answers-what-done-means]{ref:rule-case-build}
> ```

### Case 800.2 — ask-guppi opens a deferred Decision only for a page a finding names

> **given:**
> `rule-ask`: the rule of `ask-guppi`; one sentence of its Render changes.
> **＋** `.claude/agents/ask-guppi.md`: the file rendered from `rule-ask`.
> **＋** `.claude/skills/pre-spec/SKILL.md`: the skill that dispatches `ask-guppi` at `/pre-spec`.
> **＋** `vault/wiki/decisions/`: the folder of the Decision pages.
> **＋** `estimate-ask-opens-a-decision-only-for-a-finding`: the new check of when `ask-guppi` opens a Decision at `/pre-spec`.
> **＋** `rule-search-leaves-out-decisions`: a Decision page is read only for a reason the frame of the agent names.
> **＋** `estimate-search-leaves-out-decisions-in-every-agent`: the check of Decision reads in every agent, which stands.

> **when:**
> At the first run of `/pre-spec` in a session, the main agent dispatches `ask-guppi` through the `Agent` tool with the plan file and the questions of `.claude/skills/pre-spec/SKILL.md`, and the agent follows `.claude/agents/ask-guppi.md` as rendered from `rule-ask`.

> **then:**
> Each page under `vault/wiki/decisions/` that `ask-guppi` reads, by a Read or by a Grep inside that folder, for a page that carries `deferred_by`, is the Decision of a page that a finding of its answer names.
> **＋** A page that carries `deferred_by` and stands in no finding has its Decision left unread, also when a Case of the plan changes that page.
> **－** A Decision read because the question asks why something was decided, reached through the `origin` of a page, is outside this promise.
> **－** Decision reads by the main agent and by `case-guppi` are outside this promise: `estimate-search-leaves-out-decisions-in-every-agent` reads them.

> **tasks:**
> - [ ] update `rule-ask`
>   - old: `since a deferred decision is something already decided; or the question asks why something was decided`
>   - new: `` since a deferred decision is something already decided; at `/pre-spec` you open it only after a finding of yours names the page, never to judge whether a finding stands, and a page that carries `deferred_by` and stands in no finding has its Decision left closed (case 800.2); or the question asks why something was decided ``
>   - change: `at /pre-spec the Decision of a page with deferred_by is opened only after a finding names the page (case 800.2)`
> - [ ] create `estimate-ask-opens-a-decision-only-for-a-finding`
>   - ref: `rule-ask`
>   - kind: `QA`
>   - purpose: `Whether ask-guppi at /pre-spec opens the Decision behind a page with deferred_by only for a page that a finding of its answer names`
>   - method: `by hand, after a /pre-spec whose ask-guppi runs on .claude/agents/ask-guppi.md as rendered by case 800.2: the Read and Grep calls of ask-guppi on vault/wiki/decisions/ in its agent transcript and the findings of its answer read against the Criterion, recorded in the estimate line`
>   - tags: `[session, workflow, harness]`
> - [ ] `uv run guppi render`: `.claude/agents/ask-guppi.md`
> - [ ] read `estimate-ask-opens-a-decision-only-for-a-finding`

> **ratification:**
> ```
> - decision[case 800.2][update][rule-ask]{ref:rule-ask}
> - decision[case 800.2][create][estimate-ask-opens-a-decision-only-for-a-finding]{ref:rule-ask}{tags:session,workflow,harness}
> ```
