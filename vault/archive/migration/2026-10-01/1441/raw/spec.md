<!-- approved 17:05:24 · session 85988eb7 -->

# Spec — session 1441, 2026-10-01

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

```then
update:
- slug: rule-retro-onward
  replace:
  - old: It judges only the state of files and of the payload — the mark `retro` of the session in the event log, the absence of `handoff.md`, the flag `stop_hook_active` and the first word `STOP:` of the reply — and counts nothing, so it fires at most once a turn and cannot loop.
    new: It judges only the state of files, of the payload and of the transcript — the mark `retro` of the session in the event log, the absence of `handoff.md`, its own refusal after the person's last message in the transcript, and the first word `STOP:` of the reply — and counts nothing, so it fires at most once a stretch, from one message of the person to the next, and cannot loop. A refusal of another `Stop` hook earlier in the stretch does not silence it, and neither does the flag `stop_hook_active`, which Claude Code keeps set from that refusal until the person's next message, as the transcript of session 1237 shows; with the flag set and a transcript it cannot read, it exits 0. The stretch and its own refusal are judged by one function of `guppi/ledger.py`, which the ledger hook calls too (case 577.1).
  set:
    implementation_ref:
    - guppi/onward.py
    - guppi/ledger.py
    - tests/test_onward.py
    - .claude/settings.json
  change: the hook fires once a stretch, judged by its own refusal after the person's last message in the transcript; stop_hook_active no longer silences it (case 577.1)
- slug: estimate-retro-onward-sends-the-agent-to-the-handoff
  set:
    status: pending
    purpose: Whether guppi onward refuses the end of a reply after the retro mark while handoff.md does not stand, once a stretch by its own refusal in the transcript whatever stop_hook_active says, not on a reply that opens with STOP:, and is silent otherwise, counting nothing
    method: 'uv run pytest tests/test_onward.py; by hand at the first end of Retro after the render that follows a refusal of another Stop hook in the same stretch: the transcript, the event log and handoff.md, recorded in the estimate line'
  change: the Criterion replaced whole — the hook fires once a stretch, judged by its own refusal in the transcript, and stop_hook_active no longer silences it (case 577.1)
```

```tasks
- [x] update `rule-retro-onward` — the hook fires once a stretch, judged by its own refusal in the transcript, not by `stop_hook_active`
- [x] update `estimate-retro-onward-sends-the-agent-to-the-handoff`
- [x] `guppi/ledger.py`: one function that gives the text of the refusals of a given hook command in the transcript after the last `user` record whose `origin.kind` is `human`, and None when the transcript cannot be read
- [x] `guppi/onward.py`: the run without `--plan` judges its own refusal in the stretch by that function in place of `stop_hook_active`, and exits 0 when the flag is set and the function gives None; the docstring follows
- [x] `tests/test_onward.py`: with the flag set after another hook's refusal it exits 2; with its own refusal in the stretch it exits 0; after a later message of the person it exits 2 again; with the flag set and no readable transcript it exits 0; `--plan` with the flag still exits 0
- [ ] read `estimate-retro-onward-sends-the-agent-to-the-handoff` — in a later session
```

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

```then
update:
- slug: rule-retro-onward
  replace:
  - old: an exception while it reads the reply, the session folder or the event log
    new: an exception while it reads the reply, the session folder, the event log or the transcript
  - old: on the re-fire it exits 0, so this too fires at most once a turn (case 555.3).
    new: once its own refusal stands in the stretch it exits 0, and so it does with `stop_hook_active` set when it cannot tell whether one stands, so this too fires at most once a stretch (cases 555.3, 577.2).
  change: an error of the hook exits 2 once a stretch, judged by its own refusal in the transcript, which is among its reads (case 577.2)
- slug: estimate-retro-onward-exits-2-on-an-error
  set:
    status: pending
    purpose: Whether guppi onward exits 2 with the error and the advice to call /handoff on stderr when it raises after reading the payload, once a stretch by its own refusal in the transcript, and exits 0 on an empty payload
  change: the Criterion replaced whole — the error comes back once a stretch, judged by the hook's own refusal in the transcript, not by stop_hook_active (case 577.2)
```

```tasks
- [x] update `rule-retro-onward` — an error of the hook comes back once a stretch, and the transcript is among its reads
- [x] update `estimate-retro-onward-exits-2-on-an-error`
- [x] `tests/test_onward.py`: an error with its own refusal in the stretch exits 0; with another hook's refusal and the flag set it exits 2; with the flag set and no readable transcript it exits 0
- [x] read `estimate-retro-onward-exits-2-on-an-error` — in a later session
```

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

```then
update:
- slug: rule-ledger-write
  replace:
  - old: With `stop_hook_active` set (the re-fire after a block) it exits 0 and writes nothing, so it cannot loop.
    new: 'It writes and judges the lines whether `stop_hook_active` is set or not, since a line already in a ledger is never written twice: Claude Code keeps the flag set from the first refusal of any `Stop` hook until the person''s next message, as the transcript of session 1237 shows, so a run that a hook sends on — Plan Mode into Work Mode and Retro — would otherwise write nothing until the person writes. Its refusals are judged over the stretch — the records of the transcript after the person''s last message, the last `user` record whose `origin.kind` is `human` — its own refusal being a `user` record marked `isMeta` whose text opens with `Stop hook feedback:` and holds a line opening with `[uv run guppi ledger]: `. For each refused line of the reply just finished, every refusal this page names prints its stderr line only when that stderr line does not already stand in its own refusals of the stretch, and exits 2 when it prints one, so each faulty line is told once and a repeat of it stays silent; no `hi` and an error of its own exit 2 only when no refusal of its own stands in the stretch. Otherwise it exits 0 and prints nothing, and with the flag set and a transcript it cannot read it exits 0 too. One function of `guppi/ledger.py` judges the stretch, and `guppi onward` calls it (case 577.3).'
  change: the hook writes whatever stop_hook_active says; each refused line is told once a stretch, and no hi and its own error once a stretch, judged by its own refusals in the transcript (case 577.3)
- slug: estimate-ledger-write-lifts
  set:
    status: pending
    method: 'pytest in tests/test_ledger.py and tests/test_gate.py with piped payloads against a temp vault; by hand once, the ledger of the first session after the change whose reply that ends Retro follows a refusal of a Stop hook in the same stretch: its lines written at that Stop, with its time'
  change: the Criterion replaced whole — the hook writes whatever stop_hook_active says, tells each refused line once a stretch, and tells no hi and its own error once a stretch (case 577.3)
```

```tasks
- [x] update `rule-ledger-write` — the hook writes whatever `stop_hook_active` says, tells each refused line once a stretch, and tells no `hi` and its own error once a stretch
- [x] update `estimate-ledger-write-lifts`
- [x] `guppi/ledger.py`: `run` no longer returns on `stop_hook_active`; it prints the stderr line of a refused line only when the text of its own refusals in the stretch does not hold it, exits 2 for no `hi` or an error only when that text is empty, and exits 0 when the flag is set and the function gives None; the docstring follows
- [x] `tests/test_ledger.py`: the test of the flag writes the lines; a refused line already told in the stretch is silent while a new refused line in a later reply of the stretch exits 2; no `hi` and an error each exit 2 with no own refusal in the stretch and exit 0 with one; with the flag set and no readable transcript the lines of `last_assistant_message` are written and the hook exits 0
- [ ] read `estimate-ledger-write-lifts` — in a later session
```

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

