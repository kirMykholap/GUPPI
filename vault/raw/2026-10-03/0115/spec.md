<!-- approved 02:59:42 · session cf8077b8 -->

# Spec — session 0115, 2026-10-03

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

```then
update:
- slug: estimate-case-check-sends-back-a-faulty-case
  set:
    status: pending
    method: uv run pytest tests/test_casecheck.py -k subagent, then by hand the first answer of case-guppi the hook sends back, the first file of cases/ it writes, and the first live round after a built Case, which is not sent back for that Case and leaves its stored entry and its file as they stood
  change: the Criterion replaced whole — the answer is the newest output that is a Case, a round or a Fact answer; a round or a Fact answer gets no check of a Case, and an earlier Case is not checked, stored or written again (case 607.1)
```

```tasks
- [x] update `estimate-case-check-sends-back-a-faulty-case`
- [x] `guppi/casecheck.py`: the Fact test of `is_round` becomes a predicate of its own, unchanged in what it answers: a text with no Case heading in which a line that opens with `**Fact:**` stands before any line that opens with `❓`, the indent set aside. `is_round` and `answer_of` both use it. `answer_of` walks back from the newest output and returns the first one that holds a Case heading, that `is_round` finds a round, or that the predicate finds a Fact answer, else `last_assistant_message`. `subagent` checks, stores and writes nothing for an answer with no Case. The module docstring on the answer says so, and its sentence that an answer with no Case heading, where no earlier output holds one either, is not checked becomes: an answer that is a round or a Fact answer is not checked or stored as a Case, and an earlier Case is not read again.
- [x] `tests/test_casecheck.py`, each test named `subagent`: a Case followed by a round in form whose titles its `recommend` lacks exits 0 and leaves the stored entry, its time and the case file unchanged; a Case followed by a Fact answer does the same; the existing tests of a Case by hand-back followed by a summary text still pass.
- [x] `uv run pytest tests/test_casecheck.py -k subagent`
- [ ] read `estimate-case-check-sends-back-a-faulty-case`
```

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

```then
update:
- slug: estimate-case-check-sends-back-a-faulty-round
  set:
    status: pending
  change: the Criterion replaced whole — a round is known by is_round as the code holds it, and gets no check of a Case in the same run, so its exit 2 carries the findings of its form alone (case 607.2)
```

```tasks
- [x] update `estimate-case-check-sends-back-a-faulty-round`
- [x] `guppi/casecheck.py`: the docstring paragraph on the form of a round says that a round gets no check of a Case, and its exit 2 carries the findings of its form alone, in place of the sentence that the findings join those of the check of a Case in one exit 2.
- [x] `tests/test_casecheck.py`: a Case followed by a round out of form exits 2 with the findings of the form alone, none naming the earlier Case; the test is named `round_form`.
- [x] `uv run pytest tests/test_casecheck.py -k round_form`
- [ ] read `estimate-case-check-sends-back-a-faulty-round`
```

## Case 609 — The defer Estimate reads only a deferred decision

