<!-- approved 00:18:16 · session 747ffece -->

# Session 2118 — sprint plugin

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

```then
update:
- slug: rule-orchestration
  replace:
  - old: and in Work Mode when a ratified Case is built again, and the showing
    new: and in Work Mode when a ratified Case is built again or a new Case replaces a sub-case of one, and the showing
  - old: after its ratification — in the Spec, at pre-spec or in Work Mode — is shown again.
    new: after its ratification — in the Spec or at pre-spec — is shown again; in Work Mode a new Case replaces it, as the end of this paragraph sets it.
  - old: Its new file is sent again whole, in Plan Mode as in Work Mode, and ratified again, since the hook of `rule-spec-write` writes a Case only from the text the check of `rule-case-check` stored from its file after a reply that carries its lines; until then nothing of the change is acted on (cases 438, 441).
    new: 'Its new file is sent again whole in Plan Mode, and ratified again, since the hook of `rule-spec-write` writes a Case only from the text the check of `rule-case-check` stored from its file after a reply that carries its lines; until then nothing of the change is acted on (cases 438, 441). In Work Mode a ratified Case of the approved Spec is never built again under its own number, whatever asks for the change — a fork that changes its contract, as the first condition of `where-to-stop.md` sets it, a change the person asks for, or a text the agent finds wrong or too narrow: the agent dispatches `case-guppi` for a new top-level Case under the id that `uv run guppi caseid --next` prints, with the path of the file of the ratified Case, the sub-case of it that must change and the reason, and shows the new Case as any built Case for the person to ratify; the new Case holds each sub-case it replaces whole, and its decision lines carry `{supersedes:case N.M}` for each such sub-case, or `{supersedes:case N}` for a ratified Case with no sub-cases, so that the hook of `rule-spec-write` writes it into the plan file and `spec.md` and removes the sections it replaces, and `materialize` takes only the new Case; the other sub-cases stand as approved, and `/work` checks the plan before the first task of the new Case, as `rule-work-mode` sets it. A Case ratified in that Work Mode, none of whose tasks has run, changes through its `case-guppi` under its own number, as in Plan Mode. In a `/work` that `/box` calls no Case is built: a fork stops the run, as `rule-spec-box` sets it, and the choice goes to `handoff.md` as a line (case 806.1).'
  - old: 'after `/pre-spec`, no question: the reply ends with the Frontier, and the hook of `rule-prespec-onward` sends the agent on (case 561.8).'
    new: 'after `/pre-spec`, no question: the reply ends with the Frontier, and the hook of `rule-prespec-onward` sends the agent on (case 561.8); in Work Mode the reply that acknowledges a Case ratified there ends with the Frontier too, but that hook sends nothing on once the session''s `spec.md` stands, so the reply ends the turn and the run goes on at the person''s next message, as `rule-work-mode` sets it (case 806.1).'
  change: 'in Work Mode a ratified Case is not built again: a new Case under a new number replaces the sub-case that must change, and the replaced sub-case leaves the Spec; the reply that acknowledges it ends the turn (case 806.1)'
- slug: estimate-orchestration-shows-the-built-case
  set:
    status: pending
  change: the Criterion replaced whole — in Work Mode a new Case replaces the sub-case of a ratified Case that must change, and only that sub-case leaves the Spec (case 806.1)
```

```tasks
- [x] update `rule-orchestration`
- [x] update `estimate-orchestration-shows-the-built-case`
- [x] `uv run guppi render`: `vault/wiki/orchestration.md`
- [x] read `estimate-orchestration-shows-the-built-case`
```

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

```then
update:
- slug: rule-case-build
  replace:
  - old: and in Work Mode when a ratified Case is built again.
    new: and in Work Mode when a ratified Case is built again or you build a new Case that replaces a sub-case of one.
  - old: 'description: Build one Case of Plan Mode from a Frontier item and the person''s words'
    new: 'description: Build one Case of Plan Mode from a Frontier item and the person''s words, or of Work Mode where a ratified Case must change'
  - old: You build one Case of Plan Mode. Write it whole
    new: You build one Case of Plan Mode, or of Work Mode where a ratified Case of the approved Spec must change. Write it whole
  - old: one sentence on what it sets and the path of its case file (case 579.2);
    new: one sentence on what it sets and the path of its case file (case 579.2); in Work Mode, where a ratified Case must change, the prompt holds instead the id of the new Case, the path of the file of the ratified Case, which you read whole, the sub-case of it that must change and the reason (case 806.2);
  - old: a fix that changes what the ratified Case already set you build again under a new number, as `vault/wiki/case-schema.md` sets it (case 725.1).
    new: 'a fix that changes what the ratified Case already set you build again under a new number, as `vault/wiki/case-schema.md` sets it (case 725.1). In Work Mode, where the prompt names a ratified Case of the approved Spec, the sub-case of it that must change and the reason, you never build that Case again under its own number: you build under the id of the prompt a new top-level Case that holds each sub-case it replaces whole, as it is to stand — each page change, task and Estimate of that sub-case that still holds, with the change, since `materialize` applies nothing of a sub-case that a mark retires — and each of its decision lines carries `{supersedes:case N.M}` for each sub-case it replaces, or `{supersedes:case N}` for a ratified Case with no sub-cases; the file of the ratified Case stays as it is. A Case ratified in that Work Mode that comes back to you before any of its tasks has run you change under its own number, as in Plan Mode (case 806.2).'
  change: in Work Mode case-guppi builds a new Case that holds whole each sub-case of a ratified Case it replaces and supersedes it, never the ratified Case again under its own number (case 806.2)
- slug: estimate-case-build-writes-the-case
  set:
    status: pending
  change: the Criterion replaced whole — in Work Mode case-guppi builds a new Case that replaces the sub-case of a ratified Case, never that Case under its own number (case 806.2)
```