```then
update:
- slug: rule-ledger-write
  replace:
  - old: and while the cause stands the error comes back at every `Stop`.
    new: and while the cause stands the error comes back at the first `Stop` of each stretch (case 577.4).
  - old: An error while it reads the payload exits 0 with the error on stderr, since the hook cannot tell a re-fire then (case 552.4).
    new: An error while it reads the payload exits 0 with the error on stderr, since the hook cannot tell its own refusal then (cases 552.4, 577.4).
  change: an error of the hook comes back at the first Stop of each stretch; an error while it reads the payload exits 0, since the hook cannot tell its own refusal then (case 577.4)
- slug: estimate-ledger-write-exits-2-on-an-error
  set:
    status: pending
    purpose: Whether the ledger hook exits 2 with the error on stderr when it raises after reading the payload, once a stretch by its own refusal in the transcript, and exits 0 on an error while reading the payload
  change: the Criterion replaced whole — the error comes back once a stretch, judged by the hook's own refusal in the transcript, not by stop_hook_active (case 577.4)
```

```tasks
- [x] update `rule-ledger-write` — an error of the hook comes back once a stretch, and an error while it reads the payload is told by its own refusal
- [x] update `estimate-ledger-write-exits-2-on-an-error`
- [x] `guppi/ledger.py`: the docstring and the comment of the payload error say that the hook cannot tell its own refusal then
- [x] `tests/test_ledger.py`: an error with its own refusal in the stretch exits 0; with another hook's refusal and the flag set it exits 2
- [x] read `estimate-ledger-write-exits-2-on-an-error` — in a later session
```

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

```then
update:
- slug: estimate-ledger-write-refuses-a-line-it-cannot-read
  set:
    status: pending
  change: the Criterion replaced whole — with stop_hook_active the line is judged the same, and its stderr line is told once a stretch (case 577.5)
```

```tasks
- [x] update `estimate-ledger-write-refuses-a-line-it-cannot-read`
- [x] `tests/test_ledger.py`: with the flag set, a line the grammar cannot read is not written, and the hook exits 2 when its stderr line does not stand in its own refusals of the stretch
- [x] read `estimate-ledger-write-refuses-a-line-it-cannot-read` — in a later session
```

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

```then
update:
- slug: estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session
  set:
    status: pending
  change: the Criterion replaced whole — with stop_hook_active the line is judged the same, and its stderr line is told once a stretch (case 577.6)
```

```tasks
- [x] update `estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session`
- [x] `tests/test_ledger.py`: with the flag set, a reading of a page the session updates is not written, and the hook exits 2 when its stderr line does not stand in its own refusals of the stretch
- [x] read `estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session` — in a later session
```

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

```then
update:
- slug: estimate-ledger-write-refuses-a-lesson-without-its-prefix
  set:
    status: pending
  change: the Criterion replaced whole — with stop_hook_active the line is judged the same, and its stderr line is told once a stretch (case 577.7)
```

```tasks
- [x] update `estimate-ledger-write-refuses-a-lesson-without-its-prefix`
- [x] `tests/test_ledger.py`: with the flag set, a lesson line without the prefix is not written, and the hook exits 2 when its stderr line does not stand in its own refusals of the stretch
- [x] read `estimate-ledger-write-refuses-a-lesson-without-its-prefix` — in a later session
```

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

```then
update:
- slug: estimate-ledger-write-refuses-a-mark-with-no-decision-line
  set:
    status: pending
  change: the Criterion replaced whole — with stop_hook_active the line is judged the same, and its stderr line is told once a stretch (case 577.8)
```

```tasks
- [x] update `estimate-ledger-write-refuses-a-mark-with-no-decision-line`
- [x] `tests/test_ledger.py`: with the flag set, a lesson line whose mark has no decision line is not written, and is written at a later `Stop` once the decision line stands
- [x] read `estimate-ledger-write-refuses-a-mark-with-no-decision-line` — in a later session
```

## Case 578 — A later Frontier folds the open Work lines into one line

