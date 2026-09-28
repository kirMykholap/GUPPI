## Case 485 — Slice 3g: the old-layout Estimates of session start and `/hi` recut to one Criterion

> **context:**
> Each Estimate page states one promise about a rule and says how to check it. Pages written before the Estimate model of case 193 still use the old layout. They have a `## Context` section and a `## Method` section instead of a `method` field, no `purpose` field, and often a Criterion built as a stack of dated `### case N` blocks, one added per change. `make lint` counts these pages as `unmigrated` and reports 18 (brief). The stacks mix behaviour that repeats at every run with things done once or with bookkeeping. For example, `estimate-git-context-current` still promises that it "gets a `### case 115` block, `pending`", and `estimate-hi-no-read-calls` that it "gets a `### case 101.3` block". One of the 18, `estimate-close-commits`, is already recut by case 482, so 17 remain, over 16 rules.
> The person decided in two rounds. The 17 pages go in four Cases by area: session start and `/hi`, render and settings, the end of a session and the librarian, and the rest (`estimate-ask-finds`, `estimate-tests-clock-pinned`). This Case takes session start and `/hi`, with one sub-case per Estimate. Each new Criterion keeps the behaviour that the code and the Render show today. It drops lines that record a one-time act or bookkeeping, and this `context` names each dropped line. A line that the code no longer honours, with no decision that removed it, is dropped as well. Each old `## Method` becomes a `method` field that a later session can repeat, and the update that sets it also removes `## Context` and `## Method` (case 211). The pages also get the `purpose` field they lack. A one-time act is a line of a Case's `tasks` list, never an Estimate, and no new status is made for it. The fate of a sprint's done-conditions after the close of the sprint stays with the open item of Slice 5 (case 478.2). The Slice 3g note stays as it is until the last group, as on C1 (484.7). The Case of the last group ticks the note and adds a new note: remove the code that still reads the old layout, in a later session, once lint shows zero (case 202).
> What each new Criterion keeps and drops. The check of the answer notes every old line as not carried, because each new line is a whole statement and not the old wording. Their content is carried, except for the lines named here. 485.1 keeps both halves of the promise: without `/hi` the line reaches no ledger and the reply the person sees names the cause, and with `/hi` it reaches the ledger with its time. The ledger path is now `vault/raw/<hi date>/<hi HHMM>/ledger.md`, since case 103.1 moved the ledger into the session folder. The exit code and the stderr line of the refusal are not written into 485.1, because `estimate-ledger-write-lifts` promises them ("Without a `hi`: exit 2 with the reason, the ledger untouched"), and a second copy would sign one promise twice. "Both readings taken end to end" is a way of reading, so it moves into `method`. 485.2 drops the `hi` line of `event_log.md`, because `estimate-event-log-records` promises it. It also drops the marker bookkeeping of block 101.3, and keeps the order of the children as the order of the context, with the output of `guppi tail` as the line `Tail:`. 485.3 drops "a diff on that line is a Frontier item", because `estimate-hi-writes-frontier` promises it ("a hand edit shown by `Render:`"). It also drops the bookkeeping line and the `{supersedes:case 106}` line of block 115. 485.3 keeps "no pull happens later in the session": no code enforces it, but the event log records every Bash call with its command, so a reading can check it. 485.4 and 485.5 drop nothing. They carry every old line as a whole statement, and the Render note in brackets of block 101.2, `partial` and the skill file, becomes its own line. Every kept line was read against `.claude/skills/hi/SKILL.md`, `guppi/tail.py` with `uncovered_lines` and `units_with`, and `guppi/ledger.py`. None of them is contradicted by the code, so the rule on a line the code no longer honours drops nothing here.
> The frame. No behaviour changes, so no Render, code, test or hook changes, and no reader keeps an old form. `rule-estimates-schema` says the older pages lack `purpose` and `method` "until their recut", and that stays true. `estimate-lint-counts-the-unmigrated` promises how lint counts, not how many pages it counts, so it is not touched. The other Estimates of these rules (`estimate-hi-writes-frontier`, `estimate-internal-context-loaded`) are already in the new layout and are not touched. `rule-git-context` and `rule-github-issues` carry `deferred_by` for the pull and `gh` state. No open Frontier line of this session names them, and this Case changes only their Estimates, so their backlog items stand. `rule-session-start` is a MOC, so its Estimate's method names `make test-session-start`. All the children of `rule-skill-hi` are render children of a full MOC, so `by hand` passes lint for `estimate-hi-no-read-calls`. The Case creates no page, so no vault query was run. Not done: the other three groups, the ticking of the Slice 3g note, and the removal of the old-layout code.

