## Case 561 — The main agent's run from the Frontier to the approved Spec

> **context:**
> The main agent runs each working session from `/hi` to the approved Spec. It takes its orders from `vault/wiki/case-schema.md`, the Render of `rule-case-protocol` that `/hi` loads, and from the skill `/pre-spec`, the Render of `rule-prespec`. The worst failure comes after `/pre-spec` reports findings. The skill says to report them and to show the changed Cases again in one reply. It sets no order for the fixes, the rounds and the waiting in between. In session 2042 the main agent sent findings to four `case-guppi` agents at once and passed on each answer as it came. Two rounds, two Cases built again and one question of its own were spread over four replies, and the person could not tell what to answer (`lesson-prespec-findings-relayed-piecemeal-lose-the-person`). A second run of the skill then sent `ask-guppi` over the whole plan again for eight minutes, with no word to the person first (`lesson-prespec-second-run-dispatches-ask-guppi-again`). The open insight `insight-prespec-after-findings-loop-unruled` joins the two lessons. The main agent's own questions in the pre-spec report took no fixed shape (`insight-prespec-main-agent-question-off-the-grill-me-shape`). Case 546 put that decision off onto the placeholder `rule-orchestration`. The schema also has other gaps. After the last Case of the Frontier, the main agent asks whether to run `/pre-spec`, although no other step is left: cases 461 and 547 wrote that question into the Frontier reply and the defer reply. The acknowledging reply always ends with the question which item is next. The hook on `ExitPlanMode` checks only that `/pre-spec` was called, not that its check is clean. The reply before a ratification shows each sub-case under its own heading with a text on what it changes, but not what done means and how it is checked. When the person asks to discuss an item, the main agent reads the pages itself, which is the work of `case-guppi`. The person decided the design in six rounds, and the recommend below records them. The person chose to move the main agent's rules into files of their own: a file of `rule-orchestration` loaded by `/hi` in place of `case-schema.md`, a third small file for the parts both agents need, and `case-schema.md` read by `case-guppi` alone. The checks of the behaviours that move would become new Estimates on the new rules. That move is left for a later session, and this Case changes the behaviours where their text stands today. `rule-orchestration` keeps its defer of case 424, which holds that move. Case 561.13 rewrites its `purpose` to the design the person ratified, so the later session finds the move in the backlog. This Case takes up three defers, as the rule of case 429 requires, each on a decision line that also names its page. 561.13 carries `{supersedes:case 546}`, because the question shape that case put off onto `rule-orchestration` is decided here. 561.1 carries `{supersedes:case 503}` on its line for `rule-prespec`. Case 503 deferred the question that the skill `/pre-spec` sets neither the numbering of its report in one sequence nor its split into two parts, so the form of the report depends on the agent. The new Render of 561.1 numbers the findings and sets apart those that need the person from those that do not. 561.9 carries `{supersedes:case 560}` on its line for `estimate-case-protocol-shows-the-built-case`. Case 560 deferred that Estimate over the fault it found in session 1736: the main agent wrote a line of its own before the first question of a round of `case-guppi`. The problem of that defer, as its Decision page states it, was only that the defer must not target a page that Case 557.2 changed in the same Spec. The History of the Estimate records the defer of case 560. A Grep of the page for `^deferred_by:` printed nothing, and a Grep for `560|deferred` printed its History line and one line of its Criterion. 561.9 replaces the Criterion of that Estimate whole. The new Criterion carries word for word the line that the main agent writes no context of its own before the first question of a round, and the Estimate is set `pending`, so its reading after the render judges that fault again. The person decided this in the first round of Case 562. Case 562 adds a `Stop` check in `guppi casecheck` that refuses a reply showing a round of `case-guppi` unless the reply opens with the round's `**Context:**` paragraph or its first question. Its `case-guppi` found that the schema's sentence on a refused reply — followed by a reply that sends the file and shows the `ratification` — becomes false for a round, which has no Case file and no ledger lines. The person chose that 561.9 narrows that sentence, and its line in the Criterion, to a reply that shows a Case, and adds that a refused round is shown again with nothing before it. Case 562 does not replace this Criterion. Item C3 asked whether a second pre-spec run tells the person its cost first. That question falls away: 561.1 runs `ask-guppi` at the first run only. Each sub-case holds one promise, and each creates or replaces an Estimate, so each one answers what done means. What `case-guppi` found in the frame: after a reply that carries a `LEDGER` block, the schema allows no tool call in the same reply, so the main agent cannot call `/pre-spec` by itself after the last ratification. That is why 561.5 adds a `Stop` hook on the model of `rule-retro-onward`. It is a new flag `--plan` of `guppi onward`, registered as a hook of its own after `guppi onward`, so the run without the flag and its promise `estimate-retro-onward-sends-the-agent-to-the-handoff` stand. The `Stop` hooks run in parallel, so the new hook reads the decision lines of the reply beside `ledger.md`, as the check after the write in `guppi/prespec.py` already does. `rule-rules-schema` gives a Leaf no `## How it works`, says a Purpose states the failure the rule prevents, and keeps the mechanism of a Leaf in the docstring of its code. So 561.1 moves the description of what the check compares out of the skill into the module docstring of `guppi/prespec.py`, and appends to the Purpose of the Leaf `rule-prespec-hook` one sentence that points there. The sentence on the comparison that 561.4 adds goes into the same docstring by 561.4's own task. 561.3 changes two other sentences of the same Purpose, and its anchors stay on the page: 561.1 appends after a third sentence, and the three anchors each stand once and do not overlap. 561.3 also gives `estimate-prespec-hook-gates` a new `purpose`, since the old one stated only the wait for `/pre-spec`. The loop of 561.2 stands in the Render of `rule-prespec` that 561.1 writes whole. 561.2 changes only the schema's rule that no Case is taken up before the current one is ratified, at both places the rule stands. The schema's line that one reply is one Case stands beside the showing of every rebuilt Case in one reply, as it has since case 388. For 561.13, `estimate-where-to-stop-stops-only-on-its-conditions` speaks of when the agent stops at a fork, not of the shape of its question, so it stands. `estimate-hi-takes-its-readings` and `rule-skill-hi` stand too: the question of an open `A` line at `/hi` asks for a reading, not a choice among options, and the person chose that it keeps its own form, the Estimate by slug and its question. `rule-case-check` is a Leaf that still carries `## How it works`. 561.10 changes one sentence there, as case 555.1 did, and the removal of that section, which the schema of rules asks for at its next touch, is not taken up here. The exit hook of 561.3 runs the same judgment as `--check` within its 30-second timeout. `judge` already runs inside the 30-second `SubagentStop` hook of `rule-case-check`. The vault holds no record of whether `SendMessage` calls to several `case-guppi` agents come back in one turn. A Grep of `vault/wiki/` for `background|foreground|task-notification|run_in_background` printed `estimate-skill-wait-what-re-pitches` and `decision-case-502`, and neither is about it. The reading of `estimate-prespec-gathers-the-answers-after-findings` will show whether the main agent can stay quiet while answers are out. Searches over the frame: a Grep for `pre-spec|ExitPlanMode` over `vault/wiki/rules/` printed `rule-retro-commit`, `rule-ledger-write`, `rule-case-protocol`, `rule-case-check`, `rule-spec-write`, `rule-skill-hi`, `rule-prespec`, `rule-ask`, `rule-entities-schema`, `rule-spec-capture`, `rule-carry-over`, `rule-hook-registry`, `rule-work-mode`, `rule-prespec-hook`, `rule-atomicity`, `rule-guppi-config`, `rule-prespec-script-skips-code-spans` and `rule-session`. Over `.claude/` the same Grep printed `skills/work/SKILL.md`, `skills/hi/SKILL.md`, `settings.json`, `skills/pre-spec/SKILL.md`, `skills/carry/SKILL.md` and `agents/ask-guppi.md`. Of the hits outside `given`, `rule-ask` and `ask-guppi.md` say that the main agent asks `ask-guppi` once at pre-spec, which stays true. `rule-session` says that the pre-spec hook refuses `ExitPlanMode` before `/pre-spec` ran, which stays true. `rule-spec-write` runs `judge` after a write, so the finding of 561.4 opens with the later Case. The other hits set no form at these moments. A Grep for `rule-prespec-hook|rule-prespec\b|rule-case-check|rule-case-build|rule-case-protocol` over `vault/wiki/rules/` printed nineteen files, and over `vault/wiki/entities/` three. Among the hits outside `given`, `rule-backlog`, `rule-insights-schema`, `rule-entities-schema` and `entity-glossary` name `rule-case-protocol` for the clearing of a defer, `rule-plan-mode` lists the children, and `rule-spec-write` and `rule-spec-reconcile` name the store. None becomes false. A Grep for `short .{0,20}text` printed `rule-case-build`, `rule-case-protocol`, `rule-case-check`, `rule-language`, `rule-spec-write` and `rule-skill-wait-what` under `rules/`. Under `estimates/` it printed `estimate-case-protocol-defers-in-one-reply`, `estimate-case-check-shows-only-the-checked-case`, `estimate-case-protocol-case-form`, `estimate-case-protocol-shows-the-built-case`, `estimate-language-followed`, `estimate-spec-write-writes-a-defer` and `estimate-skill-wait-what-re-pitches`. The chat still holds a short text in the chat language on each Case and sub-case, now the answer on what done means, so the pages of the language, of `wait-what` and of the form stand. The two Estimates that set how the chat shows a Case, `estimate-case-protocol-shows-the-built-case` and `estimate-case-check-shows-only-the-checked-case`, are replaced by 561.9 and 561.10. A Grep for ``shows? `?## Case|under its heading|at least one of its sections`` over `vault/wiki/estimates/` printed `estimate-case-check-shows-only-the-checked-case`, `estimate-spec-write-copies-the-ratified-case` and `estimate-spec-write-writes-a-defer`. The Spec hook's promise reads a showing through the comparison it imports from `guppi/casecheck.py`, so it stands. `estimate-case-build-writes-the-case` names the promise among the forks of `case-guppi` and stays true, and the new answer on what done means is the Estimate of 561.11. The check of the answer noted lines of the replaced Criteria that are not carried. Each of them changes on purpose. In 561.1 these are the dispatch of `ask-guppi`, now at the first run only; the report, which now sorts the findings; and the exit after the gate line, which now follows the loop. In 561.3 the first `then` line changes, because the hook now exits 0 only on a clean check. In 561.6 and 561.7 the line of the question changes, and in 561.7 the line on the text after it. In 561.8 the first `then` line loses the unconditional question. In 561.9 the line of the showing changes, and the line of a refused reply is narrowed to a Case and joined by the line of a refused round. Every other line of those Criteria is carried word for word. The check also noted `then` lines of sibling sub-cases that share most of their words. They share the words of the Frontier, the findings, the plan, the hooks and the showing, and some of them are lines carried word for word from the Criteria they replace. Each line is still a promise of its own sub-case and names its own reply, hook or check.

