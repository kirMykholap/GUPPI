## Case 577 — The checks at the end of a reply go silent for the rest of a stretch after any refusal

> **context:**
> Six checks run each time a reply of the main agent ends. They are the `Stop` hooks of `.claude/settings.json`: `guppi ledger`, `guppi ratified`, `guppi casecheck`, `guppi context`, `guppi onward` and `guppi onward --plan`. Claude Code gives each one the flag `stop_hook_active`. Each of the six returns at once when the flag is set, so that it cannot send the agent back again and again. The design read the flag as marking only the one reply after a refusal. The transcript of session 1237 (`dd5dac5e`) shows otherwise: the flag stays set until the person writes again. In record 529, `guppi onward --plan` refused the end of the reply that acknowledged the re-ratification of 567 and 569, and sent the agent on. In the same stretch, with no `user` record of `origin.kind` `human` until record 657, the agent left Plan Mode, ran `/work` and ended Retro. At the `Stop` of record 654, after the reply that ended Retro, all six hooks ran in about half a second each with no output (`hasOutput` false). So the ledger wrote none of the fourteen readings, no size line showed, and `guppi onward` did not send the agent to `/handoff`. The person had to ask what comes next. The readings landed at the next `Stop`, after the person's message, and needed a second commit (`a9e58997`). The two other `Stop` records of that session with `hasOutput` false, 490 and 735, also follow a refusal of a `Stop` hook in the same stretch (records 457 and 700). The transcript does not hold the flag itself. The person took the transcript as enough evidence, and the live readings below confirm the fix. No lesson page records this behaviour of the flag. The person chose to fix the two checks on the path from Retro to `/handoff`, `guppi onward` and `guppi ledger`. Neither trusts the flag any more. Each judges by its own refusal in the stretch, which runs from the person's last message to now. `guppi onward` exits 2 at most once in a stretch. The ledger writes and judges its lines whatever the flag says, since it never writes a line twice. `/pre-spec` found that a ledger refusal limited to once a stretch would lose a second faulty line of the same stretch without a word. The person chose that the ledger tells each refused line once in a stretch: it prints the stderr line of a refused line of the reply just finished only when that line does not already stand in its own refusals of the stretch. A repeat of the same faulty line stays silent, so the hook cannot loop. No `hi` and an error of its own stay once a stretch. The shape of the transcript records rests on the same transcript, on Claude Code 2.1.282. A refusal is a `user` record marked `isMeta`, its text opening with `Stop hook feedback:` and holding a line `[<command>]: <stderr>` (records 457, 529, 700). A message of the person is a `user` record whose `origin.kind` is `human` (records 524, 657). The other four hooks keep the flag as their guard: the size line is a small loss, and `ratified` and `casecheck` have nothing to do at the end of Retro, since a Case is ratified only by a message of the person, which clears the flag. `guppi onward --plan` keeps its guard too, and `rule-prespec-onward` and `estimate-prespec-onward-sends-the-agent-on` stand. The docstring of `guppi/casecheck.py` says that a refusal of a `Stop` hook adds no `user` record (measured 2026-09-27). The transcript of 1237 shows that it adds one, marked `isMeta`. Its judgment skips records marked `isMeta`, so its behaviour stands and this Case leaves it alone. The stale sentence is a note for the handoff. Each sub-case replaces the Criterion of one Estimate whose Criterion speaks of the flag: two of `rule-retro-onward` and six of `rule-ledger-write`. The four refusal Estimates of the ledger said that with the flag set the hook judges no line, and that sentence becomes false. The check of the answer noted Criterion lines that the new Criteria do not carry, and each change is on purpose. Each line that named the flag or the re-fire is rewritten for the stretch. The line on errors of `guppi onward` now names the transcript among its reads. The When of `estimate-ledger-write-lifts` says "a reply" in place of "a turn", since the hook fires at the end of each reply. Its four lines on the refusals are folded into one line that names `rule-ledger-write`, because each refusal has its own Estimate. In `estimate-ledger-write-exits-2-on-an-error`, four lines are rewritten for the stretch: the error coming back, an error while the hook reads the payload, the re-fire, and a refusal with no error. The check also noted that sibling sub-cases share lines. That is on purpose too: each Estimate must read alone. So the definition of the stretch stands in both hooks' Criteria, and the lines on silence and errors promise the same thing of each hook. The lines on a missing `hi` and the lines common to the four refusals also stand in each Criterion that needs them. `/pre-spec` also found two sentences of the rule pages that the change leaves stale, and each now has its own pair. 577.4 rewords the sentence of `rule-ledger-write` on an error while the hook reads the payload, which still spoke of a re-fire. 577.2 adds the transcript to the reads that `rule-retro-onward` lists for an error of the hook. `estimate-retro-runs-on-to-the-handoff` already promises that the agent commits the session folder and calls `/handoff` after the reply that ends Retro, in the same turn. This Case makes that hold after a long stretch, so its Criterion stands, and its pending reading checks the change too. No page is created, so no vault query was run. The rule texts change at the librarian's run and the code in Work Mode. No reader refuses a text in between, since the hooks read only Claude Code's transcript, so no old form is kept. Searches follow. A Grep for `stop_hook_active|re-fire|once a turn|follows a refusal` over `vault/wiki/rules/`, `vault/wiki/*.md`, `.claude/`, `guppi/`, `tests/` and `CLAUDE.md` printed 17 files: `tests/test_casecheck.py`, `log.md`, `rule-case-check`, `rule-context-size`, `guppi/ledger.py`, `guppi/context.py`, `guppi/casecheck.py`, `guppi/ratified.py`, `guppi/onward.py`, `rule-ledger-write`, `tests/test_ratified.py`, `rule-prespec-onward`, `tests/test_onward.py`, `tests/test_ledger.py`, `rule-retro-onward`, `rule-spec-write` and `tests/test_context.py`. The hits in `rule-case-check`, `rule-context-size`, `rule-spec-write`, `rule-prespec-onward` and their code and tests describe the hooks that keep the flag, so they stand. A Grep for `stop_hook_active|re-fire|refusal of a .Stop. hook` over the Estimates of `rule-ledger-write` and `rule-retro-onward` printed the eight Estimates this Case replaces. A Grep for `guppi onward|rule-retro-onward|fires at most` over `vault/wiki/` printed 20 files: `brief.md`, `log.md`, `where-to-stop.md`, `rule-where-to-stop`, `rule-end-of-work`, `rule-hook-registry`, `rule-retro`, `rule-retro-onward`, `rule-prespec-onward`, `estimate-retro-onward-sends-the-agent-to-the-handoff`, `estimate-retro-onward-exits-2-on-an-error`, `estimate-retro-runs-on-to-the-handoff`, `estimate-prespec-onward-sends-the-agent-on`, `estimate-case-protocol-defers-in-one-reply`, `estimate-python-utf8-output-intact`, `estimate-where-to-stop-stops-only-on-its-conditions`, `decision-case-531.9`, `decision-case-555`, `decision-case-555.3` and `decision-case-575`; the decision pages were not opened. In `rule-where-to-stop` and `where-to-stop.md`, a reply that opens with `STOP:` still ends. The hit in `rule-retro`, that the hook sends the agent on after the reply that ends Retro, becomes true after a long stretch. `rule-hook-registry` and `rule-end-of-work` name only the registration and the child, which do not change. The hits in the three other Estimates stand in their Results. A Grep for `guppi onward|fires at most` over `.claude/skills/` printed nothing.

