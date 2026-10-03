## Case 607 — The check of a Case stops at a round or a Fact answer and does not check an earlier Case again

> **context:**
> When `case-guppi` answers, the `SubagentStop` hook `uv run guppi casecheck --subagent` of `rule-case-check` looks for the answer in the agent's transcript. It takes the newest output that holds a Case heading, and it reaches back to an older output when the newest one holds none. The reach-back exists for one case. A subagent can pass its Case through a `SubagentHandback` call and then end with a short summary text, as `lesson-hooks-subagentstop-reads-the-last-text-not-the-handback` records, and the hook must still check that Case (case 434). The reach-back also goes past a round or a `**Fact:**` answer. When the agent answers a message on a Case it built with a new round, the hook checks the earlier Case again. That check uses the titles of every round, the new round's titles too. In session 2300 this sent the second round on Case 601 back once, because the earlier Case 601 held no `recommend` item for that round's titles. Case 601 named this as not done, and the handoff of session 2300 put it under Next session. The same re-check stores the earlier Case again with a new time, and it writes its file again when it passes.
>
> Case 607.1 makes the hook stop at the newest output that is a Case, a round or a `**Fact:**` answer. Only a Case gets the check of a Case. A summary text after a hand-back is none of the three, so it is still passed over. A plain prose answer that is none of the three still reaches back to an earlier Case. That is not done here: no answer of the agent's rules takes that form. 607.1 replaces the Criterion of `estimate-case-check-sends-back-a-faulty-case` whole, and it sets that Estimate's `method` anew with a check by hand of the first live round after a built Case. Its `purpose` still holds. 607.1 replaces only the first `then` line and adds two `－` lines. Every other line is carried word for word. The check of this answer noted that the old first line is not carried. That is on purpose: the new first line replaces it.
>
> A `**Fact:**` answer is judged by one predicate that `is_round` and the reading of the answer share (`rule-one-judgment-one-implementation`). It is the test `is_round` already makes, lines 937 to 951 of `guppi/casecheck.py` (case 601.1): a text with no Case heading in which a line that opens with `**Fact:**` stands before any line that opens with `❓`. The predicate is only moved into a function of its own, so `is_round` answers as before. `estimate-case-check-refuses-text-before-a-round` rests on `is_round` in its line 21, and that line stays true. `orchestration.md`, line 13, and `estimate-orchestration-shows-the-built-case`, line 23, say that `case-guppi` answers a fact under a first line `**Fact:**`. Those lines set the form the agent writes. The predicate accepts that form and reads a little wider, so it does not contradict them, and their texts do not change. Line 25 of `estimate-orchestration-forwards-a-discussion-question` says that the hook of `rule-case-check` reads a `**Fact:**` answer as no Case. Today the reach-back makes that false whenever a Case stands earlier in the transcript. 607.1 makes it true, so the line stands.
>
> Case 607.2 replaces the Criterion of `estimate-case-check-sends-back-a-faulty-round`. Its line said that the findings of a round stand beside those of the check of a Case in one exit 2. After 607.1 a round gets no check of a Case, so that line would be false. A new `－` line replaces it. The first `then` line of that Estimate said that a round's first line that is not blank is not `**Fact:**`. That is narrower than `is_round` as the code holds it, so 607.2 rewords it to the shared predicate. Every other line is carried. The check of this answer noted that the old first line is not carried. That is on purpose. The `purpose` and `method` of that Estimate speak of the form of a round, not of the changed lines, so they stand.
>
> The check of this answer gave two more notes, on lines of the two sub-cases that share words. In each pair, both lines stand:
> - The line of 607.2 that a round gets no check of a Case, and the second `－` line of 607.1, describe the same fact from two sides: the reading of the answer in 607.1, and the exit of the round check in 607.2.
> - The `－` line of 607.2 that lists what the round check does not judge is carried unchanged from its Estimate. The first `then` line of 607.1 says which output the check of a Case takes as its answer. They share the words for a Case heading and a `**Fact:**` answer, but they state different things.
>
> The other Estimates of `rule-case-check` stand. Their Criteria speak of an answer that holds a Case, of the `Stop` comparison, or of an error of the run, and none of them names an earlier output. `estimate-case-check-requires-each-question-of-the-rounds` still takes its titles from the earlier outputs with no Case heading. `estimate-case-build-writes-the-case` says the hook neither checks nor stores a round as a Case, and this Case makes that more true. Both stay true. The Case creates no page, so the vault query was not run. `rule-case-rebuild-cost`, a page in `draft` deferred by two Decisions, names a merge of a changed sub-case on the same hook. This Case does not take it up, and the two do not conflict.
>
> Frame checks:
> - A Grep of `estimate-case-check-sends-back-a-faulty-(case|round)` over the repository outside `vault/raw/` and `vault/archive/` printed 42 files. Outside `decisions/`, `brief.md` and `log.md` the hits are `estimate-case-check-sends-back-a-faulty-case.md` itself and `rule-case-check.md`, in its `estimates` field. Neither text changes.
> - A Grep of `holds a Case heading|earlier output` over the same paths printed 10 files:
>   - the three Estimates `estimate-case-check-sends-back-a-faulty-case.md`, `estimate-case-check-sends-back-a-faulty-round.md` and `estimate-case-check-requires-each-question-of-the-rounds.md`
>   - `guppi/casecheck.py`, whose docstring both sub-cases change
>   - the Decision pages of cases 601, 477.1 to 477.4 and 434, which are not read
> - A Grep of `Fact:|reads it as no Case|is_round` over `vault/wiki/` outside `decisions/` printed these files:
>   - `brief.md` and `log.md`, which are not read
>   - `rule-case-build.md`, `rule-orchestration.md` and `orchestration.md`, which set the form the agent writes a fact in
>   - `estimate-case-check-refuses-text-before-a-round.md`, `estimate-case-check-sends-back-a-faulty-round.md`, `estimate-orchestration-forwards-a-discussion-question.md` and `estimate-orchestration-shows-the-built-case.md`, treated above
> - A Grep of `SubagentStop` over `vault/wiki/rules/` and `.claude/` printed:
>   - `rule-case-check.md`, in a History line
>   - `rule-case-rebuild-cost.md`
>   - `rule-hook-registry.md`
>   - `rule-orchestration.md`
>   - `rule-spec-reconcile.md`
>   - `.claude/settings.json`
>
>   In `.claude/settings.json` the one hook on that event is `uv run guppi casecheck --subagent`. `rule-orchestration` and `rule-spec-reconcile` name the file the hook writes from an answer that holds a Case. That stays true, and none of these hits sets what the hook does with a round.

