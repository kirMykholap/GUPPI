<!-- approved 13:49:16 · session 07a95bd2 -->

# Spec — 2026-09-14, session O (hi 12:29)

## Case 133 — the `deferred_by` line of `insights/schema.yaml`

> **context:**
> Case 124.3 added a `deferred_by` row to `insights/schema.md` (no; a list of decision slugs; the `defer` decisions that postponed the Insight, set by `generate`, cleared by a `supersedes`). Lint requires `schema.md` and `schema.yaml` to agree, so Work Mode of session N added `deferred_by` to `optional` of `schema.yaml` with a two-line comment — commit `a5dc64e`, outside every `then` block. The brief raised it as a Flag: ratify or revert.

> **problem:**
> The line lives in a Rule-class file and nobody signed it. A revert breaks lint and `generate` (124.2 writes `deferred_by` on an Insight at a `defer`; Case 129 already did). A signature after the fact is the one path on which the chain 124.2 → 124.3 → yaml agrees.

> **given:**
> `vault/wiki/insights/schema.yaml` at HEAD: `optional: [addressed_by, deferred_by]` and the comment "`deferred_by`: the `defer` decisions that postponed the Insight; set by `generate`, cleared by a `supersedes` (case 124.2)".
> **＋** `rules/schema.yaml` and `entities/schema.yaml` carry the same line with the same comment, signed by Case 52.3.
> **＋** `guppi lint` today: 74 findings, none on `insights/schema` — md and yaml agree.
> **＋** Slug precedent: `decisions-schema-yaml`, `rules-schema-yaml`, `estimates-schema-yaml` (Cases 31.1, 52.3, 72.2) — here `insights-schema-yaml`.
> **－** `generate` already leans on the line: `decision-case-129` stands in `deferred_by` of two Rule pages, and any future `defer` with an Insight as target writes the field on the Insight.

> **when:**
> Someone reads `vault/wiki/insights/schema.yaml`, or `guppi lint` compares it with `insights/schema.md`.

> **then:**
> `optional` holds `deferred_by`, with the comment below it as in `a5dc64e`; lint gives no finding on the Insight md/yaml pair.
> **＋** The file does not change: the `update` signs the text that already stands at HEAD.
> **－** Rule-class file: no Estimate, applied by hand (here — already applied).
> **－** The Frontier line F3 closes on this Case.

```then
update:
  - slug: insights-schema-yaml
    file: vault/wiki/insights/schema.yaml
    change: "deferred_by in optional, with its comment, as committed in a5dc64e outside a then block; signed after the fact, no edit (case 133)"
```

```tasks
- [x] `vault/wiki/insights/schema.yaml`: confirm the file at HEAD equals the `then` — no edit; `uv run guppi lint` gives no finding on `insights/schema` (133)
```

## Case 134 — `insight-session-vault-knowledge-not-loaded`: actioned

> **context:**
> An Insight of severity 5, `open` since 2026-09-12, five children. Pattern: a fact the vault holds does not reach the session that needs it — only `brief.md`, `CLAUDE.md`, the skills and the agent frames are loaded, and everything else waits for a read the agent must first think to make. The page's Proposal: a second channel beside the brief — the ledger tail at `/hi`, and a way for a Rule page to name the lessons that bear on it; prompt or hook, a Case of its own.

> **problem:**
> The children fall into two groups, and each has a mechanical answer already. The first child (readings after the librarian invisible to the next `/hi`) is closed by `rule-ledger-tail` (101.2, `built`, `estimate-ledger-tail` `passed`; the `Tail:` line of `/hi`). The four heredoc children are closed by `rule-bash-guard` (127): the hook refuses instead of the agent remembering a lesson; the first live refusal today at 12:34. What stays open is the second half of the Proposal — "a Rule page names its lessons". Decide: is the Insight actioned, and what becomes of that half.

> **given:**
> `insight-session-vault-knowledge-not-loaded`: `open`, `severity: 5`, children `lesson-readings-after-librarian-invisible-to-next-hi`, `lesson-vault-lesson-absent-at-the-moment-it-applies`, `lesson-heredoc-trap-hit-twice-with-its-lesson-live`, `lesson-heredoc-trap-hit-a-third-time-in-work-mode`, `lesson-heredoc-trap-hit-a-fourth-time-in-the-session-that-ratified-its-hook`; all `clustered`.
> **＋** `rule-ledger-tail` `built`, `estimate-ledger-tail` `passed`: `/hi` prints the unmaterialized ledger tail — the answer to the first child.
> **＋** `rule-bash-guard` `built`, `estimate-bash-guard` `passed` (the test of 127, the live refusal at 12:34 today) — the answer to the four heredoc children.
> **＋** `insights/schema.md`: `addressed_by` is one decision slug, "the ratified decision that fixed the pattern, or rejected it (case 124)"; `## Addressed by` is derived by `generate` from the field (124.2).
> **＋** The cascade of `generate` (104.2): the children of an actioned Insight go `archived`; `cleanup` moves the five lesson pages to the archive; `severity` is recomputed over the live children.
> **＋** `actioned` is not an end state: a new lesson with the same root cause returns the Insight to `open`, the old children stay archived (schema.md).
> **－** An Insight is not a Leaf: no `contract`, no Estimate; `generate` accepts an `update` of an Insight, not a `create` or `delete` (124.2).
> **－** The first `update` of an Insight under 124: the `then` block carries `set` with `status` and `addressed_by`, and `change` for History.