> **problem:**
> After `/pre-spec` the main agent has no rule for the loop over the findings. It passes on answers one by one, runs `ask-guppi` again on each call, and asks its own questions in a shape of its own. Before the Spec it stops for questions with only one possible answer. Its exit from Plan Mode is not tied to a clean check. It shows a Case without saying what done means. And it reads the pages itself to discuss an item. The question is how the main agent runs from the Frontier to the approved Spec, in the texts that govern it today.

> **recommend:**
> - **Where do the main agent's rules live?**
>   Recommended: (a) a rule of its own for the main agent, `rule-orchestration`, loaded by `/hi` in place of `case-schema.md`, with `case-guppi` alone reading `case-schema.md`.
>   Answer: (a). Carried out in a later session, as the later question on the size of this session decided.
> - **What happens after the pre-spec findings?**
>   Recommended: (a) one gathered loop. The main agent sorts the findings, sends the fixes that need no answer at once in one message, waits quietly for every answer, gathers every question into one numbered list in the grill-me shape, sends the answers back, and shows all the rebuilt Cases in one reply for one ratification.
>   Answer: (a).
> - **Which of the main agent's own questions take the grill-me shape?**
>   Recommended: (a) every question the main agent asks the person itself, at pre-spec, at `/hi` and at a stop of Work Mode.
>   Answer: (a).
> - **What does the reply before ratification hold?**
>   Recommended: (a) the file and its path, one list of the Case and its sub-cases by name, a short answer under each name on what done means and how it is checked, and the ledger lines; the main agent asks `case-guppi` when a Case gives no such answer.
>   Answer: (a).
> - **How does every Case answer "what does done mean"?**
>   Recommended: (a) every Case creates or changes an Estimate, or names the Estimate that already checks the change and says why its Criterion stands; with neither, `case-guppi` asks in a round what the Estimate will check.
>   Answer: (a).
> - **Does the main agent ask before `/pre-spec`?**
>   Recommended: (a) run it at once when no line under `## Cases` is open.
>   Answer: (a).
> - **What blocks leaving Plan Mode?**
>   Recommended: (a) the hook on the exit runs the mechanical check itself and refuses while it prints a finding; a note does not block.
>   Answer: (a). The person added the order: the skill runs the check and, when it is clean, `ask-guppi`; the hook makes sure the check is clean, and the skill itself can be shortened.
> - **Does the main agent call `/pre-spec` again after the rebuilt Cases?**
>   Recommended: (a) no second call: after the rebuilt Cases are ratified, the main agent runs the check alone, fixes what it prints and exits Plan Mode, and the hook runs the check again at the exit.
>   Answer: (a).
> - **How is this item split?**
>   Recommended: (a) one Case with one sub-case per promise.
>   Answer: (a).
> - **Where does the text both agents need go?**
>   Recommended: (b) the parts both agents need in a third small file of its own rule, loaded by `/hi` and read by `case-guppi`; the main agent's file for what it alone does; `case-schema.md` for the form of a Case.
>   Answer: (b), agreed. The person had first asked whether option (a) duplicated text and why `case-guppi` would read the orchestration text. The question was asked again with this option. Carried out in a later session.
> - **What happens to the checks of the behaviours that move?**
>   Recommended: (a) new Estimates on `rule-orchestration` for the behaviours that move, the old ones withdrawn, and the check of the loaded file rewritten.
>   Answer: (a). Carried out in a later session.
> - **What form does the list in the reply take?**
>   Recommended: (a) one heading, one list with an item per sub-case and its line on what done means, and one block of ledger lines; the two hooks that read a showing learn this form.
>   Answer: (a).
> - **Does the whole item stay in this session?**
>   Recommended: (b) the behaviours now, in the texts where they stand today; the split into three files and the move of the checks in a later session.
>   Answer: (b), agreed. The decisions on where the rules live and on the three files stand and are carried out later.
> - **How does `/pre-spec` start with no question?**
>   Recommended: (a) a `Stop` hook sends the agent on, in the same way as the hook after Retro: once, after the reply that leaves no Case open, with the ledger lines already written.
>   Answer: (a), agreed.

### Case 561.1 — The pre-spec skill gives the order and asks the vault once

> **recommend:**
> - **How often does `ask-guppi` check the plan?**
>   Recommended: (a) once per session, at the first `/pre-spec`; later checks are mechanical, and a rebuilt Case is checked by its own `case-guppi`.
>   Answer: (a). The person accepts the risk left and asked for another option to be named. That option became Case 561.4.
> - **What stays in the `/pre-spec` skill?**
>   Recommended: (a) a short skill that gives the order, with the list of what the check prints moved to `rule-prespec-hook`.
>   Answer: (a).
> - **Change**
>   Asked: the pre-spec check found that the new Render decides the question that case 503 put off on `rule-prespec`, the numbering of the report and its split into two parts. The person agreed with the recommended fix.
>   Taken: the decision line of this sub-case on `rule-prespec` carries `{supersedes:case 503}`.
> - **Change**
>   Asked: the pre-spec check found that a catalog of what the check compares in the Purpose of the Leaf `rule-prespec-hook` goes against `rule-rules-schema`, which keeps the mechanism of a Leaf in the docstring of its code. The person agreed with the recommended fix. The choice to take the catalog out of the skill and put it beside the code stands.
>   Taken: the catalog goes into the module docstring of `guppi/prespec.py` as a Work Mode task. The Purpose of `rule-prespec-hook` gains one sentence that points there, and the Render of the skill names the docstring.

> **given:**
> `rule-prespec` — the rule of the skill `/pre-spec`, whose Render this sub-case writes whole, and whose defer of case 503 it retires
> **＋** `.claude/skills/pre-spec/SKILL.md` — the skill file it renders into
> **＋** `rule-prespec-hook` — the rule of `guppi/prespec.py`, whose module docstring takes the description of what the check compares and whose Purpose points there
> **＋** `estimate-prespec-reconciles` — the promise of the run of the skill, whose Criterion this sub-case replaces whole
> **＋** `rule-ask` — the rule of `ask-guppi`, which says that the main agent asks once at pre-spec
> **＋** `rule-case-build` — `case-guppi`, which checks each Case built again against the vault and its frame
> **＋** `rule-spec-write` — the hook that writes a Case ratified again into the plan

> **when:**
> The person invokes `/pre-spec`, or the agent calls the skill, before the Spec is approved.

> **then:**
> The agent runs `guppi prespec --check` on the plan file with `--session <id>`, the eight-character id of the `hi:` line, and reads the first line of the output before the exit code — "no hi recorded for session …; nothing checked" means the wrong value; nothing is translated before the run.
> **＋** A finding in a Case — in its prose or in its body, a wrong fact of its `context` included — goes to the `case-guppi` of that Case by `SendMessage`; its new answer is shown and ratified again, and the hook of `rule-spec-write` writes it into the plan; the agent does not edit the text of a Case in the plan file.
> **＋** A finding in the Frontier or in a ledger line is fixed there, and the command runs again until it prints no finding.
> **＋** At the first run of `/pre-spec` in the session, `ask-guppi` is dispatched once with the absolute path of the plan file and the instruction to read every Case outside `## Deferred` — `context`, `when`, `then`, the `then` block — and, for an `update` of a rule or an entity, the page's `estimates`; of a Case under `## Deferred` it reads only the slugs of its `defer` items; a later run of `/pre-spec` in the session dispatches no `ask-guppi`.
> **＋** Three questions: which decisions contradict a page of the vault, a rule of the vault, or each other; whether an Estimate the Case does not name speaks of the thing the Case changes; which fact of a `context` — a page's status, a count, a case number, a claim that no page holds a thing — the vault does not bear out.
> **＋** The agent answers the findings with one report before any Case is sent back: each finding numbered, with the fix it proposes or why it is already known, the findings that need the person apart from those that do not, and the decisions it needs from the person; after the Cases built again on the findings are ratified, it does not call `/pre-spec` again, but runs the check, fixes what it prints, and exits Plan Mode when the check prints no finding.
> **＋** `guppi gate` writes the stamped `prespec` line on the Skill call.
> **－** The agent writes no list of the decisions: the plan is the list.
> **－** The body of a deferred decision is not read; a Case that changes a page another Case of the plan defers is still a finding.