> **context:**
> After the first reply of `/hi`, three kinds of reply show the Frontier, the checklist of `frontier.md`. They are the reply that closes a line with no ratification, the reply that acknowledges a ratification and the reply that records a defer. The first reply of `/hi` shows the Work list as one block. `rule-skill-hi` says the Work is one block. Every later Frontier follows the form that the acknowledging-reply paragraph of `rule-case-protocol` sets, and that paragraph says the open ones stand one per line with a short title. In session 1237 the main agent folded the open `W` lines into one line in the later replies too. So the reading of `estimate-case-protocol-shows-the-frontier-after-a-closed-line` failed, and the reading of `estimate-case-protocol-acknowledging-reply` failed on the same point. In session 1441 the later replies kept the rule and listed 28 `W` lines before the question about which Case is next. The person decided that folding the `W` lines is the norm and that the Estimate is what is wrong. They also decided that the fold covers every later Frontier of Plan Mode. The `W` lines are readings the agent closes at `/hi`, in Work Mode or at Retro. The person does not pick them, and `frontier.md` keeps the full list.
>
> The text of the form stands in one sentence of the Render of `rule-case-protocol`, in its acknowledging-reply paragraph. The paragraph on Plan Mode and the Frontier makes the reply that closes a line end "as the acknowledging reply ends", so one `replace` pair changes both replies. Sub-case 578.2 carries that pair and replaces the Criterion of `estimate-case-protocol-acknowledging-reply` whole. Sub-case 578.1 replaces the Criterion of `estimate-case-protocol-shows-the-frontier-after-a-closed-line` whole. That Criterion states the fold itself and does not only point to the other Estimate. The reply that records a defer has no line form of its own. Its Estimate, `estimate-case-protocol-defers-in-one-reply`, checks only that the Frontier stands with the deferred line closed and the question after it, so its Criterion stands. The closing line of the old Criterion of 578.1 already says that the defer reply keeps the form of the acknowledging reply. The first reply of `/hi` keeps its own form, and `rule-skill-hi` does not change.
>
> Item C2 of the Frontier also failed `estimate-case-protocol-acknowledging-reply` on the length of the `Changes:` paragraph. After this Case was ratified, the person took C2 up. They kept the rule of one or two sentences as it stands, with no Case, and judged the length point passed. `raw/2026-10-01/1441/frontier.md` now shows the line closed `[x] C2 … · brief · work`. So 578.2 keeps that rule word for word. No reading line on the length point could be written in this session, because 578.2 updates `estimate-case-protocol-acknowledging-reply` and the ledger hook refuses a reading of an Estimate that a decision line of the same session updates. The reading in a later session covers that point.
>
> The check of the answer noted Criterion lines that the two sub-cases do not carry word for word. Each was changed on purpose. The `when` of each Estimate gains the clause that the schema is rendered from `rule-case-protocol`. In 578.1 the line on the checklist is split, so that the fold of the `W` lines stands on a line of its own. In 578.2 the four-part line now ends at the checklist, and the fold moves to the lines after it. The check also noted that some `then` lines of 578.2 share most of their words with lines of 578.1. That is on purpose. Both Estimates promise one form of the Frontier and one rule for the question after it, so each Criterion says the same thing in the same words.
>
> No code reads the Frontier of a reply. A Grep of `Frontier` over `guppi/*.py` printed `casecheck.py`, `backlog.py`, `recall.py`, `generate.py`, `ratified.py`, `prespec.py`, `context.py` and `onward.py`. Their hit lines read `frontier.md` or describe it, and none of them judges the checklist a reply shows. So no old form is kept. The schema reaches the chat only at the render of the librarian's run, so until then the loaded `case-schema.md` still asks for one line per open item. No vault query was run, because no page is created.
>
> Searches:
> - A Grep of `one per line|one line per open|Work is one block` over `vault/wiki/` outside `decisions/` printed seven files: `brief.md`, `case-schema.md`, `rule-case-protocol`, `rule-skill-hi`, `rule-skill-grill-me`, `estimate-case-protocol-acknowledging-reply` and `estimate-case-protocol-shows-the-frontier-after-a-closed-line`. The hit in `rule-skill-grill-me` is the list rule of a round. It says nothing of a Frontier and stands. The hit in `rule-skill-hi` sets the first reply of `/hi`, which stays. `case-schema.md` is the render of `rule-case-protocol` and follows it. `brief.md` was not read.
> - A Grep of `## Frontier` over `vault/wiki/rules/` printed one file, `rule-case-protocol`. Over `.claude/` it printed no file.
> - A Grep of `Frontier` over `.claude/` printed three files: `.claude/skills/pre-spec/SKILL.md`, `.claude/skills/hi/SKILL.md` and `.claude/agents/case-guppi.md`. The skill `hi` is rendered from `rule-skill-hi`, which was read. The other two hits speak of the open lines that `/pre-spec` checks and of the Frontier item of a dispatch, and they set no form for a shown Frontier.
> - A Grep of `Frontier` over `vault/wiki/estimates/estimate-case-protocol-*.md` printed six files. Beyond the two Estimates replaced here and `estimate-case-protocol-defers-in-one-reply`, the hits in `estimate-case-protocol-asks-in-the-grill-me-shape`, `estimate-case-protocol-shows-the-built-case` and `estimate-case-protocol-loaded` speak of the question which item is next, of the item of a dispatch and of a History line. None of them speaks of the form of the open lines, so they stand. `estimate-hi-writes-frontier` sets the file `frontier.md` and not a reply, so it stands too.

> **problem:**
> The schema wants each open line of a later Frontier on its own line, while the first reply of `/hi` folds the Work list. So a long list of open readings pushes the question about the next item far down each reply, and the Estimates fail the fold the person holds to be correct. The question was whether a later Frontier may fold the open `W` lines, and which replies that covers.

> **recommend:**
> - **Should a later Frontier fold the open Work lines into one line?**
>   - Recommended: (b) fold the open `W` lines into one line that lists their ids, as `/hi` does; each open `C` and `A` line stays on its own line with its title, and `frontier.md` keeps the full list.
>   - Answer: (b). Folding the `W` lines is the norm, so the Estimate is what is wrong.
> - **Which replies does the fold cover?**
>   - Recommended: (a) every later Frontier in Plan Mode: the reply that closes a line, the acknowledging reply and the defer reply fold alike, and this Case replaces the Criterion of both Estimates.
>   - Answer: (a).

### Case 578.1 — The reply that closes a line folds the open Work lines

> **given:**
> `estimate-case-protocol-shows-the-frontier-after-a-closed-line` — the promise whose Criterion this sub-case replaces
> **＋** `rule-case-protocol` — the Case schema, whose Render makes this reply end as the acknowledging reply ends
> **＋** `vault/wiki/case-schema.md` — the file rendered from that Render
> **＋** `estimate-case-protocol-acknowledging-reply` — the promise of the form this reply takes
> **＋** `raw/<date>/<hi HHMM>/frontier.md` — the Frontier of the session
> **＋** `rule-skill-hi` — the rule of the first reply of `/hi`
> **＋** `/pre-spec` — the step of `rule-prespec`, which the reply calls when no line under `## Cases` is open
> **＋** `rule-prespec-onward` — the hook that sends the agent on when no line under `## Cases` is open

> **when:**
> After the first reply of `/hi` and before the end of Plan Mode, with `vault/wiki/case-schema.md` rendered from `rule-case-protocol`, the agent closes a line of `raw/<date>/<hi HHMM>/frontier.md` in a reply that carries no ratification and no defer. Examples are an `A` line closed by the person's answer, a `W` line closed by a reading, a `C` line that needs no decision, or an item closed `[-] … · sprint · defer` or `[-] … · backlog · kept`.

> **then:**
> The reply ends with the heading `## Frontier` and the lines of `raw/<date>/<hi HHMM>/frontier.md` as a checklist, in the form that `estimate-case-protocol-acknowledging-reply` sets.
> **＋** In the checklist the closed lines are folded into one line, and the lines put off stand as they are closed.
> **＋** The open `W` lines are folded into one line that lists their ids.
> **＋** Each other open line stands on its own line with a short title.
> **＋** While a line under `## Cases` of `raw/<date>/<hi HHMM>/frontier.md` is open, a question follows the Frontier and ends the reply: which open item is next.
> **＋** When no line under `## Cases` is open, no question follows the Frontier: a reply with no `LEDGER` block calls `/pre-spec` after it, and a reply with a `LEDGER` block ends with the Frontier, for the hook of `rule-prespec-onward` to send the agent on.
> **＋** A reply that closes several lines shows one Frontier, after its `LEDGER` block when it carries one.
> **－** The first reply of `/hi` keeps the form that `rule-skill-hi` sets, the lines it closes included.
> **－** A line closed in Work Mode or at Retro shows no Frontier.
> **－** The reply that acknowledges a ratification and the reply that carries a defer keep their own form, as `estimate-case-protocol-acknowledging-reply` sets it.

```then
update:
- slug: estimate-case-protocol-shows-the-frontier-after-a-closed-line
  set:
    status: pending
  change: the Criterion replaced whole — the open W lines are folded into one line that lists their ids; each other open line stands on its own line (case 578.1)
```

```tasks
- [x] update `estimate-case-protocol-shows-the-frontier-after-a-closed-line`
- [x] read `estimate-case-protocol-shows-the-frontier-after-a-closed-line` — by hand, in a later session after the render, the first Plan Mode reply after the first reply of `/hi` that closes a line of `frontier.md` with no ratification and no defer
```

### Case 578.2 — The acknowledging reply folds the open Work lines

