## Case 915 — The Case marks the lesson it fixes, and the ledger hook stops asking

> **context:**
> Today the `Stop` hook `uv run --project .guppi guppi ledger` writes the decision lines of a reply. Then, for each lesson of the session that no mark ties to a Case, it exits 2 with one stderr line asking whether a Case of the session fixed the lesson's cause: `unaddressed` and `reminder_message` of `.guppi/guppi/ledger.py`, called in `run` after `append`, judged by `unlinked_lessons` of `.guppi/guppi/materialize.py`. `untold` of the same module stays silent only while the line already stands in a refusal of the hook since the person's last message. So the question comes back at every ratification. In session 2341 the lesson `lesson-librarian-writes-a-total-no-count-printed` drew it after Case 913 and again after Case 914, and each time the answer was no. Each time it cost one more reply in the chat. The person found this noisy and pointed out two things. A later Case may still fix a lesson. Only an `error` lesson needs this judgment, since a `knowledge` lesson records a fact and has no cause for a Case to fix. The person asked for a quiet question, or an answer inside the reply that holds the Frontier.
>
> A `Stop` hook cannot ask quietly. Claude Code's hook documentation (https://code.claude.com/docs/en/hooks, the first 100 000 characters read) says that exit 2 on `Stop` "continues the conversation", and that `additionalContext` on `Stop` is "feedback that continues the conversation". The quiet way it gives, `additionalContext` on `UserPromptSubmit`, "doesn't appear as a chat message in the interface". The person chose instead that `case-guppi` weighs each `error` lesson of the session that has no mark while it builds a Case. Where the Case fixes the cause, `case-guppi` puts `{addresses:<slug>}` on a decision line of its `ratification`. The person sees the mark and ratifies it with the Case, and the main agent copies it into the reply that acknowledges the ratification, above the Frontier. The rule that governs the choice is the one rule of `ratification.md`: nothing changes without a ratified decision. A mark changes which Case the lesson entry names in `addressed_by`, so the person signs it in the Case. The person also chose that the hold of a lesson written after a Case (case 682.1) leaves out a `knowledge` lesson. That is a second promise with its own Estimate, so the Case splits: 915.1 removes the reminder, 915.2 gives `case-guppi` the judgment, and 915.3 narrows the hold.
>
> A line with the mark lands today. `off_store` of `.guppi/guppi/ledger.py` removes `{addresses:...}` by `ADDRESSES_MARK` from both the fresh line and the stored lines, which it reads by `fence_ledger_lines` of `.guppi/guppi/casecheck.py`, before it compares them. So no reader needs an old form. The kind of a lesson is read by `parse_line` of `.guppi/guppi/materialize.py`, which gives a lesson record its `kind`, `error` or `knowledge`. A Grep of `.guppi/guppi/` for `"error"|"knowledge"|== .error|lesson\[error` printed `materialize.py` and `sprint_close.py`. The second judges the `kind` of a lesson page, not of a ledger line. So the hold reads `record["kind"]` of the same parse and adds no second copy. A Grep of `.guppi/` for `unlinked_lessons|reminder|addresses`, `test_ledger.py` left out, printed `test_onward.py`, `casecheck.py`, `test_materialize.py`, `ledger.py`, `onward.py` and `materialize.py`. A Grep of `.guppi/` for `unlinked_lessons` printed only `ledger.py`, in `unaddressed` and its docstring, `materialize.py`, its definition, and two tests of `test_ledger.py`, so 915.1 removes it with them.
>
> A Grep of `vault/wiki/` for `reminder|has no mark|lesson with no mark`, `log.md` and `brief.md` left out, printed `orchestration.md`, `rules/rule-orchestration.md`, `rules/rule-prespec-onward.md`, `estimates/estimate-ledger-write-asks-for-the-mark-of-a-lesson.md`, `estimates/estimate-ledger-write-reminds-of-the-mark-on-a-decision-line.md` and `estimates/estimate-prespec-onward-sends-the-agent-on.md`. The same Grep of `.claude/` printed nothing. The hits in `orchestration.md` and `rule-orchestration.md` under the example Case 7 speak of a booking reminder and stand. The sentence of `rule-orchestration` on the reply that answers the reminder, and the three places in the Purpose of `rule-prespec-onward`, change in 915.1. The Criterion of `estimate-prespec-onward-sends-the-agent-on` stands. `guppi onward --plan` judges a refusal of the ledger hook by its command through `sent_back_last`, never by its text. The Criterion names the reminder only as one kind of such a refusal, and replacing it whole would sign the same promise again. The tests of `.guppi/tests/test_onward.py` that feed a hand-made reminder text stand for the same reason. The sentence of `ratification.md` (`rule-ratification`) on `{addresses:<lesson slug>}` sets only the form of the mark and stays true. The slug `estimate-ledger-write-reminds-of-the-mark-on-a-decision-line` stays as it is: 915.1 replaces its Criterion and `purpose`, which now say that the hook reminds of nothing, and a rename would change its links in the middle of the readings of this session. The sentence of `rule-orchestration` around its pair, read whole under `## Writing the ledger lines`, keeps the hold of a decision line off the stored Case and the readings, and drops only the reply that answers the reminder. A Grep of `case-913.md` and `case-914.md` under `cases/` for `rule-ledger-write|rule-orchestration|rule-case-build|rule-prespec-onward|ledger\.py|onward\.py` printed nothing, so no other Case of the session writes into the pages of this Case.
>
> A Grep of `.guppi/tests/` for `case-guppi\.md|orchestration\.md|rule-ledger-write|rule-case-build|rule-orchestration` printed `test_gate.py`, `test_guppi_package.py`, `test_ledger.py`, `test_onward.py` and `test_orchestration.py`. Only `test_orchestration.py` reads a live file, `vault/wiki/orchestration.md`. It reads only the blocks tagged `showing` and `defer`, which this Case does not touch. The code changes in Work Mode of this session. `.claude/agents/case-guppi.md` and `orchestration.md` change at the librarian's render after it, so for the rest of this session nothing asks about a lesson. A lesson written after `case-guppi` built a Case, and before that Case is ratified, is not weighed against it. The person accepted that cost in the round.