> **tasks:**
> - [ ] update `rule-prespec` — the Render written whole
>   - sections.Render:
>     ````
>     <!-- rule-prespec -->
>     ---
>     name: pre-spec
>     description: Check this Plan Mode's ratified decisions against each other and the vault before the Spec is approved.
>     ---
>
>     Run `uv run guppi prespec --check <the plan file of this Plan Mode> --session <id>`, the eight-character session id — the second token of the `hi:` line the `UserPromptSubmit` hook put in the context at `/hi`, between the time and the folder (cases 213.3, 256). Read the first line of the output before the exit code: 'no hi recorded for session …; nothing checked' means the wrong value, and the check did not run. Each line it prints is a finding, except a line that opens with `note:`, which is no finding: it sets no exit code and is answered in one line in the chat (case 378.8). What the check compares is written in the module docstring of `guppi/prespec.py`, beside its code (case 561.1). Fix a finding in the Frontier or in a ledger line yourself, and run the check again until it prints no finding of that kind. A finding in a Case — its prose or its body, a wrong fact of its `context` included — goes to the `case-guppi` of that Case in the loop below; do not edit the text of a Case in the plan (cases 438, 441).
>
>     At the first run of `/pre-spec` in the session only, dispatch the `ask-guppi` agent once with the absolute path of the plan file and the instruction to read for every Case there outside the `## Deferred` heading its `context`, its `when` and `then` sections and its `then` block — `replace` old and new, `set`, `sections` — and, for an `update` of a rule or an entity, the page's `estimates`, before judging a page, so that a finding can name a wrong wording or a wrong place, and of a Case under `## Deferred` only the slugs of its `defer` items; the agent writes no list of the decisions — the plan is the list (case 388). Three questions: which of these contradict a page of the vault, a rule of the vault, or each other; whether an Estimate the Case does not name speaks of the thing the Case changes — one that does is a finding (case 203.2); which fact of a `context` — a page's status, a count, a case number, a claim that no page holds a thing — the vault does not bear out (case 388). A later run in the session dispatches no `ask-guppi`: each Case built again is checked against the vault and its frame by its own `case-guppi` (case 561.1). The body of a Case under `## Deferred` is not read: the session that takes the defer up judges it with its own pre-spec. A Case of this plan that changes a page another Case of this plan defers is still a finding (case 186.2).
>
>     Answer the findings with one report before any Case is sent back: each finding numbered, with the fix you propose or, in one line, why it is already known; the findings that need no word of the person apart from those that need one; and each decision you need from the person as a question in the shape of `.claude/skills/grill-me/SKILL.md` (case 561.13). Then run the loop (case 561.2):
>
>     1. Send each finding in a Case that needs no word of the person to the `case-guppi` of that Case by `SendMessage`, all of them in one message. Hold back a finding whose fix waits for the person's answer.
>     2. Wait for every `case-guppi` you sent to answer. Write nothing in the chat while an answer is still out, and pass on no answer of one `case-guppi` alone.
>     3. Show the person one list of what to answer: your own questions still open and every round that came back, each question in its grill-me shape, translated as a round of `case-guppi` is, and numbered `<Case id>.Q<n>` — the id of its Case and its number in the round, or in your report for your own — so that each answer goes back to its `case-guppi`.
>     4. Send each answer, and each finding held back for it, to the `case-guppi` of its Case, all in one message, and go on from step 2 until every `case-guppi` you sent has answered with its Case.
>     5. Show every Case built again in one reply, each in the showing that `vault/wiki/case-schema.md` sets, for one ratification.
>
>     Inside this loop the rule of `vault/wiki/case-schema.md` that no Case is taken up before the current one is ratified does not hold: the Cases built again go out together and come back together. After their ratification do not call `/pre-spec` again: run the check above and fix what it prints; when it prints no finding, exit Plan Mode. The hook of `rule-prespec-onward` sends you on after the reply that acknowledges the ratification, and the hook of `rule-prespec-hook` refuses the exit while the check prints a finding (cases 561.3, 561.5).
>     <!-- /rule-prespec -->
>     ````
>   - change: `the skill gives the order - the check, the fixes, ask-guppi at the first run of the session only, one numbered report that sets apart the findings that need the person, the loop after the findings, no second call; what the check compares moves to the docstring of guppi/prespec.py; the defer of case 503 retired (cases 561.1, 561.2)`
> - [ ] update `rule-prespec-hook` — the Purpose points to the docstring that says what the check compares
>   - old:
>     ````
>     Named `pretask` until case 261.
>     ````
>   - new:
>     ````
>     Named `pretask` until case 261. What `--check` compares, the check the skill `/pre-spec` runs, is written in the module docstring of `guppi/prespec.py`, beside its code (case 561.1).
>     ````
>   - change: `the Purpose points to the module docstring of guppi/prespec.py for what the check compares (case 561.1)`
> - [ ] update `estimate-prespec-reconciles`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole - ask-guppi at the first run of the session only, one report that sorts the findings, no second call after the Cases built again are ratified (case 561.1)`
> - [ ] `guppi/prespec.py`: the module docstring holds what `--check` compares, the paragraph the Render of `rule-prespec` held before this Case — from the decision line with no item to the `note:` lines — with the language of `guppi.toml` named as the documentation language
> - [ ] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
> - [ ] read `estimate-prespec-reconciles` — in a later session

> **ratification:**
> ```
> - decision[case 561.1][update][rule-prespec]{ref:rule-prespec}{supersedes:case 503}
> - decision[case 561.1][update][rule-prespec-hook]{ref:rule-prespec-hook}
> - decision[case 561.1][update][estimate-prespec-reconciles]{ref:rule-prespec}
> ```

### Case 561.2 — The answers after the findings are gathered into one list

> **given:**
> `rule-prespec` — the rule of `/pre-spec`, whose Render, written by Case 561.1, holds the loop
> **＋** `rule-case-protocol` — the schema rendered into `vault/wiki/case-schema.md`, whose rule that no Case is taken up before the current one is ratified gains the exception of the loop
> **＋** `estimate-prespec-gathers-the-answers-after-findings` — the promise this sub-case creates
> **＋** `.claude/skills/grill-me/SKILL.md` — the question shape of each question of the list
> **＋** `rule-case-build` — `case-guppi`, which answers each message of the loop

> **when:**
> `/pre-spec` has reported findings in Cases of the plan, and the main agent sends them to the `case-guppi` of those Cases.

> **then:**
> The main agent sends each finding in a Case that needs no word of the person to the `case-guppi` of that Case by `SendMessage`, all of them in one message, and holds back a finding whose fix waits for the person's answer.
> **＋** It writes nothing in the chat while an answer of a `case-guppi` it sent is still out, and passes on no answer of one `case-guppi` alone.
> **＋** It then shows the person one list of what to answer: its own questions still open and every round that came back, each question in the shape of `.claude/skills/grill-me/SKILL.md` and numbered `<Case id>.Q<n>` by the Case it belongs to.
> **＋** It sends each answer, with each finding held back for it, to the `case-guppi` of its Case in one message, and repeats the wait and the list until every `case-guppi` it sent has answered with its Case.
> **＋** It then shows every Case built again in one reply, for one ratification.
> **－** Outside this loop no Case is taken up before the current one is ratified or deferred.
> **－** A question that no answer settles stays in the next list under its number.

> **tasks:**
> - [ ] update `rule-case-protocol` — the rule of one Case at a time names the loop as its exception
>   - old:
>     ````
>     Never move to the next Case until this one is ratified or deferred.
>     ````
>   - new:
>     ````
>     Never move to the next Case until this one is ratified or deferred — but in the loop after the findings of `/pre-spec`, where the Cases built again go out together and come back for one ratification, as `rule-prespec` sets it (case 561.2).
>     ````
>   - old:
>     ````
>     **Never move to another Case until the current one is ratified or deferred.**
>     ````
>   - new:
>     ````
>     **Never move to another Case until the current one is ratified or deferred** — but in the loop after the findings of `/pre-spec`, which `rule-prespec` sets (case 561.2).
>     ````
>   - change: `one Case at a time holds outside the loop after the findings of pre-spec (case 561.2)`
> - [ ] create `estimate-prespec-gathers-the-answers-after-findings`
>   - ref: `rule-prespec`
>   - kind: `QA`
>   - purpose: `Whether after the findings of pre-spec the main agent sends the fixes to their case-guppi at once, stays quiet while answers are out, gathers every question into one numbered list, and shows the Cases built again in one reply`
>   - method: `by hand at the /pre-spec of a later session whose report sends findings to two or more case-guppi, the replies between the report and the showing again and the SendMessage calls read in the transcript`
>   - tags: `[session, workflow]`
> - [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
> - [ ] read `estimate-prespec-gathers-the-answers-after-findings` — in a later session

> **ratification:**
> ```
> - decision[case 561.2][update][rule-case-protocol]{ref:rule-case-protocol}
> - decision[case 561.2][create][estimate-prespec-gathers-the-answers-after-findings]{ref:rule-prespec}{tags:session,workflow}
> ```

### Case 561.3 — The exit from Plan Mode waits for a clean check

> **recommend:**
> - **Change**
>   Asked: the pre-spec check found that the `purpose` of `estimate-prespec-hook-gates` still states the old promise, a wait for `/pre-spec` alone. The person agreed with the recommended fix.
>   Taken: the same update sets a new `purpose`: the exit waits for `/pre-spec` and for a check of the plan that finds nothing.

> **given:**
> `rule-prespec-hook` — the rule of the hook on `ExitPlanMode`
> **＋** `guppi/prespec.py` — the hook's run, which calls the judgment of `--check`
> **＋** `guppi/ledger.py` — `plan_path`, which finds the plan file of the session
> **＋** `tests/test_prespec.py` — the tests of the hook
> **＋** `estimate-prespec-hook-gates` — the promise of the hook, whose Criterion and `purpose` this sub-case replaces
> **＋** `/pre-spec` — the skill whose call leaves the `prespec` line
> **＋** `rule-hook-registry` — the registration of the hook, which does not change

> **when:**
> The hook `guppi prespec` receives a `PreToolUse` payload naming `ExitPlanMode` with the session's stamp, and asks whether `/pre-spec` ran in this session.

> **then:**
> With no `prespec` line of this session's stamp after its `hi`, the hook exits 2 with a reason that names `/pre-spec` and the session.
> **＋** With the line, it finds the plan file of the session by `plan_path` of `guppi/ledger.py`, runs on it the judgment of `uv run guppi prespec --check`, and exits 2 with the findings on stderr while the judgment finds one.
> **＋** With the line and a judgment that finds nothing it exits 0; a line that opens with `note:` does not block.
> **＋** With the line and no plan file of the session it exits 0.
> **＋** The window is open when the logs hold a `hi` of the session's stamp and a `prespec` of the same stamp after it; a mark of another stamp or `--------` does not count; a foreign `session-start` resets nothing.
> **＋** The logs it reads are the ledger hook's, from today back to the date of this session's `session-start`, so the `hi` and the `prespec` of yesterday's session are found after midnight.
> **＋** Any other tool exits 0.
> **－** Without a `hi` of this session the call passes.
> **－** An error of the hook itself prints `prespec: check skipped: <error>` on stderr and exits 0.

> **tasks:**
> - [ ] update `rule-prespec-hook` — the hook runs the check at the exit
>   - old:
>     ````
>     blocks the approval once; the `/pre-spec` call leaves the stamped line through `guppi gate` and the next exit passes.
>     ````
>   - new:
>     ````
>     blocks the approval; the `/pre-spec` call leaves the stamped line through `guppi gate`. With the line, the hook finds the plan file of the session by `plan_path` of `guppi/ledger.py`, runs on it the judgment of `--check` — the same function, not a copy — and exits 2 with its findings on stderr while it finds one; a line that opens with `note:` does not block, and with no plan file of the session the exit passes on the line alone (case 561.3).
>     ````
>   - old:
>     ````
>     `/pre-spec` runs it, the hook does not.
>     ````
>   - new:
>     ````
>     `/pre-spec` runs it, and the hook runs the same judgment at the exit (case 561.3).
>     ````
>   - change: `the hook on ExitPlanMode refuses while the check of the plan prints a finding (case 561.3)`
> - [ ] update `estimate-prespec-hook-gates`
>   - set: `{status: pending, purpose: "The ExitPlanMode hook holds a working session in Plan Mode until /pre-spec has run in it and the check of its plan finds nothing, across midnight too"}`
>   - change: `the Criterion replaced whole and the purpose set anew - with the prespec line the hook runs the check of the plan and refuses while it finds one (case 561.3)`
> - [ ] `guppi/prespec.py`: one function returns the findings and the notes of `--check` for a plan, a session and a moment; `check` prints them, and the hook's run calls the same function on the plan file that `plan_path` names, exits 2 with the findings on stderr while there is one, and exits 0 on notes alone or with no plan file; the module docstring says so
> - [ ] `tests/test_prespec.py`: with the `prespec` line, a plan with a finding gives exit 2 and the finding on stderr; a plan with only a note gives exit 0; no plan file gives exit 0; without the line the reason names `/pre-spec` as before
> - [ ] read `estimate-prespec-hook-gates` — in a later session

> **ratification:**
> ```
> - decision[case 561.3][update][rule-prespec-hook]{ref:rule-prespec-hook}
> - decision[case 561.3][update][estimate-prespec-hook-gates]{ref:rule-prespec-hook}
> ```

### Case 561.4 — The check finds two Cases that change one thing

> **recommend:**
> - **Does the check compare Cases that change the same thing?**
>   Recommended: (a) add the three comparisons as findings: one field set to two values, one section written twice, one Criterion replaced twice.
>   Answer: (a).
> - **Change**
>   Asked: the pre-spec check moved the description of what the check compares from the Purpose of `rule-prespec-hook` to the module docstring of `guppi/prespec.py`. The person agreed with the recommended fix.
>   Taken: the sentence on this comparison stands in that docstring, written by this sub-case's task on `guppi/prespec.py`, and no longer on the page of `rule-prespec-hook`.

> **given:**
> `rule-prespec` — the rule of the check, whose promises this one joins
> **＋** `guppi/prespec.py` — the function that compares the Cases, called by `judge`, and the module docstring that describes it
> **＋** `guppi/materialize.py` — `names_a_part`, which tells an `update` that replaces a Criterion whole
> **＋** `tests/test_prespec.py` — the tests of the check
> **＋** `estimate-prespec-catches-two-cases-on-one-target` — the promise this sub-case creates
> **＋** `rule-case-check` — the check of an answer of `case-guppi`, which runs `judge`

> **when:**
> `uv run guppi prespec --check` runs on a plan file, or the hook of `rule-case-check` runs `judge` of `guppi/prespec.py` on an answer of `case-guppi`.

> **then:**
> It prints one finding for each two Cases of the plan whose `update` items name one page and set one field under `set` to two different values, naming both Cases, the page's slug and the field.
> **＋** It prints one finding for each two Cases whose `update` items write one section of one page under `sections`, naming both Cases, the page's slug and the section.
> **＋** It prints one finding for each two Cases that each replace the Criterion of one Estimate whole — an `update` of the Estimate that names no part by `names_a_part` of `guppi/materialize.py` — naming both Cases and the Estimate's slug.
> **＋** Each such finding opens with the later of the two Cases, so the check that runs after a Case is written into the plan gives it to that Case.
> **＋** The comparison is one function of `guppi/prespec.py` that `judge` calls, so the check of an answer of `case-guppi` finds the same between the Cases of one answer.
> **－** Two Cases that change different fields, different sections or different anchors of one page are no finding; their `replace` pairs stay judged by the simulation of the pairs.
> **－** Two items of one Case are no such finding: a second item of one kind and slug under one Case keeps the finding it has.
> **－** A Case under `## Deferred` is not compared.

