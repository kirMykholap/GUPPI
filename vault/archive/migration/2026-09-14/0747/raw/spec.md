<!-- approved 09:07:48 · session fde37e7c -->

# Spec — session M, 2026-09-14, hi 07:47

## Work without a decision

F1, F2, F11 of the Frontier: no Case, no ledger `decision` line; the readings are written as `estimate[...]` lines the moment they exist.

```tasks
- [x] F1: read `estimate-settings` against this session start
- [x] F1: read `estimate-hi-no-read-calls` against this session start (101.3: the `Tail:` line arrived with no read call)
- [x] F1: read `estimate-hi-writes-frontier` against this session start (101.4: `raw/2026-09-14/0747/frontier.md`)
- [x] F1: read `estimate-pretask-reconciles`, live, at `/pre-task`
- [x] F1: read `estimate-ask-finds` — dispatch `ask-guppi` with the archived slug `estimate-agents-at-import-not-expanded`
- [ ] F1: read `estimate-retro-loads`, live, at `/retro`
- [ ] F2: read `estimate-documentation-completes` against the librarian's run of session L
- [x] F2: read `estimate-close-commits` against the librarian's run of session L
- [x] F2: read `estimate-generate-writes` against the librarian's run of session L — `failed` on block 104.3 (07:47); read again after Case 110
- [x] F2: read `estimate-cleanup-moves` against the librarian's run of session L
- [x] F2: read `estimate-materialize-walks-dates` against the librarian's run of session L
- [x] F2: read `estimate-generate-walks-dates` against the librarian's run of session L
- [x] F2: read `estimate-materialize-assembles` against the librarian's run of session L
- [x] F2: read `estimate-ledger-tail`, live: `Tail:` printed nothing after commit `18907ec`, both units of 09-13 applied
- [ ] F7: the librarian's Archive step moves `raw/2026-09-13` and `raw/2026-09-13/0652` (both `kept_reason` None on 2026-09-14, targets `vault/archive/migration/2026-09-13/raw/` and `.../0652/raw/` free); the handoff names the two expected stdout lines, the brief reports what moved
- [ ] F11: `handoff.md` tells the librarian to add to Slice 5 of `sprint.md`: remove the date folders of `raw/` that hold only an `event_log.md`; no one-off cleanup now
```

## Case 110 — the cascade reads a child's status in the archive

> **context:**
> Case 104.3 made the cascade of `generate` recount the `severity` of every Insight and archive an `open` one with no live child. The brief of session L flags the same page a second time: `insight-ledger-hook-reads-only-the-final-text` says `severity: 3` with three children, one of them — `lesson-ledger-hook-drops-a-block-followed-by-tool-calls-in-the-turn` — `status: archived` in `vault/archive/migration/2026-09-12/1156/lessons/`. The brief ranks the deferred list by Insight severity, so a wrong count moves items.

> **problem:**
> The recount reads the status of a child from `wiki/lessons/` only. A child whose page `cleanup` moved into the archive has no page there; the code gives it an empty Page with no status and counts it as live (`generate.py:711`). The count is wrong the moment a child is archived, which is exactly the moment the count matters.

> **given:**
> `generate.cascade` (`generate.py:688-721`) reads `wiki/lessons/*.md` into a dict and counts a child live when `lessons.get(s, Page(...)).status != "archived"`; a slug absent from the dict is an empty Page, status `None`, counted live.
> **＋** `Vault.find` and `archived_paths` (`generate.py:207-258`) already reach a page in the archive by slug, in a category folder, `raw/` excluded (case 105.3).
> **＋** The contract of 104.3, block `### case 104.3` of `estimate-generate-writes`: `severity` 0 — every child `archived` — gives `status: archived`; 1 or more — as it is. `insights/schema.md:19`: `severity` = `count(children where status != archived)`. Neither says where the status is read.
> **＋** The page today: `severity: 3`, three children, one archived; the right count is 2. `estimate-generate-writes` is `pending` with five blocks (101.1, 104.1, 104.2, 104.3, 105.3); `rule-page-generation` is `draft` on it.
> **＋** The branch for an `actioned` Insight (104.2) skips a child absent from the dict; a child already in the archive is already `archived`, so that branch is right as it is.
> **－** `insights/schema.md:30` and `rule-synthesis:22` say "the archive is not read" — of synthesis, which matches lessons by meaning. Resolving a known slug is what `find` does since 105.3, not a search.
> **－** `insights/schema.md:19` says the count is "recomputed by lint"; no code in `lint.py` recounts it, `generate` alone does: Case 110.1.
> **－** The Frontier line F6 closes on this Case.

> **when:**
> In the cascade `generate` recounts the `severity` of an Insight.

> **then:**
> The status of a child is read from its live page under `wiki/lessons/`, else from its page under `vault/archive/` found the way `find` finds a page for an `update` (case 105.3).
> **＋** A child with no page anywhere is counted live, as today — a missing page is a lint `ref` finding, not a withdrawal.
> **＋** On the next librarian run `insight-ledger-hook-reads-only-the-final-text` goes to `severity: 2`; its `children` keep the three slugs.
> **＋** A test in `tests/test_generate.py`: an Insight with one live child and one child in `vault/archive/<sprint>/<date>/<HHMM>/lessons/` recounts to 1; with its only child there, to 0 and `archived · no live child`.
> **－** `contract: same`: no block is added to `estimate-generate-writes`; its reading, due against session L's run (F2), fails today on block 104.3 and is taken again after the fix.

```then
update:
  - slug: rule-page-generation
    contract: same
    replace:
      - old: "the `severity` of every insight is recounted;"
        new: "the `severity` of every insight is recounted, the status of a child read from its page under `wiki/lessons/` or, failing that, under `vault/archive/` the way `find` reaches a page, a child with no page anywhere counted live (case 110);"
    change: the cascade reads a child's status in the archive too, so an archived child is not counted live (case 110)
```

```tasks
- [x] `guppi/generate.py`: in `cascade`, resolve a child slug absent from `wiki/lessons/` through `archived_paths` (a `raw/`-excluded category folder under `vault/archive/`) and read its status there; no page anywhere stays live
- [x] `tests/test_generate.py`: an Insight with one live and one archived child (`vault/archive/<sprint>/<date>/<HHMM>/lessons/`) recounts to 1; with its only child archived, to 0 and History `archived · no live child`
- [x] `make test`, `make style`
- [x] read `estimate-generate-writes` again after the fix (block 104.3 against the test; the other four blocks against the librarian's run of session L)
```

### Case 110.1 — the schema names the recount's owner

