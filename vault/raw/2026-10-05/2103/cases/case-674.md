## Case 674 — Pre-spec goes back to one ask-guppi run over the whole Spec

> **context:**
> At its first run in a session, `/pre-spec` sends `ask-guppi` to read the ratified Cases against the vault. Until case 634.1 it sent one run over the whole plan. `lesson-prespec-one-ask-guppi-run-samples-the-spec` records why that changed: one run over the Spec of session 1439, about twenty sub-cases, found 10 findings, and a later run over the same Spec found 12 more, 8 of them in sub-cases the first run had read. Since case 634.1 the skill sends one run per top-level Case, all at once; each judges its own Case and reads the others only for a clash. At the `/pre-spec` of session 0109 the person said that the check of the whole plan worked better, and case 643 put the question off as the placeholder `rule-prespec-judges-the-spec-whole`. In this session the person weighed the two ways. No record measures the cost of the per-Case runs or compares the two ways on one Spec; the vault records two costs of a single run only, 88 728 tokens in 204 s and 95 tool calls in about eight minutes. The person judged the per-Case runs too costly for an unclear benefit, chose to go back to one run, and said to think further later.
> The person chose the three questions of the single run as they stand, no question on what the Cases leave open together, a report that still never says the whole Spec is checked, and the placeholder kept in the backlog with its purpose rewritten for the later thought. The Case is cut by `rule-atomicity`: 674.1 changes the skill and the agent frame and replaces the Criterion of `estimate-prespec-reconciles`; 674.2 changes the one sentence of `rule-orchestration` and replaces the Criterion of `estimate-orchestration-shows-the-built-case`, whose line on the dispatch it makes false; 674.3 keeps the placeholder. No measurement of the cost of a run is added, and none is done.
> The vault's answer: the Case creates no page, so no vault query on a `create` ran. The Frontier line has the source `backlog`, and `rule-prespec-judges-the-spec-whole` carries `deferred_by` the Decision of case 643, whose page holds no `## Problem`. 674.3 names the page on an `update` that carries `{supersedes:case 643}`, and defers it again by its own `defer` line; `guppi generate` adds the new Decision to `deferred_by` and clears only the Decision of case 643 from it, so the page stays in `## Deferred` of the backlog. `estimate-backlog-renders` checks that a page with `deferred_by` stands there with its `purpose`; its Criterion does not change, so it stands and checks 674.3.
> The frame. A Grep of `per top-level Case|for each top-level Case|ask-guppi` runs?|ask-guppi runs?|find a clash` over `vault/wiki/` printed 16 files: `backlog.md`, `orchestration.md`, `log.md`, `rules/rule-prespec.md`, `rules/rule-orchestration.md`, `rules/rule-ask.md`, `rules/rule-prespec-judges-the-spec-whole.md`, `estimates/estimate-prespec-confirms-the-findings-once.md`, `estimates/estimate-case-build-checks-the-finished-case.md`, `estimates/estimate-orchestration-shows-the-built-case.md`, `estimates/estimate-ask-finds.md`, `estimates/estimate-prespec-reconciles.md`, `estimates/estimate-orchestration-asks-in-the-grill-me-shape.md`, `lessons/lesson-ask-search-exclusion-of-decisions-left-to-each-agent.md`, `lessons/lesson-orchestration-dispatch-prompt-carried-counts-not-from-a-run.md` and `lessons/lesson-prespec-confirmation-prompt-invites-a-new-finding.md`. Over `.claude/` it printed `.claude/skills/pre-spec/SKILL.md` and `.claude/agents/ask-guppi.md`, and over `guppi/` it printed `guppi/casecheck.py`. The rules, their rendered files, the placeholder, and the `method` of `estimate-case-build-checks-the-finished-case` enter the Case; `backlog.md` is written by `guppi backlog`, and `log.md` was not read. The three lessons and the Result line of `estimate-ask-finds` record past runs, and the hit in `guppi/casecheck.py` speaks of the top-level Cases of an answer of `case-guppi`; they stand. Step 6 of the skill and `estimate-prespec-confirms-the-findings-once` send each run whose findings sent a Case back its Cases built again; with one run that is the one run, so both stay true and the Criterion stands. `estimate-orchestration-asks-in-the-grill-me-shape` names the question after the runs confirm their findings; it speaks of the shape of that question, not of the number of runs, so it stands. `estimate-ask-finds` promises the form of the answer, whose first line names the Cases the run checked; that stays true of one run, so it stands.
> The other rules of the moment of `/pre-spec`, `rule-prespec-hook` and `rule-prespec-onward`, act on the check and the exit, not on the dispatch, and this Case does not cover them. Cases 672 and 673 of this session update other paragraphs of `rule-orchestration`, on who ticks which box and on the acknowledging reply; 674.2 changes neither paragraph. The skill and agent texts change at the librarian's render, so the `/pre-spec` of this session still sends one run per Case. By case 670 the Retro of this session reads `estimate-prespec-reconciles` and `estimate-orchestration-shows-the-built-case` on the new text of the Spec. Their old `method` lines read a live `/pre-spec` and the transcript of a session's close, which in this session still show one run per Case; by case 670.4 a method holds only what runs in the Case's own session, so both are set anew to a reading at Retro of the new Render in the Spec, as Case 672 does for its Estimate. The `purpose` of `estimate-orchestration-shows-the-built-case` does not state the number of runs, and `estimate-prespec-reconciles` has no `purpose`, so neither is set anew.

> **problem:**
> `/pre-spec` sends one `ask-guppi` run per top-level Case. The person judges that cost too high for an unclear benefit, and wants one run over the whole Spec again. The question of what one run misses on a large Spec, and of what the Cases leave open together, stays open for later.

> **recommend:**
> - **How pre-spec checks the Spec**
>   - Recommended: (b) keep the per-Case runs and add one run over the whole Spec that asks only about the Cases together.
>   - Answer: after asking to weigh the pros and cons, the person said the per-Case runs are rather expensive and their benefit is unclear, and chose (a): back to one check of the whole Spec, to be thought over further later.
> - **What the single check asks**
>   - Recommended: (a) the same three questions as before the per-Case runs.
>   - Answer: agreed, (a).
> - **What happens to the backlog page**
>   - Recommended: (b) keep the placeholder as a draft, its purpose rewritten for what is left to think over, in the backlog as a reminder.
>   - Answer: agreed, (b).
> - **What the report says about how much was checked**
>   - Recommended: (a) keep the warning: the report gives the run's list of what it did not check and never says the whole Spec is checked.
>   - Answer: agreed, (a).

### Case 674.1 — Pre-spec sends one ask-guppi over the whole plan

> **given:**
> `rule-prespec`: the rule of the skill, whose Render sets the dispatch of `ask-guppi` and the report.
> **＋** `.claude/skills/pre-spec/SKILL.md`: the skill rendered from `rule-prespec`.
> **＋** `rule-ask`: the rule of the agent `ask-guppi`, whose Purpose and Render name its runs at pre-spec.
> **＋** `.claude/agents/ask-guppi.md`: the agent file rendered from `rule-ask`.
> **＋** `estimate-prespec-reconciles`: the check of pre-spec, its Criterion replaced whole.
> **＋** `estimate-case-build-checks-the-finished-case`: the check of the build of a Case, its `method` set anew.
> **＋** `rule-spec-write`: the hook that writes a Case ratified again into the plan.
> **＋** `vault/raw/<date>/<hi HHMM>/frontier.md`: the Frontier of the session, which the check reads.
> **＋** `rule-skill-hi`: the rule that sets the title line of the plan.

> **when:**
> The person invokes `/pre-spec`, or the agent calls the skill, before the Spec is approved, with `.claude/skills/pre-spec/SKILL.md` rendered from `rule-prespec` and `.claude/agents/ask-guppi.md` rendered from `rule-ask`.

> **then:**
> The agent runs `uv run guppi prespec --check` on the plan file with `--session <id>`, the eight-character id of the `hi:` line, and reads the first line of the output before the exit code — "no hi recorded for session …; nothing checked" means the wrong value; nothing is translated before the run.
> **＋** A finding in a Case — in its prose or in its body, a wrong fact of its `context` included — goes to the `case-guppi` of that Case by `SendMessage`; its new answer is shown and ratified again, and the hook of `rule-spec-write` writes it into the plan; the agent does not edit the text of a Case in the plan file.
> **＋** A finding in `vault/raw/<date>/<hi HHMM>/frontier.md` or in a line of the session's ledger is fixed there, and the command runs again until it prints no finding.
> **＋** At the first run of `/pre-spec` in the session, the agent dispatches one `ask-guppi` over the plan, or over the conserved Spec that the plan's title line names, as `rule-skill-hi` sets that line, with the absolute path of the plan file, the instruction to judge every Case outside `## Deferred` with its sub-cases, and the instruction to read for each such Case its `context`, `when`, `then` and `then` block and, for an `update` of a rule or an entity, the page's `estimates`; of a Case under `## Deferred` it reads only the slugs of its `defer` items.
> **＋** Three questions: which decisions contradict a page of the vault, a rule of the vault, or each other; whether an Estimate the Case does not name speaks of the thing the Case changes; which fact of a `context` — a page's status, a count, a case number, a claim that no page holds a thing — the vault does not bear out.
> **＋** The agent answers the findings with one report before any Case is sent back: the list of what the `ask-guppi` run did not check; each finding numbered, with the fix it proposes or why it is already known, the findings that need the person apart from those that do not, and the decisions it needs from the person; after the Cases built again on the findings are ratified, it does not call `/pre-spec` again, but runs the check, fixes what it prints, and exits Plan Mode when the check prints no finding.
> **＋** `guppi gate` writes the stamped `prespec` line on the Skill call.
> **－** No second `ask-guppi` is dispatched at the first run, and a later run of `/pre-spec` in the session dispatches none.
> **－** The report never says that the whole Spec is checked.
> **－** The agent writes no list of the decisions: the plan is the list.
> **－** The body of a deferred decision is not read; a Case that changes a page another Case of the plan defers is still a finding.