> **problem:**
> Five Estimates of session start and `/hi` still use the old layout: sections instead of a `method` field, no `purpose`, and Criteria stacked from dated blocks. Their promises mix repeating behaviour with one-time acts and bookkeeping, lint counts them as `unmigrated`, and a reading cannot tell which lines still hold.

> **recommend:**
> Replace each Criterion whole with one `When:` and `Then:` of today's behaviour, set `purpose` and a repeatable `method`, and set the page `pending`. Its reading waits for a later session. Name the sprint page with an `update` that has only `change`. Carrying the blocks word for word was rejected: the one-time lines could never pass an honest reading.

### Case 485.1 — A ledger line only in a session opened with `/hi`

> **given:**
> `estimate-session-start-context` — the promise, its Criterion replaced whole
> **＋** `rule-session-start` — the MOC it promises for
> **＋** `/hi` — the skill that opens a working session
> **＋** `guppi/ledger.py` — the `Stop` hook that writes or refuses the lines
> **＋** `vault/raw/<date>/event_log.md` — the log the hook reads for a `hi` line
> **＋** `vault/raw/<hi date>/<hi HHMM>/ledger.md` — the ledger of the session
> **＋** `tests/test_event.py` — tests the reading runs
> **＋** `tests/test_ledger.py` — tests the reading runs

> **when:**
> The main agent ends a reply that carries a `- decision[...]` line inside a `LEDGER` block, and the `Stop` hook `guppi/ledger.py` looks in `vault/raw/<date>/event_log.md` for a `hi` line of the session.

> **then:**
> In a session opened without `/hi`, the line reaches no ledger of the session, and the reply the person sees names the cause.
> **＋** In a session opened with `/hi`, the line reaches `vault/raw/<hi date>/<hi HHMM>/ledger.md` once, with the time of writing before it.

> **tasks:**
> - [ ] update `estimate-session-start-context`
>   - set: `{status: pending, purpose: "A ledger line reaches the session's ledger only in a session opened with /hi, and a refusal tells the person why", method: "make test-session-start; by hand: one session opened without /hi whose reply carries a LEDGER block, and the ledger of the next working session after its first ratification, written into the estimate line"}`
>   - change: `the Criterion replaced whole — one When and Then, the session folder of the ledger; purpose and method set, Context and Method out (case 485.1)`
> - [ ] read `estimate-session-start-context` — `make test-session-start`, then by hand in a later session

> **ratification:**
> ```
> - decision[case 485.1][update][estimate-session-start-context]{ref:estimate-session-start-context}
> ```

### Case 485.2 — The output of `/hi` present with no read call

> **given:**
> `estimate-hi-no-read-calls` — the promise, its Criterion replaced whole
> **＋** `rule-skill-hi` — the MOC that renders the skill, its children in order
> **＋** `.claude/skills/hi/SKILL.md` — the skill `/hi`
> **＋** `rule-internal-context` — the child that loads the vault files
> **＋** `rule-git-context` — the child of the lines `Pull:`, `Render:`, `Branch:`, `Status:`
> **＋** `rule-github-issues` — the child of the line `Open issues:`
> **＋** `rule-ledger-tail` — the child of the line `Tail:`

> **when:**
> The person invokes `/hi`, and Claude Code expands `.claude/skills/hi/SKILL.md` before the agent's first turn.

