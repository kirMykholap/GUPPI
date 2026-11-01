## Case 981 — A summary of case-guppi reaches the main agent only with Built first

> **context:**
> When `case-guppi` finishes a Case, it answers with a summary whose first line is `**Built:**` and the path of the file, and the main agent reads that first line to tell a built Case from a round, a `**Fact:**` answer or a `**Dropped:**` answer. `estimate-orchestration-shows-the-built-case` failed at the Retro of session 0431 (line 45 of `vault/archive/plugin/2026-10-31/0431/raw/ledger.md`): the `case-guppi` of Case 956 answered a change with three paragraphs of prose and `**Built:**` on its fourth line, and the main agent showed that answer as a built Case, where the Render of `rule-orchestration` takes an answer with no first line `**Built:**`, `**Fact:**` or `**Dropped:**` for a round. Cases 971 and 976 put the Estimate off, and `backlog.md` says it was put off in 4 sessions. The `SubagentStop` check of `rule-case-check` let that answer through: in `.guppi/guppi/casecheck.py`, `subagent` calls `summary_findings` after the files of `cases/` the agent wrote are found by `written_case_files`, and `summary_findings` judges the newest output, from `subagent_outputs`, only when `is_summary` finds it a summary, that is when its first line that is not blank opens with `**Built:**`; any other answer gets no finding on its summary. The person chose to fix the slip where it starts: Case 981.1 makes the same check send back an answer that holds a line opening with `**Built:**` after a first line of other text, once for each text and when the agent wrote a file of `cases/`, so that `case-guppi` answers again with the summary alone, and Case 981.2 sets the failed Estimate `pending` with its Criterion written back word for word and reads it at the Retro of this session; its decision line retires the defers of Cases 971 and 976. The frame of `case-guppi`, `.claude/agents/case-guppi.md` rendered from `rule-case-build`, already says to answer with the summary alone and, on a finding on the summary alone, to answer with the summary again and leave the file as it stands, so it stands. The sentence of the Render of `rule-orchestration` that takes such an answer for a round stays true, and the new check is what keeps it from being met. The new judgment reuses `BUILT_LABEL` and `is_summary` of `.guppi/guppi/casecheck.py`, as `rule-one-judgment-one-implementation` sets it: a Grep for `\*\*Built:\*\*` over `.guppi/guppi/` printed hits in `casecheck.py` alone, so no other module judges a summary. A Grep for `subagent\(|Built|summary_findings|is_summary` over `.guppi/tests/`, `test_casecheck.py` left out, printed nothing, and `test_casecheck.py` builds its files in a temporary folder, so no test that reads a live file reaches the changed code. `test_case_schema.py` imports `casecheck` but calls `check_answer`, which this Case does not change. A Grep for `SubagentStop` over `.claude/` printed `.claude/settings.json`, where `guppi libreport` runs beside the check on the same event; it reads the outputs of the librarian and is not touched. In `.guppi/links.md` the block of `rule-case-check` names `estimate-case-check-sends-back-a-summary-without-the-case-name`, whose Criterion judges the `**Case:**` line of an answer that opens with `**Built:**` and leaves out a round, a `**Fact:**` answer and an answer with no file; it stands, since the new check judges only an answer whose first line does not open with `**Built:**`. The front-matter `purpose` of `rule-case-check` names a summary without the id and the name of its Case; it stays true and is not widened. The `purpose` of `estimate-orchestration-shows-the-built-case` says a Case is built by `case-guppi` and shown by the main agent unchanged; it names no part of the old `method`, so only the `method` is set anew. The answers the new check leaves alone rest on the tests the other checks call: `is_round` and `is_fact` of `.guppi/guppi/casecheck.py`, read whole, know a round by a line opening with `❓` with no Case heading and no `**Fact:**` line before it, and a Fact answer by a line opening with `**Fact:**` before any such line; a Grep for `Dropped` over `.guppi/` printed nothing, so no code judges a `**Dropped:**` answer yet, and the task adds its one constant. `estimate-case-build-writes-the-case`, the check of `rule-case-build`, says in its Criterion that the answer is a summary alone with a first line `**Built:**`, and that sent a finding on its summary alone `case-guppi` answers with the summary again and leaves the file as it stands; its Criterion stands, since the new send-back is a finding on the summary alone that asks for exactly that answer. The check of this file noted that the `then` line of Case 981.2 on an answer with no first line `**Built:**`, `**Fact:**` or `**Dropped:**` shares most of its words with the `－` line of Case 981.1 on the answers the hook leaves alone; both stand, since the first sets what the main agent shows and is the old Criterion written back word for word, and the second sets which answers the hook does not send back. A Grep for `lesson\[error\]` over the session's ledger printed nothing, so no `addresses` mark is written.

> **problem:**
> An answer of `case-guppi` with prose before its `**Built:**` line reaches the main agent unchecked and is shown as a built Case, and the check of that showing failed and has been put off for four sessions.

> **recommend:**
> - **What settles the failed check?**
>   - Recommended: (a) the hook sends such an answer back, and the check is read again in this session.
>   - Answer: agreed, (a).

### Case 981.1 — The check sends back a summary after text of its own

> **given:**
> `rule-case-check`: its Purpose gains the new send-back.
> **＋** `.guppi/guppi/casecheck.py`: the `SubagentStop` check `guppi casecheck --subagent`, its `subagent` function and module docstring.
> **＋** `.guppi/tests/test_casecheck.py`: the tests of the check.
> **＋** `estimate-case-check-sends-back-a-summary-after-text`: the new check of the send-back.
> **＋** `rule-one-judgment-one-implementation`: the test of a summary lives in one function.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md` under `cases/`: the file of a Case that `case-guppi` writes.
> **＋** `.claude/settings.json`: where the hook is registered.

> **when:**
> `case-guppi` stops after it wrote or edited a file `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and the `SubagentStop` hook `guppi casecheck --subagent` of `.guppi/guppi/casecheck.py`, registered in `.claude/settings.json`, reads its newest output.