> **context:**
> `estimate-orchestration-defers-in-one-reply` checks the reply in which the person puts off an item in Plan Mode. Its Criterion has one trigger: the person asks to defer an item. Its result is always a short-form Case with a `LEDGER` line, and the Frontier line closes `[-] … · defer case N`. `orchestration.md` handles an item of the sprint differently: it is put off with no Case and no ledger line, and its line closes `[-] … · sprint · defer`. An item of the backlog left as it stands closes `[-] … · backlog · kept`, also with no Case. In session 2300 the only defer was a sprint item. The trigger fit it, but the result could not, so the reading was not taken. The Estimate is still `pending` (Work line W14 of this session). Its `method` names "the first defer the person asks for", so a reader could take a sprint defer as its moment and mark it `failed`.
>
> This Case narrows the trigger to a decision whose source is neither the sprint nor the backlog. It replaces the Criterion whole. The old `when` line is not carried, on purpose: the new `when` replaces it. The check of this answer noted that the old line is missing, and that is the reason. Every `then` line is carried word for word, and one `－` line is added for the sprint and backlog closers. In the same `update` the Case sets the `purpose` and `method` anew, since both state the broad promise. The Estimate is already `pending`, so its status does not change.
>
> A sprint defer is already checked by other Estimates, each within its own trigger:
> - `estimate-orchestration-shows-the-frontier-after-a-closed-line` names an item closed `[-] … · sprint · defer` in its trigger. Its trigger is a reply that carries no ratification and no defer, so it checks only a reply that closes such lines alone.
> - `estimate-orchestration-acknowledging-reply` checks the put-off lines in the Frontier of a reply that acknowledges a ratification.
> - `estimate-hi-writes-frontier` checks the closer.
> - `estimate-prespec-binds-a-sprint-line` checks that such a line needs nothing more.
>
> None of them changes. Pre-spec found that the first wording of the new `－` line said the closed-line Estimate checks every reply that puts off a sprint item. That was wider than its trigger, so the line now names only the reply that closes such lines alone.
>
> Not done: in a reply that also carries a short-form defer, as the reply of session 1237 in this Estimate's Result did, no Estimate judges the form of the sprint line in the Frontier. This Case checks only the defer lines of that reply. The gap stays a known one, with no decision of its own now. The `－` line of the closed-line Estimate on "the reply that carries a defer" means a short-form defer, so it agrees with the new trigger.
>
> No rule text becomes false. The Case changes no behaviour: `orchestration.md` already sets both the sprint closer and the short form. The Case creates no page, so the vault query was not run.
>
> Frame checks:
> - A Grep of `estimate-orchestration-defers-in-one-reply` over the repository outside `vault/raw/` and `vault/archive/` printed 56 files. Leaving out `decisions/` (not opened), `brief.md` and `log.md`, the live hits are the Estimate itself and `rule-orchestration.md`, in its `estimates` field and a History line. There are no hits in code. Neither text changes.
> - A Grep of `sprint · defer|estimate-orchestration-defers-in-one-reply` over the same paths printed, outside `decisions/`, these files:
>   - `brief.md` and `log.md`, which were not read
>   - `orchestration.md` and `rule-orchestration.md`
>   - `rule-case-protocol.md`, in a History line
>   - `rule-skill-hi.md` and `.claude/skills/hi/SKILL.md`
>   - `estimate-orchestration-acknowledging-reply.md`, `estimate-orchestration-shows-the-frontier-after-a-closed-line.md`, `estimate-hi-writes-frontier.md`, `estimate-hi-takes-a-conserved-spec.md` and `estimate-prespec-binds-a-sprint-line.md`
>   - `tests/test_prespec.py` and `tests/test_backlog.py`
>
>   Each of these sets or checks the sprint closer as `orchestration.md` does, and each stays true.
> - A Grep of `short-form|short Case|defer case N` over `vault/wiki/rules/` and `.claude/` printed 9 files:
>   - `.claude/skills/hi/SKILL.md`
>   - `rule-prespec.md`, `rule-case-protocol.md`, `rule-orchestration.md`, `rule-retro.md`, `rule-language.md`, `rule-skill-hi.md`, `rule-decisions-schema.md` and `rule-spec-write.md`
>
>   These set the form of the defer reply and its closers. The Case changes none of them.

> **problem:**
> The Criterion of `estimate-orchestration-defers-in-one-reply` is triggered by any defer in Plan Mode, but its result fits only a decision put off as a short-form Case. The defer of a sprint item fits the trigger and can never meet the result. So the reading is either skipped, as in session 2300, or taken and wrongly marked `failed`.

> **recommend:**
> - **Which defer should `estimate-orchestration-defers-in-one-reply` read?**
>   - Recommended: (a) narrow the trigger to a deferred decision, replacing the Criterion whole, with a `－` line saying that a sprint or backlog item put off is not this moment, and the method naming the same defer. A sprint defer stays checked by the three Estimates that already check it.
>   - Answer: agreed with the recommendation, (a).