> **problem:**
> After any `Stop` hook refuses a reply, Claude Code keeps `stop_hook_active` set until the person writes again. Every `Stop` hook reads that flag as "do nothing". When the run goes on from Plan Mode through Work Mode to Retro in one stretch, the reply that ends Retro writes no ledger line and nothing sends the agent to `/handoff`. The question was how to answer this, and how the checks that change keep themselves from looping.

> **recommend:**
> - **How to deal with the silent end of Retro**
>   - Recommended: (a) fix the checks on the path. They no longer trust the mark and keep themselves from looping by what they can see themselves, so at the end of Retro the readings reach the ledger and the agent is sent to `/handoff`, even in a long stretch.
>   - Answer: (a), as recommended.
> - **Whether to confirm the cause before the change**
>   - Recommended: (a) take the transcript as enough. The Case states the cause as the transcript shows it, the tests cover a reply that ends with the mark on, and a live reading at the end of Retro after a long stretch confirms the fix.
>   - Answer: (a), as recommended.
> - **Which checks stop trusting the mark**
>   - Recommended: (b) the check that sends the agent to `/handoff` and the ledger writer. The other four checks stay as they are.
>   - Answer: (b), as recommended.
> - **How the check that sends the agent to `/handoff` avoids looping**
>   - Recommended: (a) once per stretch, by its own earlier message. It stops a reply only when its own message does not already stand in the transcript since the person's last message, and a stop by another check earlier in the stretch no longer silences it.
>   - Answer: (a), as recommended.
> - **How the ledger writer reports a refused line while the mark is on**
>   - Recommended: (a) once per stretch, like the check that sends the agent to `/handoff`. With the mark on it writes the good lines, and it stops the reply to report a refused line or an error of its own only when its own message does not already stand since the person's last message. One module holds this judgment for both checks.
>   - Answer: (a), as recommended.
> - **Change**
>   - Asked: on the finding of `/pre-spec` that a second faulty line in the same stretch would be lost without a word, the person chose to report each refused line once per stretch. The hook exits 2 when a refused line of the reply just finished is not already named in its own refusals of the stretch, and a repeat of the same line stays silent. An error of the hook itself and a missing `hi` stay once a stretch.
>   - Taken: 577.3 and the rule text tell each refused line once in a stretch, and 577.5 to 577.8 point their exit to that rule.

