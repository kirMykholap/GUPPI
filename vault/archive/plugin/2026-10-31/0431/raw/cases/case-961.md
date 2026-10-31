## Case 961 — Estimates that wait for a rare event are read in this session

> **context:**
> Ten Estimates stay `pending` because each waits for an event that seldom comes. Their pages keep `draft`, and a page with `core: true` that stands `draft` blocks `guppi ship`. Today the reading of such an Estimate is taken only when the librarian sees the event and puts it on the Work list of a later session. Some of the events have already come, in this session or in an earlier one, and nothing reads them. Retro reads, on the Criterion of the Spec, an Estimate that a Case of the session sets `pending`. It leaves `pending` an Estimate whose `method` waits for an event that has not come in this session (`.claude/skills/retro/SKILL.md`, read whole). So each sub-case below sets its Estimate `pending`, writes its Criterion back word for word as its `when` and `then`, and rewrites its `method` as Case 960 of this session sets for a reading by hand: the method names the place where the evidence is saved, and names an event by its kind with no "first". A method whose event has already come opens with `by hand, at Retro`, so that Retro reads it in this session. Case 961.1 reads the showing of Cases 960 and 956: the main transcript of this session, line 777, holds the summary of Case 960 with a line `**Other Case:** Case 956`. Case 961.2 reads the dispatch of this Case, whose prompt names Case 960, which sets the form of the `method` of an Estimate, a text this Case writes. Case 961.3 reads the `/pre-spec` of this session, whose plan holds Case 956.1; that Case adds the hook `guppi libreport` to the `SubagentStop` hooks of `rule-hook-registry`, a list. Case 961.4 reads two earlier builds of a `create` with no `ref`. A Grep `\]\[create\]\[[a-z0-9-]+\](\{tags|$)` over `vault/**/ledger.md` printed, after the render of case 626.1 on 2026-10-04, `vault/archive/plugin/2026-10-12/2349/raw/ledger.md` (787.1, `rule-github-repository`) and `vault/archive/plugin/2026-10-13/1753/raw/ledger.md` (804.6, `rule-clean-branch`). Their case files stand in the archive, and agent transcripts under `~/.claude/projects/` hold those builds. Case 961.5 reads `estimate-ratification-ledger-line-form` from archived ledgers. A Grep `\{addresses:|addressed_by:case` over the ledgers of `vault/archive/plugin/` printed `2026-10-14/0232`, `2026-10-14/1536`, `2026-10-16/2104`, `2026-10-17/2307` and `2026-10-29/2341`. Its last Result read the take-up line of case 629.2 in the ledger of session 2026-10-04/1439. A Grep `\{newtag:` over `vault/**/ledger.md` printed no file, so the line on a new tag cannot be read yet. As the person chose, its method waits only for a lesson line that declares a new tag. Case 961.6 stages the event of `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` on purpose. A task stops Work Mode, and a new Case replaces Case 961.6, its one change being the id of that new Case written into the bracket at the end of the method. The person ratifies it, and Retro reads the run. Each method names its event by its kind, and the case, decision or session it reads now stands in a bracket of its own at the end, as `rule-clean-branch` sets for the text of an Estimate, so the method reads whole without it; `/pre-spec` reported those pointers outside a bracket. Four Estimates keep waiting, as the person chose, since staging them would plant a record or cost a large build that yields no Case. `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` waits for a Case that changes a check and the text it reads. `estimate-case-build-goes-on-after-a-live-compaction` waits for a compaction: a Grep `"subtype":"compact_boundary"` over the subagent transcripts under `~/.claude/projects/c--PROJECTS-GUPPI/` printed no file. `estimate-orchestration-signs-items-taken-together` waits for one answer that takes up two items, and C7 is the last open item. `estimate-synthesis-keeps-actioned-by-the-mark` waits for a real `error` lesson under an `actioned` Insight. `rule-ratification` and `rule-work-mode` both have a line in `backlog.md`. `rule-ratification` carries `deferred_by: ["[[decision-case-907]]"]`. `rule-work-mode` carries no `deferred_by`: its line comes from the Backlog of the closed sprint page `entity-sprint-migration`, archived at `vault/archive/migration/2026-10-10/1555/entities/entity-sprint-migration.md`. This Case changes only one Estimate of each and no line of either page, so it takes up neither line. A Grep of the six slugs over `.guppi/` printed no file, so no test reads these pages. The session's ledger holds no `error` lesson, so no line carries `{addresses:...}`. The check of this file notes that a `－` line of 961.6 on a `/work` that `/box` calls shares most of its words with one of 961.1. Both stand, since each is a line of a live Criterion written back word for word: one bounds what `/work` does, the other what the main agent builds. Cases 960, 956 and 959 of this session are related. This Case writes methods under the rule of Case 960 and changes no page that Case 956 or 959 changes.