> **when:**
> `guppi generate` applies the entry; then someone reads the Insight page or the brief.

> **then:**
> `insight-session-vault-knowledge-not-loaded`: `status: actioned`, `addressed_by: decision-case-134`; `## Addressed by` derived from the field; History carries the line `open → actioned`.
> **＋** The five children are `archived` by the cascade and moved by `cleanup`; `severity` recomputed.
> **＋** The Insight leaves the Deferred list of the next brief; it returns when the librarian puts a new lesson into it.
> **－** The half of the Proposal "a Rule page names its lessons" is rejected by this same decision: a list of lessons on a page is one more text the agent must remember to read, the class of channel that failed four times; the channel that worked is lesson → Insight → brief (124.1) → Case (124) → hook (127). No new Rule, no new field.
> **－** The Frontier line F4 closes on this Case.

```then
update:
  - slug: insight-session-vault-knowledge-not-loaded
    set: {status: actioned, addressed_by: decision-case-134}
    change: "actioned: the ledger tail (rule-ledger-tail, 101.2) answers the first child, the bash guard (rule-bash-guard, 127) the four heredoc children; a lessons list on a Rule page rejected — a text to remember is the channel that failed (case 134)"
```

```tasks
- [ ] nothing to code: the librarian's `generate` applies the `update`, the cascade archives the five children, `cleanup` moves them (134)
```

## Case 135 — `insight-ledger-line-written-unchecked`: actioned

> **context:**
> An Insight of severity 4, `open` since 2026-09-12, four children. Pattern: a ledger line is written verbatim and nothing reads it back until `materialize`, so a line that does not parse or does not match the Spec costs a session. The page's Proposal: (a) `guppi pretask --check` already reads the ledger for the `then`-item comparison (59.1) — put every line through `materialize.parse_line` in the same pass; (b) the table of `case-schema.md` should show `decision[case N]`, not `decision[case_id]` (Case 67 deferred it).

> **problem:**
> Both halves of the Proposal were ratified on the day the Insight was created — session I, 2026-09-12: 75.2 (the grammar of the lines at pre-task) and 75.1 (the table of `case-schema.md`, `index.md`, `rule-case-protocol`). The Insight was not updated because an Insight could not be a Decision target then (124 made it one). The other children were closed on the way: 59.1 (every line to its `then` item and back), 72.5 (no nested Estimates any more — the Estimate is derived from a Leaf `create`, pre-task checks `method` and the slug), 122 (`guppi gate` refuses a Skill call while a `then` item has no line — a preview in `ratification` no longer passes for the record). Decide: is the Insight actioned.

> **given:**
> `insight-ledger-line-written-unchecked`: `open`, `severity: 4`, children `lesson-spec-then-items-unchecked-against-ledger-lines`, `lesson-ledger-decision-line-written-without-the-case-word`, `lesson-ledger-preview-in-ratification-taken-for-the-record`, `lesson-pretask-nested-estimate-exempt-from-the-line-check`; all `clustered`.
> **＋** `rule-pretask` `built`, `estimate-pretask-reconciles` `passed`: the `### case 75.2` block — every record line of the window through `materialize.parse_line`, one that does not read is a finding with its date and line number, exit 1; `check_grammar` in `guppi/pretask.py`; the blocks of 59.1 and 72.5 on the same page.
> **＋** `case-schema.md`, the table "What a Case produces": `- decision[case 12][update][rule-x]{ref:rule-x}`; "The id is `case N` — the word and a space … (case 75.1)".
> **＋** `rule-ledger-write` `built`, `estimate-ledger-write-lifts` `passed` with the block of 122: `guppi gate` on `PreToolUse Skill` refuses while a `then` item of the Spec has no decision line.
> **＋** `CLAUDE.md` (Case protocol): a line outside a `LEDGER` fence is a preview, never a record.
> **＋** The cascade of 104.2: the four children go `archived`, `cleanup` moves them; `actioned` is not an end state.
> **－** An Insight is not a Leaf: no `contract`, no Estimate.
> **－** The `Stop` moment stays verbatim: the hook does not validate the grammar — signed so in 75.2, not changed here.

> **when:**
> `guppi generate` applies the entry; then someone reads the Insight page or the brief.

> **then:**
> `insight-ledger-line-written-unchecked`: `status: actioned`, `addressed_by: decision-case-135`; `## Addressed by` derived from the field; History carries `open → actioned`.
> **＋** The four children are `archived` by the cascade and moved by `cleanup`; `severity` recomputed.
> **＋** The Insight leaves the Deferred list of the next brief; it returns with a new lesson of the same cause.
> **－** No new code, no change to `rule-ledger-write` or `rule-pretask`.
> **－** The Frontier line F5 closes on this Case.

