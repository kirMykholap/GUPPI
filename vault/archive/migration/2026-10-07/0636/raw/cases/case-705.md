## Case 705 — A dropped change takes a ratified Case back to its ratified form

> **context:**
> After `/pre-spec`, the hook of `rule-prespec-onward` sends the agent on by itself only when no Case is still out. `case_out` of `guppi/onward.py` counts a Case as out when its file under `cases/` was written after its last decision line, and it skips a file that holds nothing but blank space, the file of a dropped Case (case 701.1). Case 701 lets `case-guppi` empty only the file of a Case with no decision line, since `guppi/generate.py` leaves the `context` and `given` of a ratified Case in its Case file. So when the person ratifies a Case, sends it back for a change, and then drops the change, the file holds a changed text that nobody ratified, written after the last decision line. The hook stays silent for the rest of Plan Mode, and the Case file that the Decision page points to holds the wrong text. The handoff of session 0425 left this not done. The person chose that dropping a ratified Case after a change means dropping the change, so the Case stays ratified in the form the person ratified. The main agent sends the drop to the `case-guppi` of the Case. `case-guppi` undoes its edits, and the Case is shown again and ratified again, the reply carrying the same decision lines. Taking back the whole decision of a ratified Case is left not done; no rule sets it today, and the handoff carries it to a later session.
>
> The hook needs no change. `last_decisions` of `guppi/onward.py` reads the decision lines of every reply of the main agent in the transcript at the time of its record, so a reply that carries lines the ledger already holds makes the Case ratified again (case 604); `estimate-prespec-onward-reads-the-decisions-of-the-session` already checks this, so its Criterion stands. The hook of `rule-spec-write` writes the restored text from the store after the reply that sends the file and carries the lines, as for any Case ratified again. The check of `rule-case-check` sends back a Case whose `recommend` has no item for a question of the earlier rounds of `case-guppi`, as `estimate-case-check-requires-each-question-of-the-rounds` says. So a full undo would fail the check when the change came with a round, and the person chose that `recommend` keeps its items and gains one `**Change**` item that records the drop. A Case built again under a new number keeps its old file untouched; dropping the new Case empties the new file by Case 701, and the old file stays older than its decision lines, so it is not out. The Criterion of `estimate-case-build-writes-the-case` says that `case-guppi` answers the drop of a ratified Case with `**Fact:**`, and the Criterion of `estimate-orchestration-shows-the-built-case` says that a Case with a decision line gets no drop message; Case 705.1 and Case 705.2 replace them. The purpose and method of the first state the old promise, so 705.1 sets them anew. The purpose and method of the second state no part of it and stand. Each replaced Criterion keeps its old lines word for word, except the lines that change on purpose. In 705.1 these are the `when` line of the drop, which gains the drop of a change, the line that bars writing the whole Case again, which gains the undo, and the line that bars emptying a ratified Case, which now holds only for a Case not changed since its ratification. In 705.2 it is the line that a Case with a decision line gets no drop message, which now says only that its file is never emptied. No promise is lost: the drop of a Case and the bar on writing the whole Case again stay, each with one more case added, and a ratified Case is still never emptied. Only two answers change on purpose: a ratified Case changed since its ratification no longer answers `**Fact:**`, and it now gets a drop message. The `then` of each sub-case holds more than seven ＋ lines because it carries the whole Criterion it replaces. Each sub-case adds one line, so the unit stays atomic: one sub-case is the agent's undo, the other is the main agent's handling of the drop. The two sub-cases share words because they carry the whole Criteria of the agent and of the main agent that reads its answers, and they describe one drop from each side; their promises stay apart. `estimate-case-build-records-the-rounds-in-recommend` says that a change the person asked for on a shown Case is an item `**Change**` with a line `Asked:` and a line `Taken:`. Dropping a change is such a change, and 705.1 records it in that form, so that Criterion stands. `estimate-orchestration-acknowledging-reply` says that the reply that acknowledges a re-ratification carries the `LEDGER` block with the decision lines of each Case ratified again. That is the reply 705.2 relies on after the undo, unchanged, so that Criterion stands too. The prompt says that Case 711 of this session will also update `rule-case-build`; its case file, as it stands, holds no pair on that page. Its pair must not anchor on the drop sentence of the Render, which 705.1 replaces. The rendered `case-guppi.md` changes only at the librarian's render. Until then `case-guppi` answers such a drop with `**Fact:**` as before; no hook refuses anything in between, so no old form is kept.
>
> A Grep for `(?i)\bdrop(s|ped)? (that|the|its|your) Case|drop message|drop of (a|its|the) Case` over `vault/wiki/rules/` printed `rule-case-build.md` and `rule-orchestration.md`, and over `.claude/` printed `.claude/agents/case-guppi.md`. In `rule-case-build.md` one hit is the `description` of `case-guppi`, which stays true, and the other is the paragraph of the drop, which 705.1 changes. In `rule-orchestration.md` one hit is a History line, and the other is the paragraph of the drop, which 705.2 changes. `.claude/agents/case-guppi.md` is rendered from `rule-case-build`. Case 703 of this session changes `rule-case-check` and `guppi/casecheck.py`, which this Case does not touch, and it sets no behaviour at the drop of a Case.