> **tasks:**
> - [ ] create `estimate-prespec-catches-two-cases-on-one-target`
>   - ref: `rule-prespec`
>   - kind: `QA`
>   - purpose: `Whether the check finds two Cases of one plan that set one field of a page to two values, write one section twice, or replace the Criterion of one Estimate twice`
>   - method: `uv run pytest tests/test_prespec.py`
>   - tags: `[session, workflow, harness]`
> - [ ] `guppi/prespec.py`: a function over the Cases and their `then` blocks that gives the three findings, each opening with the later Case, called by `judge`; the module docstring, beside what `--check` compares, says so
> - [ ] `tests/test_prespec.py`: two Cases that set one field to two values, two that write one section, two that replace one Criterion whole — one finding each, opening with the later Case; two Cases that change different fields, sections or anchors of one page, and two that set one field to one value — no finding
> - [ ] read `estimate-prespec-catches-two-cases-on-one-target` — in a later session

> **ratification:**
> ```
> - decision[case 561.4][create][estimate-prespec-catches-two-cases-on-one-target]{ref:rule-prespec}{tags:session,workflow,harness}
> ```

### Case 561.5 — A hook sends the agent on to pre-spec and to the exit

> **given:**
> `rule-prespec-onward` — the rule of the hook, which this sub-case creates
> **＋** `estimate-prespec-onward-sends-the-agent-on` — the promise of the hook
> **＋** `guppi/onward.py` — the module of `guppi onward`, which takes the run of `--plan`; `guppi/cli.py` names it among the hook commands
> **＋** `tests/test_onward.py` — the tests of the hook
> **＋** `rule-hook-registry` — the registration of the hook on `Stop` in `.claude/settings.json`
> **＋** `rule-retro-onward` — the run of `guppi onward` without `--plan`, from Retro to `/handoff`, which stays as it is
> **＋** `raw/<date>/<hi HHMM>/spec.md`, `raw/<date>/<hi HHMM>/frontier.md`, `raw/<date>/<hi HHMM>/ledger.md` and `raw/<date>/<hi HHMM>/cases/` — the files of the session the hook reads
> **＋** `/pre-spec` — the skill the reason names, and `rule-prespec-hook`, the gate at the exit

> **when:**
> The `Stop` hook `uv run guppi onward --plan` receives the payload of the end of a reply of the main agent.

> **then:**
> It exits 2 when all of these hold: the event log of the session's window holds a `hi` of this session; `raw/<date>/<hi HHMM>/spec.md` does not stand; `raw/<date>/<hi HHMM>/frontier.md` holds no open line under `## Cases`; the reply carries a `LEDGER` block; no file under `raw/<date>/<hi HHMM>/cases/` was written after the last decision line of its Case, or of a sub-case, in `raw/<date>/<hi HHMM>/ledger.md` or in that block; `stop_hook_active` is false; and the reply does not open with `STOP:`.
> **＋** With no `prespec` line of this session after its `hi` in the event log, its reason on stderr tells the agent to call `/pre-spec` now.
> **＋** With that line, its reason tells the agent to run `uv run guppi prespec --check` on the plan file with `--session <id>`, to fix what it prints, and to call `ExitPlanMode` when it prints no finding.
> **＋** Each reason adds that, when only the person can go on — a Case still out with its `case-guppi`, or a question the person must answer — the agent opens its reply with `STOP:` and asks the person instead.
> **＋** In every other case with no error of its own it exits 0 and prints nothing.
> **＋** An error of its own after it has read the payload exits 2 with `onward: not checked: <error>` on stderr and the advice to call `/pre-spec`, or to run the check and exit Plan Mode, when no Case is left open; an empty payload exits 0.
> **＋** `.claude/settings.json` registers it on `Stop`, after `uv run guppi onward`.
> **－** On the re-fire (`stop_hook_active`) it exits 0, so it fires at most once a turn.
> **－** It counts nothing, calls no model and writes no file and no mark: its judgment is the marks, the files and their times, the flag and the first word of the reply.
> **－** `uv run guppi onward` without `--plan` keeps its own judgment, the run from Retro to `/handoff`.