> **given:**
> `rule-case-protocol` — the Case schema, whose Render sets the reply that acknowledges a ratification
> **＋** `vault/wiki/case-schema.md` — the file rendered from that Render
> **＋** `estimate-case-protocol-acknowledging-reply` — the promise whose Criterion this sub-case replaces
> **＋** `raw/<date>/<hi HHMM>/frontier.md` — the Frontier of the session
> **＋** `rule-ledger-write` — the ledger hook that writes the `LEDGER` block
> **＋** `rule-prespec-onward` — the hook that sends the agent on when no line under `## Cases` is open

> **when:**
> The person ratifies a Case, or ratifies again a Case shown again after its ratification, and the agent writes the reply that acknowledges it, with `vault/wiki/case-schema.md` rendered from `rule-case-protocol`.

> **then:**
> The reply has four parts, in this order. First, the `LEDGER` block. Second, the heading `## Case N — ratified` and a paragraph `Changes:` that says what changes, in one or two sentences. Third, a paragraph `Notes:` with facts that did not enter the Case, left out when there are none. Last, the heading `## Frontier` and the lines of `raw/<date>/<hi HHMM>/frontier.md` as a checklist.
> **＋** In the checklist the closed lines are folded into one line, and the lines put off stand as `[-] … · sprint · defer`, `[-] … · backlog · kept` or `[-] … · defer case N`.
> **＋** The open `W` lines are folded into one line that lists their ids, and each other open line stands on its own line with a short title.
> **＋** While a line under `## Cases` is open, the question which item is next ends the reply; when none is open, the reply ends with the Frontier and asks nothing, and the hook of `rule-prespec-onward` sends the agent on.
> **＋** For a Case with sub-cases, one reply acknowledges every sub-case ratified: one `LEDGER` block with all their lines, one heading `## Case N — ratified` that names the ids, one Frontier.
> **＋** The reply that acknowledges a re-ratification carries the `LEDGER` block with the decision lines of each Case ratified again, as at its first ratification.
> **＋** The headings and labels are in the language of the chat.
> **＋** No tool call follows the `LEDGER` block in the same reply.
> **－** The ledger hook of `rule-ledger-write` does not append a repeated decision line a second time.
> **－** When a `Stop` hook other than the ledger hook of `rule-ledger-write` refuses the reply with exit 2, the agent's answer to the refusal is a reply of its own and may call tools. The `LEDGER` block stands written.

```then
update:
- slug: rule-case-protocol
  replace:
  - old: the closed lines folded into one, the open ones one per line with a short title,
    new: the closed lines folded into one, the open `W` lines folded into one line that lists their ids, the other open ones one per line with a short title (case 578.2),
  change: a later Frontier folds the open W lines into one line that lists their ids; the other open lines stand one per line (case 578.2)
- slug: estimate-case-protocol-acknowledging-reply
  set:
    status: pending
  change: the Criterion replaced whole — the open W lines are folded into one line that lists their ids; each other open line stands on its own line (case 578.2)
```

```tasks
- [x] update `rule-case-protocol` — the acknowledging reply folds the open `W` lines into one line of their ids
- [x] update `estimate-case-protocol-acknowledging-reply`
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
- [x] read `estimate-case-protocol-acknowledging-reply` — by hand, the first acknowledging reply of a later session after the render
```

## Case 579 — The main agent names the related Cases of the session, and case-guppi checks them and the replaced Estimate's purpose

> **context:**
> Before it answers, `case-guppi` checks its finished Case. It looks for the pages the change makes false and for the rules that act at the moment the change sets. For the second part it searches `vault/wiki/rules/` and `.claude/`. `estimate-case-build-checks-the-finished-case` measures this check by what `ask-guppi` still finds at `/pre-spec`. The reading of session 2356, ledger line 44, failed with three misses over Cases 561 and 562, which were built after the render that carried case 557.1.
>
> In the first miss, 561.13 changed the shape of the main agent's own questions and missed `rule-skill-hi` and `estimate-hi-takes-its-readings`, which set the question about an open reading at `/hi`. That miss happened under the current text. The handoff of session 2356 puts it down to the size of Case 561, which the backlog page `rule-case-rebuild-cost` holds. In the second miss, 561.3 replaced the Criterion of `estimate-prespec-hook-gates` but left its `purpose` stating the old promise. The rule never names the `purpose` and `method` fields of a replaced Estimate. In the third miss, Case 562 added an end-of-reply check that refused the gathered list of the loop that 561.1 and 561.2 had set earlier in the same session. That loop stood only in the Cases of the session, which are not in `vault/wiki/rules/` or `.claude/` until the librarian's run. Case 571 put the item off.
>
> The person decided that `case-guppi` does not search the Cases of the session. The main agent knows them, so it names each related Case in its prompt to `case-guppi`. That is a Case of the session, ratified or already shown, that changes a page the item names or sets what happens at the same moment. The prompt gives its id, one sentence on what it sets and which pages it changes, and the path of its case file. `case-guppi` reads only the case files the prompt names. The person also decided that, when `case-guppi` replaces an Estimate's Criterion, it rewrites that Estimate's `purpose` and `method` where they state the old promise. The dispatch is a promise of its own, so 579.1 changes `rule-case-protocol` and creates `estimate-case-protocol-names-related-cases-in-the-dispatch`. 579.2 changes `rule-case-build` and replaces the Criterion of `estimate-case-build-checks-the-finished-case`, with a new `purpose` and `method`, and carries `{supersedes:case 571}` on that line. An Estimate carries no `deferred_by`, so only the Decision page of 571 is superseded, as with case 560 in session 2356. The dispatch of this Case already named Cases 577 and 578. Case 578 changes `rule-case-protocol` in the acknowledging-reply paragraph of its Render. The pair of 579.1 stands in the paragraph on who builds a Case, in the same Render section, and the two anchors do not overlap. Case 577 touches neither page nor moment.
>
> The check of the answer noted that six lines of the old Criterion are not carried word for word, and that one `then` line of 579.2 shares most of its words with the `then` of 579.1. Both are on purpose:
> - The old Criterion had seven `＋` lines, and this Case adds two. To stay within seven `＋` lines, the line on a chosen option that cannot hold joins the line on the chosen options. The line on a fact that no slug marks joins the line on the slug search. The part of the hit line on a claim of `context` moves into the line on a claim about a search. Each old promise stands, in the merged line.
> - The shared words describe one thing from two sides: 579.1 says what the main agent puts in its prompt, and 579.2 says what `case-guppi` does with it. Each Criterion reads without the other.
>
> Frame. A Grep of `dispatches it with|the Case id, the Frontier item` over the repository outside `vault/raw/` and `vault/archive/` printed five files: `.claude/agents/case-guppi.md`, `vault/wiki/case-schema.md`, `estimate-case-protocol-shows-the-built-case`, `rule-case-protocol` and `rule-case-build`. The two rendered files follow their rules. `estimate-case-protocol-shows-the-built-case` lists what the dispatch carries and does not say it carries nothing else, so its Criterion stays true and stands. The person chose a new Estimate over replacing that wide promise. `estimate-case-build-writes-the-case` words its `when` the same way and stands for the same reason. A Grep of `dispatch\w*[^.]{0,60}case-guppi|case-guppi[^.]{0,60}dispatch` over `vault/wiki/rules/` printed `rule-orchestration`, `rule-case-protocol`, `rule-ask` and `rule-spec-reconcile`. Over `.claude/` it printed no file. `rule-ask` says that `case-guppi` cannot dispatch a subagent. `rule-spec-reconcile` names the title line of the plan, written before the first dispatch. `rule-orchestration` lists the dispatch among what moves to a file of its own in a later session, and the new clause moves with it. All three stay true. A Grep of `SubagentStop` over `vault/wiki/rules/` printed `rule-case-rebuild-cost`, `rule-case-protocol`, `rule-case-check`, `rule-hook-registry` and `rule-spec-reconcile`. Over `.claude/` it printed `.claude/settings.json`. The `set` of 579.2 carries `status`, `purpose` and `method` together, and the scripts foresee that form:
> - `guppi/prespec.py`, lines 906 to 917, reads the `method` under `set` of an Estimate `update`. It judges that `method` by `names_a_form` of `guppi/lint.py`, which accepts the words `by hand`, and the `method` here opens with them.
> - `guppi/generate.py`, lines 793 to 796, writes each key under `set` onto the page.
> - The hook of `rule-case-check` checked the earlier answer of this Case with this same `set`, and none of its notes spoke of it.
>
> Case 568 set `status` and `purpose` alone, so it is a precedent for `purpose` only. The Purpose of `rule-case-build` says that the agent gets an item and the person's words. It stays true and is not reworded. I read the Criteria of the other Estimates of `rule-case-build`: the ones on the plain round, the record of rounds in `recommend`, the old form and what done means. None speaks of the frame check, so each stands. A Glob of `vault/**/estimate-case-protocol-names-*` printed no file, so the slug is free. The `create` carries a `ref`, so no vault query ran. No code reads the prompt or these texts, so no old form is kept. The main agent's own Cases with too many sub-cases are not addressed here. A Case ratified after the dispatch, while `case-guppi` is still in its rounds, is not covered either, because the prompt is the dispatch alone.