> **problem:**
> Ten Estimates wait for an event that seldom comes, and their pages stay `draft`. For several of them the event has already come, or can be staged, but no reading in this session is set to take it.

> **recommend:**
> - **How an Estimate is read in this session**
>   - Recommended: (a) one sub-case per Estimate read in this session: its `method` rewritten to name the event by its kind and the file or transcript that holds the evidence, the Estimate set `pending`, its Criterion kept word for word, so that Retro reads it.
>   - Answer: agreed, (a).
> - **Which Estimates are read from an event that already came**
>   - Recommended: (a) read all five in this session: `estimate-orchestration-shows-the-built-case`, `estimate-orchestration-names-related-cases-in-the-dispatch`, `estimate-case-build-reads-each-list-of-a-new-member`, `estimate-ask-query-before-a-create` and `estimate-ratification-ledger-line-form`.
>   - Answer: agreed, (a).
> - **Which events are staged on purpose in Work Mode**
>   - Recommended: (a) stage only the Work Mode trial: a task stops the run, a new Case replaces a sub-case of this Case with a small real change, and the person ratifies it; the other four Estimates keep waiting.
>   - Answer: agreed, (a).
> - **How the Estimate on the form of a ledger line is read**
>   - Recommended: (b) read the archived ledgers now, and wait only for a lesson line that declares a new tag, since no ledger holds one.
>   - Answer: agreed, (b).

### Case 961.1 — The showing of a built Case is read in this session