```tasks
- [x] update `rule-case-build`
- [x] update `estimate-case-build-writes-the-case`
- [x] `uv run guppi render`: `.claude/agents/case-guppi.md`
- [x] read `estimate-case-build-writes-the-case`
```

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

```then
update:
- slug: rule-work-mode
  replace:
  - old: the librarian runs it, and the command ticks it (`rule-sprint-close`, case 628.4).
    new: 'the librarian runs it, and the command ticks it (`rule-sprint-close`, case 628.4). When a Case is ratified in this Work Mode — a new Case that replaces a sub-case of a ratified Case, as `vault/wiki/orchestration.md` sets it — run `uv run guppi prespec --check <the plan file> --session <id>`, the session id of the `hi:` line as `/pre-spec` takes it, after the reply that acknowledges that Case and before its first task. Each line it prints that does not open with `note:` is a finding: stop as the first condition of `vault/wiki/where-to-stop.md` sets it, and send the finding to the `case-guppi` of that Case, which fixes it under its own number while none of its tasks has run; the person ratifies it again, and the run goes on once the check prints no finding. Tick a task of the new Case whose work already stands, done under the sub-case it replaces, and do not run it again. The reply that acknowledges such a Case ends the turn, since no hook sends the agent on once `spec.md` stands: the run goes on at the person''s next message, the check first. In a `/work` that `/box` calls no Case is built: a fork stops the run, as `rule-spec-box` sets it, and the choice goes to `handoff.md` as a line (case 806.3).'
  change: after a Case ratified in Work Mode, /work runs the check of the plan before its first task, stops on a finding, and ticks a task whose work already stands (case 806.3)
- slug: estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline
  set:
    status: pending
    purpose: Whether /work stops on main, writes the baseline of make test and make lint into work.md before the first change — running a command itself when its substitution is empty — and keeps it on a resume, runs the tasks of the Spec of the session or of the folder /box gives it in order with their ticks but leaves a guppi sprint-close line to the librarian, names that folder under Conserved Spec and deletes its carry.md, marks an expected red under Expected red, runs the check of the plan before the first task of a Case ratified in Work Mode, stops on its finding and ticks a task of that Case whose work already stands, and after the last task runs make test in full and holds each failing test against the baseline, fixing a new one within ratified work
    method: 'by hand, at Retro: the new Render of rule-work-mode in the Spec read against each line of the Criterion, recorded in the estimate line; uv run guppi render --check; by hand, after the first /work that runs on the rendered .claude/skills/work/SKILL.md and in which a Case is ratified in Work Mode: the end of the turn after its acknowledging reply, the check of the plan before its first task, what followed a finding and the ticks of its tasks read against the Criterion, recorded in the estimate line'
  change: the Criterion replaced whole — the check of the plan before the tasks of a Case ratified in Work Mode, the stop on its finding, and the tick of a task whose work already stands (case 806.3)
```

```tasks
- [x] update `rule-work-mode`
- [x] update `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`
- [x] `uv run guppi render`: `.claude/skills/work/SKILL.md`
- [ ] read `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`
```

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

```then
update:
- slug: rule-where-to-stop
  replace:
  - old: '1. A fork that changes a contract: the work needs a choice that no ratified Case makes, so a new Case is needed.'
    new: '1. A fork that changes a contract: the work needs a choice that no ratified Case makes, or a ratified Case turns out wrong — by a text you find wrong or too narrow, or by a finding of `uv run guppi prespec --check` on the plan after a Case ratified in Work Mode — so a new Case is needed, or that Case is fixed, as `orchestration.md` sets it; in a `/work` that `/box` calls no Case is built, as `rule-spec-box` sets it, and the choice goes to `handoff.md` as a line (case 806.4).'
  change: the first condition also covers a ratified Case found wrong, by a text the agent finds wrong or by a finding of the check of the plan in Work Mode; under /box no Case is built (case 806.4)
- slug: estimate-where-to-stop-stops-only-on-its-conditions
  set:
    status: pending
  change: the Criterion replaced whole — a fork that changes a contract covers a ratified Case found wrong, by a text the agent finds wrong or by a finding of the check of the plan after a Case ratified in Work Mode (case 806.4)
```

```tasks
- [x] update `rule-where-to-stop`
- [x] update `estimate-where-to-stop-stops-only-on-its-conditions`
- [x] `uv run guppi render`: `vault/wiki/where-to-stop.md`
- [x] read `estimate-where-to-stop-stops-only-on-its-conditions`
```

## Case 807 — A pointer stands in a bracket of its own, which guppi ship removes whole

