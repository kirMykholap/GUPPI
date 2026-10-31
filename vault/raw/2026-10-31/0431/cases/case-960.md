## Case 960 — A reading by hand names where its evidence is saved

> **context:**
> Some Estimates are checked by a reading by hand that waits for an event, and then reads what an agent did in a chat. `estimate-where-to-stop-writes-each-step-whole` reads the reply of a stop of Work Mode that asks the person to run commands by hand. `estimate-case-build-reads-the-readers-of-a-changed-step` reads the findings of `ask-guppi` at a `/pre-spec`. Both events came in the session 2026-10-31/0128: its handoff names the by-hand test of Case 953 in Work Mode and eleven findings of `ask-guppi` at its `/pre-spec`. Both texts stood only in the chat of that session, and neither method names a place where they are saved. So `/hi` cannot take the readings, since it reads no transcript of an earlier session (case 670.5), and the Work lines stay open from session to session, as `lesson-brief-lists-transcript-readings-under-work` records. Claude Code saves every chat as a transcript under `~/.claude/projects/`; the transcript of the main session of 0128, `850a2e1e-ab70-422f-8401-df00a3a64d5e.jsonl`, stands there, as a Glob printed. Both methods also tie the reading to the first event of a kind. The description of the field `method` in `rule-estimates-schema` already says that any moment of the named kind counts, in this session or an earlier one, and that the word "first" fits only an event that has never happened. It says nothing about where the evidence of a reading must stand, and `case-schema.md`, which `case-guppi` reads when it writes a method, says nothing about it either. The person chose that a reading by hand names the place where its evidence is saved: a file of the repository, the output of a command, or a transcript. The rule goes into the field description of `rule-estimates-schema` and into one sentence of `case-schema.md`, with no lint check. The two methods name an event of a kind, not the first one, and read in the transcript of a session where it happened. Retro (`.claude/skills/retro/SKILL.md`, line 22) reads an Estimate whose `method` opens with `by hand, after` and names its event before a colon only when the event came in this session, and leaves it `pending` otherwise. The events came in 0128, so the two methods open with `by hand, at Retro` and name the event by its kind inside the reading, as the finding 1.7 of `ask-guppi` at the `/pre-spec` of this session asked. Case 961 of this session, read whole in its finished file, writes its methods whose event has already come in the same form, with the case or session it reads now in a bracket of its own at the end of the method, so the method reads whole without it; the two methods here take that bracket too. A new Estimate on `rule-estimates-schema` checks the rule, read at the Retro of this session over the methods of its Spec. In `lint.py` I read `tied_to_a_one_off_moment`, `waits_for_an_event`, `waits_for_another_session`, `waits_for_a_later_moment`, `check_moment` and `check_unread` whole: the new methods hold no "first", so the class `moment` gives no finding; they wait for no later moment, so `check_unread` gives each one the finding `unread: pending` until its reading of this Retro lands at the librarian's run of this session. `/work` (`.claude/skills/work/SKILL.md`, line 25) leaves the reading of an Estimate that this session updates to Retro. Retro (`.claude/skills/retro/SKILL.md`, line 22) reads such an Estimate on the Criterion of the Spec, but neither reads an Estimate whose `update` names one part of the page alone nor sets it `failed`. So Cases 960.2 and 960.3 set each Estimate `pending` and write its Criterion back word for word as their `when` and `then`. With a method that opens with `by hand, at Retro`, the Retro of this session reads both from the transcripts of 0128. A Grep of `transcript of an earlier session|read no transcript|only in the chat|shown only in the chat` over the `.md` files of `vault/wiki/` and `.claude/` printed `.claude/skills/hi/SKILL.md`, `vault/wiki/rules/rule-skill-hi.md`, `vault/wiki/estimates/estimate-hi-takes-its-readings.md` and `vault/wiki/lessons/lesson-brief-lists-transcript-readings-under-work.md`. The skill, its Rule and its Estimate stand: `/hi` still reads no transcript, and the readings that do are taken in Work Mode or at Retro. The lesson stands as a record. A Grep of `rule-case-protocol|rule-estimates-schema|estimate-where-to-stop-writes|estimate-case-build-reads-the-readers` over `.guppi/` printed `.guppi/tests/test_casecheck.py`, `.guppi/guppi/materialize.py`, `.guppi/tests/test_guard.py` and `.guppi/tests/test_glossary.py`. Each test writes its own copy under a temporary folder or a string, and `materialize.py` names the slug in a docstring. `.guppi/tests/test_schemas.py` reads the live `vault/wiki/estimates/schema.yaml`, but only its lists of fields, values and sections, which this Case leaves unchanged. `estimate-estimates-schema-checked` stands, since it checks those lists and that each name has a description. `estimate-case-protocol-loaded` and `estimate-case-protocol-case-form` stand, since one checks that the file equals the Render and the other checks the form of a Case, not what a `method` reads. The row of the Estimate fields in `glossary.md` stands. A Glob `vault/**/estimate-estimates-schema-method*.md` printed nothing, so the new slug is free. Case 956 of this session is a related Case. Its methods for `estimate-handoff-dispatches` (956.3) and `estimate-spec-box-runs-a-conserved-spec` (956.4) now read the dispatch line and the text shown to the person in the transcript of the session under `~/.claude/projects/`, the transcript named in the estimate line, as its case file holds them, so they keep the new rule and ask no change of Case 956. The session's ledger holds no `error` lesson, so no line carries `{addresses:...}`.