> **problem:**
> When the person drops a change to a ratified Case, its file keeps the changed text that nobody ratified. That file is newer than the Case's last decision line, so the hook of `rule-prespec-onward` stays silent for the rest of Plan Mode.

> **recommend:**
> - **What dropping an approved Case after a change covers**
>   - Recommended: (a) drop the change and keep the approved Case; taking back the whole decision is left not done and goes to the handoff.
>   - Answer: agreed, (a).
> - **How the file of the approved Case comes back**
>   - Recommended: (a) `case-guppi` undoes its edits and answers with its summary; the main agent shows the Case again, and the person ratifies it again with the same lines.
>   - Answer: agreed, (a).
> - **What happens to `recommend` when the change is undone**
>   - Recommended: (a) undo every section but `recommend`, which keeps its items and gains a `**Change**` item that records the drop.
>   - Answer: agreed, (a).

### Case 705.1 — case-guppi undoes a dropped change to a ratified Case

> **given:**
> `rule-case-build`: its Render, the agent file of `case-guppi`, gains the undo of a dropped change.
> **＋** `estimate-case-build-writes-the-case`: its Criterion is replaced whole; its purpose and method are set anew.
> **＋** `.claude/agents/case-guppi.md`: the file rendered from `rule-case-build`.
> **＋** `.claude/skills/grill-me/SKILL.md`: the form of a round.
> **＋** `vault/wiki/case-schema.md`, `vault/wiki/ratification.md` and `.claude/agents/ask-guppi.md`: what `case-guppi` reads before it answers.
> **＋** `rule-case-check` and `.claude/settings.json`: the check of its file and summary, and the hooks it reads for a Case that changes a hook.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md` and `raw/<date>/<hi HHMM>/ledger.md`: the file of its Case and the ledger of the session.

> **when:**
> The main agent dispatches `case-guppi` with a Case id, a Frontier item and its source, and the person's words on it; or sends it by `SendMessage` the person's answers to a round, or the person's question or change on a Case it built.
> **＋** Or the hook of `rule-case-check` sends it findings on the file of its Case or on its summary.
> **＋** Or the main agent sends it by `SendMessage` the drop of the Case it built, or the drop of a change to that Case.

> **then:**
> `case-guppi` starts with `.claude/skills/grill-me/SKILL.md` in its context by `skills: [grill-me]` in `.claude/agents/case-guppi.md`, and reads `vault/wiki/case-schema.md` and `vault/wiki/ratification.md` whole before it answers.
> **＋** Before a `create` without a `ref`, it runs the vault query of `.claude/agents/ask-guppi.md` itself, and the `context` of the Case gives the answer.
> **＋** It reads each page and file the `given` names, the Criterion of each Estimate such a page lists, and, for a Case that adds or changes a hook, the hooks on the same event in `.claude/settings.json`; each contradiction is fixed in the Case, or the `context` says why it stands.
> **＋** While a fork is open — the bound, the alternative, the promise, the split, the exceptions or what is left not done — its answer is a round of questions in the form of `.claude/skills/grill-me/SKILL.md`, in English, with no Case heading and nothing else but the context of a first round.
> **＋** The first round on an item opens, before its first question, with one prose paragraph under the label `**Context:**`: what the item is about, what the thing does today and where it goes wrong, and what the round decides — a sentence per part where one is enough, a part with nothing to say left out.
> **＋** When no fork is open, it writes the Case whole in English in the chat form of `vault/wiki/case-schema.md`, its ledger lines in the form of `vault/wiki/ratification.md`, from the heading to the fence of `ratification` and nothing else, into `raw/<date>/<hi HHMM>/cases/case-<N>.md` by `Write`, N the id of the top-level Case.
> **＋** Its answer is then a summary alone: a first line `**Built:**` and the path of the file; a second line `**Case:**` with the id and the name of the top-level Case as the heading of the file writes them, a Case with sub-cases included; then one list item per Case and sub-case with its id and name, the Estimate that checks it and one line on what that Estimate checks, and under the item its ledger lines in an untagged fence, as the file holds them.
> **＋** When the `context` of a Case says that another Case of the session should change instead, the item of that Case in the summary carries a line `**Other Case:**` that names the other Case and the change it needs.
> **＋** Sent findings by the hook on the file, or asked for a change by a message, it changes the file by `Edit` of the lines that change and answers with the summary again; sent a finding on its summary alone, it answers with the summary again and leaves the file as it stands; asked by a message that opens a fork, it answers with a round.
> **＋** A round may come at the first answer on an item, after a message on a Case it built, and in Work Mode when a ratified Case is built again.
> **＋** It runs on `model: opus` with `effort: medium`, the tools Read, Grep, Glob, Write and Edit, and `permissionMode: auto`, so it writes its file with no prompt while the session is in Plan Mode.
> **＋** Sent the drop of its Case, which has no decision line in `raw/<date>/<hi HHMM>/ledger.md`, it writes empty text into the file of that Case by `Write` and answers with a first line `**Dropped:**` and the path of the file, and nothing else. A file of its own that it leaves behind, when it builds the Case again under another number, it empties the same way.
> **＋** Sent the drop of a change to its Case, which has a decision line in `raw/<date>/<hi HHMM>/ledger.md` and which it changed after the Case was last ratified, it undoes by `Edit` each edit it made since then in every section but `recommend`. `recommend` keeps its items and gains one item `**Change**`: its `Asked:` line says that the person dropped the change, and its `Taken:` line says that the Case went back to its ratified form. It answers with the summary again, so that the check of `rule-case-check` finds an item for each question of its rounds.
> **－** The `**Case:**` line is no Markdown heading, so the hook of `rule-case-check` does not read the summary as a Case.
> **－** It does not write the whole Case again to fix a finding, make a change or undo a change.
> **－** A later round on the item, a round after a message on a Case it built and a round in Work Mode carry no context.
> **－** The context carries no Case heading, so the hook of `rule-case-check` neither checks nor stores the round as a Case; it judges only the form of the questions of the round, not its context.
> **－** It writes no file but the file of its Case, the file it leaves behind under an earlier number of the same Case included, and no ledger line.
> **－** It empties no file of a Case that has a decision line in `raw/<date>/<hi HHMM>/ledger.md`: sent the drop of such a Case that it did not change after the Case was last ratified, it answers under a first line `**Fact:**` that the Case is ratified, and the file stands.

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `` a Case with a decision line you do not empty, and you answer under a first line `**Fact:**` that it is ratified (case 701.3). ``
>   - new: `` a Case with a decision line you do not empty: when the message drops a change you made to it after it was last ratified, you undo by `Edit` each edit you made since then in every section but `recommend`, which keeps its items and gains one item `**Change**` whose `Asked:` line says that the person dropped the change and whose `Taken:` line says that the Case went back to its ratified form, and you answer with the summary again, so that the main agent shows the Case again and the person ratifies it again; when you did not change it since, you answer under a first line `**Fact:**` that it is ratified (cases 701.3, 705.1). ``
>   - change: `case-guppi undoes a change the person dropped on a ratified Case, keeping the items of recommend and adding a Change item, and answers with the summary again (case 705.1)`
> - [ ] update `estimate-case-build-writes-the-case`
>   - set:
>     ```
>     status: pending
>     purpose: "case-guppi asks about the forks of an item in rounds by the skill grill-me, then builds the Case against the vault and its frame, writes it into its file and answers with a short summary, empties the file of a Case it drops, and undoes a change the person dropped on a ratified Case"
>     method: "by hand: live dispatches in a session after the render — one item with a fork, answered by a round and then the Case written into its file and a summary, one Case with a create without a ref, one that changes a hook, a Case the hook sent back and fixed by Edit, a change the person asked for on one sub-case, made by Edit of that sub-case, a Case dropped by a message of the main agent, its file emptied and its answer opening with Dropped, and a change dropped on a ratified Case, its edits undone by Edit but for one Change item in recommend and its answer a summary, the file written in Plan Mode with no prompt; the tokens and seconds of each dispatch in the estimate line"
>     ```
>   - change: `the Criterion replaced whole — case-guppi undoes a change the person dropped on a ratified Case and answers with the summary again (case 705.1)`
> - [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
> - [ ] read `estimate-case-build-writes-the-case`

> **ratification:**
> ```
> - decision[case 705.1][update][rule-case-build]{ref:rule-case-build}
> - decision[case 705.1][update][estimate-case-build-writes-the-case]{ref:rule-case-build}
> ```

### Case 705.2 — The main agent sends a dropped change to its case-guppi and shows the Case again

> **given:**
> `rule-orchestration`: its Render sets how the main agent reads an answer of `case-guppi` and handles a drop.
> **＋** `estimate-orchestration-shows-the-built-case`: its Criterion is replaced whole.
> **＋** `vault/wiki/orchestration.md`: the file rendered from `rule-orchestration`.
> **＋** `rule-case-check`: the check of a showing.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`, `raw/<date>/<hi HHMM>/frontier.md` and `raw/<date>/<hi HHMM>/ledger.md`: the file of a Case, the Frontier and the ledger of the session.
> **＋** `.claude/skills/wait-what/SKILL.md` and `.claude/skills/grill-me/SKILL.md`: the skill of a plain explanation and the form of a question.
> **＋** `rule-prespec-onward`: the hook that counts a Case ratified again by a reply that carries its decision lines.