> **given:**
> `estimate-orchestration-shows-the-built-case`: its `method` changes, and its Criterion is written back word for word.
> **＋** `rule-orchestration`: the rule it checks, rendered into `vault/wiki/orchestration.md`.
> **＋** `case-guppi` and `ask-guppi`: the agents the main agent dispatches, and `estimate-orchestration-starts-ask-guppi-for-a-hook-test`, which reads a start of `ask-guppi`.
> **＋** `/wait-what`, `.claude/skills/wait-what/SKILL.md` and `.claude/skills/grill-me/SKILL.md`: the explanation and the form of a round.
> **＋** `rule-case-check`, `rule-prespec-onward` and `rule-spec-box` with `/work` and `/box`: the checks and the runs that bound the showing.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`, `raw/<date>/<hi HHMM>/cases/case-<N>.md`, `raw/<date>/<hi HHMM>/ledger.md`, `raw/<date>/<hi HHMM>/handoff.md` and `uv run --project .guppi guppi caseid`: the files and the command of the session.
> **＋** `~/.claude/projects/`: the folder of the transcript of the session.

> **when:**
> The main agent takes up a Frontier item, the person answers a round of questions, answers a shown Case with a question or a change, or asks for a plain explanation of the agent's text — by `/wait-what` on `UserPromptSubmit` or in words — or a ratified Case changes and is shown again, in Plan Mode or in Work Mode, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.
> **＋** Or the person puts off or keeps the item of a Case that `case-guppi` built and that is not ratified, or drops that Case so that the item ends another way.
> **＋** Or the person drops a change to a ratified Case that its `case-guppi` made after the Case was last ratified.
> **＋** Or, in Work Mode, a ratified Case of the approved Spec must change: the work meets a choice it did not make, the person asks for a change, or the main agent finds its text wrong or too narrow.

> **then:**
> The main agent dispatches `case-guppi` with the Case id, the Frontier item and its source, and the person's words on it, in the prompt of the call, after the plan file stands with its title line; nothing of the Case stands in the chat before the answer.
> **＋** The person's answers to a round go to the same `case-guppi` by `SendMessage`, verbatim and untranslated, and so does a question or a change of the person on a shown Case that is not a request for a plain explanation.
> **＋** A request for a plain explanation of a round, of the short text on a Case or of a reply the main agent answers itself by `.claude/skills/wait-what/SKILL.md`; it sends the `case-guppi` of the Case a `SendMessage` only to ask for a fact of the Case, and `case-guppi` answers with the fact alone, under a first line `**Fact:**` and with no Case heading.
> **＋** An answer with no first line `**Built:**`, `**Fact:**` or `**Dropped:**` is a round of questions: the main agent shows it in the chat translated into the language of the chat line by line, slugs, paths and quotations unchanged, each quotation in its blockquote — the `**Context:**` paragraph that opens the first round on an item translated in place before the first question, its label naming its Case and its item of `raw/<date>/<hi HHMM>/frontier.md` when the round is one of a batch, each question in the order and with the number of the answer, opening with its `❓ **Qn** - **<title>**:` line of `.claude/skills/grill-me/SKILL.md` and closing with its `➡️` line, its title, body and recommended answer translated in place, nothing merged, dropped or added between the questions, the agent's own text after the last question and one horizontal rule; no Case is shown, no file is sent, and no step of confirmation follows the last round.
> **＋** The main agent shows a built Case at every showing by `SendUserFile` with `display: render` on `raw/<date>/<hi HHMM>/cases/case-<N>.md`, the file `case-guppi` wrote and the hook of `rule-case-check` checked. In the same reply it writes the heading of the top-level Case: its id, and its name in the language of the chat translated from the `**Case:**` line of the summary `case-guppi` answered with. Under the heading it writes one list with an item per Case and sub-case of the summary: its id, its name in the language of the chat, and a short text in the language of the chat on what done means and how it is checked, taken from the Estimate the summary names for it. Then it writes one `ratification` with the ledger lines of every Case of the list as the summary holds them, and its own text after one horizontal rule. A summary in which a Case names no such Estimate goes back to its `case-guppi` by `SendMessage` before the Case is shown.
> **＋** A Case whose item in the summary carries a line `**Other Case:**` is shown as it stands. In Plan Mode the main agent asks the person no question on it: it sends the other Case to its `case-guppi` by `SendMessage` with the change the line names, and the two Cases are shown together in a batch; in a send of Cases built at the same time it does so after the second pass that `vault/wiki/orchestration.md` sets. Where the `case-guppi` of the other Case answers with a round instead, the round stands in the list of the rounds of the batch, as any round does. In Work Mode it asks the person whether that other Case changes.
> **＋** A reply that shows a Case and that the `Stop` check of `rule-case-check` refuses — its file not sent, or a showing that differs from the checked text — is followed, before the person answers, by a reply that sends the file and shows the `ratification` as the summary holds it.
> **＋** A round or a Case shown with a text of the main agent's own before it or outside its list is not refused and is not shown again: `rule-case-check` tells the agent of it at the person's next message, and the agent keeps the form from the next showing on.
> **＋** A ratified Case that changes — in its prose or in its body — changes through its `case-guppi`, and its new file is sent and ratified again; the main agent edits no Case in the plan file or under `cases/`.
> **＋** In Work Mode, when a ratified Case of the approved Spec must change, the main agent dispatches `case-guppi` for a new top-level Case under the id that `uv run --project .guppi guppi caseid --next --session <stamp>` prints, `<stamp>` the stamp of the `hi:` line of the session, with the path of the file of the ratified Case, the sub-case of it that must change and the reason, shows the new Case as any built Case, and the person ratifies it.
> **＋** An item that needs no decision the main agent closes alone, with no dispatch; outside the start of `ask-guppi` that `estimate-orchestration-starts-ask-guppi-for-a-hook-test` reads, it dispatches `ask-guppi` only at pre-spec, one run over the whole plan at its first run, never to build a Case, and asks that run again only to confirm its own findings.
> **＋** When the person puts off or keeps the item of a Case that `case-guppi` built and that has no decision line in `raw/<date>/<hi HHMM>/ledger.md`, or drops that Case so that the item ends another way, the main agent sends the drop by `SendMessage` to the `case-guppi` of that Case, and the turn of the person's words ends with one line under the bold label `**Waiting:**`, translated, and nothing else. The agent goes on with the item only in the turn that the answer `**Dropped:**` of that `case-guppi` opens, so that the hook of `rule-prespec-onward` finds the file of the Case empty at the end of every later reply.
> **＋** The drop adds no closer: the line of the item in `raw/<date>/<hi HHMM>/frontier.md` closes by one of the closers of `vault/wiki/orchestration.md`, as fits what the person chose — `[x] … · work`, `[x] … · case N` of another Case, `[-] … · sprint · defer`, `[-] … · backlog · kept` or `[-] … · defer case N`.
> **＋** When the person drops a change to a ratified Case that its `case-guppi` made after the Case was last ratified, the main agent sends the drop to that `case-guppi` by `SendMessage`. `case-guppi` undoes the change and answers with the summary of the Case in its ratified form. The main agent shows the Case again as after a change, and the person ratifies it again, the acknowledging reply carrying the same decision lines, so that the hook of `rule-prespec-onward` counts the Case as ratified.
> **－** A start of `ask-guppi` in Work Mode that `estimate-orchestration-starts-ask-guppi-for-a-hook-test` reads is outside this promise.
> **－** In Work Mode the main agent sends no Case of the approved Spec back to its `case-guppi` to be built again under its own number; only a Case ratified in that Work Mode, none of whose tasks has run, changes that way.
> **－** In a `/work` that `/box` calls, no Case is built: a fork stops the run, as `rule-spec-box` sets it, and the choice goes to `raw/<date>/<hi HHMM>/handoff.md` as a line.
> **－** The main agent writes the heading, the list, the `ratification` and the send of another Case from the summary, and does not read the file of the Case.
> **－** The heading carries no name of the main agent's own and not the words of the Frontier item.
> **－** The main agent writes no context of its own before the first question of a round. The label that names the Case of a round in a batch is no such context.
> **－** The main agent writes no `given`, `when`, `then` or `tasks` of a built Case into the chat.
> **－** A deferred decision in the short form is written by the main agent in English in the chat, with no dispatch and no file.
> **－** The file of a Case with a decision line in `raw/<date>/<hi HHMM>/ledger.md` is never emptied: it keeps the `context` and `given` that its Decision page leaves there.

> **tasks:**
> - [ ] update `estimate-orchestration-shows-the-built-case`
>   - set:
>     ```
>     status: pending
>     method: "by hand, at Retro: vault/wiki/orchestration.md read against the Criterion, and the replies of the main agent from a summary of case-guppi in Plan Mode that carries a line Other Case naming a Case of the session to the reply that shows the two Cases, read in the transcript of the session under ~/.claude/projects/ against the Criterion, both recorded in one estimate line with the transcript named (the summary of Case 960 that names Case 956, in session 2026-10-31/0431)"
>     ```
>   - change: `the method reads the showing of Cases 960 and 956 in the transcript of session 0431, the Criterion written back unchanged`
> - [ ] read `estimate-orchestration-shows-the-built-case`

> **ratification:**
> ```
> - decision[case 961.1][update][estimate-orchestration-shows-the-built-case]{ref:rule-orchestration}
> ```

### Case 961.2 — The dispatch that names related Cases is read in this session

> **given:**
> `estimate-orchestration-names-related-cases-in-the-dispatch`: its `method` changes, and its Criterion is written back word for word.
> **＋** `rule-orchestration`: the rule it checks, rendered into `vault/wiki/orchestration.md`.
> **＋** `case-guppi`: the agent the dispatch starts.
> **＋** `raw/<date>/<hi HHMM>/frontier.md` and `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the item and the case files the prompt names.
> **＋** `~/.claude/projects/`: the folder of the transcript of the session.