### Case 577.1 — `guppi onward` sends the agent to `/handoff` once a stretch, whatever the flag says

> **given:**
> `rule-retro-onward` — the rule of the hook that sends the agent from Retro to `/handoff`
> **＋** `estimate-retro-onward-sends-the-agent-to-the-handoff` — the promise whose Criterion this sub-case replaces
> **＋** `guppi/onward.py` — the hook
> **＋** `guppi/ledger.py` — the module that holds the one judgment of the stretch and of a hook's own refusal
> **＋** `tests/test_onward.py` — the tests of the hook
> **＋** `.claude/settings.json` — the registration of the hook on `Stop`
> **＋** `vault/wiki/where-to-stop.md` — the conditions under which the agent stops for the person
> **＋** `raw/<date>/<hi HHMM>/handoff.md` — the file whose presence ends the hook's work

> **when:**
> The `Stop` hook `uv run guppi onward` receives the payload of the end of a reply of the main agent.

> **then:**
> It exits 2 when the event log of the session's window holds the mark `retro` of this session, `raw/<date>/<hi HHMM>/handoff.md` does not stand, the reply that ended does not open with `STOP:`, and its own refusal does not stand in the stretch.
> **＋** The stretch is the records of the transcript at `transcript_path` after the last `user` record whose `origin.kind` is `human`. Its own refusal is a `user` record marked `isMeta` whose text opens with `Stop hook feedback:` and holds a line that opens with `[uv run guppi onward]: `.
> **＋** A refusal of another `Stop` hook in the stretch does not silence it, and neither does `stop_hook_active`.
> **＋** Its reason on stderr tells the agent to commit the session folder and call `/handoff`, and, when a condition of `vault/wiki/where-to-stop.md` holds, to open its reply with `STOP:` and ask the person instead.
> **＋** In every other case with no error of its own it exits 0 and prints nothing: before the mark `retro`, once `handoff.md` stands, once its own refusal stands in the stretch, on a reply that opens with `STOP:`, and with `stop_hook_active` set when it cannot read the transcript.
> **＋** It judges the stretch and its own refusal by the one function of `guppi/ledger.py` that the ledger hook calls.
> **＋** `.claude/settings.json` registers it on `Stop`, after `uv run guppi ledger`, `uv run guppi ratified`, `uv run guppi casecheck` and `uv run guppi context`.
> **－** It counts nothing, reads no test result and calls no model: its judgment is the mark, the file, its own refusal in the transcript and the first word of the reply.
> **－** Without a `hi` of the session in the event log, and with no error of its own, it exits 0.
> **－** It writes no file and no mark.
> **－** `uv run guppi onward --plan` keeps `stop_hook_active` as its guard.

