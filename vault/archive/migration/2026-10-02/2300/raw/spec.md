<!-- approved 00:55:56 · session 92f1ae46 -->

# Spec — session 2300, 2026-10-02

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

```then
create:
- slug: estimate-case-check-sends-back-a-faulty-round
  type: estimate
  ref: rule-case-check
  kind: QA
  purpose: Whether the SubagentStop check sends back to case-guppi a round whose question has a title line out of the grill-me form or misses a fixed label, once per text, and leaves a round in form, a Case and a Fact answer alone
  method: 'uv run pytest tests/test_casecheck.py -k round_form over a temp agent transcript: a round in form, a title line without the colon, a question with no Now line, no lone Options label, no option with an After item and no arrow line, the same faulty round given twice, a Fact answer, an answer with a Case, an unreadable transcript; then by hand the first round the hook sends back live, its stderr and the round case-guppi gave again'
  tags:
  - hooks
  - harness
  - workflow
update:
- slug: rule-case-check
  set:
    purpose: Prevents a Case from being shown to the person in a form the checks of pre-spec refuse, or with other given, when, then, tasks or ratification than the ones that passed them, a round of case-guppi from reaching the main agent with a question out of the form of the grill-me template, and a round of case-guppi from being shown after a text of the main agent's own
  replace:
  - old: and a round of `case-guppi` from being shown after a text of the main agent's own (case 562);
    new: a round of `case-guppi` from reaching the main agent with a question out of the form of the template of `.claude/skills/grill-me/SKILL.md` (case 601.1), and a round of `case-guppi` from being shown after a text of the main agent's own (case 562);
  - old: The checks are the ones of pre-spec and of the Spec hook, imported, not copied ([[rule-one-judgment-one-implementation]]);
    new: The checks of a Case are the ones of pre-spec and of the Spec hook, imported, not copied ([[rule-one-judgment-one-implementation]]), and every check of a round knows a round by one test and its title line by one pattern (case 601.1);
  change: the SubagentStop check sends back a round of case-guppi with a question out of the grill-me form, once per text; one test of a round serves every check of a round (case 601.1)
```

```tasks
- [x] update `rule-case-check`
- [x] create `estimate-case-check-sends-back-a-faulty-round`
- [x] `guppi/casecheck.py`: `is_round` becomes the one test of a round: no Case heading, a first line that is not blank and is not `**Fact:**`, and a line that opens with `❓`, the indent set aside. A new function, importing it, gives the findings of each question of a round out of form, its title line judged by `QUESTION_LINE`. `subagent` runs it on the newest output of `case-guppi`, read by `outputs`. When that output is a round with findings, and no earlier output of the transcript holds the same text, the findings join those of the check of a Case, and the run exits 2. The check of the form stores nothing. The module docstring describes the check. Its sentence that an answer with no Case heading, where no earlier output holds one either, is not checked or stored gains: such an output is still judged as a round by the check of the form, which stores nothing.
- [x] `tests/test_casecheck.py`: the cases of the `method` of `estimate-case-check-sends-back-a-faulty-round`, each named `round_form`.
- [x] `uv run pytest tests/test_casecheck.py`
- [ ] read `estimate-case-check-sends-back-a-faulty-round`
```

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

```then
update:
- slug: estimate-case-check-sends-back-a-faulty-case
  set:
    status: pending
  change: the Criterion replaced whole — an answer whose outputs hold no Case heading gets none of the checks of a Case, and the form of a round is the promise of estimate-case-check-sends-back-a-faulty-round (case 601.2)
```

```tasks
- [x] update `estimate-case-check-sends-back-a-faulty-case`
- [ ] read `estimate-case-check-sends-back-a-faulty-case`
```

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

```then
update:
- slug: estimate-case-build-writes-the-case
  set:
    status: pending
  change: the Criterion replaced whole — the hook of rule-case-check judges the form of the questions of a round, not its context, and stores nothing of it (case 601.3)
```

```tasks
- [x] update `estimate-case-build-writes-the-case`
- [ ] read `estimate-case-build-writes-the-case`
```

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

```then
update:
- slug: estimate-case-check-refuses-text-before-a-round
  set:
    status: pending
  change: the Criterion replaced whole — a round is known by is_round, the one test of a round (case 601.4)
```

```tasks
- [x] update `estimate-case-check-refuses-text-before-a-round`
- [x] `guppi/casecheck.py`: the docstring paragraph on how a round opens says that a round is known by `is_round`, the one test of a round, not by a `QUESTION_LINE` match.
- [x] `tests/test_casecheck.py`: a round whose only question lacks the colon after its title is a round to the `Stop` run, and a reply that shows it after a text of the main agent's own is refused; the test is named `round`.
- [x] `uv run pytest tests/test_casecheck.py -k round`
- [x] read `estimate-case-check-refuses-text-before-a-round`
```

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

```then
update:
- slug: estimate-case-check-requires-each-question-of-the-rounds
  set:
    status: pending
    purpose: Whether the check of each answer of case-guppi sends back a Case whose recommend misses the title of a question of its rounds in the grill-me form
    method: 'pytest tests/test_casecheck.py -k rounds over a temp agent transcript: a round and a Case whose recommend holds every title, one that misses a title, a title asked in two rounds, a round out of form whose titles are not required, an answer with no round; then by hand the first Case the hook sends back for a missing title'
  change: the Criterion replaced whole — only a round in form gives the titles recommend must hold (case 601.5)
```

```tasks
- [x] update `estimate-case-check-requires-each-question-of-the-rounds`
- [x] `guppi/casecheck.py`: `round_titles` skips an output that the function of the form of a round finds out of form; its docstring and the module docstring say so.
- [x] `tests/test_casecheck.py`: a round sent back for its form, followed by a round in form with a changed title, requires only the titles of the round in form; the test is named `rounds`.
- [x] `uv run pytest tests/test_casecheck.py -k rounds`
- [ ] read `estimate-case-check-requires-each-question-of-the-rounds`
```

