## Case 662 — The summary of case-guppi names the Case it built, and the heading of a showing takes that name

> **context:**
> When `case-guppi` has written a Case into its file, it answers the main agent with a summary: the path, then one list item per Case and sub-case with its Estimate and its ledger lines. A top-level Case with sub-cases has no Estimate and no ledger lines of its own, so `case-guppi` gives it no item, and no line of the summary holds its name. The main agent writes the showing from the summary and does not read the file (case 645.6), so it wrote the heading of the showing in its own words. In session 1343 Case 653 was shown under the words of Frontier item C3, and the reading of `estimate-orchestration-shows-the-built-case` failed on it (L36 of that session's ledger; lesson L44). In this session Cases 660 and 661 were shown under headings the main agent composed, not the names their files hold. The person chose three things: the summary carries, after its `**Built:**` line, a line `**Case:**` with the id and the name of the top-level Case as the heading of the file writes them, and the main agent translates that name for the heading; the `SubagentStop` check of `rule-case-check` sends back a summary whose line is missing or differs from the file; and `insight-case-show-built-case-retyped-by-hand` stays open. The line is a bold label and not a Markdown heading, because `answer_of` of `guppi/casecheck.py` takes an output that holds a `## Case` heading as a Case to check, and would judge the summary as a faulty Case.
>
> Three promises change, so the Case has three sub-cases. Case 662.1 changes the summary in the Render of `rule-case-build` and replaces the Criterion of `estimate-case-build-writes-the-case`, whose summary line the change makes false. Case 662.2 changes the showing in the Render of `rule-orchestration` and replaces the Criterion of `estimate-orchestration-shows-the-built-case`, whose heading line said only that the name stands in Russian. Case 662.3 adds the check to `guppi/casecheck.py` and creates `estimate-case-check-sends-back-a-summary-without-the-case-name`, read by a test. The `purpose` and `method` of both replaced Estimates speak of a summary and of showings in general, not of where the heading takes its name, so they stand. The check is a reader in code that lands in Work Mode, while the new text of `.claude/agents/case-guppi.md` lands at the render; a `case-guppi` that builds a Case again before the render is sent back once with the line it must write, and nothing it wrote is lost, so the check keeps no old form. `guppi/casecheck.py` is changed by Case 660.2 too, in `in_family` of the clash check at the same `SubagentStop` moment; this Case touches the judgment of the summary only, so the two do not clash, and 662.3 names the case file of 660. The lesson of session 1343 gets no `{addresses}` mark, since its fix is ratified in another session (case 284.2). `insight-case-show-built-case-retyped-by-hand` stays open: its pattern is any line of a Case the main agent writes out by hand, and this Case fixes the heading alone.
>
> The check of the file noted lines of the two replaced Criteria that the new ones do not carry word for word: in `estimate-case-build-writes-the-case` the line on findings of the hook, the line of the summary and the line on findings and changes, and in `estimate-orchestration-shows-the-built-case` the line of the showing and the `－` line on what the main agent writes from the summary. Each is rewritten by intent, to add the `**Case:**` line, the finding on a summary, or the heading taken from that line; the rest of each Criterion is carried whole. It noted too that `then` lines of the three sub-cases share most of their words. That is by intent: the three Estimates check one summary from three sides, `case-guppi` that writes it, the main agent that reads it and the hook that checks it, and each line names its own actor.
>
> The searches this Case rests on. A Grep of `\*\*Built:\*\*` over the repository root, with the glob `!**/decisions/** !**/raw/**`, printed 7 files: `vault/wiki/orchestration.md`, `.claude/agents/case-guppi.md`, `vault/wiki/estimates/estimate-orchestration-shows-the-built-case.md`, `vault/wiki/rules/rule-orchestration.md`, `vault/wiki/estimates/estimate-case-build-writes-the-case.md`, `vault/wiki/rules/rule-case-build.md` and `tests/test_casecheck.py`. The two rendered files follow their rules at the render; the other five enter the Case. A Grep of `summary|Built` over `vault/wiki/estimates/` printed 6 files: the two Estimates above, which enter the Case; `estimate-case-build-answers-what-done-means`, whose line that the summary names the Estimate under each item stays true; `estimate-case-check-sends-back-a-faulty-case`, whose line that an output with no Case heading, a summary among them, is not read as a Case stays true, since the new check reads only the `**Case:**` line of a summary; and `estimate-ask-finds` and `estimate-synthesis-clusters`, which speak of other summaries.

> **problem:**
> The summary of `case-guppi` gives no name for a top-level Case with sub-cases, and the main agent may not read the file, so it shows the Case under a heading of its own words. The person ratifies a Case under a name its file does not hold. The question was where the heading takes its name, whether a script checks it, and what happens to the open Insight.

> **recommend:**
> - **Where the main agent gets the name of the heading**
>   - Recommended: (a) a labelled `**Case:**` line in the summary, right after `**Built:**`, with the id and name as the file's heading holds them, not a Markdown heading.
>   - Answer: agreed, (a).
> - **Whether a script checks that the summary names the top-level Case**
>   - Recommended: (a) the check that runs when `case-guppi` stops sends back a summary whose line is missing or differs from the file's heading.
>   - Answer: agreed, (a).
> - **What happens to the open Insight**
>   - Recommended: (a) leave it open; the `context` names it and says this Case fixes the heading part only.
>   - Answer: agreed, (a).

### Case 662.1 — The summary of case-guppi names the top-level Case

> **given:**
> `rule-case-build`: its Render is the instructions of `case-guppi`, which set the summary.
> **＋** `.claude/agents/case-guppi.md`: the file rendered from `rule-case-build`.
> **＋** `estimate-case-build-writes-the-case`: its Criterion is replaced whole.
> **＋** `rule-case-check`: its `SubagentStop` hook checks the file and the summary.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a Case that `case-guppi` writes.
> **＋** `.claude/skills/grill-me/SKILL.md`: the form of a round.
> **＋** `vault/wiki/case-schema.md`: the form of a Case, read by `case-guppi`.
> **＋** `vault/wiki/ratification.md`: the form of the ledger lines, read by `case-guppi`.
> **＋** `.claude/agents/ask-guppi.md`: the vault query that `case-guppi` runs before a `create` without a `ref`.
> **＋** `.claude/settings.json`: the hooks that `case-guppi` reads for a Case that changes a hook.

> **when:**
> The main agent dispatches `case-guppi` with a Case id, a Frontier item and its source, and the person's words on it; or sends it by `SendMessage` the person's answers to a round, or the person's question or change on a Case it built.
> **＋** Or the hook of `rule-case-check` sends it findings on the file of its Case or on its summary.

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
> **＋** It runs on `model: opus` with `effort: medium`, the tools Read, Grep, Glob, Write and Edit, and `permissionMode: acceptEdits`, so it writes its file with no prompt while the session is in Plan Mode.
> **－** The `**Case:**` line is no Markdown heading, so the hook of `rule-case-check` does not read the summary as a Case.
> **－** It does not write the whole Case again to fix a finding or make a change.
> **－** A later round on the item, a round after a message on a Case it built and a round in Work Mode carry no context.
> **－** The context carries no Case heading, so the hook of `rule-case-check` neither checks nor stores the round as a Case; it judges only the form of the questions of the round, not its context.
> **－** It writes no file but the file of its Case, and no ledger line.

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `` Then answer with the summary alone: a first line `**Built:**` and the path of the file, then one list item per Case and sub-case ``
>   - new: `` Then answer with the summary alone: a first line `**Built:**` and the path of the file, a second line `**Case:**` with the id and the name of the top-level Case as the heading of the file writes them, such as `**Case:** 7 — The cart stands before payment`, for a Case with sub-cases too, since the main agent takes the heading of its showing from it; the line is no Markdown heading, since the hook reads an answer that holds a Case heading as a Case, and the hook sends back a summary whose line is missing or gives another id or name than the heading of the file (case 662.1); then one list item per Case and sub-case ``
>   - old: `` when it sends findings back, fix the lines at fault by `Edit` and answer with the summary again, never by writing the whole Case again (case 645.1) ``
>   - new: `` when it sends findings back on the file, fix the lines at fault by `Edit` and answer with the summary again, never by writing the whole Case again (case 645.1); when it sends a finding back on the summary alone, answer with the summary again and leave the file as it stands (case 662.1) ``
>   - change: `the summary names the top-level Case in a line **Case:** after its Built line (case 662.1)`
> - [ ] update `estimate-case-build-writes-the-case`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the summary carries a line **Case:** with the id and the name of the top-level Case as the file heads it (case 662.1)`
> - [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
> - [ ] read `estimate-case-build-writes-the-case`, by hand in a later session after the render

> **ratification:**
> ```
> - decision[case 662.1][update][rule-case-build]{ref:rule-case-build}
> - decision[case 662.1][update][estimate-case-build-writes-the-case]{ref:rule-case-build}
> ```

### Case 662.2 — The heading of a showing takes the name from the summary

> **given:**
> `rule-orchestration`: its Render sets what the main agent shows of a built Case.
> **＋** `vault/wiki/orchestration.md`: the page rendered from `rule-orchestration`.
> **＋** `estimate-orchestration-shows-the-built-case`: its Criterion is replaced whole.
> **＋** `rule-case-build`: it sets the summary that the main agent reads.
> **＋** `rule-case-check`: its checks of a built Case and of a showing.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a Case that the main agent sends, under the folder `cases/`.
> **＋** `cases/`: the folder of the files of built Cases, which the main agent does not edit.
> **＋** `/wait-what`: the command by which the person asks for a plain explanation.
> **＋** `.claude/skills/wait-what/SKILL.md`: the skill by which the main agent explains in plain words.
> **＋** `.claude/skills/grill-me/SKILL.md`: the form of a round that the main agent shows.

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
> **＋** An item that needs no decision the main agent closes alone, with no dispatch; it dispatches `ask-guppi` only at pre-spec, one run per top-level Case at its first run, never to build a Case, and asks a run again only to confirm its own findings.
> **－** The main agent writes the heading, the list, the `ratification` and the question on another Case from the summary, and does not read the file of the Case.
> **－** The heading carries no name of the main agent's own and not the words of the Frontier item.
> **－** The main agent writes no context of its own before the first question of a round.
> **－** The main agent writes no `given`, `when`, `then` or `tasks` of a built Case into the chat.
> **－** A deferred decision in the short form is written by the main agent in English in the chat, with no dispatch and no file.

> **tasks:**
> - [ ] update `rule-orchestration`
>   - old: `` `case-guppi` answers with a summary of it — the path, then for each Case and sub-case its id ``
>   - new: `` `case-guppi` answers with a summary of it — the path, a line `**Case:**` with the id and the name of the top-level Case as the heading of its file writes them, then for each Case and sub-case its id ``
>   - old: `in the same reply it writes the heading of the top-level Case, its name in {{chat_lang}}, and under it`
>   - new: `` in the same reply it writes the heading of the top-level Case, its id and its name in {{chat_lang}} translated from the `**Case:**` line of the summary, never a name of its own or the words of the Frontier item (case 662.2), and under it ``
>   - change: `the heading of a showing takes the name of the top-level Case from the Case line of the summary (case 662.2)`
> - [ ] update `estimate-orchestration-shows-the-built-case`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the heading of a showing is the id and the name of the Case line of the summary, translated (case 662.2)`
> - [ ] `uv run guppi render`: `vault/wiki/orchestration.md`
> - [ ] read `estimate-orchestration-shows-the-built-case`, by hand at the close of a later session after the render

> **ratification:**
> ```
> - decision[case 662.2][update][rule-orchestration]{ref:rule-orchestration}
> - decision[case 662.2][update][estimate-orchestration-shows-the-built-case]{ref:rule-orchestration}
> ```

### Case 662.3 — The check of case-guppi sends back a summary that does not name its Case

> **given:**
> `estimate-case-check-sends-back-a-summary-without-the-case-name`: the new check of the line `**Case:**` of a summary.
> **＋** `rule-case-check`: the rule of the hook, whose Purpose names what it prevents.
> **＋** `guppi/casecheck.py`: the `SubagentStop` hook `guppi casecheck --subagent`.
> **＋** `tests/test_casecheck.py`: the tests of the hook.
> **＋** `vault/raw/2026-10-05/1616/cases/case-660.md`: Case 660.2 changes `in_family` of the same module, at the same hook.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a Case whose heading the check reads.
> **＋** `.claude/settings.json`: it registers the hook on `SubagentStop`.

> **when:**
> `case-guppi` stops after it wrote or edited a file `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and the `SubagentStop` hook `guppi casecheck --subagent` of `guppi/casecheck.py`, registered in `.claude/settings.json`, reads its newest output: a summary whose first line that is not blank opens with `**Built:**`.

> **then:**
> A summary with no line `**Case:**` for the top-level Case of a file it wrote, or with one whose id and name differ from the heading `## Case N — name` of that file, gets a finding that names the file and the line to write, and the hook exits 2.
> **＋** A summary whose `**Case:**` line gives the same id and the same name as the heading of each such file, trailing spaces aside, gets no finding on its line.
> **＋** A finding on the summary is sent back in the same exit 2 as the findings on the file.
> **＋** A summary sent back once is sent back again when the heading of its file has changed since, even if an earlier output holds its text.
> **－** A summary whose text an earlier output of the subagent already holds, trailing spaces aside, is not sent back again for its line while the heading of its file is the same as when it was sent back.
> **－** A round, a `**Fact:**` answer, and an answer with no file written are not judged for the line.

> **tasks:**
> - [ ] create `estimate-case-check-sends-back-a-summary-without-the-case-name`
>   - ref: `rule-case-check`
>   - kind: `QA`
>   - purpose: `Whether the check of case-guppi sends back a summary that does not name the top-level Case as its file heads it`
>   - method: `uv run pytest tests/test_casecheck.py -k summary_names_the_case`
>   - tags: `[hooks, harness, workflow]`
> - [ ] update `rule-case-check`
>   - old: `` outside the list under its heading and its `ratification` (case 611); the Case reaches ``
>   - new: `` outside the list under its heading and its `ratification` (case 611), and a summary of `case-guppi` from reaching the main agent without the id and the name of the Case it built (case 662.3); the Case reaches ``
>   - set:
>     ```
>     purpose: "Prevents a Case from being shown to the person in a form the checks of pre-spec refuse, or with other given, when, then, tasks or ratification than the ones that passed them, a round of case-guppi from reaching the main agent with a question out of the form of the grill-me template, a round of case-guppi from being shown after a text of the main agent's own, a Case from being shown with a text of the main agent's own outside the list under its heading and its ratification, and a summary of case-guppi from reaching the main agent without the id and the name of the Case it built"
>     ```
>   - change: `the SubagentStop check sends back a summary whose Case line is missing or differs from the heading of the file (case 662.3)`
> - [ ] `guppi/casecheck.py`: in `subagent`, when the subagent wrote a file of `cases/` and its newest output opens with `**Built:**`, one function compares the `**Case:**` lines of that output with the top-level heading of each written file, read by `CASE_HEADING` of `guppi/materialize.py`, compares the id and the name of the line with those of the heading, not the whole line, and gives a finding for each one missing or different; the guard against a loop keys on the text of the summary, trailing spaces aside, and the heading of the file together, so an earlier summary with the same text gives no finding again only while the heading stands as it was; the findings join those of the files in one `send_back`; the module docstring describes the check.
> - [ ] `tests/test_casecheck.py`: tests named `summary_names_the_case` for each line of the `then`; the helpers that write a summary — the one beside `case_path` and `built` — give it its `**Case:**` line, so the tests of a passing file still pass.
> - [ ] read `estimate-case-check-sends-back-a-summary-without-the-case-name`, at the `/hi` of a later session

> **ratification:**
> ```
> - decision[case 662.3][create][estimate-case-check-sends-back-a-summary-without-the-case-name]{ref:rule-case-check}{tags:hooks,harness,workflow}
> - decision[case 662.3][update][rule-case-check]{ref:rule-case-check}
> ```
