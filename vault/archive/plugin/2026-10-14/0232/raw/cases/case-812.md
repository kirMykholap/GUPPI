## Case 812 — The id of a new Case comes only with the session's stamp and its plan file

> **context:**
> The main agent takes the number of a new top-level Case from `uv run guppi caseid --next`, which prints the next free id and holds it in the store of the session's plan file, so that the next run prints the id after it. `guppi/caseid.py` finds the session by its stamp, which `session_stamp` of `guppi/event.py` takes from `--session` or a hook payload; a Bash call has no payload, so without the option the stamp is `--------`, `session_dir` and `plan_path` of `guppi/ledger.py` find no folder and no plan file, and the command prints an id it does not hold and counts it without the session's ledger and Case files. With a stamp that finds no plan file, a wrong stamp or a plan file not yet created, it prints the id too, holds nothing and exits 0. `orchestration.md` (twice) and `ratification.md` name the command without the option, and last session it printed one id twice, as `lesson-caseid-held-no-id-without-the-session-option` records. The person chose that the pages name `--session <stamp>`, the stamp of the `hi:` line, that the command refuses to run without it, as `guppi box` does, and, at `/pre-spec`, that it refuses a stamp with no plan file too: a Grep of `add_argument\("--session"` over `guppi/` printed `guppi/box.py` (`required=True`), `guppi/caseid.py`, `guppi/event.py` and `guppi/prespec.py`. The rule weighed against the option of reading the newest `hi` line of the event log is the one that `resolve_session` of `guppi/prespec.py` states for the same stamp: the session is never guessed, since a parallel session writes its own `hi` into the same log and after midnight today's log holds none (case 213.1). The change adds no judgment of a text, only a required option of the parser and a refusal.
> This Case replaces case 810, ratified in this session, after three findings of `/pre-spec`. First, its placeholder `<id>` would have clashed with the sprint `<id>` of the same sentence of `ratification.md`, which names the opening Case of a sprint `<id>-1`, so the stamp is `<stamp>`. Second, `estimate-orchestration-shows-the-built-case` promises the Work Mode dispatch under the id that `uv run guppi caseid --next` prints, a run that now prints no id, and its `method` reads the new Render of `rule-orchestration` at Retro, so Case 812.2 replaces its Criterion; that is a second promise, so the Case is built again with sub-cases under a new number, its decision lines marked `{supersedes:case 810}`. Third, the refusal of a stamp with no plan file. Since the command then refuses before the plan file stands, the Render sentence that has the main agent create the plan file before the first dispatch now says before its first run of the command; the Then of `estimate-orchestration-shows-the-built-case`, which names the dispatch after the plan file stands, stays true. A Grep of `title line` over `vault/wiki/` printed `orchestration.md`, `log.md`, `rule-ask.md`, `rule-spec-reconcile.md`, `rule-skill-hi.md`, `rule-orchestration.md`, `rule-case-check.md`, `estimate-orchestration-shows-the-built-case.md`, `rule-prespec.md`, `estimate-ask-finds.md`, `estimate-prespec-reconciles.md`, `estimate-hi-takes-a-conserved-spec.md`, `estimate-spec-reconcile-refuses-an-edit-of-the-plan.md`, `estimate-prespec-checks-the-frontier.md`, `estimate-case-check-sends-back-a-faulty-round.md` and `estimate-case-check-requires-each-question-of-the-rounds.md`, and over `.claude/` it printed `.claude/skills/hi/SKILL.md`, `.claude/skills/pre-spec/SKILL.md` and `.claude/agents/ask-guppi.md`. `log.md` is not read. Of the rest, only `orchestration.md` and `rule-orchestration.md` set when the plan file of a session that builds Cases is created. `rule-skill-hi`, its estimate and its skill set only the plan file of a conserved Spec, which builds no Case. The others speak of the title line that names a conserved Spec, of the guard that lets that line through, or of the title line of a question.
> `estimate-ratification-case-id-carries-the-sprint` checks the command, and its Criterion names it without the option, so its Criterion is replaced whole, written under `sections`, and its `purpose` names the option; its `method`, `uv run pytest tests/test_caseid.py` and the reading of the new Renders in `spec.md` at Retro, stands. Five lines of the old Criterion are not carried word for word: three now name `--session` — the run of the main agent, the sprint the command takes and the id it holds — and two name case 788.2 where they said this Case, since in a Criterion replaced by case 812 those words would name case 812, which brought in no sprint ids. A Grep of `caseid` over `vault/wiki/` printed `brief.md`, `ratification.md`, `orchestration.md`, `log.md`, `lesson-caseid-held-no-id-without-the-session-option.md`, `rule-orchestration.md`, `rule-ratification.md`, `estimate-orchestration-shows-the-built-case.md`, `estimate-case-check-sends-back-a-case-number-held-by-another-agent.md`, `estimate-spec-box-refuses-a-stale-spec.md`, `estimate-case-check-sends-back-a-ratified-case-in-another-shape.md` and `estimate-ratification-case-id-carries-the-sprint.md`; over `.claude/` it printed nothing. `brief.md` and `log.md` are not read. `estimate-case-check-sends-back-a-case-number-held-by-another-agent`, `estimate-case-check-sends-back-a-ratified-case-in-another-shape` and `estimate-spec-box-refuses-a-stale-spec` speak of the store entry, of `next_id` and of the grammar of an id, which do not change, so they stand. The lesson gets no mark, since it was written in another session; it quotes the old message of the command as what it printed then, so it stands. A Grep of `orchestration\.md|ratification\.md` over `tests/` printed `tests/test_ship.py`, `tests/test_ledger.py` and `tests/test_orchestration.py`: the first reads a copy under a temporary folder, the second only names the file in a message, and the third reads only the blocks tagged `showing` and `defer`, which this Case does not touch, so they stand. A Grep of `caseid\.run|"caseid"` over `tests/` printed `tests/test_caseid.py` and `tests/test_casecheck.py`; both run the command with `--session` over a session whose plan file stands, so they pass the new refusals.

