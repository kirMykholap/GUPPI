## Case 634 — /pre-spec checks each Case in its own ask-guppi run, and the same runs confirm their findings once

> **context:**
> At the first `/pre-spec` of a session, the main agent sends the read-only agent `ask-guppi` once over the whole plan, and the report then treats its answer as the check of the whole Spec. A Case rebuilt on a finding is checked only by the `case-guppi` that rebuilt it (case 561.1). One model run over twenty-odd sub-cases returns a sample of the findings, not all of them. `lesson-prespec-one-ask-guppi-run-samples-the-spec` records an example. The conserved Spec of session 1439 got ten findings at its own `/pre-spec`, and twelve at the `/pre-spec` of 1934. The lesson places eleven of the twelve:
> - eight on sub-cases that the first run had read and passed;
> - two on sub-cases written from that run's findings after it;
> - one on the fix of one of its findings.
>
> It places no twelfth, and this Case leaves that one unplaced. The lesson is clustered under `insight-prespec-after-findings-loop-unruled`, which is open again. Its `addressed_by` is `decision-case-561.1`. In that decision the person accepted the risk of a single run and asked for another option to be named (Case 561.4).
>
> The person chose these changes. The first `/pre-spec` sends one `ask-guppi` per top-level Case, all in one message. Each run judges its own Case and that Case's sub-cases, and reads the other Cases only to find a clash. The report names, for each run, the Case it judged and the list of what it did not check. That list is the one Case 633.1 adds to the answer of `ask-guppi`. The report never says the whole Spec is checked. The person asked whether a rebuilt Case would go to a new run. The person ruled a new run out, because a fresh agent always finds something and the checks would never end. The person chose that the same `ask-guppi` confirms its own findings once, with no new search and a fixed end. The confirmation comes after every `case-guppi` has answered and before the rebuilt Cases are shown. That way each rebuilt Case is ratified once, and the hook of `rule-prespec-onward` does not change. Its text in `guppi/onward.py` sends the agent on to the check and the exit after that ratification, which stays true. The person chose three sub-cases. 634.1 replaces the Criterion of `estimate-prespec-reconciles`, which has no `purpose`, and whose `method` names one reading by hand and does not state the old promise. 634.2 creates `estimate-prespec-confirms-the-findings-once`. A Glob of `vault/**/estimate-prespec-confirms*.md` printed nothing, so the slug is free. It has `ref: rule-prespec`, so the vault query was not run. 634.3 rewords the sentence of `rule-orchestration` that says `ask-guppi` is sent once, and replaces the Criterion of `estimate-orchestration-shows-the-built-case`. That Criterion says the same thing, and also says no `ask-guppi` comes before a showing, while the confirmation now comes before the showing of the rebuilt Cases. The `purpose` and `method` of that Estimate do not state the old promise, so they stand.
>
> The `/pre-spec` of session 2041 found six points in this Case, and each is fixed here:
> - A session that takes a conserved Spec has a plan file with only its title line, as `rule-skill-hi` sets it. So in that session the runs go one per top-level Case of the Spec that the title line names, as the opening line of 633.1 already expects.
> - The result of the confirmation stands in the main agent's own text after the horizontal rule. The `Stop` check of `rule-case-check` judges no text there (`estimate-case-check-refuses-text-outside-the-list`), so that Estimate already checks it and its Criterion stands. The list item of a Case keeps the form `orchestration.md` sets.
> - The question to fix or leave a finding comes after the confirmation, not in the report, since step 1 of the loop ties a question of the report to the time before any Case is sent back. Case 632.10, built again in parallel, adds that question to the list of the main agent's own questions in `rule-orchestration` and to `estimate-orchestration-asks-in-the-grill-me-shape`, so this Case touches neither.
> - The confirmation runs no Grep. The frame of `rule-ask` opens with the Grep of the rules for every question, so that sentence now leaves out the confirmation.
> - `estimate-case-build-checks-the-finished-case` reads its count from "the report of ask-guppi". 634.1 sets its `method` on the answers of the runs, one per top-level Case. Its Criterion reads only the index lines of the recipe of `ask-guppi`, not the runs, so it stands. Its `purpose`, counted by what `ask-guppi` still finds at `/pre-spec`, stays true.
> - The count of the lesson is stated above.
>
> The frame. Case 633 of this session changes `rule-ask` on the answer of `ask-guppi` at `/pre-spec`. No anchor of 634.1 or 634.2 in `rule-ask` touches text that 633 replaces or adds. The new paragraph of 634.2 stands after the five-line form of the answer, just before the paragraph on `/pre-spec`. Case 632 changes other sentences of `rule-orchestration`, so the anchor of 634.3 does not overlap them. `estimate-ask-finds`, as 633.1 replaces it, checks the answer of a run sent with the plan file and the questions. Each run per Case still is one, and it names the Cases it checked, so its Criterion stands. `estimate-prespec-gathers-the-answers-after-findings` stands: each of its lines stays true with the confirmation before the showing, and the showing in one reply stays. The batch of `rule-orchestration` lists the loop steps it takes, and it sends no Case on a finding of `ask-guppi`, so the new step does not reach it. The Purpose of `rule-prespec` says its question is asked once. That stays true, since the first run asks it once, split across the Cases.
>
> The check of this answer noted lines of the replaced Criteria that are not carried word for word. That is on purpose:
> - In 634.1, the When also names the render of `.claude/agents/ask-guppi.md`. The line on the check names the command as `uv run guppi prespec --check`. The line on the Frontier names its file and the session's ledger. The line on the dispatch gives one run per top-level Case of the plan, or of the conserved Spec that its title line names. The line on the report opens with what each run covered.
> - In 634.3, the line on `ask-guppi` drops the words that no `ask-guppi` comes before a showing, since the confirmation does.
>
> The check also noted that some `then` lines of 634.3 share words with lines of its siblings. Each pair speaks of a different promise, so each line stays in its own sub-case:
> - The line of 634.3 on how any built Case is shown sets the file, the list and the `ratification` of every showing. The line of 634.2 on the Cases built again sets only that they come in one reply after the confirmation, with its result after the horizontal rule.
> - The line of 634.3 on a ratified Case that changes, and the line of 634.1 on a finding in a Case, speak of different triggers.
> - The line of 634.3 on the showing, and the line of 634.1 that the agent writes no list of the decisions, speak of different replies.
>
> The searches this Case rests on:
> - A Grep of `ask-guppi.{0,80}once|once.{0,80}ask-guppi|asks once` over the repository, leaving out `vault/raw/`, `vault/archive/` and `vault/wiki/decisions/`, printed 11 files. Each is placed below:
>   - `.claude/skills/pre-spec/SKILL.md`, `.claude/agents/ask-guppi.md`, `vault/wiki/orchestration.md`, `rule-prespec.md`, `rule-ask.md`, `rule-orchestration.md`, `estimate-prespec-reconciles.md` and `estimate-orchestration-shows-the-built-case.md` enter the Case.
>   - `rule-index-check.md` speaks of the vault query of `case-guppi` and stands.
>   - `lesson-prespec-one-ask-guppi-run-samples-the-spec.md` records the error and stands.
>   - `tests/test_generate.py` holds a made-up page and stands.
>   - The other hits in the two Estimates are their `## Result` lines, a record that stands.
> - A Grep of `ask-guppi` over `vault/wiki/estimates/` printed 10 files: `estimate-ask-query-before-a-create`, `estimate-ask-finds`, `estimate-case-build-checks-the-finished-case`, `estimate-case-build-writes-the-case`, `estimate-hi-writes-frontier`, `estimate-hi-takes-a-conserved-spec`, `estimate-internal-context-loaded`, `estimate-orchestration-shows-the-built-case`, `estimate-orchestration-puts-the-harness-before-plan-mode` and `estimate-prespec-reconciles`. Three of them enter the Case. The others speak of the query of `case-guppi`, of the `- near` lines of `/hi`, of a conserved Spec, of what a subagent loads, or of `ask-guppi` asking at `/pre-spec`. Each stays true.
> - A Grep of `ask-guppi|ask_guppi` over `guppi/` printed nothing, so no code judges the dispatch.
> - A Grep of `ask-guppi` over `vault/wiki/rules/rule-case-protocol.md` printed two History lines, which were not read.
> - A Grep of `Waiting|bold label` over `vault/wiki/rules/`, `.claude/` and `guppi/` printed `.claude/skills/pre-spec/SKILL.md`, `rule-prespec.md`, `rule-orchestration.md` and `guppi/casecheck.py`. In `casecheck.py`, `round_opening` judges only a reply that shows a round of `case-guppi`, and an answer of `ask-guppi` is no round. So the new step waits as step 3 sets it.
>
> Not done:
> - A sub-case born of a finding is read by the confirmation only as far as the finding goes. The person accepted that a new error a fix brings in can show itself later.
> - No mark is written on `insight-prespec-after-findings-loop-unruled` or on its lesson. The lesson is of another session, and the librarian's run judges the Insight.