> **problem:**
> When `case-guppi` answers with a round or a `**Fact:**` answer after a Case it built, the `SubagentStop` check of a Case goes back to that earlier Case and checks it again, against the titles of the new round too. It sends back a sound round for a fault of the earlier Case, and it stores that Case again and writes its file again.

> **recommend:**
> - **Which output should the hook take as the answer?**
>   - Recommended: (a) the newest output that is a Case, a round or a Fact answer. A summary after a hand-back is still passed over, and only a Case gets the check of a Case.
>   - Answer: agreed with the recommendation, (a).
> - **What should become of the round check's promise that both checks run in one exit?**
>   - Recommended: (a) replace the Criterion of `estimate-case-check-sends-back-a-faulty-round` too, in a second sub-case. Its line says instead that a round gets no check of a Case in the same run.
>   - Answer: agreed with the recommendation, (a).
> - **How should done be checked for the main change?**
>   - Recommended: (a) replace the Criterion of `estimate-case-check-sends-back-a-faulty-case` whole, and add to its method a check by hand that the first live round after a built Case is not sent back for that Case.
>   - Answer: agreed with the recommendation, (a).

### Case 607.1 — The check of a Case takes the newest Case, round or Fact answer as the answer

> **given:**
> `estimate-case-check-sends-back-a-faulty-case` — the promise of the check of a Case; its Criterion is replaced whole and its `method` is set anew
> **＋** `estimate-case-check-sends-back-a-faulty-round` — the promise of the form of a round, which a line of this Criterion names; changed by 607.2
> **＋** `guppi/casecheck.py` and `tests/test_casecheck.py` — `answer_of`, `is_round`, the predicate of a Fact answer they share, the module docstring, and their tests
> **＋** `guppi/ratified.py` and `guppi/prespec.py` — the readings the check imports; unchanged
> **＋** `agent_transcript_path` and `last_assistant_message` of the `SubagentStop` payload — the outputs of `case-guppi` the check reads
> **＋** `<plan>.checked.json` — the store beside the plan file of the session
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md` — the file of a Case that passed
> **＋** `rule-case-check` — the rule of the check; unchanged

> **when:**
> `SubagentStop` fires when `case-guppi` answers; its payload carries `last_assistant_message`, `agent_transcript_path` and `stop_hook_active`, and it may fire twice after one message to the subagent, the second time after a `SubagentHandback` call, with `stop_hook_active` true though no hook exited 2.

> **then:**
> `uv run guppi casecheck --subagent` takes as the answer the newest output of the subagent in `agent_transcript_path` that holds a Case heading, that `is_round` of `guppi/casecheck.py` finds a round, or that is a `**Fact:**` answer, a text with no Case heading in which a line that opens with `**Fact:**` stands before any line that opens with `❓` — the `message` input of a `SubagentHandback` tool call or the text of an assistant message, whichever stands later — or `last_assistant_message` when `agent_transcript_path` is not readable or holds no such output.
> **＋** It reads each Case of the answer in the chat form, by the functions of `guppi/ratified.py`, builds each Case's section of the Spec in memory, as the Spec hook writes it, and runs `judge` of `guppi/prespec.py` over them, the decision lines of the `ratification` fence standing for the ledger.
> **＋** The categories whose schema rule the session changes, whose `create` and `defer` items `judge` does not judge by their keys, it takes from the decision lines of the `ratification` fences and of the session's window.
> **＋** It checks the chat form besides: the sections in the order of the schema, none missing that the schema requires, and a `ratification` that holds one untagged fence of ledger lines and nothing else.
> **＋** Each Case of the answer is stored, its text as the answer holds it, with its findings and the time of the store, in `<plan>.checked.json` beside the plan file of the session.
> **＋** When no Case of the answer has findings, it writes the Cases of the answer, as the store holds their text, into `raw/<date>/<hi HHMM>/cases/case-<N>.md`, N the id of the top-level Case: the file is replaced whole when the answer holds the top-level Case, and only the section of a sub-case is replaced when the answer holds that sub-case alone.
> **＋** A finding exits 2 with the findings on stderr, each naming its Case, and `case-guppi` answers again, whatever `stop_hook_active` says.
> **－** An answer with a finding writes no file, and a finding for a Case whose text the store already holds with findings is stored again and exits 0, so an unchanged answer is not sent back twice.
> **－** An output that is none of the three, such as a short text after a `SubagentHandback` call, is passed over for an older output.
> **－** An answer that is a round or a `**Fact:**` answer gets none of these checks of a Case, and a Case in an earlier output of the subagent is not checked, stored or written again.
> **－** An answer of another agent, and one whose outputs hold no Case heading, get none of these checks of a Case and are not stored or written. A session with no plan file is not sent back for a fault of a Case.
> **－** The form of the questions of a round is the promise of `estimate-case-check-sends-back-a-faulty-round`, not of this one.

> **tasks:**
> - [ ] update `estimate-case-check-sends-back-a-faulty-case`
>   - set: `{status: pending, method: "uv run pytest tests/test_casecheck.py -k subagent, then by hand the first answer of case-guppi the hook sends back, the first file of cases/ it writes, and the first live round after a built Case, which is not sent back for that Case and leaves its stored entry and its file as they stood"}`
>   - change: `the Criterion replaced whole — the answer is the newest output that is a Case, a round or a Fact answer; a round or a Fact answer gets no check of a Case, and an earlier Case is not checked, stored or written again (case 607.1)`
> - [ ] `guppi/casecheck.py`: the Fact test of `is_round` becomes a predicate of its own, unchanged in what it answers: a text with no Case heading in which a line that opens with `**Fact:**` stands before any line that opens with `❓`, the indent set aside. `is_round` and `answer_of` both use it. `answer_of` walks back from the newest output and returns the first one that holds a Case heading, that `is_round` finds a round, or that the predicate finds a Fact answer, else `last_assistant_message`. `subagent` checks, stores and writes nothing for an answer with no Case. The module docstring on the answer says so, and its sentence that an answer with no Case heading, where no earlier output holds one either, is not checked becomes: an answer that is a round or a Fact answer is not checked or stored as a Case, and an earlier Case is not read again.
> - [ ] `tests/test_casecheck.py`, each test named `subagent`: a Case followed by a round in form whose titles its `recommend` lacks exits 0 and leaves the stored entry, its time and the case file unchanged; a Case followed by a Fact answer does the same; the existing tests of a Case by hand-back followed by a summary text still pass.
> - [ ] `uv run pytest tests/test_casecheck.py -k subagent`
> - [ ] read `estimate-case-check-sends-back-a-faulty-case`

> **ratification:**
> ```
> - decision[case 607.1][update][estimate-case-check-sends-back-a-faulty-case]{ref:rule-case-check}
> ```

### Case 607.2 — A round's exit carries the findings of its form alone

> **given:**
> `estimate-case-check-sends-back-a-faulty-round` — the promise of the check of the form of a round; its Criterion is replaced whole
> **＋** `estimate-case-check-sends-back-a-faulty-case` — the promise of 607.1, which takes no round as the answer of the check of a Case
> **＋** `guppi/casecheck.py` and `tests/test_casecheck.py` — `is_round`, `round_form`, `faulty_round`, `subagent`, the module docstring, and their tests
> **＋** `agent_transcript_path` of the `SubagentStop` payload — the transcript of `case-guppi`, whose outputs the check reads
> **＋** `.claude/skills/grill-me/SKILL.md` — the question template the check reads; unchanged

> **when:**
> `SubagentStop` fires when `case-guppi` answers, and `uv run guppi casecheck --subagent` reads its newest output in `agent_transcript_path`: a text, or the `message` of a `SubagentHandback` call, whichever stands later.

> **then:**
> `uv run guppi casecheck --subagent` takes that output as a round when `is_round` of `guppi/casecheck.py`, the one test of a round that the `Stop` run also imports, finds it one. That means three things hold: it holds no Case heading; no line that opens with `**Fact:**` stands before its first line that opens with `❓`; and one of its lines opens with the mark `❓`, with the indent of each line set aside.
> **＋** Each line that opens with `❓` opens a question, and the question runs to the next such line or to the end of the output. The text before the first question, the `**Context:**` paragraph, is not judged.
> **＋** A question is out of form when its first line does not match the title line `❓ **Q<n>** - **<title>**:` of `.claude/skills/grill-me/SKILL.md`, judged by `QUESTION_LINE` of `guppi/casecheck.py`.
> **＋** A question is out of form when it holds no line that opens with `**Now:**`, or no line that holds `**Options:**` and nothing else.
> **＋** A question is out of form when it holds no line that opens with `➡️`, or when none of its lines that open with `🔹` has a line that opens with `- **After:**` after it, before the next line that opens with `🔹` or `➡️`.
> **＋** A round with a question out of form exits 2. Its stderr names each such question by its first line and each part it misses, and tells `case-guppi` to answer with the round whole again, and `case-guppi` answers again.
> **－** A round gets none of the checks of a Case in the same run, and no earlier Case of the transcript is checked for it, so the exit 2 of a round carries the findings of its form alone.
> **－** A round out of form is not sent back again when an earlier output of `case-guppi` in `agent_transcript_path` holds the same text, trailing spaces aside.
> **－** A round in form gives no finding and prints nothing of its own.
> **－** These are not judged here: an output with a Case heading, a `**Fact:**` answer, an output with no line that opens with `❓`, an answer of another agent, and an `agent_transcript_path` that cannot be read.
> **－** The check of the form stores nothing and writes no file, whether or not the session has a plan file.
> **－** A round as the main agent shows it in the chat is not judged here.

> **tasks:**
> - [ ] update `estimate-case-check-sends-back-a-faulty-round`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a round is known by is_round as the code holds it, and gets no check of a Case in the same run, so its exit 2 carries the findings of its form alone (case 607.2)`
> - [ ] `guppi/casecheck.py`: the docstring paragraph on the form of a round says that a round gets no check of a Case, and its exit 2 carries the findings of its form alone, in place of the sentence that the findings join those of the check of a Case in one exit 2.
> - [ ] `tests/test_casecheck.py`: a Case followed by a round out of form exits 2 with the findings of the form alone, none naming the earlier Case; the test is named `round_form`.
> - [ ] `uv run pytest tests/test_casecheck.py -k round_form`
> - [ ] read `estimate-case-check-sends-back-a-faulty-round`

> **ratification:**
> ```
> - decision[case 607.2][update][estimate-case-check-sends-back-a-faulty-round]{ref:rule-case-check}
> ```