> **tasks:**
> - [ ] update `rule-prespec`
>   - old: `` dispatch one `ask-guppi` agent for each top-level Case outside the `## Deferred` heading — of the plan, or, when the plan's title line names a conserved Spec, of that Spec — all in one message, each with the absolute path of the plan file, the id of the Case it judges — that Case and its sub-cases, the other Cases read only to find a clash with them (case 634.1) — and the instruction to read ``
>   - new: `` dispatch one `ask-guppi` agent over the plan, or, when the plan's title line names a conserved Spec, over that Spec, with the absolute path of the plan file, the instruction to judge every Case outside the `## Deferred` heading with its sub-cases (case 674.1), and the instruction to read ``
>   - old: `` for each `ask-guppi` run, the Case it judged and its list of what it did not check, with no claim that the whole Spec is checked (case 634.1); ``
>   - new: `` the list of what the `ask-guppi` run did not check, with no claim that the whole Spec is checked, since one run over a large Spec returns only part of the findings (cases 634.1, 674.1); ``
>   - change: `the first run of /pre-spec sends one ask-guppi over the whole plan or the conserved Spec its title line names; the report gives what that run did not check and never says the whole Spec is checked (case 674.1)`
> - [ ] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
> - [ ] update `rule-ask`
>   - old: `The main agent asks at pre-spec, one run for each top-level Case of the set of ratified Cases (case 634.1);`
>   - new: `The main agent asks at pre-spec, one run over the whole set of ratified Cases (case 674.1);`
>   - old: `the main agent asks at pre-spec, one run per top-level Case of the set;`
>   - new: `the main agent asks at pre-spec, one run over the whole set;`
>   - old: `where the caller names the Case you judge — that Case and its sub-cases, the other Cases of the plan read only to find a clash with them (case 634.1) — and asks`
>   - new: `where the caller asks you to judge every Case of the plan with its sub-cases (case 674.1), and asks`
>   - change: `at pre-spec one ask-guppi run judges every Case of the plan with its sub-cases (case 674.1)`
> - [ ] `uv run guppi render`: `.claude/agents/ask-guppi.md`
> - [ ] update `estimate-prespec-reconciles`
>   - set:
>     ```
>     status: pending
>     method: "by hand at Retro of the session that changes it: the new Render of rule-prespec and rule-ask in the Spec, read against the Criterion, recorded in the estimate line"
>     ```
>   - change: `the Criterion replaced whole — one ask-guppi over the whole plan at the first run, the report giving what that run did not check; the method a reading of the new Render in the Spec at Retro (case 674.1)`
> - [ ] update `estimate-case-build-checks-the-finished-case`
>   - set:
>     ```
>     method: "by hand: at /pre-spec, the findings of ask-guppi, read for each Case case-guppi built — a Case that departs from a chosen option, a page naming a changed slug that the Case misses, a rule acting at the same moment that the Case misses, a Case of the session named in the prompt whose page or moment the Case clashes with, an Estimate whose purpose or method still states the promise its replaced Criterion dropped, a claim of context that its search did not print, a search in context that the Case does not rest on, two sub-cases whose texts on one page contradict; the count of each in the reading line"
>     ```
>   - change: `the method reads the findings of ask-guppi at pre-spec, no longer one run per top-level Case (case 674.1)`
> - [ ] read `estimate-prespec-reconciles`