## Case 602 — the synthesis gives one line per lesson

> **context:**
> At the end of a session, the synthesis step of `librarian-guppi` compares the root cause of each new lesson with the index lines of the live lessons and Insights. It adds a lesson to an Insight when the cause is the same. The frame (`rule-synthesis`) says that a lesson without a pair stays `new` and that this needs no flag. The frame names a page in the report only when the librarian opened that page to decide. The Criterion of `estimate-synthesis-clusters` asks for more: the report must name the comparisons made against the lines of both Greps, and the outcome of each lesson read, "or none and why". The reading at the /hi of session 2300 failed on this gap. The yaml of session 2049 held two lesson entries. The brief gave a reason against the Insights for `lesson-prespec-onward-re-ratification-out-after-its-stretch` and none for `lesson-case-check-question-line-without-colon-unseen`, although the librarian followed its frame. The person chose to change the frame, not to narrow the Criterion. The person also chose to replace the Criterion whole so that it states the same promise, and to make the line of an unpaired lesson say "none" with a short reason. The new Criterion changes two lines of the old one on purpose. The line on the Greps now names the brief and the number of lines each Grep printed, in place of the loose "comparisons made against their lines". The line on an unpaired lesson now adds that its line in the brief is no flag. The other lines are carried as they stand. The synthesis is reported in the brief: the frame already says that a pair goes "in the brief beside the synthesis". The answer of `rule-close` holds at most twenty lines and nothing else, so the new line goes into the brief. Pre-spec found two weak points, and both stand. First, the Render of `rule-brief` sets five sections of the brief and takes Where things stand from the handoff and the counts of the yaml. The new sentence of `rule-synthesis` names no section, so it makes no sentence of `rule-brief` false. The brief of session 2049 already carries the index check and the synthesis as lines of Where things stand, under the same frame. Naming that section here would add a source that `rule-brief` does not list. Second, `estimate-brief-carries-the-run-facts` has the Readings due line of a `pending` Estimate whose `method` names the librarian's run end with the facts its `method` and Criterion name, and that line compares nothing and carries no passed or failed. `estimate-synthesis-clusters` is such an Estimate, so its Readings due line may repeat the lines of each lesson. That repeat is a copy of facts the run left, not a second judgment. The "none and why" of a lesson is the comparison of root causes that the synthesis makes as its own step. It is not a comparison of the facts with the Criterion of the Estimate, and it is not a verdict. So that Criterion stays true, and this Case does not touch it. A Grep `Where things stand|synthesis|index check` over `vault/wiki/estimates/estimate-brief-*.md` printed hits only in `estimate-brief-written.md`, on the order of the sections of the brief, and none of them speaks of the synthesis line, so `estimate-brief-written` stands. A Grep `without a pair` over the repository, outside `vault/raw/` and `vault/archive/`, printed seven files: `.claude/agents/librarian-guppi.md`, `rule-synthesis.md`, `estimate-synthesis-clusters.md` and `decision-case-487.1` to `decision-case-487.4`. The Decision pages are history and were not read. The rendered file follows by the render. The `method` of the Estimate names a reading of the yaml and the report after a live run with at least two lesson entries. That method states no part of the old promise, so it stands. The page carries no `purpose` field. `estimate-synthesis-keeps-actioned-by-the-mark` speaks of the `addressed_by` mark, not of the report of each lesson, so it is not touched. `estimate-documentation-completes` names a page opened at the synthesis in the report, and this Case keeps that. The new lesson about a question line without its colon has a different cause from the pattern of `insight-prespec-main-agent-question-off-the-grill-me-shape`. This Case clusters no lesson by hand. A Grep `librarian|synthesis` over the case file of Case 601 printed no match, so that Case does not touch this item.

> **problem:**
> The frame of the synthesis lets a lesson that joins nothing go with no word in the report. The Criterion of its Estimate asks for the comparison and the reason for each lesson. Each live reading after a run with an unpaired lesson can fail while the librarian does what its frame says.

> **recommend:**
> - **Does the check of this step get new wording?**
>   - Recommended: (a) replace the wording of the check, so that it says plainly that the report gives one line per new lesson, with the result against both searches
>   - Answer: agreed with the recommendation, (a)
> - **What does the line say for a lesson that joins nothing?**
>   - Recommended: (a) "none" and a short reason — one line per new lesson in the synthesis of the brief: its slug and the lesson or Insight it joined, or none with a few words on why no line of either search shares its cause
>   - Answer: agreed with the recommendation, (a)

> **given:**
> `rule-synthesis` — the frame of the synthesis, rendered into the librarian's frame
> **＋** `.claude/agents/librarian-guppi.md` — the frame of the librarian, which the render writes
> **＋** `estimate-synthesis-clusters` — the promise of the synthesis, its Criterion replaced
> **＋** `vault/wiki/brief.md` — where the librarian reports the synthesis
> **＋** `materialize.yaml` — the lesson entries the synthesis reads and the entries it adds
> **＋** `vault/wiki/lessons/` and `vault/wiki/insights/` — the index lines of the two Greps
> **＋** `vault/archive/` — the archive, whose read the synthesis does not need
> **＋** `estimate-documentation-completes` — the promise that holds the flag of a read outside the frame

> **when:**
> `librarian-guppi` does the synthesis in a live run whose `materialize.yaml` holds at least two lesson entries.

> **then:**
> The brief names the Greps of the synthesis, `^(root_cause|deferred_by):` over `vault/wiki/lessons/` and `^(pattern|deferred_by):` over `vault/wiki/insights/`, with the number of lines each printed.
> **＋** The brief gives one line for each lesson entry: its slug and the lesson or Insight it joined, or none and a few words on why no index line of either Grep shares its root cause.
> **＋** Two lessons with one root cause and no Insight give one `create` of an Insight with `pattern`, both children, the union of their tags, `Pattern` and `Proposal`, and one `update` per lesson with `set: {status: clustered, insight: <slug>}`.
> **＋** A lesson whose root cause matches the pattern of a live Insight gives an `update` of that Insight with the lesson added to its `children`, and an `update` of the lesson.
> **＋** Every entry the synthesis adds carries `librarian: synthesis`.
> **＋** Every lesson page read at synthesis is named in the report with the outcome: the Insight it joined, or none and why.
> **＋** A lesson without a pair stays `new`, and its line in the brief is no flag.
> **－** A read of another session's `materialize.yaml` or of a page under `vault/archive/` fails nothing here: an actioned Insight stays live with its pattern in its index line, and the flag of such a read is the promise of `estimate-documentation-completes`.