> **context:**
> `guppi ship` builds the clean copy of GUPPI that other people install, and the workflow `.github/workflows/prod.yml` writes it to the branch `prod` as a commit of its own; `main` is never changed by the build. Today the script removes a bracket that holds only references to cases, and cuts a reference out of a longer bracket, which can leave words that mean nothing, such as `(supersedes 518)` from `(case 523, supersedes 518)`. It fails on a reference inside a sentence, on a session number and on a link to a page that does not ship, so the run of session 1753 printed 206 lines, all in `guppi/*.py` (`vault/raw/2026-10-13/1753/ship.txt`), and the CI run cannot write `prod`. The person chose a rule that ends the same work at every release: a pointer to a Case, a decision or a session stands in this repository in a bracket of its own at the end of its sentence, with the words that go with it, such as `(as set in case 12)`, and the script removes each bracket that holds a pointer whole. The person asked who checks that the script removes nothing needed: what it removes is a bracket that holds a pointer into the records of this repository, which the copy does not hold, and `--review` lists each such bracket that holds other words, so that a needed word is found once and moved out; the writing rule in `case-schema.md`, the check of the plan and a step of `make lint` keep new text in the form.
>
> The run of this session, `uv run guppi ship` at commit 6d9afab, stands in `vault/raw/2026-10-13/2118/ship.txt`; a Grep `^ship: [^g]` over it printed its lines 207 to 312, all under `vault/wiki/`: the rendered schema files, `case-example.md`, `orchestration.md`, `entity-glossary` and rule pages. Some are ids of example Cases, such as `## Case 7 — Members get a reminder before a booking` inside a fenced block of `orchestration.md`, and sample slugs in code spans of `vault/wiki/decisions/schema.yaml`, which the script reads as plain text since it masks code spans only in `.md` files. That schema file ships by right: a new project writes Decision pages of its own. In a round I said that the example of `case-example.md` cannot be fenced; the frame shows that it stands inside a fence tagged `case`, so the fence rule alone covers it, and the exemption of that file and of the Render of `rule-case-example` by name, which the person chose on my word, adds nothing today; the Case keeps it as chosen, and the person may drop it at the showing. The person first chose to reword the pages in this Case from that run; I had said that the run shows every page line that holds a pointer, which is false, since today's script cuts pointers out of longer brackets without a line, and the person then chose a Case of the next session that rewords the pages from the list of the changed script. 807.1 updates `entity-sprint-plugin` with a `change` alone, since the check of the plan asks for an update of the sprint page under a Case that works on its item, and the item stays open until that Case; Case 805 of this session defers the same page, by its line `defer case 805` in `vault/raw/2026-10-13/2118/frontier.md`, and touches no line this Case touches.
>
> The judgment. A Grep `\[Cc\]ases?|[Ss]essions?\\s|decision-case-\{` over `guppi/` printed `guppi/box.py`, `guppi/materialize.py`, `guppi/lint.py` and `guppi/ship.py`. The lines of `guppi/box.py` and `guppi/materialize.py` write a slug `decision-case-N`, and those of `guppi/lint.py` judge the words of a `method`; only `REFS`, `DECISION_LINK`, `DECISION` and `SESSION` of `guppi/ship.py` judge a pointer in prose — a reference to a case, a link or an id of a Decision page, and a mention of a session — so the check of the plan in 807.4 and `--check` in 807.1 import the judgment of `guppi/ship.py`, as `rule-one-judgment-one-implementation` sets it, and no second copy is written. `guppi/prespec.py` judges no pointer today, so the two sides cannot part on an older input.
>
> The frame. A Grep `guppi ship|all five|five steps` over `vault/wiki/` printed 12 files: `brief.md`, not read; the three `schema.yaml` files of entities, rules and estimates and their rule pages `rule-entities-schema`, `rule-rules-schema` and `rule-estimates-schema`, which name the value `guppi` of a shipped page and stand; `rule-clean-branch` and `estimate-clean-branch-writes-a-clean-copy`, set anew in 807.1; `rule-lint` and `estimate-lint-runs-every-step`, which name the five steps of `make lint` and change in 807.2; and `estimate-sprint-plugin-ci-writes-a-clean-branch`, whose line that no text of the copy holds a link to a page the copy leaves out stays true, since such a link becomes a slug in a code span, so its Criterion stands and it is read after the Case of the next session. The same Grep over `.claude/` printed nothing. A Grep `case-schema\.md|rule-case-protocol|rule-lint\.md|rule-clean-branch|rule-prespec-hook|entity-sprint-plugin|estimate-lint-runs-every-step|estimate-clean-branch` over `tests/` printed `tests/test_guard.py`, `tests/test_glossary.py`, `tests/test_ship.py`, `tests/test_case_schema.py`, `tests/test_render.py`, `tests/test_lint.py`, `tests/test_prespec.py` and `tests/test_recall.py`. `tests/test_case_schema.py` reads only the block tagged `case` of the live `case-example.md` or `case-schema.md`, which no pair touches; `tests/test_recall.py` names the path of `case-schema.md` alone; the others seed pages of their own in a temporary folder. `tests/test_lint.py` copies the live `Makefile` and lists the steps of `make lint` in `LINT_STEPS`, so 807.2 changes it. In the page of `rule-case-protocol` the sentence that the story sections may name a case number speaks of text that reaches no shipped page, and stands. The Render of `rule-case-protocol` changes in 807.4 and touches no Estimate of the live reading; the behaviour it tells `case-guppi` is the one the check of 807.4 finds. The brief reports `make lint` at 0 lines and `make test` at 1601 passed and 6 skipped under `## Readings at the close`; the new step of 807.2 is red until the code is reworded in 807.3, an expected red of the same Work Mode. Case 806 of this session changes `rule-orchestration`, `rule-case-build` and `rule-work-mode`, none of the pages of this Case; its check of the plan in Work Mode runs the finding of 807.4 once the code stands. The pair of 807.4 on `rule-case-protocol` adds one sentence, after the sentence on counts, inside the long paragraph of the Language section on the story sections, `given`, `when`, `then` and the chat form, which I read whole: that paragraph lets the story sections name a case number and sets the form of the values of a task, and the new sentence speaks only of the new text of a page with `core: true`, so it contradicts neither; Case 803 of session 1753 wrote into the same page, in the paragraph on the derivable fields, and touches no sentence of this one. The new Criteria carry word for word each old line that still holds: in 807.1 the set of files written, the shipped values, the exit on a section of a page without `core: true`, the pages and files left out, and the form of a line; in 807.2 the printing of each step, the exit code, stdin and the tree. Three old lines are dropped on purpose and stand rewritten: in 807.1 the line that removes a parenthesis of references and cuts references out of a longer one, and the line that exits 1 on a link to a page left out, since the person's rule removes each bracket that holds a pointer whole and turns such a link into a slug; in 807.2 the line that names five steps, since `guppi ship --check` is a sixth. `--check` judges each file outside `vault/` that the clean version holds — `guppi/`, `.claude/`, `CLAUDE.md`, `Makefile`, `pyproject.toml` and `.gitattributes`, by `TREES` and `ROOT_FILES` of `guppi/ship.py` but `uv.lock`, which it does not clean. The rewording of 807.3 covers `guppi/` and the root files edited in Work Mode; a file of `.claude/` and `CLAUDE.md` is rendered from a Rule page and changes only through it, as `rule-governed-files-hook` sets it, so a line on it goes to the handoff with the pages, and the red of `make lint` it makes is a note for the handoff by `rule-retro`. The run of today's script printed no line outside `guppi/` and `vault/wiki/`; the new judgment has not run. The line of 807.3 on `--check` shares words with the lines of 807.1 on `--check` and on the files the command writes, since all three name the same files, but sets another promise: 807.1 promises what the command does, 807.3 that the code of this repository passes it.