```then
update:
  - slug: insight-ledger-line-written-unchecked
    set: {status: actioned, addressed_by: decision-case-135}
    change: "actioned: the Proposal was done by 75.2 (line grammar at pre-task) and 75.1 (the case N form in case-schema.md); the children closed by 59.1, 72.5 and 122 (case 135)"
```

```tasks
- [ ] nothing to code: the librarian's `generate` applies the `update`, the cascade archives the four children, `cleanup` moves them (135)
```

## Case 136 — `insight-ledger-hi-tied-to-its-session-by-position`: session marks by stamp, not by position

> **context:**
> An Insight of severity 3, three children: the `hi` lost at midnight (session H), the `hi` taken by a session started in the same second (M), and the `pretask` line unstamped and bound by position (N). One cause: a mark in the event log without a session id, and a reader that binds it to a session by the `session-start` lines around it. The `hi` half is closed by Case 111: the `UserPromptSubmit` hook writes `<stamp> hi`, the readings 111.1/111.3/111.6 and 125 passed — today `12:29:47 07a95bd2 hi`. What remains: (1) the marks `pretask`, `retro`, `handoff` are still written through a `!` substitution with an empty `CLAUDE_SESSION_ID` — `--------` — and `pretask.window` counts any `pretask` after our `hi`; (2) `ledger.py` keeps the fallback of 111.6 — a `--------` `hi` by position, kept for the sessions opened before the hook; no such session is open, and since 111.4 nothing writes a `--------` `hi`.

> **problem:**
> Close the pattern whole: every mark of a session carries its stamp, and no reader binds by position. Who writes the marks of the three skills, and whether the fallback goes.

> **given:**
> `rule-event-log` (`Leaf`, `hook`, `built`, `estimate-event-log-records` `passed`, `implementation_ref: [guppi/event.py, guppi/cli.py, .claude/settings.json]`): `guppi event <name> [--session ID]` writes the line, the stamp from `--session` or the payload's `session_id`, `--------` with neither.
> **＋** `rule-pretask`, `rule-retro`, `rule-handoff` (`Leaf`, `render`): line 32/33/32 of the Render — `Recorded: !`uv run guppi event <name> --session "${CLAUDE_SESSION_ID:-}"``; the variable is empty there, every mark reads `--------` (event log 08:48:57, 09:23:25, 09:55:47, 11:26:29, 11:55:48, 12:10:50).
> **＋** `rule-pretask` (`built`, `estimate-pretask-reconciles` `passed`): the hook `guppi pretask` on `ExitPlanMode`, `window()` at `guppi/pretask.py:76` — a `hi` of our session, then any `pretask`, a foreign `session-start` resets.
> **＋** `rule-ledger-write` (`built`, `estimate-ledger-write-lifts` `passed`, `implementation_ref` holds `guppi/gate.py`): `hi_moment` by stamp (111.3), `unstamped_hi_moment` — the fallback of 111.6 (`ledger.py:187`); `rule-retro-commit` also points at `gate.py`.
> **＋** `guppi gate` (`PreToolUse Skill`, 122 and `rule-retro-commit`): reads the payload with `session_id` and `tool_input.skill`; on a refusal the skill does not expand, so today its `!` line is not written — a refused call leaves no mark.
> **＋** All three skills come through the Skill tool (event log: `tool Skill: pre-task`, `tool Skill: handoff`; `retro` in session N never reached the call — the skill failed to load).
> **＋** The criteria of `estimate-retro-loads` and `estimate-handoff-dispatches` say "event_log.md carries a retro/handoff line" — still true, the writer is not named.
> **＋** Every session opened before the hook of 111 (dates ≤ 09-13) is closed and archived; `raw/` holds 2026-09-14 only.
> **－** `estimate-retro-loads` is `failed` (109.1) — this Case does not touch its criterion; the reading of 126 is at `/retro`.
> **－** `hi` is not touched: 111 stands.

### Case 136.1 — the marks `pretask`, `retro`, `handoff` are written by `guppi gate`

> **when:**
> The agent calls the Skill tool with `pre-task`, `retro` or `handoff`, and `guppi gate` on `PreToolUse` lets the call through.

> **then:**
> The gate appends one line `- HH:MM:SS <stamp> <mark>` to `raw/<date>/event_log.md` — `pretask`, `retro` or `handoff`, the stamp from the payload's `session_id` — in the form `guppi event` writes; on a refusal there is no line.
> **＋** The Render of `rule-pretask`, `rule-retro`, `rule-handoff` loses its `Recorded:` line; `guppi event <name>` stays as a CLI, the skills do not call it.
> **＋** `rule-event-log`: `implementation_ref` gains `guppi/gate.py`, `tests/test_gate.py`; the paragraph on the marks says who writes them; `contract: changed`; `estimate-event-log-records` gets a `### case 136.1` block, `pending`: the test — a Skill payload `pre-task` → the line `<stamp> pretask`; `handoff` on a dirty tree → refused and no line; the live reading — the `/pre-task` of this session with the stamp `07a95bd2`.
> **＋** `rule-pretask`, `rule-retro`, `rule-handoff`: `contract: same`.
> **－** Other skills (`hi`, `grill-me`) get no mark.
> **－** The Frontier line F12 closes on this sub-case.

