## Case 497 — A lesson's pointer to its fix must name a decision line of the session

> **context:**
> A lesson line written after the Case that fixed its cause carries `{addressed_by:case N}`. The librarian's run (`materialize`) links the lesson to the decision only when a decision line of Case N stands before the lesson line in the session's ledger. Nothing checks the pointer when the line is written. A Case with sub-cases has no decision line of its own: its lines are N.1, N.2 and so on, and each has its own Decision page. So a pointer to the parent number never resolves. In session 2229, ledger line 52 pointed at `case 487`, whose lines are 487.1 to 487.4. The lesson `lesson-prespec-judged-a-pair-by-its-anchor-alone` went out without its link, and only the next morning's brief showed it. This is the pattern of `insight-ledger-line-written-unchecked`: a line written verbatim and read back only by `materialize`.
> The person chose three things. The ledger hook refuses such a line at once, the way it already refuses a lesson slug without its prefix (case 460.5). The rule text of `rule-case-protocol` says which number to name. The lesson of line 52 stays as it is. Nothing reads the mark once synthesis has run, the lesson joined no Insight, and the handoff of 2229 names the fix. Its `incomplete: [addressed_by]` stays in the yaml of 2229. Case 442 deferred a neighbour on `rule-ledger-write`: a lesson line with no mark at all, although a Case of the session closed its cause. The person chose to leave it deferred. This Case catches a mark that names the wrong Case, not a missing mark.
> The vault's answer: the only `create` is an Estimate with a `ref`, so no vault query ran. The ledgers under `vault/raw` hold exactly one `{addressed_by:...}` mark and no `{addresses:...}` mark. The first is the line of 2229. The frame:
> - The hook and `materialize` judge the mark by one function in `guppi/materialize.py`, by `CLAUDE.md` ("one judgment, one implementation"). The function reads the ledger lines in order, and one test runs both callers on the same lines. The order matters. `materialize` links a lesson only to a decision line that stands before it, so the hook asks the same thing. A decision line later in the same `LEDGER` block does not count.
> - `materialize` keeps its behaviour: `rule-materialize` and the Criterion of `estimate-materialize-carries-addresses` ("no decision line of Case N earlier in the unit") stay true and are not touched.
> - `estimate-ledger-write-lifts` lists each refusal of the hook in its `－` lines. It gains one line, so its Criterion is replaced whole (497.2).
> - `estimate-ledger-write-refuses-a-lesson-without-its-prefix` says that a lesson line with the prefix "is written as before". This Case would make that false for a line with a bad mark. So its Criterion is replaced whole (497.3), and that one sentence is not carried: it becomes "is not refused for its prefix", and the mark is judged apart. The prefix is judged first. A line refused for its prefix is not judged for its mark, so it gets one stderr line, not two.
> - `estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session` speaks only of `estimate[...]` lines and stands.
> - `estimate-case-protocol-ledger-line-form` promises the form of the mark. It gains the sub-case rule, and its Criterion is replaced whole (497.4). `estimate-case-protocol-loaded` is not touched by a change of a Render (case 378.5).
> - The other `Stop` hooks, `guppi ratified`, `guppi casecheck` and `guppi context`, do not read lesson lines.
> - The prefix refusal refuses a line at every `Stop`, since its slug never changes. The mark refusal depends on the ledger. A line refused from an earlier text is judged again at every `Stop` until it stands in the ledger. It is written at the first `Stop` where a decision line of its Case stands before it. The hook speaks only for the line in the reply just finished. A line whose Case never gets a decision line stays unwritten at the end of the session, and Retro sees it.
> - `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` stays true, and the Case does not update it. The hook runs from the working tree at once, and the text of 497.4 lands at the render. But that Criterion asks for the old form only where the reader refuses, in between, what the old text asks for, and the refused line is lost.
>   - Neither holds here. The old text says to name "that Case", and a mark with no decision line of its Case did not link under the old text either. A line that names a Case without sub-cases passes, as before.
>   - A refused line is not lost. In the reply just finished, the hook exits 2 and the agent writes the line again. From an earlier text, the line is judged again until its decision line stands.
> - Not done: the hook does not judge the `{addresses:<lesson slug>}` mark of a decision line, it does not catch a missing mark (case 442, still deferred), and the lesson of line 52 is not repaired.
> - The new Estimate and the three set `pending` are read in a later session (case 428.1).
>
> This Case is built again after pre-spec found these faults: the hook ignored the order of lines, a later `Stop` was said to skip a line it in fact writes, a line with both faults got two stderr lines, the Estimate of old forms was not named, and defer 442 was not named. The answer check noted that some `then` lines of 497.2, 497.3 and 497.4 share words with 497.1 and with each other. This is expected. All four speak of the same hook and the same mark. 497.1 is modelled on the prefix refusal that 497.3 keeps. 497.2 and 497.4 keep the other lines of their old Criteria word for word.

