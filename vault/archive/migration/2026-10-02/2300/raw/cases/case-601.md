## Case 601 — The check of case-guppi sends back a round whose questions are out of the grill-me form

> **context:**
> When `case-guppi` answers with a round of questions, each question opens with a fixed title line: the question mark, the number in bold, a dash, the title in bold and a colon. The rest of the question follows the template of `.claude/skills/grill-me/SKILL.md`: a `**Now:**` line, the `**Options:**` label alone on its line, options marked with a blue diamond, each with an `**After:**` item, and the recommended answer on an arrow line. Today no script reads the form of a round. The `SubagentStop` check of `rule-case-check`, `uv run guppi casecheck --subagent`, checks only Cases. It takes as the answer the newest output of the agent that holds a Case heading. When the agent's newest output is a round and an earlier output in the same transcript holds a Case, it checks and stores that earlier Case again. Two checks find the questions of a round by the `QUESTION_LINE` pattern of `guppi/casecheck.py`, which requires the colon after the bold title: `round_titles`, for the titles that `recommend` must hold, and `is_round`, for the end-of-reply check of how a reply that shows a round opens. In session 2049 the round on Case 599 opened its only question with the bold title and no colon. Neither check saw a question there, and nothing sent the round back. The main agent showed it as the answer held it. Two hand readings failed on that line: `estimate-skill-grill-me-asks-in-rounds` (ledger line 24 of session 2049) and `estimate-orchestration-shows-the-built-case` (ledger line 30). The same session recorded the cause as `lesson-case-check-question-line-without-colon-unseen`.
>
> Case 601.1 changes `is_round` into the one test of a round: a line that opens with the question mark, no Case heading, and no `**Fact:**` first line. It adds a check of the form of each question on `SubagentStop`, which reads the title line by `QUESTION_LINE` and checks the fixed labels. A round out of form goes back to `case-guppi` before the main agent sees it. A round sent back once and returned with the same text is not sent back again; the agent's own transcript tells the check this, and nothing is stored. Case 601.2 replaces the Criterion of `estimate-case-check-sends-back-a-faulty-case`, whose last line says that an answer with no Case heading is not checked. Case 601.3 replaces the Criterion of `estimate-case-build-writes-the-case`, whose line says that the hook neither checks nor stores a round. Case 601.4 replaces the Criterion of `estimate-case-check-refuses-text-before-a-round`, which defines a round by the full title line. Its new line names `is_round` as the one test and leaves the parts of that test to 601.1 (case 601, the answer on the single test of a round). Case 601.5 replaces the Criterion of `estimate-case-check-requires-each-question-of-the-rounds`, so that only a round in form gives titles. Otherwise a round the hook sent back, still in the transcript, would require an item for a question the person never saw (case 601, the answer on which rounds give the titles). Each replaced Criterion is carried whole, with only the named lines changed. The `purpose` and `method` of 601.5 state the old promise and are set anew. Those of the other replaced Estimates speak of a Case, the agent's build, or the opening of a reply, not of a changed line, and they stand.
>
> The check of this answer gave notes. Each note that a line of a Criterion is not carried names a line this Case changes on purpose, as said above. Several notes say that a `then` line of 601.3, 601.4 or 601.5 shares most of its words with a line of 601.1. Each such pair states a different thing. One line of each pair is the old line its Estimate carries, or the line of 601.4 that names `is_round`. The other is a line of 601.1 on the form of a question or on what its check stores. So both lines of each pair stand.
>
> The two failed Estimates stay `failed` with their Criteria unchanged, by the person's answers in the first round and at pre-spec. Their promise of the title line is sound, and the agent broke it. The frame of the librarian, `.claude/agents/librarian-guppi.md`, lists each `failed` Estimate under Readings due and under the `Cases` list of Next session in the brief. So both come back as Cases lines at the next `/hi` and close there by a reading, once the check is live. A Grep of `failed` over `guppi/prespec.py` printed nothing, so no check requires this Case to name them. By the person's answer at pre-spec, Case 605 places `lesson-case-check-question-line-without-colon-unseen` under `insight-case-form-chat-form-read-by-no-script`, its `addressed_by` naming `decision-case-601.1`. The lesson line stands in the ledger of session 2049, not this one, so no decision line here carries `{addresses}` (`ratification.md`). `estimate-case-check-exits-2-on-an-error` stands: the new check runs inside the `--subagent` run, whose own error still exits 0. The other Estimates of `rule-case-check` speak of an answer that holds a Case. The new Estimate has a `ref`, so the vault query was not run. The slug `estimate-case-check-sends-back-a-faulty-round` is free: a Glob of `vault/**/*faulty-round*.md` found no file.
>
> Frame checks:
> - A Grep of `no Case heading` over `vault/wiki/rules/`, `vault/wiki/estimates/`, `vault/wiki/entities/`, `vault/wiki/*.md`, `.claude/` and `guppi/` printed these files:
>   - `orchestration.md`, `rule-orchestration.md`, `rule-case-build.md`, `.claude/agents/case-guppi.md`, `guppi/casecheck.py`
>   - `estimate-case-check-sends-back-a-faulty-case.md`, `estimate-case-check-requires-each-question-of-the-rounds.md`, `estimate-case-check-refuses-text-before-a-round.md`, `estimate-case-build-writes-the-case.md`, `estimate-orchestration-shows-the-built-case.md`, `estimate-orchestration-forwards-a-discussion-question.md`
> - The hits read, and what becomes of them:
>   - The four Estimates of 601.2 to 601.5 are replaced.
>   - The docstring of `guppi/casecheck.py` is changed by 601.1, 601.4 and 601.5, each in its own sentences.
>   - `orchestration.md`, `rule-orchestration` and the two Estimates of `rule-orchestration` say that an answer with no Case heading and no `**Fact:**` line is a round. That stays true.
>   - `rule-case-build` and `case-guppi.md` say that a round carries no Case heading, and that a hook sends back a faulty Case for the agent to answer whole again. Both stay true. The reason the new check prints tells the agent to answer with the round whole again.
> - A Grep of `SubagentStop` over `vault/wiki/`, `.claude/`, `guppi/` and `tests/` printed 52 files, 24 of them outside `decisions/`. In `.claude/settings.json` the one hook on that event is `uv run guppi casecheck --subagent`, the hook this Case changes. Outside `decisions/`, History, `log.md`, `brief.md` and `backlog.md`, the other hits stand:
>   - The rules and Estimates name the `SubagentStop` check of a Case, its registration, or the case file it writes.
>   - The three lessons record what the payload carries, the double fire around a handback, and how a `systemMessage` shows.
>   - The two Insights record that the form of a Case is checked on that event.
>
>   None sets a form for a round.
> - A Grep of `estimate-case-check-sends-back-a-faulty-case|estimate-case-build-writes-the-case` over `vault/wiki/`, `guppi/`, `tests/` and `.claude/` printed 65 files. Outside `decisions/`, `brief.md` and `log.md` the hits are `rule-case-check.md` and `rule-case-build.md`, in their `estimates` fields, and `estimate-skill-grill-me-asks-in-rounds.md`, in a History line.
>
> Not done:
> - The main agent's showing of a round gets no check of its own. It stays with the hand reading of `estimate-orchestration-shows-the-built-case`.
> - A round that passes because it came back unchanged gives no titles to `recommend`.
> - The check of a Case still re-reads an earlier Case when the agent's newest output is a round. In this session the second round on Case 601 was sent back once, because the earlier Case 601 held no item for that round's titles. No question put this to the person. It is a fault for a later Case on `estimate-case-check-sends-back-a-faulty-case`, and this Case leaves that reading as it is.