```then
update:
  - slug: rule-event-log
    contract: changed
    set: {implementation_ref: [guppi/event.py, guppi/gate.py, guppi/cli.py, tests/test_gate.py, .claude/settings.json]}
    replace:
      - old: "Until case 111.4 the skill's `!` substitution writes a second, unstamped `hi` line, which the ledger hook ignores."
        new: "The marks `pretask`, `retro` and `handoff` are written by `guppi gate` on `PreToolUse Skill` when it lets the call through, one line `- HH:MM:SS <stamp> <mark>` with the stamp from the payload's `session_id`; a refused call leaves no mark. Until case 136.1 the three skills wrote them through a `!` substitution where `CLAUDE_SESSION_ID` is empty, so every mark read `--------` (case 136.1)."
    change: "the marks pretask, retro, handoff written by guppi gate with the session's stamp; the skills' Recorded lines dropped (case 136.1)"
  - slug: rule-pretask
    contract: same
    replace:
      - old: "Recorded: !`uv run guppi event pretask --session \"${CLAUDE_SESSION_ID:-}\"`\n\n"
        new: ""
      - old: "The skill records its own run through a `!` substitution, which is what the pre-task hook looks for, and whoever calls it — the agent through the `Skill` tool or the person — leaves the same line."
        new: "Its run is recorded by `guppi gate` on the `Skill` call, one `pretask` line with the session's stamp, which is what the pre-task hook looks for (case 136.1)."
    change: "the Recorded line dropped; guppi gate writes the stamped pretask mark (case 136.1)"
  - slug: rule-retro
    contract: same
    replace:
      - old: "Recorded: !`uv run guppi event retro --session \"${CLAUDE_SESSION_ID:-}\"`\n\n"
        new: ""
    change: "the Recorded line dropped; guppi gate writes the stamped retro mark (case 136.1)"
  - slug: rule-handoff
    contract: same
    replace:
      - old: "Recorded: !`uv run guppi event handoff --session \"${CLAUDE_SESSION_ID:-}\"`\n\n"
        new: ""
    change: "the Recorded line dropped; guppi gate writes the stamped handoff mark (case 136.1)"
```

```tasks
- [x] `guppi/gate.py`: after its checks pass for a skill in {`pre-task`→`pretask`, `retro`, `handoff`}, append the stamped mark to the day's event log through `guppi.event` (`format_line`, `append`, `log_path`); no mark on a refusal or for any other skill (136.1)
- [x] `tests/test_gate.py`: `pre-task` payload → the line `<stamp> pretask` in the log; `handoff` on a dirty tree → exit 2 and no line; `hi` skill → no line (136.1)
- [ ] `vault/wiki/rules/rule-pretask.md`, `rule-retro.md`, `rule-handoff.md`: the `Recorded:` line removed by `generate` (the `replace` above); then `uv run guppi render` rewrites the three `SKILL.md` and `guppi render --check` exits 0 (136.1)
- [x] read `estimate-event-log-records` block 136.1: the test, then the live `/pre-task` of this session stamped `07a95bd2` — call the Skill tool with `pre-task` once the gate writes marks, before 136.2 is built (`lesson-reader-changed-before-its-writer-closed-the-live-session`: the new writer measured live before the reader drops the old form); at `/retro` note whether the gate fires for a skill with `disable-model-invocation: true` typed by the person — no `retro` mark is a lesson, not a fix (136.1)
```

### Case 136.2 — `pretask.window` by stamp

> **when:**
> The hook `guppi pretask` on `ExitPlanMode` asks whether `/pre-task` ran in this session.

> **then:**
> The window is open when the log holds a `hi` of the session's stamp and a `pretask` of the same stamp after it; a mark of another stamp or `--------` does not count; a foreign `session-start` resets nothing.
> **＋** `rule-pretask-hook` `contract: changed`; `estimate-pretask-hook-gates` gets a `### case 136.2` block, `pending`: the test — a `pretask` of a foreign stamp between our `hi` and `ExitPlanMode` → refused; ours → passes.
> **－** The `--check` pass (grammar, `then` items, frontier) of `rule-pretask` does not change.

```then
update:
  - slug: rule-pretask-hook
    contract: changed
    replace:
      - old: "in a working session with no `pretask`\nline after this session's `hi`, `uv run guppi pretask` exits 2 with the reason, which\nblocks the approval once; `/pre-task` records the line and the next exit passes."
        new: "in a working session with no `pretask`\nline of this session's stamp after its `hi`, `uv run guppi pretask` exits 2 with the reason, which\nblocks the approval once; the `/pre-task` call leaves the stamped line through `guppi gate` and the next exit passes. A `pretask` of another stamp or `--------` does not count, and a foreign `session-start` resets nothing (case 136.2)."
    change: "the ExitPlanMode hook binds the pretask mark by the session's stamp, not by position (case 136.2)"
```