> **tasks:**
> - [ ] update `rule-retro-onward` — the hook fires once a stretch, judged by its own refusal in the transcript, not by `stop_hook_active`
>   - old: `` It judges only the state of files and of the payload — the mark `retro` of the session in the event log, the absence of `handoff.md`, the flag `stop_hook_active` and the first word `STOP:` of the reply — and counts nothing, so it fires at most once a turn and cannot loop. ``
>   - new: `` It judges only the state of files, of the payload and of the transcript — the mark `retro` of the session in the event log, the absence of `handoff.md`, its own refusal after the person's last message in the transcript, and the first word `STOP:` of the reply — and counts nothing, so it fires at most once a stretch, from one message of the person to the next, and cannot loop. A refusal of another `Stop` hook earlier in the stretch does not silence it, and neither does the flag `stop_hook_active`, which Claude Code keeps set from that refusal until the person's next message, as the transcript of session 1237 shows; with the flag set and a transcript it cannot read, it exits 0. The stretch and its own refusal are judged by one function of `guppi/ledger.py`, which the ledger hook calls too (case 577.1). ``
>   - set: `{implementation_ref: [guppi/onward.py, guppi/ledger.py, tests/test_onward.py, .claude/settings.json]}`
>   - change: `the hook fires once a stretch, judged by its own refusal after the person's last message in the transcript; stop_hook_active no longer silences it (case 577.1)`
> - [ ] update `estimate-retro-onward-sends-the-agent-to-the-handoff`
>   - set: `{status: pending, purpose: "Whether guppi onward refuses the end of a reply after the retro mark while handoff.md does not stand, once a stretch by its own refusal in the transcript whatever stop_hook_active says, not on a reply that opens with STOP:, and is silent otherwise, counting nothing", method: "uv run pytest tests/test_onward.py; by hand at the first end of Retro after the render that follows a refusal of another Stop hook in the same stretch: the transcript, the event log and handoff.md, recorded in the estimate line"}`
>   - change: `the Criterion replaced whole — the hook fires once a stretch, judged by its own refusal in the transcript, and stop_hook_active no longer silences it (case 577.1)`
> - [ ] `guppi/ledger.py`: one function that gives the text of the refusals of a given hook command in the transcript after the last `user` record whose `origin.kind` is `human`, and None when the transcript cannot be read
> - [ ] `guppi/onward.py`: the run without `--plan` judges its own refusal in the stretch by that function in place of `stop_hook_active`, and exits 0 when the flag is set and the function gives None; the docstring follows
> - [ ] `tests/test_onward.py`: with the flag set after another hook's refusal it exits 2; with its own refusal in the stretch it exits 0; after a later message of the person it exits 2 again; with the flag set and no readable transcript it exits 0; `--plan` with the flag still exits 0
> - [ ] read `estimate-retro-onward-sends-the-agent-to-the-handoff` — in a later session

> **ratification:**
> ```
> - decision[case 577.1][update][rule-retro-onward]{ref:rule-retro-onward}
> - decision[case 577.1][update][estimate-retro-onward-sends-the-agent-to-the-handoff]{ref:rule-retro-onward}
> ```

### Case 577.2 — An error of `guppi onward` comes back once a stretch

> **given:**
> `rule-retro-onward` — the rule of the hook that sends the agent from Retro to `/handoff`
> **＋** `estimate-retro-onward-exits-2-on-an-error` — the promise whose Criterion this sub-case replaces
> **＋** `estimate-retro-onward-sends-the-agent-to-the-handoff` — the promise that sets the stretch and the hook's own refusal
> **＋** `guppi/onward.py` — the hook
> **＋** `tests/test_onward.py` — the tests of the hook

> **when:**
> The `Stop` hook `uv run guppi onward` fires, and an exception rises in `guppi/onward.py` after the hook has read the payload: while it reads the reply, the session folder, the event log or the transcript.

> **then:**
> `guppi onward` exits 2. Its stderr holds `onward: not checked: <error>` and the advice: if Retro has ended and `handoff.md` does not stand, commit the session folder and call `/handoff`.
> **＋** While the cause stands, `guppi onward` blocks with the same error at the first `Stop` of each stretch of the session, before Retro too.
> **－** An empty payload of `guppi onward` exits 0 with nothing on stderr.
> **－** It exits 0 and prints nothing when its own refusal stands in the stretch, as `estimate-retro-onward-sends-the-agent-to-the-handoff` judges it, or when `stop_hook_active` is set and it cannot tell whether one stands, so it fires at most once a stretch.
> **－** With no error, `guppi onward` exits 2 or 0 by its own judgment, as before.

> **tasks:**
> - [ ] update `rule-retro-onward` — an error of the hook comes back once a stretch, and the transcript is among its reads
>   - old: `an exception while it reads the reply, the session folder or the event log`
>   - new: `an exception while it reads the reply, the session folder, the event log or the transcript`
>   - old: `on the re-fire it exits 0, so this too fires at most once a turn (case 555.3).`
>   - new: `` once its own refusal stands in the stretch it exits 0, and so it does with `stop_hook_active` set when it cannot tell whether one stands, so this too fires at most once a stretch (cases 555.3, 577.2). ``
>   - change: `an error of the hook exits 2 once a stretch, judged by its own refusal in the transcript, which is among its reads (case 577.2)`
> - [ ] update `estimate-retro-onward-exits-2-on-an-error`
>   - set: `{status: pending, purpose: "Whether guppi onward exits 2 with the error and the advice to call /handoff on stderr when it raises after reading the payload, once a stretch by its own refusal in the transcript, and exits 0 on an empty payload"}`
>   - change: `the Criterion replaced whole — the error comes back once a stretch, judged by the hook's own refusal in the transcript, not by stop_hook_active (case 577.2)`
> - [ ] `tests/test_onward.py`: an error with its own refusal in the stretch exits 0; with another hook's refusal and the flag set it exits 2; with the flag set and no readable transcript it exits 0
> - [ ] read `estimate-retro-onward-exits-2-on-an-error` — in a later session