> **problem:**
> A lesson line can point to a Case that has no decision line before it in the session, such as the parent of sub-cases. The mark then never links, and nobody sees it until the librarian's run of the next day.

> **recommend:**
> Four sub-cases. 497.1 makes the ledger hook refuse a lesson line whose `{addressed_by:case N}` has no decision line of Case N before it, with a message that lists the sub-case lines it found. The hook and `materialize` share one ordered judgment. 497.2 and 497.3 bring the two Estimates of the hook up to date with the new refusal. 497.4 writes the rule into `case-schema.md`: for a Case with sub-cases, name the sub-case whose decision line closes the cause. The rejected option was to let `materialize` resolve a parent number to its first sub-case. That would guess the link, since the pointer holds one decision page and the fix may be another sub-case.

### Case 497.1 — The ledger hook refuses a lesson mark with no decision line before it

> **given:**
> `rule-ledger-write` — the rule of the ledger hook; its `How it works` gains the refusal
> **＋** `guppi/ledger.py` — the hook: the refusal, its order after the prefix check, and its stderr line
> **＋** `guppi/materialize.py` — the one ordered judgment of a mark, which the hook imports and `materialize` uses
> **＋** `tests/test_ledger.py` — the cases of the refusal, and the test that runs both callers on the same lines
> **＋** `estimate-ledger-write-refuses-a-lesson-without-its-prefix` — the prefix refusal, judged first
> **＋** `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` — the rule of old forms for a reader that refuses
> **＋** `estimate-ledger-write-refuses-a-mark-with-no-decision-line` — the new promise

> **when:**
> The `Stop` hook `uv run guppi ledger` finds a fresh `lesson[<slug>]` line in a `LEDGER` block of the session, and the line carries `{addressed_by:case N}`.

> **then:**
> When no decision line of Case N stands before the lesson line — in the session's ledger, or earlier among the lines of the same `Stop` — the line is not written.
> **＋** The other lines of the `Stop` are written as before.
> **＋** When the refused line stands in the reply just finished, the hook exits 2 with one stderr line per refused line: "ledger: lesson[<slug>] not written — {addressed_by:case <N>} names no decision line before it in this session; its sub-cases have case <N.1>, case <N.2>: write the line again after the decision line of the Case that closed the cause, naming that Case." The part on the sub-cases stands only when a decision line of a sub-case of N stands in the session.
> **＋** A refused line from an earlier text of the transcript is judged again at every `Stop` until it stands in the ledger. It is written at the first `Stop` where a decision line of Case N stands in the ledger before it. The hook says nothing about it.
> **＋** The hook and `guppi materialize` judge the mark by one function of `guppi/materialize.py`, over the ledger lines in their order, and give the same answer for the same lines.
> **－** A line that `estimate-ledger-write-refuses-a-lesson-without-its-prefix` refuses is not judged for its mark, and gets that refusal's stderr line alone.
> **－** A lesson line whose mark has a decision line of Case N before it is written as before, and so is a lesson line with no mark. A line already in the ledger of any session is not judged again.
> **－** Without a `hi`, and with `stop_hook_active`, the hook acts as before and judges no line.