> **given:**
> `estimate-orchestration-defers-in-one-reply` — the promise of the defer reply; its Criterion is replaced whole and its `purpose` and `method` are set anew
> **＋** `vault/wiki/orchestration.md` — the Render that sets the short form and the closers of a Frontier line; unchanged
> **＋** `rule-orchestration` — the rule of the main agent's replies, rendered into `orchestration.md`; unchanged
> **＋** `raw/<date>/<hi HHMM>/frontier.md` — the Frontier whose line the defer closes
> **＋** `rule-spec-write` — the `Stop` hook that writes the short-form Case; unchanged
> **＋** `rule-prespec-onward` — the hook that sends the agent on when no line under `## Cases` is open; unchanged
> **＋** `raw/<date>/<hi HHMM>/handoff.md` — where Retro writes what it would put off; unchanged
> **＋** `estimate-orchestration-shows-the-frontier-after-a-closed-line` — the promise that checks a reply that closes lines with no ratification and no defer; unchanged

> **when:**
> In Plan Mode, the person asks in the chat to put off a decision: an item of `raw/<date>/<hi HHMM>/frontier.md` whose source is neither the sprint nor the backlog, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> In the same reply the agent shows the Case in the short form — `context`, `problem` and a fence tagged `then` with one `defer` item per target, no other section — and carries its `LEDGER` block, one `defer` line per target, with no tool call after it.
> **＋** The agent writes nothing of the Case into the plan file: the `Stop` hook of `rule-spec-write` writes it.
> **＋** The person's words asking for the defer are its ratification: no question asks for it.
> **＋** The reply shows the Frontier of `raw/<date>/<hi HHMM>/frontier.md` after the Case, with the line of the item closed `[-] … · defer case N`.
> **＋** While a line under `## Cases` of `raw/<date>/<hi HHMM>/frontier.md` is open, a question follows the Frontier and ends the reply: which open item is next.
> **＋** When no line under `## Cases` is open, no question follows: the reply ends with the Frontier, and the hook of `rule-prespec-onward` sends the agent on.
> **＋** A wording the person corrects is a new short Case with `{supersedes:case N}` on its line, shown the same way.
> **－** No text follows the question, or the Frontier when no question stands.
> **－** Retro writes no short defer: what it would put off is a line of `## For the next session` of `raw/<date>/<hi HHMM>/handoff.md`.
> **－** An item of the sprint put off, its line of `raw/<date>/<hi HHMM>/frontier.md` closed `[-] … · sprint · defer`, and an item of the backlog left as it stands, closed `[-] … · backlog · kept`, are not this moment: they take no short Case and no ledger line, and a reply that closes only such lines is the moment of `estimate-orchestration-shows-the-frontier-after-a-closed-line`.

```then
update:
- slug: estimate-orchestration-defers-in-one-reply
  set:
    status: pending
    purpose: A decision the person asks to put off in Plan Mode, from a source other than the sprint or the backlog, is shown as a short-form Case and written in the same reply, with no round of ratification
    method: by hand, the first decision the person asks to put off after the render, its line of frontier.md closed [-] … · defer case N, in a reply that leaves no line under the Cases heading of frontier.md open; a sprint item put off or a backlog item kept is not this reading
  change: the Criterion replaced whole — the trigger is a decision put off, not an item of the sprint or the backlog; their closers are not this moment (case 609)
```

```tasks
- [x] update `estimate-orchestration-defers-in-one-reply`
- [ ] read `estimate-orchestration-defers-in-one-reply`
```

## Case 610 — A ratified Case built again in another shape takes a new number