> **problem:**
> No script reads the form of a round of `case-guppi`. A question whose title line lacks the colon is no question to the checks that look for questions. A round out of the grill-me form reaches the main agent and the person, and is found only by a hand reading after the session.

> **recommend:**
> - **Where should a question title line without the colon be caught?**
>   - Recommended: (a) send the round back to `case-guppi`. The `SubagentStop` check also reads an answer that holds no Case and does not open with `**Fact:**`. A line in it that opens with the question mark but is not a full title line sends it back, and the reason names the line. A round sent back once and returned with the same text is not sent back again.
>   - Answer: agreed with the recommendation, (a).
> - **How much of each question should the new catch read?**
>   - Recommended: (a) the title line only. The rest of each question's form stays with the hand reading of `estimate-skill-grill-me-asks-in-rounds`.
>   - Answer: (b) the title line and the fixed labels. Each question needs one `**Now:**` line, the `**Options:**` label alone on its line, at least one option marked with the diamond and with an `**After:**` item, and an arrow line.
> - **Should the main agent's showing of a round get a check of its own?**
>   - Recommended: (a) no. The answer is checked before the main agent sees it, and `estimate-orchestration-shows-the-built-case` keeps reading the showing by hand.
>   - Answer: agreed with the recommendation, (a).
> - **What should happen to the two failed readings?**
>   - Recommended: (a) leave them failed and read them again in a later session, once the new catch is live. Their Criteria stay as they are.
>   - Answer: agreed with the recommendation, (a).
> - **How should done be checked for the new catch?**
>   - Recommended: (a) a new Estimate for the round, `estimate-case-check-sends-back-a-faulty-round`, and the Criterion of `estimate-case-check-sends-back-a-faulty-case` replaced so that its last line no longer says that an answer without a Case heading goes unchecked. That makes two sub-cases.
>   - Answer: agreed with the recommendation, (a).
> - **Should the two checks that already find questions also see a title line without the colon?**
>   - Recommended: (a) keep them as they are. Both keep the full title line, and their Estimates stay untouched.
>   - Answer: agreed with the recommendation, (a). Replaced in part by the two questions below, after pre-spec showed that the new check and `is_round` cannot share one test as written.
> - **How should the catch know a round was already sent back?**
>   - Recommended: (a) from the agent's own transcript. A faulty round is not sent back when an earlier output in the transcript holds the same text. Nothing is stored, and the check runs with or without a plan file.
>   - Answer: agreed with the recommendation, (a).
> - **Which single test should decide that an answer is a round?**
>   - Recommended: (a) one test, by the question mark at the start of a line. One function decides that an answer is a round: no Case, no `**Fact:**` opening, and a line that opens with the question mark. The new check and the end-of-reply check both import it, and the pass condition of `estimate-case-check-refuses-text-before-a-round` is rewritten in one more sub-case.
>   - Answer: agreed with the recommendation, (a).
> - **Which rounds should give the titles that the Case's `recommend` must hold?**
>   - Recommended: (a) only rounds the new check finds in form. A round sent back gives no titles, and the pass condition of `estimate-case-check-requires-each-question-of-the-rounds` is rewritten in one more sub-case.
>   - Answer: agreed with the recommendation, (a).