> **problem:**
> The command that numbers a new Case is written without the option that tells it the session, and without it, or without the plan file of that session, the command prints an id that it does not hold and that may already be taken.

> **recommend:**
> - **Where should the command get the session id when you start a new Case?**
>   - Recommended: (c) the pages name `--session <id>`, and the command refuses to run without it.
>   - Answer: agreed, (c).
> - **Which check should prove the fix?**
>   - Recommended: (a) rewrite the text of `estimate-ratification-case-id-carries-the-sprint` whole.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: a finding of `/pre-spec` — the placeholder `<id>` of the stamp clashes with the sprint `<id>` of the same sentence of `ratification.md`.
>   - Taken: the stamp is written `<stamp>` in every new text.
> - **Change**
>   - Asked: a finding of `/pre-spec` — `estimate-orchestration-shows-the-built-case` promises the dispatch under the id of a run that now prints no id.
>   - Taken: Case 812.2 replaces its Criterion, and the Case is built again with sub-cases under a new number.
> - **Change**
>   - Asked: a finding of `/pre-spec`, put to the person — with a stamp that finds no plan file the command still prints an id it does not hold; the person agreed that it refuses: prints no id and exits 1, and the main agent creates the plan file before it takes a number.
>   - Taken: the refusal stands in the `then` and the Criterion of Case 812.1, with a task for the code and its test, and the Render has the plan file created before the first run of the command.

### Case 812.1 — The command takes the session's stamp and refuses without its plan file

> **given:**
> `rule-orchestration`: its Render, `vault/wiki/orchestration.md`, gives the command for a new top-level Case.
> **＋** `rule-ratification`: its Render, `vault/wiki/ratification.md`, states what the command does.
> **＋** `guppi/caseid.py`: the command `guppi caseid --next`.
> **＋** `tests/test_caseid.py`: the tests of the command.
> **＋** `estimate-ratification-case-id-carries-the-sprint`: its Criterion is replaced whole.

> **when:**
> The main agent runs `guppi/caseid.py` by `uv run guppi caseid --next` before it dispatches a new top-level Case, with `vault/wiki/orchestration.md` and `vault/wiki/ratification.md` rendered from `rule-orchestration` and `rule-ratification`.

> **then:**
> `vault/wiki/orchestration.md` and `vault/wiki/ratification.md` give the command as `uv run guppi caseid --next --session <stamp>`, `<stamp>` the stamp of the `hi:` line of the session.
> **＋** `vault/wiki/orchestration.md` has the main agent create the plan file of the session with its title line before its first run of the command.
> **＋** With `--session` and the plan file of the session of that stamp, `guppi/caseid.py` prints and holds the next id of that session, as before.
> **－** Without `--session`, `guppi/caseid.py` prints no id: it prints its usage error and exits 2.
> **－** With `--session` and no plan file of the session of that stamp, `guppi/caseid.py` prints no id, holds nothing, prints one line on stderr and exits 1.