```then
update:
- slug: rule-synthesis
  replace:
  - old: One lesson without a pair stays `new`; that needs no flag.
    new: 'Write the synthesis into the brief: the two Greps with the number of lines each printed, then one line for each `lesson` entry — its slug and the lesson or Insight it joined, or none and a few words on why no index line of either Grep shares its root cause (case 602). One lesson without a pair stays `new`; its line in the brief is no flag.'
  change: the synthesis gives one line per lesson entry in the brief, a lesson that joins nothing with the reason (case 602)
- slug: estimate-synthesis-clusters
  set:
    status: pending
  change: the Criterion replaced whole — the brief gives one line per lesson entry with its outcome against both Greps, or none and why (case 602)
```

```tasks
- [x] update `rule-synthesis`
- [x] update `estimate-synthesis-clusters`
- [x] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
- [ ] read `estimate-synthesis-clusters` — by hand, the yaml and the brief after the first live librarian run after the render whose yaml holds at least two lesson entries
```

## Case 604 — `guppi onward --plan` counts a re-ratification for the whole session

> **context:**
> At the end of each reply in Plan Mode, the `Stop` hook `uv run guppi onward --plan` decides whether to send the agent on to `/pre-spec` or to the exit. It holds back while a Case is still out, meaning a file under `cases/` was written after that Case's last decision line. Today it finds that time in three places: the timed lines of `ledger.md`, the replies since the person's last message (the stretch, case 597.2), and the reply that ended. The ledger hook does not write a line it already holds. So when a Case is built again and ratified again with the same decision lines, `ledger.md` keeps the time of the first ratification. Only the reply that ratified it again shows the later time. Once the person writes another message, that reply falls out of the stretch, and the Case counts as out for the rest of the session. In session 2049, Case 596 was ratified again with unchanged lines. At the last ratification of the Frontier, the hook stayed silent and the person had to ask the agent to go on. That session recorded this as `lesson-prespec-onward-re-ratification-out-after-its-stretch`.
>
> By the person's answers, the hook now reads the decision lines of every reply of the main agent in the transcript, each at the time of its record. It uses `transcript_records` of `guppi/ledger.py`, the reading the ledger hook already makes when it collects lines. Case numbers are never reused, so a reply of an earlier session in the same transcript cannot name a Case of this one. The judgment of refusals (`spent`, `told`, `refusals`) stays on the stretch. The Criterion of `estimate-prespec-onward-reads-the-decisions-of-the-stretch` is replaced whole. Its `purpose` and `method` both state the old limit, so they are set anew. The page is renamed `estimate-prespec-onward-reads-the-decisions-of-the-session`, and a Glob of `vault/**/*reads-the-decisions-of-the-session*.md` found no file. The Estimate has not been read since case 597.2, and it stays `pending`. `estimate-prespec-onward-sends-the-agent-on` stands: its Criterion speaks of a Case still out only "as `rule-prespec-onward` judges it", and of refusals in the stretch, which do not change. The Case creates no page, so the vault query was not run. Only the hook's code changes; its registration in `.claude/settings.json` does not. That file registers six hooks on `Stop`: `uv run guppi ledger`, `uv run guppi ratified`, `uv run guppi casecheck`, `uv run guppi context`, `uv run guppi onward` and this one. None of them reads the judgment this hook makes. No text that the hook reads changes form, so no old form is kept. The lesson stands in the ledger of session 2049, not this one, so no decision line carries `{addresses}` (`ratification.md`). `rule-ledger-line-withdrawn-on-re-ratification`, deferred by case 594, deals with a line dropped on re-ratification, not with its time, and it is not taken up. `insight-spec-write-parent-body-kept-on-re-ratification` deals with the Spec hook and is not named. Cases 601, 602 and 603 of this session change neither `rule-prespec-onward` nor the `Stop` judgment of this hook.
>
> The check of this answer gave four notes, one for each line of the old Criterion that is not carried word for word. Each of those lines changes on purpose:
> - The line on the sources now says "the transcript" in place of "the stretch".
> - The line that defined the stretch is dropped, because the reading of decision lines no longer uses it. The new last line keeps the stretch for the refusals.
> - The line on the time of a record now speaks of a reply of the transcript.
> - The line on the outcome now reaches every later reply of the session, after a later message of the person too.
>
> Frame checks:
> - A Grep of `estimate-prespec-onward-reads-the-decisions-of-the-stretch` over the repository outside `vault/raw/` printed five files: `brief.md`, `log.md`, `rule-prespec-onward.md`, `decision-case-597.2.md` and `decision-case-597.md`. The only live hit is the `estimates` field of the rule, and the rename moves that link.
> - A Grep of `rule-prespec-onward` over the repository outside `vault/raw/` and `vault/archive/` printed 20 files. The live hits outside the rule, its Estimates, `decisions/`, `brief.md` and `log.md` were read around their lines: `orchestration.md`, `rule-orchestration.md`, `rule-prespec.md`, `rule-plan-mode.md`, `.claude/skills/pre-spec/SKILL.md`, `guppi/prespec.py`, `guppi/onward.py`, three Estimates of `rule-orchestration` and `estimate-retro-onward-sends-the-agent-to-the-handoff`. Each says that the hook sends the agent on, or names it as a child. None says which replies it reads.
> - A Grep of the pattern `(still out|is out|decision lines?).{0,200}(stretch|person's last message)|(stretch|person's last message).{0,200}(still out|decision line)` over the repository outside `vault/raw/` and `vault/archive/` printed six files: `log.md`, `rule-prespec-onward.md`, the lesson, the Estimate replaced here, `decision-case-597.md` and `guppi/onward.py`. This Case changes the rule, the Estimate and the module. The lesson and the Decision page are history.
> - The docstring of `stretch` in `guppi/ledger.py` says that `guppi onward` calls it. That stays true, because the refusals are still judged by the stretch.

