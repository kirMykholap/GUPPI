## Case 806 — In Work Mode a new Case replaces the sub-case of a ratified Case

> **context:**
> When the work of Work Mode meets a choice that a ratified Case of the approved Spec did not make, the rules today let the main agent send that Case back to its `case-guppi`, which builds it again under its own number; the person ratifies it again, and the `Stop` hook of `rule-spec-write` replaces its sections in `spec.md` in place, by `place` of `guppi/ratified.py`. In session 1753 this happened to Case 804: the `stop:` task of 804.7 failed when GitHub refused the GitHub Actions app on the bypass list of the ruleset `prod` (HTTP 422), and Case 804 was built again around a deploy key and ratified again after the Spec was approved (handoff of 1753, line 38; ledger of 1753, line 121). The person called this a bad step: a Case that `/pre-spec` checked and the person approved was changed after the fact. The person turned down moving such a choice to the next session, and chose instead that a new Case under a new number replaces only the sub-case the choice touches, and that the replaced sub-case leaves the Spec, so that only what is confirmed reaches the wiki.
>
> Most of that path works in the code today. `remove_superseded` of `guppi/ratified.py` removes from the plan and from `spec.md` the sections of the sub-case that a `{supersedes:case N.M}` on a decision line of the reply names, and the parent only once each of its sub-cases with a decision line is retired; `place` puts a Case that `spec.md` does not hold into the last approved document. The docstring of `guppi/materialize.py` reads one unit as its ledger and its own `spec.md` and nothing else, marks every entry of a retired sub-case `superseded_by`, and `guppi/generate.py` applies no such entry and gives its Decision page a two-line body naming the Decision that replaced it. The docstring of `guppi/casecheck.py` leaves out of the clash check a Case that a `{supersedes}` mark on a decision line of the answer names (case 725.2), so a new Case that changes the pages of the sub-case it replaces passes the check of its file. The decision line of the rebuilt Case 804 stands at 20:13 on line 112 of the ledger of 1753, after the Spec was approved, so the ledger hook takes a decision line in Work Mode. What is missing is the rule: `orchestration.md`, the agent file of `case-guppi` and `/work` still say that a ratified Case is built again in Work Mode, and no check of the plan runs on a Case ratified there. The docstring of `guppi/prespec.py` says that an open line under `## Work` of the Frontier is no finding, so `uv run guppi prespec --check` can run on the plan in Work Mode; no run of it on a plan in Work Mode was taken for this Case, so whether it prints nothing there on a sound plan is not known; 806.3 makes its finding a stop, so a false finding stops the run rather than passing unseen.
>
> The searches. A Grep of the pattern `in Work Mode when a ratified Case is built again` over the repository outside `vault/raw/` and `vault/archive/` printed 5 files: `vault/wiki/orchestration.md`, `.claude/agents/case-guppi.md`, `vault/wiki/rules/rule-orchestration.md`, `vault/wiki/rules/rule-case-build.md` and `vault/wiki/estimates/estimate-case-build-writes-the-case.md`; each enters the Case, the two rendered files through the render of their rule. A Grep of the pattern `(?i)built again|ratified again|shown again` over `vault/wiki/rules/*.md` and `.claude/**/*.md` printed 14 files: `.claude/skills/sprint-open/SKILL.md`, `.claude/skills/pre-spec/SKILL.md`, `.claude/agents/case-guppi.md`, `.claude/agents/ask-guppi.md`, `rule-ask`, `rule-spec-write`, `rule-spec-box`, `rule-skill-sprint-open`, `rule-prespec-onward`, `rule-prespec`, `rule-orchestration`, `rule-case-protocol`, `rule-case-check` and `rule-case-build`. Beside the files above, the hits read stand: those of `rule-prespec-onward`, `rule-prespec`, `.claude/skills/pre-spec/SKILL.md`, `rule-ask`, `.claude/agents/ask-guppi.md`, `rule-skill-sprint-open` and `.claude/skills/sprint-open/SKILL.md` speak of Cases built again in Plan Mode — in the loop after `/pre-spec`, and the opening Case of a sprint built again under another id when its id is taken; the hit of `rule-spec-box` says that a conserved Spec is not built again; the hit of `rule-spec-write` is a History line; the Splitting paragraph of `rule-case-protocol` sets a new number for a Case built again in another shape, and its sentence that a Case superseded in its own session leaves the Spec is the way the person chose; the hit of `rule-case-check` is the clash rule of case 725.2 named above. A Grep of the pattern `orchestration\.md|case-guppi\.md|skills/work/SKILL\.md` over `tests/` printed 1 file, `tests/test_orchestration.py`; it reads only the blocks tagged `showing` and `defer` of the rendered page, which no pair of this Case touches. A Grep of the pattern `where-to-stop` over `tests/` printed 2 files, `tests/test_gate.py` and `tests/test_onward.py`; both assert that a hook message names the path `vault/wiki/where-to-stop.md`, not its text, so the new first condition of 806.4 breaks neither.
>
> The first condition of `where-to-stop.md` speaks only of a choice that no ratified Case makes, and the page closes with "Nothing else is a stop", so a finding of the check on a Case ratified in Work Mode, or a text the agent finds wrong, would be no stop; at `/pre-spec` the person chose to widen that condition, and 806.4 does it with the Criterion of `estimate-where-to-stop-stops-only-on-its-conditions`. A `/work` that `/box` calls runs a conserved Spec, and `rule-spec-box` says that in its first part a Case of that Spec is not checked again or built again and that its check refuses a session that ratified a Case of its own, while the hook of `rule-spec-write` writes only into the plan file and the session's own `spec.md`; at `/pre-spec` the person chose that the route of this Case does not hold there: a fork is a stop with no new Case, and the choice goes to the handoff as a line, which 806.1 and 806.3 say and no code of `/box` changes. In Work Mode the reply that acknowledges the new Case carries a `LEDGER` block and ends in text, and the docstring of `guppi/onward.py` sends the agent on by `guppi onward --plan` only while `raw/<hi date>/<hi HHMM>/spec.md` does not stand, so in Work Mode nothing sends it on: 806.3 says that this reply ends the turn and that the run goes on at the person's next message, the check of the plan first, and its Estimate checks it; 806.1 changes to match the sentence of `## The acknowledging reply` of `rule-orchestration` that says the hook of `rule-prespec-onward` sends the agent on after `/pre-spec`, which would be false in Work Mode, and signs no line of its own on it. The removal of the replaced sub-case from the plan file and `spec.md`, with the parent and the other sub-cases kept, is already the promise of `estimate-spec-write-removes-a-superseded-case`, so no line of this Case signs it again. The sentence of `orchestration.md` that no Case is taken back in Work Mode, and the line of `estimate-orchestration-takes-back-a-ratified-case` that says the same, stand: a take-back retires a Case whole with no replacement, while this route builds a new Case that replaces a sub-case; a Case of a later session may still replace a Case the person wants gone. The Criterion of `estimate-spec-write-reaches-the-approved-spec` stands: the hook places a new Case in `spec.md` as that Criterion says. The opening sentence of `## Who builds a Case`, that every Case, a ratified Case that changed included, is built by `case-guppi`, stays true. The lesson `lesson-case-build-recommended-an-unchecked-github-fact` stays `new` for a Case of its own, by the person's answer. Case 805 of this session defers `entity-sprint-plugin` and touches no page of this Case. Each sub-case replaces the Criterion of the Estimate of its own page, every old line carried word for word, since a Case ratified in Work Mode none of whose tasks has run still changes under its own number, and the Work Mode lines added. The `method` of `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` waited for the session that closes a sprint, which the check of the file refuses for a replaced Criterion; 806.3 sets a `method` that reads the Render in the Spec at Retro, and leaves the lines that need the rendered `.claude/skills/work/SKILL.md` to the first `/work` on that file in which a Case is ratified in Work Mode, an event its `method` names. Lines of sibling sub-cases that share words are not one promise twice: those of 806.1 and 806.2 set two sides of one moment, what the main agent does and what `case-guppi` builds; the `/box` lines of 806.1 and 806.3 set what the main agent and `/work` each do there, as the person asked both to say; and the lines of 806.4 that share words with 806.3 are old lines of the two Criteria, carried word for word, on different stops and steps.