> **tasks:**
> - [ ] update `rule-orchestration`
>   - old: `` for a new top-level Case the id that `uv run guppi caseid --next` prints and holds ``
>   - new: `` for a new top-level Case the id that `uv run guppi caseid --next --session <stamp>` prints and holds, `<stamp>` the stamp of the `hi:` line of the session ``
>   - old: `and creates the plan file with its title line before the first dispatch of the session.`
>   - new: `` and creates the plan file with its title line before its first run of `uv run guppi caseid --next --session <stamp>` in the session, since the command prints no id without that file. ``
>   - old: `` under the id that `uv run guppi caseid --next` prints, with the path of the file of the ratified Case ``
>   - new: `` under the id that `uv run guppi caseid --next --session <stamp>` prints, with the path of the file of the ratified Case ``
>   - change: `the command for the id of a new Case carries --session with the stamp of the hi: line, and the plan file stands before its first run`
> - [ ] update `rule-ratification`
>   - old: `` `uv run guppi caseid --next` prints the id of the next Case of the open sprint and holds it ``
>   - new: `` `uv run guppi caseid --next --session <stamp>`, `<stamp>` the stamp of the `hi:` line of the session, prints the id of the next Case of the open sprint and holds it in the store of the session's plan file, and prints no id without `--session` or without that plan file ``
>   - change: `guppi caseid --next takes --session, and prints no id without it or without the plan file of the session`
> - [ ] update `estimate-ratification-case-id-carries-the-sprint`
>   - set:
>     ```
>     status: pending
>     purpose: Whether every reader of a Case id takes an id that carries its sprint and a plain id from before sprint ids alike, and guppi caseid --next --session <stamp> prints and holds the next id of the open sprint, which the main agent uses, and prints no id without --session or without the plan file of the session
>     ```
>   - sections.Criterion:
>     ```
>     When:
>     `guppi/casecheck.py`, `guppi/ratified.py`, `guppi/lint.py`, `guppi/gate.py` or `guppi/materialize.py` reads a Case id in a ledger line, a heading of a Case file, a file name `case-<id>.md` or an `origin`.
>     **＋** The main agent, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`, runs `uv run guppi caseid --next --session <stamp>`, `<stamp>` the stamp of the `hi:` line of its session, before it dispatches a new top-level Case.
>     **＋** Or `uv run guppi caseid --next` runs without `--session`, or with a stamp whose session has no plan file.
>
>     Then:
>     A Case id of a sprint opened after case 788.2 is the sprint id, a hyphen and the number of the Case in that sprint, from 1, with a dot for each sub-case level, such as `kir-plugin-12.1`, and its Case file is `case-<id>.md` of its top-level Case.
>     **＋** The readers read a Case id through `guppi/caseid.py`, which takes both forms and reads the sprint id as the text before the last hyphen ahead of the number.
>     **＋** The sprints `migration` and `plugin`, opened before case 788.2, keep plain ids to their close, by a fixed list in `guppi/caseid.py`.
>     **＋** The main agent creates the plan file of its session with its title line before its first run of the command.
>     **＋** `uv run guppi caseid --next --session <stamp>` takes the open sprint from the `create` decision line of a sprint page in `raw/<date>/<hi HHMM>/ledger.md` of the session of that stamp, else from the first heading of `vault/wiki/sprint.md`, and prints the next id of that sprint.
>     **＋** It holds the id it prints in `<plan>.checked.json` of the plan file of that session, under that id, with no `agent_id` and no text, so that the next run prints the id after it.
>     **＋** The main agent dispatches each new top-level Case with the id that the command printed, but the opening Case of a sprint, whose id `/sprint-open` sets.
>     **－** Without `--session` the command prints no id: it prints its usage error and exits 2.
>     **－** With a stamp whose session has no plan file, the command prints no id, holds nothing, prints one line on stderr and exits 1.
>     **－** An id with no sprint part, such as `785.1`, stays a Case from before sprint ids, and no page, file or citation is renamed.
>     ```
>   - change: `the Criterion replaced whole — guppi caseid --next takes --session with the stamp of the hi: line, and prints no id without it or without the plan file of the session`
> - [ ] `guppi/caseid.py`: the option `--session` is required; with no plan file of the session the command prints one line on stderr that names the missing plan file, prints no id, holds nothing and exits 1; the docstring says both.
> - [ ] `tests/test_caseid.py`: a test that a run of `guppi caseid --next` without `--session` exits 2 and prints no id, and a test that a run with `--session` over a session with no plan file exits 1, prints no id and writes no store.
> - [ ] `uv run guppi render`: `vault/wiki/orchestration.md`
> - [ ] `uv run guppi render`: `vault/wiki/ratification.md`
> - [ ] read `estimate-ratification-case-id-carries-the-sprint`

> **ratification:**
> ```
> - decision[case 812.1][update][rule-orchestration]{ref:rule-orchestration}{supersedes:case 810}
> - decision[case 812.1][update][rule-ratification]{ref:rule-ratification}{supersedes:case 810}
> - decision[case 812.1][update][estimate-ratification-case-id-carries-the-sprint]{ref:rule-ratification}{supersedes:case 810}
> ```

### Case 812.2 — The Work Mode dispatch names the command with the stamp

> **given:**
> `rule-orchestration`: its Render, `vault/wiki/orchestration.md`, sets the Work Mode dispatch of a new Case.
> **＋** `estimate-orchestration-shows-the-built-case`: its Criterion is replaced whole.

> **when:**
> In Work Mode a ratified Case of the approved Spec must change, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> The main agent dispatches `case-guppi` for a new top-level Case under the id that `uv run guppi caseid --next --session <stamp>` prints, `<stamp>` the stamp of the `hi:` line of the session.

> **tasks:**
> - [ ] update `estimate-orchestration-shows-the-built-case`
>   - set: `{status: pending}`
>   - sections.Criterion:
>     ```
>     When:
>     The main agent takes up a Frontier item, the person answers a round of questions, answers a shown Case with a question or a change, or asks for a plain explanation of the agent's text — by `/wait-what` on `UserPromptSubmit` or in words — or a ratified Case changes and is shown again, in Plan Mode or in Work Mode, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.
>     **＋** Or the person puts off or keeps the item of a Case that `case-guppi` built and that is not ratified, or drops that Case so that the item ends another way.
>     **＋** Or the person drops a change to a ratified Case that its `case-guppi` made after the Case was last ratified.
>     **＋** Or, in Work Mode, a ratified Case of the approved Spec must change: the work meets a choice it did not make, the person asks for a change, or the main agent finds its text wrong or too narrow.
>
>     Then:
>     The main agent dispatches `case-guppi` with the Case id, the Frontier item and its source, and the person's words on it, in the prompt of the call, after the plan file stands with its title line; nothing of the Case stands in the chat before the answer.
>     **＋** The person's answers to a round go to the same `case-guppi` by `SendMessage`, verbatim and untranslated, and so does a question or a change of the person on a shown Case that is not a request for a plain explanation.
>     **＋** A request for a plain explanation of a round, of the short text on a Case or of a reply the main agent answers itself by `.claude/skills/wait-what/SKILL.md`; it sends the `case-guppi` of the Case a `SendMessage` only to ask for a fact of the Case, and `case-guppi` answers with the fact alone, under a first line `**Fact:**` and with no Case heading.
>     **＋** An answer with no first line `**Built:**`, `**Fact:**` or `**Dropped:**` is a round of questions: the main agent shows it in the chat translated into Russian line by line, slugs, paths and quotations unchanged, each quotation in its blockquote — the `**Context:**` paragraph that opens the first round on an item translated in place before the first question, its label naming its Case and its item of `raw/<date>/<hi HHMM>/frontier.md` when the round is one of a batch, each question in the order and with the number of the answer, opening with its `❓ **Qn** - **<title>**:` line of `.claude/skills/grill-me/SKILL.md` and closing with its `➡️` line, its title, body and recommended answer translated in place, nothing merged, dropped or added between the questions, the agent's own text after the last question and one horizontal rule; no Case is shown, no file is sent, and no step of confirmation follows the last round.
>     **＋** The main agent shows a built Case at every showing by `SendUserFile` with `display: render` on `raw/<date>/<hi HHMM>/cases/case-<N>.md`, the file `case-guppi` wrote and the hook of `rule-case-check` checked. In the same reply it writes the heading of the top-level Case: its id, and its name in Russian translated from the `**Case:**` line of the summary `case-guppi` answered with. Under the heading it writes one list with an item per Case and sub-case of the summary: its id, its name in Russian, and a short text in Russian on what done means and how it is checked, taken from the Estimate the summary names for it. Then it writes one `ratification` with the ledger lines of every Case of the list as the summary holds them, and its own text after one horizontal rule. A summary in which a Case names no such Estimate goes back to its `case-guppi` by `SendMessage` before the Case is shown.
>     **＋** A Case whose item in the summary carries a line `**Other Case:**` is shown as it stands, and the main agent asks the person whether that other Case is built again.
>     **＋** A reply that shows a Case and that the `Stop` check of `rule-case-check` refuses — its file not sent, or a showing that differs from the checked text — is followed, before the person answers, by a reply that sends the file and shows the `ratification` as the summary holds it.
>     **＋** A round or a Case shown with a text of the main agent's own before it or outside its list is not refused and is not shown again: `rule-case-check` tells the agent of it at the person's next message, and the agent keeps the form from the next showing on.
>     **＋** A ratified Case that changes — in its prose or in its body — changes through its `case-guppi`, and its new file is sent and ratified again; the main agent edits no Case in the plan file or under `cases/`.
>     **＋** In Work Mode, when a ratified Case of the approved Spec must change, the main agent dispatches `case-guppi` for a new top-level Case under the id that `uv run guppi caseid --next --session <stamp>` prints, `<stamp>` the stamp of the `hi:` line of the session, with the path of the file of the ratified Case, the sub-case of it that must change and the reason, shows the new Case as any built Case, and the person ratifies it.
>     **＋** An item that needs no decision the main agent closes alone, with no dispatch; it dispatches `ask-guppi` only at pre-spec, one run over the whole plan at its first run, never to build a Case, and asks that run again only to confirm its own findings.
>     **＋** When the person puts off or keeps the item of a Case that `case-guppi` built and that has no decision line in `raw/<date>/<hi HHMM>/ledger.md`, or drops that Case so that the item ends another way, the main agent sends the drop by `SendMessage` to the `case-guppi` of that Case, and the turn of the person's words ends with one line under the bold label `**Waiting:**`, translated, and nothing else. The agent goes on with the item only in the turn that the answer `**Dropped:**` of that `case-guppi` opens, so that the hook of `rule-prespec-onward` finds the file of the Case empty at the end of every later reply.
>     **＋** The drop adds no closer: the line of the item in `raw/<date>/<hi HHMM>/frontier.md` closes by one of the closers of `vault/wiki/orchestration.md`, as fits what the person chose — `[x] … · work`, `[x] … · case N` of another Case, `[-] … · sprint · defer`, `[-] … · backlog · kept` or `[-] … · defer case N`.
>     **＋** When the person drops a change to a ratified Case that its `case-guppi` made after the Case was last ratified, the main agent sends the drop to that `case-guppi` by `SendMessage`. `case-guppi` undoes the change and answers with the summary of the Case in its ratified form. The main agent shows the Case again as after a change, and the person ratifies it again, the acknowledging reply carrying the same decision lines, so that the hook of `rule-prespec-onward` counts the Case as ratified.
>     **－** In Work Mode the main agent sends no Case of the approved Spec back to its `case-guppi` to be built again under its own number; only a Case ratified in that Work Mode, none of whose tasks has run, changes that way.
>     **－** In a `/work` that `/box` calls, no Case is built: a fork stops the run, as `rule-spec-box` sets it, and the choice goes to `raw/<date>/<hi HHMM>/handoff.md` as a line.
>     **－** The main agent writes the heading, the list, the `ratification` and the question on another Case from the summary, and does not read the file of the Case.
>     **－** The heading carries no name of the main agent's own and not the words of the Frontier item.
>     **－** The main agent writes no context of its own before the first question of a round. The label that names the Case of a round in a batch is no such context.
>     **－** The main agent writes no `given`, `when`, `then` or `tasks` of a built Case into the chat.
>     **－** A deferred decision in the short form is written by the main agent in English in the chat, with no dispatch and no file.
>     **－** The file of a Case with a decision line in `raw/<date>/<hi HHMM>/ledger.md` is never emptied: it keeps the `context` and `given` that its Decision page leaves there.
>     ```
>   - change: `the Criterion replaced whole — the Work Mode dispatch names guppi caseid --next with --session and the stamp of the hi: line`
> - [ ] read `estimate-orchestration-shows-the-built-case`

> **ratification:**
> ```
> - decision[case 812.2][update][estimate-orchestration-shows-the-built-case]{ref:rule-orchestration}
> ```