> **then:**
> The context of the first turn holds the output of each block of the skill, in the order of the children of `rule-skill-hi`: the text of the files `rule-internal-context` loads, the lines `Pull:`, `Render:`, `Branch:` and `Status:` of `rule-git-context`, the line `Open issues:` of `rule-github-issues`, and the line `Tail:` of `rule-ledger-tail`.
> **－** The agent makes no read-tool call to get any of them.

> **tasks:**
> - [ ] update `estimate-hi-no-read-calls`
>   - set: `{status: pending, purpose: "After /hi the output of every block of the skill is in the first turn's context with no read call", method: "by hand at the /hi of the next session: the first turn's context and the tool calls before it read in the transcript, written into the estimate line"}`
>   - change: `the Criterion replaced whole — one When and Then; the hi line left to estimate-event-log-records, the block bookkeeping out; purpose and method set, Context and Method out (case 485.2)`
> - [ ] read `estimate-hi-no-read-calls` — by hand, at the `/hi` of a later session

> **ratification:**
> ```
> - decision[case 485.2][update][estimate-hi-no-read-calls]{ref:estimate-hi-no-read-calls}
> ```

### Case 485.3 — The git state at `/hi`, and no pull after it

> **given:**
> `estimate-git-context-current` — the promise, its Criterion replaced whole
> **＋** `rule-git-context` — the rule it promises for; its Render holds the four lines
> **＋** `.claude/skills/hi/SKILL.md` — the skill `/hi` that runs them
> **＋** `guppi/render.py` — `render --sync`, the command of the `Render:` line
> **＋** `vault/raw/<date>/event_log.md` — the log that records each Bash call of the session

> **when:**
> The person invokes `/hi`, and `.claude/skills/hi/SKILL.md` runs the four commands of `rule-git-context`.

> **then:**
> The context holds `Pull:` with the output of `git pull --ff-only`, then `Render:` with the output of `uv run guppi render --sync` (a diff for each governed file that differed and was written, or nothing), then `Branch:` with the current branch and `Status:` with `git status --short`.
> **＋** A pull that fails prints its message on the `Pull:` line, and the skill still completes.
> **－** No `git pull` runs later in the session: `vault/raw/<date>/event_log.md` shows none after the `hi` line.

> **tasks:**
> - [ ] update `estimate-git-context-current`
>   - set: `{status: pending, purpose: "At /hi the context holds the pull, the render sync, the branch and the status; a failing pull does not stop the skill, and no pull runs later", method: "by hand at the /hi of the next session on the current remote, and that session's event_log.md read at its close for a later git pull, written into the estimate line"}`
>   - change: `the Criterion replaced whole — one When and Then; the Frontier item left to estimate-hi-writes-frontier, the block bookkeeping out; purpose and method set, Context and Method out (case 485.3)`
> - [ ] read `estimate-git-context-current` — by hand, at the `/hi` of a later session and at its close

> **ratification:**
> ```
> - decision[case 485.3][update][estimate-git-context-current]{ref:estimate-git-context-current}
> ```

### Case 485.4 — The open issues, or the reason there are none

> **given:**
> `estimate-github-issues-listed` — the promise, its Criterion replaced whole
> **＋** `rule-github-issues` — the rule it promises for; its Render holds the line `Open issues:`
> **＋** `.claude/skills/hi/SKILL.md` — the skill `/hi` that runs it

> **when:**
> The person invokes `/hi`, and `.claude/skills/hi/SKILL.md` runs `gh issue list --limit 5`.

> **then:**
> The line `Open issues:` holds the list of open issues, or the message of `gh` itself that names why there is none.
> **＋** Neither answer stops `/hi`: the blocks after the line still run.

> **tasks:**
> - [ ] update `estimate-github-issues-listed`
>   - set: `{status: pending, purpose: "At /hi the context holds the open issues or the reason gh gives for none, and the skill completes", method: "by hand at the /hi of the next session, in the current gh state, written into the estimate line"}`
>   - change: `the Criterion replaced whole — one When and Then; purpose and method set, Context and Method out (case 485.4)`
> - [ ] read `estimate-github-issues-listed` — by hand, at the `/hi` of a later session