### Case 601.1 — The SubagentStop check sends back a round with a question out of form

> **given:**
> `rule-case-check` — the rule of the check, its `purpose` and its `Purpose` section changed
> **＋** `estimate-case-check-sends-back-a-faulty-round` — the new promise
> **＋** `guppi/casecheck.py` and `tests/test_casecheck.py` — the check on `SubagentStop`, `is_round`, the one test of a round, `QUESTION_LINE`, and their tests
> **＋** `agent_transcript_path` of the `SubagentStop` payload — the transcript of `case-guppi`, whose outputs the check reads
> **＋** `.claude/skills/grill-me/SKILL.md` — the question template the check reads; unchanged
> **＋** `.claude/agents/case-guppi.md` — the agent whose rounds are judged; unchanged
> **＋** `.claude/settings.json` — registers `uv run guppi casecheck --subagent`, the one hook on `SubagentStop`; unchanged

> **when:**
> `SubagentStop` fires when `case-guppi` answers, and `uv run guppi casecheck --subagent` reads its newest output in `agent_transcript_path`: a text, or the `message` of a `SubagentHandback` call, whichever stands later.

> **then:**
> `uv run guppi casecheck --subagent` takes that output as a round when `is_round` of `guppi/casecheck.py`, the one test of a round that the `Stop` run also imports, finds it one. That means three things hold: it holds no Case heading; its first line that is not blank is not `**Fact:**`; and one of its lines opens with the mark `❓`, with the indent of each line set aside.
> **＋** Each line that opens with `❓` opens a question, and the question runs to the next such line or to the end of the output. The text before the first question, the `**Context:**` paragraph, is not judged.
> **＋** A question is out of form when its first line does not match the title line `❓ **Q<n>** - **<title>**:` of `.claude/skills/grill-me/SKILL.md`, judged by `QUESTION_LINE` of `guppi/casecheck.py`.
> **＋** A question is out of form when it holds no line that opens with `**Now:**`, or no line that holds `**Options:**` and nothing else.
> **＋** A question is out of form when it holds no line that opens with `➡️`, or when none of its lines that open with `🔹` has a line that opens with `- **After:**` after it, before the next line that opens with `🔹` or `➡️`.
> **＋** A round with a question out of form exits 2. Its stderr names each such question by its first line and each part it misses, and tells `case-guppi` to answer with the round whole again, and `case-guppi` answers again.
> **＋** These findings stand beside those of the check of a Case in the same run, which keeps its own reading of the answer, and one exit 2 carries both.
> **－** A round out of form is not sent back again when an earlier output of `case-guppi` in `agent_transcript_path` holds the same text, trailing spaces aside.
> **－** A round in form gives no finding and prints nothing of its own.
> **－** These are not judged here: an output with a Case heading, a `**Fact:**` answer, an output with no line that opens with `❓`, an answer of another agent, and an `agent_transcript_path` that cannot be read.
> **－** The check of the form stores nothing and writes no file, whether or not the session has a plan file.
> **－** A round as the main agent shows it in the chat is not judged here.