> **problem:**
> In Work Mode a ratified Case of the approved Spec is built again under its own number when the work meets a choice it did not make, so the Spec the person approved and `/pre-spec` checked is rewritten after the fact, and no check of the plan runs on the changed Case before its work.

> **recommend:**
> - **What does Work Mode do when the work meets a choice that a ratified Case did not make?**
>   - Recommended: (b) the ratified Case stands, and the choice goes to the next session.
>   - Answer: not (b); the person does not move the Case to the next session, and wants a new Case that replaces the old one, most likely only the sub-case, since replacing a whole Case for one point is too much.
> - **Does this Case also fix why the fork happened?**
>   - Recommended: (a) no, only what Work Mode does at the fork.
>   - Answer: agreed, (a).
> - **What does the new Case replace?**
>   - Recommended: (a) only the sub-case the choice touches.
>   - Answer: (a).
> - **Does the approved Spec change when a new Case replaces a sub-case?**
>   - Recommended: (b) the Spec stays as signed, and the new Case is added after it.
>   - Answer: (a), after a discussion of both ways: the Spec changes, the replaced sub-case leaves it, the hook writes the new Case into the Spec so that `materialize` takes it, and only what is confirmed reaches the wiki.
> - **Is the new Case checked before its tasks run?**
>   - Recommended: (a) the script of `/pre-spec` runs on the plan before the new tasks run.
>   - Answer: agreed, (a).
> - **Does this hold for every change to a ratified Case in Work Mode, or only for a fork the work runs into?**
>   - Recommended: (a) every route.
>   - Answer: agreed, (a).
> - **How is a finding of the check on the new Case fixed?**
>   - Recommended: (a) a Case ratified in Work Mode is fixed in place until its tasks start.
>   - Answer: agreed, (a).
> - **How is this Case checked?**
>   - Recommended: (a) each sub-case replaces the Criterion of the existing Estimate of its page.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: at pre-spec, the first condition of `where-to-stop.md` is widened: the work needs a choice no ratified Case makes, or a ratified Case turns out wrong, by a finding of the check or by a text the agent finds wrong, and a new Case is needed.
>   - Taken: 806.4 updates `rule-where-to-stop` and replaces the Criterion of `estimate-where-to-stop-stops-only-on-its-conditions`.
> - **Change**
>   - Asked: at pre-spec, the route of this Case does not hold in a `/work` that `/box` calls: there a fork is a stop with no new Case, and the choice goes to the handoff as a line; no code of `/box` changes.
>   - Taken: 806.1 and 806.3 say so in their `then` and in the text they render.

### Case 806.1 — The main agent has a new Case built for a ratified Case that changes in Work Mode

> **given:**
> `rule-orchestration`: renders what the main agent does.
> **＋** `vault/wiki/orchestration.md`: the file rendered from it.
> **＋** `estimate-orchestration-shows-the-built-case`: its Criterion is replaced whole.
> **＋** `rule-case-check`: the check of a case file and of a showing.
> **＋** `rule-spec-write`: the hook that writes a ratified Case into the plan file and the Spec and removes a superseded one.
> **＋** `rule-prespec-onward`: the hook that sends the agent on after `/pre-spec`.
> **＋** `rule-work-mode`: what `/work` runs after a Case ratified in Work Mode.
> **＋** `/wait-what` and `.claude/skills/wait-what/SKILL.md`: the plain explanation the main agent gives itself.
> **＋** `.claude/skills/grill-me/SKILL.md`: the shape of a round.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier of the session.
> **＋** `raw/<date>/<hi HHMM>/ledger.md`: the ledger of the session.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a Case, in the folder `cases/`.
> **＋** `raw/<date>/<hi HHMM>/spec.md`: the approved Spec of the session.
> **＋** `/work` and `/box`: Work Mode on the Spec of the session, and on a conserved Spec.
> **＋** `rule-spec-box`: the rule of `/box`, which builds no Case of a conserved Spec again.
> **＋** `raw/<date>/<hi HHMM>/handoff.md`: the handoff of the session.