> **problem:**
> The clean copy cannot be written: the script fails on pointers it cannot remove safely, and it cuts pointers out of longer brackets in a way that can leave words that mean nothing. No rule says how a pointer is written so that the script can remove it, and nothing keeps new text in such a form.

> **recommend:**
> - **How should a pointer inside a sentence of the code be reworded?**
>   - Recommended: (a) move the pointer into brackets at the end of the sentence.
>   - Answer: not answered; the person stopped the round to ask what is removed from the pages and how. It was replaced by **What is the one form a pointer takes, so the script strips it at every build?**
> - **Does `guppi ship` learn to clean more forms, or is every leftover reworded at its source?**
>   - Recommended: (c) reword every leftover at its source, and the check flags each number of a list of sessions.
>   - Answer: not answered; replaced by **What is the one form a pointer takes, so the script strips it at every build?** and later by **What marks a bracket that the script removes?**
> - **Does this Case also reword the pages and the files built from them?**
>   - Recommended: (b) run `guppi ship` now and cover the pages too.
>   - Answer: not answered; replaced by **Does this Case also reword the page leftovers, which needs a run of the script before I build?**
> - **What is the one form a pointer takes, so the script strips it at every build?**
>   - Recommended: (a) a bracket that holds only pointers to Cases, decisions or sessions; any other bracket with a pointer is listed, and each number of a list of sessions is flagged.
>   - Answer: agreed, (a); later replaced by **What marks a bracket that the script removes?**
> - **What happens to a link to a page that does not ship?**
>   - Recommended: (a) the script turns it into the slug in a code span.
>   - Answer: agreed, (a).
> - **Where is the right form checked as new text is written?**
>   - Recommended: (a) in the check of the plan for pages, told to `case-guppi` in `case-schema.md`, and in `make lint` for the code and the harness, both importing the one check of `guppi/ship.py`.
>   - Answer: agreed, (a).
> - **Does this Case also reword the page leftovers, which needs a run of the script before I build?**
>   - Recommended: (a) yes, after a run of `uv run guppi ship` saved in the session folder.
>   - Answer: agreed, (a); the run was made. Later replaced by **Does this Case still reword the pages, now that the script's list will change?**
> - **What happens to a pointer that shares a bracket with other words?**
>   - Recommended: (b) also strip a pointer that ends a bracket after a comma, a semicolon or a dash.
>   - Answer: not answered; the person asked who checks that the script removes nothing needed, and asked that a pointer and the words that go with it, session numbers and times among them, stand inside the bracket. It was replaced by **What marks a bracket that the script removes?**
> - **What marks a bracket that the script removes?**
>   - Recommended: (a) any bracket that holds a pointer is removed whole; a pointer outside a bracket fails the run; the script lists every bracket that holds a pointer and other words, so that each is reviewed once.
>   - Answer: agreed, (a).
> - **Does this Case still reword the pages, now that the script's list will change?**
>   - Recommended: (a) this Case changes the script, writes the rule, adds the two guards and rewords the code; a Case of the next session rewords the pages from the list of the changed script.
>   - Answer: agreed, (a), in place of the earlier answer.
> - **How does the script treat the ids of example Cases?**
>   - Recommended: (a) the script reads a fenced block of a Markdown file as a sample, like a code span, and leaves `case-example.md` and the Render of `rule-case-example` out of the pointer check.
>   - Answer: agreed, (a).
> - **How does the script read the text of a `schema.yaml`?**
>   - Recommended: (a) the script reads a code span in a `schema.yaml` as it reads one in Markdown.
>   - Answer: agreed, (a).
> - **How does the Case split, and how is each part checked?**
>   - Recommended: (a) three sub-cases, each with its own check.
>   - Answer: agreed, (a); later replaced by **How is the rewording of the code checked, now that one sub-case cannot carry two checks?**
> - **How is the rewording of the code checked, now that one sub-case cannot carry two checks?**
>   - Recommended: (a) four sub-cases: the new step of `make lint` and the rewording of the code are separate.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: at pre-spec, carry each line of the old Criteria that still holds, say why a dropped line is dropped, and date the check of the plan before the Spec is approved, not before a Case is signed.
>   - Taken: 807.1 carries word for word the lines on the pages and files left out, on the sections of a page without `core: true` and on the form of a line, and the `context` says why three lines stand rewritten; the Purpose of `rule-clean-branch` says that `/pre-spec` finds a pointer before the Spec is approved, or, for a Case ratified in Work Mode, before its tasks run.
> - **Change**
>   - Asked: at pre-spec, `--check` judges every file outside `vault/` that `guppi ship` writes, the root files included, and the rewording of the code covers only the files Work Mode may edit.
>   - Taken: `--check` judges `guppi/`, `.claude/` and the root files in 807.1, 807.2 and the Purpose of `rule-clean-branch`; 807.3 rewords `guppi/`, `Makefile`, `pyproject.toml` and `.gitattributes`, and a line on `.claude/` or `CLAUDE.md` goes to the handoff with the pages.
> - **Change**
>   - Asked: at pre-spec, the `context` names `SESSION` among the patterns of `guppi/ship.py` that judge a pointer.
>   - Taken: the `context` names it.
> - **Change**
>   - Asked: at pre-spec, the line of 807.1 on `--check` leaves out `uv.lock`, as the task and the `context` do.
>   - Taken: the line says that `--check` judges each file it would write outside `vault/` but `uv.lock`.