> **ratification:**
> ```
> - decision[case 674.1][update][rule-prespec]{ref:rule-prespec}
> - decision[case 674.1][update][rule-ask]{ref:rule-ask}
> - decision[case 674.1][update][estimate-prespec-reconciles]{ref:rule-prespec}
> - decision[case 674.1][update][estimate-case-build-checks-the-finished-case]{ref:rule-case-build}
> ```

### Case 674.2 — The orchestration file names one ask-guppi run at pre-spec

> **given:**
> `rule-orchestration`: its Render says when the main agent dispatches `ask-guppi`.
> **＋** `vault/wiki/orchestration.md`: the file rendered from `rule-orchestration`.
> **＋** `estimate-orchestration-shows-the-built-case`: the check of the dispatch and the showing, its Criterion replaced whole.
> **＋** `.claude/skills/wait-what/SKILL.md`: the skill by which the main agent explains its own text.
> **＋** `.claude/skills/grill-me/SKILL.md`: the shape of a question of a round.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a Case that the main agent sends.
> **＋** `rule-case-check`: the hook that checks the file of a Case and the reply that shows it.

> **when:**
> The main agent takes up a Frontier item, the person answers a round of questions, answers a shown Case with a question or a change, or asks for a plain explanation of the agent's text — by `/wait-what` on `UserPromptSubmit` or in words — or a ratified Case changes and is shown again, in Plan Mode or in Work Mode, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> The main agent dispatches `case-guppi` with the Case id, the Frontier item and its source, and the person's words on it, in the prompt of the call, after the plan file stands with its title line; nothing of the Case stands in the chat before the answer.
> **＋** The person's answers to a round go to the same `case-guppi` by `SendMessage`, verbatim and untranslated, and so does a question or a change of the person on a shown Case that is not a request for a plain explanation.
> **＋** A request for a plain explanation of a round, of the short text on a Case or of a reply the main agent answers itself by `.claude/skills/wait-what/SKILL.md`; it sends the `case-guppi` of the Case a `SendMessage` only to ask for a fact of the Case, and `case-guppi` answers with the fact alone, under a first line `**Fact:**` and with no Case heading.
> **＋** An answer with no first line `**Built:**` and no first line `**Fact:**` is a round of questions: the main agent shows it in the chat translated into Russian line by line, slugs, paths and quotations unchanged, each quotation in its blockquote — the `**Context:**` paragraph that opens the first round on an item translated in place before the first question, each question in the order and with the number of the answer, opening with its `❓ **Qn** - **<title>**:` line of `.claude/skills/grill-me/SKILL.md` and closing with its `➡️` line, its title, body and recommended answer translated in place, nothing merged, dropped or added between the questions, the agent's own text after the last question and one horizontal rule; no Case is shown, no file is sent, and no step of confirmation follows the last round.
> **＋** The main agent shows a built Case at every showing by `SendUserFile` with `display: render` on `raw/<date>/<hi HHMM>/cases/case-<N>.md`, the file `case-guppi` wrote and the hook of `rule-case-check` checked. In the same reply it writes the heading of the top-level Case: its id, and its name in Russian translated from the `**Case:**` line of the summary `case-guppi` answered with. Under the heading it writes one list with an item per Case and sub-case of the summary: its id, its name in Russian, and a short text in Russian on what done means and how it is checked, taken from the Estimate the summary names for it. Then it writes one `ratification` with the ledger lines of every Case of the list as the summary holds them, and its own text after one horizontal rule. A summary in which a Case names no such Estimate goes back to its `case-guppi` by `SendMessage` before the Case is shown.
> **＋** A Case whose item in the summary carries a line `**Other Case:**` is shown as it stands, and the main agent asks the person whether that other Case is built again.
> **＋** A reply that shows a Case and that the `Stop` check of `rule-case-check` refuses is followed, before the person answers, by a reply that sends the file and shows the `ratification` as the summary holds it; a reply that shows a round and that the `Stop` check refuses is followed, before the person answers, by a reply that shows the round again with nothing before its `**Context:**` paragraph or its first question.
> **＋** A ratified Case that changes — in its prose or in its body — changes through its `case-guppi`, and its new file is sent and ratified again; the main agent edits no Case in the plan file or under `cases/`.
> **＋** An item that needs no decision the main agent closes alone, with no dispatch; it dispatches `ask-guppi` only at pre-spec, one run over the whole plan at its first run, never to build a Case, and asks that run again only to confirm its own findings.
> **－** The main agent writes the heading, the list, the `ratification` and the question on another Case from the summary, and does not read the file of the Case.
> **－** The heading carries no name of the main agent's own and not the words of the Frontier item.
> **－** The main agent writes no context of its own before the first question of a round.
> **－** The main agent writes no `given`, `when`, `then` or `tasks` of a built Case into the chat.
> **－** A deferred decision in the short form is written by the main agent in English in the chat, with no dispatch and no file.

