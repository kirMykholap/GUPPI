## Case 682 — The ledger hook asks for the mark of a lesson written after a Case

> **context:**
> When a Case of a session closes the cause of a lesson of the same session, one of two marks links them: a lesson line written after the Case carries `{addressed_by:case N}`, and a decision line written after the lesson carries `{addresses:<lesson slug>}` (case 379). The ledger hook writes the record lines of each reply into the session's ledger. It refuses a lesson line whose `{addressed_by:case N}` has no decision line of Case N before it (case 497.1), but it writes a lesson line with no mark at all without a word. In session 1337 the line `lesson-hooks-subagentstop-fires-before-and-after-the-handback` stayed with no mark, although Case 434 had closed its cause, so the librarian did not link it and the lesson stayed `new`. Case 442 deferred the question onto `rule-ledger-write`. No code can judge whether a Case closed a cause, so the hook can only stop a likely miss and ask the agent.
> The person chose three things. The ledger hook holds a fresh lesson line with no `{addressed_by:...}` once, when a decision line of the session stands before it, and asks the agent: a Case that closed the cause gets the mark on the line written again, and no Case gets the line written again unchanged, which the hook then writes. Every such lesson line is held, not only one that names a page a Case changed. The `{addresses:...}` side is not covered: a decision line with no `{addresses:...}` after an unmarked lesson is not judged, and that stays not done.
> The hold uses the told-once rule of the hook: a stderr line already in a refusal of the hook since the person's last message is not printed again, so the line written again unchanged is written at its `Stop`, and a line from an earlier text is written without a word. An unmarked line is never written beside a marked line of the same slug, so the ledger never holds the lesson twice. Case 682.1 updates `rule-ledger-write`, carries `{supersedes:case 442}` and creates `estimate-ledger-write-asks-for-the-mark-of-a-lesson`, checked by pytest. The form of a ledger line does not change, so no old form is kept; during Work Mode the hook runs from the working tree, and a held line is written again, not lost.
> The frame. `estimate-ledger-write-refuses-a-mark-with-no-decision-line` says that a lesson line with no mark is written as before, which the hold makes false, so Case 682.2 replaces its Criterion whole with that sentence changed; its `purpose` and `method` speak only of a marked line and stand. `estimate-ledger-write-lifts` says that a line a refusal of `rule-ledger-write` refuses does not land while that refusal holds, and that each refused line is told once a stretch; the hold is such a refusal, so its Criterion stands. `estimate-ledger-write-refuses-a-lesson-without-its-prefix` says that a lesson line with the prefix has its mark judged by the check of the mark; that stays true, and a line refused for its prefix is not judged for a missing mark, so it stands. The other Estimates of the page speak of readings, unreadable lines, errors and the kind of a user record, and stand. The other `Stop` hooks of `.claude/settings.json` stand: `guppi onward` already sends the agent on only after the reply that writes the refused lines again (case 596.1), and the Render of `rule-retro` lets the reply that ends Retro be followed by a `LEDGER` block that answers a refusal of the ledger hook, which a lesson line written again with its mark or unchanged is.
> The searches. A Grep of `with no mark|nothing catches|missing mark` over `vault/wiki/` printed `estimate-ledger-write-refuses-a-mark-with-no-decision-line.md`, which enters Case 682.2, `estimate-case-check-requires-a-backlog-item-decided-on-its-page.md`, whose missing mark is a `{supersedes:...}` mark and stands, and `lesson-hooks-a-stop-system-message-shows-no-markdown-in-vs-code.md`, which speaks of a hook's message and stands. A Grep of `refusal of the ledger hook|ledger hook refuses` over `vault/wiki/rules/` and `.claude/` printed `.claude/skills/retro/SKILL.md`, `rule-retro.md`, `rule-ledger-write.md`, `rule-orchestration.md`, `rule-ratification.md` and `rule-session.md`: the first two let a reply answer a refusal of the ledger hook, the hits in `rule-ratification` and `rule-orchestration` name other refusals of the hook and a History line, the hits in `rule-ledger-write` are History lines, and the hit in `rule-session` names the refusal without `/hi`; each stays true and stands. A Glob of `vault/**/*mark-of-a-lesson*` printed nothing, so the new slug is free. Case 681 of this session changes `rule-orchestration` and Case 683 changes `rule-page-generation`; neither changes a page this Case changes.