### Case 807.1 — guppi ship removes each bracket that holds a pointer

> **given:**
> `rule-clean-branch`: the rule of the clean version; its Purpose is set anew.
> **＋** `estimate-clean-branch-writes-a-clean-copy`: its Criterion is replaced whole.
> **＋** `guppi/ship.py`: the command `guppi ship` and the one judgment of a pointer.
> **＋** `tests/test_ship.py`: the tests of the command over a sample tree.
> **＋** `entity-sprint-plugin`: the sprint page whose milestone The clean branch this Case works on.
> **＋** `vault/wiki/case-example.md` and `rule-case-example`: the example Case, whose ids are no pointers.
> **＋** `vault/wiki/decisions/schema.yaml`: a schema file of the copy whose text holds sample slugs in code spans.
> **＋** `raw/<date>/<hi HHMM>/handoff.md`: the handoff of the session, which takes the list of the pages.
> **＋** `.claude/` and `vault/wiki/tags.md`: the harness and the tag registry the command copies.
> **＋** `CLAUDE.md`, `Makefile`, `pyproject.toml`, `uv.lock` and `.gitattributes`: the files at the root of the project that the command copies, outside `vault/`.
> **＋** `decision-case-N`: the slug of a Decision page, a pointer the command removes.
> **＋** `vault/raw/`, `vault/archive/` and `.github/`: the session records and the workflows the command leaves out.

> **when:**
> `uv run guppi ship <folder>`, as `rule-clean-branch` sets it, builds the clean version of the project from its working tree into an empty folder.
> **＋** Or `uv run guppi ship --review <folder>` does the same.
> **＋** Or `uv run guppi ship --check` judges the working tree and writes no folder.

> **then:**
> It writes `guppi/`, `.claude/`, `CLAUDE.md`, `Makefile`, `pyproject.toml`, `uv.lock`, `.gitattributes`, the `schema.yaml` of each category, `vault/wiki/tags.md`, each page under `vault/wiki/` with `core: true`, and each file rendered from such a page.
> **＋** In each file it writes, it removes whole each bracket that holds a pointer — a reference to a case, an id `decision-case-N` or a mention of a session by its id — with every word in it and the space before it, and each `[[decision-case-N]]` link; a bracket that holds no pointer stays as it is.
> **＋** It writes each other `[[…]]` link of a Markdown file to a page or a file it does not write as the slug in a code span.
> **＋** Each page it writes carries `origin: guppi`, `sprint: guppi`, the date of the run in `created` and a `## History` of one line that says the page shipped with GUPPI, and its link fields keep only the pages it writes.
> **＋** It exits 1, and prints the file and the line, for each pointer that stands outside such a bracket, each id of a list of sessions included.
> **＋** It exits 1 when a file it writes holds a section between the markers of a page without `core: true`.
> **＋** With `--review` it also prints the file, the line and the bracket for each bracket it removes that holds words beside its pointers, and those lines set no exit code.
> **＋** With `--check` it judges each file it would write outside `vault/` — `guppi/`, `.claude/` and the files at the root of the project — but `uv.lock`, which it does not clean, as it would write it, prints the same lines for it, exits 1 on any, and writes nothing.
> **－** It writes no page without `core: true`, nothing of `vault/raw/`, `vault/archive/` or `.github/`, and no `sprint.md`, `backlog.md`, `brief.md`, `log.md` or `guppi.toml`.
> **－** It writes no file that a page without `core: true` renders in full.
> **－** A case id inside a code span of a Markdown file, or after `[case ` or `#case-`, is the form of a line, not a reference.
> **－** A case id inside a fenced block of a Markdown file, inside a code span of the text of a `schema.yaml`, in `vault/wiki/case-example.md` or the Render of `rule-case-example`, or after `:case `, is the form of a sample or of a line: it is neither removed nor printed.