> **tasks:**
> - [ ] update `rule-orchestration`
>   - old: `` the agent dispatches `ask-guppi` only at pre-spec, one run per top-level Case at its first run, and asks a run again only to confirm its own findings, as `rule-prespec` sets it (case 634.3). ``
>   - new: `` the agent dispatches `ask-guppi` only at pre-spec, one run over the whole plan at its first run, and asks that run again only to confirm its own findings, as `rule-prespec` sets it (cases 634.3, 674.2). ``
>   - change: `ask-guppi is dispatched only at pre-spec, one run over the whole plan, and asked again only to confirm its findings (case 674.2)`
> - [ ] `uv run guppi render`: `vault/wiki/orchestration.md`
> - [ ] update `estimate-orchestration-shows-the-built-case`
>   - set:
>     ```
>     status: pending
>     method: "by hand at Retro of the session that changes it: the new Render of rule-orchestration in the Spec, read against the Criterion, recorded in the estimate line"
>     ```
>   - change: `the Criterion replaced whole — ask-guppi only at pre-spec, one run over the whole plan, asked again only to confirm its findings; the method a reading of the new Render in the Spec at Retro (case 674.2)`
> - [ ] read `estimate-orchestration-shows-the-built-case`

> **ratification:**
> ```
> - decision[case 674.2][update][rule-orchestration]{ref:rule-orchestration}
> - decision[case 674.2][update][estimate-orchestration-shows-the-built-case]{ref:rule-orchestration}
> ```