> **tasks:**
> - [ ] update `rule-ledger-write`
>   - old: `skips an older one without a word, and writes the other lines as before.`
>   - new:
>     ````
>     skips an older one without a word, and writes the other lines as before. A mark names a decision line before it (case 497.1): a `lesson[...]` line whose `{addressed_by:case N}` has no decision line of Case N before it — in the session's ledger, or earlier among the lines of the same `Stop` — is not written, since `materialize` links a lesson only to a decision line of that Case earlier in the unit, and a Case with sub-cases has no line of its own (session 2229, ledger line 52). One function of `guppi/materialize.py` reads the ledger lines in order and gives each lesson line whose mark has no such decision line; the hook and `materialize` both call it. A line refused for its prefix is not judged for its mark. The hook exits 2 with one stderr line per refused line only when the line stands in the reply just finished, and that line names the decision lines of the sub-cases of N that stand in the session, when there are any. A refused line from an earlier text is judged again at every `Stop`, without a word, until a decision line of its Case stands before it, and is written then.
>     ````
>   - change: `the ledger hook refuses a lesson line whose {addressed_by:case N} has no decision line of Case N before it (case 497.1)`
> - [ ] create `estimate-ledger-write-refuses-a-mark-with-no-decision-line`
>   - type: `estimate`
>   - ref: `rule-ledger-write`
>   - kind: `QA`
>   - purpose: `Whether the ledger hook refuses a lesson line whose addressed_by mark has no decision line of its Case before it in the session, judges it again until that line stands, and says why only for the reply just finished`
>   - method: `uv run pytest tests/test_ledger.py — piped payloads and a session ledger in a temp vault`
>   - tags: `[session, hooks, harness, ledger]`
> - [ ] `guppi/materialize.py` — one function over ledger lines in order that gives each lesson line whose `{addressed_by:case N}` has no decision line of Case N before it. `lift_line` judges the lesson mark by it. The docstring names the hook as its second caller
> - [ ] `guppi/ledger.py` — `refused_marks` beside `refused_lessons`, which calls that function on the session's ledger followed by the fresh lines and skips a line `refused_lessons` already refused. `run` leaves the lines out and prints the stderr line for the finished reply. The module docstring names the refusal and the order of the two checks
> - [ ] `tests/test_ledger.py` — `-k mark`: a mark to a parent with sub-case lines is refused aloud, with the sub-case ids. A mark to a Case with no line is refused aloud, with no sub-case part. A lesson above its decision line in the same block is refused. A refused line in an earlier text is not written while its Case has no line, and is written without a word at the `Stop` after the decision line lands. A mark with its decision line before it, in the ledger or in the same block, is written. A lesson with no mark is written. A line with no prefix and a bad mark gets the prefix line alone. A line already in a ledger is not judged. One test runs the hook and `materialize` on the same ledger lines and asserts that the lines they refuse and leave `incomplete: [addressed_by]` are the same
> - [ ] read `estimate-ledger-write-refuses-a-mark-with-no-decision-line`

> **ratification:**
> ```
> - decision[case 497.1][update][rule-ledger-write]{ref:rule-ledger-write}
> - decision[case 497.1][create][estimate-ledger-write-refuses-a-mark-with-no-decision-line]{ref:rule-ledger-write}{tags:session,hooks,harness,ledger}
> ```

### Case 497.2 — The promise of the ledger hook names the new refusal

> **given:**
> `estimate-ledger-write-lifts` — the promise of the hook; its Criterion replaced whole
> **＋** `guppi/ledger.py` — the hook it reads
> **＋** `guppi/gate.py` — the gate it names
> **＋** `raw/<hi date>/<hi HHMM>/ledger.md` — the session's ledger the hook writes
> **＋** `estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session` — a refusal it names
> **＋** `estimate-ledger-write-refuses-a-lesson-without-its-prefix` — a refusal it names
> **＋** `estimate-ledger-write-refuses-a-mark-with-no-decision-line` — the refusal it gains

> **when:**
> The `Stop` hook `uv run guppi ledger` fires at the end of a turn of the main agent, with `transcript_path` and `last_assistant_message` in its payload; or `guppi gate` refuses a `Skill` call for an item of the Spec without a ledger line.

> **then:**
> In a session with a `hi` recorded, every line `- decision[`, `- estimate[`, `- lesson[` inside a `LEDGER` block of any text of the main agent in the transcript, the reply just finished included, lands in `raw/<hi date>/<hi HHMM>/ledger.md` with the time of writing, once — a body already in the ledger of any session is not written again.
> **＋** A block in a text followed by a tool call in the same turn reaches the ledger at the next `Stop` of the session, with the time of that `Stop`; the reply that ends in the text lands it now.
> **＋** The gate's advice to the agent reads "The text before a tool call waits for the next Stop: end this reply in text with the LEDGER block, then call /<skill> in the next reply."
> **－** An `estimate[...]` line the hook refuses by `estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session` does not land.
> **－** A `lesson[...]` line the hook refuses by `estimate-ledger-write-refuses-a-lesson-without-its-prefix` does not land.
> **－** A `lesson[...]` line the hook refuses by `estimate-ledger-write-refuses-a-mark-with-no-decision-line` does not land while that refusal holds.
> **－** Without a `hi`: exit 2 with the reason, the ledger untouched; with `stop_hook_active`: exit 0, nothing written.
> **－** The last turn of a session that ends in a tool call has no `Stop` after it; its lines are a finding of Retro, not of the hook.