> **tasks:**
> - [ ] create `rule-prespec-onward` — the page of the hook
>   - type: `rule`
>   - kind: `Leaf`
>   - ref: `rule-plan-mode`
>   - purpose: `Prevents Plan Mode from stopping where no person is needed, between the reply that acknowledges the last ratification and /pre-spec, and between the ratification of the Cases built again on its findings and the exit`
>   - enforcement: `hook`
>   - implementation_ref: `[guppi/onward.py, tests/test_onward.py, .claude/settings.json]`
>   - tags: `[session, workflow, hooks, harness]`
>   - sections.Purpose:
>     ````
>     Prevents Plan Mode from stopping where no person is needed: between the reply that acknowledges the last ratification of the Frontier and `/pre-spec`, and between the ratification of the Cases built again on its findings and the exit. In Claude Code the end of a reply hands the turn to the person, and a reply that carries a `LEDGER` block ends in that text, so that the ledger hook writes it; so the agent cannot call `/pre-spec` or exit Plan Mode in that reply. This hook, `uv run guppi onward --plan` on `Stop`, sends the agent on in the same turn, as `rule-retro-onward` does after Retro (case 561.5). It judges only the state of files and of the payload — the `hi` and `prespec` marks of the session in the event log, `spec.md`, the open lines under `## Cases` of `frontier.md`, the files under `cases/` against the times of the decision lines in `ledger.md` and in the reply, the flag `stop_hook_active` and the first word `STOP:` of the reply — and counts nothing, so it fires at most once a turn and cannot loop. With no `prespec` line it sends the agent to `/pre-spec`; with the line it sends the agent to run the check and exit Plan Mode, where the hook of `rule-prespec-hook` refuses the exit while the check prints a finding. A reply that opens with `STOP:` ends, for the case where only the person can go on. An error of the hook itself after it has read the payload exits 2 with `onward: not checked: <error>` on stderr and the advice to go on, and on the re-fire it exits 0.
>     ````
> - [ ] update `rule-hook-registry` — `guppi onward --plan` registered on `Stop`
>   - old:
>     ````
>     "uv run guppi onward", "timeout": 30 } ] }
>     ````
>   - new:
>     ````
>     "uv run guppi onward", "timeout": 30 }, { "type": "command", "command": "uv run guppi onward --plan", "timeout": 30 } ] }
>     ````
>   - change: `guppi onward --plan registered on Stop after guppi onward (case 561.5)`
> - [ ] create `estimate-prespec-onward-sends-the-agent-on`
>   - ref: `rule-prespec-onward`
>   - kind: `QA`
>   - purpose: `Whether guppi onward --plan refuses the end of a reply that leaves no Case open and no Case waiting in Plan Mode, sends the agent to /pre-spec or to the check and the exit, once a turn and not on a reply that opens with STOP, and is silent otherwise`
>   - method: `uv run pytest tests/test_onward.py; by hand at the first Plan Mode after the render, the replies after the last ratification and after the ratification that follows the findings read in the transcript`
>   - tags: `[session, workflow, hooks, harness]`
> - [ ] `guppi/onward.py`: `run` with `--plan` judges the seven conditions over the session window, the stamp and the folder of `guppi/ledger.py`, the times of the files under `cases/` against the times of the decision lines of `ledger.md` and of the reply, and gives the reason of the `prespec` mark; the payload, the flag and the `STOP:` word are read by the functions the run without the flag uses; the module docstring says so
> - [ ] `guppi/cli.py`: `onward --plan` in the docstring's list of hook commands
> - [ ] `tests/test_onward.py`: a refusal with the reason for `/pre-spec`, and one with the reason for the check and the exit; silence with an open Cases line, with `spec.md`, with no `LEDGER` block, with a Case file newer than its last decision line, on `stop_hook_active`, on a reply opening with `STOP:`, and without a `hi`; a patched function that raises gives exit 2 with `onward: not checked:`; the run without `--plan` unchanged
> - [ ] `uv run guppi render`: `.claude/settings.json`
> - [ ] read `estimate-prespec-onward-sends-the-agent-on` — in a later session

> **ratification:**
> ```
> - decision[case 561.5][create][rule-prespec-onward]{ref:rule-plan-mode}{tags:session,workflow,hooks,harness}
> - decision[case 561.5][update][rule-hook-registry]{ref:rule-hook-registry}
> - decision[case 561.5][create][estimate-prespec-onward-sends-the-agent-on]{ref:rule-prespec-onward}{tags:session,workflow,hooks,harness}
> ```

### Case 561.6 — The Frontier after a closed line asks nothing when no Case is left

> **given:**
> `estimate-case-protocol-shows-the-frontier-after-a-closed-line` — the promise of the Frontier after a closed line, whose Criterion this sub-case replaces whole
> **＋** `rule-case-protocol` — the schema rendered into `vault/wiki/case-schema.md`, whose paragraph on the Frontier changes
> **＋** `raw/<date>/<hi HHMM>/frontier.md` — the Frontier of the session
> **＋** `/pre-spec` — the skill the reply calls when no Case is left
> **＋** `rule-skill-hi` — the rule of `/hi`, whose first reply keeps its own form
> **＋** `estimate-case-protocol-acknowledging-reply` — the form of the Frontier in the acknowledging reply
> **＋** `rule-prespec-onward` — the hook that sends the agent on after a reply with a `LEDGER` block

> **when:**
> After the first reply of `/hi` and before the end of Plan Mode, the agent closes a line of `raw/<date>/<hi HHMM>/frontier.md` in a reply that carries no ratification and no defer. Examples are an `A` line closed by the person's answer, a `W` line closed by a reading, a `C` line that needs no decision, or an item closed `[-] … · sprint · defer` or `[-] … · backlog · kept`.

> **then:**
> The reply ends with the heading `## Frontier` and the lines of `raw/<date>/<hi HHMM>/frontier.md` as a checklist, in the form that `estimate-case-protocol-acknowledging-reply` sets. The closed lines are folded into one, the open ones stand one per line with a short title, and the lines put off stand as they are closed.
> **＋** While a line under `## Cases` of `raw/<date>/<hi HHMM>/frontier.md` is open, a question follows the Frontier and ends the reply: which open item is next.
> **＋** When no line under `## Cases` is open, no question follows the Frontier: a reply with no `LEDGER` block calls `/pre-spec` after it, and a reply with a `LEDGER` block ends with the Frontier, for the hook of `rule-prespec-onward` to send the agent on.
> **＋** A reply that closes several lines shows one Frontier, after its `LEDGER` block when it carries one.
> **－** The first reply of `/hi` keeps the form that `rule-skill-hi` sets, the lines it closes included.
> **－** A line closed in Work Mode or at Retro shows no Frontier.
> **－** The reply that acknowledges a ratification and the reply that carries a defer keep their own form, as `estimate-case-protocol-acknowledging-reply` sets it.

> **tasks:**
> - [ ] update `rule-case-protocol` — the Frontier after a closed line asks nothing when no Case is left
>   - old:
>     ````
>     and, last, the question which open item is next or, when no line under `## Cases` is open, whether to run `/pre-spec`; a reply that closes several lines shows one Frontier;
>     ````
>   - new:
>     ````
>     and, last, the question which open item is next; when no line under `## Cases` is open, it asks nothing: a reply with no `LEDGER` block calls `/pre-spec` after the Frontier, and a reply with a `LEDGER` block ends with the Frontier, for the hook of `rule-prespec-onward` to send the agent on (case 561.6); a reply that closes several lines shows one Frontier;
>     ````
>   - change: `the Frontier after a closed line asks nothing when no line under Cases is open (case 561.6)`
> - [ ] update `estimate-case-protocol-shows-the-frontier-after-a-closed-line`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole - no question when no line under Cases is open; the reply calls /pre-spec or ends for the hook (case 561.6)`
> - [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
> - [ ] read `estimate-case-protocol-shows-the-frontier-after-a-closed-line` — in a later session

> **ratification:**
> ```
> - decision[case 561.6][update][rule-case-protocol]{ref:rule-case-protocol}
> - decision[case 561.6][update][estimate-case-protocol-shows-the-frontier-after-a-closed-line]{ref:rule-case-protocol}
> ```

### Case 561.7 — The defer reply asks nothing when no Case is left

> **given:**
> `estimate-case-protocol-defers-in-one-reply` — the promise of the defer reply, whose Criterion this sub-case replaces whole
> **＋** `rule-case-protocol` — the schema rendered into `vault/wiki/case-schema.md`, whose paragraph on the short form changes
> **＋** `raw/<date>/<hi HHMM>/frontier.md` — the Frontier of the session
> **＋** `rule-spec-write` — the `Stop` hook that writes the short form into the plan file
> **＋** `rule-prespec-onward` — the hook that sends the agent on after the reply
> **＋** `raw/<date>/<hi HHMM>/handoff.md` — the report of the session, where Retro leaves what it would put off

> **when:**
> The person asks in the chat to defer an item in Plan Mode.

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

> **tasks:**
> - [ ] update `rule-case-protocol` — the defer reply asks nothing when no Case is left
>   - old:
>     ````
>     and, last, a question — which open item is next or, when no line under `## Cases` is open, whether to run `/pre-spec` — with no text after it;
>     ````
>   - new:
>     ````
>     and, last, the question which open item is next, with no text after it — or, when no line under `## Cases` is open, no question: the reply ends with the Frontier, and the hook of `rule-prespec-onward` sends the agent on to `/pre-spec` (case 561.7);
>     ````
>   - change: `the defer reply asks nothing when no line under Cases is open (case 561.7)`
> - [ ] update `estimate-case-protocol-defers-in-one-reply`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole - no question when no line under Cases is open; the reply ends with the Frontier (case 561.7)`
> - [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
> - [ ] read `estimate-case-protocol-defers-in-one-reply` — in a later session

> **ratification:**
> ```
> - decision[case 561.7][update][rule-case-protocol]{ref:rule-case-protocol}
> - decision[case 561.7][update][estimate-case-protocol-defers-in-one-reply]{ref:rule-case-protocol}
> ```

### Case 561.8 — The acknowledging reply asks nothing when no Case is left

> **given:**
> `estimate-case-protocol-acknowledging-reply` — the promise of the acknowledging reply, whose Criterion this sub-case replaces whole
> **＋** `rule-case-protocol` — the schema rendered into `vault/wiki/case-schema.md`, whose paragraph on the acknowledging reply changes
> **＋** `raw/<date>/<hi HHMM>/frontier.md` — the Frontier of the session
> **＋** `rule-ledger-write` — the ledger hook, which writes the `LEDGER` block of the reply
> **＋** `rule-prespec-onward` — the hook that sends the agent on after the reply

> **when:**
> The person ratifies a Case, or ratifies again a Case shown again after its ratification, and the agent writes the reply that acknowledges it.

> **then:**
> The reply has four parts, in this order. First, the `LEDGER` block. Second, the heading `## Case N — ratified` and a paragraph `Changes:` that says what changes, in one or two sentences. Third, a paragraph `Notes:` with facts that did not enter the Case, left out when there are none. Last, the heading `## Frontier` and the lines of `raw/<date>/<hi HHMM>/frontier.md` as a checklist. In the checklist the closed lines are folded into one, the open ones stand one per line with a short title, and the lines put off stand as `[-] … · sprint · defer`, `[-] … · backlog · kept` or `[-] … · defer case N`.
> **＋** While a line under `## Cases` is open, the question which item is next ends the reply; when none is open, the reply ends with the Frontier and asks nothing, and the hook of `rule-prespec-onward` sends the agent on.
> **＋** For a Case with sub-cases, one reply acknowledges every sub-case ratified: one `LEDGER` block with all their lines, one heading `## Case N — ratified` that names the ids, one Frontier.
> **＋** The reply that acknowledges a re-ratification carries the `LEDGER` block with the decision lines of each Case ratified again, as at its first ratification.
> **＋** The headings and labels are in the language of the chat.
> **＋** No tool call follows the `LEDGER` block in the same reply.
> **－** The ledger hook of `rule-ledger-write` does not append a repeated decision line a second time.
> **－** When a `Stop` hook other than the ledger hook of `rule-ledger-write` refuses the reply with exit 2, the agent's answer to the refusal is a reply of its own and may call tools. The `LEDGER` block stands written.