> **tasks:**
> - [ ] update `rule-case-check`
>   - set: `{purpose: "Prevents a Case from being shown to the person in a form the checks of pre-spec refuse, or with other given, when, then, tasks or ratification than the ones that passed them, a round of case-guppi from reaching the main agent with a question out of the form of the grill-me template, and a round of case-guppi from being shown after a text of the main agent's own"}`
>   - old: `` and a round of `case-guppi` from being shown after a text of the main agent's own (case 562); ``
>   - new: `` a round of `case-guppi` from reaching the main agent with a question out of the form of the template of `.claude/skills/grill-me/SKILL.md` (case 601.1), and a round of `case-guppi` from being shown after a text of the main agent's own (case 562); ``
>   - old: `The checks are the ones of pre-spec and of the Spec hook, imported, not copied ([[rule-one-judgment-one-implementation]]);`
>   - new: `` The checks of a Case are the ones of pre-spec and of the Spec hook, imported, not copied ([[rule-one-judgment-one-implementation]]), and every check of a round knows a round by one test and its title line by one pattern (case 601.1); ``
>   - change: `the SubagentStop check sends back a round of case-guppi with a question out of the grill-me form, once per text; one test of a round serves every check of a round (case 601.1)`
> - [ ] create `estimate-case-check-sends-back-a-faulty-round`
>   - type: `estimate`
>   - ref: `rule-case-check`
>   - kind: `QA`
>   - purpose: `Whether the SubagentStop check sends back to case-guppi a round whose question has a title line out of the grill-me form or misses a fixed label, once per text, and leaves a round in form, a Case and a Fact answer alone`
>   - method: `uv run pytest tests/test_casecheck.py -k round_form over a temp agent transcript: a round in form, a title line without the colon, a question with no Now line, no lone Options label, no option with an After item and no arrow line, the same faulty round given twice, a Fact answer, an answer with a Case, an unreadable transcript; then by hand the first round the hook sends back live, its stderr and the round case-guppi gave again`
>   - tags: `[hooks, harness, workflow]`
> - [ ] `guppi/casecheck.py`: `is_round` becomes the one test of a round: no Case heading, a first line that is not blank and is not `**Fact:**`, and a line that opens with `❓`, the indent set aside. A new function, importing it, gives the findings of each question of a round out of form, its title line judged by `QUESTION_LINE`. `subagent` runs it on the newest output of `case-guppi`, read by `outputs`. When that output is a round with findings, and no earlier output of the transcript holds the same text, the findings join those of the check of a Case, and the run exits 2. The check of the form stores nothing. The module docstring describes the check. Its sentence that an answer with no Case heading, where no earlier output holds one either, is not checked or stored gains: such an output is still judged as a round by the check of the form, which stores nothing.
> - [ ] `tests/test_casecheck.py`: the cases of the `method` of `estimate-case-check-sends-back-a-faulty-round`, each named `round_form`.
> - [ ] `uv run pytest tests/test_casecheck.py`
> - [ ] read `estimate-case-check-sends-back-a-faulty-round`

> **ratification:**
> ```
> - decision[case 601.1][update][rule-case-check]{ref:rule-case-check}
> - decision[case 601.1][create][estimate-case-check-sends-back-a-faulty-round]{ref:rule-case-check}{tags:hooks,harness,workflow}
> ```

### Case 601.2 — The promise of the check of a Case leaves the round to its own Estimate