> **when:**
> The main agent takes up a Frontier item, the person answers a round of questions, answers a shown Case with a question or a change, or asks for a plain explanation of the agent's text — by `/wait-what` on `UserPromptSubmit` or in words — or a ratified Case changes and is shown again, in Plan Mode or in Work Mode, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.
> **＋** Or the person puts off or keeps the item of a Case that `case-guppi` built and that is not ratified, or drops that Case so that the item ends another way.
> **＋** Or the person drops a change to a ratified Case that its `case-guppi` made after the Case was last ratified.
> **＋** Or, in Work Mode, a ratified Case of the approved Spec must change: the work meets a choice it did not make, the person asks for a change, or the main agent finds its text wrong or too narrow.

> **then:**
> The main agent dispatches `case-guppi` with the Case id, the Frontier item and its source, and the person's words on it, in the prompt of the call, after the plan file stands with its title line; nothing of the Case stands in the chat before the answer.
> **＋** The person's answers to a round go to the same `case-guppi` by `SendMessage`, verbatim and untranslated, and so does a question or a change of the person on a shown Case that is not a request for a plain explanation.
> **＋** A request for a plain explanation of a round, of the short text on a Case or of a reply the main agent answers itself by `.claude/skills/wait-what/SKILL.md`; it sends the `case-guppi` of the Case a `SendMessage` only to ask for a fact of the Case, and `case-guppi` answers with the fact alone, under a first line `**Fact:**` and with no Case heading.
> **＋** An answer with no first line `**Built:**`, `**Fact:**` or `**Dropped:**` is a round of questions: the main agent shows it in the chat translated into Russian line by line, slugs, paths and quotations unchanged, each quotation in its blockquote — the `**Context:**` paragraph that opens the first round on an item translated in place before the first question, its label naming its Case and its item of `raw/<date>/<hi HHMM>/frontier.md` when the round is one of a batch, each question in the order and with the number of the answer, opening with its `❓ **Qn** - **<title>**:` line of `.claude/skills/grill-me/SKILL.md` and closing with its `➡️` line, its title, body and recommended answer translated in place, nothing merged, dropped or added between the questions, the agent's own text after the last question and one horizontal rule; no Case is shown, no file is sent, and no step of confirmation follows the last round.
> **＋** The main agent shows a built Case at every showing by `SendUserFile` with `display: render` on `raw/<date>/<hi HHMM>/cases/case-<N>.md`, the file `case-guppi` wrote and the hook of `rule-case-check` checked. In the same reply it writes the heading of the top-level Case: its id, and its name in Russian translated from the `**Case:**` line of the summary `case-guppi` answered with. Under the heading it writes one list with an item per Case and sub-case of the summary: its id, its name in Russian, and a short text in Russian on what done means and how it is checked, taken from the Estimate the summary names for it. Then it writes one `ratification` with the ledger lines of every Case of the list as the summary holds them, and its own text after one horizontal rule. A summary in which a Case names no such Estimate goes back to its `case-guppi` by `SendMessage` before the Case is shown.
> **＋** A Case whose item in the summary carries a line `**Other Case:**` is shown as it stands, and the main agent asks the person whether that other Case is built again.
> **＋** A reply that shows a Case and that the `Stop` check of `rule-case-check` refuses — its file not sent, or a showing that differs from the checked text — is followed, before the person answers, by a reply that sends the file and shows the `ratification` as the summary holds it.
> **＋** A round or a Case shown with a text of the main agent's own before it or outside its list is not refused and is not shown again: `rule-case-check` tells the agent of it at the person's next message, and the agent keeps the form from the next showing on.
> **＋** A ratified Case that changes — in its prose or in its body — changes through its `case-guppi`, and its new file is sent and ratified again; the main agent edits no Case in the plan file or under `cases/`.
> **＋** In Work Mode, when a ratified Case of the approved Spec must change, the main agent dispatches `case-guppi` for a new top-level Case under the id that `uv run guppi caseid --next` prints, with the path of the file of the ratified Case, the sub-case of it that must change and the reason, shows the new Case as any built Case, and the person ratifies it.
> **＋** An item that needs no decision the main agent closes alone, with no dispatch; it dispatches `ask-guppi` only at pre-spec, one run over the whole plan at its first run, never to build a Case, and asks that run again only to confirm its own findings.
> **＋** When the person puts off or keeps the item of a Case that `case-guppi` built and that has no decision line in `raw/<date>/<hi HHMM>/ledger.md`, or drops that Case so that the item ends another way, the main agent sends the drop by `SendMessage` to the `case-guppi` of that Case, and the turn of the person's words ends with one line under the bold label `**Waiting:**`, translated, and nothing else. The agent goes on with the item only in the turn that the answer `**Dropped:**` of that `case-guppi` opens, so that the hook of `rule-prespec-onward` finds the file of the Case empty at the end of every later reply.
> **＋** The drop adds no closer: the line of the item in `raw/<date>/<hi HHMM>/frontier.md` closes by one of the closers of `vault/wiki/orchestration.md`, as fits what the person chose — `[x] … · work`, `[x] … · case N` of another Case, `[-] … · sprint · defer`, `[-] … · backlog · kept` or `[-] … · defer case N`.
> **＋** When the person drops a change to a ratified Case that its `case-guppi` made after the Case was last ratified, the main agent sends the drop to that `case-guppi` by `SendMessage`. `case-guppi` undoes the change and answers with the summary of the Case in its ratified form. The main agent shows the Case again as after a change, and the person ratifies it again, the acknowledging reply carrying the same decision lines, so that the hook of `rule-prespec-onward` counts the Case as ratified.
> **－** In Work Mode the main agent sends no Case of the approved Spec back to its `case-guppi` to be built again under its own number; only a Case ratified in that Work Mode, none of whose tasks has run, changes that way.
> **－** In a `/work` that `/box` calls, no Case is built: a fork stops the run, as `rule-spec-box` sets it, and the choice goes to `raw/<date>/<hi HHMM>/handoff.md` as a line.
> **－** The main agent writes the heading, the list, the `ratification` and the question on another Case from the summary, and does not read the file of the Case.
> **－** The heading carries no name of the main agent's own and not the words of the Frontier item.
> **－** The main agent writes no context of its own before the first question of a round. The label that names the Case of a round in a batch is no such context.
> **－** The main agent writes no `given`, `when`, `then` or `tasks` of a built Case into the chat.
> **－** A deferred decision in the short form is written by the main agent in English in the chat, with no dispatch and no file.
> **－** The file of a Case with a decision line in `raw/<date>/<hi HHMM>/ledger.md` is never emptied: it keeps the `context` and `given` that its Decision page leaves there.