> **problem:**
> When a Case is ratified again with the decision lines the ledger already holds, `guppi onward --plan` sees that re-ratification only until the person's next message. After that, the Case counts as out for the rest of the session. The hook then stays silent at the last ratification, and the person has to send the agent on by hand.

> **recommend:**
> - **How far back the hook reads the replies for decision lines**
>   - Recommended: (a) every reply of the main agent in the transcript, each counted at the time of its record, the way the ledger hook reads it.
>   - Answer: agreed with the recommendation, (a).
> - **What happens to the Estimate that checks the reading of the decision lines**
>   - Recommended: (a) replace the Criterion, set anew the `purpose` and `method`, and rename it `estimate-prespec-onward-reads-the-decisions-of-the-session`.
>   - Answer: agreed with the recommendation, (a).

> **given:**
> `rule-prespec-onward` — the rule of the hook, its `Purpose` section changed
> **＋** `estimate-prespec-onward-reads-the-decisions-of-the-stretch` — the promise of the reading of decision lines, its Criterion replaced whole and renamed `estimate-prespec-onward-reads-the-decisions-of-the-session`
> **＋** `guppi/onward.py` — the hook, its `stretch_replies`, `last_decisions` and `case_out`
> **＋** `guppi/ledger.py` — `transcript_records`, the reading of the transcript the ledger hook makes, and `refusals`, the judgment of the stretch; unchanged
> **＋** `guppi/casecheck.py` — `moment`, the time of a record; unchanged
> **＋** `tests/test_onward.py` and `tests/test_ledger.py` — the tests of the hook and of the readings it imports
> **＋** `transcript_path` of the `Stop` payload — the transcript the hook reads
> **＋** `raw/<date>/<hi HHMM>/ledger.md` — the session's ledger, whose timed decision lines the hook reads
> **＋** `raw/<date>/<hi HHMM>/cases/` — the files of the Cases, whose times the hook compares

> **when:**
> The `Stop` hook `uv run guppi onward --plan` judges, at the end of a reply of the main agent, whether a Case is still out.

> **then:**
> A Case N is still out when a file `case-<N>.md` under `raw/<date>/<hi HHMM>/cases/` was written after the last decision line of Case N or of a sub-case of N.
> **＋** The decision lines it reads are the timed lines of `raw/<date>/<hi HHMM>/ledger.md`, the lines inside a `LEDGER` block of each reply of the main agent in the transcript at `transcript_path`, and those of the reply that ended.
> **＋** The replies of the transcript are its `assistant` records of the main agent, read by `transcript_records` of `guppi/ledger.py`, the reading the ledger hook makes. A reply before the person's last message counts like one after it.
> **＋** A line of a reply of the transcript counts at the time of its record, read by `moment` of `guppi/casecheck.py`. A line of the reply that ended counts as written now.
> **＋** A line of `ledger.md` counts at its time on the `hi` date, rolled to the next date when the time runs backwards.
> **＋** So a Case built again and ratified by a reply whose decision lines the ledger already held is not out after that reply, and not at any later reply of the session, after a later message of the person too. This includes the reply that writes again a line the ledger hook refused.
> **－** A file of a Case with no decision line is out.
> **－** A record whose time cannot be read counts none of its lines. A transcript that cannot be read leaves `ledger.md` and the reply that ended as the only sources.
> **－** Its own refusals and those of the ledger hook are still judged in the stretch, by `refusals` of `guppi/ledger.py`.

```then
update:
- slug: rule-prespec-onward
  replace:
  - old: and in the replies since the person's last message, each at the time of its record in the transcript, the reply that ended counted as now (case 597.2)
    new: and in every reply of the main agent in the transcript, each at the time of its record, the reply that ended counted as now (cases 597.2, 604)
  change: a Case is judged out by the decision lines of every reply of the transcript, not only of the stretch, so a re-ratification with unchanged lines counts for the rest of the session (case 604)
- slug: estimate-prespec-onward-reads-the-decisions-of-the-stretch
  rename: estimate-prespec-onward-reads-the-decisions-of-the-session
  set:
    status: pending
    purpose: Whether guppi onward --plan judges a Case out by the decision lines of ledger.md and of every reply of the main agent in the transcript, each at the time of its record, so that a re-ratification with lines the ledger already held counts at every later reply of the session
    method: 'uv run pytest tests/test_onward.py; by hand at the first Case ratified again with unchanged decision lines in Plan Mode after the change, at the reply that closes the last line under Cases after a later message of the person: the transcript, ledger.md and the times of the files under cases/, recorded in the estimate line'
  change: renamed; the Criterion, purpose and method replaced — the decision lines of every reply of the transcript count, not only those of the stretch (case 604)
```

```tasks
- [x] update `rule-prespec-onward`
- [x] update `estimate-prespec-onward-reads-the-decisions-of-the-stretch`
- [x] `guppi/onward.py`: the replies whose decision lines count are every `assistant` record of `transcript_records` of `guppi/ledger.py`, each at its `moment`, not the records of `stretch`. `spent` and `told` are unchanged. The module docstring and the docstrings of the changed functions say so, with case 604.
- [x] `tests/test_onward.py`: a Case whose ratifying reply stands before the person's last message in the transcript, its file written before that reply and after its line in `ledger.md`, is not out and the hook exits 2. The existing tests of the stretch replies stay green.
- [x] `uv run pytest tests/test_onward.py tests/test_ledger.py`
- [x] read `estimate-prespec-onward-reads-the-decisions-of-the-session`
```

## Case 605 — The Insight on the chat form of a Case takes the colon lesson and is closed by the check of the form of a round

