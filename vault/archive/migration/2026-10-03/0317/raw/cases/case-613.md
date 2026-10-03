## Case 613 — A check by hand names the kind of its moment, and `/hi` reads a past moment from its transcript

> **context:**
> Each Estimate has a `method` line that says how its promise is checked. Many checks by hand tie their reading to one moment, "the first X after the render": the first `/handoff`, the first `/retro`, the first `/work`. That moment passes once, and nobody reads it. Take `estimate-handoff-holds-each-fact-once`, read "at the first /handoff after the render". `/handoff` runs after Retro has written the session's readings, so no step of that session is left to read it. The next `/hi` takes only readings whose method names `/hi` or the librarian's run. The handoff of session 0115 then listed it as "moment not come". The moment is not lost. The event logs `vault/raw/<date>/event_log.md` name each session by its id and mark `hi`, `prespec`, `retro`, `handoff` and each `Skill` and `Agent` call. The transcript of that session holds the turn until Claude Code deletes it. `rule-work-mode` already says that a moment of an earlier session has come, but no step opens an old transcript. The main agent's diagnosis holds: the tests run at every session, and one reading covers a whole `method`.
>
> The person chose this. A method names the kind of its moment, and any such moment after the render counts, in this session or an earlier one (613.3). The word "first" stays only for an event that has never happened, such as the first close of a sprint in the methods of case 612. `/hi` reads each moment of an earlier session from the transcript of the latest session that held it, part by part (613.2). One predicate in `guppi/lint.py` finds a reading by hand tied to "the first ... after the render" or "the first ... after the change". `make lint` and `pre-spec` both use it (613.1). The waiting Estimates, and the passed ones in the old wording, get their `method` line rewritten. The person did not choose a bulk `passed`: a reading line with no reading behind it is a false record.
>
> These facts come from the searches:
> - A Grep of `^status: (pending|failed)` over `vault/wiki/estimates/` printed 38 files. 613.3 rewrites 27 of them, and 11 keep their method.
> - A Grep of `^method:.*\bfirst\b.*after the (render|change)` over `vault/wiki/estimates/` printed 21 files. Ten of them are waiting Estimates. Ten are passed Estimates, which 613.3 rewrites. The last is `estimate-hi-takes-its-readings`, which 613.2 rewrites.
> - 613.3 also rewrites 17 waiting Estimates that tie their reading to a one-off moment in other words, such as "the first /retro" or "the first compaction".
> - A Grep of `^method:.*\bfirst\b` over the same folder printed 64 files. A passed Estimate among them that does not match the pattern stays as it is.
>
> The 11 waiting Estimates that keep their method fall into two groups:
> - Eight name no one-off moment: `estimate-end-of-work-order`, `estimate-event-log-records`, `estimate-ask-finds`, `estimate-plan-mode-verified`, `estimate-case-build-writes-the-case`, `estimate-session-start-context`, `estimate-orchestration-shows-the-built-case` (case 611 has it read again) and `estimate-synthesis-clusters` (read `passed` at this session's `/hi`).
> - Three are the done-conditions of `entity-sprint-migration`, read at the close of the sprint (case 612). `estimate-sprint-migration-leftovers-gone` names the close of the sprint and `estimate-sprint-migration-merges` the merge to main. Both are one-off moments, but each belongs to that close and comes only once by design. `estimate-sprint-migration-lint-clean` names `make lint`. All three keep their method.
>
> This session changes the Estimates of 613.3, so none of them is read in this session. The ledger hook refuses such a reading, and they are read from the next session on.
>
> These texts and Estimates were checked against the frame:
> - The new finding is a class of its own, `moment`. So `estimate-lint-checks-the-method` keeps its Criterion: it speaks of the `method` finding of the forms.
> - `estimate-prespec-catches-a-method-without-a-form` keeps its Criterion: it speaks of the line "method names no form".
> - `estimate-lint-catches` lists other classes and stays as it is.
> - `estimate-estimates-schema-checked` speaks of the lists of `schema.yaml`, not of the prose of `method`, and stands.
> - Three lines of the old Criterion of `estimate-hi-takes-its-readings` are not carried into 613.2, on purpose. They are the line on which readings `/hi` takes, the line on where it reads them, and the line that a later moment waits. 613.2 replaces each of them.
> - The check of the answer notes that the `then` of 613.3 shares words with the `then` of 613.1 and 613.2. 613.3 rewrites the methods that 613.1 judges and that 613.2 reads, so they speak of the same thing.
> - Lint changes in Work Mode, but the rewritten pages land at the librarian's run. In between, `make lint` shows red on them. Work Mode marks this under `## Expected red` of `work.md`, and Retro makes it a note for the handoff. Lint only goes red, so the check keeps no old form.
> - A Grep of `` /hi`? (takes|reads)|readings? of `?/hi|at `?/hi`? .{0,30}reading `` over the repository outside `vault/wiki/decisions/`, `vault/archive/` and `vault/raw/` printed 11 files. They are `glossary.md`, `librarian-guppi.md`, `carry/SKILL.md`, `log.md`, `entity-glossary.md`, `rule-skill-hi.md`, `estimate-carry-over-writes.md`, `rule-carry-over.md`, `rule-brief.md`, `estimate-hi-takes-its-readings.md` and `lesson-carry-short-brief-drops-the-work-list.md`. `log.md` was not read. The others outside this Case speak of where `/hi` takes its Work list, or of the sprint, and stay true.
> - A Grep of `first reply|previous session|transcript of` over `vault/wiki/rules/` printed seven files. They are `schema.yaml`, `rule-internal-context.md`, `rule-orchestration.md`, `rule-retro-onward.md`, `rule-rules-schema.md`, `rule-skill-hi.md` and `rule-case-protocol.md`. `rule-orchestration` defers the form of the first reply of `/hi` to `rule-skill-hi`. The other hits speak of the handover, of a refusal and of History, and stand.
> - The Work readings of `rule-work-mode` take what `/hi` leaves, and do not change.
> - Cases 611 and 612 change no page of this Case and set nothing at `/hi`.
> - The Case makes no `create` without a `ref`. A Glob of `vault/**/estimate-lint-reports*` printed no file, so the new slug is free.
>
> Not done: an Estimate whose event is rare still waits for it, and the close of a sprint settles it (case 612.4). An Estimate that pairs tests with a check by hand keeps one reading. The 11 waiting Estimates named above keep their method.

> **problem:**
> A check by hand is tied to one moment that passes unread, and no step reads it afterwards, so its Estimate waits for good. The question was how a method names its moment, which step reads a moment that came after its session's readings, how the old wording is caught, and what happens to the Estimates that wait today.

> **recommend:**
> - **How should a check by hand name its moment?**
>   - Recommended: (a) any such moment counts; the method names the kind of moment, and "the first" stays only for an event that has never happened.
>   - Answer: agreed with the recommendation, (a).
> - **Which step reads a moment that comes after its session's readings are written?**
>   - Recommended: (a) the next `/hi` reads it from the previous session's transcript.
>   - Answer: agreed with the recommendation, (a).
> - **What happens to the Estimates that wait today?**
>   - Recommended: (a) this Case rewrites their methods; they are read from the next session on.
>   - Answer: agreed with the recommendation, (a).
> - **What happens to an Estimate whose event is rare or has not happened yet?**
>   - Recommended: (a) it waits for the event, and the close of the sprint settles the rest.
>   - Answer: agreed with the recommendation, (a).
> - **What happens to an Estimate that pairs tests with a check by hand?**
>   - Recommended: (a) keep both parts in one reading.
>   - Answer: agreed with the recommendation, (a).
> - **What happens when a method names more than one moment?**
>   - Recommended: (a) `/hi` reads each part from the session where its moment came.
>   - Answer: agreed with the recommendation, (a).
> - **How is the new form of a method checked?**
>   - Recommended: (a) one pattern in `guppi/lint.py`, used by `pre-spec` and `make lint`, finds a method that ties its check by hand to "the first ... after the render"; a new Estimate read by tests.
>   - Answer: agreed with the recommendation, (a).
> - **What happens to the Estimates that already passed but whose method uses the old wording?**
>   - Recommended: (a) this Case rewrites their methods too; promise and status stand.
>   - Answer: agreed, (a).
> - **Does the pattern also catch "after the change"?**
>   - Recommended: (a) yes, both "after the render" and "after the change".
>   - Answer: agreed, (a).

### Case 613.1 — Lint and pre-spec report a check by hand tied to the first moment after the render or the change

> **given:**
> `guppi/lint.py` and `tests/test_lint.py` — lint, which gains the class `moment` and its predicate, and its tests
> **＋** `guppi/prespec.py` and `tests/test_prespec.py` — pre-spec, which imports the predicate, and its tests
> **＋** `rule-lint` — the rule of lint; its classes live in the docstring of `guppi/lint.py`
> **＋** `rule-prespec` — the rule of pre-spec; its checks live in the docstring of `guppi/prespec.py`
> **＋** `rule-estimates-schema` and `vault/wiki/estimates/schema.yaml` — the `method` field and its render, which gain the form of a moment
> **＋** `vault/wiki/estimates/` — the Estimate pages lint reads
> **＋** the plan file of Plan Mode — the `then` blocks pre-spec reads
> **＋** `estimate-lint-reports-a-method-tied-to-a-one-off-moment` — the new promise

> **when:**
> `uv run guppi lint` reads the `method` field of each live Estimate under `vault/wiki/estimates/`.
> **＋** Or `uv run guppi prespec --check <plan> --session <id>` reads the `method` of a `create` of an Estimate, or of an `update` that carries `set: {method: …}`, in the `then` blocks of the plan file.

> **then:**
> A `method` that holds `by hand` and names the first of something after the render or after the change, with no `;` between the two, is one lint finding of the class `moment`.
> **＋** The same `method` in the plan gives one line `case N: <create|update> <slug>: method ties its reading by hand to the first moment after the render or the change`, which goes on to say that the method names the kind of its moment.
> **＋** Both sides judge by one predicate in `guppi/lint.py`, which `guppi/prespec.py` imports.
> **－** A `method` that names the kind of its moment, with no word "first", gets no such finding.
> **－** A `method` that names the first of an event without "after the render" or "after the change", such as the first close of a sprint, gets no such finding.
> **－** A `method` without `by hand` gets no such finding.
> **－** The finding does not replace the `method` finding of a `method` that names no form.

> **tasks:**
> - [ ] `guppi/lint.py`: one predicate of a reading by hand tied to the first moment after the render or the change; the class `moment` in the checks of an Estimate; the module docstring names the class
> - [ ] `guppi/prespec.py`: imports the predicate and gives the finding line on a `create` or a `set` of `method`; the module docstring names the check
> - [ ] `tests/test_lint.py` and `tests/test_prespec.py`: tests named `moment` for each wording, "after the render" and "after the change", a kind of moment, the first of an event with no "after", a method without `by hand`, and two clauses split by `;`
> - [ ] update `rule-estimates-schema`
>   - old:
>     ```
>     with where and when it is taken, a session start, the brief of a librarian's run.
>     ```
>   - new:
>     ```
>     with where and when it is taken, a session start, the brief of a librarian's run. A reading names its moment by its kind — a `/handoff`, a run of `/box`, a compaction — and any such moment after the render counts, in this session or in an earlier one; the word "first" stands only for an event that has never happened. A reading by hand tied to the first of something after the render or after the change is a finding of the class `moment` of lint and a finding of pre-spec, judged by one predicate of `guppi/lint.py` (case 613.1).
>     ```
>   - change: `a reading names its moment by its kind; a reading by hand tied to the first moment after the render or the change is a finding of lint and pre-spec (case 613.1)`
> - [ ] `uv run guppi render`: `vault/wiki/estimates/schema.yaml`
> - [ ] create `estimate-lint-reports-a-method-tied-to-a-one-off-moment`
>   - type: `estimate`
>   - ref: `rule-lint`
>   - kind: `QA`
>   - purpose: `Whether lint and pre-spec report a method that ties its reading by hand to the first moment after the render or after the change, by one predicate, and leave a method that names the kind of its moment`
>   - method: `uv run pytest tests/test_lint.py tests/test_prespec.py -k moment; the make lint of a later session, no moment finding on wiki/estimates/`
>   - tags: `[harness, workflow]`
> - [ ] read `estimate-lint-reports-a-method-tied-to-a-one-off-moment`

> **ratification:**
> ```
> - decision[case 613.1][update][rule-estimates-schema]{ref:rule-estimates-schema}
> - decision[case 613.1][create][estimate-lint-reports-a-method-tied-to-a-one-off-moment]{ref:rule-lint}{tags:harness,workflow}
> ```

### Case 613.2 — `/hi` reads a moment of an earlier session from the transcript of the session that held it

> **given:**
> `rule-skill-hi` and `.claude/skills/hi/SKILL.md` — the rule of `/hi` and its render, whose reading step changes
> **＋** `estimate-hi-takes-its-readings` — the promise of the reading step, replaced
> **＋** `vault/wiki/brief.md` — the brief whose readings `/hi` takes
> **＋** `raw/<date>/<hi HHMM>/frontier.md` — the Frontier whose `W` and `A` lines the step closes
> **＋** `vault/raw/<date>/event_log.md` — the event logs, which name each session by the first characters of its id
> **＋** the transcripts of Claude Code — one file per session, its name opening with the session's id
> **＋** `rule-work-mode` — the Work readings, which take what `/hi` leaves; unchanged

> **when:**
> The person types `/hi` on `UserPromptSubmit`, and the agent writes `raw/<date>/<hi HHMM>/frontier.md`, whose `## Work` holds the `pending` readings of `vault/wiki/brief.md` and whose `## Ask` holds its readings that only the person can take.

> **then:**
> In its first reply, before the question on the order, the agent takes each reading of an open `W` line whose every moment, as its `method` names it, is this `/hi` or has come in an earlier session.
> **＋** It reads what the method names from `vault/wiki/brief.md`, `git log`, `git status` and the commands of the method.
> **＋** It reads each moment of an earlier session from the transcript of the latest session that held it, found by the session ids of `vault/raw/<date>/event_log.md`, and each part of the method from the session where its moment came.
> **＋** It opens the page of each Estimate it reads and judges the reading against its `## Criterion`.
> **＋** It closes the `W` line of each reading taken as `[x] … · work` in `raw/<date>/<hi HHMM>/frontier.md`, then writes one `estimate[...]` line per reading in a `LEDGER` block of the reply, which ends in text.
> **＋** In the same reply, before the question on the order, it puts each open `A` line to the person as a question: the Estimate by slug and its question.
> **＋** When the person answers one, the agent closes its `A` line `[x] … · work` in `raw/<date>/<hi HHMM>/frontier.md` first, then writes its `estimate[...]` line, the answer as its result, in a `LEDGER` block of the reply, which ends in text.
> **－** The Frontier is still assembled with no page opened. Only the reading step opens the pages of the Estimates it reads.
> **－** A reading with a moment that has come in no session yet, or whose transcript Claude Code no longer holds, is not taken, and its `W` line stays open.
> **－** A reading whose `method` asks for a `/hi` run of its own, such as one outside plan mode, is not taken at `/hi`.
> **－** At `/hi` the agent changes no page and no file except `raw/<date>/<hi HHMM>/frontier.md`.

> **tasks:**
> - [ ] update `rule-skill-hi`
>   - old:
>     ```
>     take each reading of an open `W` line whose `method` names the `/hi` of a session or the librarian's run and whose whole method can be done now: from the brief, `git log`, `git status`, the commands the method names, and the transcript of the previous session for the librarian's report.
>     ```
>   - new:
>     ```
>     take each reading of an open `W` line whose whole method can be done now: each moment its `method` names is this `/hi` or has come in an earlier session (case 613.2). Read what the method names from the brief, `git log`, `git status` and the commands the method names, and each moment of an earlier session — the librarian's run, `/retro`, `/handoff` or any other — from the transcript of the latest session that held it: the event logs `vault/raw/<date>/event_log.md` name each session by the first characters of its id, and its transcript is the file of Claude Code whose name opens with that id; read each part of the method from the session where its moment came.
>     ```
>   - old:
>     ```
>     A reading whose `method` also names a later moment waits for that moment, its `/hi` part read then from the session's first turn; a reading whose `method` asks for a `/hi` run of its own is not taken here (case 508.1).
>     ```
>   - new:
>     ```
>     A reading with a moment that has come in no session yet, or whose transcript Claude Code no longer holds, waits for its next moment, and its line stays open; a reading whose `method` asks for a `/hi` run of its own is not taken here (cases 508.1, 613.2).
>     ```
>   - change: `/hi reads each moment of an earlier session from the transcript of the latest session that held it, part by part (case 613.2)`
> - [ ] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
> - [ ] update `estimate-hi-takes-its-readings`
>   - set: `{status: pending, purpose: "Whether /hi takes, in its first reply, each open W reading whose every moment is that /hi or came in an earlier session, reads each moment of an earlier session from the transcript of the latest session that held it, puts each open Ask line to the person as a question and writes the answer as its reading line, closes each line it ends, opens no page but the Estimates it reads, and leaves a reading with a moment not come, a transcript gone or a /hi run of its own", method: "by hand at a /hi of a later session whose open W lines hold a reading whose moment came in an earlier session: the first reply, its tool calls, its LEDGER block and frontier.md read against the Criterion, recorded in the estimate line"}`
>   - change: `the Criterion replaced whole — /hi reads a moment of an earlier session from its transcript (case 613.2)`
> - [ ] read `estimate-hi-takes-its-readings`

> **ratification:**
> ```
> - decision[case 613.2][update][rule-skill-hi]{ref:rule-skill-hi}
> - decision[case 613.2][update][estimate-hi-takes-its-readings]{ref:estimate-hi-takes-its-readings}
> ```

### Case 613.3 — The methods that tie a reading to a one-off moment name its kind

> **given:**
> `rule-estimates-schema` — the form of a `method`, which 613.1 sets
> **＋** `estimate-generate-rewords` — waiting; its `method` rewritten
> **＋** `estimate-case-check-sends-back-a-ratified-case-in-another-shape` — waiting; its `method` rewritten
> **＋** `estimate-hi-takes-a-conserved-spec` — waiting; its `method` rewritten
> **＋** `estimate-handoff-dispatches` — waiting; its `method` rewritten
> **＋** `estimate-case-check-requires-each-question-of-the-rounds` — waiting; its `method` rewritten
> **＋** `estimate-lint-runs-every-step` — waiting; its `method` rewritten
> **＋** `estimate-ledger-write-lifts` — waiting; its `method` rewritten
> **＋** `estimate-compact-recall-reloads` — waiting; its `method` rewritten
> **＋** `estimate-prespec-onward-sends-the-agent-on` — waiting; its `method` rewritten
> **＋** `estimate-case-check-sends-back-a-faulty-round` — waiting; its `method` rewritten
> **＋** `estimate-case-check-sends-back-a-faulty-case` — waiting; its `method` rewritten
> **＋** `estimate-carry-over-writes` — waiting; its `method` rewritten
> **＋** `estimate-case-check-sends-back-a-case-number-held-by-another-agent` — waiting; its `method` rewritten
> **＋** `estimate-ratification-ledger-line-form` — waiting; its `method` rewritten
> **＋** `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — waiting; its `method` rewritten
> **＋** `estimate-spec-write-reaches-the-approved-spec` — waiting; its `method` rewritten
> **＋** `estimate-spec-box-runs-a-conserved-spec` — waiting; its `method` rewritten
> **＋** `estimate-retro-onward-sends-the-agent-to-the-handoff` — waiting; its `method` rewritten
> **＋** `estimate-retro-loads` — waiting; its `method` rewritten
> **＋** `estimate-orchestration-defers-in-one-reply` — waiting; its `method` rewritten
> **＋** `estimate-retro-runs-on-to-the-handoff` — waiting; its `method` rewritten
> **＋** `estimate-orchestration-signs-a-batch-together` — waiting; its `method` rewritten
> **＋** `estimate-spec-capture-offers-the-fork` — waiting; its `method` rewritten
> **＋** `estimate-work-mode-takes-the-work-readings` — waiting; its `method` rewritten
> **＋** `estimate-where-to-stop-stops-only-on-its-conditions` — waiting; its `method` rewritten
> **＋** `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` — waiting; its `method` rewritten
> **＋** `estimate-handoff-holds-each-fact-once` — waiting; its `method` rewritten
> **＋** `estimate-prespec-onward-reads-the-decisions-of-the-session` — passed; its `method` rewritten
> **＋** `estimate-ratification-loaded` — passed; its `method` rewritten
> **＋** `estimate-orchestration-loaded` — passed; its `method` rewritten
> **＋** `estimate-spec-write-writes-a-defer` — passed; its `method` rewritten
> **＋** `estimate-prespec-reconciles` — passed; its `method` rewritten
> **＋** `estimate-retro-red-in-the-baseline-is-not-charged` — passed; its `method` rewritten
> **＋** `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` — passed; its `method` rewritten
> **＋** `estimate-harness-make-runs-in-both-shells` — passed; its `method` rewritten
> **＋** `estimate-spec-write-removes-a-superseded-case` — passed; its `method` rewritten
> **＋** `estimate-spec-write-checks-the-written-case` — passed; its `method` rewritten

> **when:**
> Someone reads the `method` of an Estimate that this sub-case rewrites, to know at which moment its reading is taken.

> **then:**
> The `method` names the kind of its moment, and any such moment after the render, in this session or an earlier one, is its moment.
> **＋** The `## Criterion` and the `status` of each Estimate stand.
> **－** No `method` of them ties a reading by hand to the first of something after the render or after the change.

> **tasks:**
> - [ ] update `estimate-generate-rewords`
>   - set: `{method: "pytest tests/test_generate.py on a temp vault with three pages and an archive; the live reading a librarian's run that applies a reword"}`
>   - change: `method names the kind of its moment (case 613.3)`
> - [ ] update `estimate-case-check-sends-back-a-ratified-case-in-another-shape`
>   - set: `{method: "uv run pytest tests/test_casecheck.py -k shape, then by hand an answer of case-guppi the hook sends back for this reason"}`
>   - change: `method names the kind of its moment (case 613.3)`
> - [ ] update `estimate-hi-takes-a-conserved-spec`
>   - set: `{method: "uv run guppi render --check; by hand, a session whose person takes a conserved Spec at the Frontier: frontier.md, the title line of the plan file and the session's ledger read against the Criterion"}`
>   - change: `method names the kind of its moment (case 613.3)`
> - [ ] update `estimate-handoff-dispatches`
>   - set: `{method: "by hand at the /handoff of a later session and at the /handoff of a session that /box runs: the event log, handoff.md, the dispatch line and git log"}`
>   - change: `method names the kind of its moment (case 613.3)`
> - [ ] update `estimate-case-check-requires-each-question-of-the-rounds`
>   - set: `{method: "pytest tests/test_casecheck.py -k rounds over a temp agent transcript: a round and a Case whose recommend holds every title, one that misses a title, a title asked in two rounds, a round out of form whose titles are not required, an answer with no round; then by hand a Case the hook sends back for a missing title"}`
>   - change: `method names the kind of its moment (case 613.3)`
> - [ ] update `estimate-lint-runs-every-step`
>   - set: `{method: "by hand, the make lint of the Baseline of a /work of a later session whose backlog step is red: the steps that printed, the page findings of guppi lint and the exit code, recorded in the estimate line"}`
>   - change: `method names the kind of its moment (case 613.3)`
> - [ ] update `estimate-ledger-write-lifts`
>   - set: `{method: "pytest in tests/test_ledger.py and tests/test_gate.py with piped payloads against a temp vault; by hand once, the ledger of a session whose reply that ends Retro follows a refusal of a Stop hook in the same stretch: its lines written at that Stop, with its time"}`
>   - change: `method names the kind of its moment (case 613.3)`
> - [ ] update `estimate-compact-recall-reloads`
>   - set: `{method: "pytest tests/test_recall.py on a temp project; live — a compaction of a working session, by hand, the hook's text in the context after it"}`
>   - change: `method names the kind of its moment (case 613.3)`
> - [ ] update `estimate-prespec-onward-sends-the-agent-on`
>   - set: `{method: "uv run pytest tests/test_onward.py tests/test_ledger.py; by hand at a Plan Mode at which the ledger hook refuses a line of the reply that acknowledges the last ratification: the transcript, the event log and frontier.md, recorded in the estimate line"}`
>   - change: `method names the kind of its moment (case 613.3)`
> - [ ] update `estimate-case-check-sends-back-a-faulty-round`
>   - set: `{method: "uv run pytest tests/test_casecheck.py -k round_form over a temp agent transcript: a round in form, a title line without the colon, a question with no Now line, no lone Options label, no option with an After item and no arrow line, the same faulty round given twice, a Fact answer, an answer with a Case, an unreadable transcript; then by hand a round the hook sends back live, its stderr and the round case-guppi gave again"}`
>   - change: `method names the kind of its moment (case 613.3)`
> - [ ] update `estimate-case-check-sends-back-a-faulty-case`
>   - set: `{method: "uv run pytest tests/test_casecheck.py -k subagent, then by hand an answer of case-guppi the hook sends back, a file of cases/ it writes, and a live round after a built Case, which is not sent back for that Case and leaves its stored entry and its file as they stood"}`
>   - change: `method names the kind of its moment (case 613.3)`
> - [ ] update `estimate-carry-over-writes`
>   - set: `{method: "uv run guppi render --check; by hand, a /carry after the fork of ExitPlanMode — the tree, vault/wiki/brief.md, carry.md, vault/wiki/backlog.md, the commit and git branch read"}`
>   - change: `method names the kind of its moment (case 613.3)`
> - [ ] update `estimate-case-check-sends-back-a-case-number-held-by-another-agent`
>   - set: `{method: "uv run pytest tests/test_casecheck.py -k clash, then by hand an answer of case-guppi the hook sends back for this reason"}`
>   - change: `method names the kind of its moment (case 613.3)`
> - [ ] update `estimate-ratification-ledger-line-form`
>   - set: `{method: "by hand: the ledger and the preview of a session where a lesson and the Case that closes its cause stand together, and of a Case that takes up a decision with more than one Case in its deferred_by"}`
>   - change: `method names the kind of its moment (case 613.3)`
> - [ ] update `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`
>   - set: `{method: "uv run guppi render --check; by hand, a /work the agent calls at the fork, a /work the person types and a /work that /box calls: the branch, work.md, the ticks of the Spec, the carry.md of the folder and each Expected red line read against the Criterion, and, where a substitution came back empty, the agent's own run of its command, recorded in the estimate line"}`
>   - change: `method names the kind of its moment (case 613.3)`
> - [ ] update `estimate-spec-write-reaches-the-approved-spec`
>   - set: `{method: "uv run pytest tests/test_ratified.py -k approved_spec; by hand, a Case ratified in Work Mode"}`
>   - change: `method names the kind of its moment (case 613.3)`
> - [ ] update `estimate-spec-box-runs-a-conserved-spec`
>   - set: `{method: "uv run guppi render --check; by hand, a session that takes a conserved Spec at the Frontier and runs it by /box: git log, the branches, the folders of the session and of the conserved Spec, the dispatch line and the librarian's commit, recorded in the estimate line"}`
>   - change: `method names the kind of its moment (case 613.3)`
> - [ ] update `estimate-retro-onward-sends-the-agent-to-the-handoff`
>   - set: `{method: "uv run pytest tests/test_onward.py tests/test_ledger.py; by hand at an end of Retro at which the ledger hook refuses a line: the transcript, the event log and handoff.md, recorded in the estimate line"}`
>   - change: `method names the kind of its moment (case 613.3)`
> - [ ] update `estimate-retro-loads`
>   - set: `{method: "by hand at a /retro, and at a /retro of a session that /box runs, recorded in the estimate line"}`
>   - change: `method names the kind of its moment (case 613.3)`
> - [ ] update `estimate-orchestration-defers-in-one-reply`
>   - set: `{method: "by hand, a decision the person asks to put off, its line of frontier.md closed [-] … · defer case N, in a reply that leaves no line under the Cases heading of frontier.md open; a sprint item put off or a backlog item kept is not this reading"}`
>   - change: `method names the kind of its moment (case 613.3)`
> - [ ] update `estimate-retro-runs-on-to-the-handoff`
>   - set: `{method: "by hand at a run from /work to the librarian, and for the answer to a refusal of the ledger hook at a Retro where that hook refuses a line: the replies of the turn, the ledger, git log and handoff.md read against the Criterion, recorded in the estimate line"}`
>   - change: `method names the kind of its moment (case 613.3)`
> - [ ] update `estimate-orchestration-signs-a-batch-together`
>   - set: `{method: "by hand at a Plan Mode of a later session in which the person's word asks that a ratified Case change: the SendMessage calls and the replies from that word to the acknowledging reply, read in the transcript"}`
>   - change: `method names the kind of its moment (case 613.3)`
> - [ ] update `estimate-spec-capture-offers-the-fork`
>   - set: `{method: "uv run pytest tests/test_spec.py -k 'fork or box'; by hand, an ExitPlanMode of a session, and an ExitPlanMode of a session that took a conserved Spec"}`
>   - change: `method names the kind of its moment (case 613.3)`
> - [ ] update `estimate-work-mode-takes-the-work-readings`
>   - set: `{method: "by hand at a /work and at a /work that /box calls: the replies after the last task, their LEDGER blocks and frontier.md read against the Criterion, recorded in the estimate line"}`
>   - change: `method names the kind of its moment (case 613.3)`
> - [ ] update `estimate-where-to-stop-stops-only-on-its-conditions`
>   - set: `{method: "by hand at a run from /work to the librarian, and at a run of /box: the context of /work and of /box, the replies of the turn and the Spec read against the Criterion, recorded in the estimate line; a condition that does not arise is named as not exercised"}`
>   - change: `method names the kind of its moment (case 613.3)`
> - [ ] update `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note`
>   - set: `{method: "one reading by hand at a /retro in a session whose work.md names a check under Expected red, recorded in the estimate line"}`
>   - change: `method names the kind of its moment (case 613.3)`
> - [ ] update `estimate-handoff-holds-each-fact-once`
>   - set: `{method: "one reading by hand at a /handoff, against the close of its Retro, recorded in the estimate line"}`
>   - change: `method names the kind of its moment (case 613.3)`
> - [ ] update `estimate-prespec-onward-reads-the-decisions-of-the-session`
>   - set: `{method: "uv run pytest tests/test_onward.py; by hand at a Case ratified again with unchanged decision lines in Plan Mode, at the reply that closes the last line under Cases after a later message of the person: the transcript, ledger.md and the times of the files under cases/, recorded in the estimate line"}`
>   - change: `method names the kind of its moment (case 613.3)`
> - [ ] update `estimate-ratification-loaded`
>   - set: `{method: "uv run guppi render --check; by hand at a /hi of a later session, vault/wiki/ratification.md in the first turn's context and its paragraphs compared with CLAUDE.md, case-schema.md and orchestration.md"}`
>   - change: `method names the kind of its moment (case 613.3)`
> - [ ] update `estimate-orchestration-loaded`
>   - set: `{method: "uv run guppi render --check; by hand at a /hi of a later session, vault/wiki/orchestration.md in the first turn's context and its paragraphs compared with CLAUDE.md, case-schema.md and ratification.md"}`
>   - change: `method names the kind of its moment (case 613.3)`
> - [ ] update `estimate-spec-write-writes-a-defer`
>   - set: `{method: "uv run pytest tests/test_ratified.py -k defer, then by hand a defer the person asks for"}`
>   - change: `method names the kind of its moment (case 613.3)`
> - [ ] update `estimate-prespec-reconciles`
>   - set: `{method: "One reading by hand of a /pre-spec, written into the estimate line — the exception the Method rule allows"}`
>   - change: `method names the kind of its moment (case 613.3)`
> - [ ] update `estimate-retro-red-in-the-baseline-is-not-charged`
>   - set: `{method: "one reading by hand at a /retro in a session whose work.md Baseline holds a failing test or a lint finding line, recorded in the estimate line"}`
>   - change: `method names the kind of its moment (case 613.3)`
> - [ ] update `estimate-case-build-keeps-the-old-form-until-the-writer-is-live`
>   - set: `{method: "one reading by hand at a Case case-guppi builds that changes a reader and the text or writer it reads, recorded in the estimate line"}`
>   - change: `method names the kind of its moment (case 613.3)`
> - [ ] update `estimate-harness-make-runs-in-both-shells`
>   - set: `{method: "by hand, make help, make style, make test and make lint from PowerShell and from Git Bash on Windows, in a session"}`
>   - change: `method names the kind of its moment (case 613.3)`
> - [ ] update `estimate-spec-write-removes-a-superseded-case`
>   - set: `{method: "uv run pytest tests/test_ratified.py -k superseded; by hand, a supersedes of a Case of the same session"}`
>   - change: `method names the kind of its moment (case 613.3)`
> - [ ] update `estimate-spec-write-checks-the-written-case`
>   - set: `{method: "uv run pytest tests/test_ratified.py -k checks_the_written; by hand, a ratification of a session"}`
>   - change: `method names the kind of its moment (case 613.3)`

> **ratification:**
> ```
> - decision[case 613.3][update][estimate-generate-rewords]{ref:estimate-generate-rewords}
> - decision[case 613.3][update][estimate-case-check-sends-back-a-ratified-case-in-another-shape]{ref:estimate-case-check-sends-back-a-ratified-case-in-another-shape}
> - decision[case 613.3][update][estimate-hi-takes-a-conserved-spec]{ref:estimate-hi-takes-a-conserved-spec}
> - decision[case 613.3][update][estimate-handoff-dispatches]{ref:estimate-handoff-dispatches}
> - decision[case 613.3][update][estimate-case-check-requires-each-question-of-the-rounds]{ref:estimate-case-check-requires-each-question-of-the-rounds}
> - decision[case 613.3][update][estimate-lint-runs-every-step]{ref:estimate-lint-runs-every-step}
> - decision[case 613.3][update][estimate-ledger-write-lifts]{ref:estimate-ledger-write-lifts}
> - decision[case 613.3][update][estimate-compact-recall-reloads]{ref:estimate-compact-recall-reloads}
> - decision[case 613.3][update][estimate-prespec-onward-sends-the-agent-on]{ref:estimate-prespec-onward-sends-the-agent-on}
> - decision[case 613.3][update][estimate-case-check-sends-back-a-faulty-round]{ref:estimate-case-check-sends-back-a-faulty-round}
> - decision[case 613.3][update][estimate-case-check-sends-back-a-faulty-case]{ref:estimate-case-check-sends-back-a-faulty-case}
> - decision[case 613.3][update][estimate-carry-over-writes]{ref:estimate-carry-over-writes}
> - decision[case 613.3][update][estimate-case-check-sends-back-a-case-number-held-by-another-agent]{ref:estimate-case-check-sends-back-a-case-number-held-by-another-agent}
> - decision[case 613.3][update][estimate-ratification-ledger-line-form]{ref:estimate-ratification-ledger-line-form}
> - decision[case 613.3][update][estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline]{ref:estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline}
> - decision[case 613.3][update][estimate-spec-write-reaches-the-approved-spec]{ref:estimate-spec-write-reaches-the-approved-spec}
> - decision[case 613.3][update][estimate-spec-box-runs-a-conserved-spec]{ref:estimate-spec-box-runs-a-conserved-spec}
> - decision[case 613.3][update][estimate-retro-onward-sends-the-agent-to-the-handoff]{ref:estimate-retro-onward-sends-the-agent-to-the-handoff}
> - decision[case 613.3][update][estimate-retro-loads]{ref:estimate-retro-loads}
> - decision[case 613.3][update][estimate-orchestration-defers-in-one-reply]{ref:estimate-orchestration-defers-in-one-reply}
> - decision[case 613.3][update][estimate-retro-runs-on-to-the-handoff]{ref:estimate-retro-runs-on-to-the-handoff}
> - decision[case 613.3][update][estimate-orchestration-signs-a-batch-together]{ref:estimate-orchestration-signs-a-batch-together}
> - decision[case 613.3][update][estimate-spec-capture-offers-the-fork]{ref:estimate-spec-capture-offers-the-fork}
> - decision[case 613.3][update][estimate-work-mode-takes-the-work-readings]{ref:estimate-work-mode-takes-the-work-readings}
> - decision[case 613.3][update][estimate-where-to-stop-stops-only-on-its-conditions]{ref:estimate-where-to-stop-stops-only-on-its-conditions}
> - decision[case 613.3][update][estimate-retro-red-check-of-an-updated-page-is-a-handoff-note]{ref:estimate-retro-red-check-of-an-updated-page-is-a-handoff-note}
> - decision[case 613.3][update][estimate-handoff-holds-each-fact-once]{ref:estimate-handoff-holds-each-fact-once}
> - decision[case 613.3][update][estimate-prespec-onward-reads-the-decisions-of-the-session]{ref:estimate-prespec-onward-reads-the-decisions-of-the-session}
> - decision[case 613.3][update][estimate-ratification-loaded]{ref:estimate-ratification-loaded}
> - decision[case 613.3][update][estimate-orchestration-loaded]{ref:estimate-orchestration-loaded}
> - decision[case 613.3][update][estimate-spec-write-writes-a-defer]{ref:estimate-spec-write-writes-a-defer}
> - decision[case 613.3][update][estimate-prespec-reconciles]{ref:estimate-prespec-reconciles}
> - decision[case 613.3][update][estimate-retro-red-in-the-baseline-is-not-charged]{ref:estimate-retro-red-in-the-baseline-is-not-charged}
> - decision[case 613.3][update][estimate-case-build-keeps-the-old-form-until-the-writer-is-live]{ref:estimate-case-build-keeps-the-old-form-until-the-writer-is-live}
> - decision[case 613.3][update][estimate-harness-make-runs-in-both-shells]{ref:estimate-harness-make-runs-in-both-shells}
> - decision[case 613.3][update][estimate-spec-write-removes-a-superseded-case]{ref:estimate-spec-write-removes-a-superseded-case}
> - decision[case 613.3][update][estimate-spec-write-checks-the-written-case]{ref:estimate-spec-write-checks-the-written-case}
> ```