> **problem:**
> The check `case-guppi` runs on its finished Case missed a clash with a Case ratified earlier in the same session, because such a Case is not yet in the rule pages it searches. It also missed an Estimate whose `purpose` still stated the promise its replaced Criterion had dropped. The question was how the related Cases of the session reach `case-guppi`, which Cases count as related, whether the `purpose` and `method` of a replaced Estimate are checked, and how each change is measured.

> **recommend:**
> - **Change the rule, or read the Estimate again?**
>   - Recommended: (b) a Case that adds both checks: `case-guppi` reads the case files of the session for a Case at the same moment or on the same pages, and checks the `purpose` and `method` of an Estimate whose Criterion it replaces.
>   - Answer: none of the options. `case-guppi` must not read the Cases of this session. The main agent knows all the Cases, so it is the main agent's task to tell `case-guppi` that a related Case already exists.
> - **What the main agent writes about a related Case**
>   - Recommended: (a) the id, one sentence on what it sets and which pages it changes, and the path of its case file; `case-guppi` reads that file and no other Case of the session.
>   - Answer: (a).
> - **Which Cases count as related**
>   - Recommended: (a) each Case of the session, ratified or already shown, that changes a page the item names or sets what happens at the same moment.
>   - Answer: (a).
> - **The `purpose` and `method` lines of a replaced Estimate**
>   - Recommended: (a) keep this check: when `case-guppi` replaces a Criterion, it rewrites in the same Case each of those lines that states the old promise.
>   - Answer: (a).
> - **How the change is checked**
>   - Recommended: (a) two sub-cases: a new Estimate on `rule-case-protocol` for the dispatch, and the Criterion of `estimate-case-build-checks-the-finished-case` replaced; both read in a later session after the render.
>   - Answer: (a).

### Case 579.1 — The main agent names the related Cases of the session in its prompt to case-guppi

> **given:**
> `rule-case-protocol` — the Case schema, whose paragraph on who builds a Case sets what the main agent's prompt to `case-guppi` holds
> **＋** `vault/wiki/case-schema.md` — the file rendered from that Render, loaded by `/hi`
> **＋** `estimate-case-protocol-names-related-cases-in-the-dispatch` — the promise this sub-case creates
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md` — the case file of a Case of the session, written by the hook of `rule-case-check`
> **＋** `estimate-case-protocol-shows-the-built-case` — the promise of the dispatch and the showing, whose Criterion stands
> **＋** `raw/2026-10-01/1441/cases/case-578.md` — Case 578, which changes another paragraph of the same Render in this session

> **when:**
> The main agent dispatches `case-guppi` by an `Agent` call to build the Case of a Frontier item, with `vault/wiki/case-schema.md` rendered from `rule-case-protocol`.

> **then:**
> The prompt of the call names each Case of the session, ratified or already shown, that changes a page the item names or sets what happens at the same moment as the item: the same kind of reply, the same hook event or the same command.
> **＋** Each such Case stands in the prompt by its id, one sentence on what it sets and which pages it changes, and the path of its case file `raw/<date>/<hi HHMM>/cases/case-<N>.md`.
> **＋** The main agent judges which Cases of the session are related, and the prompt does not send `case-guppi` to search the Cases of the session.
> **－** A Case of the session that changes no page the item names and acts at another moment need not stand in the prompt.
> **－** When no Case of the session is related, the prompt names none and holds the Case id, the Frontier item with its source and the person's words.

```then
create:
- slug: estimate-case-protocol-names-related-cases-in-the-dispatch
  ref: rule-case-protocol
  kind: QA
  purpose: Whether the main agent's prompt to case-guppi names each Case of the session that changes a page the item names or acts at the same moment, by its id, one sentence on what it sets and the path of its case file
  method: by hand at the close of a later session after the render, each Agent call to case-guppi in the transcript read against the Cases ratified or shown before it; a related Case not named, and a named Case without its sentence or its case file, counted in the reading line
  tags:
  - session
  - workflow
update:
- slug: rule-case-protocol
  replace:
  - old: and the person's words on it — in the prompt of the call, not in the chat — and creates the plan file
    new: and the person's words on it, and each Case of the session, ratified or already shown, that changes a page the item names or sets what happens at the same moment, such as a reply, a hook event or a command, by its id, one sentence on what it sets and which pages it changes, and the path of its case file `raw/<date>/<hi HHMM>/cases/case-<N>.md`, the main agent judging which Cases are related and `case-guppi` reading no other Case of the session (case 579.1) — in the prompt of the call, not in the chat — and creates the plan file
  change: the main agent names in its prompt to case-guppi each Case of the session that changes a page the item names or acts at the same moment, with its id, a sentence and its case file (case 579.1)