> **problem:**
> `/pre-spec` sends one `ask-guppi` over the whole plan and takes its answer as the check of the whole Spec, though one run returns only a sample of the findings. A Case rebuilt on a finding reaches the approved Spec read only by the agent that rebuilt it. The question is how the first check covers each Case, how a rebuilt Case is confirmed without a loop of checks that never ends, and what the report says about how much was checked.

> **recommend:**
> - **How the first check covers the whole plan**
>   - Recommended: (a) one `ask-guppi` run per top-level Case, all at once; each judges its own Case and its sub-cases and reads the others only to find a clash; no run is repeated.
>   - Answer: agreed with the recommendation, (a).
> - **How a rebuilt Case is read against the vault**
>   - Recommended: (b) one more `ask-guppi` run over the rebuilt Cases only, announced to the person before it starts.
>   - Answer: not answered. The person asked whether this meant the same `ask-guppi` or a new one, and said a new one is bad: an agent always finds an error, so the checks would never end, and the real question is how many checks are enough, a small point missed being acceptable. Replaced by **How many checks a rebuilt Case gets**.
> - **What the report says about how much was checked**
>   - Recommended: (a) the report names which Cases each run read and repeats each run's list of what it did not check, and never says the Spec is checked as a whole.
>   - Answer: agreed with the recommendation, (a).
> - **How many checks a rebuilt Case gets**
>   - Recommended: (b) the same `ask-guppi` confirms its own findings once: no new search and no new question; a finding not closed goes to the person as one question, fix or leave; the loop ends there.
>   - Answer: agreed with the recommendation, (b).
> - **When the found errors are confirmed as fixed**
>   - Recommended: (a) before the rebuilt Cases are shown, so that each is ratified once, already confirmed, and no hook changes.
>   - Answer: agreed with the recommendation, (a).
> - **How the Case is cut and checked**
>   - Recommended: (a) three sub-cases: the runs per Case with the coverage of the report, replacing the Criterion of `estimate-prespec-reconciles`; the confirmation, with a new Estimate; the sentence of `rule-orchestration`, replacing the Criterion of `estimate-orchestration-shows-the-built-case`.
>   - Answer: agreed with the recommendation, (a).
> - **Change**
>   - Asked: the `/pre-spec` of session 2041 found six points in this Case, and no question was put to the person on them.
>   - Taken: the runs follow the conserved Spec that the plan's title line names; the result of the confirmation stands after the horizontal rule; the question to fix or leave is a question after the confirmation; the confirmation runs no Grep, and the opening sentence of the frame of `rule-ask` leaves it out; the `method` of `estimate-case-build-checks-the-finished-case` reads the answers of the runs; the count of the lesson is stated with one finding unplaced.