> **problem:**
> A lesson line whose cause a Case of the same session closed can be written with no mark, and nothing catches it, so the librarian never links the lesson to its Case.

> **recommend:**
> - **Where the missing mark is caught**
>   - Recommended: (a) the ledger hook holds the line once and asks; a line written again with the mark, or unchanged, is then written.
>   - Answer: agreed, (a).
> - **Which lesson lines the check stops**
>   - Recommended: (a) every unmarked lesson line written after a decision line of the session.
>   - Answer: agreed, (a).
> - **Whether the `{addresses:...}` side is covered too**
>   - Recommended: (a) leave it out, and name it as not done.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: at `/pre-spec` the person agreed to the fix of a finding: the Criterion of Case 682.2 said a lesson line with no mark that the new check does not hold is written, while Case 682.1 drops an unmarked line beside a marked line of the same slug.
>   - Taken: the Criterion of Case 682.2 now says a lesson line with no mark is written when the new check neither holds nor drops it.

### Case 682.1 — The ledger hook holds an unmarked lesson once and asks

> **given:**
> `rule-ledger-write`: the rule of the ledger hook, whose deferred item this Case takes up.
> **＋** `guppi/ledger.py`: the `Stop` hook `uv run guppi ledger` that judges the fresh lines.
> **＋** `tests/test_ledger.py`: the tests of the hook.
> **＋** `estimate-ledger-write-asks-for-the-mark-of-a-lesson`: the new check of the hold.
> **＋** `estimate-ledger-write-lifts`: the told-once rule the hold uses, which stands.
> **＋** `rule-retro`: the reply that answers a refusal of the ledger hook at the end of Retro, unchanged.
> **＋** `rule-retro-onward`: the hook that sends the agent on after the reply that writes refused lines again, unchanged.

> **when:**
> The `Stop` hook `uv run guppi ledger` of `guppi/ledger.py` finds a fresh `lesson[<slug>]` line in a `LEDGER` block of the session that carries no `{addressed_by:...}`, and a decision line of the session stands before it, in the session's ledger or earlier among the lines of the same `Stop`.

> **then:**
> At the `Stop` of the reply that carries it, the hook holds the line back once, unless it already asked about it since the person's last message.
> **＋** For each held line the hook exits 2 and prints: "ledger: lesson[<slug>] held — did case <N> or case <M> fix its cause? Then add {addressed_by:case <N>}, the Case or sub-case that fixed it, and repeat the line; otherwise repeat it unchanged."
> **＋** The Cases the stderr line names are those whose decision lines stand before the lesson line, in the order first seen.
> **＋** The line lands as it stands once the hook's question about it stands in a refusal since the person's last message, or when it stands only in an earlier text of the transcript.
> **＋** A held line keeps back no other line: the rest of that `Stop` lands in the ledger.
> **－** An unmarked line never lands beside a marked one: `{addressed_by:...}` on a `lesson[<slug>]` line in the session's ledger, or in that `Stop`, drops the unmarked line of the slug.
> **－** The hook asks nothing about a lesson that precedes every decision line of the session, about a line it refuses for its prefix or cannot parse, or about a line that the ledger of some session already holds.
> **－** The hook never asks for `{addresses:...}` on a decision line.
> **－** A session with no `hi` gets no question. The flag `stop_hook_active` changes nothing here, but when it is set and the transcript is unreadable, the hook lets the line land as it stands.