```

```tasks
- [x] update `rule-case-protocol` — the main agent names the related Cases of the session in its prompt to `case-guppi`
- [x] create `estimate-case-protocol-names-related-cases-in-the-dispatch`
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
- [x] read `estimate-case-protocol-names-related-cases-in-the-dispatch` — by hand at the close of a later session after the render
```

### Case 579.2 — case-guppi checks the named Cases of the session and the purpose of a replaced Estimate

> **given:**
> `rule-case-build` — the rule of `case-guppi`, whose Render sets what its prompt holds and how it checks its finished Case
> **＋** `.claude/agents/case-guppi.md` — the agent file rendered from that Render
> **＋** `estimate-case-build-checks-the-finished-case` — the promise whose Criterion, `purpose` and `method` this sub-case replaces
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md` — the case file of a Case of the session that the prompt names
> **＋** `rule-case-protocol` — the schema, which sets that the main agent names the related Cases in the prompt (579.1)
> **＋** `.claude/agents/ask-guppi.md` — the recipe whose index lines it reads for a fact that no slug marks
> **＋** `vault/wiki/rules/` and `.claude/` — where it searches for a rule acting at the same moment

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, has built a Case and is about to answer with it.

> **then:**
> It puts each option the person chose in its rounds, or the person's own words where they answered outside the options, beside the `then` and `recommend` of the Case, and the Case holds each one; where the frame shows after a round that a chosen option cannot hold as written, its answer is a round on that point, not a Case with another behaviour.
> **＋** For each page whose text the change makes false, it searches the live pages of the vault, leaving out the Decision pages, and the code, for the page's slug, and reads each hit that `given` does not name around the line of the hit; for a fact that no slug marks, it reads the index lines of the recipe of `.claude/agents/ask-guppi.md` and judges them by meaning.
> **＋** When the change sets what happens at a moment — a reply, a hook event, a command — it searches `vault/wiki/rules/` and `.claude/` for the words that name that moment, reads each passage of each hit that sets a form or a behaviour at that moment, and the Case either does not cover that moment or names the other rule in `given`.
> **＋** It reads the case file `raw/<date>/<hi HHMM>/cases/case-<N>.md` of each Case of the session that the prompt of its call names, and no other Case of the session; where that Case changes a page the Case changes or sets what happens at the same moment, the Case does not cover that moment or names the case file in `given`, and its new text of that page does not contradict the text of that Case.
> **＋** When the Case replaces the Criterion of an Estimate, it reads the `purpose` and `method` of that Estimate, and the same `update` sets anew each one that states the old promise.
> **＋** Each hit that the change makes false enters the Case, or its `context` says why it stands.
> **＋** A claim of `context` about a text names the search it rests on: its pattern, the paths it ran over, and each file the search printed, a file it does not read included, or the count it printed; it claims nothing the search did not print.
> **＋** It reads side by side the finished new texts of all its sub-cases that change one page, and the Case holds no contradiction between them.
> **－** A hit in a History line, in `log.md` or in `brief.md` is not read.

```then
update:
- slug: rule-case-build
  replace:
  - old: The caller's prompt holds the Case id, the Frontier item with its source, and the person's words that bear on it;
    new: The caller's prompt holds the Case id, the Frontier item with its source, the person's words that bear on it, and each Case of the session that the main agent judges related to the item, by its id, one sentence on what it sets and the path of its case file (case 579.2);
  - old: bound the Case so that it does not cover that moment, or name the other rule in `given` (case 557.1).
    new: 'bound the Case so that it does not cover that moment, or name the other rule in `given` (case 557.1). Read the case file of each Case of the session that the caller''s prompt names, and no other Case of the session: where it changes a page your Case changes or sets what happens at the same moment, bound your Case so that it does not cover that moment, or name its case file in `given`, and read your new text of that page beside its text and fix a contradiction between them (case 579.2). When your Case replaces the Criterion of an Estimate, read the `purpose` and `method` of that Estimate, and set anew in the same `update` each one that states the old promise (case 579.2).'
  change: case-guppi reads the case file of each related Case of the session that its prompt names, and sets anew the purpose and method of an Estimate whose Criterion it replaces where they state the old promise (case 579.2)
- slug: estimate-case-build-checks-the-finished-case
  set:
    status: pending
    purpose: Whether case-guppi checks its finished Case before it answers — the chosen options, the pages that name a slug the change makes false, the rules that act at the moment the change sets, the Cases of the session its prompt names, the purpose and method of an Estimate whose Criterion it replaces, what each search printed, the sub-cases that change one page — counted by what ask-guppi still finds at pre-spec
    method: 'by hand: at /pre-spec of a later session after the render, the report of ask-guppi read for each Case case-guppi built — a Case that departs from a chosen option, a page naming a changed slug that the Case misses, a rule acting at the same moment that the Case misses, a Case of the session named in the prompt whose page or moment the Case clashes with, an Estimate whose purpose or method still states the promise its replaced Criterion dropped, a claim of context that its search did not print, two sub-cases whose texts on one page contradict; the count of each in the reading line'
  change: the Criterion replaced whole — the case files of the related Cases the prompt names, and the purpose and method of an Estimate whose Criterion is replaced; the defer of case 571 retired (case 579.2)
```

```tasks
- [x] update `rule-case-build` — `case-guppi` reads the case files of the related Cases its prompt names, and the `purpose` and `method` of an Estimate whose Criterion it replaces
- [x] update `estimate-case-build-checks-the-finished-case`
- [x] `uv run guppi render`: `.claude/agents/case-guppi.md`
- [x] read `estimate-case-build-checks-the-finished-case` — by hand at `/pre-spec` of a later session after the render, the report of ask-guppi read for each Case
```

## Case 581 — While answers of case-guppi are out after pre-spec, the main agent ends each waiting turn with one labelled line