### Case 674.3 — The placeholder of the whole-Spec check stays in the backlog for later

> **given:**
> `rule-prespec-judges-the-spec-whole`: the placeholder page of the backlog item, kept and put off again.
> **＋** `rule-page-generation`: the rule of `guppi generate`, which clears the defer this Case supersedes and writes the new one.
> **＋** `vault/wiki/backlog.md`: the backlog that lists a deferred page with its purpose.

> **when:**
> `guppi generate` of `rule-page-generation` applies the decisions of this Case, and `guppi backlog` writes `vault/wiki/backlog.md`.

> **then:**
> `rule-prespec-judges-the-spec-whole` stays a `draft` rule whose `purpose` and Purpose name what is left to think over: the problems the one `ask-guppi` run misses on a large Spec, and a question on what the Cases leave open together.
> **＋** Its `deferred_by` names the Decision page of this Case, and no longer the Decision page of case 643.
> **＋** `vault/wiki/backlog.md` lists it under `## Deferred` with its new purpose.
> **－** No harness file changes, and the `ask-guppi` run of pre-spec asks no question on what the Cases leave open together.

> **tasks:**
> - [ ] update `rule-prespec-judges-the-spec-whole`
>   - set:
>     ```
>     purpose: "Prevents a large Spec from being approved with problems that the one ask-guppi run of /pre-spec did not return, and holds open whether that run also asks what the Cases together leave unanswered; left by the person to think over (case 674.3)"
>     ```
>   - sections.Purpose: `Prevents a large Spec from being approved with problems that the one ask-guppi run of /pre-spec did not return, and holds open whether that run also asks what the Cases together leave unanswered; left by the person to think over (case 674.3)`
>   - change: `the purpose rewritten for what is left to think over after pre-spec went back to one ask-guppi run; the defer of case 643 retired and the page put off again (case 674.3)`
> - [ ] defer `rule-prespec-judges-the-spec-whole`
>   - type: `rule`
>   - purpose: `Prevents a large Spec from being approved with problems that the one ask-guppi run of /pre-spec did not return, and holds open whether that run also asks what the Cases together leave unanswered; left by the person to think over (case 674.3)`

> **ratification:**
> ```
> - decision[case 674.3][update][rule-prespec-judges-the-spec-whole]{ref:rule-prespec-judges-the-spec-whole}{supersedes:case 643}
> - decision[case 674.3][defer][rule-prespec-judges-the-spec-whole]
> ```