> **ratification:**
> ```
> - decision[case 577.2][update][rule-retro-onward]{ref:rule-retro-onward}
> - decision[case 577.2][update][estimate-retro-onward-exits-2-on-an-error]{ref:rule-retro-onward}
> ```

### Case 577.3 — The ledger hook writes whatever the flag says and tells each refused line once a stretch

> **given:**
> `rule-ledger-write` — the rule of the hook that writes the ledger lines
> **＋** `estimate-ledger-write-lifts` — the promise whose Criterion this sub-case replaces
> **＋** `guppi/ledger.py` — the hook, and the one judgment of the stretch and of a hook's own refusals
> **＋** `guppi/gate.py` — the gate whose advice the Criterion quotes
> **＋** `guppi/onward.py` — the other hook that calls the judgment
> **＋** `tests/test_ledger.py` — the tests of the hook
> **＋** `raw/<hi date>/<hi HHMM>/ledger.md` — the session's ledger, which the hook appends to

> **when:**
> The `Stop` hook `uv run guppi ledger` fires at the end of a reply of the main agent, with `transcript_path` and `last_assistant_message` in its payload; or `guppi gate` refuses a `Skill` call for an item of the Spec without a ledger line.

> **then:**
> In a session with a `hi` recorded, every line `- decision[`, `- estimate[`, `- lesson[` inside a `LEDGER` block of any text of the main agent in the transcript, the reply just finished included, lands in `raw/<hi date>/<hi HHMM>/ledger.md` with the time of writing, once — a body already in the ledger of any session is not written again.
> **＋** With `stop_hook_active` set, the hook writes and judges the lines as without it.
> **＋** A block in a text followed by a tool call in the same turn reaches the ledger at the next `Stop` of the session, with the time of that `Stop`; the reply that ends in the text lands it now.
> **＋** The gate's advice to the agent reads "The text before a tool call waits for the next Stop: end this reply in text with the LEDGER block, then call /<skill> in the next reply."
> **＋** For each refused line of the reply just finished, the hook prints its stderr line only when that stderr line does not already stand in its own refusals of the stretch, and exits 2 when it prints one; a repeat of a line already told stays silent.
> **＋** No `hi`, and an error of its own after it read the payload, exit 2 only when no refusal of its own stands in the stretch; otherwise the hook exits 0 and prints nothing.
> **＋** The stretch is the records of the transcript at `transcript_path` after the last `user` record whose `origin.kind` is `human`. Its own refusal is a `user` record marked `isMeta` whose text opens with `Stop hook feedback:` and holds a line that opens with `[uv run guppi ledger]: `; one function of `guppi/ledger.py` judges both, and `guppi/onward.py` calls it with its own command.
> **－** A line that a refusal of `rule-ledger-write` refuses does not land while that refusal holds.
> **－** Without a `hi`, the ledger is untouched.
> **－** With `stop_hook_active` set and a transcript it cannot read, it writes the lines of `last_assistant_message` and exits 0.
> **－** The last turn of a session that ends in a tool call has no `Stop` after it; its lines are a finding of Retro, not of the hook.