> **context:**
> This Case is Case 580 built again under a new id, its content unchanged. Case 580 was first ratified with no sub-cases, then ratified again as 580.1 and 580.2. The plan file kept the old body of 580 beside the two sub-cases. So `guppi prespec --check` found the `replace` of `rule-prespec` and the Criterion of `estimate-prespec-gathers-the-answers-after-findings` signed twice. Per `rule-spec-write`, a decision line that carries `{supersedes:case N}` removes the section of Case N, with its sub-cases, from the plan file and from `spec.md`. So 581.1 carries `{supersedes:case 580}` and `{supersedes:case 580.1}`, and 581.2 carries `{supersedes:case 580.2}`. Each Case superseded has its own block, which retires all three sets of ledger lines. The Frontier line that Case 580 closed is closed again by this Case.
>
> After `/pre-spec` reports findings, the main agent sends each fix to the `case-guppi` that built the Case. It waits until every answer is back, then shows the person one gathered list. Step 2 of the loop in `rule-prespec`, rendered into `.claude/skills/pre-spec/SKILL.md`, forbids any text in the chat while an answer is still out. An answer to `SendMessage` does not come back inside the turn, though. It arrives later as a notice, and that notice opens a turn of its own, as `lesson-sendmessage-answers-open-a-turn-of-their-own` records. Every turn ends with a reply. So the reading of `estimate-prespec-gathers-the-answers-after-findings` in session 1237, ledger line 37, failed: the main agent wrote in the chat twice while answers were out. Once was at the end of the turn that sent the fixes. The other was in the turn opened by the answer for 567, while the answer for 569 was still out. The handoff of that session asked whether the clause should allow one short line per such turn.
>
> The person chose three things. First, one short line closes each turn that sends to a `case-guppi` and each turn an answer opens while another answer is still out. The line names the Cases that have answered and the Cases still out, and holds nothing of an answer and no question. Second, the line opens with a fixed bold label that ends in a colon. Third, only the loop after the findings changes. The label matters because of `uv run guppi casecheck` on `Stop`. After `/pre-spec`, when the turn brought back a round of questions, it refuses a reply whose first line opens neither with `❓ ` nor with a bold label that ends in a colon. The pattern `LABEL_LINE` in `guppi/casecheck.py` accepts any such label. So if one answer brings a round while another answer is still out, a plain waiting line would be refused, and the labelled line passes with no change to the logic of the check. Session 1237 brought back no round in the loop, so this was not seen live.
>
> `/pre-spec` then found that the same check states a false reason for its exemption after `/pre-spec`. It says that the loop after the findings runs in one turn. This Case puts the opposite into the skill. The reason stands in three places:
> - the passage of `rule-case-check` on how a round opens
> - the module docstring of `guppi/casecheck.py` and the docstring of its function `round_opening`
> - the `－` line on the exemption after `/pre-spec` in the Criterion of `estimate-case-check-refuses-text-before-a-round`
>
> The person chose to correct the reason in all three with the behaviour unchanged. That is 581.2. A promise changes only whole, so 581.2 replaces that Criterion whole and sets the Estimate `pending`. Its `purpose` and `method` do not state the reason, so they stand. The change to `guppi/casecheck.py` is to its docstrings only, so the person's choice of no code change still holds for the logic. 581.1 changes `rule-prespec` and replaces the Criterion of `estimate-prespec-gathers-the-answers-after-findings` whole. 581.1 also sets a new `purpose`, because the old one says the agent stays quiet, and a new `method`, so that the reading looks for refusals of `guppi casecheck` in the loop.
>
> The check of the answer noted lines of the old Criteria that are not carried word for word. All of these changes are on purpose:
> - The `when` of 581.1 now also names `.claude/skills/pre-spec/SKILL.md`, rendered from `rule-prespec`. The trigger is the same.
> - In 581.1, the line that the agent writes nothing in the chat while an answer is out is the promise this Case changes. It becomes the two lines on the labelled waiting line and on what that line may hold. Its clause that no answer of one `case-guppi` is passed on alone is kept.
> - In 581.2, only the `－` line on the exemption after `/pre-spec` changes: its reason. Every other line is carried word for word.
>
> Frame. These searches back the claims above:
> - A Grep of `(?i)notification|while an answer|answers? (is|are) (still )?out|write nothing in the chat` over `vault/wiki/`, leaving out `decisions/`, printed `rule-prespec`, `brief.md`, `lesson-sendmessage-answers-open-a-turn-of-their-own` and `estimate-prespec-gathers-the-answers-after-findings`. The `brief.md` hit is not read.
> - A Grep of `(?i)notification|while an answer|write nothing in the chat` over `.claude/` printed only `.claude/skills/pre-spec/SKILL.md`, which the render rewrites.
> - A Grep of `SendMessage` over `vault/wiki/rules/` printed `rule-case-protocol`, `rule-case-check`, `rule-case-build`, `rule-prespec` and `rule-skill-wait-what`. The same Grep over `.claude/` printed `.claude/agents/case-guppi.md`, `.claude/skills/wait-what/SKILL.md` and `.claude/skills/pre-spec/SKILL.md`.
> - A Grep of `(?i)runs in one turn|in one turn` over the repository, leaving out `vault/raw/` and `vault/archive/`, printed these files:
>   - `vault/wiki/where-to-stop.md`
>   - `.claude/skills/work/SKILL.md`
>   - `guppi/casecheck.py`
>   - `rule-case-check`
>   - `log.md`
>   - `rule-work-mode`
>   - `rule-where-to-stop`
>   - `estimate-case-check-refuses-text-before-a-round`
>   - `estimate-work-mode-takes-the-work-readings`
>   - `decision-case-562`
> - A Grep of `(?i)in the chat|SendMessage|loop` over the Estimates `estimate-prespec-*` printed three files: the target, `estimate-prespec-reconciles` and `estimate-prespec-notes-a-long-chain`.
>
> What the hits mean:
> - Of the `SendMessage` hits, the `rule-case-protocol` passage on who builds a Case sets what goes by `SendMessage`, not what the agent writes while it waits. `rule-skill-wait-what` uses `SendMessage` to ask for a fact. `rule-case-build` and its render describe how `case-guppi` is asked again. None of them sets a form for the waiting reply. The `rule-case-check` hit is the passage that 581.2 corrects.
> - Of the one-turn hits, the Work Mode files speak of the run from `/work` to the handoff, another moment. `log.md` is not read, and the Decision page is history.
> - Of the Estimates, `estimate-prespec-reconciles` speaks of sending a finding to its `case-guppi`, and `estimate-prespec-notes-a-long-chain` speaks of a one-line answer to a `note:` line. Neither speaks of what is written while an answer is out, so both stand.
> - `case-schema.md` says the Cases built again in the loop go out together and come back together. That stays true.
>
> The comparison of `guppi casecheck` judges only a reply that shows a Case heading, and the waiting line shows none. That reply also carries no `LEDGER` block, so the hooks that Case 577 changes do not act on it. Case 579 sets the dispatch prompt, which this Case does not touch.
>
> No code reads the changed texts, so no old form is kept. Not done here: waits on a `case-guppi` outside this loop, where no rule sets anything. `insight-prespec-after-findings-loop-unruled` stays open.

> **problem:**
> The loop after the findings of `/pre-spec` forbids any text in the chat while an answer of a `case-guppi` is out. But each answer opens a turn of its own, and each turn ends with a reply, so the clause cannot hold and its Estimate failed. The question was what the main agent may write in those turns, how that line gets past the end-of-reply check when an answer brings a round, whether the same allowance covers waits outside the loop, and what to do with the check's stated reason that the loop runs in one turn.

> **recommend:**
> - **What the main agent may write while it waits**
>   - Recommended: (a) one short line in each waiting turn: the turn that sends the fixes and each turn opened by an answer while another is still out end with one line that names the Cases that have answered and those still out, and nothing of what an answer says, and no question.
>   - Answer: (a).
> - **How the waiting line gets past the end-of-reply check**
>   - Recommended: (a) the line opens with a fixed bold label such as `**Waiting:**`, which the check accepts as it stands, with no code change.
>   - Answer: (a).
> - **Waits outside the loop after the findings**
>   - Recommended: (a) only the loop after the findings: only step 2 of `/pre-spec` changes, and waits in ordinary Plan Mode stay as they are.
>   - Answer: (a).
> - **The check's stated reason that the loop runs in one turn**
>   - Recommended: (a) correct the reason everywhere, behaviour unchanged: a second part of the Case rewrites the reason on `rule-case-check` and in the docstrings of `guppi/casecheck.py`, and replaces the promise of the check whole with the same behaviour and the true reason, read again in a later session.
>   - Answer: (a).