### Case 634.1 — The first /pre-spec sends one ask-guppi per top-level Case, and the report names what each run covered

> **given:**
> `rule-prespec` and `.claude/skills/pre-spec/SKILL.md` — the skill and its render; the dispatch sentence and the opening of the report change
> **＋** `rule-ask` and `.claude/agents/ask-guppi.md` — the frame of the agent and its render; its Purpose, its description and its paragraph on `/pre-spec` change
> **＋** `estimate-prespec-reconciles` — its Criterion replaced whole
> **＋** `estimate-case-build-checks-the-finished-case` — its `method` set anew; its Criterion and `purpose` stand
> **＋** `guppi/prespec.py`, `vault/raw/<date>/<hi HHMM>/frontier.md` and the session's ledger — the check `uv run guppi prespec --check`, what it reads, and the `prespec` line that `guppi gate` writes; unchanged
> **＋** `case-guppi` and the hook of `rule-spec-write` — rebuild a Case on a finding and write it into the plan; unchanged
> **＋** `estimate-ask-finds` and `vault/raw/2026-10-04/2041/cases/case-633.md` — the answer of a run at `/pre-spec`, its list of what it did not check, as Case 633 sets it; unchanged here
> **＋** `rule-skill-hi` — sets the title line of the plan file of a session that takes a conserved Spec