> **problem:**
> The ledger hook asks the same question about a lesson with no mark after every ratification, and each time it costs one more reply in the chat. It asks about `knowledge` lessons too, though no Case fixes the cause of a fact.

> **recommend:**
> - **How often should the hook ask about a lesson with no mark?**
>   - Recommended: (a) once a lesson, at the first ratification after it, judged from the session's ledger.
>   - Answer: none of the options; a later Case may still fix the lesson, only an error lesson needs the judgment and a knowledge lesson none, and the question should be quiet or answered inside the reply that holds the Frontier; replaced by **Where should the question about an error lesson with no mark reach the agent?**
> - **Where should the question about an error lesson with no mark reach the agent?**
>   - Recommended: (b) the Case answers it when it is built: `case-guppi` weighs each open error lesson and writes the mark on its own ledger lines, which the person ratifies.
>   - Answer: agreed, (b).
> - **Which lessons does the question cover?**
>   - Recommended: (a) error lessons only, for the new question and for the hold of a lesson written after a Case.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: the person agreed with the fixes that `/pre-spec` proposed: the new text of `rule-case-build` names only a lesson that stands before the decision lines of a reply, and reads the ledger by a Grep for `lesson\[error\]` and a Grep for `\{addresses:`; the pair of `rule-prespec-onward` keeps the pointer to case 688.7; the `then` of 915.1 names the new Render of `rule-orchestration` in the Spec.
>   - Taken: each fix as proposed; the `method` of `estimate-ledger-write-reminds-of-the-mark-on-a-decision-line` adds the reading of that Render at Retro.

### Case 915.1 — The ledger hook writes a decision line after a lesson without a reminder

> **given:**
> `rule-ledger-write`: the page of the ledger hook; its Purpose names the reminder.
> **＋** `estimate-ledger-write-reminds-of-the-mark-on-a-decision-line`: its Criterion is replaced whole; its slug stays.
> **＋** `.guppi/guppi/ledger.py`: the hook; `unaddressed`, `reminder_message`, their call in `run` and the docstring.
> **＋** `.guppi/guppi/materialize.py`: `unlinked_lessons`, which only the reminder calls.
> **＋** `.guppi/tests/test_ledger.py`: the tests of the reminder.
> **＋** `rule-orchestration`: renders `vault/wiki/orchestration.md`, which names the reply that answers the reminder.
> **＋** `rule-prespec-onward`: its Purpose names the reminder among the refusals after which it sends the agent on.
> **＋** `.guppi/guppi/onward.py`: its docstring names the reminder.

