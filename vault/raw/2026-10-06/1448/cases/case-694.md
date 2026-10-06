## Case 694 — The ledger hook asks about a lesson's mark without naming Cases

> **context:**
> The `Stop` hook `uv run guppi ledger` asks the agent whether a Case of the session fixed the cause of a lesson that no mark links to a Case. It asks at two moments. First, it holds once a lesson line written after decision lines of the session (case 682.1, `held_message`). Second, it reminds the agent after the write when fresh decision lines follow a lesson that has no mark (case 685.1, `reminder_message`). Both messages list the Cases through one function, `named_cases` of `guppi/ledger.py`. The hold lists every Case whose decision lines stand before the lesson. The reminder lists every Case of the fresh decision lines after it. The hook cannot judge which Case is related to a lesson. The ledger of session 0104 holds two Retro lessons, at lines 47 and 48, after decision lines of nineteen Cases, 685.1 to 690.3; the brief records that the hold named all nineteen, once for each lesson. In this session the ledger holds `lesson-hooks-a-mod-draws-nothing-in-the-mobile-code-tab` at line 1, before the decision lines of Cases 691, 692.1, 692.2 and 693. By `reminder_message`, the reminder after their write names those four Cases, and none of them touches the lesson's subject. The person chose to change both messages, to name no Case and to ask only whether a Case of this session fixed the cause, and to keep the timing: the hold still asks once, and the reminder still comes once a stretch. A stretch ends at the person's next message, and the hook judges whether a line was told by its text (`untold`). With no Case list, the reminder's line is the same for one lesson at every ratification, so a second ratification inside one stretch no longer reminds again for other Cases; the person's answer kept the reminder at once for each message the person sends. Case 694.1 replaces the Criterion of `estimate-ledger-write-asks-for-the-mark-of-a-lesson`, and Case 694.2 that of `estimate-ledger-write-reminds-of-the-mark-on-a-decision-line`. Each Criterion promises which Cases its stderr line names. The two lines of each old Criterion that the new one does not carry are its stderr line with the list of Cases and its line on which Cases are named; both are replaced by design, and every other line is carried word for word. The then lines of the two sub-cases share many words because the hold and the reminder are two messages of one hook, checked by two Estimates. Each sub-case states its own message, so the likeness stands. The `purpose` and `method` of both Estimates state no list of Cases, so they stand. The Purpose of `rule-ledger-write` says that the hook asks whether a Case of the session closed the cause and reminds the agent; it names no list, so it stands, and this Case does not touch that page, which Case 691 of this session changes. Case 691 and Case 692 change other functions of `guppi/ledger.py`; this Case changes only the two stderr lines and their docstrings. A Grep `has no mark|held —|fix its cause` over `guppi/`, `tests/`, `.claude/` and `vault/wiki/` printed `guppi/ledger.py`, `guppi/ratified.py`, `tests/test_ledger.py`, `tests/test_onward.py`, `vault/wiki/estimates/estimate-ledger-write-asks-for-the-mark-of-a-lesson.md` and `vault/wiki/estimates/estimate-ledger-write-reminds-of-the-mark-on-a-decision-line.md`. The hit in `guppi/ratified.py` is a docstring about the text a Case file held, not about a lesson, so it stands. The hit in `tests/test_onward.py` is a sample refusal of the ledger hook in a test of `guppi/onward.py`. By its docstring, that hook acts on any line the ledger hook sent back, not on its words, so the sample stands. `orchestration.md` sets what the reply after the reminder holds and names no Case of the message, so it stands.

> **problem:**
> The question about a lesson's mark lists every candidate Case, nineteen at the end of a session, though the hook cannot tell which of them relates to the lesson. The list is noise, and it suggests a link where there is none.

> **recommend:**
> - **Which question does the change cover?**
>   - Recommended: (a) both the hold and the reminder, one sub-case per Estimate, through the one shared function.
>   - Answer: agreed, (a).
> - **Which Cases should the question name?**
>   - Recommended: (a) name no Case; the message asks whether a Case of this session fixed the cause of the lesson, and the rest of the message stays.
>   - Answer: agreed, (a).
> - **Should the reminder come again at later ratifications?**
>   - Recommended: (a) keep the timing as it is; only the wording changes.
>   - Answer: agreed, (a).

### Case 694.1 — The hold of an unmarked lesson names no Case

> **given:**
> `guppi/ledger.py`: the ledger hook, whose `held_message` gives the stderr line of the hold.
> **＋** `tests/test_ledger.py`: the tests of the ledger hook.
> **＋** `estimate-ledger-write-asks-for-the-mark-of-a-lesson`: its Criterion is replaced whole.
> **＋** `estimate-ledger-write-reminds-of-the-mark-on-a-decision-line`: the reminder after the write, which Case 694.2 sets.

> **when:**
> The `Stop` hook `uv run guppi ledger` of `guppi/ledger.py` finds a fresh `lesson[<slug>]` line in a `LEDGER` block of the session that carries no `{addressed_by:...}`, and a decision line of the session stands before it, in the session's ledger or earlier among the lines of the same `Stop`.