> **when:**
> The person invokes `/pre-spec`, or the agent calls the skill, before the Spec is approved, with `.claude/skills/pre-spec/SKILL.md` rendered from `rule-prespec` and `.claude/agents/ask-guppi.md` rendered from `rule-ask`.

> **then:**
> The agent runs `uv run guppi prespec --check` on the plan file with `--session <id>`, the eight-character id of the `hi:` line, and reads the first line of the output before the exit code — "no hi recorded for session …; nothing checked" means the wrong value; nothing is translated before the run.
> **＋** A finding in a Case — in its prose or in its body, a wrong fact of its `context` included — goes to the `case-guppi` of that Case by `SendMessage`; its new answer is shown and ratified again, and the hook of `rule-spec-write` writes it into the plan; the agent does not edit the text of a Case in the plan file.
> **＋** A finding in `vault/raw/<date>/<hi HHMM>/frontier.md` or in a line of the session's ledger is fixed there, and the command runs again until it prints no finding.
> **＋** At the first run of `/pre-spec` in the session, one `ask-guppi` is dispatched for each top-level Case outside `## Deferred` — of the plan, or of the conserved Spec that the plan's title line names, as `rule-skill-hi` sets that line — all in one message, each with the absolute path of the plan file, the id of the Case it judges and the instruction to read every Case outside `## Deferred` — `context`, `when`, `then`, the `then` block — and, for an `update` of a rule or an entity, the page's `estimates`; each run judges its own Case and its sub-cases and reads the other Cases only to find a clash with them; of a Case under `## Deferred` it reads only the slugs of its `defer` items; a later run of `/pre-spec` in the session dispatches no `ask-guppi`.
> **＋** Three questions: which decisions contradict a page of the vault, a rule of the vault, or each other; whether an Estimate the Case does not name speaks of the thing the Case changes; which fact of a `context` — a page's status, a count, a case number, a claim that no page holds a thing — the vault does not bear out.
> **＋** The agent answers the findings with one report before any Case is sent back: for each `ask-guppi` run, the Case it judged and its list of what it did not check; each finding numbered, with the fix it proposes or why it is already known, the findings that need the person apart from those that do not, and the decisions it needs from the person; after the Cases built again on the findings are ratified, it does not call `/pre-spec` again, but runs the check, fixes what it prints, and exits Plan Mode when the check prints no finding.
> **＋** `guppi gate` writes the stamped `prespec` line on the Skill call.
> **－** The report never says that the whole Spec is checked.
> **－** The agent writes no list of the decisions: the plan is the list.
> **－** The body of a deferred decision is not read; a Case that changes a page another Case of the plan defers is still a finding.