> **tasks:**
> - [ ] update `rule-orchestration`
>   - old: `and in Work Mode when a ratified Case is built again, and the showing`
>   - new: `and in Work Mode when a ratified Case is built again or a new Case replaces a sub-case of one, and the showing`
>   - old: `after its ratification — in the Spec, at pre-spec or in Work Mode — is shown again.`
>   - new: `after its ratification — in the Spec or at pre-spec — is shown again; in Work Mode a new Case replaces it, as the end of this paragraph sets it.`
>   - old: `` Its new file is sent again whole, in Plan Mode as in Work Mode, and ratified again, since the hook of `rule-spec-write` writes a Case only from the text the check of `rule-case-check` stored from its file after a reply that carries its lines; until then nothing of the change is acted on (cases 438, 441). ``
>   - new: `` Its new file is sent again whole in Plan Mode, and ratified again, since the hook of `rule-spec-write` writes a Case only from the text the check of `rule-case-check` stored from its file after a reply that carries its lines; until then nothing of the change is acted on (cases 438, 441). In Work Mode a ratified Case of the approved Spec is never built again under its own number, whatever asks for the change — a fork that changes its contract, as the first condition of `where-to-stop.md` sets it, a change the person asks for, or a text the agent finds wrong or too narrow: the agent dispatches `case-guppi` for a new top-level Case under the id that `uv run guppi caseid --next` prints, with the path of the file of the ratified Case, the sub-case of it that must change and the reason, and shows the new Case as any built Case for the person to ratify; the new Case holds each sub-case it replaces whole, and its decision lines carry `{supersedes:case N.M}` for each such sub-case, or `{supersedes:case N}` for a ratified Case with no sub-cases, so that the hook of `rule-spec-write` writes it into the plan file and `spec.md` and removes the sections it replaces, and `materialize` takes only the new Case; the other sub-cases stand as approved, and `/work` checks the plan before the first task of the new Case, as `rule-work-mode` sets it. A Case ratified in that Work Mode, none of whose tasks has run, changes through its `case-guppi` under its own number, as in Plan Mode. In a `/work` that `/box` calls no Case is built: a fork stops the run, as `rule-spec-box` sets it, and the choice goes to `handoff.md` as a line (case 806.1). ``
>   - old: `` after `/pre-spec`, no question: the reply ends with the Frontier, and the hook of `rule-prespec-onward` sends the agent on (case 561.8). ``
>   - new: `` after `/pre-spec`, no question: the reply ends with the Frontier, and the hook of `rule-prespec-onward` sends the agent on (case 561.8); in Work Mode the reply that acknowledges a Case ratified there ends with the Frontier too, but that hook sends nothing on once the session's `spec.md` stands, so the reply ends the turn and the run goes on at the person's next message, as `rule-work-mode` sets it (case 806.1). ``
>   - change: `in Work Mode a ratified Case is not built again: a new Case under a new number replaces the sub-case that must change, and the replaced sub-case leaves the Spec; the reply that acknowledges it ends the turn (case 806.1)`
> - [ ] update `estimate-orchestration-shows-the-built-case`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — in Work Mode a new Case replaces the sub-case of a ratified Case that must change, and only that sub-case leaves the Spec (case 806.1)`
> - [ ] `uv run guppi render`: `vault/wiki/orchestration.md`
> - [ ] read `estimate-orchestration-shows-the-built-case`

> **ratification:**
> ```
> - decision[case 806.1][update][rule-orchestration]{ref:rule-orchestration}
> - decision[case 806.1][update][estimate-orchestration-shows-the-built-case]{ref:rule-orchestration}
> ```

### Case 806.2 — case-guppi builds the new Case that replaces a sub-case in Work Mode

> **given:**
> `rule-case-build`: renders the agent file of `case-guppi`.
> **＋** `.claude/agents/case-guppi.md`: the file rendered from it.
> **＋** `estimate-case-build-writes-the-case`: its Criterion is replaced whole.
> **＋** `rule-case-check`: the check of the file and the summary of `case-guppi`.
> **＋** `/pre-spec`: the check of the plan whose findings reach `case-guppi`.
> **＋** `.claude/skills/grill-me/SKILL.md`: the shape of a round.
> **＋** `vault/wiki/case-schema.md`: the form of a Case.
> **＋** `vault/wiki/ratification.md`: the form of the ledger lines.
> **＋** `.claude/agents/ask-guppi.md`: the vault query `case-guppi` runs itself.
> **＋** `.claude/settings.json`: the hooks registered on an event.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a Case, in the folder `raw/<date>/<hi HHMM>/cases/`.
> **＋** `raw/<date>/<hi HHMM>/ledger.md`: the ledger of the session.
> **＋** `guppi/ratified.py`: the guard that names a free number for a case file.

> **when:**
> The main agent dispatches `case-guppi` with a Case id, a Frontier item and its source, and the person's words on it; or sends it by `SendMessage` the person's answers to a round, or the person's question or change on a Case it built.
> **＋** Or the hook of `rule-case-check` sends it findings on the file of its Case or on its summary.
> **＋** Or the main agent sends it by `SendMessage` the drop of the Case it built, the drop of a change to that Case, or a finding of `/pre-spec` on that Case.
> **＋** Or, in Work Mode, the main agent dispatches it with the id of a new top-level Case, the path of the file of a ratified Case of the approved Spec, the sub-case of it that must change and the reason.

> **then:**
> `case-guppi` starts with `.claude/skills/grill-me/SKILL.md` in its context by `skills: [grill-me]` in `.claude/agents/case-guppi.md`, and reads `vault/wiki/case-schema.md` and `vault/wiki/ratification.md` whole before it answers.
> **＋** Before a `create` without a `ref`, it runs the vault query of `.claude/agents/ask-guppi.md` itself, and the `context` of the Case gives the answer.
> **＋** It reads each page and file the `given` names, the Criterion of each Estimate such a page lists, and, for a Case that adds or changes a hook, the hooks on the same event in `.claude/settings.json`; each contradiction is fixed in the Case, or the `context` says why it stands.
> **＋** While a fork is open — the bound, the alternative, the promise, the split, the exceptions or what is left not done — its answer is a round of questions in the form of `.claude/skills/grill-me/SKILL.md`, in English, with no Case heading and nothing else but the context of a first round.
> **＋** The first round on an item opens, before its first question, with one prose paragraph under the label `**Context:**`: what the item is about, what the thing does today and where it goes wrong, and what the round decides — a sentence per part where one is enough, a part with nothing to say left out.
> **＋** When no fork is open, it writes the Case whole in English in the chat form of `vault/wiki/case-schema.md`, its ledger lines in the form of `vault/wiki/ratification.md`, from the heading to the fence of `ratification` and nothing else, into `raw/<date>/<hi HHMM>/cases/case-<N>.md` by `Write`, N the id of the top-level Case.
> **＋** Its answer is then a summary alone: a first line `**Built:**` and the path of the file; a second line `**Case:**` with the id and the name of the top-level Case as the heading of the file writes them, a Case with sub-cases included; then one list item per Case and sub-case with its id and name, the Estimate that checks it and one line on what that Estimate checks, and under the item its ledger lines in an untagged fence, as the file holds them.
> **＋** When the `context` of a Case says that another Case of the session should change instead, the item of that Case in the summary carries a line `**Other Case:**` that names the other Case and the change it needs.
> **＋** Where an Estimate that the Case creates, or whose Criterion it replaces, already makes the promise behind that change, the change it names is a pointer to that Estimate, never that promise written again.
> **＋** Sent findings by the hook on the file, or asked for a change by a message, it changes the file by `Edit` of the lines that change and answers with the summary again; sent a finding on its summary alone, it answers with the summary again and leaves the file as it stands; asked by a message that opens a fork, it answers with a round.
> **＋** Asked, by a message or by a finding of `/pre-spec`, for a fix that adds a second behaviour with a promise of its own to a Case that has a decision line in `raw/<date>/<hi HHMM>/ledger.md` and no sub-cases, it builds that behaviour as a new top-level Case beside it, in its own file and with no `{supersedes:case N}` mark. The number of the new Case is one above the highest number of the files under `raw/<date>/<hi HHMM>/cases/` and of the decision lines of that ledger, or the free number that the guard of `guppi/ratified.py` names when it refuses that number. The ratified Case and its file stay as they are, and its summary names the new Case.
> **＋** A pair of that new Case whose sentence the ratified Case changed takes that sentence as the ratified Case leaves it.
> **＋** Dispatched in Work Mode with a ratified Case and the sub-case of it that must change, it reads the file of that Case whole and builds under the id of the prompt a new top-level Case that holds each sub-case it replaces whole, as it is to stand: each page change, task and Estimate of that sub-case that still holds, with the change.
> **＋** Each decision line of that new Case carries `{supersedes:case N.M}` for each sub-case it replaces, or `{supersedes:case N}` for a ratified Case with no sub-cases, and the file of the ratified Case stays as it is.
> **＋** A round may come at the first answer on an item, after a message on a Case it built, and in Work Mode when a ratified Case is built again.
> **＋** In Work Mode a round may also come when it builds a new Case that replaces a sub-case of a ratified Case.
> **＋** It runs on `model: opus` with `effort: medium`, the tools Read, Grep, Glob, Write and Edit, and `permissionMode: auto`, so it writes its file with no prompt while the session is in Plan Mode.
> **＋** Sent the drop of its Case, which has no decision line in `raw/<date>/<hi HHMM>/ledger.md`, it writes empty text into the file of that Case by `Write` and answers with a first line `**Dropped:**` and the path of the file, and nothing else. A file of its own that it leaves behind, when it builds the Case again under another number, it empties the same way only when that Case has no decision line in that ledger.
> **＋** Sent the drop of a change to its Case, which has a decision line in `raw/<date>/<hi HHMM>/ledger.md` and which it changed after the Case was last ratified, it undoes by `Edit` each edit it made since then in every section but `recommend`. `recommend` keeps its items and gains one item `**Change**`: its `Asked:` line says that the person dropped the change, and its `Taken:` line says that the Case went back to its ratified form. It answers with the summary again, so that the check of `rule-case-check` finds an item for each question of its rounds.
> **－** A fix that changes what the ratified Case already set is not built beside it: `case-guppi` builds the Case again under a new number, as `vault/wiki/case-schema.md` sets it.
> **－** In Work Mode it never builds a Case of the approved Spec again under its own number; a Case ratified in that Work Mode that comes back to it before any of its tasks has run it changes under its own number, as in Plan Mode.
> **－** The `**Case:**` line is no Markdown heading, so the hook of `rule-case-check` does not read the summary as a Case.
> **－** It does not write the whole Case again to fix a finding, make a change or undo a change.
> **－** A later round on the item, a round after a message on a Case it built and a round in Work Mode carry no context.
> **－** The context carries no Case heading, so the hook of `rule-case-check` neither checks nor stores the round as a Case; it judges only the form of the questions of the round, not its context.
> **－** It writes no file but the file of its Case, the file it leaves behind under an earlier number of the same Case, and the file of a new Case it builds beside a ratified Case, and no ledger line.
> **－** It empties no file of a Case that has a decision line in `raw/<date>/<hi HHMM>/ledger.md`, the file it leaves behind when it builds that Case again under a new number included: sent the drop of such a Case that it did not change after the Case was last ratified, it answers under a first line `**Fact:**` that the Case is ratified, and the file stands.

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `and in Work Mode when a ratified Case is built again.`
>   - new: `and in Work Mode when a ratified Case is built again or you build a new Case that replaces a sub-case of one.`
>   - old: `description: Build one Case of Plan Mode from a Frontier item and the person's words`
>   - new: `description: Build one Case of Plan Mode from a Frontier item and the person's words, or of Work Mode where a ratified Case must change`
>   - old: `You build one Case of Plan Mode. Write it whole`
>   - new: `You build one Case of Plan Mode, or of Work Mode where a ratified Case of the approved Spec must change. Write it whole`
>   - old: `one sentence on what it sets and the path of its case file (case 579.2);`
>   - new: `one sentence on what it sets and the path of its case file (case 579.2); in Work Mode, where a ratified Case must change, the prompt holds instead the id of the new Case, the path of the file of the ratified Case, which you read whole, the sub-case of it that must change and the reason (case 806.2);`
>   - old: `` a fix that changes what the ratified Case already set you build again under a new number, as `vault/wiki/case-schema.md` sets it (case 725.1). ``
>   - new: `` a fix that changes what the ratified Case already set you build again under a new number, as `vault/wiki/case-schema.md` sets it (case 725.1). In Work Mode, where the prompt names a ratified Case of the approved Spec, the sub-case of it that must change and the reason, you never build that Case again under its own number: you build under the id of the prompt a new top-level Case that holds each sub-case it replaces whole, as it is to stand — each page change, task and Estimate of that sub-case that still holds, with the change, since `materialize` applies nothing of a sub-case that a mark retires — and each of its decision lines carries `{supersedes:case N.M}` for each sub-case it replaces, or `{supersedes:case N}` for a ratified Case with no sub-cases; the file of the ratified Case stays as it is. A Case ratified in that Work Mode that comes back to you before any of its tasks has run you change under its own number, as in Plan Mode (case 806.2). ``
>   - change: `in Work Mode case-guppi builds a new Case that holds whole each sub-case of a ratified Case it replaces and supersedes it, never the ratified Case again under its own number (case 806.2)`
> - [ ] update `estimate-case-build-writes-the-case`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — in Work Mode case-guppi builds a new Case that replaces the sub-case of a ratified Case, never that Case under its own number (case 806.2)`
> - [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
> - [ ] read `estimate-case-build-writes-the-case`

> **ratification:**
> ```
> - decision[case 806.2][update][rule-case-build]{ref:rule-case-build}
> - decision[case 806.2][update][estimate-case-build-writes-the-case]{ref:rule-case-build}
> ```

### Case 806.3 — /work checks the plan before the tasks of a Case ratified in Work Mode

> **given:**
> `rule-work-mode`: renders the skill `/work`.
> **＋** `.claude/skills/work/SKILL.md`: the file rendered from it.
> **＋** `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`: its Criterion is replaced whole.
> **＋** `/box` and `vault/raw/<date>/<HHMM>/`: the conserved Spec that `/box` gives `/work`.
> **＋** `raw/<date>/<hi HHMM>/spec.md`: the approved Spec of the session.
> **＋** `raw/<date>/<hi HHMM>/work.md`: the baseline of Work Mode.
> **＋** `vault/wiki/where-to-stop.md`: the conditions on which the run stops.
> **＋** `/retro` and `vault/wiki/`: the step after Work Mode, and the pages the skill does not write.
> **＋** `rule-prespec-onward`: the hook that sends the agent on after a `LEDGER` block, only while the session's Spec does not stand.
> **＋** `rule-spec-box`: the rule of `/box`, which builds no Case of a conserved Spec again.
> **＋** `raw/<date>/<hi HHMM>/handoff.md`: the handoff of the session.

> **when:**
> The agent calls `/work` on `PreToolUse Skill` after the person picked it at the fork of `ExitPlanMode`, or the person types `/work` on `UserPromptSubmit`, after `uv run guppi render` wrote `.claude/skills/work/SKILL.md` from `rule-work-mode`.
> **＋** Or `/box` calls `/work` with the folder `vault/raw/<date>/<HHMM>/` of a conserved Spec.
> **＋** Or, while the run of `/work` goes on, the person ratifies a Case built in Work Mode.

> **then:**
> `uv run guppi render --check` exits 0: `.claude/skills/work/SKILL.md` equals the Render of `rule-work-mode`.
> **＋** When a `!` substitution of `.claude/skills/work/SKILL.md` comes back empty, the agent runs its command itself — `git branch --show-current` before the check of the branch, `make test` and `make lint` before the first change — and uses that result.
> **＋** On the branch `main` the skill stops and says so, and nothing is written or changed.
> **＋** On another branch, before the first change, the agent writes `raw/<date>/<hi HHMM>/work.md`: under `## Baseline` the exit code of `make test` and of `make lint` with each failing test and each lint finding line as printed, and an empty `## Expected red`.
> **＋** When `work.md` already stands, its `## Baseline` stays as it is.
> **＋** The agent runs the tasks of `raw/<date>/<hi HHMM>/spec.md` in the order the Spec holds them, and ticks each box of code, a test, a migration or a `by hand` check in the reply that finishes the task; a task line that opens with a code span holding `guppi sprint-close` it neither runs nor ticks, since the librarian runs it.
> **＋** The reply that acknowledges a Case ratified in Work Mode ends the turn, since the hook of `rule-prespec-onward` sends nothing on once `raw/<date>/<hi HHMM>/spec.md` stands; at the person's next message the run goes on from where it stopped.
> **＋** After the reply that acknowledges a Case ratified in Work Mode, and before the first task of that Case, the agent runs `uv run guppi prespec --check` on the plan file of the session, with the session id of its `hi:` line.
> **＋** When that check prints a line that does not open with `note:`, the agent stops as the first condition of `vault/wiki/where-to-stop.md` sets it and sends the finding to the `case-guppi` of that Case; the run goes on after the person ratifies the fixed Case and the check prints no such line.
> **＋** A task of that Case whose work already stands, done under the sub-case the Case replaces, is ticked in `raw/<date>/<hi HHMM>/spec.md` and not run again.
> **＋** A task that changes `make lint`, one of its steps or a hook of the working tree that reads a page or a governed file the same Spec updates adds one line under `## Expected red` in the same reply: the check, and the page or file it waits for.
> **＋** When the last task of `raw/<date>/<hi HHMM>/spec.md` is done, before the Work readings, the agent runs `make test` in full and holds each failing test against `## Baseline` of `raw/<date>/<hi HHMM>/work.md`.
> **＋** A failing test that `## Baseline` holds goes on, and a new one whose fix finishes ratified work is fixed.
> **＋** With a folder from `/box`, `work.md` holds a third section, `## Conserved Spec`, naming the folder; the tasks run and ticked are those of that folder's `spec.md`; and the agent deletes that folder's `carry.md` when the last task is done, before the Work readings.
> **－** The skill writes no page of `vault/wiki/`, and it ticks no line of a page, a render, the sprint, the glossary or a reading.
> **－** A new failing test whose fix needs a choice that no ratified Case makes is not fixed in that step: it is a stop of `vault/wiki/where-to-stop.md`.
> **－** Any other new failing test goes on to `/retro`, which fixes it or reverts it into a patch.
> **－** In a `/work` that `/box` calls no Case is ratified, so the check of the plan does not run there: a fork stops the run, as `rule-spec-box` sets it, and the choice goes to `raw/<date>/<hi HHMM>/handoff.md` as a line.