> **when:**
> The main agent dispatches `case-guppi` by an `Agent` call to build the Case of an item of `raw/<date>/<hi HHMM>/frontier.md`, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> The prompt of the call names each Case of the session, ratified or already shown, that changes a page the item names or sets what happens at the same moment as the item: the same kind of reply, the same hook event or the same command.
> **＋** The prompt also names each Case of the session, ratified or already shown, that sets the form of a text a check reads, or how the check reads it, when the Case of the item may write text of that kind, such as the `method` of an Estimate.
> **＋** Each such Case stands in the prompt by its id, one sentence on what it sets and which pages it changes, and the path of its case file `raw/<date>/<hi HHMM>/cases/case-<N>.md`.
> **＋** When the item is one of two or more items that one answer of the person took up, the prompt also names each other Case of that batch by its id and its Frontier item, and by the path of its case file where that file stands.
> **＋** The main agent judges which Cases of the session are related, and the prompt does not send `case-guppi` to search the Cases of the session.
> **－** A Case of the session that changes no page the item names, acts at another moment, sets no form of a text of a kind the Case of the item may write and is no Case of the same batch need not stand in the prompt.
> **－** A Case that only writes a text a check reads, and sets no form of it, is not related by that text alone.
> **－** When no Case of the session is related and the item is taken up alone, the prompt names none and holds the Case id, the Frontier item with its source and the person's words.