> **when:**
> The `Stop` hook `uv run --project .guppi guppi ledger` of `.guppi/guppi/ledger.py` writes fresh decision lines of the reply just finished, and a `lesson[<slug>]` line of the session stands before them, in the session's ledger or among the lines of the same `Stop`, with no `{addressed_by:...}` and no decision line after it that carries `{addresses:<slug>}`.

> **then:**
> The hook writes every line of the `Stop` and prints no line about the lesson.
> **＋** When no other refusal of the hook stands at that `Stop`, it exits 0.
> **＋** A decision line that carries `{addresses:<slug>}` lands in the session's ledger as any decision line of its Case does.
> **＋** `.guppi/guppi/ledger.py` holds no question about a lesson before a Case, and the new Render of `rule-orchestration` in the Spec names no reply that answers one.
> **－** The hook holds back no decision line because it lacks `{addresses:...}`.

> **tasks:**
> - [ ] update `rule-ledger-write`
>   - old: `` It writes the decision lines of a reply that follow a lesson of the session no mark links to a Case, and then reminds the agent once a stretch: the Case that fixed the cause writes one of its decision lines again with `{addresses:<lesson slug>}` (case 685.1). ``
>   - new: `` It writes the decision lines of a reply that follow a lesson of the session no mark links to a Case, and asks nothing about the lesson: the mark `{addresses:<lesson slug>}` comes on a ledger line of the Case that fixed its cause, as `case-guppi` writes it and the person ratifies it, as `rule-case-build` sets it (as set in case 915.1). ``
>   - change: `the hook no longer reminds the agent of a lesson with no mark; the Case carries the mark`
> - [ ] update `estimate-ledger-write-reminds-of-the-mark-on-a-decision-line`
>   - set:
>     ```
>     status: pending
>     purpose: Whether the ledger hook writes the decision lines of a reply that follow an unmarked lesson of the session with no reminder of the addresses mark, and lands a decision line that carries it
>     method: uv run --project .guppi pytest .guppi/tests/test_ledger.py — piped payloads and a session ledger in a temp vault; by hand, at the Retro of the session that changes it, the new Render of rule-orchestration in the Spec read against the Criterion
>     ```
>   - change: `the Criterion replaced whole — no reminder of a lesson with no mark`
> - [ ] update `rule-orchestration`
>   - old: `` in the reply that answers the ledger hook's reminder of a lesson with no mark, which, when a Case of the reply fixed the cause, holds only a `LEDGER` block with one decision line of that Case or sub-case written again with `{addresses:<lesson slug>}`, and otherwise no block (case 685.1); and in the reply ``
>   - new: `` with each mark `{addresses:<lesson slug>}` that the summary of `case-guppi` holds on a line, and in the reply ``
>   - change: `no reply answers a reminder of a lesson with no mark; the reply that acknowledges a ratification carries the mark the summary holds`
> - [ ] update `rule-prespec-onward`
>   - old: `— a line it refused or held, or its reminder of a lesson with no mark (cases 685.1, 688.7):`
>   - new: `— a line it refused or held (case 688.7):`
>   - old: `such as the answer that no Case fixed the cause of a lesson,`
>   - new: `such as the answer to a held decision line whose stored line is wrong,`
>   - old: `The ledger hook tells each refused or held line and each reminder once a stretch, so the hook cannot loop.`
>   - new: `The ledger hook tells each refused or held line once a stretch, so the hook cannot loop.`
>   - change: `the reminder of a lesson with no mark is gone from the refusals it follows`
> - [ ] `uv run --project .guppi guppi render`: `vault/wiki/orchestration.md`
> - [ ] `.guppi/guppi/ledger.py`: remove `unaddressed`, `reminder_message` and the `reminders` of `run`; remove the paragraph of the module docstring on the reminder (case 685.1) and its mention in the paragraph on the hold.
> - [ ] `.guppi/guppi/materialize.py`: remove `unlinked_lessons`.
> - [ ] `.guppi/guppi/onward.py`: the docstring names a line the ledger hook refused or held, and no reminder.
> - [ ] `.guppi/tests/test_ledger.py`: replace the tests of the reminder and `test_unlinked_lessons_reads_the_marks_of_both_kinds` with tests that a lesson before fresh decision lines brings no stderr line and exit 0, that a decision line with `{addresses:<slug>}` lands, and that the hook holds back no decision line for the mark; `test_a_lesson_before_every_decision_line_is_not_asked` expects `(0, "")`.
> - [ ] `uv run --project .guppi pytest .guppi/tests/test_ledger.py .guppi/tests/test_onward.py`
> - [ ] read `estimate-ledger-write-reminds-of-the-mark-on-a-decision-line`