```then
update:
- slug: rule-clean-branch
  sections:
    Purpose: |-
      Prevents a reference to a case, a mention of a session of this repository or a page that stays in this repository from reaching the clean version of GUPPI that other people install. `guppi ship` builds that version from the working tree into an empty folder: `guppi/`, `.claude/`, `CLAUDE.md`, `Makefile`, `pyproject.toml`, `uv.lock`, `.gitattributes`, the `schema.yaml` of each category, `vault/wiki/tags.md`, each page with `core: true` and each file rendered from such a page, but `sprint.md`, `backlog.md` and `guppi.toml`, which belong to this project. It gives each page `origin: guppi`, `sprint: guppi`, the date of the run in `created` and a `## History` of one line, and keeps in its link fields only the pages it writes.

      A pointer — a reference to a case, an id `decision-case-N` or a mention of a session by its id — stands in this repository in a bracket of its own at the end of its sentence, together with the words that go with it, such as `(as set in case 12)` or `(measured 2026-09-25, session 0051)`, so that the sentence reads whole without it. `guppi ship` removes each bracket that holds a pointer whole, every word in it included, and each `[[decision-case-N]]` link; a bracket that holds no pointer stays. It writes any other `[[…]]` link to a page or a file it does not write as the slug in a code span. A case id in a code span or a fenced block, of a Markdown file or of the text of a `schema.yaml`, in `case-example.md` or the Render of `rule-case-example`, or in the form of a line after `[case `, `#case-` or `:case `, is no pointer. It exits 1 on each pointer that stands outside such a bracket, and on each section of a page without `core: true`; a Case rewords that text at its source. `guppi ship --review` also lists each bracket it removes that holds words beside its pointer, so that a word the sentence needs is found and moved out of the bracket. `guppi ship --check` judges in place each file outside `vault/` that the clean version holds — the code, the harness and the files at the root of the project — and `make lint` runs it; `/pre-spec` finds a pointer outside such a bracket in the new text of a page with `core: true` before the Spec is approved, or, for a Case ratified in Work Mode, before its tasks run (case 807).

      The workflow `.github/workflows/prod.yml` runs it on each push to `main`, and on each push of a tag `prod-*`, such as `prod-1`, on a commit of another branch. It writes the result to the branch `prod` as one new commit on top of the last, whose message names the commit it was built from, and writes none when nothing changed or when the command exits 1. It pushes with a deploy key of this repository with write access, whose private half is the repository secret `PROD_DEPLOY_KEY`; deploy keys stand on the bypass list of the ruleset on `prod` that [[rule-github-repository]] sets. This rule and the workflow belong to this repository: neither carries `core`, and `.github/` is not part of the clean version (case 804).
  change: a pointer stands in a bracket of its own, which guppi ship removes whole; a link to a page left out becomes its slug; --review and --check (case 807.1)
- slug: estimate-clean-branch-writes-a-clean-copy
  set:
    status: pending
    purpose: 'Whether guppi ship writes only the code, the harness and the pages with core: true, removes whole each bracket that holds a pointer, writes a link to a page it leaves out as its slug, writes the shipped values, exits 1 on a pointer outside such a bracket, lists the brackets with words under --review, and judges in place under --check each file outside vault/ that it writes'
  change: the Criterion replaced whole — each bracket that holds a pointer removed whole, a link to a page left out as its slug, samples and examples kept, --review and --check (case 807.1)
- slug: entity-sprint-plugin
  change: 'the clean branch: guppi ship removes each bracket that holds a pointer; the pages are reworded by a Case of the next session (case 807.1)'