> **given:**
> `insights/schema.md:19`: "`count(children where status != archived)`. Recomputed by lint, never written by hand." No code in `lint.py` recounts `severity`; `generate.cascade` does (case 104.3). A Rule-class file, slug `insights-schema`, applied by hand.

> **when:**
> Someone reads the `severity` row of `insights/schema.md`.

> **then:**
> The row says the count is recomputed by the cascade of `generate`, never written by hand.

```then
update:
  - slug: insights-schema
    file: vault/wiki/insights/schema.md
    change: "severity row: recomputed by the cascade of `generate` (case 104.3), not by lint, never written by hand (case 110.1)"
```

```tasks
- [x] `vault/wiki/insights/schema.md` `severity` row, by hand (110.1)
```

## Case 111 — the `hi` line carries the session id

> **context:**
> Today at 07:30:30 two sessions started in one second: this one, `fde37e7c`, and `19b07bbc`, session L, restored by `resume`. The `hi` of 07:30:39 carries `--------` — `CLAUDE_SESSION_ID` is empty in the `!` substitution of the skill — so the ledger hook tied it to the start nearest before it, the foreign one, and refused every line of this session. A second `/hi` did not help: `hi_recorded` sets `ours = False` on the foreign start and only a new `session-start` of our own sets it back; a `resume` of this session at 07:46:53 did. The lesson line of 07:44 ends "A second /hi at 07:44 fixed the window", which is false.

> **problem:**
> The window of a session is inferred from the order of starts around an unstamped `hi`. One foreign start between our start and our `hi` — a restored tab is enough — takes the `hi` away, and the session cannot recover by any command of its own. `rule-event-log` names this as a known limit since Case 9. The lesson page will be born with a wrong root cause.

> **given:**
> `guppi event <name>` (`guppi/event.py`) writes `- HH:MM:SS <stamp> <event> <detail>`, the stamp from `--session` or the payload's `session_id`, `--------` when neither; registered on `SessionStart` and `PostToolUse` (`rule-hook-registry`, `.claude/settings.json`). The `/hi` skill (`rule-skill-hi`, `render_mode: full`) writes its `hi` through a `Recorded:` `!` substitution of `guppi event hi --session "${CLAUDE_SESSION_ID:-}"`; the variable is empty there, every `hi` in the logs is `--------`.
> **＋** `hi_recorded` and `hi_moment` (`guppi/ledger.py:126-146, 176-196`): a `hi` after a `session-start` of this stamp with no other session's start in between; a `resume` or `compact` of our own does not close the window (case 14). `session_dir` — used by `ledger`, `gate`, `pretask`, `spec`, `cleanup` — takes the first such `hi`.
> **＋** `UserPromptSubmit` hooks receive `session_id` and `prompt` on stdin; no matcher on the prompt text, so the filter is the script's. Not yet measured in this repository: whether the event fires for a slash command; the reading of 111.1 at the next `/hi` says.
> **＋** `rule-event-log` (`built`, `estimate-event-log-records` `passed`): "Known limit" paragraph, lines 47–49. `rule-ledger-write` (`built`, `estimate-ledger-write-lifts` `passed`): the window paragraph, lines 41–46. `rule-hook-registry` (`built`, `estimate-hook-registry-rendered` `passed`), the Render is the `hooks` section of `settings.json`. `rule-skill-hi` (`draft`, `deferred_by: decision-case-106`).
> **＋** The lesson line `lesson-hi-taken-by-a-session-started-in-the-same-second` is in the ledger of this session (07:47); its page is created by the next librarian run, and an `update` in the same yaml applies after it, in ledger order.
> **－** The `--------` lines of the older logs are not rewritten; `event_log.md` is gitignored and no page points at a `hi` line.
> **－** Case 106 (a render inside `/hi`) is not touched; it stays deferred on `rule-skill-hi`.
> **－** The Frontier line F12 closes on this Case.

### Case 111.1 — `rule-event-log`: the `hi` event on `UserPromptSubmit`

> **given:**
> `UserPromptSubmit` fires on every prompt; there is no matcher on the prompt text, so the filter is the script's. The payload carries `session_id` and `prompt`. The `!` substitution of the skill sees no session id (`--------` on every `hi` line today); a `PreToolUse Skill` hook does not see a command the person types (`rule-skill-hi`, Purpose). `guppi event tool` already runs once per tool call, on `PostToolUse` with no matcher.
> **＋** `hi_moment` takes the first `hi` of the window; a second `hi` line of the same session changes nothing there, it is log noise.
> **＋** The `hi` of this session in the logs walked: `session_event_logs` from today back to the first date holding this session's `session-start` (case 55.1).

> **when:**
> The person submits a prompt and the `UserPromptSubmit` hook `uv run guppi event prompt` runs.

> **then:**
> When the prompt, trimmed, is `/hi` or starts with `/hi `, and no `hi` of this session's stamp follows its first `session-start` in the logs walked, the log gains `- HH:MM:SS <stamp> hi`, the stamp from the payload's `session_id`.
> **＋** A second `/hi` of the same session writes nothing: one session, one `hi` line.
> **＋** Any other prompt writes nothing; exit 0 either way, an error on stderr only.
> **＋** The "Known limit" paragraph of the page says the limit is lifted by this Case; a `hi` of one session no longer belongs to another.
> **＋** `estimate-event-log-records` gets a `### case 111.1` block, `pending`; read at the next `/hi`: the log carries `<stamp> hi` for that session, and a repeated `/hi` adds no line.

```then
update:
  - slug: rule-event-log
    contract: changed
    replace:
      - old: "`/hi` writes its own `hi` line through a `!` substitution, with the session id when `CLAUDE_SESSION_ID` reaches a substitution and `--------` when it does not."
        new: "The `hi` line is written by `guppi event prompt` on `UserPromptSubmit`: when the prompt, trimmed, is `/hi` or starts with `/hi `, and no `hi` of this session's stamp follows its first `session-start` in the logs the ledger hook walks, the log gains `- HH:MM:SS <stamp> hi`, the stamp from the payload's `session_id`; a second `/hi` of the same session and any other prompt write nothing (case 111.1). Until case 111.4 the skill's `!` substitution writes a second, unstamped `hi` line, which the ledger hook ignores."
      - old: "**Known limit.** With `--------` on the `hi` line, two sessions open at once in one repository cannot be told apart by the ledger hook, which looks for a `hi` after the last `session-start` of its own session. Sequential sessions are fine."
        new: "**A limit lifted.** Until case 111 the `hi` line carried `--------` and the ledger hook looked for a `hi` after the last `session-start` of its own session, so two sessions open at once could not be told apart; on 2026-09-14 a session restored by `resume` in the same second took the `hi` of the session that typed it. With the stamp on the `hi` line a `hi` of one session never belongs to another (case 111.1)."
    change: the hi line is written by guppi event prompt on UserPromptSubmit with the session's stamp, once per session; the known limit is lifted (case 111.1)
```