```tasks
- [x] order: build 136.2 only after the live reading of 136.1 shows `<stamp> pretask` in the log — this session's own mark of 13:5x is `--------` and would not open the window (136.2)
- [x] `guppi/pretask.py` `window()`: `hi` and `pretask` of `stamp` only; drop the reset on a foreign `session-start`; update the module docstring (136.2)
- [x] `tests/test_pretask.py`: a foreign-stamped `pretask` after our `hi` → exit 2; an unstamped one → exit 2; ours → exit 0 (136.2)
- [x] read `estimate-pretask-hook-gates` block 136.2 against the test (136.2)
```

### Case 136.3 — the fallback by position removed from `ledger.py`

> **when:**
> The `Stop` hook, `pretask`, `spec`, `gate` or `cleanup` asks whether the session has a `hi`, and where its folder is.

> **then:**
> Only a `hi` of the session's stamp after its first `session-start` opens the window (111.3); with no such line there is no window, the ledger refuses "no /hi recorded", `unstamped_hi_moment` is removed.
> **＋** `rule-ledger-write` `contract: changed`; `estimate-ledger-write-lifts` gets a `### case 136.3` block, `pending`; the test of 111.6 flips: a `--------` `hi` under our start → refused.
> **＋** The `### case 111.6` block leaves the criterion: `{supersedes:case 111.6}`.
> **－** `hi_recorded`, `session_dir`, `ledger_path` — unchanged beyond the removal of the fallback.

```then
update:
  - slug: rule-ledger-write
    contract: changed
    replace:
      - old: "With no stamped `hi` in the logs walked, a `--------` `hi` counts by the rule before 111.3 — after a `session-start` of this session with no other session's start in between — for the sessions the old skill line opened (case 111.6). "
        new: "A `--------` `hi` never counts: the fallback by position of case 111.6 was removed once every session opened before the stamped `hi` had closed (case 136.3). "
    change: "the fallback of 111.6 — an unstamped hi bound by position — removed; a hi of the session's stamp is the one way to open the window (case 136.3)"
```

```tasks
- [x] `guppi/ledger.py`: remove `unstamped_hi_moment` and its call in `hi_moment`; the docstrings say a stamped `hi` is the one opener (136.3)
- [x] `tests/test_ledger.py`: the 111.6 test flips — an unstamped `hi` under our start → the lines refused with "no /hi recorded"; a foreign start between → refused as before (136.3)
- [x] read `estimate-ledger-write-lifts` block 136.3 against the test (136.3)
```

### Case 136.4 — the Insight actioned

> **when:**
> `guppi generate` applies the entry; then someone reads the Insight page or the brief.

> **then:**
> `insight-ledger-hi-tied-to-its-session-by-position`: `status: actioned`, `addressed_by: decision-case-136.4`; the three children `archived` by the cascade, moved by `cleanup`.
> **－** The Frontier line F6 closes on this sub-case.

```then
update:
  - slug: insight-ledger-hi-tied-to-its-session-by-position
    set: {status: actioned, addressed_by: decision-case-136.4}
    change: "actioned: the hi is stamped by 111, the marks pretask/retro/handoff by guppi gate (136.1), pretask.window and the ledger window read by stamp only (136.2, 136.3) (case 136.4)"
```

```tasks
- [ ] nothing to code: the librarian's `generate` applies the `update`, the cascade archives the three children (136.4)
```

## Case 137 — `insight-ledger-hook-reads-only-the-final-text`: actioned

> **context:**
> An Insight of severity 3, four children: blocks in replies that ended in a Skill call and in `ExitPlanMode` (session F); blocks in a text followed by tool calls in the same turn (I); the text before a tool call is absent from the transcript altogether (L); blocks lost in a reply ending in a Skill call with the Insight live (M). Pattern: the ledger writer sees the last text of a turn, not the turn. Proposal: settle whether an intermediate text is in the transcript; if present collect every text of the window, if absent the writer needs a second event beside `Stop`; and count blocks seen against lines written at `/hi`.

> **problem:**
> The Proposal's question is settled by the third child: the text before a tool call is not in the transcript — Claude Code does not keep it. So "collect every text" is impossible, and there is nothing to count "blocks seen" from. A second event beside `Stop` does not help either: no hook sees a reply's text before its end. What was possible was done by Case 122: the rule in `CLAUDE.md` ("A reply that carries a `LEDGER` block ends in that text. No tool call follows it") and `guppi gate` on `PreToolUse Skill`, refusing a skill call while a `then` item of the Spec has no decision line — the very move that lost the lines in F and M. Decide: is the Insight actioned.