> **ratification:**
> ```
> - decision[case 915.1][update][rule-ledger-write]{ref:rule-ledger-write}
> - decision[case 915.1][update][estimate-ledger-write-reminds-of-the-mark-on-a-decision-line]{ref:rule-ledger-write}
> - decision[case 915.1][update][rule-orchestration]{ref:rule-orchestration}
> - decision[case 915.1][update][rule-prespec-onward]{ref:rule-prespec-onward}
> ```

### Case 915.2 — case-guppi marks the error lesson its Case fixes

> **given:**
> `rule-case-build`: renders `.claude/agents/case-guppi.md`, the agent that builds a Case.
> **＋** `estimate-case-build-marks-the-lesson-its-case-fixes`: the new check.
> **＋** `raw/<date>/<hi HHMM>/ledger.md`: the session's ledger, which `case-guppi` reads for the lessons.
> **＋** `vault/wiki/ratification.md`: the form of the mark `{addresses:<lesson slug>}`.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of the Case, whose `ratification` carries the mark.

> **when:**
> `case-guppi`, by `.claude/agents/case-guppi.md`, writes the `ratification` of a Case into its file `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and the session's ledger `raw/<date>/<hi HHMM>/ledger.md` holds a `lesson[error][<slug>]` line that no mark ties to a Case.

> **then:**
> `case-guppi` judges whether the Case, or one of its sub-cases, fixes the root cause of that lesson.
> **＋** Where one does, one decision line of that Case or sub-case carries `{addresses:<slug>}`, in the form of `vault/wiki/ratification.md`, and `context` names the lesson and why the Case closes it.
> **＋** The summary of `case-guppi` holds the line with the mark as the file holds it, so the person ratifies the mark with the Case.
> **－** A `lesson[knowledge]` line of the ledger gets no mark from this judgment.
> **－** A lesson with `{addressed_by:...}` on a line of its slug, or that a decision line of the ledger already marks with `{addresses:<slug>}`, is not judged again.

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `says why it stands (case 784).`
>   - new: `` says why it stands (case 784). Before you write the `ratification` of a Case, read the session's ledger `raw/<date>/<hi HHMM>/ledger.md` by a Grep for `lesson\[error\]` and a Grep for `\{addresses:`, and for each `error` lesson there that no mark ties to a Case — no `{addressed_by:...}` on a line of its slug and no decision line after it with `{addresses:<slug>}` — judge whether your Case, or one of its sub-cases, fixes its root cause; where one does, add `{addresses:<slug>}` to one decision line of that Case or sub-case and say in `context` which lesson it closes and why, and add no mark for a `knowledge` lesson, since the ledger hook asks nothing about a lesson that stands before the decision lines of a reply (as set in case 915.2). ``
>   - change: `case-guppi weighs each error lesson of the session with no mark and writes the addresses mark on the Case that fixes it`
> - [ ] create `estimate-case-build-marks-the-lesson-its-case-fixes`
>   - ref: `rule-case-build`
>   - kind: `QA`
>   - purpose: `Whether case-guppi weighs each error lesson of the session that no mark ties to a Case, and writes the addresses mark on a decision line of the Case or sub-case that fixes its cause`
>   - method: `by hand, at the Retro of the session that changes it, the new Render of rule-case-build in the Spec read against the Criterion, recorded in the estimate line`
>   - tags: `[session, workflow, harness]`
> - [ ] `uv run --project .guppi guppi render`: `.claude/agents/case-guppi.md`
> - [ ] read `estimate-case-build-marks-the-lesson-its-case-fixes`

> **ratification:**
> ```
> - decision[case 915.2][update][rule-case-build]{ref:rule-case-build}
> - decision[case 915.2][create][estimate-case-build-marks-the-lesson-its-case-fixes]{ref:rule-case-build}{tags:session,workflow,harness}
> ```

### Case 915.3 — The ledger hook holds only an error lesson for its mark

> **given:**
> `rule-ledger-write`: the page of the ledger hook; its Purpose names the hold of a lesson written after a Case.
> **＋** `estimate-ledger-write-asks-for-the-mark-of-a-lesson`: its Criterion is replaced whole.
> **＋** `.guppi/guppi/ledger.py`: `unmarked_lessons` and the docstring of the hold.
> **＋** `.guppi/tests/test_ledger.py`: the tests of the hold.
> **＋** `estimate-ledger-write-lifts`: the other refusals that keep a line out.
> **＋** `estimate-ledger-write-refuses-a-lesson-with-an-unlisted-tag`: a line refused for its tag.

> **when:**
> The `Stop` hook `uv run --project .guppi guppi ledger` of `.guppi/guppi/ledger.py` finds a fresh `lesson[<kind>][<slug>]` line in a `LEDGER` block of the session that carries no `{addressed_by:...}`, and a decision line of the session stands before it, in the session's ledger or earlier among the lines of the same `Stop`.

> **then:**
> For a `lesson[error]` line, at the `Stop` of the reply that carries it, the hook holds the line back once, unless it already asked about it since the person's last message.
> **＋** For each held line the hook exits 2 and prints: "ledger: lesson[<slug>] held — did a Case of this session fix its cause? Then add {addressed_by:case <N>}, the Case or sub-case that fixed it, and repeat the line; otherwise repeat it unchanged." The line names no Case, however many decision lines stand before the lesson line.
> **＋** The held line lands as it stands once the hook's question about it stands in a refusal since the person's last message, or when it stands only in an earlier text of the transcript; neither way lands it while another refusal of the hook keeps it out, as `estimate-ledger-write-lifts` sets it.
> **＋** A held line keeps back no other line: the rest of that `Stop` lands in the ledger.
> **＋** A `lesson[knowledge]` line is never held for its mark: it lands at its first `Stop`, unless another refusal of the hook keeps it out.
> **－** An unmarked line of either kind never lands beside a marked one: `{addressed_by:...}` on a `lesson[<slug>]` line in the session's ledger, or in that `Stop`, drops the unmarked line of the slug.
> **－** The hook holds no lesson line that stands before every decision line of the session, no line it refuses for its prefix or cannot parse, no line that the ledger of some session already holds, and no line that `estimate-ledger-write-refuses-a-lesson-with-an-unlisted-tag` keeps out.
> **－** A session with no `hi` gets no question; with `stop_hook_active` set and a transcript the hook cannot read, the line lands as it stands.

> **tasks:**
> - [ ] update `rule-ledger-write`
>   - old: `` It holds once a lesson line with no `{addressed_by:case N}` written after a decision line of the session ``
>   - new: `` It holds once an `error` lesson line with no `{addressed_by:case N}` written after a decision line of the session ``
>   - old: `the line written again with the mark, or unchanged, is written (case 682.1).`
>   - new: `` the line written again with the mark, or unchanged, is written (case 682.1). It never holds a `knowledge` lesson line for its mark, since such a lesson records a fact and no Case fixes its cause (as set in case 915.3). ``
>   - change: `the hold of a lesson written after a Case covers only an error lesson`
> - [ ] update `estimate-ledger-write-asks-for-the-mark-of-a-lesson`
>   - set:
>     ```
>     status: pending
>     purpose: Whether the ledger hook holds once an error lesson line with no addressed_by mark written after a decision line of the session, asks for the mark, writes the line written again unless another refusal of the hook keeps it out, and never holds a knowledge lesson line for its mark
>     ```
>   - change: `the Criterion replaced whole — only an error lesson is held for its mark`
> - [ ] `.guppi/guppi/ledger.py`: `unmarked_lessons` leaves out a `knowledge` lesson line by the `kind` that `parse_line` gives, unless a line of its slug carries `{addressed_by:...}`, so that it is still dropped beside that line; the docstring of the hold (case 682.1) says so.
> - [ ] `.guppi/tests/test_ledger.py`: a test that a `lesson[knowledge]` line after a decision line lands at its first `Stop` with exit 0, and one that a `lesson[knowledge]` line beside a marked line of its slug is dropped.
> - [ ] `uv run --project .guppi pytest .guppi/tests/test_ledger.py`
> - [ ] read `estimate-ledger-write-asks-for-the-mark-of-a-lesson`

> **ratification:**
> ```
> - decision[case 915.3][update][rule-ledger-write]{ref:rule-ledger-write}
> - decision[case 915.3][update][estimate-ledger-write-asks-for-the-mark-of-a-lesson]{ref:rule-ledger-write}
> ```