> **given:**
> `estimate-case-check-sends-back-a-faulty-case` — the promise of the check of a Case, its Criterion replaced whole
> **＋** `estimate-case-check-sends-back-a-faulty-round` — the promise of 601.1, which the changed lines name
> **＋** `guppi/casecheck.py`, `guppi/ratified.py` and `guppi/prespec.py` — the check and the readings it imports; unchanged by this sub-case
> **＋** `agent_transcript_path` and `last_assistant_message` of the `SubagentStop` payload — the outputs of `case-guppi` the check reads
> **＋** `<plan>.checked.json` — the store beside the plan file of the session
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md` — the file of a Case that passed

> **when:**
> `SubagentStop` fires when `case-guppi` answers; its payload carries `last_assistant_message`, `agent_transcript_path` and `stop_hook_active`, and it may fire twice after one message to the subagent, the second time after a `SubagentHandback` call, with `stop_hook_active` true though no hook exited 2.

> **then:**
> `uv run guppi casecheck --subagent` takes as the answer the newest output of the subagent in `agent_transcript_path` that holds a Case heading — the `message` input of a `SubagentHandback` tool call or the text of an assistant message, whichever stands later — or `last_assistant_message` when `agent_transcript_path` is not readable or holds no such output.
> **＋** It reads each Case of the answer in the chat form, by the functions of `guppi/ratified.py`, builds each Case's section of the Spec in memory, as the Spec hook writes it, and runs `judge` of `guppi/prespec.py` over them, the decision lines of the `ratification` fence standing for the ledger.
> **＋** The categories whose schema rule the session changes, whose `create` and `defer` items `judge` does not judge by their keys, it takes from the decision lines of the `ratification` fences and of the session's window.
> **＋** It checks the chat form besides: the sections in the order of the schema, none missing that the schema requires, and a `ratification` that holds one untagged fence of ledger lines and nothing else.
> **＋** Each Case of the answer is stored, its text as the answer holds it, with its findings and the time of the store, in `<plan>.checked.json` beside the plan file of the session.
> **＋** When no Case of the answer has findings, it writes the Cases of the answer, as the store holds their text, into `raw/<date>/<hi HHMM>/cases/case-<N>.md`, N the id of the top-level Case: the file is replaced whole when the answer holds the top-level Case, and only the section of a sub-case is replaced when the answer holds that sub-case alone.
> **＋** A finding exits 2 with the findings on stderr, each naming its Case, and `case-guppi` answers again, whatever `stop_hook_active` says.
> **－** An answer with a finding writes no file, and a finding for a Case whose text the store already holds with findings is stored again and exits 0, so an unchanged answer is not sent back twice.
> **－** An answer of another agent, and one whose outputs hold no Case heading, get none of these checks of a Case and are not stored or written. A session with no plan file is not sent back for a fault of a Case.
> **－** The form of the questions of a round is the promise of `estimate-case-check-sends-back-a-faulty-round`, not of this one.

> **tasks:**
> - [ ] update `estimate-case-check-sends-back-a-faulty-case`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — an answer whose outputs hold no Case heading gets none of the checks of a Case, and the form of a round is the promise of estimate-case-check-sends-back-a-faulty-round (case 601.2)`
> - [ ] read `estimate-case-check-sends-back-a-faulty-case`

> **ratification:**
> ```
> - decision[case 601.2][update][estimate-case-check-sends-back-a-faulty-case]{ref:rule-case-check}
> ```

### Case 601.3 — The promise of case-guppi says the hook judges the form of its questions

> **given:**
> `estimate-case-build-writes-the-case` — the promise of `case-guppi`, its Criterion replaced whole
> **＋** `.claude/agents/case-guppi.md` — the agent, rendered from `rule-case-build`; unchanged
> **＋** `.claude/skills/grill-me/SKILL.md` — the skill the agent loads by its `skills` field; unchanged
> **＋** `vault/wiki/case-schema.md` and `vault/wiki/ratification.md` — the texts the agent reads whole; unchanged
> **＋** `.claude/agents/ask-guppi.md` — the vault query the agent runs itself; unchanged
> **＋** `.claude/settings.json` — the hooks the agent reads for a Case that changes a hook; unchanged
> **＋** `rule-case-check` — the hook that judges the form of the questions of a round, by Case 601.1

> **when:**
> The main agent dispatches `case-guppi` with a Case id, a Frontier item and its source, and the person's words on it; or sends it by `SendMessage` the person's answers to a round, or the person's question or change on a Case it built.