> **context:**
> A rule on how a Case or a round looks in the chat holds only if a script reads it. Otherwise the fault is found later, by the person or at pre-spec. `insight-case-form-chat-form-read-by-no-script` gathers the lessons of this pattern. Earlier Cases closed it three times: case 419.3 (the chat form of a Case is checked on `SubagentStop`), case 449 (the person judges the text of the story sections, so a count in a story section is not checked by a script) and case 537 (the language finding on each answer). Each time a new lesson with the same cause came in, the Insight became `open` again. Its one live child is `lesson-case-protocol-own-text-before-a-round`, clustered on 2026-09-30. In session 1736 the main agent opened each round of `case-guppi` with a line of its own, and no check read the reply. Case 562 closed that cause: the `Stop` run of `rule-case-check` refuses a reply that shows a round after text the main agent wrote itself. `estimate-case-check-refuses-text-before-a-round` checks it.
>
> Case 562 did not close the pattern. `lesson-case-check-question-line-without-colon-unseen` (`new`, 2026-10-02, ledger line 25 of session 2049) records a second fault of the same kind. A round of `case-guppi` came with a question title line that had no colon after the bold title. `QUESTION_LINE` of `guppi/casecheck.py` did not see that line as a question, so no script read the form of the question, and two hand readings found the fault later. That is the Insight's pattern. The synthesis of the librarian did not cluster the lesson, and the brief gave no reason (case 602 fixes that report from now on). Pre-spec found the gap, and the person chose to add the lesson to the Insight in this Case. Case 601.1 of this session closes the cause of that lesson: the `SubagentStop` check sends back a round whose question is out of the grill-me form, and it judges the title line by `QUESTION_LINE`. `rule-insights-schema` makes `addressed_by` one link, to the latest fix, so it names `decision-case-601.1`. The case file of Case 601 is being built again, and the new version names this Insight.
>
> This Case gives the two `update` items that the frame of `rule-synthesis` gives when a lesson joins a live Insight. The Insight gets its `children` with the new lesson. The lesson gets `status: clustered` and `insight`. In the same `update` the Insight is set `actioned`. The values are bare slugs. `guppi/generate.py` writes each field that `REF_FIELDS` of `guppi/pages.py` names — `children`, `insight` and `addressed_by` among them — as a quoted wikilink. A link would also name `decision-case-601.1` before that page exists, and the check of bare links refuses that. The cascade of `guppi/generate.py` then archives both `clustered` children, and `guppi backlog` drops the Insight's line. The Insight stays live, so a new lesson with the same cause opens it again. The Insight's tags stand: the frame of `rule-synthesis` sets the union of tags only when it creates an Insight. Both lessons stand in the ledgers of earlier sessions, so no decision line carries `{addresses}` (`ratification.md`). The Insight has no `deferred_by`, so no `{supersedes:case N}` block is needed. The Case makes no `create`, so the vault query was not run.
>
> Two Estimates check the fixes: `estimate-case-check-refuses-text-before-a-round` for case 562, and `estimate-case-check-sends-back-a-faulty-round`, created by Case 601.1, for the colon lesson. This Case changes no behaviour, so the Criterion of each stands. `estimate-insights-schema-checked` and `estimate-lessons-schema-checked` cover the schema files, which this Case does not change. The other seven children of the Insight are archived: a Glob of their slugs under `vault/` found each of them under `vault/archive/`.
>
> Frame checks:
> - A Grep of `insight-case-form-chat-form-read-by-no-script` over `vault/wiki/` outside `decisions/` printed these files:
>   - `rules/rule-case-check.md`: its Purpose says that until case 419 no script read a Case before its ratification. That stays true.
>   - `backlog.md`: the Insight's line, which comes from its `open` status.
>   - `lessons/lesson-case-protocol-own-text-before-a-round.md`: the child.
>   - `log.md`: not read.
> - A Grep of `lesson-case-check-question-line-without-colon-unseen` over the repository outside `vault/wiki/decisions/` printed these files:
>   - `vault/wiki/brief.md`: line 85 lists the lesson as a question for this session. Case 601 answers that question.
>   - `log.md`: not read.
>   - Under `raw/2026-10-02/`, `2300/ledger.md`, `2300/frontier.md`, the case files of Cases 601, 602 and 605, `2049/materialize.yaml`, `2049/ledger.md` and `2049/handoff.md`: these are records of the sessions.
>
>   The context of Case 602 says that Case 602 clusters no lesson by hand. That stays true of Case 602.
> - A Grep of both Insight and lesson slugs over the repository outside `vault/` printed no file.
>
> Not done: the Insight's Proposal on a count in a story section stays rejected, as case 449 decided.

> **problem:**
> The Insight still stands `open` in the backlog. Its one live lesson was closed by case 562. A second lesson of its pattern, the question title line without the colon, stands `new` and is part of no Insight. Case 601.1 of this session closes the cause of that second lesson. The question was whether to close the Insight now, and with which lessons and which fix.

> **recommend:**
> - Recommended: close the Insight now, with `addressed_by` naming `decision-case-562`, the decision whose `Stop` check refuses a round shown after the main agent's own text.
>   - Answer: ratified as built
> - **Change**
>   - Asked: pre-spec found that `lesson-case-check-question-line-without-colon-unseen`, recorded after case 562, fits the Insight's pattern, and that Case 601.1 is then the latest fix. The person chose to add that lesson to the Insight's `children`, set it `clustered` with `insight`, have `addressed_by` name `decision-case-601.1`, and let the cascade archive both lessons with the Insight `actioned`.
>   - Taken: the Insight's `update` sets `children` with the new lesson, `status: actioned` and `addressed_by: decision-case-601.1`. A second `update` sets the lesson `clustered` with `insight`. The context no longer claims that no lesson of the cause came in after case 562.