> **context:**
> After each ratification, the `Stop` hook of `rule-spec-write` copies the Case into the plan file. A Case can be ratified whole and then built again with sub-cases, which pre-spec findings often cause. On the second ratification the hook rewrites only the parent's `context`, `problem` and `recommend`. It keeps the parent's old `given`, `when`, `then` and blocks beside the new sub-cases (`write_parent` of `guppi/ratified.py`). The plan then signs the same change twice, and the check after the write refuses it. This happened with Cases 471, 580 and 603. Each time, the way out was a new Case number that supersedes the old one: 474, 581 and 606. `insight-spec-write-parent-body-kept-on-re-ratification` clusters the three lessons, and case 585 put it off. Case 475 put off the matching change on `rule-spec-write`, which was to drop the old body so that the Case keeps its number.
>
> Dropping the body is not enough. The ledger still holds the decision lines of the first ratification. Once their items leave the plan, `check_lines` of `guppi/prespec.py` reports each of them as a line with no item in the plan. A line is retired only by `{supersedes:case N}`, one block per number, since `superseded_in_window` matches the number exactly. So the person chose to make the new number the rule and to guard it. The way to retire old lines without a new Case stays with the put-off `rule-ledger-line-withdrawn-on-re-ratification` (case 594). At pre-spec the person chose to keep that defer, and this Case does not name that page. A dropped sub-case goes by the new number too, and the backlog does not change.
>
> This Case was first ratified whole as Case 608. Pre-spec then found that it needs a second promise, so it is built again with sub-cases. By the rule it sets, it takes a new number. 609 is the highest number in the session's ledger `raw/2026-10-03/0115/ledger.md` and among the keys of the store `curious-petting-pearl.checked.json`, so the new number is 610. Its first decision line carries `{supersedes:case 608}`, and Case 610 closes the Frontier line C4 again.
>
> 610.1 sets the guard. It covers three shapes: a Case ratified whole that comes back with sub-cases; a Case ratified with sub-cases that comes back whole, which keeps its old sub-cases in the plan because `place` replaces only the parent's section; and a Case that comes back without a ratified sub-case. The last one keeps that sub-case and its lines, and no check sees it.
>
> The first build said that `estimate-spec-write-removes-a-superseded-case` already checks that the plan loses the old Case. That holds only for a mark on the top-level number. A parent first ratified with sub-cases has no decision line of its own, and a mark on a sub-case removes that sub-case alone, as that Estimate says, so the old parent would stay in the plan. `lesson-prespec-parent-of-superseded-sub-cases` records this shape. So the finding names a mark for the old top-level number too. `remove_case` then removes it with every sub-case. In `guppi/materialize.py` a mark on a parent with no line of its own marks the parent's Decision record, which exists once its sub-cases have lines (case 544.6). The ledger hook does not judge the marks. With that mark, the Criterion of `estimate-spec-write-removes-a-superseded-case` stands.
>
> 610.2 makes true the claim that a clash of the new number is caught. Two Cases sent back in one batch could be given the same number. So could a new Case the main agent has sent out but that has not answered yet. Each stored Case keeps the `agent_id` of the payload, and an answer under a number that another agent holds is sent back. That answer is stored apart, so the line of `estimate-case-check-sends-back-a-faulty-case` that every Case of an answer is stored stays true. Case 607.1 has just replaced that Criterion, and a second replacement in this session would be refused at pre-spec. Every reader that looks a Case up by its number still finds the first agent's entry, so `estimate-case-check-shows-only-the-checked-case` stands. The notes of `estimate-case-check-notes-a-criterion-line-not-carried` are kept per entry, and an answer that clashes is built again under a new number anyway, so that Criterion stands. A fresh `case-guppi` sent out on a number another one has already answered is sent back too. The rules send every change to the same agent, so that only happens outside them.
>
> The two sub-cases count the new number with one function. 610.2 names that count through the Estimate of 610.1 rather than repeating it, so that the count is promised in one wording.
>
> Both checks run in the existing `SubagentStop` hook `uv run guppi casecheck --subagent`, the only hook on that event in `.claude/settings.json`. Case 607 changes which output that hook takes as the answer. These sub-cases add findings on an answer that holds a Case, and the two do not conflict. The Spec hook does not change. 610.1 retires the two defers with `{supersedes:case 475}` on the line of `rule-spec-write` and `{supersedes:case 585}` on the line of the Insight, and sets the Insight `actioned`. The other Estimates of `rule-case-check` speak of other findings, of the `Stop` comparison or of errors of the run, and stay true. Its Purpose already covers a Case in a form the checks of pre-spec refuse. An update of the Render of `rule-case-protocol` touches no Estimate of the live reading, and the Criterion of `estimate-case-protocol-case-form` says nothing about Case numbers.
>
> Both new Estimates have a `ref`, so the vault query of `ask-guppi` was not run. A Glob for each slug over `vault/wiki/` and `vault/archive/` printed no file. A Grep of `ratified again|built again` over `vault/wiki/rules/*.md`, `.claude/**/*.md` and `vault/wiki/*.md` printed 12 files:
> - `brief.md`
> - `backlog.md`
> - `log.md`
> - `orchestration.md`
> - `.claude/skills/pre-spec/SKILL.md`
> - `.claude/agents/case-guppi.md`
> - `rule-prespec.md`
> - `rule-prespec-onward.md`
> - `rule-orchestration.md`
> - `rule-case-build.md`
> - `rule-spec-box.md`
> - `rule-ledger-line-withdrawn-on-re-ratification.md`
>
> The hits in `brief.md` and `log.md` were not read. The hit in `backlog.md` is the line of the Insight, which leaves the backlog when its defer is retired. `orchestration.md`, the Render of `rule-orchestration`, was read whole. The hits in `rule-prespec.md`, `rule-prespec-onward.md`, `rule-case-build.md`, `rule-spec-box.md` and `.claude/agents/case-guppi.md` were read around the line of each hit. The hit in `.claude/skills/pre-spec/SKILL.md` is the rendered text of `rule-prespec.md`. None of these says which number a Case built again keeps, and each stays true. `case-schema.md` already says that the superseding Case closes again the Frontier line that the superseded Case closed.