> **tasks:**
> - [ ] update `rule-work-mode`
>   - old: `` the librarian runs it, and the command ticks it (`rule-sprint-close`, case 628.4). ``
>   - new: `` the librarian runs it, and the command ticks it (`rule-sprint-close`, case 628.4). When a Case is ratified in this Work Mode — a new Case that replaces a sub-case of a ratified Case, as `vault/wiki/orchestration.md` sets it — run `uv run guppi prespec --check <the plan file> --session <id>`, the session id of the `hi:` line as `/pre-spec` takes it, after the reply that acknowledges that Case and before its first task. Each line it prints that does not open with `note:` is a finding: stop as the first condition of `vault/wiki/where-to-stop.md` sets it, and send the finding to the `case-guppi` of that Case, which fixes it under its own number while none of its tasks has run; the person ratifies it again, and the run goes on once the check prints no finding. Tick a task of the new Case whose work already stands, done under the sub-case it replaces, and do not run it again. The reply that acknowledges such a Case ends the turn, since no hook sends the agent on once `spec.md` stands: the run goes on at the person's next message, the check first. In a `/work` that `/box` calls no Case is built: a fork stops the run, as `rule-spec-box` sets it, and the choice goes to `handoff.md` as a line (case 806.3). ``
>   - change: `after a Case ratified in Work Mode, /work runs the check of the plan before its first task, stops on a finding, and ticks a task whose work already stands (case 806.3)`
> - [ ] update `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`
>   - set:
>     ```
>     status: pending
>     purpose: "Whether /work stops on main, writes the baseline of make test and make lint into work.md before the first change — running a command itself when its substitution is empty — and keeps it on a resume, runs the tasks of the Spec of the session or of the folder /box gives it in order with their ticks but leaves a guppi sprint-close line to the librarian, names that folder under Conserved Spec and deletes its carry.md, marks an expected red under Expected red, runs the check of the plan before the first task of a Case ratified in Work Mode, stops on its finding and ticks a task of that Case whose work already stands, and after the last task runs make test in full and holds each failing test against the baseline, fixing a new one within ratified work"
>     method: "by hand, at Retro: the new Render of rule-work-mode in the Spec read against each line of the Criterion, recorded in the estimate line; uv run guppi render --check; by hand, after the first /work that runs on the rendered .claude/skills/work/SKILL.md and in which a Case is ratified in Work Mode: the end of the turn after its acknowledging reply, the check of the plan before its first task, what followed a finding and the ticks of its tasks read against the Criterion, recorded in the estimate line"
>     ```
>   - change: `the Criterion replaced whole — the check of the plan before the tasks of a Case ratified in Work Mode, the stop on its finding, and the tick of a task whose work already stands (case 806.3)`
> - [ ] `uv run guppi render`: `.claude/skills/work/SKILL.md`
> - [ ] read `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`