> **given:**
> `insight-case-form-chat-form-read-by-no-script` — the Insight; its `children` widened and its status set `actioned`
> **＋** `lesson-case-check-question-line-without-colon-unseen` — the lesson of the colon, set `clustered` under the Insight
> **＋** `lesson-case-protocol-own-text-before-a-round` — the live `clustered` child that already stands
> **＋** `decision-case-601.1` — the decision that closes the cause of the colon lesson, named by `addressed_by`; built from `raw/2026-10-02/2300/cases/case-601.md`; unchanged here
> **＋** `rule-insights-schema` and `rule-lessons-schema` — the fields `children`, `addressed_by`, `insight` and the cascade; unchanged
> **＋** `rule-synthesis` — the form of the `update` items that add a lesson to a live Insight; unchanged
> **＋** `guppi/generate.py` and `guppi/pages.py` — apply the items, write the slug fields as wikilinks and run the cascade; unchanged
> **＋** `guppi/backlog.py` and `vault/wiki/backlog.md` — the list of the `open` Insights; unchanged code

> **when:**
> `uv run guppi generate` applies the `update` items of `insight-case-form-chat-form-read-by-no-script` and `lesson-case-check-question-line-without-colon-unseen`, and `uv run guppi backlog` then writes `vault/wiki/backlog.md`.

> **then:**
> `insight-case-form-chat-form-read-by-no-script` has `lesson-case-check-question-line-without-colon-unseen` among its `children`, `status: actioned` and `addressed_by` naming `decision-case-601.1`.
> **＋** `lesson-case-check-question-line-without-colon-unseen` has `status: clustered` and `insight` naming `insight-case-form-chat-form-read-by-no-script`.
> **＋** The cascade of `guppi/generate.py` archives `lesson-case-protocol-own-text-before-a-round` and `lesson-case-check-question-line-without-colon-unseen`.
> **＋** `vault/wiki/backlog.md` holds no line for the Insight.
> **－** The Insight is not archived. It stays live, and a new lesson with its cause opens it again.
> **－** The tags of the Insight do not change.
> **－** `decision-case-601.1`, `rule-insights-schema`, `rule-lessons-schema` and `rule-synthesis` do not change.

```then
update:
- slug: insight-case-form-chat-form-read-by-no-script
  set:
    children:
    - lesson-case-form-the-spec-free-sections-written-last
    - lesson-case-form-ratification-used-for-the-agents-caveats
    - lesson-case-form-a-count-in-the-sentence-that-opens-a-list
    - lesson-case-form-given-written-before-tasks
    - lesson-case-build-a-list-in-context
    - lesson-case-build-quotes-the-person-in-the-chat-language
    - lesson-case-build-rebuild-quotes-the-relayed-words
    - lesson-case-protocol-own-text-before-a-round
    - lesson-case-check-question-line-without-colon-unseen
    status: actioned
    addressed_by: decision-case-601.1
  change: 'child lesson-case-check-question-line-without-colon-unseen added; actioned: the Stop check of rule-case-check refuses a round shown after a text of the main agent''s own (case 562), and the SubagentStop check sends back a round with a question out of the grill-me form (case 601.1); a count in a story section stays rejected (case 449) (case 605)'
- slug: lesson-case-check-question-line-without-colon-unseen
  set:
    status: clustered
    insight: insight-case-form-chat-form-read-by-no-script
  change: clustered under insight-case-form-chat-form-read-by-no-script (case 605)
```

```tasks
- [x] update `insight-case-form-chat-form-read-by-no-script`
- [x] update `lesson-case-check-question-line-without-colon-unseen`
```

## Case 606 — A Case writes no `by hand` box that waits for the librarian's run