> **then:**
> `case-guppi` starts with `.claude/skills/grill-me/SKILL.md` in its context by `skills: [grill-me]` in `.claude/agents/case-guppi.md`, and reads `vault/wiki/case-schema.md` and `vault/wiki/ratification.md` whole before it answers.
> **＋** Before a `create` without a `ref`, it runs the vault query of `.claude/agents/ask-guppi.md` itself, and the `context` of the Case gives the answer.
> **＋** It reads each page and file the `given` names, the Criterion of each Estimate such a page lists, and, for a Case that adds or changes a hook, the hooks on the same event in `.claude/settings.json`; each contradiction is fixed in the Case, or the `context` says why it stands.
> **＋** While a fork is open — the bound, the alternative, the promise, the split, the exceptions or what is left not done — its answer is a round of questions in the form of `.claude/skills/grill-me/SKILL.md`, in English, with no Case heading and nothing else but the context of a first round.
> **＋** The first round on an item opens, before its first question, with one prose paragraph under the label `**Context:**`: what the item is about, what the thing does today and where it goes wrong, and what the round decides — a sentence per part where one is enough, a part with nothing to say left out.
> **＋** When no fork is open, its answer is the Case whole in English in the chat form of `vault/wiki/case-schema.md`, its ledger lines in the form of `vault/wiki/ratification.md`, from the heading to the fence of `ratification`, and nothing else.
> **＋** A round may come at the first answer on an item, after a message on a Case it built, and in Work Mode when a ratified Case is built again.
> **＋** It runs on `model: opus` with `effort: medium` and the tools Read, Grep and Glob.
> **－** A later round on the item, a round after a message on a Case it built and a round in Work Mode carry no context.
> **－** The context carries no Case heading, so the hook of `rule-case-check` neither checks nor stores the round as a Case; it judges only the form of the questions of the round, not its context.
> **－** It writes no file and no ledger line.

> **tasks:**
> - [ ] update `estimate-case-build-writes-the-case`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the hook of rule-case-check judges the form of the questions of a round, not its context, and stores nothing of it (case 601.3)`
> - [ ] read `estimate-case-build-writes-the-case`

> **ratification:**
> ```
> - decision[case 601.3][update][estimate-case-build-writes-the-case]{ref:rule-case-build}
> ```

### Case 601.4 — The end-of-reply check knows a round by the one test of a round

> **given:**
> `estimate-case-check-refuses-text-before-a-round` — the promise of the check of how a reply that shows a round opens, its Criterion replaced whole
> **＋** `guppi/casecheck.py` and `tests/test_casecheck.py` — the `Stop` run, `is_round` as 601.1 sets it, and their tests
> **＋** `guppi/ledger.py` and `guppi/prespec.py` — the function that names the person's message or a returned answer, and `window`, which reads the `prespec` line of the session's event log
> **＋** `/hi` — opens the working session; its `hi` line in the event log bounds the window
> **＋** `.claude/skills/grill-me/SKILL.md` — the question template; unchanged
> **＋** `rule-prespec` — sets the text of the main agent in the loop after the findings of `/pre-spec`
> **＋** `.claude/skills/wait-what/SKILL.md` — the re-pitch, a turn with no round

> **when:**
> `Stop` fires after a reply of the main agent, and `uv run guppi casecheck` runs on it.

> **then:**
> When the turn of the reply, the records after the last `user` record that the function of `guppi/ledger.py` names the person's message or a returned answer, holds a round of `case-guppi`, `uv run guppi casecheck` judges how the reply opens. A round is a text that `case-guppi` gives back to an `Agent` or `SendMessage` call and that `is_round` of `guppi/casecheck.py`, the one test of a round, finds one.
> **＋** While the session's event log holds no `prespec` line of this session after its `hi`, it exits 2 when the main agent wrote text in the turn before its last tool call.
> **＋** It exits 2 when the first line of the reply that is not blank opens neither with `❓ ` nor with a bold label that ends in a colon, the label of the Context paragraph as it stands translated.
> **＋** Its reason on stderr quotes the text that stands before the round and tells the agent to show the round again, opening with its Context paragraph or its first question, with nothing before it.
> **＋** Text after the last question and one horizontal rule is not judged.
> **＋** The check runs in the same `Stop` run as the comparison of shown Cases, and a reply that both refuse gives both reasons.
> **－** Once the session's event log holds a `prespec` line of this session after its `hi`, text before the last tool call of the turn is not judged, and a reply of the loop after the findings of `/pre-spec` is judged only by its first line; in that loop each answer of a `case-guppi` comes back in a turn of its own, and the text the main agent writes there is set by `rule-prespec`.
> **－** A turn with no round of `case-guppi` is not judged: the main agent's own questions in the report of `/pre-spec`, at `/hi` or at a stop of Work Mode, a `**Fact:**` answer shown with the question that stood open, and a re-pitch by `.claude/skills/wait-what/SKILL.md`.
> **－** On the re-fire (`stop_hook_active`) it exits 0, so the round shown again after a refusal is not judged again.
> **－** It stores nothing and writes no file.

> **tasks:**
> - [ ] update `estimate-case-check-refuses-text-before-a-round`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a round is known by is_round, the one test of a round (case 601.4)`
> - [ ] `guppi/casecheck.py`: the docstring paragraph on how a round opens says that a round is known by `is_round`, the one test of a round, not by a `QUESTION_LINE` match.
> - [ ] `tests/test_casecheck.py`: a round whose only question lacks the colon after its title is a round to the `Stop` run, and a reply that shows it after a text of the main agent's own is refused; the test is named `round`.
> - [ ] `uv run pytest tests/test_casecheck.py -k round`
> - [ ] read `estimate-case-check-refuses-text-before-a-round`