> **tasks:**
> - [ ] update `rule-ledger-write` — the hook writes whatever `stop_hook_active` says, tells each refused line once a stretch, and tells no `hi` and its own error once a stretch
>   - old: `` With `stop_hook_active` set (the re-fire after a block) it exits 0 and writes nothing, so it cannot loop. ``
>   - new: `` It writes and judges the lines whether `stop_hook_active` is set or not, since a line already in a ledger is never written twice: Claude Code keeps the flag set from the first refusal of any `Stop` hook until the person's next message, as the transcript of session 1237 shows, so a run that a hook sends on — Plan Mode into Work Mode and Retro — would otherwise write nothing until the person writes. Its refusals are judged over the stretch — the records of the transcript after the person's last message, the last `user` record whose `origin.kind` is `human` — its own refusal being a `user` record marked `isMeta` whose text opens with `Stop hook feedback:` and holds a line opening with `[uv run guppi ledger]: `. For each refused line of the reply just finished, every refusal this page names prints its stderr line only when that stderr line does not already stand in its own refusals of the stretch, and exits 2 when it prints one, so each faulty line is told once and a repeat of it stays silent; no `hi` and an error of its own exit 2 only when no refusal of its own stands in the stretch. Otherwise it exits 0 and prints nothing, and with the flag set and a transcript it cannot read it exits 0 too. One function of `guppi/ledger.py` judges the stretch, and `guppi onward` calls it (case 577.3). ``
>   - change: `the hook writes whatever stop_hook_active says; each refused line is told once a stretch, and no hi and its own error once a stretch, judged by its own refusals in the transcript (case 577.3)`
> - [ ] update `estimate-ledger-write-lifts`
>   - set: `{status: pending, method: "pytest in tests/test_ledger.py and tests/test_gate.py with piped payloads against a temp vault; by hand once, the ledger of the first session after the change whose reply that ends Retro follows a refusal of a Stop hook in the same stretch: its lines written at that Stop, with its time"}`
>   - change: `the Criterion replaced whole — the hook writes whatever stop_hook_active says, tells each refused line once a stretch, and tells no hi and its own error once a stretch (case 577.3)`
> - [ ] `guppi/ledger.py`: `run` no longer returns on `stop_hook_active`; it prints the stderr line of a refused line only when the text of its own refusals in the stretch does not hold it, exits 2 for no `hi` or an error only when that text is empty, and exits 0 when the flag is set and the function gives None; the docstring follows
> - [ ] `tests/test_ledger.py`: the test of the flag writes the lines; a refused line already told in the stretch is silent while a new refused line in a later reply of the stretch exits 2; no `hi` and an error each exit 2 with no own refusal in the stretch and exit 0 with one; with the flag set and no readable transcript the lines of `last_assistant_message` are written and the hook exits 0
> - [ ] read `estimate-ledger-write-lifts` — in a later session

> **ratification:**
> ```
> - decision[case 577.3][update][rule-ledger-write]{ref:rule-ledger-write}
> - decision[case 577.3][update][estimate-ledger-write-lifts]{ref:rule-ledger-write}
> ```

### Case 577.4 — An error of the ledger hook comes back once a stretch

> **given:**
> `rule-ledger-write` — the rule of the hook that writes the ledger lines
> **＋** `estimate-ledger-write-exits-2-on-an-error` — the promise whose Criterion this sub-case replaces
> **＋** `estimate-ledger-write-lifts` — the promise that sets the stretch and the hook's own refusals
> **＋** `guppi/ledger.py` — the hook
> **＋** `tests/test_ledger.py` — the tests of the hook

> **when:**
> The `Stop` hook `uv run guppi ledger` fires, and an exception rises in `run` of `guppi/ledger.py` after it has read the payload: while it reads the transcript, the event log or the ledger, or while it judges or appends the lines.

> **then:**
> The hook exits 2 with `ledger: ledger.md not written: <error>` on stderr, so the agent sees the error at the end of that reply.
> **＋** A line not yet appended when the error rose waits for the next `Stop` of the session, which reads the transcript again.
> **＋** While the cause stands, the error comes back at the first `Stop` of each stretch.
> **－** An error while the hook reads the payload exits 0 with the error on stderr: the hook cannot tell its own refusal then, and exit 2 could loop.
> **－** When a refusal of its own stands in the stretch, as `estimate-ledger-write-lifts` judges it, or when `stop_hook_active` is set and it cannot tell whether one stands, the hook exits 0 and prints nothing, so it cannot loop.
> **－** A refusal of the hook with no error — no `hi`, or a refused line — keeps its own stderr line, and its exit as `estimate-ledger-write-lifts` sets it.

> **tasks:**
> - [ ] update `rule-ledger-write` — an error of the hook comes back once a stretch, and an error while it reads the payload is told by its own refusal
>   - old: `` and while the cause stands the error comes back at every `Stop`. ``
>   - new: `` and while the cause stands the error comes back at the first `Stop` of each stretch (case 577.4). ``
>   - old: `An error while it reads the payload exits 0 with the error on stderr, since the hook cannot tell a re-fire then (case 552.4).`
>   - new: `An error while it reads the payload exits 0 with the error on stderr, since the hook cannot tell its own refusal then (cases 552.4, 577.4).`
>   - change: `an error of the hook comes back at the first Stop of each stretch; an error while it reads the payload exits 0, since the hook cannot tell its own refusal then (case 577.4)`
> - [ ] update `estimate-ledger-write-exits-2-on-an-error`
>   - set: `{status: pending, purpose: "Whether the ledger hook exits 2 with the error on stderr when it raises after reading the payload, once a stretch by its own refusal in the transcript, and exits 0 on an error while reading the payload"}`
>   - change: `the Criterion replaced whole — the error comes back once a stretch, judged by the hook's own refusal in the transcript, not by stop_hook_active (case 577.4)`
> - [ ] `guppi/ledger.py`: the docstring and the comment of the payload error say that the hook cannot tell its own refusal then
> - [ ] `tests/test_ledger.py`: an error with its own refusal in the stretch exits 0; with another hook's refusal and the flag set it exits 2
> - [ ] read `estimate-ledger-write-exits-2-on-an-error` — in a later session