> **context:**
> Work Mode ticks each code, test, migration and `by hand` box of its own session's Spec in the reply that finishes the task. Retro counts what stays unticked. The librarian carries every unticked box of the Specs into the Work list of the brief. Case 591.11 wrote a `by hand` box whose check can only run after the librarian's run of its own session: `make lint` prints no `fence` line on `decision-case-13`. That moment comes after Work Mode and Retro have ended, so no one could tick the box in session 1202. Retro of that session did not count it, and the librarian carried it into the brief. Twice a later session took the check and closed its Work line `· work` without ticking the box: W41 of the Frontier of session 1834, and W49 of the Frontier of session 2049. Nothing told either one to tick it. The librarian carried the box each time, and it is open again as W41 of this session's Frontier. The cause is the box itself. The check it asks for already has two homes: the reading of an Estimate, whose `read` line `generate` ticks from the ledger in every `spec.md` under `vault/raw/`, and the `make lint` of the librarian's run, which the brief reports. Case 591.11 itself named `estimate-sprint-migration-lint-clean` as the Estimate of a clean lint. Case 606.1 adds one sentence to the `tasks` form in `case-schema.md`, the Render of `rule-case-protocol`. The sentence bars such a box and says where such a check goes. Case 606.2 closes, once, the one box of this kind open today. The two can fail apart and need different fixes, so they are two sub-cases. Case 606.2 changes no text of a page. Its decision line is an `update` of `decision-case-13` with `change` alone, which writes one History line on that page, the form `case-schema.md` sets for a Case that names a page whose text does not change. This Case replaces Case 603 and its sub-cases 603.1 and 603.2, with the same content. Case 603 was first ratified whole, then split into 603.1 and 603.2 and ratified again. The Spec hook kept the old body of the parent under its heading beside the sub-cases, the fault that `insight-spec-write-parent-body-kept-on-re-ratification` records. The old body then wrote the Criterion of `estimate-case-protocol-case-form` a second time, so one promise stood in two wordings, and the main agent may not edit the plan file. As case 581 did for Case 580, this Case is built again under a new id. Its decision lines supersede 603, 603.1 and 603.2, so the Spec hook removes their text, and the Frontier line C4 closes again under this Case. The person asked whether the librarian needs new instructions. It does not: it ticks no box by hand, `generate` ticks the `read` lines, and the `make lint` of its run is already in the brief, so `rule-brief` stands. `orchestration.md` says that Work Mode ticks the boxes of `raw/<date>/<hi HHMM>/spec.md`, the Spec of its own session. That sentence stays true. The one-off is a task of this session's Spec, which Work Mode ticks there. What the task does is tick one box in the Spec of session 1202, by this ratification, once. No rule names who ticks a box of an earlier Spec, and after Case 606.1 no new Case writes a box that needs one. The Case creates no page, so no vault query was run. In the frame, a Grep of `unticked` over `.claude/`, `vault/wiki/rules/` and `vault/wiki/estimates/` printed 16 files: `rule-brief`, `rule-documentation`, `rule-glossary`, `.claude/agents/librarian-guppi.md`, `rule-materialize`, `rule-page-generation`, `rule-orchestration`, `.claude/skills/retro/SKILL.md`, `rule-retro`, `rule-sprint`, `estimate-brief-written`, `estimate-generate-ticks-the-spec`, `estimate-documentation-completes`, `estimate-glossary-ticks-the-spec`, `estimate-render-harness-ticks-the-spec` and `estimate-sprint-ticks-the-spec`. Each hit, read around its line, says who ticks which line or what the librarian reads and carries. None says which boxes a Case may write. A Grep of `librarian's run` over `vault/wiki/rules/*.md` and `.claude/**/*.md` printed 12 files: `.claude/skills/work/SKILL.md`, `.claude/skills/hi/SKILL.md`, `.claude/skills/retro/SKILL.md`, `.claude/agents/librarian-guppi.md`, `.claude/agents/case-guppi.md`, `rule-retro`, `rule-estimates-schema`, `rule-case-build`, `rule-skill-hi`, `rule-work-mode`, `rule-documentation` and `rule-brief`. None lets a Case write a box that waits for that run. `rule-retro` already says that the librarian's `make lint` is the reading of a check that waits for it, which this Case agrees with. A Grep of the `old` anchor over `vault/wiki/` outside `decisions/` printed `vault/wiki/case-schema.md` and `rules/rule-case-protocol.md`; the pair hits the page once. A Grep of `decision-case-13`` over the `frontier.md` files of `vault/raw/2026-10-02/` printed the lines of sessions 1834, 2049 and 2300. Case 606.1 replaces whole the Criterion of `estimate-case-protocol-case-form`, which reads the `tasks` of the Cases of a session by hand, and writes it under `sections`: the lines case 544.11 left stand, and one line is added on the `by hand` box. Its `purpose` and `method` do not state the old promise and stand. `estimate-case-protocol-loaded` checks that the file is rendered and loaded, so it stands. `estimate-case-build-writes-the-case` speaks of the chat form of `case-schema.md` as a whole, so it stands. Case 606.2 is checked by `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`: its Criterion has Work Mode run each task of the session's Spec in order and tick each `by hand` box in the reply that finishes the task. It stands, because the one-off is one more such task, and Retro counts it as debt when it stays unticked. Cases 601 and 602 of this session change neither `rule-case-protocol` nor the writing of `tasks`.

> **problem:**
> A Case can write a `by hand` box whose check only runs after Work Mode and Retro of its own session have ended. Nobody ticks such a box, and the brief carries it from session to session. The question was whether to tick it later or stop writing it. The person chose to fix the cause and to close the box open today by a Work Mode task.

> **recommend:**
> - **Which boxes does the closer tick?**
>   - Recommended: (a) every box Work Mode ticks — code, a test, a migration or a `by hand` check — in an earlier session's Spec, ticked by whoever closes its Work line.
>   - Answer: not answered; replaced by **Fix the cause, or tick the box later?**
> - **Where is the rule written?**
>   - Recommended: (a) one sentence in the ticking paragraph of `orchestration.md`, which applies at `/hi`, in Work Mode and at Retro.
>   - Answer: not answered; replaced by **Fix the cause, or tick the box later?**
> - **The box open today**
>   - Recommended: (a) a Work Mode task of this Case: run `make lint`, tick the box in `raw/2026-10-02/1202/spec.md` when no `fence` line on `decision-case-13` appears, and close its Work line. Whatever the answer on the cause, the tick then rests on a ratified decision.
>   - Answer: (a).
> - **How is the new rule checked?**
>   - Recommended: (a) rewrite the Criterion of `estimate-case-protocol-case-form` whole, adding a line that `tasks` holds no `by hand` box whose moment comes after Work Mode of its session, read by hand at the close of a later session. A hook that matches words would miss other phrasings.
>   - Answer: (a). The first round asked this question about the ticking rule, and it went unanswered there.
> - **Fix the cause, or tick the box later?**
>   - Recommended: (a) fix the cause. A Case writes no `by hand` box whose moment comes after Work Mode of its session. Such a check is the reading of an Estimate or the `make lint` of the librarian's run, and the box open today is closed once.
>   - Answer: (a). The person asked why such a box stays unticked at all and said the earlier direction was wrong.
> - **Where is the new rule written?**
>   - Recommended: (a) one sentence in the `tasks` part of `case-schema.md`, the Render of `rule-case-protocol`, which `case-guppi` reads whole.
>   - Answer: (a).
> - **What does the second sub-case record in the ledger?**
>   - Recommended: (a) an `update` of `decision-case-13` with `change` alone, which writes one History line on that page saying that the check of its fence has been run and the box ticked; nothing else on the page changes.
>   - Answer: not answered in a round; the person ratified Case 603, which was built on (a), with its sub-cases.

### Case 606.1 — The form of `tasks` bars a `by hand` box that waits for the librarian's run

> **given:**
> `rule-case-protocol` — the form of a Case, rendered into `vault/wiki/case-schema.md`, which `case-guppi` reads whole
> **＋** `estimate-case-protocol-case-form` — the promise on the form of a built Case, its Criterion replaced whole
> **＋** `rule-brief` — the brief of the librarian, which carries the unticked boxes of the Specs under Work; unchanged

> **when:**
> `case-guppi` writes the `tasks` of a Case, following `vault/wiki/case-schema.md` as rendered from `rule-case-protocol`.