> **problem:**
> A reading by hand may point at a text that stood only in the chat of a session, so it cannot be taken once that chat ends. No rule says where the evidence of a reading must stand.

> **recommend:**
> - **Where the evidence of a reading may stand**
>   - Recommended: (a) a saved file, a transcript included: a file of the repository, the output of a command, or the transcript of the session under `~/.claude/projects/`.
>   - Answer: agreed, (a).
> - **Which texts carry the new rule**
>   - Recommended: (c) both texts, the field `method` of `rule-estimates-schema` and one sentence of `case-schema.md`, with no lint check.
>   - Answer: agreed, (c).
> - **How the two methods change**
>   - Recommended: (a) any event of the kind, read in its transcript, read in this session.
>   - Answer: agreed, (a).
> - **Which methods this Case fixes**
>   - Recommended: (a) the two Estimates, and a change asked of the Case of this session.
>   - Answer: agreed, (a).
> - **How the new rule is checked**
>   - Recommended: (a) a new Estimate on `rule-estimates-schema`.
>   - Answer: agreed, (a).

### Case 960.1 — A reading by hand names where its evidence is saved

> **given:**
> `rule-estimates-schema`: the field `method` of the schema of an Estimate, rendered into `vault/wiki/estimates/schema.yaml`.
> **＋** `rule-case-protocol`: the form of a Case, rendered into `vault/wiki/case-schema.md`, which `case-guppi` reads when it writes a method.
> **＋** `estimate-estimates-schema-method-names-its-evidence`: the new check of the rule.
> **＋** `raw/<date>/<hi HHMM>/spec.md`: the Spec whose methods the check reads.
> **＋** `~/.claude/projects/`: the folder where Claude Code saves the transcripts of sessions and agents.

> **when:**
> At the Retro of a session, the `method` of each Estimate that a Case of its Spec `raw/<date>/<hi HHMM>/spec.md` creates or sets `pending` is read.

> **then:**
> Each reading by hand in such a method names the place where its evidence is saved: a file of the repository, the output of a command, or the transcript of a session under `~/.claude/projects/`.
> **＋** A reading whose evidence is a reply, a text shown to the person or the output of an agent reads it in the transcript of the session where it stood.
> **＋** A reading that waits for an event names the kind of the event, and the word "first" stands only for an event that has never happened.
> **－** No reading by hand names a text of a chat as its evidence with no file, command or transcript to read it in.
> **－** A reading that is the person's answer is no fault: the estimate line keeps that answer.

> **tasks:**
> - [ ] update `rule-estimates-schema`
>   - old: `the word "first" stands only for an event that has never happened.`
>   - new: `` the word "first" stands only for an event that has never happened. A reading by hand names the place where its evidence is saved: a file of the repository, the output of a command, or the transcript of a session under `~/.claude/projects/`; it reads a reply, a text shown to the person or the output of an agent in the transcript of the session where it stood, never in the chat alone, and the estimate line names that file; the person's answer is kept by the estimate line itself (as set in case 960.1). ``
>   - change: `a reading by hand names the place where its evidence is saved, a transcript included`
> - [ ] update `rule-case-protocol`
>   - old: `` or under `Ask the person` when its `method` names the person's answer (case 781). ``
>   - new: `` or under `Ask the person` when its `method` names the person's answer (case 781). A reading by hand names the place where its evidence is saved — a file of the repository, the output of a command, or the transcript of a session under `~/.claude/projects/` — and reads a reply, a text shown to the person or the output of an agent in the transcript of the session where it stood, as `rule-estimates-schema` sets it for the field `method` (as set in case 960.1). ``
>   - change: `a method names the place where the evidence of its reading by hand is saved`
> - [ ] create `estimate-estimates-schema-method-names-its-evidence`
>   - ref: `rule-estimates-schema`
>   - kind: `QA`
>   - purpose: `Whether each reading by hand of a method that a Spec creates or sets pending names the file, command or transcript where its evidence is saved, reads a text of a chat in its transcript, and names an event by its kind`
>   - method: `by hand, at Retro: the method of each Estimate that a Case of the session's spec.md creates or sets pending, read against the Criterion, each fault counted in the estimate line`
>   - tags: `[schema, workflow]`
> - [ ] `uv run --project .guppi guppi render`: `vault/wiki/estimates/schema.yaml`
> - [ ] `uv run --project .guppi guppi render`: `vault/wiki/case-schema.md`
> - [ ] read `estimate-estimates-schema-method-names-its-evidence`