> **ratification:**
> ```
> - decision[case 577.4][update][rule-ledger-write]{ref:rule-ledger-write}
> - decision[case 577.4][update][estimate-ledger-write-exits-2-on-an-error]{ref:rule-ledger-write}
> ```

### Case 577.5 — A line the grammar cannot read is judged whatever the flag says

> **given:**
> `estimate-ledger-write-refuses-a-line-it-cannot-read` — the promise whose Criterion this sub-case replaces
> **＋** `estimate-ledger-write-lifts` — the promise that sets when a refused line is told
> **＋** `guppi/ledger.py` — the hook
> **＋** `guppi/materialize.py` — `parse_line`, the one parse of a ledger line
> **＋** `tests/test_ledger.py` — the tests of the hook

> **when:**
> The `Stop` hook `uv run guppi ledger` finds a fresh line `- decision[`, `- estimate[` or `- lesson[` in a `LEDGER` block of the session, and `parse_line` of `guppi/materialize.py` returns None for it.

> **then:**
> The line is not written.
> **＋** The other lines of the `Stop` are written as before.
> **＋** When the refused line stands in the reply just finished, the hook exits 2 with one stderr line per refused line: "ledger: line not written — the grammar of a ledger line does not read it: <line>. Write it again in the form of the table in case-schema.md."
> **＋** At every later `Stop`, a refused line from an earlier text of the transcript is skipped without a word.
> **－** A refused line gets no other refusal of the hook and no other stderr line.
> **－** A line already in the ledger of any session is not judged again.
> **－** Without a `hi` the hook judges no line. With `stop_hook_active` set it judges the line the same, and its stderr line is told once a stretch, as `estimate-ledger-write-lifts` sets it.