> **when:**
> The main agent takes up a Frontier item, the person answers a round of questions, answers a shown Case with a question or a change, or asks for a plain explanation of the agent's text — by `/wait-what` on `UserPromptSubmit` or in words — or a ratified Case changes and is shown again, in Plan Mode or in Work Mode, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.
> **＋** Or the person puts off or keeps the item of a Case that `case-guppi` built and that is not ratified, or drops that Case so that the item ends another way.
> **＋** Or the person drops a change to a ratified Case that its `case-guppi` made after the Case was last ratified.

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
> **＋** An item that needs no decision the main agent closes alone, with no dispatch; it dispatches `ask-guppi` only at pre-spec, one run over the whole plan at its first run, never to build a Case, and asks that run again only to confirm its own findings.
> **＋** When the person puts off or keeps the item of a Case that `case-guppi` built and that has no decision line in `raw/<date>/<hi HHMM>/ledger.md`, or drops that Case so that the item ends another way, the main agent sends the drop by `SendMessage` to the `case-guppi` of that Case, and the turn of the person's words ends with one line under the bold label `**Waiting:**`, translated, and nothing else. The agent goes on with the item only in the turn that the answer `**Dropped:**` of that `case-guppi` opens, so that the hook of `rule-prespec-onward` finds the file of the Case empty at the end of every later reply.
> **＋** The drop adds no closer: the line of the item in `raw/<date>/<hi HHMM>/frontier.md` closes by one of the closers of `vault/wiki/orchestration.md`, as fits what the person chose — `[x] … · work`, `[x] … · case N` of another Case, `[-] … · sprint · defer`, `[-] … · backlog · kept` or `[-] … · defer case N`.
> **＋** When the person drops a change to a ratified Case that its `case-guppi` made after the Case was last ratified, the main agent sends the drop to that `case-guppi` by `SendMessage`. `case-guppi` undoes the change and answers with the summary of the Case in its ratified form. The main agent shows the Case again as after a change, and the person ratifies it again, the acknowledging reply carrying the same decision lines, so that the hook of `rule-prespec-onward` counts the Case as ratified.
> **－** The main agent writes the heading, the list, the `ratification` and the question on another Case from the summary, and does not read the file of the Case.
> **－** The heading carries no name of the main agent's own and not the words of the Frontier item.
> **－** The main agent writes no context of its own before the first question of a round. The label that names the Case of a round in a batch is no such context.
> **－** The main agent writes no `given`, `when`, `then` or `tasks` of a built Case into the chat.
> **－** A deferred decision in the short form is written by the main agent in English in the chat, with no dispatch and no file.
> **－** The file of a Case with a decision line in `raw/<date>/<hi HHMM>/ledger.md` is never emptied: it keeps the `context` and `given` that its Decision page leaves there.