> **given:**
> `insight-ledger-hook-reads-only-the-final-text`: `open`, `severity: 3`, children `lesson-ledger-hook-misses-a-reply-ending-in-a-tool-call`, `lesson-ledger-hook-drops-a-block-followed-by-tool-calls-in-the-turn` (`archived`), `lesson-transcript-omits-text-emitted-before-tool-calls`, `lesson-ledger-lines-lost-in-a-reply-ending-in-a-skill-call-with-the-insight-live`.
> **＋** `rule-ledger-write` `built`, `estimate-ledger-write-lifts` `passed` with the block of 122: the gate on `PreToolUse Skill` refuses while a `then` item of the Spec or plan file has no line; 55.2 — every `Stop` reads every `LEDGER` block of the window's transcript, so the final text of any earlier turn is never lost.
> **＋** `rule-case-protocol` → `CLAUDE.md`: "A reply that carries a `LEDGER` block ends in that text. No tool call follows it in the same reply: the text before a tool call is never kept, and the hook reads nothing" (122); `estimate-claude-md-rendered` passed today with that sentence.
> **＋** 122 signed the limits: the gate does not see `estimate`/`lesson` lines, a loss is a Retro finding; `ExitPlanMode` is not gated, `/pre-task` before it is a Skill call.
> **＋** This session: every block was the final text, the ledger of `1229/` holds every line.
> **＋** The cascade of 104.2: the three live children go `archived`; the fourth is archived already.
> **－** An Insight is not a Leaf: no `contract`, no Estimate.
> **－** No live refusal of the gate observed yet (the test of 122 passed); that reading stays with `estimate-ledger-write-lifts`, the Insight does not wait for it — a ratified decision is enough by the schema.

> **when:**
> `guppi generate` applies the entry; then someone reads the Insight page or the brief.

> **then:**
> `insight-ledger-hook-reads-only-the-final-text`: `status: actioned`, `addressed_by: decision-case-137`; `## Addressed by` derived; History carries `open → actioned`.
> **＋** The three live children are `archived` by the cascade, moved by `cleanup`; `severity` recomputed.
> **－** The half of the Proposal "collect every text / a second event / count the blocks" is rejected as impossible: the text is not in the transcript and no hook sees it.
> **－** The Frontier line F7 closes on this Case.

```then
update:
  - slug: insight-ledger-hook-reads-only-the-final-text
    set: {status: actioned, addressed_by: decision-case-137}
    change: "actioned by 122 — the rule that a reply with a LEDGER block ends in that text, and guppi gate on the Skill call; collecting intermediate texts rejected as impossible, the transcript omits them (case 137)"
```

```tasks
- [ ] nothing to code: the librarian's `generate` applies the `update`, the cascade archives the three live children (137)
```

## Case 138 — `insight-workflow-contract-change-leaves-its-derived-text-stale`: actioned

> **context:**
> An Insight of severity 3, three children, all before 2026-09-12: Estimate criteria described the old contract after 15.1 (session A); `CLAUDE.md` was edited by hand as a file item while `rule-case-protocol`, whose Render it was, stayed (I); the live clauses of two Estimates were written against the files before the librarian applied the pages, and the first render broke them (J). Pattern: a derived text has no pointer to its source, and nothing checks the pair. Proposal: at pre-task, for each changed slug the Estimates whose criterion quotes it; for each `file` the Rule whose `governs` names it; a change without its pair is a finding.

> **problem:**
> The path half is done: 59.6 — the `guard` hook refuses a hand edit of a governed file; 59.8 — `CLAUDE.md` is rendered from `rule-claude-md`/`rule-case-protocol`, a file item on it is impossible; pre-task `check_governed` — an `update` with `file:` on a path a live Rule `governs` is a finding. The criterion half is closed differently from the Proposal: since 72.1 the criterion is the Case's `when`/`then`, copied by the scripts as `### case N` blocks; `contract: changed` appends a block and sets `pending` by machine, `{supersedes}` removes the old block; 88.2 took the last stale live clause out of the prose. There is no hand-written criterion text left to go stale. No new child since 09-12 — seven sessions under the new model. Decide: is the Insight actioned.

> **given:**
> `insight-workflow-contract-change-leaves-its-derived-text-stale`: `open`, `severity: 3`, children `lesson-estimates-criterion-stale-after-contract-change`, `lesson-render-governed-file-updated-as-rule-class-file`, `lesson-estimates-live-clause-stale-at-first-render`; all `clustered`, the last of 2026-09-12.
> **＋** `rule-governed-files-hook` (`guard` on `Edit|Write|MultiEdit`, 59.6): a hand edit of a file a Rule governs is refused; `rule-claude-md` (59.8): `CLAUDE.md` is a Render, not a Rule-class file.
> **＋** `rule-pretask` `built`, `estimate-pretask-reconciles` `passed`: `check_governed` — "an `update` item with `file:` on a path a live Rule page `governs`" — a finding (59.6).
> **＋** `case-schema.md`, "`when` and `then` are the criterion" (72.1): the scripts copy `when`/`then` as a `### case N` block; `contract: changed` appends a block and sets `pending`; `{supersedes:case N}` removes a block; "nothing is signed in two wordings".
> **＋** `estimate-claude-md-rendered`: 88.2 — "the stale live clause of case 59.8 leaves the Criterion prose"; passed today.
> **＋** The cascade of 104.2: the three children go `archived`.
> **－** An Insight is not a Leaf: no `contract`, no Estimate.
> **－** The `## Criterion` prose of the older Estimates (before 72.1) stays as context; nothing checks it — and nothing reads by it: readings go by the blocks.

> **when:**
> `guppi generate` applies the entry; then someone reads the Insight page or the brief.