> **tasks:**
> - [ ] update `estimate-ledger-write-refuses-a-line-it-cannot-read`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — with stop_hook_active the line is judged the same, and its stderr line is told once a stretch (case 577.5)`
> - [ ] `tests/test_ledger.py`: with the flag set, a line the grammar cannot read is not written, and the hook exits 2 when its stderr line does not stand in its own refusals of the stretch
> - [ ] read `estimate-ledger-write-refuses-a-line-it-cannot-read` — in a later session

> **ratification:**
> ```
> - decision[case 577.5][update][estimate-ledger-write-refuses-a-line-it-cannot-read]{ref:rule-ledger-write}
> ```

### Case 577.6 — A reading of a page the session changes is judged whatever the flag says

> **given:**
> `estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session` — the promise whose Criterion this sub-case replaces
> **＋** `estimate-ledger-write-lifts` — the promise that sets when a refused line is told
> **＋** `guppi/ledger.py` — the hook
> **＋** `tests/test_ledger.py` — the tests of the hook

> **when:**
> The `Stop` hook `uv run guppi ledger` finds a fresh `estimate[<slug>]` line in a `LEDGER` block of the session, and a decision line `create` or `update` of `<slug>` stands in the session's ledger or among the lines the hook writes on the same `Stop`.

> **then:**
> The line is not written: what a session changes, it does not measure, and the reading of `<slug>` waits for a later session.
> **＋** A reading of the old slug of a page that an `update` of this session renames is refused by the same rule: the decision line names the old slug.
> **＋** The other lines of the `Stop` are written as before.
> **＋** When the refused line stands in the reply just finished, the hook exits 2 with one stderr line per refused line: "ledger: estimate[<slug>] not written — case N creates or updates <slug> in this session; what a session changes it does not measure: take the reading in a later session and name it in the handoff."
> **＋** A refused line of an earlier text of the transcript is skipped at every later `Stop` without a word.
> **－** A reading of a slug that no decision line `create` or `update` of this session names is written as before; a `defer` line of the slug does not refuse it.
> **－** Without a `hi` the hook judges no line. With `stop_hook_active` set it judges the line the same, and its stderr line is told once a stretch, as `estimate-ledger-write-lifts` sets it.

> **tasks:**
> - [ ] update `estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — with stop_hook_active the line is judged the same, and its stderr line is told once a stretch (case 577.6)`
> - [ ] `tests/test_ledger.py`: with the flag set, a reading of a page the session updates is not written, and the hook exits 2 when its stderr line does not stand in its own refusals of the stretch
> - [ ] read `estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session` — in a later session

> **ratification:**
> ```
> - decision[case 577.6][update][estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session]{ref:rule-ledger-write}
> ```

### Case 577.7 — A lesson without its prefix is judged whatever the flag says

> **given:**
> `estimate-ledger-write-refuses-a-lesson-without-its-prefix` — the promise whose Criterion this sub-case replaces
> **＋** `estimate-ledger-write-lifts` — the promise that sets when a refused line is told
> **＋** `estimate-ledger-write-refuses-a-mark-with-no-decision-line` — the promise that judges the mark of a lesson
> **＋** `guppi/ledger.py` — the hook
> **＋** `guppi/materialize.py` — `category_of`, the one table of prefixes
> **＋** `tests/test_ledger.py` — the tests of the hook

> **when:**
> The `Stop` hook `uv run guppi ledger` finds a fresh `lesson[<slug>]` line in a `LEDGER` block of the session. `category_of` of `guppi/materialize.py` does not put its slug under the lessons folder: the slug does not start with the lesson prefix.

> **then:**
> The line is not written.
> **＋** The other lines of the `Stop` are written as before.
> **＋** When the refused line stands in the reply just finished, the hook exits 2 with one stderr line per refused line: "ledger: lesson[<slug>] not written — a lesson slug starts with lesson-, then the area, then the cause: write the line again with the prefix."
> **＋** At every later `Stop`, a refused line from an earlier text of the transcript is skipped without a word.
> **－** A lesson line whose slug starts with the lesson prefix is not refused for its prefix; its mark is judged by `estimate-ledger-write-refuses-a-mark-with-no-decision-line`. A line already in the ledger of any session is not judged again.
> **－** `estimate[...]` and `decision[...]` lines are not judged by their prefix.
> **－** Without a `hi` the hook judges no line. With `stop_hook_active` set it judges the line the same, and its stderr line is told once a stretch, as `estimate-ledger-write-lifts` sets it.

> **tasks:**
> - [ ] update `estimate-ledger-write-refuses-a-lesson-without-its-prefix`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — with stop_hook_active the line is judged the same, and its stderr line is told once a stretch (case 577.7)`
> - [ ] `tests/test_ledger.py`: with the flag set, a lesson line without the prefix is not written, and the hook exits 2 when its stderr line does not stand in its own refusals of the stretch
> - [ ] read `estimate-ledger-write-refuses-a-lesson-without-its-prefix` — in a later session

> **ratification:**
> ```
> - decision[case 577.7][update][estimate-ledger-write-refuses-a-lesson-without-its-prefix]{ref:rule-ledger-write}
> ```

### Case 577.8 — A lesson mark with no decision line is judged whatever the flag says

> **given:**
> `estimate-ledger-write-refuses-a-mark-with-no-decision-line` — the promise whose Criterion this sub-case replaces
> **＋** `estimate-ledger-write-lifts` — the promise that sets when a refused line is told
> **＋** `estimate-ledger-write-refuses-a-lesson-without-its-prefix` — the refusal judged before the mark
> **＋** `guppi/ledger.py` — the hook
> **＋** `guppi/materialize.py` — the one judgment of the mark, which `guppi materialize` makes too
> **＋** `tests/test_ledger.py` — the tests of the hook

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
> **－** Without a `hi` the hook judges no line. With `stop_hook_active` set it judges the line the same, and its stderr line is told once a stretch, as `estimate-ledger-write-lifts` sets it.

> **tasks:**
> - [ ] update `estimate-ledger-write-refuses-a-mark-with-no-decision-line`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — with stop_hook_active the line is judged the same, and its stderr line is told once a stretch (case 577.8)`
> - [ ] `tests/test_ledger.py`: with the flag set, a lesson line whose mark has no decision line is not written, and is written at a later `Stop` once the decision line stands
> - [ ] read `estimate-ledger-write-refuses-a-mark-with-no-decision-line` — in a later session

> **ratification:**
> ```
> - decision[case 577.8][update][estimate-ledger-write-refuses-a-mark-with-no-decision-line]{ref:rule-ledger-write}
> ```