> **ratification:**
> ```
> - decision[case 485.4][update][estimate-github-issues-listed]{ref:estimate-github-issues-listed}
> ```

### Case 485.5 — The Tail of the ledger

> **given:**
> `estimate-ledger-tail` — the promise, its Criterion replaced whole
> **＋** `rule-ledger-tail` — the rule it promises for; its Render holds the line `Tail:`
> **＋** `guppi/tail.py` — the script `guppi tail`
> **＋** `guppi/archive.py` — `uncovered_lines`, the coverage of a line
> **＋** `guppi/materialize.py` — `units_with` and `parse_line`, the walk and the record lines
> **＋** `vault/raw/` — the folder of the ledgers and their yaml files
> **＋** `tests/test_tail.py` — the tests the reading runs
> **＋** `.claude/skills/hi/SKILL.md` — the skill `/hi` that splices the line

> **when:**
> `uv run guppi tail` runs, from the line `Tail:` of `.claude/skills/hi/SKILL.md` or by hand, over every `ledger.md` under `vault/raw/` and the `materialize.yaml` beside each.

> **then:**
> The script walks the date-level ledger of a date first, then its session ledgers in folder order, dates ascending. It prints every line that `parse_line` reads as a record and whose number is neither in the `line` or `folded` of an entry nor under `unparsed` of the yaml beside it. Each printed line opens with the date, and for a session ledger with the date, a slash and the session folder, then `L<n>:` and the line as the ledger holds it.
> **＋** A ledger without a yaml beside it prints every record line it has.
> **＋** A ledger fully covered prints nothing; with an empty tail the output is empty.
> **＋** Exit 0 always; a ledger that cannot be read is a line on stderr, and the walk goes on.
> **＋** The Render of `rule-ledger-tail`, `partial`, puts one line into `.claude/skills/hi/SKILL.md` between its markers: `` Tail: !`uv run guppi tail` ``.
> **－** `guppi/tail.py` holds no judgment of coverage of its own: the coverage of a line is `uncovered_lines` of `guppi/archive.py`, the one `guppi archive` uses.

> **tasks:**
> - [ ] update `estimate-ledger-tail`
>   - set: `{status: pending, purpose: "guppi tail prints every ledger record line that no materialize.yaml covers, and /hi shows it as Tail", method: "pytest tests/test_tail.py; by hand at the /hi of the next session: the Tail line against a run of uv run guppi tail by hand, written into the estimate line"}`
>   - change: `the Criterion replaced whole — one When and Then; purpose and method set, Context and Method out (case 485.5)`
> - [ ] read `estimate-ledger-tail` — `pytest tests/test_tail.py`, then by hand at the `/hi` of a later session

> **ratification:**
> ```
> - decision[case 485.5][update][estimate-ledger-tail]{ref:estimate-ledger-tail}
> ```

### Case 485.6 — The note of Slice 3g stands after the group of session start and `/hi`

> **given:**
> `entity-sprint-migration` — the sprint page; its Slice 3g holds the note on the old layout
> **＋** `vault/wiki/sprint.md` — the render of the sprint page
> **＋** `/hi` — builds the Frontier from `vault/wiki/sprint.md`
> **＋** `rule-session-start` — the rule of the group this Case recuts

> **when:**
> The next `/hi` builds the Frontier from `vault/wiki/sprint.md`, drawn from `entity-sprint-migration`.

> **then:**
> Slice 3g still shows the one unticked note on the old layout, and the Frontier holds it as a `C` line.
> **＋** The History of `entity-sprint-migration` says that the old-layout Estimates of session start and `/hi` are recut.
> **－** The note is not ticked or reworded: the Case that recuts the last group ticks it.

> **tasks:**
> - [ ] update `entity-sprint-migration`
>   - change: `Slice 3g: the old-layout Estimates of session start and /hi recut to one Criterion; the note on the old layout stands (case 485)`

> **ratification:**
> ```
> - decision[case 485.6][update][entity-sprint-migration]{ref:entity-sprint-migration}
> ```