> **tasks:**
> - [ ] update `estimate-orchestration-names-related-cases-in-the-dispatch`
>   - set:
>     ```
>     status: pending
>     method: "by hand, at Retro: an Agent call that dispatched case-guppi for the Case of an item while a Case of the session sets the form of the method of an Estimate and the Case of the item may write such a method, read in the transcript of the session under ~/.claude/projects/ against the Criterion, a related Case left unnamed counted in the reading line and the transcript named (the dispatch of Case 961, which names Case 960, in session 2026-10-31/0431)"
>     ```
>   - change: `the method reads the dispatch of Case 961 in the transcript of session 0431, the Criterion written back unchanged`
> - [ ] read `estimate-orchestration-names-related-cases-in-the-dispatch`

> **ratification:**
> ```
> - decision[case 961.2][update][estimate-orchestration-names-related-cases-in-the-dispatch]{ref:rule-orchestration}
> ```

### Case 961.3 — The search for a new member of a list is read in this session

> **given:**
> `estimate-case-build-reads-each-list-of-a-new-member`: its `method` changes, and its Criterion is written back word for word.
> **＋** `rule-case-build`: the rule it checks, rendered into `.claude/agents/case-guppi.md`.
> **＋** `vault/wiki/`, `.claude/` and `.guppi/guppi/`: the texts the agent searches for a member of the list, and `decisions/`, the folder of `vault/wiki/` it leaves out.
> **＋** `log.md` and `brief.md`: files whose hits are not read.
> **＋** `~/.claude/projects/`: the folder of the agent transcripts of `case-guppi` and `ask-guppi`.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case that adds a member to a list that texts spell out one by one — a key of an item, a kind, a status or a field — and is about to answer with its summary.

> **then:**
> It searches the live pages of `vault/wiki/` outside `decisions/`, `.claude/` and `.guppi/guppi/` for a member that stands in the list already.
> **＋** It reads each hit that lists the members of the list.
> **＋** Each text that lists the members and would miss the new member enters the Case, or the `context` of the Case names it and says why it stands.
> **－** A hit in a History line, in `log.md` or in `brief.md` is not read.

> **tasks:**
> - [ ] update `estimate-case-build-reads-each-list-of-a-new-member`
>   - set:
>     ```
>     status: pending
>     method: "by hand, at Retro: .claude/agents/case-guppi.md read against the Criterion; the agent transcript of a case-guppi that built a Case that adds a hook to the SubagentStop hooks of rule-hook-registry, read for its search of a hook that stands in the list already; and the findings of ask-guppi at the /pre-spec of that session, read in its agent transcript, for a Case that adds a member to a list and misses a text that lists the members; all under ~/.claude/projects/, recorded in one estimate line with the count and the transcripts (the build of Case 956.1, which adds the hook guppi libreport, and the /pre-spec of session 2026-10-31/0431)"
>     ```
>   - change: `the method reads the build of Case 956 and the /pre-spec of session 0431 in their transcripts, the Criterion written back unchanged`
> - [ ] read `estimate-case-build-reads-each-list-of-a-new-member`

> **ratification:**
> ```
> - decision[case 961.3][update][estimate-case-build-reads-each-list-of-a-new-member]{ref:rule-case-build}
> ```

### Case 961.4 — The vault query before a create is read from two earlier builds