> **then:**
> An output whose first line that is not blank does not open with `**Built:**`, and that holds a later line opening with `**Built:**`, its indent set aside, gets a finding that quotes its first line and tells the agent to answer with the summary alone, its first line `**Built:**`, and the hook exits 2.
> **＋** That finding is sent back in the same exit 2 as the findings on the file and on the `**Case:**` line.
> **＋** A summary is known by `is_summary`, a round by `is_round` and a `**Fact:**` answer by `is_fact` of `.guppi/guppi/casecheck.py`, the one test of each that the other checks call, and a `**Dropped:**` answer by its first line that is not blank opening with one constant of that module.
> **－** An output whose text an earlier output of the subagent already holds, trailing spaces aside, is not sent back again for it.
> **－** An output whose first line that is not blank opens with `**Built:**`, a round, a `**Fact:**` answer, a `**Dropped:**` answer and an output with no line opening with `**Built:**` get no such finding.
> **－** A subagent that wrote no file of `cases/` gets no such finding.

> **tasks:**
> - [ ] update `rule-case-check`
>   - old: `` the one reading that `.guppi/guppi/ledger.py` and `.guppi/guppi/generate.py` share (case 703.1). ``
>   - new: `` the one reading that `.guppi/guppi/ledger.py` and `.guppi/guppi/generate.py` share (case 703.1). The check also sends back, once for each text, an answer of `case-guppi` that wrote a file of a Case, that is no round, no `**Fact:**` answer and no `**Dropped:**` answer, and that holds a line opening with `**Built:**` after a first line of other text, so that `case-guppi` answers again with the summary alone, its first line `**Built:**` (as set in case 981.1). ``
>   - change: `the SubagentStop check sends back an answer with text before its Built line`
> - [ ] create `estimate-case-check-sends-back-a-summary-after-text`
>   - ref: `rule-case-check`
>   - kind: `QA`
>   - purpose: `Whether the check of case-guppi sends back an answer that holds a Built line after a first line of other text, once per text, and leaves a summary that opens with Built, a round, a Fact answer and a Dropped answer alone`
>   - method: `uv run --project .guppi pytest .guppi/tests/test_casecheck.py -k summary_after_text`
>   - tags: `[hooks, harness, workflow]`
> - [ ] `.guppi/guppi/casecheck.py`: a function that, for a subagent that wrote a file of `cases/`, judges the newest output by `BUILT_LABEL`, `is_summary`, `is_round`, `is_fact` and a new constant `DROPPED_LABEL`, `**Dropped:**`, the first judgment of a Dropped answer in `.guppi/guppi/`, and gives the finding; `subagent` joins it with the other findings in one exit 2; the module docstring says so beside the paragraph on the name in the summary.
> - [ ] `.guppi/tests/test_casecheck.py`: tests named `test_subagent_summary_after_text_*` for an answer with prose before `**Built:**` sent back, the same text not sent back twice, a summary that opens with `**Built:**`, a round, a `**Fact:**` answer and a `**Dropped:**` answer passing, and no file written passing.
> - [ ] read `estimate-case-check-sends-back-a-summary-after-text`

> **ratification:**
> ```
> - decision[case 981.1][update][rule-case-check]{ref:rule-case-check}
> - decision[case 981.1][create][estimate-case-check-sends-back-a-summary-after-text]{ref:rule-case-check}{tags:hooks,harness,workflow}
> ```

### Case 981.2 — The showing of a built Case is read again in this session

> **given:**
> `estimate-orchestration-shows-the-built-case`: its `method` changes, and its Criterion is written back word for word.
> **＋** `rule-orchestration`: the rule it checks, rendered into `vault/wiki/orchestration.md`.
> **＋** `case-guppi`: the agent whose answers the main agent shows.
> **＋** `.claude/skills/grill-me/SKILL.md` and `.claude/skills/wait-what/SKILL.md`: the form of a round and the plain explanation.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`, `raw/<date>/<hi HHMM>/ledger.md` and `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the item, the ledger and the file of a Case.
> **＋** `~/.claude/projects/`: the folder of the transcript of the session.
> **＋** `rule-case-check`: the check of a shown Case and of the file of a Case.
> **＋** `rule-prespec-onward`: the hook that counts a Case as ratified and finds a dropped file empty.
> **＋** `estimate-orchestration-starts-ask-guppi-for-a-hook-test`: the check of the start of `ask-guppi` left out of this promise.
> **＋** `/work`, `/box` and `rule-spec-box`: the run in which no Case is built.
> **＋** `raw/<date>/<hi HHMM>/handoff.md`: where a fork of that run goes.

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
>     method: "by hand, at Retro: vault/wiki/orchestration.md read against the Criterion, and the replies of the main agent of the session from each answer of case-guppi to the reply that shows its round or its Case, read in the transcript of the session under ~/.claude/projects/ against the Criterion, a part of the Criterion the session did not meet named as not met, both recorded in one estimate line with the transcript named (the showings of session 2026-11-01/0141)"
>     ```
>   - change: `the method reads the showings of session 0141 at its Retro, the Criterion written back unchanged; the defers of cases 971 and 976 retired`
> - [ ] read `estimate-orchestration-shows-the-built-case`

> **ratification:**
> ```
> - decision[case 981.2][update][estimate-orchestration-shows-the-built-case]{ref:rule-orchestration}{supersedes:case 971}{supersedes:case 976}
> ```