> **tasks:**
> - [ ] update `rule-case-protocol` — the acknowledging reply asks nothing when no Case is left
>   - old:
>     ````
>     — and the question which item is next, last.
>     ````
>   - new:
>     ````
>     — and, last, the question which item is next, or, when no line under `## Cases` is open, no question: the reply ends with the Frontier, and the hook of `rule-prespec-onward` sends the agent on (case 561.8).
>     ````
>   - change: `the acknowledging reply asks nothing when no line under Cases is open (case 561.8)`
> - [ ] update `estimate-case-protocol-acknowledging-reply`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole - the question which item is next only while a line under Cases is open (case 561.8)`
> - [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
> - [ ] read `estimate-case-protocol-acknowledging-reply` — in a later session

> **ratification:**
> ```
> - decision[case 561.8][update][rule-case-protocol]{ref:rule-case-protocol}
> - decision[case 561.8][update][estimate-case-protocol-acknowledging-reply]{ref:rule-case-protocol}
> ```

### Case 561.9 — The reply before ratification shows one list and what done means

> **recommend:**
> - **Change**
>   Asked: in the first round of Case 562, on the failed reading of `estimate-case-protocol-shows-the-built-case` and its defer by case 560, the person agreed that this sub-case retires that defer, since it already replaces the Estimate's Criterion whole.
>   Taken: the decision line of this sub-case on `estimate-case-protocol-shows-the-built-case` carries `{supersedes:case 560}`. The Criterion is not changed by this: it already carries the line that the main agent writes no context of its own before the first question of a round.
> - **Change**
>   Asked: Case 562 adds a `Stop` check that refuses a reply showing a round unless it opens with the round. Its `case-guppi` found that the schema's sentence on a refused reply, and its line in this Criterion, would then be false for a round, which has no Case file and no ledger lines. The person agreed that this sub-case fixes it.
>   Taken: the sentence in `rule-case-protocol` and its line in the Criterion are narrowed to a reply that shows a Case. A new part of the same line says that a refused reply showing a round is followed, before the person answers, by a reply that shows the round again with nothing before its `**Context:**` paragraph or its first question.

> **given:**
> `estimate-case-protocol-shows-the-built-case` — the promise of the building and the showing of a Case, whose Criterion this sub-case replaces whole and whose defer of case 560 it retires
> **＋** `rule-case-protocol` — the schema rendered into `vault/wiki/case-schema.md`, whose paragraphs on the showing change
> **＋** `rule-case-build` — `case-guppi`, which builds each Case
> **＋** `rule-case-check` — the hook that writes the file of a built Case and checks its showing
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md` — the file of a built Case
> **＋** `.claude/skills/wait-what/SKILL.md` — the plain explanation the main agent gives itself
> **＋** `.claude/skills/grill-me/SKILL.md` — the question shape of a round

> **when:**
> The main agent takes up a Frontier item, the person answers a round of questions, answers a shown Case with a question or a change, or asks for a plain explanation of the agent's text — by `/wait-what` on `UserPromptSubmit` or in words — or a ratified Case changes and is shown again, in Plan Mode or in Work Mode.

> **then:**
> The main agent dispatches `case-guppi` with the Case id, the Frontier item and its source, and the person's words on it, in the prompt of the call, after the plan file stands with its title line; nothing of the Case stands in the chat before the answer.
> **＋** The person's answers to a round go to the same `case-guppi` by `SendMessage`, verbatim and untranslated, and so does a question or a change of the person on a shown Case that is not a request for a plain explanation.
> **＋** A request for a plain explanation of a round, of the short text on a Case or of a reply the main agent answers itself by `.claude/skills/wait-what/SKILL.md`; it sends the `case-guppi` of the Case a `SendMessage` only to ask for a fact of the Case, and `case-guppi` answers with the fact alone, under a first line `**Fact:**` and with no Case heading.
> **＋** An answer with no Case heading and no first line `**Fact:**` is a round of questions: the main agent shows it in the chat translated into Russian line by line, slugs, paths and quotations unchanged, each quotation in its blockquote — the `**Context:**` paragraph that opens the first round on an item translated in place before the first question, each question in the order and with the number of the answer, opening with its `❓ **Qn** - **<title>**:` line of `.claude/skills/grill-me/SKILL.md` and closing with its `➡️` line, its title, body and recommended answer translated in place, nothing merged, dropped or added between the questions, the agent's own text after the last question and one horizontal rule; no Case is shown, no file is sent, and no step of confirmation follows the last round.
> **＋** The main agent shows the Case of an answer at every showing by `SendUserFile` with `display: render` on `raw/<date>/<hi HHMM>/cases/case-<N>.md`, the file the hook of `rule-case-check` wrote from the answer. In the same reply it writes the heading of the top-level Case with its name in Russian and, under it, one list with an item per Case and sub-case of the answer: its id, its name in Russian, and a short text in Russian on what done means and how it is checked, taken from the Estimate the Case creates or whose Criterion it replaces, or from the Estimate its `context` names as already checking the change. Then it writes one `ratification` with the ledger lines of every Case of the list as the answer holds them, and its own text after one horizontal rule. An answer in which a Case gives no such Estimate goes back to its `case-guppi` by `SendMessage` before the Case is shown.
> **＋** A reply that shows a Case and that the `Stop` check of `rule-case-check` refuses is followed, before the person answers, by a reply that sends the file and shows the `ratification` as the answer holds it; a reply that shows a round and that the `Stop` check of `rule-case-check` refuses is followed, before the person answers, by a reply that shows the round again with nothing before its `**Context:**` paragraph or its first question.
> **＋** A ratified Case that changes — in its prose or in its body — changes through its `case-guppi`, and its new answer is sent and ratified again; the main agent edits no Case in the plan file.
> **＋** An item that needs no decision the main agent closes alone, with no dispatch; it dispatches `ask-guppi` once, at pre-spec, and not before a showing.
> **－** The main agent writes no context of its own before the first question of a round.
> **－** The main agent writes no `given`, `when`, `then` or `tasks` of a built Case into the chat.
> **－** A deferred decision in the short form is written by the main agent in English in the chat, with no dispatch and no file.

> **tasks:**
> - [ ] update `rule-case-protocol` — the showing is one list with what done means and one `ratification`; a refused round is shown again
>   - old:
>     ````
>     in the chat the same heading, the name in {{chat_lang}}, over the short text of the Case (case 452.4); a sub-case under `### Case N.M — name` beneath its parent (case 368).
>     ````
>   - new:
>     ````
>     in the chat the heading of the top-level Case, the name in {{chat_lang}}, over the list of its Cases (cases 452.4, 561.9); in the file and in the Spec a sub-case under `### Case N.M — name` beneath its parent (case 368).
>     ````
>   - old:
>     ````
>     for the short text on each Case and sub-case that goes with the file, the name in its heading,
>     ````
>   - new:
>     ````
>     for the name and the short text of each Case and sub-case in the list that goes with the file,
>     ````
>   - old:
>     ````
>     in the same reply, under the heading of each Case and sub-case, it writes a short text in {{chat_lang}} on what the Case changes and the `ratification` section as the answer holds it, never its `given`, `when`, `then` or `tasks`, then its own text after one horizontal rule;
>     ````
>   - new:
>     ````
>     in the same reply it writes the heading of the top-level Case, its name in {{chat_lang}}, and under it one list — an item per Case and sub-case of the answer, its id, its name in {{chat_lang}} and a short text in {{chat_lang}} on what done means and how it is checked, taken from the Estimate the Case creates or whose Criterion it replaces, or from the Estimate its `context` names as already checking the change — then one `ratification` section whose fence holds the ledger lines of every Case of the list as the answer holds them, never its `given`, `when`, `then` or `tasks`, then its own text after one horizontal rule; an answer in which a Case gives no such Estimate goes back to its `case-guppi` by `SendMessage` before it is shown (case 561.9);
>     ````
>   - old:
>     ````
>     a reply that the `Stop` check of `rule-case-check` refuses is followed, before the person answers, by a reply that sends the file and shows the `ratification` as the answer holds it (case 452.4);
>     ````
>   - new:
>     ````
>     a reply that shows a Case and that the `Stop` check of `rule-case-check` refuses is followed, before the person answers, by a reply that sends the file and shows the `ratification` as the answer holds it (case 452.4); a reply that shows a round and that the `Stop` check refuses is followed, before the person answers, by a reply that shows the round again with nothing before its `**Context:**` paragraph or its first question (case 561.9);
>     ````
>   - old:
>     ````
>     and the chat a short text under each heading;
>     ````
>   - new:
>     ````
>     and the chat one list under the heading of the parent, as `Who builds a Case` sets it;
>     ````
>   - change: `the showing is one list under the heading of the top-level Case, what done means on each item, and one ratification; a refused reply that shows a round is followed by the round shown again with nothing before it (case 561.9)`
> - [ ] update `estimate-case-protocol-shows-the-built-case`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole - the showing is one list with what done means and one ratification; a Case with no such Estimate goes back to its case-guppi; a refused round is shown again with nothing before it; the defer of case 560 retired (case 561.9)`
> - [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
> - [ ] read `estimate-case-protocol-shows-the-built-case` — in a later session

> **ratification:**
> ```
> - decision[case 561.9][update][rule-case-protocol]{ref:rule-case-protocol}
> - decision[case 561.9][update][estimate-case-protocol-shows-the-built-case]{ref:rule-case-protocol}{supersedes:case 560}
> ```

### Case 561.10 — The Case check and the Spec hook read the list

> **given:**
> `rule-case-check` — the rule of the check of a shown Case
> **＋** `guppi/casecheck.py` — the reading of a showing and the comparison with the store
> **＋** `guppi/ratified.py` — the Spec hook, which imports that reading and that comparison
> **＋** `tests/test_casecheck.py` — the tests of the check on `Stop`
> **＋** `tests/test_ratified.py` — the tests of the Spec hook
> **＋** `estimate-case-check-shows-only-the-checked-case` — the promise of the comparison, whose Criterion this sub-case replaces whole
> **＋** `rule-spec-write` — the rule of the Spec hook, whose promise reads a showing through the imported comparison
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md` — the file of a built Case whose sending is checked