> **given:**
> `estimate-ask-query-before-a-create`: its `method` changes, and its Criterion is written back word for word.
> **＋** `rule-ask`: the rule it checks, rendered into `.claude/agents/ask-guppi.md`.
> **＋** `.claude/agents/case-guppi.md`: the agent that runs the query.
> **＋** `vault/wiki/rules/` and `vault/archive/`: the folders the query searches.
> **＋** `vault/archive/plugin/2026-10-12/2349/raw/cases/case-787.md` and `vault/archive/plugin/2026-10-13/1753/raw/cases/case-804.md`: the case files of the two builds.
> **＋** `~/.claude/projects/`: the folder of their agent transcripts.

> **when:**
> `case-guppi`, following `.claude/agents/case-guppi.md`, builds a Case that proposes a `create` without a `ref` and, before it answers, runs itself the vault query of `.claude/agents/ask-guppi.md` as rendered from `rule-ask`.

> **then:**
> It starts with the Grep `^(purpose|deferred_by):` over `vault/wiki/rules/`, then runs one Grep per other category the question touches.
> **＋** A page that already holds the thing is found by meaning, whether the person's words name it in the language of the chat or in the language of the repository, and the `context` of the Case names its slug.
> **＋** A proposal that crosses a rule or a lesson, such as a `SessionStart` hook meant to block, names that rule or lesson in the `context`.
> **＋** The slug the Case writes is checked by a Glob over `vault/archive/`, and the `context` says it is free, live with its category, or archived at its path by the Decision that the archived page's `origin` names.
> **＋** An archived page is opened only when the question names its slug and asks what it said or why it was withdrawn.
> **－** The archive is not searched by meaning: a page the `context` names as existing or near is a live page.

> **tasks:**
> - [ ] update `estimate-ask-query-before-a-create`
>   - set:
>     ```
>     status: pending
>     method: "by hand, at Retro: the agent transcripts under ~/.claude/projects/ of the two builds of case-guppi that create rule-github-repository and rule-clean-branch with no ref, their Grep and Glob calls read against the Criterion, and the context of vault/archive/plugin/2026-10-12/2349/raw/cases/case-787.md and vault/archive/plugin/2026-10-13/1753/raw/cases/case-804.md read with them, recorded in one estimate line with the transcripts named (Cases 787.1 and 804.6, of the sessions 2026-10-12/2349 and 2026-10-13/1753)"
>     ```
>   - change: `the method reads the builds of Cases 787 and 804 in their transcripts and case files, the Criterion written back unchanged`
> - [ ] read `estimate-ask-query-before-a-create`

> **ratification:**
> ```
> - decision[case 961.4][update][estimate-ask-query-before-a-create]{ref:rule-ask}
> ```

### Case 961.5 — The form of a ledger line waits only for a new tag

> **given:**
> `estimate-ratification-ledger-line-form`: its `method` changes, and its Criterion is written back word for word.
> **＋** `rule-ratification`: the rule it checks, rendered into `vault/wiki/ratification.md`.
> **＋** `vault/wiki/tags.md`: the tags a lesson line may carry.
> **＋** The ledgers of `vault/archive/plugin/` and `vault/archive/migration/2026-10-04/1439/raw/ledger.md`: the lines read now.
> **＋** `~/.claude/projects/`: the folder of the transcripts that hold the previews.

> **when:**
> The agent writes the ledger lines of a session — the decision lines in the reply that acknowledges a ratification, a lesson line the moment the lesson exists — with `vault/wiki/ratification.md` rendered from `rule-ratification`.

> **then:**
> A decision line is `- decision[case N][kind][slug]` with `{ref:...}` when the target has a ref, `{tags:...}` on a `create`, and `{supersedes:case N}` when it applies.
> **＋** A line that supersedes more than one Case carries one `{supersedes:case N}` block per Case, side by side, never a list inside one block.
> **＋** A Case that takes up a deferred decision carries, on one of its decision lines, one `{supersedes:case N}` block for each Case in the page's `deferred_by`.
> **＋** When a Case of this session closes the root cause of a lesson of this session, the line written second carries the mark: `{addresses:<lesson slug>}` on the decision line when the lesson line stands first, `{addressed_by:case N}` on the lesson line when the decision lines stand first; one mark per lesson.
> **＋** For a Case with sub-cases, the `N` of `{addressed_by:case N}` is the sub-case whose decision line closes the cause, never the parent, which has no decision line.
> **＋** The mark stands in the preview of the ledger lines the person ratifies, or in the `LEDGER` block of the lesson line.
> **＋** A lesson line whose tag `vault/wiki/tags.md` does not hold carries one `{newtag:<tag>|<meaning>|<aliases>}` block per such tag before `trigger:`, the tag also in its `{tags:...}`, the meaning one line and the aliases the words of the chat language for it.
> **－** A lesson whose fix is ratified in another session gets no mark.