> **ratification:**
> ```
> - decision[case 806.3][update][rule-work-mode]{ref:rule-work-mode}
> - decision[case 806.3][update][estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline]{ref:rule-work-mode}
> ```

### Case 806.4 — A ratified Case found wrong in Work Mode is a stop

> **given:**
> `rule-where-to-stop`: renders the conditions on which the run stops.
> **＋** `vault/wiki/where-to-stop.md`: the file rendered from it.
> **＋** `estimate-where-to-stop-stops-only-on-its-conditions`: its Criterion is replaced whole.
> **＋** `/work`, `/box` and `/retro`: the run from the approved Spec to the handoff.
> **＋** `.claude/skills/box/SKILL.md`, `.claude/skills/sprint-open/SKILL.md`, `.claude/skills/pr-review/SKILL.md` and `.claude/skills/merge-main/SKILL.md`: the skills whose stops the conditions name.
> **＋** `raw/<date>/<hi HHMM>/spec.md`, `raw/<date>/<hi HHMM>/work.md` and `raw/<date>/<hi HHMM>/handoff.md`: the Spec, the baseline and the handoff of the session.
> **＋** `vault/wiki/case-schema.md`: the form of a Case, which names a `stop:` task.
> **＋** `rule-spec-box`: the rule of `/box`, which builds no Case of a conserved Spec again.