```tasks
- [x] `guppi/event.py`: `prompt` — read `prompt` from the payload; when trimmed it is `/hi` or starts with `/hi `, and no `hi` of this stamp follows the first `session-start` of this stamp in the logs `session_event_logs` walks, write `hi` with the stamp; else write nothing; exit 0 always, errors on stderr (the walk lives in `ledger.py`, which imports `event.py`: import inside the function, or move `session_event_logs` to `event.py`)
- [x] `tests/test_event.py`: `/hi` writes `<stamp> hi`; `/hi again` writes it; a second `/hi` of the same session writes nothing; `hello` writes nothing; exit 0 with an unreadable payload
- [ ] read `estimate-event-log-records` at the next `/hi` after the render: `<stamp> hi` in the log; a repeated `/hi` adds no line
```

### Case 111.2 — `rule-hook-registry`: the hook is registered

> **when:**
> `guppi render` writes `.claude/settings.json`.

> **then:**
> The `hooks` section carries `"UserPromptSubmit": [ { "hooks": [ { "type": "command", "command": "uv run guppi event prompt", "timeout": 30 } ] } ]` between `SessionStart` and `PreToolUse`.
> **－** `contract: same`: the Estimate checks that the render reproduces the file, not which hooks it holds.

```then
update:
  - slug: rule-hook-registry
    contract: same
    replace:
      - old: |
          { "type": "command", "command": "uv run guppi render --sync", "timeout": 60 } ] }
          ],
          "PreToolUse": [
        new: |
          { "type": "command", "command": "uv run guppi render --sync", "timeout": 60 } ] }
          ],
          "UserPromptSubmit": [
            { "hooks": [ { "type": "command", "command": "uv run guppi event prompt", "timeout": 30 } ] }
          ],
          "PreToolUse": [
    change: guppi event prompt registered on UserPromptSubmit (case 111.2)
```

```tasks
- [ ] `vault/wiki/rules/rule-hook-registry.md` Render gains the `UserPromptSubmit` entry (the librarian's `generate` applies it); `guppi render` then writes `.claude/settings.json` — the hook is live from the session after the librarian's run
```

### Case 111.3 — `rule-ledger-write`: the window is the session's own `hi`

> **when:**
> The `Stop` hook has lines to write, or a script asks `session_dir` for the session's folder.

> **then:**
> The session is a working one when a `hi` line of this session's stamp follows its first `session-start` in the logs walked; the folder is the first such `hi`.
> **＋** A `session-start` of another session, before or after, changes nothing; a `resume` or `compact` of our own still does not close the window (case 14).
> **－** A `hi` with `--------` or another stamp does not count.
> **＋** `estimate-ledger-write-lifts` gets a `### case 111.3` block, `pending`; the test seeds our start, a foreign `resume` and a stamped `hi` and expects the window open, and a `--------` `hi` alone and expects it refused.

```then
update:
  - slug: rule-ledger-write
    contract: changed
    replace:
      - old: "The session is a working one when a `hi` line follows a `session-start` line of this session's id, with no other session's start in between. Only a `session-start` of another session closes the `hi` window; `compact` and `resume` of the same session do not — `SessionStart` fires on both, and neither changes the person, the branch or the agenda (case 14)."
        new: "The session is a working one when a `hi` line of this session's id follows its first `session-start` line in the logs walked (case 111.3); the session's folder is the first such `hi`. A `session-start` of another session, before or after, changes nothing; a `hi` with `--------` or another id does not count. `compact` and `resume` of the same session do not close the window — `SessionStart` fires on both, and neither changes the person, the branch or the agenda (case 14)."
    change: the window is the session's own stamped hi after its first start; a foreign start no longer closes it (case 111.3)
```

```tasks
- [x] `guppi/ledger.py`: `hi_recorded` and `hi_moment` — a `hi` whose stamp is ours after the first `session-start` of ours; foreign starts ignored; `--------` ignored; the refusal message unchanged
- [x] `tests/test_ledger.py`: our start, a foreign `resume`, a stamped `hi` → open, folder by that `hi`; a `--------` `hi` alone → refused; two stamped `hi` → the first names the folder; a stamped `hi` before our start → refused; the existing window tests updated to stamped `hi` lines
- [x] `make test`, `make style`
- [ ] read `estimate-ledger-write-lifts` against the tests and the first ledger write after the render
```

### Case 111.4 — `rule-skill-hi`: one writer of the `hi` line

> **when:**
> The person invokes `/hi`.

> **then:**
> The skill body no longer carries the `Recorded:` substitution; the `hi` line comes from the hook of 111.1 alone. The page's Purpose says the mark is the hook's.
> **－** `contract: same`: the two Estimates of the page are about read calls and the Frontier; the log still carries a `hi` line after `/hi`.
> **－** Work Mode removes the substitution only after the reading of 111.1 passed; until then both lines are written and the unstamped one is ignored.

```then
update:
  - slug: rule-skill-hi
    contract: same
    replace:
      - old: "The skill also leaves the `hi` mark in the event log itself: a command typed by the person does not pass through the `Skill` tool, so no hook would see it."
        new: "The `hi` mark in the event log is left by the `UserPromptSubmit` hook `guppi event prompt` (`rule-event-log`, case 111.1), which sees the session id; the skill's own `!` substitution could not (case 111.4). A command typed by the person does not pass through the `Skill` tool, so no `PreToolUse` hook sees it."
      - old: "Recorded: !`uv run guppi event hi --session \"${CLAUDE_SESSION_ID:-}\"`\n\n<!-- rule-internal-context -->"
        new: "<!-- rule-internal-context -->"
      - old: "`${CLAUDE_SESSION_ID:-}` passes the session id to the event log when the variable exists inside a substitution and an empty string otherwise; the probe of Slice 1 measures which. For that one session the skill file carries an extra `Probe:` line that is not part of this render."
        new: "The skill writes no event line of its own since case 111.4: a `!` substitution never saw `CLAUDE_SESSION_ID` (every `hi` of sessions A–M carried `--------`), so the `hi` line is the `UserPromptSubmit` hook's, which reads the session id from its payload (`rule-event-log`, case 111.1)."
    change: the Recorded substitution removed and the CLAUDE_SESSION_ID paragraph replaced; the hi line is the UserPromptSubmit hook's (case 111.4)