> **when:**
> `Stop` fires after a reply of the main agent that shows a Case under `## Case N —` or `### Case N.M —` with at least one of its sections.

> **then:**
> `uv run guppi casecheck` compares each such Case with the Case of the same id in `<plan>.checked.json` in each of its `given`, `when`, `then`, `tasks` and `ratification` that the reply shows, line by line once line ends and trailing spaces are the same.
> **＋** Under the heading of a top-level Case, one `ratification` whose fence holds the ledger lines of its sub-cases, as the list of a showing holds them, is read as the showing of each sub-case whose id a line names: the lines that name that id are compared with the `ratification` of that sub-case in the store, and a stored line that is missing or a line the store lacks is a difference.
> **＋** A section the reply does not show is not compared: a showing of the heading, a short text and `ratification` alone passes when its `ratification` equals the answer.
> **＋** The name of its heading, its `context`, `problem` and `recommend`, and text under the heading outside its sections are not compared.
> **＋** A Case the store does not hold, a Case that differs in a compared section, a Case stored with findings, or a Case with no `SendUserFile` call on `raw/<date>/<hi HHMM>/cases/case-<N>.md` in the turn of the reply, N the id of its top-level Case, exits 2, the reason and the findings on stderr.
> **＋** A parent shown with its sub-cases is compared part by part, as the store holds each.
> **＋** The Spec hook `guppi/ratified.py` judges a showing by the same comparison, and a sending by the same reading of the transcript, both imported from `guppi/casecheck.py`.
> **－** A heading with no section, as in the acknowledging reply, a fence tagged `DIFF`, and a deferred decision in the short form — `context`, `problem` and a fence tagged `then` with `defer` items, no `given` and no `when` — are not compared and need no sending.
> **－** On the re-fire (`stop_hook_active`) it exits 0.