> **then:**
> `insight-workflow-contract-change-leaves-its-derived-text-stale`: `status: actioned`, `addressed_by: decision-case-138`; `## Addressed by` derived; History carries `open → actioned`.
> **＋** The three children are `archived` by the cascade, moved by `cleanup`; `severity` recomputed.
> **－** No pre-task pass over the Estimates that quote a changed slug is built; `rule-pretask` does not change.
> **－** The Frontier line F8 closes on this Case.

```then
update:
  - slug: insight-workflow-contract-change-leaves-its-derived-text-stale
    set: {status: actioned, addressed_by: decision-case-138}
    change: "actioned: the path half by 59.6, 59.8 and pre-task's governed check; the criterion half by the derived criterion blocks of 72.1 and 88.2; no pre-task pass over quoting Estimates (case 138)"
```

```tasks
- [ ] nothing to code: the librarian's `generate` applies the `update`, the cascade archives the three children (138)
```

## Case 139 — `insight-harness-agent-visibility`: one reading instead of two opposing lessons

> **context:**
> An Insight of severity 2, the oldest (2026-09-10), two children with opposite claims: session D rendered `ask-guppi.md` and three calls in a row got "Agent type not found"; session E rendered `librarian-guppi.md` at 10:40 and the Agent tool saw it at 10:52 without a restart. The difference was not measured. Proposal: one reading — render a throwaway agent mid-session, dispatch it at once, record the result and the session state; until then plan as if a rendered agent were unusable in its own session.

> **problem:**
> Four sessions took no reading, because nothing pressed for it: the librarian's render is the last step before its commit, and its frames apply in the next session anyway. But the Insight stands in the brief and two lessons contradict each other. Decide: take the reading now, in this session's Work Mode, and close the Insight — or close it unmeasured.

> **given:**
> `insight-harness-agent-visibility`: `open`, `severity: 2`, children `lesson-agents-loaded-at-session-start` (root cause: agents are read at session start), `lesson-agents-visible-in-session` (root cause: the list is re-read during the session); both `clustered`.
> **＋** `rule-render-harness` (`Leaf`, `check`, `built`, `estimate-render-harness-reproduces` `passed`, `estimate-render-sync-reports`): writes the governed files, `.claude/agents/ask-guppi.md` and `librarian-guppi.md` among them; the page says nothing about when Claude Code reads an agent.
> **＋** `guppi guard` (59.6) refuses only a path a live Rule governs; `.claude/agents/probe-guppi.md` is governed by none — the write passes.
> **＋** The agent list of this session in the system prompt holds `ask-guppi`, `librarian-guppi` and the built-in ones — enumerated at start; whether it is re-read during the session is the question of the reading.
> **＋** The cascade of 104.2: the two children go `archived`; a new lesson reopens the Insight.
> **－** The probe file is a hand-written harness file without a Rule page; the exception is ratified here explicitly: it lives one task, is removed before Retro, and never enters a commit.
> **－** The outcome of the reading is not ratified in advance: the Rule page gets a sentence that holds under any outcome; the outcome goes into the estimate line.

### Case 139.1 — the reading on `rule-render-harness`

> **when:**
> In Work Mode of this session the agent writes `.claude/agents/probe-guppi.md` and at once calls the Agent tool with `probe-guppi`; then replaces the file's body and calls again; then removes the file.

> **then:**
> The estimate line records three facts: the new file — found or "Agent type not found"; the replaced one — the old text, the new text, or not found; the client version and whether a compaction happened between the steps.
> **＋** `rule-render-harness` `contract: changed`; `estimate-render-harness-reproduces` gets a `### case 139.1` block, `pending`; the reading is the probe itself; `passed` once the three facts are recorded, whatever the outcome.
> **＋** The body of `rule-render-harness` (How it works) gains the sentence: "When Claude Code reads an agent file under `.claude/agents/` — at session start or on the call — is the reading of case 139.1 on `estimate-render-harness-reproduces`; the librarian's render is its last step before the commit, and an agent it renders is planned for from the next session (case 139.1)."
> **－** `probe-guppi.md` stays neither in the tree nor in a commit; no Rule page for it.

```then
update:
  - slug: rule-render-harness
    contract: changed
    estimate_slug: estimate-render-harness-reproduces
    replace:
      - old: "The rendered files are committed by the librarian, in its own commit (case 89.2"
        new: "When Claude Code reads an agent file under `.claude/agents/` — at session start or on the call — is the reading of case 139.1 on `estimate-render-harness-reproduces`; the librarian's render is its last step before the commit, and an agent it renders is planned for from the next session (case 139.1). The rendered files are committed by the librarian, in its own commit (case 89.2"
    change: "the moment Claude Code reads an agent file is the reading of case 139.1; a rendered agent is planned for from the next session (case 139.1)"
```

```tasks
- [x] the probe: Write `.claude/agents/probe-guppi.md` (frontmatter `name: probe-guppi`, `description: Probe — reply with one word.`, body "Reply with the single word: probe"); call the Agent tool with `subagent_type: probe-guppi`; record found / not found (139.1)
- [x] replace the body with "Reply with the single word: replaced"; call again; record old text / new text / not found (139.1)
- [x] delete `.claude/agents/probe-guppi.md`; `git status --porcelain` shows nothing under `.claude/agents/` (139.1)
- [x] read `estimate-render-harness-reproduces` block 139.1: the estimate line with the three facts, the client version (`claude --version`) and whether a compaction happened (139.1)
```