```

```tasks
- [ ] (owner's choice at Retro, 09:50: applied by this run's librarian, before the reading of 111.1) `vault/wiki/rules/rule-skill-hi.md` Render without the `Recorded:` line (the librarian's `generate`), then `guppi render` writes `.claude/skills/hi/SKILL.md`; if the reading fails, this sub-case is superseded, not applied — the handoff says which
```

### Case 111.5 — the lesson's root cause corrected

> **when:**
> The librarian's `generate` applies this session's yaml.

> **then:**
> `lesson-hi-taken-by-a-session-started-in-the-same-second` carries a `root_cause` ending: the second `/hi` did not fix it — `hi_recorded` stays closed until a new `session-start` of the same session; a `resume` at 07:46:53 reopened it.
> **＋** History: `updated: root_cause corrected (case 111.5)`.

```then
update:
  - slug: lesson-hi-taken-by-a-session-started-in-the-same-second
    set:
      root_cause: "the hi line carries no session id (CLAUDE_SESSION_ID is empty in the skill's shell), so hi_recorded ties it to the session-start lines around it; a second session, 19b07bbc, started by resume in the same second 07:30:30 and its start stood between our start and the hi, which went to it. A second /hi at 07:44 did not fix it: hi_recorded stays closed once a foreign start follows our own, until a new session-start of our session is logged; a resume of this session at 07:46:53 reopened the window, and the hi of 07:47 named the folder."
    sections:
      Root cause: |
        the hi line carries no session id (CLAUDE_SESSION_ID is empty in the skill's shell), so hi_recorded ties it to the session-start lines around it; a second session, 19b07bbc, started by resume in the same second 07:30:30 and its start stood between our start and the hi, which went to it. A second /hi at 07:44 did not fix it: hi_recorded stays closed once a foreign start follows our own, until a new session-start of our session is logged; a resume of this session at 07:46:53 reopened the window, and the hi of 07:47 named the folder.
    change: root_cause corrected (case 111.5)
```

```tasks
- [ ] nothing in Work Mode: the librarian's `generate` creates the lesson from its ledger line and applies this update after it, in ledger order
```

### Case 111.6 — the unstamped `hi` of the sessions before the hook

> **given:**
> 111.3 says a `hi` with `--------` does not count. The hook of 111.1 that writes a stamped `hi` reaches `settings.json` only after the librarian of this session renders it. Every `hi` of sessions A–M is `--------`, this session's included; the code of 111.3 in the working tree refused 13 lines at 09:5x, and `session_dir` — the folder `0747` of this session, its Spec, its ledger — resolves through that unstamped `hi` too. A fork of Work Mode, returned as a Case.
> **＋** `hi_recorded` and `hi_moment` (`ledger.py`, as changed by 111.3) skip every line of another stamp. The tests of 111.3 stand; `test_an_unstamped_or_foreign_hi_does_not_count` splits: a foreign `hi` never counts; an unstamped `hi` counts by the old rule when no stamped one exists, and is refused after a foreign start.
> **－** The fallback leaves with a later Case, once the readings of 111.1 pass and no writer of `--------` is left (111.4).

> **when:**
> The `Stop` hook, `pretask`, `spec`, `gate` or `cleanup` asks whether the session has a `hi`, or where its folder is.

> **then:**
> A `hi` of this session's stamp after its first `session-start` opens the window, as 111.3 says.
> **＋** With no such line in the logs walked, a `--------` `hi` after a `session-start` of this session with no other session's start in between opens it — the rule before 111.3, kept for the sessions the old skill line opened.
> **－** A `hi` of another session's stamp never counts.
> **＋** `estimate-ledger-write-lifts` gets a `### case 111.6` block, `pending`; the test seeds an unstamped `hi` under our start and expects the window open, and the same with a foreign start between and expects it refused.

```then
update:
  - slug: rule-ledger-write
    contract: changed
    replace:
      - old: "A `session-start` of another session, before or after, changes nothing; a `hi` with `--------` or another id does not count."
        new: "A `session-start` of another session, before or after, changes nothing; a `hi` with another id does not count. With no stamped `hi` in the logs walked, a `--------` `hi` counts by the rule before 111.3 — after a `session-start` of this session with no other session's start in between — for the sessions the old skill line opened (case 111.6)."
    change: an unstamped hi keeps its window by the old rule while no stamped hi exists (case 111.6)
```

```tasks
- [x] `guppi/ledger.py`: `hi_moment` falls back to `unstamped_hi_moment` — the rule before 111.3 over the `--------` lines — when no stamped `hi` is found
- [x] `tests/test_ledger.py`: an unstamped `hi` under our start → open; after a foreign start → refused; a stamped `hi` later wins; a foreign `hi` never counts
- [x] `make test` (318), `make style`
- [ ] read `estimate-ledger-write-lifts` against the tests and the first ledger write after the render, with 111.3
```

## Case 112 — the text debt lint carries

> **context:**
> F8 (e): seven findings of `guppi lint` that are wording, not behaviour — four `method`, two `## Context`, one `ref` — and the two wordings of `estimate-cleanup-moves` the brief flags every run. Each has stood for two or more librarian runs.

> **problem:**
> Two of the four `method` findings are not the pages' fault: `estimate-documentation-completes` and `estimate-harness-pipeline` name a `make` target and add "the live reading by hand"; `check_method` (`lint.py:435-441`) tests for the words "by hand" before it looks for the target, so a MOC's Estimate that names both is flagged. The other five are pages with something missing or stale.

> **given:**
> `rule-lint` (`built`, one Estimate `estimate-lint-catches`, `passed`): the Method classes of case 26.2 and 28 — a Leaf's Estimate names a `tests/` file or says "by hand"; a MOC's names a `make <target>`, or says "by hand" when every child's Estimate is by hand.
> **＋** `estimate-default-mode` (target `rule-default-mode`, Leaf): Method names no `tests/` file; `tests/test_render.py` is the test that checks `defaultMode` in the rendered `settings.json`.
> **＋** `estimate-settings` (target `rule-settings`, MOC, child of `rule-harness`): Method names no `make` target; `make test-harness` is the pipeline over `rule-harness`'s children.
> **＋** `estimate-generate-walks-dates` and `estimate-materialize-walks-dates`: no `## Context`; both born of case 43, whose Problem on `decision-case-43` is in Russian — the Context is its English. `write_page` orders sections by the schema, so a section added by `update` lands before `## Criterion`.
> **＋** `estimate-cleanup-moves`: the prose Criterion from before case 72 says `vault/archived/<sprint>/<date>/<category>/`; the block `### case 102.2` says `vault/archive/…/<HHMM>/…`. The block is the contract; the prose is the stale path.
> **＋** `rule-page-generation`, History line of 2026-09-11: "History and log lines end with · [[decision-case-N]] when a decision exists" — a wikilink outside a code span, so lint resolves it. Line 44 has the same text inside a code span and is not flagged.
> **－** Case 110 already updates `rule-page-generation`; a second `update` of the same page in one session is two entries on one page, in ledger order — allowed.
> **－** The 31 decision pages of Cases 1–28 (F8 a) and the lessons (F8 d) are not this Case.

### Case 112.1 — `rule-lint`: the target before the words

> **when:**
> `guppi lint` checks the Method of an Estimate whose target is a MOC.

> **then:**
> A Method that names a `make <target>` present in the Makefile passes, whatever else it says.
> **＋** Only a Method with no target is judged on "by hand": it passes when every child's Estimate says by hand, and is a finding naming the first child that names a test file.
> **＋** `estimate-lint-catches` gets a `### case 112.1` block, `pending`; a test in `tests/test_lint.py` seeds a MOC's Estimate with `make lint` and "by hand" and expects no finding.

```then
update:
  - slug: rule-lint
    contract: changed
    replace:
      - old: "orphans, a `built` page with an Estimate not `passed`, the two Method classes of case 26.2."
        new: "orphans, a `built` page with an Estimate not `passed`, the two Method classes of case 26.2 — for a MOC's Estimate the `make <target>` is looked for first and a Method that names one passes whatever else it says; \"by hand\" is judged only when no target is named (case 112.1)."
    change: the Method check of a MOC's Estimate looks for the make target before the words by hand (case 112.1)
```

```tasks
- [x] `guppi/lint.py` `check_method`: on a MOC target, `MAKE_TARGET` first; the "by hand" branch only when no target is named
- [x] `tests/test_lint.py`: a MOC's Estimate with `make lint` and "by hand" → no finding; with "by hand" alone over a child naming a test file → the finding as before
- [x] `make test`, `make style`
- [x] read `estimate-lint-catches` against the tests and `guppi lint` on the vault: the two findings on `estimate-documentation-completes` and `estimate-harness-pipeline` gone
```

### Case 112.2 — `estimate-default-mode` names its test

> **when:**
> Someone reads the Method.

> **then:**
> It begins with `tests/test_render.py` and keeps the rest.

```then
update:
  - slug: estimate-default-mode
    contract: same
    sections:
      Method: |
        tests/test_render.py: the rendered .claude/settings.json holds permissions.defaultMode as "plan" and parses; the live half at the next session start — the session opens in Plan Mode and an edit outside the plan file is not made without a sign-off
    change: Method names tests/test_render.py (case 112.2)
```

```tasks
- [ ] nothing in Work Mode; the librarian's `generate` rewrites the Method of `estimate-default-mode`
```

### Case 112.3 — `estimate-settings` names its target

> **when:**
> Someone reads the Method.

> **then:**
> It begins with `make test-harness` and keeps the rest.

```then
update:
  - slug: estimate-settings
    contract: same
    sections:
      Method: |
        `make test-harness`; then uv run guppi render, json.load on .claude/settings.json and guppi render --check; the live half at the next session start — the session-start line in raw/<date>/event_log.md came from the rendered file
    change: Method names make test-harness (case 112.3)
```

```tasks
- [ ] nothing in Work Mode; the librarian's `generate` rewrites the Method of `estimate-settings`
```

### Case 112.4 — two Estimates of case 43 get their Context

> **when:**
> Someone reads `estimate-generate-walks-dates` or `estimate-materialize-walks-dates`.

> **then:**
> Each has `## Context` before `## Criterion`: "`materialize` and `generate` read one `raw/<date>/`, today by default. Nothing materializes the lines written after the librarian's commit unless the next session falls on the same date. The tail of session E was saved by a coincidence of dates only."

```then
update:
  - slug: estimate-generate-walks-dates
    contract: same
    sections:
      Context: |
        `materialize` and `generate` read one `raw/<date>/`, today by default. Nothing materializes the lines written after the librarian's commit unless the next session falls on the same date. The tail of session E was saved by a coincidence of dates only. (The Problem of case 43, in English.)
    change: Context added from the Problem of case 43 (case 112.4)
  - slug: estimate-materialize-walks-dates
    contract: same
    sections:
      Context: |
        `materialize` and `generate` read one `raw/<date>/`, today by default. Nothing materializes the lines written after the librarian's commit unless the next session falls on the same date. The tail of session E was saved by a coincidence of dates only. (The Problem of case 43, in English.)
    change: Context added from the Problem of case 43 (case 112.4)
```

```tasks
- [ ] nothing in Work Mode; the librarian's `generate` adds `## Context` to the two Estimates, before `## Criterion`
```

### Case 112.5 — `estimate-cleanup-moves`, one path

> **when:**
> Someone reads the prose Criterion.

> **then:**
> It says `vault/archive/<sprint>/<date>/<HHMM>/<category>/`, the path of case 102; the block `### case 102.2` is unchanged.

```then
update:
  - slug: estimate-cleanup-moves
    contract: same
    replace:
      - old: "vault/archived/<sprint>/<date>/<category>/"
        new: "vault/archive/<sprint>/<date>/<HHMM>/<category>/"
    change: the prose Criterion names the path of case 102 (case 112.5)
```

```tasks
- [ ] nothing in Work Mode; the librarian's `generate` replaces the path in the prose Criterion of `estimate-cleanup-moves`
```

### Case 112.6 — `rule-page-generation`, the literal quoted

> **when:**
> `guppi lint` reads the History of the page.

> **then:**
> The line of 2026-09-11 carries `· [[decision-case-N]]` in a code span; lint resolves nothing there.

```then
update:
  - slug: rule-page-generation
    contract: same
    replace:
      - old: "History and log lines end with · [[decision-case-N]] when a decision exists, else the ledger pointer"
        new: "History and log lines end with `· [[decision-case-N]]` when a decision exists, else the ledger pointer"
    change: the literal decision-case-N of the History line of 2026-09-11 quoted (case 112.6)
```

```tasks
- [ ] nothing in Work Mode; the librarian's `generate` applies the replace; `guppi lint` after the run shows the seven findings of 112 gone (four `method`, two `## Context`, one `ref`) — the brief says
```

## Case 113 — the ten lessons written before the hook

> **context:**
> F8 (d): ten lessons of sessions A–B, written by hand on 2026-09-09 and 2026-09-10 before the ledger hook and `materialize` existed. Nine have no `tags`; six of `kind: knowledge` have no `source`. 17 of the 116 lint findings.

> **problem:**
> `tags` and `source` are judgments — which registered tags fit, where the knowledge came from — so nobody can fill them but a ratified `update`. Until then the lessons index carries nine untagged rows and six knowledge claims with no origin.

> **given:**
> `lessons/schema.md`: `tags` required; `source` required when `kind: knowledge`, "url or reference — where the material came from". Existing sources are free references. Registered tags (`tags.md`): session, hooks, harness, ledger, git, github, workflow, render, librarian, tests.
> **＋** The Slice 1 probe files the lessons name (`probe-Stop-6.json`, `probe-PostToolUse-1.json`) were removed with `raw/notes/` by case 100.6; the source says so.
> **－** The two `tags` findings that remain after this Case are the placeholders of Case 107 (F4).
> **－** No new tag is declared; `status`, `insight`, `root_cause` are untouched.

> **when:**
> The librarian's `generate` applies this session's yaml.

> **then:**
> Each of the ten pages carries the `tags` and, for the six knowledge lessons, the `source` of the `then` block; History `updated: tags and source filled (case 113)`.
> **＋** `guppi lint` after the run shows 17 findings fewer: 9 `tags`, 6 `source`, and the lessons index rows carry their tags.

```then
update:
  - slug: lesson-agents-at-import-not-expanded
    set:
      tags: [harness, session]
      source: "session E 2026-09-10, the ask-guppi dispatch of the estimate-ask-finds reading (raw/2026-09-10/ledger.md#L3)"
    change: tags and source filled (case 113)
  - slug: lesson-agents-loaded-at-session-start
    set: {tags: [harness, render, session]}
    change: tags filled (case 113)
  - slug: lesson-agents-visible-in-session
    set:
      source: "session E 2026-09-10, the Agent tool listing librarian-guppi at 10:52 after guppi render at 10:40 (raw/2026-09-10/ledger.md#L80)"
    change: source filled (case 113)
  - slug: lesson-estimates-criterion-stale-after-contract-change
    set: {tags: [workflow, ledger]}
    change: tags filled (case 113)
  - slug: lesson-hooks-exitplanmode-payload
    set:
      tags: [hooks, harness]
      source: "the Slice 1 probe on PostToolUse ExitPlanMode, session B 2026-09-09, probe-PostToolUse-1.json — removed with raw/notes/ by case 100.6"
    change: tags and source filled (case 113)
  - slug: lesson-hooks-messagedisplay-cannot-block
    set:
      tags: [hooks, harness]
      source: "the Hook entry of the glossary of 2026-08-29, before the migration"
    change: tags and source filled (case 113)
  - slug: lesson-hooks-sessionstart-cannot-block
    set:
      tags: [hooks, harness, session]
      source: "the Hook entry of the glossary before the migration, carried from the earlier harness"
    change: tags and source filled (case 113)
  - slug: lesson-hooks-stop-payload
    set:
      tags: [hooks, ledger]
      source: "the Slice 1 probe on Stop, session B 2026-09-09, probe-Stop-6.json — removed with raw/notes/ by case 100.6"
    change: tags and source filled (case 113)
  - slug: lesson-hooks-windows-stdin-encoding
    set: {tags: [hooks, harness]}
    change: tags filled (case 113)
  - slug: lesson-tests-cli-date-pinned
    set: {tags: [tests]}
    change: tags filled (case 113)
```

```tasks
- [ ] nothing in Work Mode; the librarian's `generate` applies the ten updates; `guppi lint` after the run shows 9 `tags` and 6 `source` findings fewer — the brief says
- [ ] F8 (a): `handoff.md` tells the librarian to add to Slice 5 of `sprint.md`: the 31 decision pages of Cases 1–28 without `## Context` and `## Problem` (62 lint findings) — their fate is decided with the fate of every `current` Decision at the close of the sprint (given of case 104)
```

## Case 114 — the `## Insight` section is derived, like `## Parent`

> **context:**
> Twenty `clustered` lessons carry no `## Insight` section. The synthesis sets the `insight` field in the frontmatter, and nothing writes the section `lessons/schema.md` requires. They are 20 of lint's 125 schema findings. Deferred as 96 in session K, with its `purpose` cut short in the yaml and on `decision-case-96`. (Case 108 as it stands; 22 pages today.)

> **problem:**
> Either the synthesis entry carries the section, or the schema stops asking for it. Both are a change of what a synthesis entry holds. (Case 108 as it stands.)

> **given:**
> `lessons/schema.yaml`: `## Insight` optional, required when `status: clustered`; `schema.md:47`: "Script places the link once clustered". 23 live lessons carry `insight:`; one has the section (`lesson-hooks-sessionstart-cannot-block`, written by hand on 09-08); 22 do not — the two of session L among them.
> **＋** `rule-synthesis` Render: the librarian appends an `update` of the lesson with `set: {status: clustered, insight: <slug>}` and nothing else; `deferred_by: [decision-case-108]`. The librarian writes no page: synthesis appends to the yaml, `generate` applies the yaml after it (frame steps 3 and 4), so the field and the section are one write.
> **＋** `generate` writes a page's sections in `SECTION_ORDER`; a derived section is rebuilt from the field on every write of the page — `## Parent` from `parent`, `## Estimates` from `estimates`, `## Children` from `children` (`generate.py:361-366`). The cascade runs after all entries over every live rule, entity, decision and insight; lessons are read there for the recount only.
> **＋** `rule-page-generation` is updated by 110 and 112.6 in this session; one more entry in ledger order. Its two Estimates: `estimate-generate-writes` (blocks 101.1, 104.1–104.3, 105.3, `failed` today) and `estimate-generate-walks-dates`; `estimate_slug: estimate-generate-writes`.
> **－** `rule-synthesis` and the lessons schema do not change; the synthesis entry stays as it is.
> **－** A lesson in the archive is not touched; `cleanup` and lint do not read the section.
> **－** The Frontier line F5 closes on this Case.

> **when:**
> `generate` writes a lesson page, or its cascade runs after all entries.

> **then:**
> A lesson whose `insight` field is set gets `## Insight` holding `- [[<insight>]]`, rebuilt from the field on every write, before `## History`; a lesson without the field has no such section.
> **＋** In the cascade every live lesson with `insight` set and no `## Insight` section, or one that names another slug, is rewritten with the section and History `insight section derived`; the 22 pages are filled at the next librarian run.
> **＋** `estimate-generate-writes` gets a `### case 114` block, `pending`; a test in `tests/test_generate.py`: an `update` with `set: {status: clustered, insight: insight-x}` yields the section; a live lesson with the field and no section gets it in the cascade.
> **＋** `guppi lint` after the run shows the 22 `## Insight` findings gone.
> **－** `{supersedes:case 108}`: `decision-case-108` is superseded, `rule-synthesis` loses `deferred_by`.

```then
update:
  - slug: rule-page-generation
    contract: changed
    estimate_slug: estimate-generate-writes
    replace:
      - old: "and rebuilds that section; a derived Estimate create (case 72.3)"
        new: "and rebuilds that section; a lesson whose `insight` field is set gets `## Insight` holding the link, rebuilt from the field on every write, and the cascade fills it on every live lesson that carries the field without the section, History `insight section derived` (case 114); a derived Estimate create (case 72.3)"
    change: the ## Insight section of a lesson is derived from its insight field, on write and in the cascade; supersedes case 108 (case 114)
```

```tasks
- [x] `guppi/generate.py`: in the derived sections, `## Insight` = `links([insight])` when `insight` is set (lessons); in `cascade`, every live lesson with `insight` and no matching `## Insight` section is rewritten with it and History `insight section derived`
- [x] `tests/test_generate.py`: an `update` of a lesson with `set: {status: clustered, insight: insight-x}` writes `## Insight` with `- [[insight-x]]` before `## History`; a live lesson with the field and no section gets it in the cascade with the History line; a lesson without the field has no section
- [x] `make test`, `make style`
- [x] read `estimate-generate-writes` again after Cases 110 and 114 (blocks 104.3 and 114 against the tests; the other blocks against the librarian's run of session L)
```

## Case 115 — the render after the pull, inside `/hi`

> **context:**
> `git pull` lives inside `/hi`, which runs after the `SessionStart` hooks, so a change the pull brings is rendered only at the following session start. Case 89 puts the render in the librarian's phase and leaves this half open. Deferred as 98 in session K. (Case 106 as it stands.)

> **problem:**
> The render has to run once more after the pull, inside `/hi`. It waits for the pull itself, which has no upstream to pull from yet (sprint, Slice 5). (Case 106 as it stands.)

> **given:**
> `rule-git-context` (`Leaf`, `built`, `estimate-git-context-current` `passed`): the Render is the three lines `Pull:`, `Branch:`, `Status:`; "`git pull` happens here and only here"; a failing pull is a Frontier item, not a stop. `rule-skill-hi` carries `deferred_by: [decision-case-106]`; a supersedes clears it wherever it sits.
> **＋** `guppi render --sync` (`rule-render-harness`, case 59.7): prints a unified diff for each differing file, then writes it; exit 0 always; a `.json` that does not parse stops the write. A run right after a run with nothing changed prints nothing.
> **＋** The librarian commits the rendered files with the pages (case 89.2), so a pull that brings pages brings their render too; the line catches a commit made without the render and a hand edit made between the session start and the pull.
> **＋** The `/hi` skill already says: "what `guppi render --sync` printed at session start is an item when it shows a hand edit" — the same sentence covers this line.
> **－** Not measured: whether `!` substitutions of one skill resolve in document order, so that the render runs after the pull. The reading says; if they resolve together, the line still reports what differs, one pull late.
> **－** `rule-skill-hi` is not changed here (111.4 changes it); `rule-render-harness` is not changed: the command and its contract stay.
> **－** The Frontier line F3 closes on this Case.

> **when:**
> The person invokes `/hi`.

> **then:**
> After the `Pull:` line the context holds a `Render:` line with the output of `uv run guppi render --sync`: a diff per governed file that differed and was written, or nothing.
> **＋** A diff on that line is a Frontier item, as the one of the session start is.
> **＋** `estimate-git-context-current` gets a `### case 115` block, `pending`; read at the next `/hi` after the render: the `Render:` line is present and empty on a clean tree.
> **－** `{supersedes:case 106}`: `decision-case-106` is superseded, `rule-skill-hi` loses `deferred_by`.

```then
update:
  - slug: rule-git-context
    contract: changed
    replace:
      - old: "Pull: !`git pull --ff-only 2>&1 || true`\nBranch: !`git branch --show-current`"
        new: "Pull: !`git pull --ff-only 2>&1 || true`\nRender: !`uv run guppi render --sync`\nBranch: !`git branch --show-current`"
      - old: "`--ff-only` so a pull can never open a merge inside a session start."
        new: "`--ff-only` so a pull can never open a merge inside a session start. The `Render:` line after it runs `uv run guppi render --sync` once more, so what the pull brought reaches its governed files in the same session; a diff on that line is a Frontier item like the one of the session start (case 115)."
    change: a Render line after Pull runs guppi render --sync inside /hi; supersedes case 106 (case 115)
```

```tasks
- [ ] `vault/wiki/rules/rule-git-context.md` Render gains the `Render:` line (the librarian's `generate`); `guppi render` then writes `.claude/skills/hi/SKILL.md` — live from the session after the librarian's run
- [ ] read `estimate-git-context-current` at the next `/hi` after the render: the `Render:` line present, empty on a clean tree
```

### Case 115.1 — `rule-render-harness` names both runs of `--sync`

> **given:**
> `rule-render-harness` How it works, line 27: "`--sync`, the `SessionStart` hook, prints a unified diff for each differing file … so the agent's first turn shows what the render changed". With 115 the same command runs a second time inside `/hi`, after the pull. `contract: same`: the two Estimates of the page check the render and the report, not where `--sync` is called from.

> **when:**
> Someone reads How it works of `rule-render-harness`.

> **then:**
> The sentence names both runs: the `SessionStart` hook, and the `Render:` line of `/hi` after the pull (case 115).

```then
update:
  - slug: rule-render-harness
    contract: same
    replace:
      - old: "`--sync`, the `SessionStart` hook, prints a unified diff for each differing file"
        new: "`--sync`, the `SessionStart` hook and, since case 115, the `Render:` line of `/hi` after the pull, prints a unified diff for each differing file"
    change: --sync is named as the SessionStart hook and the Render line of /hi after the pull (case 115.1)
```

```tasks
- [ ] nothing in Work Mode; the librarian's `generate` applies the replace
```

### Case 115.2 — the Frontier sentence of `/hi` covers the `Render:` line

> **given:**
> `rule-skill-hi` body, line 45 (rendered as `.claude/skills/hi/SKILL.md:30`): "what `guppi render --sync` printed at session start is an item when it shows a hand edit". The `Render:` line of 115 is a second output of the same command inside the skill. `contract: same`: the two Estimates of the page are about read calls and the Frontier file. 111.4 updates the same page; two entries in ledger order.

> **when:**
> The agent assembles the Frontier after `/hi`.

> **then:**
> The sentence reads: what `guppi render --sync` printed at session start or on the `Render:` line above is an item when it shows a hand edit.

```then
update:
  - slug: rule-skill-hi
    contract: same
    replace:
      - old: "what `guppi render --sync` printed at session start is an item when it shows a hand edit."
        new: "what `guppi render --sync` printed at session start or on the `Render:` line above is an item when it shows a hand edit."
    change: the Frontier sentence covers the Render line of /hi (case 115.2)
```

```tasks
- [ ] nothing in Work Mode; the librarian's `generate` applies the replace, `guppi render` writes `.claude/skills/hi/SKILL.md`
```

## Deferred

## Case 116 — Slice 3b: Work Mode

> **context:**
> `rule-work-mode` and `rule-subagent-guppi` have stood as placeholders since case 29, then 64, 78, 93, 107, without `kind`, `estimates` or `tags`; the two lint orphans. The draft in `docs/migration/` still has to be reconciled with case 59.3 — no separate `plan.md`, the `tasks` blocks of the Spec — and with the fork clause. Case 101.1 gives a placeholder a way to be filled.

> **problem:**
> The phase the harness spends most of its time in is the one phase with no ratified rule. It needs a Plan Mode of its own; this session's went to the `hi` window, the cascade, lint's text debt and the render after the pull (Cases 110–115).

```then
defer:
  - slug: rule-work-mode
    type: rule
    purpose: The rule of Work Mode — the Spec as tasks with code, the ticked boxes, what a subagent may do, and the fork that comes back as a Case
  - slug: rule-subagent-guppi
    type: rule
    purpose: Governs Work Mode's subagents — they execute the Spec's tasks, never decide, and return a fork as a Case
```

## Case 117 — the ledger lines of a reply that ends in a tool call

> **context:**
> Four lessons on one writer: `lesson-ledger-hook-misses-a-reply-ending-in-a-tool-call` (F), `lesson-ledger-hook-drops-a-block-followed-by-tool-calls-in-the-turn` (I, archived), `lesson-transcript-omits-text-emitted-before-tool-calls` (L), and today's `lesson-ledger-lines-lost-in-a-reply-ending-in-a-skill-call-with-the-insight-live`. The `Stop` hook reads the final text of a turn; a reply that ends in `Skill`, `ExitPlanMode` or any tool call has no `Stop` and its text is not in the transcript. The Insight's Proposal has stood unactioned since session I.

> **problem:**
> The rule "a reply with ledger lines ends in text" lives in the agent's memory only, and the agent broke it with the lesson live. Either the hook reaches those lines — a `PreToolUse` hook on `Skill|ExitPlanMode` that reads the reply under way, if the payload carries it — or the harness makes the agent's rule mechanical: `CLAUDE.md` says it, and `guppi gate` refuses a `Skill` call while the reply holds an unwritten `LEDGER` block. Which of the two is measurable is a Plan Mode of its own.

```then
defer:
  - slug: rule-ledger-write
    type: rule
    purpose: The ledger lines of a reply that ends in a tool call reach the ledger — by a hook that sees them before the call, or by a gate that refuses the call while they are unwritten; the fourth recurrence of insight-ledger-hook-reads-only-the-final-text
```

## Retro

## Case 118 — the ledger substitution of `/retro` needs no date-level ledger

> **context:**
> The Render of `rule-retro` (109.1) reads the ledgers of the day with `cat vault/raw/$(date +%F)/ledger.md vault/raw/$(date +%F)/*/ledger.md 2>/dev/null`. On 2026-09-14 no date-level ledger exists — the first day with the session form of case 103 alone — so `cat` exits 1, the harness reports the substitution failed, and the skill text does not reach the agent; the `retro` event was still recorded.

> **problem:**
> A substitution that names a file which the model of case 103 no longer guarantees fails on every session from now on. The fix is one `|| true` or a glob-only form; it is an `update` of `rule-retro`, which Retro cannot ratify.

```then
defer:
  - slug: rule-retro
    type: rule
    purpose: The ledger substitution of /retro exits 0 without a date-level ledger — `|| true`, or cat over the files a glob finds — so the skill loads on a day with session ledgers only
```

## Case 119 — an Insight is a Decision target

> **context:**
> Today an Insight is "never a Decision target" (glossary, `insights/schema.md`); it reaches the Frontier only as the "Related Insight" of a deferred Case. `insight-session-vault-knowledge-not-loaded` (severity 3, four lessons after today, the heredoc trap among them) and `insight-ledger-hook-reads-only-the-final-text` (severity 3, four after today) have Proposals nobody was ever asked to ratify or reject; the same trap returns every session.

> **problem:**
> Lessons pile up, the librarian writes the Insight, and nothing puts it in front of the person as a Case. The owner's design: the librarian surfaces an open Insight in the brief as a Case for the next Plan Mode, where it is ratified into a decision on its Proposal, or rejected, or deferred with a count — the same lifecycle a deferred Case has.

```then
defer:
  - slug: rule-brief
    type: rule
    purpose: An open Insight is a Case of the next Plan Mode — the brief lists it beside the Deferred items, ranked by severity, with its Proposal as the recommend; the glossary and insights/schema.md stop saying "never a Decision target", and a Decision may set addressed_by and actioned on it
```

## Case 120 — the heredoc trap is refused by a hook

> **context:**
> `lesson-bash-tool-heredoc-escapes-interpreted` (session H), `lesson-heredoc-trap-hit-twice-with-its-lesson-live` (L), `lesson-heredoc-trap-hit-a-third-time-in-work-mode` (M): a heredoc passed to the Bash tool has its backslash escapes interpreted, and the agent reaches for a heredoc first every session, with the lesson live. The Insight's Proposal — pages of a phase carry its traps — is Case 119's; the trap itself has a mechanical fix.

> **problem:**
> A lesson the agent has to remember is not a rule. A `PreToolUse Bash` hook that refuses a command whose heredoc body carries a backslash escape — or refuses a heredoc that writes a file at all, pointing at Write and Edit — makes the trap impossible instead of remembered.

```then
defer:
  - slug: rule-bash-guard
    type: rule
    purpose: A PreToolUse Bash hook refuses a heredoc whose body carries a backslash escape, or any heredoc that writes a file, and names Write and Edit instead; the third recurrence of the heredoc trap
```

## Case 121 — the pre-task dispatch carries the plan's `then` blocks

> **context:**
> At pre-task of session M the dispatch to `ask-guppi` carried one summary line per decision; four of its ten findings answered things the plan's `then` blocks already did (`lesson-pretask-dispatch-summarized-the-plan-and-ask-guppi-judged-the-summary`). `rule-ask` says "one short question"; `rule-pretask` says "dispatch the agent once with that list".

> **problem:**
> The agent judged pages against a paraphrase and could not see the planned wording. The information it lacked must be in the dispatch: the `then` blocks — `replace` pairs, `set`, `sections` — or the path of the plan file, since the agent has Read.

```then
defer:
  - slug: rule-pretask
    type: rule
    purpose: The pre-task dispatch to ask-guppi carries the then blocks of every ratified Case (replace old/new, set, sections) or the plan file's path, not a summary, so the agent judges the planned text against the pages
```