> **tasks:**
> - [ ] update `rule-ledger-write`
>   - old: `` so that the session after the close of a sprint opens the next sprint first (`rule-sprint-close`, case 628.3). ``
>   - new: `` so that the session after the close of a sprint opens the next sprint first (`rule-sprint-close`, case 628.3). It holds once a lesson line with no `{addressed_by:case N}` written after a decision line of the session, and asks the agent whether a Case of the session closed its cause: the line written again with the mark, or unchanged, is written (case 682.1). ``
>   - change: `the hook holds once a lesson line with no addressed_by mark written after a decision line of the session, and asks for the mark (case 682.1)`
> - [ ] create `estimate-ledger-write-asks-for-the-mark-of-a-lesson`
>   - ref: `rule-ledger-write`
>   - kind: `QA`
>   - purpose: `Whether the ledger hook holds once a lesson line with no addressed_by mark written after a decision line of the session, asks for the mark, and then writes the line written again`
>   - method: `uv run pytest tests/test_ledger.py — piped payloads and a session ledger in a temp vault`
>   - tags: `[session, hooks, harness, ledger]`
> - [ ] `guppi/ledger.py`: a function judges each fresh unmarked lesson line after a decision line of the session over the session's ledger followed by the fresh lines; `run` holds it once by the told-once rule, skips it beside a marked line of the same slug, and the docstring says so.
> - [ ] `tests/test_ledger.py`: tests of the hold, of the line written again unchanged, of the line written again with its mark, of a line from an earlier text, of a lesson with no decision line before it and of the flag with an unreadable transcript; the existing tests whose unmarked lesson follows a decision line answer the hold.
> - [ ] read `estimate-ledger-write-asks-for-the-mark-of-a-lesson`

> **ratification:**
> ```
> - decision[case 682.1][update][rule-ledger-write]{ref:rule-ledger-write}{supersedes:case 442}
> - decision[case 682.1][create][estimate-ledger-write-asks-for-the-mark-of-a-lesson]{ref:rule-ledger-write}{tags:session,hooks,harness,ledger}
> ```

### Case 682.2 — The check of the mark leaves an unmarked lesson to the new check

> **given:**
> `estimate-ledger-write-refuses-a-mark-with-no-decision-line`: its Criterion is replaced whole.
> **＋** `guppi/ledger.py`: the `Stop` hook `uv run guppi ledger` that judges the mark.
> **＋** `guppi/materialize.py`: the one judgment of the mark, which the hook and `guppi materialize` share.
> **＋** `estimate-ledger-write-asks-for-the-mark-of-a-lesson`: the check of a lesson line with no mark.
> **＋** `estimate-ledger-write-refuses-a-lesson-without-its-prefix`: the check of the prefix, judged first.
> **＋** `estimate-ledger-write-lifts`: the told-once rule of the hook.

> **when:**
> The `Stop` hook `uv run guppi ledger` finds a fresh `lesson[<slug>]` line in a `LEDGER` block of the session, and the line carries `{addressed_by:case N}`.

> **then:**
> When no decision line of Case N stands before the lesson line — in the session's ledger, or earlier among the lines of the same `Stop` — the line is not written.
> **＋** The other lines of the `Stop` are written as before.
> **＋** When the refused line stands in the reply just finished, the hook exits 2 with one stderr line per refused line: "ledger: lesson[<slug>] not written — {addressed_by:case <N>} names no decision line before it in this session; its sub-cases have case <N.1>, case <N.2>: write the line again after the decision line of the Case that closed the cause, naming that Case." The part on the sub-cases stands only when a decision line of a sub-case of N stands in the session.
> **＋** A refused line from an earlier text of the transcript is judged again at every `Stop` until it stands in the ledger. It is written at the first `Stop` where a decision line of Case N stands in the ledger before it. The hook says nothing about it.
> **＋** The hook and `guppi materialize` judge the mark by one function of `guppi/materialize.py`, over the ledger lines in their order, and give the same answer for the same lines.
> **－** A line that `estimate-ledger-write-refuses-a-lesson-without-its-prefix` refuses is not judged for its mark, and gets that refusal's stderr line alone.
> **－** A lesson line whose mark has a decision line of Case N before it is written as before, and so is a lesson line with no mark that `estimate-ledger-write-asks-for-the-mark-of-a-lesson` neither holds nor drops. A line already in the ledger of any session is not judged again.
> **－** Without a `hi` the hook judges no line. With `stop_hook_active` set it judges the line the same, and its stderr line is told once a stretch, as `estimate-ledger-write-lifts` sets it.

> **tasks:**
> - [ ] update `estimate-ledger-write-refuses-a-mark-with-no-decision-line`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a lesson line with no mark is judged by estimate-ledger-write-asks-for-the-mark-of-a-lesson (case 682.2)`
> - [ ] read `estimate-ledger-write-refuses-a-mark-with-no-decision-line`

> **ratification:**
> ```
> - decision[case 682.2][update][estimate-ledger-write-refuses-a-mark-with-no-decision-line]{ref:rule-ledger-write}
> ```