> **when:**
> The agent calls `/work` on `PreToolUse Skill` after the person picked it at the fork of `ExitPlanMode`, or the person types `/work` on `UserPromptSubmit`, and the run goes from the tasks of `raw/<date>/<hi HHMM>/spec.md` to the librarian's report.
> **＋** Or the agent calls `/box` on `PreToolUse Skill`, and the run goes from its first step to the librarian's report.

> **then:**
> The context of `/work` holds the text of `vault/wiki/where-to-stop.md`, rendered from `rule-where-to-stop`.
> **＋** The context of `/box`, from `.claude/skills/box/SKILL.md`, holds the same text.
> **＋** The agent ends a reply with a question to the person on a fork that changes a contract, on a hook refusal whose text gives no step it can follow or says that it is a stop, and before an action that git in the repository cannot undo.
> **＋** A fork that changes a contract is a choice that no ratified Case makes, or a ratified Case that turns out wrong: by a text the agent finds wrong or too narrow, or by a finding of `uv run guppi prespec --check` on the plan after a Case ratified in Work Mode.
> **＋** Before a task of `raw/<date>/<hi HHMM>/spec.md` whose text opens with `stop:`, the agent stops and asks; the task runs after the person's word.
> **＋** On the branch `main` the agent stops and says so: Work Mode does not start there.
> **＋** In a run of `/box`, the agent stops and asks when `uv run guppi box --check` prints a line, or when a `git merge --ff-only` of `/box` refuses.
> **＋** In the merge tasks that the opening Case of a sprint holds by `.claude/skills/sprint-open/SKILL.md`, in the merge task that a review Case holds by `.claude/skills/pr-review/SKILL.md`, and in the tasks that a merge Case holds by `.claude/skills/merge-main/SKILL.md`, the agent stops, shows what stopped it and asks when a `git` or `gh` command refuses, or when the merge of a merge Case leaves in conflict a file that the merge Case does not settle.
> **－** `git merge --no-ff --no-commit` of a merge Case of `.claude/skills/merge-main/SKILL.md` that exits non-zero only on files that the merge Case settles is no refusal, and the run goes on to the tasks that settle them.
> **＋** When the full `make test` run of `/work` after its last task finds a failing test that `## Baseline` of `raw/<date>/<hi HHMM>/work.md` does not hold, and its fix needs a choice that no ratified Case makes, the agent ends a reply with a question to the person that names the test and its failure.
> **＋** When the auto mode classifier of Claude Code refuses a tool call that the run needs, the agent ends a reply with a question to the person that gives the shell command doing what the refused call would do, for the person to type after `!` in the prompt.
> **＋** A reply that stops from the call of `/retro` until `raw/<date>/<hi HHMM>/handoff.md` stands opens with `STOP:`.
> **＋** After the person's answer the run goes on from where it stopped.
> **＋** After the person has run the command that a refusal of the auto mode classifier gave, the run goes on from where it stopped.
> **＋** `vault/wiki/case-schema.md` names a task line that opens with `stop:` as a task that waits for the person's word.
> **－** No other point stops the run: any other red test, at `/retro` too, a reading that only the person can take, an observation or a doubt ends as a lesson or a line of `raw/<date>/<hi HHMM>/handoff.md`.