```

```tasks
- [x] update `rule-clean-branch`
- [x] update `estimate-clean-branch-writes-a-clean-copy`
- [x] update `entity-sprint-plugin`
- [x] `guppi/ship.py`: the `then` of this Case. A bracket with no bracket inside it, on one line or across lines, that holds a pointer is removed whole; the pointer of a session takes each id of a list, as `REFS` does for cases; a fenced block of a Markdown file and the text of a `schema.yaml` are masked like a code span; `vault/wiki/case-example.md` and the section between the markers of `rule-case-example` are not judged; `--review` and `--check` as the `then` sets them, `--check` over `TREES` and `ROOT_FILES` but `NOT_CLEANED`. The judgment of a pointer — its patterns, the masking, the removal and the list of what remains — is one set of functions of this module, which `guppi/prespec.py` imports. The docstring names the rule.
- [x] `tests/test_ship.py`: the tests of the removal and of what remains follow the new rule — a bracket with words and a pointer removed whole, a bracket with no pointer kept, a session in a bracket removed, each id of a list of sessions printed, a link to a page left out written as its slug — and new tests of a fenced block, of a code span in a `schema.yaml`, of `case-example.md`, of `--review` and of `--check`.
- [x] `uv run guppi ship --review` into an empty temporary folder after the change: its lines under `vault/wiki/`, and its lines on `.claude/` and `CLAUDE.md`, which change only through their Rule pages, go into the handoff for the Case of the next session that rewords the pages; its lines under `guppi/` and on `Makefile`, `pyproject.toml` and `.gitattributes` are the work of 807.3.
- [x] read `estimate-clean-branch-writes-a-clean-copy`
```

### Case 807.2 — make lint runs the pointer check of guppi ship

> **given:**
> `Makefile`: the recipe of `make lint`.
> **＋** `rule-lint`: the rule of lint, whose `implementation_ref` names the `Makefile`; its Purpose names the steps of `make lint`.
> **＋** `estimate-lint-runs-every-step`: its Criterion is replaced whole.
> **＋** `tests/test_lint.py`: runs the recipe of the live `Makefile` with a fake `uv`.
> **＋** `guppi ship --check`: the new step, as 807.1 sets it.
> **＋** `/work` and `.claude/agents/librarian-guppi.md`: where `make lint` runs.

> **when:**
> Someone runs `make lint` of the `Makefile`: by hand, in the Baseline of `/work`, or in the librarian's run of `.claude/agents/librarian-guppi.md`.
> **＋** Or `tests/test_lint.py` runs `make lint` of the `Makefile` in a temp folder, with a fake `uv` first on the search path that records each call and fails the step `guppi backlog --check`.
> **＋** Or `tests/test_lint.py` runs it the same way, with a fake `uv` that exits 0 for every step.

> **then:**
> `make lint` runs each of the steps `guppi render --check`, `guppi sprint --check`, `guppi backlog --check`, `guppi glossary --check`, `guppi lint` and `guppi ship --check`, in that order, whether an earlier step exited 0 or not.
> **＋** Each step prints its own lines as it does when it runs alone, so a red step hides no finding of a later step.
> **＋** `make lint` exits non-zero when any step exits non-zero, and 0 only when every step exits 0.
> **－** No step reads the stdin of its caller, and `make lint` writes nothing to the tree.

```then
update:
- slug: rule-lint
  replace:
  - old: '`make lint` runs it after `render --check`, `sprint --check`, `backlog --check` and `glossary --check`; all five only report, so the Makefile''s rule — no target writes to the tree — holds (cases 147.7, 227). It runs all five even when one of them is red,'
    new: '`make lint` runs it after `render --check`, `sprint --check`, `backlog --check` and `glossary --check`, and runs `guppi ship --check` after it, which finds a pointer outside its bracket in each file outside `vault/` that the clean version holds (case 807.2); all six only report, so the Makefile''s rule — no target writes to the tree — holds (cases 147.7, 227). It runs all six even when one of them is red,'
  change: make lint runs guppi ship --check as its last step (case 807.2)
- slug: estimate-lint-runs-every-step
  set:
    status: pending
    purpose: Whether make lint runs every step, guppi ship --check last, when an earlier one is red, prints the lines of each, and exits non-zero when any step is red
  change: the Criterion replaced whole — guppi ship --check is the last step of make lint (case 807.2)
```

```tasks
- [x] `Makefile`: the target `lint` runs `uv run guppi ship --check < /dev/null || status=1` after `guppi lint`, and its `##` line names the check of the pointers in the files outside `vault/` that the clean version holds.
- [x] `tests/test_lint.py`: `LINT_STEPS` ends with `run guppi ship --check`.
- [x] update `rule-lint`
- [x] update `estimate-lint-runs-every-step`
- [x] read `estimate-lint-runs-every-step`
```

### Case 807.3 — The code holds each pointer in a bracket of its own

> **given:**
> `guppi/`: the modules whose comments and docstrings hold pointers.
> **＋** `estimate-clean-branch-code-holds-pointers-only-in-brackets`: the new check of the code.
> **＋** `rule-clean-branch`: the rule of a pointer in a bracket of its own.
> **＋** `guppi ship --check` and `guppi ship --review`: the judgment of the working tree and the list of brackets with words, as 807.1 sets them.
> **＋** `Makefile`, `pyproject.toml` and `.gitattributes`: the files at the root that `--check` judges, edited in Work Mode.
> **＋** `.claude/` and `CLAUDE.md`: the harness that `--check` judges too, which changes only through its Rule pages.
> **＋** `raw/<date>/<hi HHMM>/handoff.md` and `rule-retro`: where a line on the harness goes, and the note of a red check.
> **＋** `make test`: the suite of the code.

> **when:**
> At Retro of the session, `uv run guppi ship --check` judges the working tree, and `uv run guppi ship --review <folder>` builds the clean version into an empty folder.

> **then:**
> `uv run guppi ship --check` prints no line on a file under `guppi/`, on `Makefile`, on `pyproject.toml` or on `.gitattributes`.
> **＋** Each line of `--review` on those files shows a bracket that holds only pointers and the words that go with them, such as what a pointer sets, when a thing was measured or which session a pointer names.
> **－** No line of `guppi/` changes but a comment or a docstring, and `make test` has no failing test that it did not have before the change.
> **－** A line of `--check` on `.claude/` or `CLAUDE.md` is no part of this promise: it goes into the handoff with the pages, and the red of `make lint` it makes is a note for the handoff by `rule-retro`.

```then
create:
- slug: estimate-clean-branch-code-holds-pointers-only-in-brackets
  ref: rule-clean-branch
  kind: QA
  purpose: Whether the code and the root files of this repository hold each pointer to a case, a decision or a session in a bracket of its own, so that guppi ship --check prints no line on them and no bracket it removes from them holds a word the sentence needs
  method: 'by hand, at Retro: the lines of uv run guppi ship --check over the working tree, and of uv run guppi ship --review into an empty temporary folder, on guppi/, Makefile, pyproject.toml and .gitattributes, read against the Criterion'
  tags:
  - ci
  - plugin