### Case 139.2 — the Insight actioned

> **when:**
> `guppi generate` applies the entry; then someone reads the Insight page or the brief.

> **then:**
> `insight-harness-agent-visibility`: `status: actioned`, `addressed_by: decision-case-139.2`; the two children `archived` by the cascade.
> **＋** The outcome of 139.1 lies on the Estimate; if it contradicts one of the lessons, that no longer reopens the Insight — the lessons are archived, the answer is on the Rule page.
> **－** The Frontier line F9 closes on this sub-case.

```then
update:
  - slug: insight-harness-agent-visibility
    set: {status: actioned, addressed_by: decision-case-139.2}
    change: "actioned: one reading on estimate-render-harness-reproduces (139.1) replaces the two opposing lessons; the Rule page names where the answer is (case 139.2)"
```

```tasks
- [ ] nothing to code: the librarian's `generate` applies the `update`, the cascade archives the two children (139.2)
```

## Case 140 — the literal `decision-case-N` on the pages of 130.1 and 130.2

> **context:**
> The shared `context` of Case 130 quotes a line of `rule-page-generation`: "History and log lines end with · [[decision-case-N]] when a decision exists" — without backticks. The librarian carried it onto `decision-case-130.1` and `decision-case-130.2` verbatim; lint sees `[[decision-case-N]]`, no page has that slug — two `ref` findings. Case 130.1 cured the same thing on the pages 112.1–112.6 by hand, with backticks.

> **problem:**
> Remove the two findings and leave the pages what was signed. Through `generate` (an `update` with `replace`, a History line) or by hand, as 130.1 did.

> **given:**
> `decision-case-130.1` (line 15) and `decision-case-130.2` (line 14): the same Context paragraph, in it `"History and log lines end with · [[decision-case-N]] when a decision exists"`; one occurrence per page.
> **＋** `guppi lint`: `ref: body names decision-case-N, which no live or archived page carries` — two of the 74 findings; `CODE_SPAN` (`lint.py:57`) does not count a `[[slug]]` inside backticks as a link.
> **＋** `generate.update` (`generate.py:468`): finds a page of any category, applies `replace` in the body, adds a History line with `change`.
> **＋** Precedent 130.1: the same literal on `decision-case-112.1`–`112.6` wrapped in backticks by hand, the ledger line on `rule-page-generation` `contract: same`.
> **－** `decisions/schema.md`: "a decision is not edited. Only `status` and `superseded_by` ever change" — the edit changes no signed content; the schema is not updated.
> **－** The other 72 findings are not touched: 62 — Slice 5, 10 — F1.

> **when:**
> `guppi generate` applies the two entries; then `guppi lint` reads the pages.

> **then:**
> On both pages the paragraph reads `… end with `· [[decision-case-N]]` when a decision exists …`; the History of each carries the `change` line.
> **＋** `guppi lint`: 72 findings, no `ref`.
> **－** Decision pages are not Leaves: no `contract`, no Estimate.
> **－** The Frontier line F14 closes on this Case.

```then
update:
  - slug: decision-case-130.1
    replace:
      - old: "end with · [[decision-case-N]] when a decision exists"
        new: "end with `· [[decision-case-N]]` when a decision exists"
    change: "the quoted literal decision-case-N wrapped in backticks, a lint ref finding; no content change (case 140)"
  - slug: decision-case-130.2
    replace:
      - old: "end with · [[decision-case-N]] when a decision exists"
        new: "end with `· [[decision-case-N]]` when a decision exists"
    change: "the quoted literal decision-case-N wrapped in backticks, a lint ref finding; no content change (case 140)"
```

```tasks
- [ ] nothing to code: the librarian's `generate` applies the two `replace` entries; `uv run guppi lint` then shows 72 findings and no `ref` (140)
```

## Deferred

## Case 141 — Slice 3b: Work Mode, deferred once more

> **context:**
> `rule-work-mode` and `rule-subagent-guppi` have stood as placeholders since case 29, then 64, 78, 93, 107, 116, 129, without `kind`, `estimates` or `tags`; the two lint orphans and 8 `schema` findings. Case 129 (session N) set Slice 3b apart as the next session's whole agenda.

> **problem:**
> The owner opened session O on the state after session N and the open Insights instead — Cases 133–140 — and skipped Slice 3b at `/hi`. The two pages stay placeholders one more session; the postponement count goes to 10.

```then
defer:
  - slug: rule-work-mode
    type: rule
    purpose: The rule of Work Mode — the Spec as tasks with code, the ticked boxes, what a subagent may do, and the fork that comes back as a Case; the Plan Mode of a session of its own
  - slug: rule-subagent-guppi
    type: rule
    purpose: Governs Work Mode's subagents — they execute the Spec's tasks, never decide, and return a fork as a Case; the Plan Mode of a session of its own
```