> **tasks:**
> - [ ] update `rule-prespec`
>   - old: `` dispatch the `ask-guppi` agent once with the absolute path of the plan file and the instruction to read ``
>   - new: `` dispatch one `ask-guppi` agent for each top-level Case outside the `## Deferred` heading — of the plan, or, when the plan's title line names a conserved Spec, of that Spec — all in one message, each with the absolute path of the plan file, the id of the Case it judges — that Case and its sub-cases, the other Cases read only to find a clash with them (case 634.1) — and the instruction to read ``
>   - old: `Answer the findings with one report before any Case is sent back:`
>   - new: `` Answer the findings with one report before any Case is sent back: for each `ask-guppi` run, the Case it judged and its list of what it did not check, with no claim that the whole Spec is checked (case 634.1); ``
>   - change: `the first run of /pre-spec sends one ask-guppi per top-level Case of the plan or of the conserved Spec its title line names, all at once; the report names the Case each run judged and what it did not check, never the whole Spec as checked (case 634.1)`
> - [ ] update `rule-ask`
>   - old: `The main agent asks once, at pre-spec, for the set of ratified Cases;`
>   - new: `The main agent asks at pre-spec, one run for each top-level Case of the set of ratified Cases (case 634.1);`
>   - old: `the main agent asks once at pre-spec for the whole set;`
>   - new: `the main agent asks at pre-spec, one run per top-level Case of the set;`
>   - old: `` At `/pre-spec`, where the caller asks which Case of the plan contradicts ``
>   - new: `` At `/pre-spec`, where the caller names the Case you judge — that Case and its sub-cases, the other Cases of the plan read only to find a clash with them (case 634.1) — and asks which Case of the plan contradicts ``
>   - change: `at pre-spec each ask-guppi run judges the top-level Case the caller names and reads the other Cases only for a clash (case 634.1)`
> - [ ] update `estimate-prespec-reconciles`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — one ask-guppi per top-level Case at the first run, of the plan or of the conserved Spec its title line names, the report naming what each run judged and did not check (case 634.1)`
> - [ ] update `estimate-case-build-checks-the-finished-case`
>   - set:
>     ```
>     method: 'by hand: at /pre-spec of a later session after the render, the answers of the ask-guppi runs, one per top-level Case, read for each Case case-guppi built — a Case that departs from a chosen option, a page naming a changed slug that the Case misses, a rule acting at the same moment that the Case misses, a Case of the session named in the prompt whose page or moment the Case clashes with, an Estimate whose purpose or method still states the promise its replaced Criterion dropped, a claim of context that its search did not print, a search in context that the Case does not rest on, two sub-cases whose texts on one page contradict; the count of each in the reading line'
>     ```
>   - change: `the method reads the answers of the ask-guppi runs, one per top-level Case (case 634.1)`
> - [ ] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
> - [ ] `uv run guppi render`: `.claude/agents/ask-guppi.md`
> - [ ] read `estimate-prespec-reconciles`

> **ratification:**
> ```
> - decision[case 634.1][update][rule-prespec]{ref:rule-prespec}
> - decision[case 634.1][update][rule-ask]{ref:rule-ask}
> - decision[case 634.1][update][estimate-prespec-reconciles]{ref:rule-prespec}
> - decision[case 634.1][update][estimate-case-build-checks-the-finished-case]{ref:rule-case-build}
> ```

### Case 634.2 — The ask-guppi runs confirm their own findings once, before the Cases built again are shown

> **given:**
> `rule-prespec` and `.claude/skills/pre-spec/SKILL.md` — the skill and its render; the sentence on a later run and a step of the loop after the findings change
> **＋** `rule-ask` and `.claude/agents/ask-guppi.md` — the frame of the agent and its render; its opening sentence on the Grep of the rules changes, and a form of answer to the confirmation is added
> **＋** `vault/raw/2026-10-04/2041/cases/case-633.md` — Case 633 changes the paragraph of `rule-ask` on `/pre-spec`, before which the new paragraph stands
> **＋** `vault/raw/2026-10-04/2041/cases/case-632.md` — Case 632.10 puts the question after the confirmation into the list of the main agent's own questions in `rule-orchestration`
> **＋** `estimate-prespec-confirms-the-findings-once` — the new Estimate
> **＋** `rule-prespec-onward` and `guppi/onward.py` — after the ratification of the Cases built again, the hook sends the agent to the check and the exit; unchanged
> **＋** `rule-case-check` — its `Stop` check judges no text after the horizontal rule, as `estimate-case-check-refuses-text-outside-the-list` checks; unchanged
> **＋** `case-guppi` and `.claude/skills/grill-me/SKILL.md` — rebuild a Case on a finding, and the shape of the question after the confirmation

> **when:**
> `/pre-spec` has reported findings that sent Cases of the plan back, and every `case-guppi` that got a finding has answered with its Case built again, with `.claude/skills/pre-spec/SKILL.md` rendered from `rule-prespec` and `.claude/agents/ask-guppi.md` rendered from `rule-ask`.

> **then:**
> The main agent sends each `ask-guppi` run whose findings sent a Case back the Cases built again on them, by `SendMessage`, all in one message, and asks whether each of its findings is closed.
> **＋** Each `ask-guppi` answers with one line per finding of its own, under its number: `closed`, or `not closed` with one sentence on what still stands.
> **＋** The main agent asks the person a question after the confirmation, in the shape of `.claude/skills/grill-me/SKILL.md`: whether each finding not closed is fixed or left; it sends a finding to be fixed to the `case-guppi` of its Case.
> **＋** It then shows every Case built again in one reply, for one ratification, and writes what the confirmation found closed and not closed in its own text after the horizontal rule.
> **－** No Case goes to `ask-guppi` a second time, and no new `ask-guppi` is dispatched.
> **－** The answer of `ask-guppi` names no new finding; it runs no Grep, the Grep of the rules included, and reads only the Cases built again and the pages its findings name.
> **－** After that ratification the hook of `rule-prespec-onward` sends the agent to the check and the exit, as before.

> **tasks:**
> - [ ] update `rule-prespec`
>   - old: `` by its own `case-guppi` (case 561.1). ``
>   - new: `` by its own `case-guppi` (case 561.1), and the findings that sent it back are confirmed once in the loop below (case 634.2). ``
>   - old: `6. Show every Case built again in one reply,`
>   - new:
>     ```
>     6. Send each `ask-guppi` run whose findings sent a Case back the Cases built again on them, by `SendMessage`, all in one message, and ask whether each of its findings is closed; wait for every answer as step 3 sets it. Then ask the person a question after the confirmation, in its grill-me shape: whether each finding not closed is fixed or left; a finding to be fixed goes to the `case-guppi` of its Case as in steps 2 to 5. No Case goes to `ask-guppi` a second time, and no new `ask-guppi` is dispatched (case 634.2).
>     7. Show every Case built again in one reply, what step 6 found closed and not closed standing in your own text after the horizontal rule,
>     ```
>   - change: `the loop after the findings: the same ask-guppi runs confirm their own findings once before the Cases built again are shown; a finding not closed is fixed or left by the person's answer to a question after the confirmation; the result stands after the horizontal rule; no second confirmation (case 634.2)`
> - [ ] update `rule-ask`
>   - old: `answer in one of the two forms set at the end`
>   - new: `answer in one of the forms set at the end`
>   - old: `Always start with the Grep of the rules, whatever the question:`
>   - new: `Always start with the Grep of the rules, whatever the question but the confirmation of your findings at /pre-spec set at the end:`
>   - old: `` N from the page's `origin` ``
>   - new:
>     ```
>     N from the page's `origin`
>
>     At `/pre-spec`, when the caller sends you again the Cases built again on the findings you gave and asks whether each finding is closed, answer with one line per finding of yours, under its number: `closed`, or `not closed` and one sentence on what still stands. Run no Grep, the Grep of the rules included: read only the Cases built again and the pages your findings name, and name no new finding (case 634.2).
>     ```
>   - change: `ask-guppi answers the confirmation of its own findings at pre-spec with no Grep, one line per finding, closed or not closed, no new finding (case 634.2)`
> - [ ] create `estimate-prespec-confirms-the-findings-once`
>   - type: `estimate`
>   - ref: `rule-prespec`
>   - kind: `QA`
>   - purpose: `Whether after the findings of pre-spec the same ask-guppi runs confirm their own findings once on the Cases built again, before those Cases are shown, with no Grep, one line per finding, closed or not closed and no new finding, a finding not closed fixed or left by the person's answer to a question after the confirmation, the result standing after the horizontal rule of the showing, and no Case confirmed twice`
>   - method: `by hand at the /pre-spec of a later session whose findings send a Case back to its case-guppi, after the render of .claude/skills/pre-spec/SKILL.md and .claude/agents/ask-guppi.md by case 634.2: the SendMessage calls to ask-guppi, its tool calls and answers, and the replies up to the showing of the Cases built again, read in the transcript against the Criterion, recorded in the estimate line`
>   - tags: `[session, workflow, harness]`
> - [ ] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
> - [ ] `uv run guppi render`: `.claude/agents/ask-guppi.md`
> - [ ] read `estimate-prespec-confirms-the-findings-once`