> **tasks:**
> - [ ] update `rule-case-check` — the check reads the list of a showing
>   - old:
>     ````
>     a parent shown with its sub-cases is compared part by part.
>     ````
>   - new:
>     ````
>     a parent shown with its sub-cases is compared part by part. Under the heading of a top-level Case, one `ratification` whose fence holds the ledger lines of its sub-cases — the list of the showing that `rule-case-protocol` sets — is read as the showing of each sub-case whose id a line names: the lines that name that id are compared with the `ratification` of that sub-case in the store, and a stored line that is missing or a line the store lacks is a difference; the Spec hook reads a showing the same way, by the same function (case 561.10).
>     ````
>   - change: `the Stop check reads one ratification under the heading of a top-level Case as the showing of each sub-case it names (case 561.10)`
> - [ ] update `estimate-case-check-shows-only-the-checked-case`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole - one ratification under the heading of a top-level Case is the showing of each sub-case its lines name (case 561.10)`
> - [ ] `guppi/casecheck.py`: the reading of a showing takes one `ratification` under the heading of a top-level Case as the showing of each sub-case whose id its lines name, and the comparison compares those lines with the stored `ratification` of each; a showing under each Case's own heading reads as before; the module docstring says so
> - [ ] `guppi/ratified.py`: `find_showing` finds a sub-case in such a showing through the reading of `guppi/casecheck.py`
> - [ ] `tests/test_casecheck.py`: a list showing whose fence holds exactly the stored lines of two sub-cases passes; a missing line and an extra line each exit 2; a showing under each sub-case's own heading passes as before
> - [ ] `tests/test_ratified.py`: a sub-case shown only in the fence of its parent's list is found and compared, and a difference refuses the write
> - [ ] read `estimate-case-check-shows-only-the-checked-case` — in a later session

> **ratification:**
> ```
> - decision[case 561.10][update][rule-case-check]{ref:rule-case-check}
> - decision[case 561.10][update][estimate-case-check-shows-only-the-checked-case]{ref:rule-case-check}
> ```

### Case 561.11 — Every Case says what done means

> **given:**
> `rule-case-build` — the rule of `case-guppi`, rendered into `.claude/agents/case-guppi.md`, whose list of forks gains the answer on what done means
> **＋** `estimate-case-build-answers-what-done-means` — the promise this sub-case creates
> **＋** `estimate-case-build-writes-the-case` — the promise of the build, which names the promise among the forks and stands
> **＋** `rule-case-protocol` — the schema, whose `context` already says why an Estimate of the rule is not touched

> **when:**
> `case-guppi` answers with a Case, following `.claude/agents/case-guppi.md` as rendered from `rule-case-build`.

> **then:**
> Each Case and sub-case of the answer creates an Estimate or replaces the Criterion of one, or its `context`, or its parent's, names by slug the Estimate that already checks the change and says why its Criterion stands.
> **＋** When the person's words and the frame give neither, `case-guppi` asks in a round, before it answers with the Case, what the Estimate will check, and the `recommend` of the Case holds that question.
> **－** A deferred decision in the short form is no answer of `case-guppi` and carries no such Estimate.

> **tasks:**
> - [ ] update `rule-case-build` — each Case answers what done means
>   - old:
>     ````
>     and what is left not done. While a fork is open,
>     ````
>   - new:
>     ````
>     and what is left not done. Each Case and sub-case answers what done means and how it is checked: it creates an Estimate or replaces the Criterion of one, or its `context` names the Estimate that already checks the change and says why its Criterion stands; a Case that can give neither has the promise open, and you ask in a round what its Estimate will check (case 561.11). While a fork is open,
>     ````
>   - change: `each Case creates or replaces an Estimate or names the one that already checks the change; with neither, the promise is a fork (case 561.11)`
> - [ ] create `estimate-case-build-answers-what-done-means`
>   - ref: `rule-case-build`
>   - kind: `QA`
>   - purpose: `Whether each Case case-guppi builds creates or replaces an Estimate or names the one that already checks the change, and asks in a round when it can do neither`
>   - method: `by hand at the close of a later session, each Case of the plan and the rounds before it read in the transcript`
>   - tags: `[session, workflow]`
> - [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
> - [ ] read `estimate-case-build-answers-what-done-means` — in a later session

> **ratification:**
> ```
> - decision[case 561.11][update][rule-case-build]{ref:rule-case-build}
> - decision[case 561.11][create][estimate-case-build-answers-what-done-means]{ref:rule-case-build}{tags:session,workflow}
> ```

### Case 561.12 — A question to discuss an item goes to its case-guppi

> **recommend:**
> - **How is a plain discussion question answered?**
>   Recommended: (a) forward it to the item's `case-guppi`, which answers in plain words under `**Fact:**`; the main agent reads nothing itself, and the open round stays open.
>   Answer: (a).

> **given:**
> `rule-case-protocol` — the schema rendered into `vault/wiki/case-schema.md`, whose paragraph on who builds a Case gains the forwarding
> **＋** `rule-case-build` — the rule of `case-guppi`, rendered into `.claude/agents/case-guppi.md`, whose answer under `**Fact:**` covers the question
> **＋** `estimate-case-protocol-forwards-a-discussion-question` — the promise this sub-case creates
> **＋** `.claude/skills/wait-what/SKILL.md` — the plain explanation, which stays with the main agent
> **＋** `rule-case-check` — the hook on the answers of `case-guppi`, which reads no `**Fact:**` answer as a Case

> **when:**
> In Plan Mode or in Work Mode, the person asks in the chat to discuss an item whose `case-guppi` is building its Case or has shown it, or to learn something of that item, and the question is no request for a plain explanation of the agent's text.

> **then:**
> The main agent sends the question to that `case-guppi` by `SendMessage`, verbatim and untranslated, and makes no `Read`, `Grep` or `Glob` call of its own to answer it.
> **＋** `case-guppi` answers in plain words under a first line `**Fact:**`, with no Case heading and no round, from the pages it read, or with a round when the question opens a fork.
> **＋** The main agent shows the answer translated into Russian, then asks again the question that stood open: the open question of the round, or the sign-off of the shown Case.
> **－** A request for a plain explanation of a round, of the short text on a Case or of a reply stays with `.claude/skills/wait-what/SKILL.md`.
> **－** A `**Fact:**` answer changes nothing of the round or of the Case, and the hook of `rule-case-check` reads it as no Case.

> **tasks:**
> - [ ] update `rule-case-protocol` — a question to discuss an item goes to its `case-guppi`
>   - old:
>     ````
>     `case-guppi` answers with the fact alone, under a first line `**Fact:**` and with no Case heading (case 477.3).
>     ````
>   - new:
>     ````
>     `case-guppi` answers with the fact alone, under a first line `**Fact:**` and with no Case heading (case 477.3). A question of the person that asks to discuss an item, or to learn something of it, while its `case-guppi` builds its Case or after it showed it, the main agent does not answer from its own reading: it sends the question to that `case-guppi` by `SendMessage`, verbatim and untranslated, and `case-guppi` answers in plain words under a first line `**Fact:**`, or with a round when the question opens a fork; the main agent shows that answer translated into {{chat_lang}} and asks again the question that stood open (case 561.12).
>     ````
>   - change: `a question to discuss an item goes to its case-guppi and comes back under Fact (case 561.12)`
> - [ ] update `rule-case-build` — `case-guppi` answers a question to discuss the item under `**Fact:**`
>   - old:
>     ````
>     A message that asks you for a fact of the Case, so that the main agent can explain the Case to the person in plain words, you answer with the fact alone, in plain words, under a first line `**Fact:**`, with no Case heading and no round (case 477.3).
>     ````
>   - new:
>     ````
>     A message that asks you for a fact of the Case, so that the main agent can explain the Case to the person in plain words, you answer with the fact alone, in plain words, under a first line `**Fact:**`, with no Case heading and no round (case 477.3). A message that carries the person's question to discuss the item, or to learn something of it, you answer the same way, from the pages you read, and you change nothing of the round or of the Case; where the question opens a fork, you answer with a round instead (case 561.12).
>     ````
>   - change: `case-guppi answers a question to discuss the item under Fact, or with a round when it opens a fork (case 561.12)`
> - [ ] create `estimate-case-protocol-forwards-a-discussion-question`
>   - ref: `rule-case-protocol`
>   - kind: `QA`
>   - purpose: `Whether a question of the person to discuss an item goes to its case-guppi and comes back under Fact, with no reading of the main agent's own`
>   - method: `by hand in a later session, the first such question, the SendMessage call, the tool calls of the main agent and the answer read in the transcript`
>   - tags: `[session, workflow]`
> - [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
> - [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
> - [ ] read `estimate-case-protocol-forwards-a-discussion-question` — in a later session

> **ratification:**
> ```
> - decision[case 561.12][update][rule-case-protocol]{ref:rule-case-protocol}
> - decision[case 561.12][update][rule-case-build]{ref:rule-case-build}
> - decision[case 561.12][create][estimate-case-protocol-forwards-a-discussion-question]{ref:rule-case-protocol}{tags:session,workflow}
> ```

### Case 561.13 — The main agent's own questions take the grill-me shape

> **recommend:**
> - **Change**
>   Asked: the pre-spec report asked whether the question of an open `A` line at `/hi` — the Estimate by slug and its question — takes the grill-me shape too. The person agreed with the recommendation (a) that it keeps its own form.
>   Taken: that question joins the exceptions, in the `－` line of `then` and in the text of the `rule-case-protocol` pair.

> **given:**
> `rule-case-protocol` — the schema rendered into `vault/wiki/case-schema.md`, whose paragraph on who builds a Case gains the shape
> **＋** `estimate-case-protocol-asks-in-the-grill-me-shape` — the promise this sub-case creates
> **＋** `.claude/skills/grill-me/SKILL.md` — the question shape
> **＋** `/pre-spec` — the skill whose report holds the main agent's decisions
> **＋** `rule-skill-hi` — the rule of `/hi`, where the main agent asks the person too, and which sets the question of an open `A` line
> **＋** `rule-where-to-stop` — the conditions of a stop of Work Mode, where the main agent asks the person
> **＋** `rule-spec-capture` — the choice between `/work` and `/carry`, which keeps its picker
> **＋** `rule-orchestration` — the placeholder whose `purpose` records the move to three files and whose defer of case 546 this sub-case retires

> **when:**
> The main agent puts a question to the person itself, outside a round of `case-guppi`: a decision it needs in the report of `/pre-spec`, a question at `/hi`, or a question at a stop of Work Mode.

> **then:**
> Each such question takes the question shape of `.claude/skills/grill-me/SKILL.md`: its numbered `❓ **Qn** - **<title>**:` line, one `**Now:**` line, the label `**Options:**`, each option on a `🔹` line with one `**After:**` item, and the `➡️` line with the recommended answer.
> **＋** It stands in Russian, and its labels may stand translated.
> **－** The question which Frontier item is next, the question of an open `A` line at `/hi` — the Estimate by slug and its question —, the question that asks for the sign-off of a shown Case, and the choice between `/work` and `/carry` of `rule-spec-capture` keep their own form.

> **tasks:**
> - [ ] update `rule-case-protocol` — the main agent's own questions take the grill-me shape
>   - old:
>     ````
>     A deferred decision in the short form is the agent's own, written with no dispatch (case 419.1).
>     ````
>   - new:
>     ````
>     A deferred decision in the short form is the agent's own, written with no dispatch (case 419.1). A question the main agent puts to the person itself — a decision it needs in the report of `/pre-spec`, a question at `/hi`, a question at a stop of Work Mode — takes the question shape of `.claude/skills/grill-me/SKILL.md`: its numbered title line, the `**Now:**` line, the options under `**Options:**`, each with its `**After:**` item, and the recommended answer on the `➡️` line, in {{chat_lang}}, the labels translated or not; the question which Frontier item is next, the question of an open `A` line at `/hi` — the Estimate by slug and its question, which asks for a reading and not a choice —, the question that asks for the sign-off of a shown Case, and the choice between `/work` and `/carry` keep their own form (case 561.13).
>     ````
>   - change: `the main agent's own questions take the grill-me shape, but for the question of the next item, of an open A line, of a sign-off and of work or carry (case 561.13, supersedes the defer of case 546)`
> - [ ] update `rule-orchestration` — the purpose records the design ratified for a later session; the defer of case 546 retired
>   - set: `{purpose: "Prevents the main agent from loading the form of a Case it does not build, a design ratified in case 561 for a later session - a file of rule-orchestration that /hi loads in place of case-schema.md, holding what the main agent alone does; a third small file of its own rule, loaded by /hi and read by case-guppi, holding the one rule, the form of the ledger lines, atomicity and the harness; case-schema.md holding the form of a Case, read by case-guppi alone; the checks of the behaviours that move made new Estimates of the new rules, the old ones withdrawn"}`
>   - sections.Purpose:
>     ````
>     Prevents the main agent from loading the form of a Case it does not build. Case 561 ratified the design and left it for a later session. A file of this rule, which `/hi` loads in place of `case-schema.md`, holds what the main agent alone does: the triage of a Frontier item, the dispatch of `case-guppi`, the showing, the acknowledging reply, the Frontier, the defers and the loop after the findings of `/pre-spec`. A third small file of its own rule, loaded by `/hi` and read by `case-guppi`, holds what both agents need: the one rule, the form of the ledger lines, atomicity and the harness. `case-schema.md` keeps the form of a Case and is read by `case-guppi` alone. The checks of the behaviours that move become new Estimates of the new rules, and the old ones on `rule-case-protocol` are withdrawn. The question shape of the main agent's own questions, which case 546 put off here, was decided by case 561.13 in `case-schema.md`, where it moves with the rest.
>     ````
>   - change: `the purpose records the three-file design ratified in case 561; the defer of case 546 retired by case 561.13`
> - [ ] create `estimate-case-protocol-asks-in-the-grill-me-shape`
>   - ref: `rule-case-protocol`
>   - kind: `QA`
>   - purpose: `Whether each question the main agent puts to the person itself, at pre-spec, at /hi or at a stop of Work Mode, takes the question shape of grill-me, the exceptions kept in their own form`
>   - method: `by hand at the close of a later session, each question of the main agent's own read in the transcript`
>   - tags: `[session, workflow]`
> - [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
> - [ ] read `estimate-case-protocol-asks-in-the-grill-me-shape` — in a later session

> **ratification:**
> ```
> - decision[case 561.13][update][rule-case-protocol]{ref:rule-case-protocol}
> - decision[case 561.13][update][rule-orchestration]{ref:rule-orchestration}{supersedes:case 546}
> - decision[case 561.13][create][estimate-case-protocol-asks-in-the-grill-me-shape]{ref:rule-case-protocol}{tags:session,workflow}
> ```

### Case 561.14 — The harness comes before the Plan Mode instructions of Claude Code

> **recommend:**
> - **Which instructions win in Plan Mode?**
>   Recommended: (a) the harness wins, and it is written down: no search agents in place of `case-guppi` and `ask-guppi`, a plain question except where a rule names a picker, and the exit from Plan Mode only after the check.
>   Answer: (a).

> **given:**
> `rule-case-protocol` — the schema rendered into `vault/wiki/case-schema.md`, whose paragraph on Plan Mode gains the order of the two instructions
> **＋** `estimate-case-protocol-puts-the-harness-before-plan-mode` — the promise this sub-case creates
> **＋** `rule-spec-capture` — the choice between `/work` and `/carry`, asked by a picker after the Spec is written
> **＋** `rule-skill-hi` — the rule of `/hi`, which opens a working session in Plan Mode
> **＋** `/pre-spec` — the skill after which the main agent exits Plan Mode
> **＋** `rule-prespec-hook` — the hook that refuses the exit before a clean check

> **when:**
> A working session opened by `/hi` runs in Plan Mode, and the Plan Mode instructions of Claude Code stand in the main agent's context.

> **then:**
> The main agent launches no Explore or Plan agent: `case-guppi` builds each Case, and `ask-guppi` asks the vault at `/pre-spec`.
> **＋** It asks the person by a plain question in the chat and calls no picker tool while Plan Mode lasts.
> **＋** It calls `ExitPlanMode` only after `/pre-spec` has run.
> **－** The choice between `/work` and `/carry` after the Spec is written stays a picker, as `rule-spec-capture` sets it.

> **tasks:**
> - [ ] update `rule-case-protocol` — the harness comes before the Plan Mode instructions of Claude Code
>   - old:
>     ````
>     That is the form of Plan Mode.
>     ````
>   - new:
>     ````
>     That is the form of Plan Mode. In a working session the rules the harness loads come before the Plan Mode instructions of Claude Code: the main agent launches no Explore or Plan agent — `case-guppi` builds each Case and `ask-guppi` asks the vault at `/pre-spec` —, asks the person by a plain question in the chat, never by a picker tool, except where a rule names one, such as the choice between `/work` and `/carry` after the Spec is written, and calls `ExitPlanMode` only after `/pre-spec` (case 561.14).
>     ````
>   - change: `the harness comes before the Plan Mode instructions of Claude Code (case 561.14)`
> - [ ] create `estimate-case-protocol-puts-the-harness-before-plan-mode`
>   - ref: `rule-case-protocol`
>   - kind: `QA`
>   - purpose: `Whether in a working session the main agent launches no Explore or Plan agent, asks by plain questions and no picker in Plan Mode, and exits Plan Mode only after pre-spec`
>   - method: `by hand at the close of a later session, the Agent calls, the picker calls and the ExitPlanMode call of Plan Mode read in the transcript`
>   - tags: `[session, workflow]`
> - [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
> - [ ] read `estimate-case-protocol-puts-the-harness-before-plan-mode` — in a later session

> **ratification:**
> ```
> - decision[case 561.14][update][rule-case-protocol]{ref:rule-case-protocol}
> - decision[case 561.14][create][estimate-case-protocol-puts-the-harness-before-plan-mode]{ref:rule-case-protocol}{tags:session,workflow}
> ```