> **tasks:**
> - [ ] update `rule-where-to-stop`
>   - old: `1. A fork that changes a contract: the work needs a choice that no ratified Case makes, so a new Case is needed.`
>   - new: `` 1. A fork that changes a contract: the work needs a choice that no ratified Case makes, or a ratified Case turns out wrong — by a text you find wrong or too narrow, or by a finding of `uv run guppi prespec --check` on the plan after a Case ratified in Work Mode — so a new Case is needed, or that Case is fixed, as `orchestration.md` sets it; in a `/work` that `/box` calls no Case is built, as `rule-spec-box` sets it, and the choice goes to `handoff.md` as a line (case 806.4). ``
>   - change: `the first condition also covers a ratified Case found wrong, by a text the agent finds wrong or by a finding of the check of the plan in Work Mode; under /box no Case is built (case 806.4)`
> - [ ] update `estimate-where-to-stop-stops-only-on-its-conditions`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a fork that changes a contract covers a ratified Case found wrong, by a text the agent finds wrong or by a finding of the check of the plan after a Case ratified in Work Mode (case 806.4)`
> - [ ] `uv run guppi render`: `vault/wiki/where-to-stop.md`
> - [ ] read `estimate-where-to-stop-stops-only-on-its-conditions`

> **ratification:**
> ```
> - decision[case 806.4][update][rule-where-to-stop]{ref:rule-where-to-stop}
> - decision[case 806.4][update][estimate-where-to-stop-stops-only-on-its-conditions]{ref:rule-where-to-stop}
> ```