> **ratification:**
> ```
> - decision[case 634.2][update][rule-prespec]{ref:rule-prespec}
> - decision[case 634.2][update][rule-ask]{ref:rule-ask}
> - decision[case 634.2][create][estimate-prespec-confirms-the-findings-once]{ref:rule-prespec}{tags:session,workflow,harness}
> ```

### Case 634.3 — orchestration.md says when ask-guppi is sent: one run per Case at the first /pre-spec, asked again only to confirm

> **given:**
> `rule-orchestration` — what the main agent does, rendered into `vault/wiki/orchestration.md`; the sentence on when `ask-guppi` is sent changes
> **＋** `vault/wiki/orchestration.md` — the render, loaded by `/hi`
> **＋** `estimate-orchestration-shows-the-built-case` — its Criterion replaced whole; its `purpose` and `method` stand
> **＋** `rule-prespec` — sets the runs per Case and their confirmation, by 634.1 and 634.2
> **＋** `vault/raw/2026-10-04/2041/cases/case-632.md` — Case 632 changes other sentences of `rule-orchestration`
> **＋** `case-guppi` and `ask-guppi` — the agents the main agent dispatches
> **＋** `.claude/skills/wait-what/SKILL.md` and `.claude/skills/grill-me/SKILL.md` — the plain explanation and the question shape
> **＋** `rule-case-check` — writes `raw/<date>/<hi HHMM>/cases/case-<N>.md` from the answer and checks the showing