> **ratification:**
> ```
> - decision[case 601.4][update][estimate-case-check-refuses-text-before-a-round]{ref:rule-case-check}
> ```

### Case 601.5 — Only a round in form gives the titles that recommend must hold

> **given:**
> `estimate-case-check-requires-each-question-of-the-rounds` — the promise of the check of the titles of `recommend`, its Criterion, `purpose` and `method` replaced
> **＋** `guppi/casecheck.py` and `tests/test_casecheck.py` — `round_titles`, the function of the form of a round that 601.1 adds, and their tests
> **＋** `agent_transcript_path` of the `SubagentStop` payload — the transcript of `case-guppi`, whose earlier outputs hold its rounds
> **＋** `.claude/skills/grill-me/SKILL.md` — the question template; unchanged

> **when:**
> `SubagentStop` fires when `case-guppi` answers with a Case, and `agent_transcript_path` holds the agent's earlier outputs with no Case heading, which are its rounds of questions on that Case.

> **then:**
> `uv run guppi casecheck --subagent` takes the title of each question of those rounds from its line `❓ **Q<n>** - **<title>**:`, the title line of the template of `.claude/skills/grill-me/SKILL.md`.
> **＋** It takes titles only from a round that the function of `guppi/casecheck.py` that judges the form of a round finds in form, the function the check of 601.1 sends a round back by; a round out of form gives no title.
> **＋** A title that no item of a `recommend` of the top-level Case or of its sub-cases in the answer opens with, in bold, is a finding of the top-level Case that names the title, sent back and stored as any other finding.
> **－** An answer with no earlier round gives no such finding.
> **－** A title asked in more than one round is looked for once.
> **－** The words of an item after its title are not judged.
> **－** A round out of form that came back unchanged, passed the check of its form and was shown gives no title either.

> **tasks:**
> - [ ] update `estimate-case-check-requires-each-question-of-the-rounds`
>   - set: `{status: pending, purpose: "Whether the check of each answer of case-guppi sends back a Case whose recommend misses the title of a question of its rounds in the grill-me form", method: "pytest tests/test_casecheck.py -k rounds over a temp agent transcript: a round and a Case whose recommend holds every title, one that misses a title, a title asked in two rounds, a round out of form whose titles are not required, an answer with no round; then by hand the first Case the hook sends back for a missing title"}`
>   - change: `the Criterion replaced whole — only a round in form gives the titles recommend must hold (case 601.5)`
> - [ ] `guppi/casecheck.py`: `round_titles` skips an output that the function of the form of a round finds out of form; its docstring and the module docstring say so.
> - [ ] `tests/test_casecheck.py`: a round sent back for its form, followed by a round in form with a changed title, requires only the titles of the round in form; the test is named `rounds`.
> - [ ] `uv run pytest tests/test_casecheck.py -k rounds`
> - [ ] read `estimate-case-check-requires-each-question-of-the-rounds`

> **ratification:**
> ```
> - decision[case 601.5][update][estimate-case-check-requires-each-question-of-the-rounds]{ref:rule-case-check}
> ```