> **problem:**
> A Case can be ratified in the session and then built again in another shape under its old number: whole after sub-cases, with sub-cases after whole, or without a ratified sub-case. The Spec hook then keeps the old parts beside the new ones, and the ledger lines of the first ratification stay. Either the plan signs content twice and is refused, or a dropped sub-case stays signed without anyone noticing. Nothing tells the agent to take a new number before the refusal comes, and nothing stops two Cases from being built under one new number.

> **recommend:**
> - **Which way to close the problem**
>   - Recommended: (b) make the new number the rule, with a guard. The check of `case-guppi`'s answer sends back a build that changes the shape of a Case already ratified in the session, the hook stays as it is, the Insight is closed and the put-off change to the hook is retired.
>   - Answer: (b).
> - **Who picks the new number**
>   - Recommended: (a) the check names it: one above the highest Case number in the session's ledger and in the store of checked answers.
>   - Answer: agreed with the recommendation, (a).
> - **Which changes of shape the check sends back**
>   - Recommended: (b) any ratified part missing from a whole answer, and a Case ratified whole that comes back with sub-cases. An answer that holds sub-cases alone is not judged this way.
>   - Answer: agreed with the recommendation, (b).
> - **Whether the form of a Case states the rule too**
>   - Recommended: (a) add one sentence to the splitting part of the form, through `rule-case-protocol`, and keep the check as the guard.
>   - Answer: agreed with the recommendation, (a).
> - **How done is checked**
>   - Recommended: (a) a new Estimate of its own under `rule-case-check`.
>   - Answer: agreed with the recommendation, (a).
> - **How a clash of the new number is caught**
>   - Recommended: (a) the store remembers which agent answered each Case. An answer under a number another agent holds is sent back with a new number and does not replace that entry. This is a sub-case of its own with its own Estimate.
>   - Answer: agreed with (a).
> - **Where the answer that clashes is kept**
>   - Recommended: (c) store it apart, under its number together with its agent's id. Readers by number still find the other agent's entry, and the related Case is not touched.
>   - Answer: (c).
> - **Change**
>   - Asked: at pre-spec, keep the defer of `rule-ledger-line-withdrawn-on-re-ratification`. The context says plainly that a dropped sub-case goes by the new number, while the way without a new Case stays with that rule, and the backlog does not change.
>   - Taken: the context says so. No line names that page, and the defer stands.

### Case 610.1 — The check sends back a ratified Case built again in another shape under its old number

> **given:**
> `guppi/casecheck.py` and `tests/test_casecheck.py` — `check_answer`, `subagent`, the function of the new number, the module docstring, and their tests
> **＋** `estimate-case-check-sends-back-a-ratified-case-in-another-shape` — the new promise of the check
> **＋** `raw/<date>/<hi HHMM>/ledger.md` and `<plan>.checked.json` — the session's decision lines and the store of checked answers, which the check reads
> **＋** `rule-case-protocol` — the rule rendered into `vault/wiki/case-schema.md`; its splitting part gains the rule of the new number
> **＋** `rule-spec-write` and `insight-spec-write-parent-body-kept-on-re-ratification` — the pages whose defers this sub-case retires
> **＋** `estimate-spec-write-removes-a-superseded-case` — the removal from the plan that the marks rely on; unchanged
> **＋** `rule-case-check` — the rule of the check; unchanged
> **＋** `raw/2026-10-03/0115/cases/case-607.md` — Case 607, which sets what the same `SubagentStop` check takes as the answer