> **tasks:**
> - [ ] update `estimate-ledger-write-lifts`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a lesson line refused for its mark does not land while the refusal holds (case 497.2)`
> - [ ] read `estimate-ledger-write-lifts` — `uv run pytest tests/test_ledger.py tests/test_gate.py`, then by hand on the ledger of a later session

> **ratification:**
> ```
> - decision[case 497.2][update][estimate-ledger-write-lifts]{ref:estimate-ledger-write-lifts}
> ```

### Case 497.3 — The prefix check no longer promises that every prefixed lesson is written

> **given:**
> `estimate-ledger-write-refuses-a-lesson-without-its-prefix` — the promise of the prefix check; its Criterion replaced whole
> **＋** `guppi/ledger.py` — the hook it reads
> **＋** `guppi/materialize.py` — `category_of`, the table of prefixes
> **＋** `estimate-ledger-write-refuses-a-mark-with-no-decision-line` — the check that judges the mark of a prefixed line

> **when:**
> The `Stop` hook `uv run guppi ledger` finds a fresh `lesson[<slug>]` line in a `LEDGER` block of the session. `category_of` of `guppi/materialize.py` does not put its slug under the lessons folder: the slug does not start with the lesson prefix.

> **then:**
> The line is not written.
> **＋** The other lines of the `Stop` are written as before.
> **＋** When the refused line stands in the reply just finished, the hook exits 2 with one stderr line per refused line: "ledger: lesson[<slug>] not written — a lesson slug starts with lesson-, then the area, then the cause: write the line again with the prefix."
> **＋** At every later `Stop`, a refused line from an earlier text of the transcript is skipped without a word.
> **－** A lesson line whose slug starts with the lesson prefix is not refused for its prefix; its mark is judged by `estimate-ledger-write-refuses-a-mark-with-no-decision-line`. A line already in the ledger of any session is not judged again.
> **－** `estimate[...]` and `decision[...]` lines are not judged by their prefix.
> **－** Without a `hi`, and with `stop_hook_active`, the hook acts as before and judges no line.

> **tasks:**
> - [ ] update `estimate-ledger-write-refuses-a-lesson-without-its-prefix`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a prefixed lesson line is not refused for its prefix, its mark judged apart (case 497.3)`
> - [ ] read `estimate-ledger-write-refuses-a-lesson-without-its-prefix` — `uv run pytest tests/test_ledger.py`

> **ratification:**
> ```
> - decision[case 497.3][update][estimate-ledger-write-refuses-a-lesson-without-its-prefix]{ref:estimate-ledger-write-refuses-a-lesson-without-its-prefix}
> ```

### Case 497.4 — The schema says which Case a lesson's mark names

> **given:**
> `rule-case-protocol` — the ledger paragraph of its Render
> **＋** `vault/wiki/case-schema.md` — the file rendered from it, which `/hi` loads
> **＋** `estimate-case-protocol-ledger-line-form` — the promise on the form of the marks; its Criterion replaced whole

> **when:**
> The agent writes the ledger lines of a session: the decision lines in the reply that acknowledges a ratification, a lesson line the moment the lesson exists.

> **then:**
> A decision line is `- decision[case N][kind][slug]` with `{ref:...}` when the target has a ref, `{tags:...}` on a `create`, and `{supersedes:case N}` when it applies.
> **＋** A line that supersedes more than one Case carries one `{supersedes:case N}` block per Case, side by side, never a list inside one block.
> **＋** A Case that takes up a deferred decision carries, on one of its decision lines, one `{supersedes:case N}` block for each Case in the page's `deferred_by`.
> **＋** When a Case of this session closes the root cause of a lesson of this session, the line written second carries the mark: `{addresses:<lesson slug>}` on the decision line when the lesson line stands first, `{addressed_by:case N}` on the lesson line when the decision lines stand first; one mark per lesson.
> **＋** For a Case with sub-cases, the `N` of `{addressed_by:case N}` is the sub-case whose decision line closes the cause, never the parent, which has no decision line.
> **＋** The mark stands in the preview of the ledger lines the person ratifies, or in the `LEDGER` block of the lesson line.
> **－** A lesson whose fix is ratified in another session gets no mark.

> **tasks:**
> - [ ] update `rule-case-protocol`
>   - old: `` carries `{addressed_by:case N}` instead, naming that Case — one of the two marks per pair ``
>   - new: `` carries `{addressed_by:case N}` instead, naming that Case — for a Case with sub-cases the sub-case whose decision line closes the cause, since the parent has no decision line and the ledger hook refuses a mark with no decision line of its Case before it (case 497.4) — one of the two marks per pair ``
>   - change: `a lesson's addressed_by mark names the sub-case whose decision line closes the cause (case 497.4)`
> - [ ] update `estimate-case-protocol-ledger-line-form`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — for a Case with sub-cases the mark names the sub-case (case 497.4)`
> - [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
> - [ ] read `estimate-case-protocol-ledger-line-form` — by hand, the reading its `method` names, in a later session

> **ratification:**
> ```
> - decision[case 497.4][update][rule-case-protocol]{ref:rule-case-protocol}
> - decision[case 497.4][update][estimate-case-protocol-ledger-line-form]{ref:estimate-case-protocol-ledger-line-form}
> ```
