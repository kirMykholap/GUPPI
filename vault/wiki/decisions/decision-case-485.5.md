---
type: decision
case: "485.5"
status: current
update: ["[[estimate-ledger-tail]]"]
origin: raw/2026-09-28/2000/ledger.md#case-485.5
sprint: migration
created: 2026-09-28
tags: [session, harness, ledger]
---

## Context

Each Estimate page states one promise about a rule and says how to check it. Pages written before the Estimate model of case 193 still use the old layout. They have a `## Context` section and a `## Method` section instead of a `method` field, no `purpose` field, and often a Criterion built as a stack of dated `### case N` blocks, one added per change. `make lint` counts these pages as `unmigrated` and reports 18 (brief). The stacks mix behaviour that repeats at every run with things done once or with bookkeeping. For example, `estimate-git-context-current` still promises that it "gets a `### case 115` block, `pending`", and `estimate-hi-no-read-calls` that it "gets a `### case 101.3` block". One of the 18, `estimate-close-commits`, is already recut by case 482, so 17 remain, over 16 rules.
The person decided in two rounds. The 17 pages go in four Cases by area: session start and `/hi`, render and settings, the end of a session and the librarian, and the rest (`estimate-ask-finds`, `estimate-tests-clock-pinned`). This Case takes session start and `/hi`, with one sub-case per Estimate. Each new Criterion keeps the behaviour that the code and the Render show today. It drops lines that record a one-time act or bookkeeping, and this `context` names each dropped line. A line that the code no longer honours, with no decision that removed it, is dropped as well. Each old `## Method` becomes a `method` field that a later session can repeat, and the update that sets it also removes `## Context` and `## Method` (case 211). The pages also get the `purpose` field they lack. A one-time act is a line of a Case's `tasks` list, never an Estimate, and no new status is made for it. The fate of a sprint's done-conditions after the close of the sprint stays with the open item of Slice 5 (case 478.2). The Slice 3g note stays as it is until the last group, as on C1 (484.7). The Case of the last group ticks the note and adds a new note: remove the code that still reads the old layout, in a later session, once lint shows zero (case 202).
What each new Criterion keeps and drops. The check of the answer notes every old line as not carried, because each new line is a whole statement and not the old wording. Their content is carried, except for the lines named here. 485.1 keeps both halves of the promise: without `/hi` the line reaches no ledger and the reply the person sees names the cause, and with `/hi` it reaches the ledger with its time. The ledger path is now `vault/raw/<hi date>/<hi HHMM>/ledger.md`, since case 103.1 moved the ledger into the session folder. The exit code and the stderr line of the refusal are not written into 485.1, because `estimate-ledger-write-lifts` promises them ("Without a `hi`: exit 2 with the reason, the ledger untouched"), and a second copy would sign one promise twice. "Both readings taken end to end" is a way of reading, so it moves into `method`. 485.2 drops the `hi` line of `event_log.md`, because `estimate-event-log-records` promises it. It also drops the marker bookkeeping of block 101.3, and keeps the order of the children as the order of the context, with the output of `guppi tail` as the line `Tail:`. 485.3 drops "a diff on that line is a Frontier item", because `estimate-hi-writes-frontier` promises it ("a hand edit shown by `Render:`"). It also drops the bookkeeping line and the `{supersedes:case 106}` line of block 115. 485.3 keeps "no pull happens later in the session": no code enforces it, but the event log records every Bash call with its command, so a reading can check it. 485.4 and 485.5 drop nothing. They carry every old line as a whole statement, and the Render note in brackets of block 101.2, `partial` and the skill file, becomes its own line. Every kept line was read against `.claude/skills/hi/SKILL.md`, `guppi/tail.py` with `uncovered_lines` and `units_with`, and `guppi/ledger.py`. None of them is contradicted by the code, so the rule on a line the code no longer honours drops nothing here.
The frame. No behaviour changes, so no Render, code, test or hook changes, and no reader keeps an old form. `rule-estimates-schema` says the older pages lack `purpose` and `method` "until their recut", and that stays true. `estimate-lint-counts-the-unmigrated` promises how lint counts, not how many pages it counts, so it is not touched. The other Estimates of these rules (`estimate-hi-writes-frontier`, `estimate-internal-context-loaded`) are already in the new layout and are not touched. `rule-git-context` and `rule-github-issues` carry `deferred_by` for the pull and `gh` state. No open Frontier line of this session names them, and this Case changes only their Estimates, so their backlog items stand. `rule-session-start` is a MOC, so its Estimate's method names `make test-session-start`. All the children of `rule-skill-hi` are render children of a full MOC, so `by hand` passes lint for `estimate-hi-no-read-calls`. The Case creates no page, so no vault query was run. Not done: the other three groups, the ticking of the Slice 3g note, and the removal of the old-layout code.

## Problem

Five Estimates of session start and `/hi` still use the old layout: sections instead of a `method` field, no `purpose`, and Criteria stacked from dated blocks. Their promises mix repeating behaviour with one-time acts and bookkeeping, lint counts them as `unmigrated`, and a reading cannot tell which lines still hold.

## Given

`estimate-ledger-tail` — the promise, its Criterion replaced whole
**＋** `rule-ledger-tail` — the rule it promises for; its Render holds the line `Tail:`
**＋** `guppi/tail.py` — the script `guppi tail`
**＋** `guppi/archive.py` — `uncovered_lines`, the coverage of a line
**＋** `guppi/materialize.py` — `units_with` and `parse_line`, the walk and the record lines
**＋** `vault/raw/` — the folder of the ledgers and their yaml files
**＋** `tests/test_tail.py` — the tests the reading runs
**＋** `.claude/skills/hi/SKILL.md` — the skill `/hi` that splices the line

## History

- 2026-09-28 created · raw/2026-09-28/2000/ledger.md#case-485.5