> **when:**
> `SubagentStop` fires when `case-guppi` answers with a Case, and `uv run guppi casecheck --subagent` reads the Cases of the answer, the decision lines of the session's `raw/<date>/<hi HHMM>/ledger.md`, and `<plan>.checked.json` beside the plan file.

> **then:**
> For an answer that holds a top-level Case N, the hook reads the decision lines of a kind other than `defer` in the session's ledger that belong to the family of Case N, which is Case N and its sub-cases at any depth.
> **＋** Case N gets a finding when a number of its family that has such a line has no section in the answer, or when a number that has such a line has a sub-case in the answer.
> **＋** The finding names each such number and a new number: one above the highest top-level Case number that the decision lines of the session's ledger and the keys of `<plan>.checked.json` hold.
> **＋** The finding tells `case-guppi` to build the Case under the new number. Its decision lines carry one `{supersedes:case N}` for the number N, and one `{supersedes:case M}` for each number M of the family that has a decision line.
> **＋** The hook exits 2 with the finding on stderr, and `case-guppi` answers again.
> **＋** The judgment and the new number come from one function of `guppi/casecheck.py`.
> **－** An answer that holds sub-cases of Case N without Case N gets no finding of this check.
> **－** A Case whose family has no decision line other than `defer` in the session's ledger gets no finding of this check. Neither does a Case built again with a section for each number of its family that has such a line and no sub-case under any of them.

```then
create:
- slug: estimate-case-check-sends-back-a-ratified-case-in-another-shape
  type: estimate
  ref: rule-case-check
  kind: QA
  purpose: A Case that has decision lines in the session and comes back from case-guppi in another shape under its old number goes back to case-guppi with a new number to build it under
  method: uv run pytest tests/test_casecheck.py -k shape, then by hand the first answer of case-guppi the hook sends back for this reason
  tags:
  - hooks
  - harness
  - workflow
update:
- slug: rule-case-protocol
  replace:
  - old: then every sub-case whole (case 355.2).
    new: 'then every sub-case whole (case 355.2). A Case that has a decision line in the session''s ledger and is built again in another shape — whole after sub-cases, with sub-cases after whole, or without a sub-case that has a decision line — is built under a new number, never its old one, and its decision lines carry one {supersedes:case N} for its old top-level number and one for each of its old numbers that has a decision line: the Spec hook keeps the old parts beside the new ones, a mark on a sub-case removes that sub-case alone, and the old lines stay in the ledger until a mark retires them. The check of the answer of case-guppi sends back a build that keeps the old number, and names the new number (case 610.1).'
  change: 'Splitting: a Case ratified in the session that is built again in another shape takes a new number, its decision lines superseding its old top-level number and each old number with a line (case 610.1)'
- slug: rule-spec-write
  change: 'the put-off change to drop the parent''s old body on re-ratification is not taken: a Case ratified in the session that is built again in another shape takes a new number that supersedes it, and the check of rule-case-check sends back one that keeps its number (case 610.1)'
- slug: insight-spec-write-parent-body-kept-on-re-ratification
  set:
    status: actioned
    addressed_by: decision-case-610.1
  change: 'actioned: a Case ratified in the session that is built again in another shape takes a new number that supersedes it, written in the splitting part of case-schema.md and guarded by the SubagentStop check of rule-case-check; the Spec hook is not changed (case 610.1)'
```

```tasks
- [x] create `estimate-case-check-sends-back-a-ratified-case-in-another-shape`
- [x] update `rule-case-protocol`
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
- [x] update `rule-spec-write`
- [x] update `insight-spec-write-parent-body-kept-on-re-ratification`
- [x] `guppi/casecheck.py`: one function gives the new number, one above the highest top-level number among the decision lines of the ledger and the keys of the store, a key joined with an agent id read by its number. A second function takes the Cases of an answer, the decision lines of the session's ledger and the store. For a top-level Case N of the answer it returns a finding for each number of the family of N that has a decision line other than `defer` and no section in the answer, and for each such number that has a sub-case in the answer. The finding carries the new number, and the marks for N and for each such number. `subagent` passes the store to `check_answer`, and `check_answer` adds the findings to Case N. The module docstring says so.
- [x] `tests/test_casecheck.py`, each test named `shape`: a Case ratified whole that comes back with sub-cases is sent back with the new number and the marks; a Case ratified with sub-cases that comes back whole is sent back with a mark for its parent too; a whole answer without a ratified sub-case is sent back; a sub-case answered alone, a Case built again in the same shape, and a Case with only `defer` lines exit 0.
- [x] `uv run pytest tests/test_casecheck.py -k shape`
- [ ] read `estimate-case-check-sends-back-a-ratified-case-in-another-shape`
```