> **tasks:**
> - [ ] update `estimate-ratification-ledger-line-form`
>   - set:
>     ```
>     status: pending
>     method: "by hand, after a lesson line that declares a new tag by a newtag block: that line read in the ledger of its session and its LEDGER block in the transcript of that session under ~/.claude/projects/; with it, the decision and lesson lines that carry an addresses or addressed_by mark in vault/archive/plugin/2026-10-14/0232/raw/ledger.md, vault/archive/plugin/2026-10-14/1536/raw/ledger.md, vault/archive/plugin/2026-10-16/2104/raw/ledger.md, vault/archive/plugin/2026-10-17/2307/raw/ledger.md and vault/archive/plugin/2026-10-29/2341/raw/ledger.md, and the line in vault/archive/migration/2026-10-04/1439/raw/ledger.md that takes up a page with two Cases in its deferred_by, each with its preview in the transcript of its session, read against the Criterion, all recorded in one estimate line (the take-up line is that of case 629.2)"
>     ```
>   - change: `the method reads the marks and the take-up line in archived ledgers and waits only for a lesson line that declares a new tag, the Criterion written back unchanged`
> - [ ] read `estimate-ratification-ledger-line-form`

> **ratification:**
> ```
> - decision[case 961.5][update][estimate-ratification-ledger-line-form]{ref:rule-ratification}
> ```

### Case 961.6 — A Case ratified in Work Mode is staged and read in this session

> **given:**
> `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`: its `method` changes, and its Criterion is written back word for word.
> **＋** `rule-work-mode`: the rule it checks, rendered into `.claude/skills/work/SKILL.md`, with `/work` and `/box`, and `vault/raw/<date>/<HHMM>/`, the folder of a conserved Spec.
> **＋** `raw/<date>/<hi HHMM>/work.md`, `raw/<date>/<hi HHMM>/spec.md` and `raw/<date>/<hi HHMM>/handoff.md`: the files of the run.
> **＋** `vault/wiki/where-to-stop.md`, `rule-prespec-onward`, `rule-spec-box` and `/retro`: the stops and the steps around the run.
> **＋** `uv run --project .guppi guppi render`, `uv run --project .guppi guppi test`, `uv run --project .guppi guppi check`, `uv run --project .guppi guppi prespec --check` and `git branch --show-current`: the commands of the run.
> **＋** `case-guppi`: the agent that builds the Case ratified in Work Mode.
> **＋** `~/.claude/projects/`: the folder of the transcript of the session.

> **when:**
> The agent calls `/work` on `PreToolUse Skill` after the person picked it at the fork of `ExitPlanMode`, or the person types `/work` on `UserPromptSubmit`, after `uv run --project .guppi guppi render` wrote `.claude/skills/work/SKILL.md` from `rule-work-mode`.
> **＋** Or `/box` calls `/work` with the folder `vault/raw/<date>/<HHMM>/` of a conserved Spec.
> **＋** Or, while the run of `/work` goes on, the person ratifies a Case built in Work Mode.