```

```tasks
- [x] `guppi/`, `Makefile`, `pyproject.toml` and `.gitattributes`: each pointer that `uv run guppi ship --check` prints on these files moves, with the words that go with it, into a bracket of its own at the end of its sentence, or its sentence is reworded so that it needs no pointer; each bracket on these files that `--review` prints is split so that a word the sentence needs stands outside it.
- [x] create `estimate-clean-branch-code-holds-pointers-only-in-brackets`
- [x] read `estimate-clean-branch-code-holds-pointers-only-in-brackets`
```

### Case 807.4 — The check of the plan finds a pointer outside its bracket

> **given:**
> `guppi/prespec.py`: the check of the plan, `uv run guppi prespec --check`, and the hook of `ExitPlanMode`.
> **＋** `rule-prespec-hook`: the rule of the check, whose `implementation_ref` names `guppi/prespec.py`.
> **＋** `estimate-prespec-hook-reports-a-pointer-outside-a-bracket`: the new check.
> **＋** `tests/test_prespec.py`: the tests of the check.
> **＋** `guppi/ship.py` and `guppi/pages.py`: the judgment of a pointer and `is_core`, which the check imports.
> **＋** `rule-case-protocol` and `vault/wiki/case-schema.md`: the form of a Case, which tells `case-guppi` how a pointer stands.
> **＋** `decision-case-N`: the slug of a Decision page, a pointer the check finds.
> **＋** `rule-one-judgment-one-implementation`: one judgment, one implementation.

> **when:**
> `uv run guppi prespec --check <plan>` checks the plan of a session, or the hook of `rule-prespec-hook` runs the same judgment when the agent calls `ExitPlanMode`.

> **then:**
> It prints a finding for each pointer — a reference to a case, an id `decision-case-N` or a mention of a session by its id — that stands outside a bracket of its own in the `new` of a `replace` pair, the text of a `sections` value or the `purpose` of an item for a page that carries `core: true`, on the live page or as the plan leaves it.
> **＋** The finding names the Case, the page and the pointer.
> **＋** It judges each text by the judgment that `guppi ship` runs over the files it writes, imported from `guppi/ship.py`.
> **－** A pointer inside such a bracket, a code span or a fenced block is no finding.
> **－** An item for a page without `core: true`, the `change` line of an item, and the `context`, `problem` and `recommend` of a Case are not judged.

```then
create:
- slug: estimate-prespec-hook-reports-a-pointer-outside-a-bracket
  ref: rule-prespec-hook
  kind: QA
  purpose: 'Whether the check of the plan finds a pointer to a case, a decision or a session that stands outside a bracket of its own in the new text of a page with core: true'
  method: uv run pytest tests/test_prespec.py -k pointer
  tags:
  - harness
  - ci
update:
- slug: rule-case-protocol
  replace:
  - old: such as more than 400 000 tokens, stands (case 449).
    new: 'such as more than 400 000 tokens, stands (case 449). In the new text a Case writes for a page with `core: true` — the `new` of a pair, a section, a `purpose` — a pointer to a Case, a decision or a session stands in a bracket of its own at the end of its sentence, with the words that go with it, such as `(as set in case 12)`, since `guppi ship` removes that bracket whole from the clean version and the sentence must read whole without it; a pointer outside such a bracket is a finding of `/pre-spec` (case 807.4).'
  change: 'a pointer in the new text of a page with core: true stands in a bracket of its own (case 807.4)'
```

```tasks
- [x] `guppi/prespec.py`: the finding as the `then` of this Case sets it, by the judgment of `guppi/ship.py` and `is_core` of `guppi/pages.py`; the module docstring names it among the findings of `--check`.
- [x] `tests/test_prespec.py`: one test per line of the `then` of this Case, the names of the tests holding `pointer`.
- [x] create `estimate-prespec-hook-reports-a-pointer-outside-a-bracket`
- [x] update `rule-case-protocol`
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
- [x] read `estimate-prespec-hook-reports-a-pointer-outside-a-bracket`
```

## Deferred

## Case 805 — The shipping of the Estimates of shipped rules with tests put off

> **context:**
> At /hi of session 2118 the person put off Frontier item C3, from the brief: whether the Estimates of shipped rules ship together with `tests/`, as a backlog line for the milestone The plugin. Case 804 of session 1753 ships no Estimate, which the person agreed to "to try it that way", and the handoff of session 1753 named shipping them with `tests/` as a possible backlog line. No Case of this session decides it.

> **problem:**
> No Case of this session decides whether the clean version ships the Estimates of its rules together with `tests/`.

```then
defer:
  - slug: entity-sprint-plugin
    type: entity
    purpose: "Whether the clean version ships the Estimates of its shipped rules together with tests/, as a backlog line for the milestone The plugin; put off at /hi of session 2118"
```