> **then:**
> At the `Stop` of the reply that carries it, the hook holds the line back once, unless it already asked about it since the person's last message.
> **＋** For each held line the hook exits 2 and prints: "ledger: lesson[<slug>] held — did a Case of this session fix its cause? Then add {addressed_by:case <N>}, the Case or sub-case that fixed it, and repeat the line; otherwise repeat it unchanged."
> **＋** The stderr line names no Case, however many decision lines stand before the lesson line.
> **＋** The line lands as it stands once the hook's question about it stands in a refusal since the person's last message, or when it stands only in an earlier text of the transcript.
> **＋** A held line keeps back no other line: the rest of that `Stop` lands in the ledger.
> **－** An unmarked line never lands beside a marked one: `{addressed_by:...}` on a `lesson[<slug>]` line in the session's ledger, or in that `Stop`, drops the unmarked line of the slug.
> **－** The hook holds no lesson line that precedes every decision line of the session, no line it refuses for its prefix or cannot parse, and no line that the ledger of some session already holds.
> **－** The hook never holds a decision line for its `{addresses:...}`: it writes it, and the reminder after the write is `estimate-ledger-write-reminds-of-the-mark-on-a-decision-line`.
> **－** A session with no `hi` gets no question. The flag `stop_hook_active` changes nothing here, but when it is set and the transcript is unreadable, the hook lets the line land as it stands.

> **tasks:**
> - [ ] update `estimate-ledger-write-asks-for-the-mark-of-a-lesson`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the question of the hold names no Case`
> - [ ] `guppi/ledger.py`: `held_message` takes the slug alone and asks whether a Case of this session fixed the cause; `named_cases` goes once no caller is left; the module docstring and the docstring of `held_message` say that the stderr line names no Case.
> - [ ] `tests/test_ledger.py`: the held line's stderr line names no Case with decision lines of several Cases before it; the test of the Cases named in first-seen order goes; the other tests of the hold build the message from the slug alone.
> - [ ] read `estimate-ledger-write-asks-for-the-mark-of-a-lesson`

> **ratification:**
> ```
> - decision[case 694.1][update][estimate-ledger-write-asks-for-the-mark-of-a-lesson]{ref:rule-ledger-write}
> ```

### Case 694.2 — The reminder of an unmarked lesson names no Case

> **given:**
> `guppi/ledger.py`: the ledger hook, whose `reminder_message` gives the stderr line of the reminder.
> **＋** `guppi/materialize.py`: its `unlinked_lessons` judges which lessons no mark links to a Case.
> **＋** `tests/test_ledger.py`: the tests of the ledger hook.
> **＋** `estimate-ledger-write-reminds-of-the-mark-on-a-decision-line`: its Criterion is replaced whole.

> **when:**
> The `Stop` hook `uv run guppi ledger` of `guppi/ledger.py` writes fresh decision lines of the reply just finished, and a `lesson[<slug>]` line stands before them, in the session's ledger or among the lines the same `Stop` writes, with no `{addressed_by:...}` and no decision line after it that carries `{addresses:<slug>}`.

> **then:**
> The hook writes every line of the `Stop` as it would without the reminder, and holds back no line for the mark.
> **＋** After the write, for each such lesson the hook exits 2 and prints: "ledger: lesson[<slug>] has no mark — did a Case of this session fix its cause? Then write the decision line of the Case or sub-case that fixed it again with {addresses:<slug>} added, alone in a LEDGER block; otherwise go on without it."
> **＋** The stderr line names no Case, however many fresh decision lines follow the lesson.
> **＋** The stderr line is printed only when it does not already stand in a refusal of the hook since the person's last message.
> **＋** A decision line written again with `{addresses:<slug>}` lands beside the first line, the hook reminds of that lesson no more, and `guppi materialize` gives the lesson entry `addressed_by`.
> **＋** The hook judges which lessons no mark links to a Case by one function of `guppi/materialize.py`, over the ledger lines in their order.
> **－** A lesson that carries `{addressed_by:...}`, that a decision line after it marks, or that stands after every fresh decision line brings no reminder; nor does a fresh lesson line that the same `Stop` holds back or refuses.
> **－** A `defer` line, and a decision line from an earlier text of the transcript, bring no reminder.
> **－** A session with no `hi` gets no reminder. With `stop_hook_active` set and a transcript the hook cannot read, the lines land and the hook prints nothing.

> **tasks:**
> - [ ] update `estimate-ledger-write-reminds-of-the-mark-on-a-decision-line`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the reminder names no Case`
> - [ ] `guppi/ledger.py`: `reminder_message` takes the slug alone and asks whether a Case of this session fixed the cause; `unaddressed` still finds the lessons that fresh decision lines follow; the module docstring and the docstrings of `unaddressed` and `reminder_message` say that the stderr line names no Case and is told once a stretch.
> - [ ] `tests/test_ledger.py`: the reminder names no Case with fresh decision lines of several Cases after the lesson; the tests of the Cases named in first-seen order and of a reminder told again for other Cases in one stretch go; the other tests of the reminder build the message from the slug alone.
> - [ ] read `estimate-ledger-write-reminds-of-the-mark-on-a-decision-line`

> **ratification:**
> ```
> - decision[case 694.2][update][estimate-ledger-write-reminds-of-the-mark-on-a-decision-line]{ref:rule-ledger-write}
> ```