### Case 581.1 — The main agent ends each waiting turn of the loop with one labelled line

> **given:**
> `rule-prespec` — the rule of `/pre-spec`, whose Render sets the loop after the findings
> **＋** `.claude/skills/pre-spec/SKILL.md` — the skill rendered from that Render
> **＋** `estimate-prespec-gathers-the-answers-after-findings` — the promise of the loop, whose Criterion, `purpose` and `method` this sub-case replaces
> **＋** `.claude/skills/grill-me/SKILL.md` — the question shape of the gathered list
> **＋** `guppi/casecheck.py` — the `Stop` check that judges the first line of a reply whose turn brought back a round
> **＋** `lesson-sendmessage-answers-open-a-turn-of-their-own` — the fact that each answer to `SendMessage` opens a turn of its own

> **when:**
> `/pre-spec` has reported findings in Cases of the plan, and the main agent sends them to the `case-guppi` of those Cases, with `.claude/skills/pre-spec/SKILL.md` rendered from `rule-prespec`.

> **then:**
> The main agent sends each finding in a Case that needs no word of the person to the `case-guppi` of that Case by `SendMessage`, all of them in one message, and holds back a finding whose fix waits for the person's answer.
> **＋** It ends each turn that sends to a `case-guppi`, and each turn that an answer opens while another answer it sent is still out, with one line that opens with a bold label ending in a colon and names the Cases that have answered and the Cases still out.
> **＋** That line holds nothing of what an answer says and no question, and the main agent writes nothing else in the chat while an answer is out and passes on no answer of one `case-guppi` alone.
> **＋** It then shows the person one list of what to answer: its own questions still open and every round that came back, each question in the shape of `.claude/skills/grill-me/SKILL.md` and numbered `<Case id>.Q<n>` by the Case it belongs to.
> **＋** It sends each answer, with each finding held back for it, to the `case-guppi` of its Case in one message, and repeats the wait and the list until every `case-guppi` it sent has answered with its Case.
> **＋** It then shows every Case built again in one reply, for one ratification.
> **－** When an answer brings back a round while another answer is still out, the round is not shown in that turn, and `uv run guppi casecheck` does not refuse the reply that opens with the labelled line.
> **－** Outside this loop no Case is taken up before the current one is ratified or deferred.
> **－** A question that no answer settles stays in the next list under its number.

```then
update:
- slug: rule-prespec
  replace:
  - old: 2. Wait for every `case-guppi` you sent to answer. Write nothing in the chat while an answer is still out, and pass on no answer of one `case-guppi` alone.
    new: '2. Wait for every `case-guppi` you sent to answer, and pass on no answer of one `case-guppi` alone. An answer to `SendMessage` comes back as a notice that opens a turn of its own, and each turn ends with a reply: end each turn that sends to a `case-guppi`, and each turn that an answer opens while another answer is still out, with one line that opens with a bold label ending in a colon — `**Waiting:**`, translated — and names the Cases that have answered and the Cases still out. Write nothing else in the chat while an answer is out: nothing of what an answer says, and no question; a round that came back waits for the list of step 3, and the label lets the reply pass the check of `rule-case-check` (case 581.1).'
  change: 'step 2 of the loop after the findings: each waiting turn ends with one line under a bold label naming the Cases answered and still out, and nothing else is written (case 581.1)'
- slug: estimate-prespec-gathers-the-answers-after-findings
  set:
    status: pending
    purpose: Whether after the findings of pre-spec the main agent sends the fixes to their case-guppi at once, ends each waiting turn with one labelled line naming the Cases answered and still out and writes nothing else while answers are out, gathers every question into one numbered list, and shows the Cases built again in one reply
    method: by hand at the /pre-spec of a later session after the render whose report sends findings to two or more case-guppi, the replies between the report and the showing again, the SendMessage calls and any refusal of guppi casecheck read in the transcript
  change: the Criterion replaced whole — one labelled line per waiting turn instead of no text while answers are out (case 581.1)
```

```tasks
- [x] update `rule-prespec` — step 2 of the loop allows one labelled line per waiting turn
- [x] update `estimate-prespec-gathers-the-answers-after-findings`
- [x] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
- [x] read `estimate-prespec-gathers-the-answers-after-findings` — by hand at the `/pre-spec` of a later session after the render whose report sends findings to two or more `case-guppi`
```

### Case 581.2 — The Case check states the true reason for its exemption after pre-spec

> **given:**
> `rule-case-check` — the rule of the Case check, whose passage on how a round opens gives the reason for the exemption after `/pre-spec`
> **＋** `guppi/casecheck.py` — the check, whose module docstring and the docstring of `round_opening` give the same reason
> **＋** `tests/test_casecheck.py` — the tests of how a round opens, unchanged and run again
> **＋** `estimate-case-check-refuses-text-before-a-round` — the promise of the check, whose Criterion this sub-case replaces
> **＋** `rule-prespec` — the loop after the findings, where each answer of a `case-guppi` comes back in a turn of its own
> **＋** `.claude/skills/grill-me/SKILL.md` — the question line that marks a round
> **＋** `/hi` — the command that opens the session and writes its `hi` line in the event log
> **＋** `.claude/skills/wait-what/SKILL.md` — the re-pitch, a turn the check does not judge

> **when:**
> `Stop` fires after a reply of the main agent, and `uv run guppi casecheck` runs on it.

> **then:**
> When the turn of the reply, the records after the person's last prompt, holds a round of `case-guppi`, `uv run guppi casecheck` judges how the reply opens. A round is a text that `case-guppi` gives back to an `Agent` or `SendMessage` call and that holds a question line `❓ **Q<n>** - **<title>**:` of `.claude/skills/grill-me/SKILL.md`, no Case heading and no first line `**Fact:**`.
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
- slug: rule-case-check
  replace:
  - old: after `/pre-spec` that text is not judged, since the loop after its findings runs in one turn.
    new: after `/pre-spec` that text is not judged, since in the loop after its findings each answer of a `case-guppi` comes back in a turn of its own and the text the main agent writes there is set by `rule-prespec` (case 581.2).
  change: 'the reason for the exemption after /pre-spec: each answer of the loop comes back in a turn of its own, and rule-prespec sets the text written there (case 581.2)'
- slug: estimate-case-check-refuses-text-before-a-round
  set:
    status: pending
  change: the Criterion replaced whole — the same behaviour, with the true reason for the exemption after /pre-spec (case 581.2)
```

```tasks
- [x] update `rule-case-check` — the reason for the exemption after `/pre-spec` no longer says the loop runs in one turn
- [x] update `estimate-case-check-refuses-text-before-a-round`
- [x] `guppi/casecheck.py` — reword the reason in the module docstring and in the docstring of `round_opening` as the new text of `rule-case-check` gives it; no line of logic changes
- [x] `uv run pytest tests/test_casecheck.py -k round` — passes unchanged
- [ ] read `estimate-case-check-refuses-text-before-a-round` — `uv run pytest tests/test_casecheck.py -k round` and by hand in a later session, the first rounds of `case-guppi` shown before and after `/pre-spec`
```