> **when:**
> The main agent takes up a Frontier item, the person answers a round of questions, answers a shown Case with a question or a change, or asks for a plain explanation of the agent's text — by `/wait-what` on `UserPromptSubmit` or in words — or a ratified Case changes and is shown again, in Plan Mode or in Work Mode, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> The main agent dispatches `case-guppi` with the Case id, the Frontier item and its source, and the person's words on it, in the prompt of the call, after the plan file stands with its title line; nothing of the Case stands in the chat before the answer.
> **＋** The person's answers to a round go to the same `case-guppi` by `SendMessage`, verbatim and untranslated, and so does a question or a change of the person on a shown Case that is not a request for a plain explanation.
> **＋** A request for a plain explanation of a round, of the short text on a Case or of a reply the main agent answers itself by `.claude/skills/wait-what/SKILL.md`; it sends the `case-guppi` of the Case a `SendMessage` only to ask for a fact of the Case, and `case-guppi` answers with the fact alone, under a first line `**Fact:**` and with no Case heading.
> **＋** An answer with no Case heading and no first line `**Fact:**` is a round of questions: the main agent shows it in the chat translated into Russian line by line, slugs, paths and quotations unchanged, each quotation in its blockquote — the `**Context:**` paragraph that opens the first round on an item translated in place before the first question, each question in the order and with the number of the answer, opening with its `❓ **Qn** - **<title>**:` line of `.claude/skills/grill-me/SKILL.md` and closing with its `➡️` line, its title, body and recommended answer translated in place, nothing merged, dropped or added between the questions, the agent's own text after the last question and one horizontal rule; no Case is shown, no file is sent, and no step of confirmation follows the last round.
> **＋** The main agent shows the Case of an answer at every showing by `SendUserFile` with `display: render` on `raw/<date>/<hi HHMM>/cases/case-<N>.md`, the file the hook of `rule-case-check` wrote from the answer. In the same reply it writes the heading of the top-level Case with its name in Russian and, under it, one list with an item per Case and sub-case of the answer: its id, its name in Russian, and a short text in Russian on what done means and how it is checked, taken from the Estimate the Case creates or whose Criterion it replaces, or from the Estimate its `context` names as already checking the change. Then it writes one `ratification` with the ledger lines of every Case of the list as the answer holds them, and its own text after one horizontal rule. An answer in which a Case gives no such Estimate goes back to its `case-guppi` by `SendMessage` before the Case is shown.
> **＋** A reply that shows a Case and that the `Stop` check of `rule-case-check` refuses is followed, before the person answers, by a reply that sends the file and shows the `ratification` as the answer holds it; a reply that shows a round and that the `Stop` check of `rule-case-check` refuses is followed, before the person answers, by a reply that shows the round again with nothing before its `**Context:**` paragraph or its first question.
> **＋** A ratified Case that changes — in its prose or in its body — changes through its `case-guppi`, and its new answer is sent and ratified again; the main agent edits no Case in the plan file.
> **＋** An item that needs no decision the main agent closes alone, with no dispatch; it dispatches `ask-guppi` only at pre-spec, one run per top-level Case at its first run, never to build a Case, and asks a run again only to confirm its own findings.
> **－** The main agent writes no context of its own before the first question of a round.
> **－** The main agent writes no `given`, `when`, `then` or `tasks` of a built Case into the chat.
> **－** A deferred decision in the short form is written by the main agent in English in the chat, with no dispatch and no file.

> **tasks:**
> - [ ] update `rule-orchestration`
>   - old: `` the agent dispatches `ask-guppi` once, at pre-spec. ``
>   - new: `` the agent dispatches `ask-guppi` only at pre-spec, one run per top-level Case at its first run, and asks a run again only to confirm its own findings, as `rule-prespec` sets it (case 634.3). ``
>   - change: `ask-guppi is dispatched only at pre-spec, one run per top-level Case, and asked again only to confirm its findings (case 634.3)`
> - [ ] update `estimate-orchestration-shows-the-built-case`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — ask-guppi only at pre-spec, one run per top-level Case, asked again only to confirm its findings (case 634.3)`
> - [ ] `uv run guppi render`: `vault/wiki/orchestration.md`
> - [ ] read `estimate-orchestration-shows-the-built-case`

> **ratification:**
> ```
> - decision[case 634.3][update][rule-orchestration]{ref:rule-orchestration}
> - decision[case 634.3][update][estimate-orchestration-shows-the-built-case]{ref:rule-orchestration}
> ```