> **then:**
> `uv run --project .guppi guppi render --check` exits 0: `.claude/skills/work/SKILL.md` equals the Render of `rule-work-mode`.
> **＋** When a `!` substitution of `.claude/skills/work/SKILL.md` comes back empty, the agent runs its command itself — `git branch --show-current` before the check of the branch, `uv run --project .guppi guppi test` and `uv run --project .guppi guppi check` before the first change — and uses that result.
> **＋** On the branch `main` the skill stops and says so, and nothing is written or changed.
> **＋** On another branch, before the first change, the agent writes `raw/<date>/<hi HHMM>/work.md`: under `## Baseline` the exit code of `uv run --project .guppi guppi test` and of `uv run --project .guppi guppi check` with each failing test and each lint finding line as printed, and an empty `## Expected red`.
> **＋** When `work.md` already stands, its `## Baseline` stays as it is.
> **＋** The agent runs the tasks of `raw/<date>/<hi HHMM>/spec.md` in the order the Spec holds them, and ticks each box of code, a test, a migration or a `by hand` check in the reply that finishes the task; a task line that opens with a code span holding `guppi sprint-close` it neither runs nor ticks, since the librarian runs it.
> **＋** The reply that acknowledges a Case ratified in Work Mode ends the turn, since the hook of `rule-prespec-onward` sends nothing on once `raw/<date>/<hi HHMM>/spec.md` stands; at the person's next message the run goes on from where it stopped.
> **＋** After the reply that acknowledges a Case ratified in Work Mode, and before the first task of that Case, the agent runs `uv run --project .guppi guppi prespec --check` on the plan file of the session, with the session id of its `hi:` line.
> **＋** When that check prints a line that does not open with `note:`, the agent stops as the first condition of `vault/wiki/where-to-stop.md` sets it and sends the finding to the `case-guppi` of that Case; the run goes on after the person ratifies the fixed Case and the check prints no such line.
> **＋** A task of that Case whose work already stands, done under the sub-case the Case replaces, is ticked in `raw/<date>/<hi HHMM>/spec.md` and not run again.
> **＋** A task that changes `uv run --project .guppi guppi check`, one of its steps or a hook of the working tree that reads a page or a governed file the same Spec updates adds one line under `## Expected red` in the same reply: the check, and the page or file it waits for.
> **＋** When the last task of `raw/<date>/<hi HHMM>/spec.md` is done, before the Work readings, the agent runs `uv run --project .guppi guppi test` in full and holds each failing test against `## Baseline` of `raw/<date>/<hi HHMM>/work.md`.
> **＋** A failing test that `## Baseline` holds goes on, and a new one whose fix finishes ratified work is fixed.
> **＋** With a folder from `/box`, `work.md` holds a third section, `## Conserved Spec`, naming the folder; the tasks run and ticked are those of that folder's `spec.md`; and the agent deletes that folder's `carry.md` when the last task is done, before the Work readings.
> **－** The skill writes no page of `vault/wiki/`, and it ticks no line of a page, a render, the sprint, the glossary or a reading.
> **－** A new failing test whose fix needs a choice that no ratified Case makes is not fixed in that step: it is a stop of `vault/wiki/where-to-stop.md`.
> **－** Any other new failing test goes on to `/retro`, which fixes it or reverts it into a patch.
> **－** In a `/work` that `/box` calls no Case is ratified, so the check of the plan does not run there: a fork stops the run, as `rule-spec-box` sets it, and the choice goes to `raw/<date>/<hi HHMM>/handoff.md` as a line.

> **tasks:**
> - [ ] update `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`
>   - set:
>     ```
>     status: pending
>     method: "by hand, at Retro: uv run --project .guppi guppi render --check; .claude/skills/work/SKILL.md read against each line of the Criterion; a Case ratified in the Work Mode of the session that replaces a sub-case of a ratified Case, the end of the turn after its acknowledging reply, the check of the plan before its first task, what followed a finding and the ticks of its tasks read in the transcript of the session under ~/.claude/projects/ and in its spec.md and work.md against the Criterion, recorded in the estimate line with the transcript named (the Case that replaces Case 961.6, staged in session 2026-10-31/0431)"
>     ```
>   - change: `the method reads a Case ratified in the Work Mode of session 0431, staged on purpose, the Criterion written back unchanged`
> - [ ] stop: in Work Mode, the main agent dispatches `case-guppi` for a new top-level Case under the id that `uv run --project .guppi guppi caseid --next --session <stamp>` prints, which replaces Case 961.6 whole with one change: the bracket at the end of the `method` names the id of that new Case as the Case ratified in Work Mode; the person ratifies it, and the run goes on as `.claude/skills/work/SKILL.md` sets it.
> - [ ] read `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`

> **ratification:**
> ```
> - decision[case 961.6][update][estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline]{ref:rule-work-mode}
> ```