### Case 610.2 — The check sends back a Case under a number another agent holds, and stores it apart

> **given:**
> `guppi/casecheck.py` and `tests/test_casecheck.py` — `subagent`, the store's entries and keys, the module docstring, and their tests
> **＋** `estimate-case-check-sends-back-a-case-number-held-by-another-agent` — the new promise of the check
> **＋** `<plan>.checked.json` — the store of checked answers, whose entries keep the agent id
> **＋** `agent_id` of the `SubagentStop` payload — the id of the agent that answered
> **＋** `guppi/ratified.py` — the Spec hook and the `Stop` comparison, which read the store by Case number; unchanged
> **＋** `rule-case-check` and `estimate-case-check-sends-back-a-ratified-case-in-another-shape` — the rule of the check, and the sibling promise whose count of the new number this check uses; unchanged here
> **＋** `raw/2026-10-03/0115/cases/case-607.md` — Case 607, which sets what the same `SubagentStop` check takes as the answer and that each Case of an answer is stored

> **when:**
> `SubagentStop` fires when `case-guppi` answers with a Case, and `uv run guppi casecheck --subagent` reads the Cases of the answer, `agent_id` of the payload, and `<plan>.checked.json` beside the plan file.

> **then:**
> The hook stores each Case of an answer in `<plan>.checked.json` with the `agent_id` of the payload beside its text, its findings and the time of the store.
> **＋** A top-level Case N of the answer is sent back when the store holds Case N, or a sub-case of it, under its number from an answer with another `agent_id`.
> **＋** Its message gives `case-guppi` a free number, counted as `estimate-case-check-sends-back-a-ratified-case-in-another-shape` counts it, to build the Case under, and the exit code is 2.
> **＋** Each Case of that answer is stored apart, under its number joined with its `agent_id`, and the entry of the other agent under the number alone stays as it was.
> **＋** The Spec hook, the `Stop` comparison and the writing of the file of a Case read the entry under the number alone.
> **－** An unchanged answer whose text its entry apart already holds with this finding is stored again and exits 0, so it is not sent back twice.
> **－** An entry with no `agent_id`, stored before the change, gives no finding of this check, and neither does an answer whose `agent_id` is the one of the entry under the number.

```then
create:
- slug: estimate-case-check-sends-back-a-case-number-held-by-another-agent
  type: estimate
  ref: rule-case-check
  kind: QA
  purpose: A Case of case-guppi under a number that the store holds from the answer of another agent goes back to it with a new number, and the other agent's entry is kept
  method: uv run pytest tests/test_casecheck.py -k clash, then by hand the first answer of case-guppi the hook sends back for this reason
  tags:
  - hooks
  - harness
  - workflow
```

```tasks
- [x] create `estimate-case-check-sends-back-a-case-number-held-by-another-agent`
- [x] `guppi/casecheck.py`: `subagent` stores `agent_id` in each entry. Before it stores, it compares the `agent_id` of the entry under the top-level number of each Case of the answer, and of its sub-cases, with the payload's. On another id it adds the finding with the new number from the function of 610.1 and stores the Cases of the answer under their number joined with the `agent_id`, with the loop guard read from that entry. An entry with no `agent_id` is not compared. The module docstring says so.
- [x] `tests/test_casecheck.py`, each test named `clash`: an answer under a number that the store holds from another agent exits 2 with the new number and leaves the other entry as it was; the answer stands under its key apart; the same answer again exits 0; an entry with no agent id and an answer of the same agent give no finding; `ratified.find_showing` and the case file still read the entry under the number alone.
- [x] `uv run pytest tests/test_casecheck.py -k clash`
- [ ] read `estimate-case-check-sends-back-a-case-number-held-by-another-agent`
```