> **tasks:**
> - [ ] update `rule-orchestration`
>   - old: `` a Case with a decision line gets no drop message, since its file keeps the `context` and `given` that its Decision page leaves there (case 701.4). ``
>   - new: `` the file of a Case with a decision line is never emptied, since it keeps the `context` and `given` that its Decision page leaves there (case 701.4); when the person drops a change to such a Case that its `case-guppi` made after the Case was last ratified, the agent sends the drop to that `case-guppi` by `SendMessage`, which undoes the change and answers with the summary of the Case in its ratified form, and the agent shows the Case again as after a change, and the person ratifies it again, the acknowledging reply carrying the same decision lines, so that the hook of `rule-prespec-onward` counts the Case as ratified (case 705.2). ``
>   - change: `a change the person drops on a ratified Case goes to its case-guppi, which undoes it, and the Case is shown and ratified again (case 705.2)`
> - [ ] update `estimate-orchestration-shows-the-built-case`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a change the person drops on a ratified Case goes to its case-guppi, and the Case is shown and ratified again with the same lines (case 705.2)`
> - [ ] `uv run guppi render`: `vault/wiki/orchestration.md`
> - [ ] read `estimate-orchestration-shows-the-built-case`

> **ratification:**
> ```
> - decision[case 705.2][update][rule-orchestration]{ref:rule-orchestration}
> - decision[case 705.2][update][estimate-orchestration-shows-the-built-case]{ref:rule-orchestration}
> ```