> **then:**
> A `by hand` box in `tasks` is a check that Work Mode of the Case's own session takes.
> **＋** A check whose moment comes after that Work Mode — the librarian's run of the session or a later session — is no box. It is the reading of an Estimate, through the `read` line of an Estimate the Case creates or sets `pending` or through an Estimate its `context` names, or it is left to the `make lint` of the librarian's run, which the brief reports.
> **－** `rule-brief` still carries the unticked boxes of the Specs under Work of the brief.

```then
update:
- slug: rule-case-protocol
  replace:
  - old: one per reading of an Estimate the Case creates or sets `pending`, by its slug.
    new: 'one per reading of an Estimate the Case creates or sets `pending`, by its slug. A `by hand` box is a check that Work Mode of the Case''s own session takes; a check whose moment comes after that Work Mode — the librarian''s run of the session or a later session — is no box: it is the reading of an Estimate, through the `read` line of one the Case creates or sets `pending` or through one its `context` names, or it is left to the `make lint` of the librarian''s run, which the brief reports (case 606.1).'
  change: a Case writes no by hand box whose moment comes after Work Mode of its session; such a check is the reading of an Estimate or the make lint of the librarian's run (case 606.1)
- slug: estimate-case-protocol-case-form
  set:
    status: pending
  sections:
    Criterion: |-
      When:
      The hook of `rule-case-check` writes a Case that `case-guppi` built into `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and the main agent sends that file to the person, at its first showing or again.

      Then:
      The file opens with the heading `## Case N — name`, a sub-case with `### Case N.M — name` under its parent, and holds the sections of each Case in the order of the Sections table of `vault/wiki/case-schema.md`, each one blockquote whose first line is `**name:**`.
      **＋** `context` and `problem` are plain prose that explains briefly — `context` opens with the mechanism in plain words, then gives the state of the pages the Case changes, the vault's answer, what `case-guppi` found in the frame and why an Estimate of the rule is not touched, and leaves out a part with nothing to say — `recommend` is the list the Sections table of `vault/wiki/case-schema.md` sets, each item plain prose, and the person raised no complaint in the session about their length or clarity.
      **＋** `given` holds the frame, one thing per line — each page, module, file and test the Case touches and the rule that constrains, its slug or path in a code span and its role — and no state.
      **＋** In `given`, `when` and `then` each line after the first opens with `**＋**` or `**－**`, a `**－**` line names something of `given` or `when`, `then` holds behaviour only, and none of them holds a count of items — pages, lines, Estimates, Cases, tests; a number that states a condition or a limit stands.
      **＋** `tasks` names by slug each Estimate the Case creates or replaces, and under a line whose item writes content that content stands as sub-points; no `contract` line and no "block N" line.
      **＋** `tasks` holds no `by hand` box whose moment comes after Work Mode of the Case's own session — the librarian's run of that session or a later session; such a check stands as the reading of an Estimate or is left to the `make lint` of the librarian's run.
      **＋** A pair under `replace` or `reword` stands only when the Case says what the sentence around each match names; a Case that changes the behaviour of a page gives an `update` to each Estimate of that page whose Criterion speaks of the change.
      **＋** `ratification` holds only the preview of the ledger lines in an untagged fence; in the chat the Case stands as the short text and that `ratification` of `estimate-orchestration-shows-the-built-case`, and the reply ends with a plain question.
      **＋** A Case with sub-cases stands in one file and is sent in one reply: the parent's `context`, `problem` and `recommend`, then each sub-case whole, with its own `recommend` when it has one.
      **－** A case number, a count, a line number or a quotation in `context`, `problem` or `recommend` is no fault of the form.
  change: the Criterion replaced whole — tasks hold no by hand box whose moment comes after Work Mode of the Case's session; the other lines as case 544.11 left them (case 606.1)
```

```tasks
- [x] update `rule-case-protocol`
- [x] update `estimate-case-protocol-case-form`
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
- [x] read `estimate-case-protocol-case-form` — by hand, the Cases of a later session at its close
```

### Case 606.2 — The box of Case 591.11 is ticked once

> **given:**
> `raw/2026-10-02/1202/spec.md` — the Spec whose `by hand` box of Case 591.11 stands unticked
> **＋** `raw/2026-10-02/2300/frontier.md` — the Frontier of this session, whose Work line carries that box
> **＋** `make lint` — the check that box names
> **＋** `decision-case-13` — the Decision page whose `fence` finding that box names; it gains a History line alone
> **＋** `rule-orchestration` — who ticks the boxes of a Spec; unchanged
> **＋** `rule-skill-hi` — a Work line closes `· work` where its work is done; unchanged
> **＋** `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — Work Mode runs and ticks each task of the session's Spec; its Criterion stands

> **when:**
> Work Mode of session 2300 runs the one-off task of Case 606.2.

> **then:**
> Work Mode runs `make lint`. When it prints no `fence` line on `decision-case-13`, Work Mode ticks the `by hand` box of Case 591.11 in `raw/2026-10-02/1202/spec.md` and closes its line of `raw/2026-10-02/2300/frontier.md` as `· work`.
> **－** When `make lint` prints a `fence` line on `decision-case-13`, the box stays unticked and its line of `raw/2026-10-02/2300/frontier.md` stays open.
> **－** `rule-orchestration` still sets who ticks the boxes of a Spec: the tick in `raw/2026-10-02/1202/spec.md` is a one-off of this sub-case and sets no rule.
> **－** The text of `decision-case-13` does not change; only its History gains a line.

```then
update:
- slug: decision-case-13
  change: the check of its closed fence taken after the librarian's run of session 1202; the box of Case 591.11 in raw/2026-10-02/1202/spec.md ticked by Work Mode of session 2300 (case 606.2)
```

```tasks
- [x] update `decision-case-13`
- [x] one-off, by hand: `make lint` prints no `fence` line on `decision-case-13`; then tick the box of Case 591.11 in `vault/raw/2026-10-02/1202/spec.md` and close its line of `vault/raw/2026-10-02/2300/frontier.md` as `· work`
```