> **ratification:**
> ```
> - decision[case 960.1][update][rule-estimates-schema]{ref:rule-estimates-schema}
> - decision[case 960.1][update][rule-case-protocol]{ref:rule-case-protocol}
> - decision[case 960.1][create][estimate-estimates-schema-method-names-its-evidence]{ref:rule-estimates-schema}{tags:schema,workflow}
> ```

### Case 960.2 — The reading of a stop that asks for commands reads its transcript

> **given:**
> `estimate-where-to-stop-writes-each-step-whole`: its `method` changes, and its Criterion is written back word for word.
> **＋** `rule-where-to-stop`: the rule it checks.
> **＋** `vault/wiki/where-to-stop.md`: the Render of that rule, the text of a stop.
> **＋** `~/.claude/projects/`: the folder of the transcript of the session where the stop came.

> **when:**
> Work Mode stops on a condition of `vault/wiki/where-to-stop.md`, and the reply asks the person to run commands by hand.

> **then:**
> Each step of the reply writes out whole each command it asks the person to run, as the person types it, with each variable, folder and flag the command needs.
> **＋** A step that starts a program in a new window or terminal writes the variables that the start needs in its own command.
> **－** No step names a part of its command by a reference to another step.

> **tasks:**
> - [ ] update `estimate-where-to-stop-writes-each-step-whole`
>   - set:
>     ```
>     status: pending
>     method: "by hand, at Retro: the reply of a stop of Work Mode under the text of vault/wiki/where-to-stop.md that holds the sentence on each command written whole in each step, which asks the person to run commands by hand, read in the transcript of a session where such a stop came, under ~/.claude/projects/, against each line of the Criterion, the transcript named in the estimate line (the stop of the by-hand test of Case 953, in session 2026-10-31/0128)"
>     ```
>   - change: `the method reads the reply of any such stop in the transcript of its session, the Criterion written back unchanged`
> - [ ] read `estimate-where-to-stop-writes-each-step-whole`

> **ratification:**
> ```
> - decision[case 960.2][update][estimate-where-to-stop-writes-each-step-whole]{ref:rule-where-to-stop}
> ```

### Case 960.3 — The reading of the findings at a pre-spec reads its transcript

> **given:**
> `estimate-case-build-reads-the-readers-of-a-changed-step`: its `method` changes, and its Criterion is written back word for word.
> **＋** `rule-case-build`: the rule it checks, rendered into `.claude/agents/case-guppi.md`.
> **＋** `vault/wiki/rules/` and `.claude/`: the texts the agent searches for the readers of a step.
> **＋** `log.md` and `brief.md`: files whose hits are not read.
> **＋** `~/.claude/projects/`: the folder of the agent transcript of `ask-guppi` at the `/pre-spec`.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case that changes what a step of a skill, an agent or a hook writes, copies or shows, or adds a path on which a step does so, and is about to answer with its summary.

> **then:**
> It searches `vault/wiki/rules/` and `.claude/` for the name of that output — a line such as `Branch:`, a file or a list — and for the name of the step.
> **＋** It reads each step and skill that reads that output or does the same step, the steps after it in the same text and the new path its own Case adds included.
> **＋** Each step or skill that the change makes false enters the Case, or the `context` of the Case names it and says why it stands.
> **－** A hit in a History line, in `log.md` or in `brief.md` is not read.

> **tasks:**
> - [ ] update `estimate-case-build-reads-the-readers-of-a-changed-step`
>   - set:
>     ```
>     status: pending
>     method: "by hand, at Retro: the findings of ask-guppi at a /pre-spec of a session whose case-guppi runs on the Render of rule-case-build that holds the sentence on the readers of a changed step, read in the agent transcript of that ask-guppi under ~/.claude/projects/, for a Case that changes a step and misses a step or skill that reads its output or does the same step, the count and the transcript in the estimate line (the /pre-spec of session 2026-10-31/0128)"
>     ```
>   - change: `the method reads the findings of any such /pre-spec in the agent transcript of ask-guppi, the Criterion written back unchanged`
> - [ ] read `estimate-case-build-reads-the-readers-of-a-changed-step`

> **ratification:**
> ```
> - decision[case 960.3][update][estimate-case-build-reads-the-readers-of-a-changed-step]{ref:rule-case-build}
> ```
