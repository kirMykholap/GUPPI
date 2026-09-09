# The harness, whole — as it stands on 2026-09-07

**One page, one topic: how the harness around a Claude Code session works in this repository.**
Written on the day the harness was split out of `job hunt ai`, from the files themselves —
`settings.json`, the hooks, the skills, the agents, the scripts, the Makefile and the vault's
schema — and not from the wiki's pages about them. Where a file's header and its code disagree,
the code is what is described and the disagreement is noted. It is the baseline the owner's new
plan is compared against, mechanism by mechanism: keep, remove, rework.

Every path is from the repository root. `$VAULT` is `job_hunt_ai_vault/`, found by every hook and
script as the top-level directory that holds a `wiki/`, never by name.

**Status words used below:** *live* — registered or callable and doing what it says; *off* —
still there, nobody runs it since 2026-09-07; *parked* — moved out of `wiki/` on 2026-09-07.

---

## 1. The life of a session — what fires, when

Everything that runs without being asked is a hook in `.claude/settings.json`, and every hook is
`powershell -NoProfile -ExecutionPolicy Bypass -File .claude/hooks/<name>.ps1`, reading one JSON
payload on stdin. `permissions.defaultMode` is `plan`, so a session opens in plan mode.

| moment | event · matcher | hook | what happens |
|---|---|---|---|
| session opens | `SessionStart` · startup, resume, clear, compact | `session-brief.ps1` | prints `$VAULT/brief.md` into the context; stamps the session id; rotates the ledger on `startup`; warns if commits landed since the brief was committed or a journal was never ingested |
| owner types a prompt | `UserPromptSubmit` | `remind-the-feedback.ps1` | counts prompts since the feedback file last changed; speaks after three quiet prompts or five silent replies |
| a page is read | `PreToolUse` · `Read` | `serve-the-rule.ps1` | if the file is under `wiki/` and carries `authority:`, names the `render: authority` rule with the same slug |
| a file is about to be written | `PreToolUse` · `Edit\|Write` | `ask-the-vault.ps1`, then `serve-the-rule.ps1` | the first says who writes this path and delivers the pre-task net on the session's first write; the second names the rule whose `governs:` is this path |
| a file was written | `PostToolUse` · `Write\|Edit` | `check-the-journal.ps1` | writes a `write` row to the ledger for every write; if the file is a journal under `raw/handoffs/`, runs the gate and reports |
| an agent is about to be dispatched | `PreToolUse` · `Agent\|Task` | `lock-the-librarian.ps1` | for `vault-librarian` only: runs the gate and **denies** the dispatch while it is red |
| an agent returned | `PostToolUse` · `Agent\|Task` | `record-the-dispatch.ps1` | writes `dispatch:<type>` to the ledger; `dispatch:pre-task` is what the harness counts as the ritual having run |
| a plan is about to be presented | `PreToolUse` · `ExitPlanMode` | `check-the-plan.ps1` | asks for `/pre-task` if none is on record since the last approved scope |
| a plan was approved | `PostToolUse` · `ExitPlanMode` | `check-the-plan.ps1` | writes `scope-approved` to the ledger |
| a skill is about to run | `PreToolUse` · `Skill` | `gate-the-handoff.ps1` | for `/handoff` only: **denies** it without a green `make smoke` behind it and nothing git-tracked written since |
| a skill ran | `PostToolUse` · `Skill` | `remind-the-smoke.ps1`, `remind-the-feedback.ps1` | on `/retro`: run `make smoke` now and again last; file a `VAULT-FEEDBACK` block every turn |
| a shell command ran | `PostToolUse` · `Bash` | `record-the-smoke.ps1` | if it was `make smoke` or `make suite`, writes `smoke:<exit code>` to the ledger from the `SMOKE-EXIT:` marker |
| the session's reply is displayed | `MessageDisplay` | `catch-the-feedback.ps1` | lifts fenced `VAULT-FEEDBACK` blocks out of the reply into `.superpowers/sdd/vault-feedback.md` |

**Two hooks refuse; everything else advises.** A refusal is a `permissionDecision: deny` in the
hook's output; advice is `additionalContext`, injected into the session. The two that refuse are
`lock-the-librarian.ps1` and `gate-the-handoff.ps1`, both on the owner's rule that a hook refuses
only an irreversible action and only when the refusal cannot be wrong.

**The ledger is the shared state.** `.superpowers/sdd/pre-task-ledger.tsv`, one TSV row per event:
`timestamp, session_id, event, permission_mode, flag, path`. Hooks append rows; `pre-task-state.ps1`
derives a per-session state from them (has a pre-task run, when was the last smoke and what did
it return, what was written after it, which rules were already served). It is rotated into
`.superpowers/sdd/ledger/` at every `startup`.

**The end of a session, as the files describe it:** `/retro` → `.superpowers/sdd/retro.md`;
`/handoff` → `$VAULT/raw/handoffs/<date>-<slug>.md`, draining the feedback file; `/ingest` →
the librarian compiles the journal into `wiki/`, writes the registers and the brief, archives the
journal; the session commits. Since 2026-09-07 none of this runs.

---

## 2. Hooks — `.claude/hooks/`, 14 files

Twelve are hooks. Two are libraries that are dot-sourced and must never be registered.

### `vault-path.ps1` — library · live
Exports `Find-Vault` (the first top-level directory holding `wiki/`) and `Find-Bash` (Git's own
`bash.exe`, found by walking up from `git`'s location, because the `bash` on PATH is the WSL shim
with no distro behind it). Used by `session-brief`, `ask-the-vault`, `serve-the-rule`,
`check-the-journal`, `lock-the-librarian`.

### `pre-task-state.ps1` — library · live
The ledger: its path (`JOBHUNT_PRETASK_LEDGER` overrides it for selftests), `Add-LedgerLine`,
the session stamp, rotation, and `Read-LedgerState`, which folds the rows of one session into a
state. Also the three questions the hooks ask of that state: is a pre-task owed for this plan, is
one owed for this write, and why `/handoff` is refused (`Get-HandoffRefusal`: no smoke, red smoke,
or tracked paths written after a green one — checked with `git check-ignore`). Reads
`.claude/hooks/messages/pre-task.md` to deliver the pre-task text. Its header says `/handoff` drains
the ledger; its line 159 says `/handoff` does not touch it — the second is what the code does.

### `session-brief.ps1` — `SessionStart` · live
Prints, never generates. Writes the transcript path to `.superpowers/sdd/session-transcript.path`,
stamps the session, rotates the ledger on `startup`, appends `session-start:<source>`. Then two
warnings, each in its own try: commits since the commit that last touched `brief.md` (the stamp
`generated-at:` is provenance for a human, not the test), and any `raw/handoffs/2*.md` lacking a
`.coverage.tsv` sidecar. Then the brief. Exits 0 on every path.

### `ask-the-vault.ps1` — `PreToolUse Edit|Write` · live · advisory
Classifies the path and says exactly one thing: a file under `raw/` is immutable; a page under
`wiki/` or `archive/` has one writer, the librarian (said once per session, never for a
`_schema.yaml`); a register is regenerated by `/ingest`; a `CLAUDE.md` is asked about with
`/vault-ask`; otherwise the path-scoped rules from `.claude/rules/*.md` whose `paths:` glob
matches. Under all of that, the **pre-task net**: on the session's first write it records
`first-write`, and if no pre-task is on record and no scope was approved, appends the pre-task
text once (`advised-write`). Its header calls the matcher narrow; the registration is every
`Edit|Write`, and the narrowing is inside the script.

### `serve-the-rule.ps1` — `PreToolUse Edit|Write` and `PreToolUse Read` · live · advisory
Two halves, exclusive. **By path, on a write:** scans the head of every `wiki/rules/*.md` for
`governs:` equal to the repo-relative path being written and names the rule with its page, saying
the text is rendered here and is changed on the page. **By slug, on a read:** if the file read is a
`wiki/` page carrying `authority:`, names every `status: current` rule with `render: authority`
and the same slug, exactly — nothing is resolved through `authority.md`. Silent on the six
registers and `archive/`, on a write inside `wiki/`, on a read outside it, and once a rule has
been served for that path this session (`served-rule` row). Never refuses.

### `check-the-journal.ps1` — `PostToolUse Write|Edit` · live · advisory
First, for every write, appends a `write` row with the path — this is the row the handoff gate
reads to know something was written after the smoke. Then, only if the path is a `.md` under
`raw/handoffs/`, runs `bash scripts/vault-check.sh` and reports a red gate as "fix it now, before
`/ingest`". Its header repeats "hooks are read at session start", which `gate-the-handoff.ps1`
records as false.

### `lock-the-librarian.ps1` — `PreToolUse Agent|Task` · live · **refuses**
Only when `subagent_type` is `vault-librarian`. Finds Git's bash; runs `bash scripts/vault-check.sh`;
on a non-zero exit denies the dispatch and quotes the gate's output minus advisory lines. When bash
cannot be found it advises to run the gate by hand and lets the dispatch through. Since the parking
of 2026-09-07 the gate is red on links, so the librarian cannot be dispatched — which matches the
owner's instruction that it is not to be.

### `check-the-plan.ps1` — `PreToolUse` and `PostToolUse ExitPlanMode` · live · advisory
Before a plan is presented: if no `dispatch:pre-task` row is newer than the last `scope-approved`
row, appends `advised-plan` and asks for the pre-task agent. After approval: appends
`scope-approved`. Advisory on the owner's ruling that exiting plan mode is reversible.

### `gate-the-handoff.ps1` — `PreToolUse Skill` · live · **refuses**
Only when the skill is `handoff`. Asks `Get-HandoffRefusal`; on a reason, denies with "the
condition is: the last `make smoke` of this session exited 0, and nothing git tracks has been
written since." When it cannot measure (no session id, unreadable ledger), it says so and lets the
skill through.

### `record-the-dispatch.ps1` — `PostToolUse Agent|Task` · live · silent
Appends `dispatch:<subagent_type>` with the dispatch's description. Writes in plan mode, which the
session cannot; that is why `dispatch:pre-task` is the evidence the state library reads.

### `remind-the-smoke.ps1` — `PostToolUse Skill` · live · advisory
On `/retro`: run `make smoke` early and in the foreground (a background run is recorded by
nothing), and again as the last thing before `/handoff`, because any tracked write — the
librarian's included — stales a green run. Its header says such a matcher was never registered in
this repository; `settings.json` registers it.

### `remind-the-feedback.ps1` — `UserPromptSubmit` and `PostToolUse Skill` · live · advisory
Never reads the prompt. Keeps its own state in `.superpowers/sdd/.feedback-silence`; reads the
feedback file's mtime and the reply counter `.superpowers/sdd/.reply-silence`. Speaks when three
owner prompts passed without the feedback file changing, or five replies filed no block. On `/retro`
demands a block in every turn, unconditionally.

### `record-the-smoke.ps1` — `PostToolUse Bash` · live · silent
If the command matched `make smoke` or `make suite`: a background launch gets one warning that
nothing was recorded; otherwise the last `SMOKE-EXIT: <n>` in the tool's response becomes a
`smoke:<n>` row. No marker, no row.

### `catch-the-feedback.ps1` — `MessageDisplay` · live · silent
Accumulates the reply's deltas per message id under `.superpowers/sdd/.message-display/`, parses at
`final`, keeps only depth-0 ```` ```VAULT-FEEDBACK ```` fences, splits records on `- kind:` lines
(`miss`, `measure`, `decision`, `harness`; an unknown kind is filed with a note; a `decision: the
owner said it` with no «» gets a note), appends them to `.superpowers/sdd/vault-feedback.md`, and
resets or increments `.reply-silence`. Files nothing in a turn where the feedback file shrank — that
is `/handoff` draining it. A `MessageDisplay` hook cannot inject context, so it prints nothing.

### `messages/pre-task.md` — generated · live
The pre-task text both advisories deliver. Generated by `scripts/vault-inject.sh` from the rule
page `a-pre-task-runs-between-the-plan-and-its-approval` (`render: whole`), banner on line 1.

---

## 3. Skills — `.claude/skills/`, 7

Sizes are bytes of `SKILL.md`; the share in brackets is text rendered from `wiki/rules/` pages
between `<!-- rule: -->` markers.

### `/vault-ask <question>` — 10,567 (37 % rendered) · live
`context: fork`, `agent: Explore`: a forked, empty-context reader, the only skill of that shape.
Reads `$VAULT/CLAUDE.md`, then folder → filename → tag (via `tags.md`) → full text, opening at most
ten pages; `bash scripts/vault-catalogue.sh` only to learn what exists; walks `[[links]]` and
`authority:` chains by `grep`. Returns Answer, Sources, Not in the vault, What could not be
narrowed. Writes nothing. The caller records `scripts/record-pre-task.ps1 -Kind vault-ask`, which
satisfies nothing about the pre-task ritual. Dispatched the librarian until 2026-08-30.

### `/retro` — 12,696 (6 %) · off since 2026-09-07
Step 0 runs `uv run python scripts/session-dialogue.py` → `.superpowers/sdd/session-dialogue.md`
(owner turns, replies, every menu with its answer, every feedback block). Builds the open-question
list from the extract, the session, what the owner raised, the feedback file (read, not drained)
and the brief's alarms; asks how to work it (menu); works it; every line ends `answered:`,
`deferred:` with a destination, or `could-not-close:`. Ratifies every attribution in one of three
shapes — he said it (verbatim Russian), he selected it (the option's label), the session understood
it (own voice, never signed). Copies `.claude/templates/retro.md` → `.superpowers/sdd/retro.md`
with a `→ handoff:` line per section. Then `/handoff`. The rendered rule demands a feedback block
every turn.

### `/handoff` — 7,194 (22 %) · off
Reads `.superpowers/sdd/retro.md` and routes each section by its `→ handoff:` line; copies
`.claude/templates/handoff.md` → `$VAULT/raw/handoffs/<date>-<slug>.md`; `commits:` is a resolved
range; every section stays, "none" is legal; drains `.superpowers/sdd/vault-feedback.md` into
*Feedback to the librarian* (`harness:` lines into *Harness*) and empties both `.superpowers` files
to their headers; never edits an existing journal; runs `bash scripts/vault-check.sh` (rule 8 judges
an uncompiled journal); then `/ingest`. Refused by `gate-the-handoff.ps1` without a green smoke.

### `/ingest` — 25,799 (1 %) · off
Dispatches `vault-librarian` once with a twelve-step instruction, one source at a time: split the
journal with `scripts/vault-units.sh`; give every unit a verdict in `<name>.coverage.tsv`
(`page:`, `journal`, `elsewhere:`, `skip:`); read the section-to-folder mapping from the
handoff template's `→ ingest:` lines; dispatch `decisions-agent` and `lessons-agent` in parallel
before writing; look every candidate up with `scripts/vault-authority.sh --near`; retire, never
delete; mark contradictions, never choose; `index.md` only on a structural change; `tags.md`;
append to `log.md`; compare the journal against `git log` and never edit it; regenerate `brief.md`
last; `vault-inject.sh`, `vault-check.sh`, `vault-coverage.sh`; `--lint`; archive the source with
`vault-archive.sh`. Then the session reviews the diff, samples ten `page:` verdicts, and commits —
"the commit is the session's and never the librarian's". A trailing comment says that commit step
owes a rule page.

### `/vault-lint` — 11,809 (0 %) · off
Once a sprint. `vault-check.sh --lint` (the only caller of `--lint`) and a coverage loop over
`raw/*/*.md`; a CRLF count with `tr -dc '\r' | wc -c`; `scripts/lessons-queue.py`, then a
librarian dispatch to group the queue into proposals (it writes `proposals/`, so it runs first);
`vault-archive.sh --dry-run --sweep`, then the sweep; a second librarian dispatch to audit
contradictions, stale `current`, missing pages, tag and index drift, brief growth.

### `/sprint` — 3,621 (0 %) · off
Open: a checkable goal and two to four acceptance criteria, written into `$VAULT/sprint.md` under
an incremented number. Close: on the goal, never on an empty backlog; a dropped item becomes a
`decisions/` page; the session never closes a sprint itself. It writes `sprint.md` directly while
`$VAULT/CLAUDE.md` names `sprint.md` a librarian-only register; neither file mentions the other.

### `/grill-me` — 1,857 (0 %) · live
An interview engine: maps a plan as a design tree, asks the whole frontier of answerable questions
in one numbered round with a recommended answer each, recomputes, repeats until the frontier is
empty. Environment facts are looked up by a sub-agent, never asked. Used by `/retro`.

---

## 4. Agents — `.claude/agents/`, 4

Every agent file carries the rendered rule `the-shared-reading-discipline-renders-into-every-agent-that-reads-the-vault`
(3,940 bytes, identical in all four and in `/vault-ask`): read `$VAULT/CLAUDE.md` first, folder
first, open at most ten pages, never a whole folder.

### `vault-librarian` — 11,308 bytes (42 %) · off, and locked out while the gate is red
`tools: Read, Grep, Glob, Bash, Write, Edit, Agent`. **The only writer of `wiki/` and the
registers.** Answers a topic query by folder — entities, decisions, concepts, lessons — then
Sources and Not in the vault. On a ritual it dispatches `decisions-agent` and `lessons-agent`,
waits, writes, returns once. Before any new page: `scripts/vault-authority.sh --near <slug>`. At
the end of a writing pass: `vault-inject.sh`, then `vault-check.sh`, fix everything. Never deletes
text, never resolves a contradiction, never closes a sprint, never writes the feedback file or the
brief by hand. Dispatched by `/ingest` once and `/vault-lint` twice.

### `pre-task` — 10,144 bytes (39 %) · off
`tools: Read, Grep, Glob, Bash`. Reads only. Phase 1: `bash scripts/vault-catalogue.sh`; drop
`lessons`; from `decisions` keep `binding: prohibition` and `deferral`; keep `concepts`,
`entities`, `proposals`, `rules` whole; match plan items against title and authority — "an
enumeration, never a search". Phase 2: read the shortlist in full, walk links, verify cheap claims
against the tree. Returns per plan item what constrains, contradicts and supports it, then what the
enumeration could not see, the two counts, Sources, Not in the vault. Since the parking there is
no `decisions/` under `wiki/`, so phase 1 enumerates the 162 live pages only.

### `decisions-agent` — 8,742 bytes (45 %) · off
`tools: Read, Grep, Glob, Bash`. Reads only; the librarian dispatches it. Two modes: the decisions
carried by one journal (every ingest) or the whole folder (on demand). One row per decision:
`stands`, `carried` by a live page, `false`, `undesigned` (a deferral with nothing behind it), or
`contradicts <slug>` under a different authority. Its folder, `wiki/decisions/`, is parked.

### `lessons-agent` — 6,968 bytes (57 %) · off
`tools: Read, Grep, Glob, Bash, Write`. Groups `wiki/lessons/` by meaning against `rules/` and
`proposals/`, drafts one proposal per group into `docs/` — its `Write` is for that alone — and
names the lessons each would retire. Rejects singletons out loud.

---

## 5. Scripts — `scripts/`, 18

Every vault script finds `$VAULT` the same way the hooks do, overridable by the `VAULT`
environment variable, and prints with a prefix of its own name. Grouped by what they are for.

### The gate and its selftests

**`vault-check.sh`** (1,945 lines) · off — **the gate.** `bash scripts/vault-check.sh [--lint] [--rules]`.
Reads every page under `wiki/`, every `wiki/*/_schema.yaml`, the registers, `archive/` for link
targets, `raw/handoffs/` against the handoff template, both `CLAUDE.md` files and `.claude/**/*.md`
for rendered regions. Prints one `VAULT-CHECK:` line per violation; `ok` on green; exit 1 on any
red verdict. `--lint` adds advisories that never change the exit code; `--rules` prints the rule
register and touches nothing. Runs three other scripts as rules: `vault-inject.sh --check` (12),
`vault-authority.sh --orphans --check` (13), `vault-measure.py --check` (15), reading their lines
and never their exit codes. Called by `make gate`, `lock-the-librarian.ps1`, `check-the-journal.ps1`,
`vault-archive.sh` after every move, `/handoff`, `/ingest`, `/vault-lint`, the librarian.

Its rules, as `--rules` prints them (red sets exit 1; advisory prints and passes):

| rule | what it decides | verdict |
|---|---|---|
| 1 | the folders and the five top-level files exist | red |
| 2 | frontmatter against the folder's `_schema.yaml`: required keys, no unknown keys, values in `values:`, `type` equals the folder, `decided:` on decisions, every `sources:` path exists, 2–4 tags, the rule-page conditions on `governs:`/`authority:`/the slice | red |
| 3 | no two `current` pages of one type share `authority:` | red |
| 4, 5 | every `[[wikilink]]` in `wiki/`, `archive/` pages and the registers resolves; no `wiki/` page is an orphan | red |
| 5b | wikilinks in the repository's `CLAUDE.md` resolve | red |
| 5c | `decided_by:` names a page of type decision; `status: idea` pairs with a `deferral` | red |
| 6 | every tag on a page is in `tags.md` | red |
| 7 | a registered tag used nowhere; under `--lint`, a tag selecting more than ten pages in one folder | advisory |
| 8 | each journal in `raw/handoffs/` keeps every section of the template | red |
| 9 | retired 2026-08-17, number never reused | — |
| 10 | a title carries no measurable quantity (red); a filename carries none (advisory) | red / advisory |
| 11 | region markers in harness files are well formed, one slug per file, and resolve to a current rule whose `governs:` names the file; prints the coverage figure | red |
| 12 | `vault-inject.sh --check` says every rule agrees | red |
| 13 | `vault-authority.sh --orphans --check`: every page outside `rules/` carries a slug and the register agrees with the tree | red |
| 14 | a block signed `owner:` carries Cyrillic (`--lint` only) | advisory |
| 15 | `vault-measure.py --check`: every measure region is well formed | red |
| 16 | a decision or proposal created on or after the schema's `lifecycle_from` carries its declared sections and fields | red |
| 17 | a decision with `target_kind: rule` or `proposal` whose target exists is named back in that page's `decided_by:` | red |
| `--lint` | proposals and rules with no `decided_by:`; retired pages still linked from live ones | advisory |

**Run once on 2026-09-07 after the parking, to measure and not to obey — exit 1 in 22 s, 698
lines:** rule 1, the two folders missing under `wiki/` (2); rule 2, `sources:` paths that left with
the product or the parking (9); rule 4, broken wikilinks into `parked/` (334); rule 5, orphans
(5); rule 13, slugs `authority.md` groups that no live page carries (337); ten advisories. That is
the parking counted, not a defect list.

**`vault-check-selftest.sh`** (3,363 lines) · off — breaks every rule on purpose in a throwaway copy of
the vault and asserts the gate names it. `--list` sweeps the case names; `--only <substring>` runs a
slice; `SCRIPTS=<dir>` tests a candidate script set. Prints `SELFTEST: caught N, missed N`; about
an hour whole. Called by `make suite` and `make smoke ONLY=`.

**`hook-selftest.ps1`** (2,103 lines) · off — the same for the hooks: copies twelve of them, the gate,
the catalogue and the handoff template into a sandbox project with a vault named `a vault with
spaces`, drives every branch, prints `HOOK-SELFTEST: caught N, missed N`. Hangs when run from
`make` with stdin inherited, which is why every recipe closes it. Called by `make smoke`.

**`vault-measure-selftest.py`**, **`session-dialogue-selftest.py`** · off — cases for the two Python
tools below, temp dirs only. Called by `make smoke`.

### Tools over the vault

**`vault-inject.sh`** (619 lines) · off — **the injector.** `bash scripts/vault-inject.sh [--check]`.
Opens only pages carrying `governs:`; writes each one's `<!-- text -->` slice between
`<!-- rule: slug -->` markers in the governed file (`render: region`) or generates the whole file
under a banner (`render: whole`), and deletes a generated file whose page is no longer current.
Refuses a slice holding a wikilink, two slices, an empty one, a `render:` it does not know, a
`governs:` written as a block list. `--check` writes nothing and prints every disagreement — that
is rule 12. No `make` target on purpose: it mutates tracked files.

**`vault-archive.sh`** (637 lines) · off — **the archiver.** Moves files into
`archive/<date>/<session>/<kind>/`, rewrites every `sources:` line that cited them (never prose),
sets `status: archived` on the way, runs the gate afterwards. Named mode: `<date> <session> <kind>
<file>...`, kinds `handoffs plans specs notes pages`. `--sweep` selects its own list from
`decisions/`, `lessons/`, `proposals/`, `rules/` — never `entities/` or `concepts/`. Refuses a page
no live page names, a `deprecated` page without a live successor, a `repealed` or `refused` page
without `decided_by:`, and any `target_kind: repeal` decision, absolutely. `--dry-run` says what it
would do.

**`vault-authority.sh`** (381 lines) · live — the index of `authority:` slugs against
`authority.md`. `--near <slug>` is the lookup the admission rule names (the family a candidate
belongs to); `--check` compares register and tree both ways (rule 13); `--orphans` names pages with
no slug; `--group`, `--list`, `--binding`, `--trace`. Prints only.

**`vault-catalogue.sh`** (136 lines) · live — every page under `wiki/`, one row per page from the
frontmatter, a table per folder with counts. The agent-readable twin of `pages.base`. Stopped
printing `archive/` on 2026-08-30. `/pre-task` phase 1 and `/vault-ask` read it. 32,957 bytes today.

**`vault-coverage.sh`** (198 lines) and **`vault-units.sh`** (81 lines) · off — the ingest's
denominator. `vault-units.sh` splits a journal into claim-sized units, one per line;
`vault-coverage.sh <journal>` reads the sidecar `<journal>.coverage.tsv` and says `INGEST COMPLETE`
or names the units with no verdict or an illegal one.

**`vault-measure.py`** (489 lines) · off — the only writer of `<!-- measure -->` regions: a
*gauge* is a subject and a command whose reading is written by `--refresh`, a *testimony* is a past
reading appended and never replaced. `--check` is rule 15 and executes nothing. Named by no skill,
agent or rule.

### Tools for a session

**`session-dialogue.py`** (428 lines) · off — extracts one session's dialogue from its transcript:
owner turns, replies, every menu with its answer, every feedback block. Writes
`.superpowers/sdd/session-dialogue.md`. Finds the transcript through the path
`session-brief.ps1` left. Step 0 of `/retro`.

**`record-pre-task.ps1`** (83 lines) · live — the command a session runs to record a `pre-task` or a
`vault-ask` into the ledger, because both used to be librarian dispatches that nothing told apart.
Exit 1 when no session stamp exists.

**`lessons-queue.py`** (122 lines) · off — the lessons nothing cites: `CITED` (a rule, proposal or
decision names it) and `LANDED` (a rule names it). Reads `decisions/` as a citer, which is now
parked. Called by `/vault-lint`.

**`build-families-table.py`** and **`build-family-rules.py`** (267 and 230 lines) · off — the
cleanup's two generators: the first prints the families table into `docs/vault-cleanup-families.md`
from `authority.md`, the tree and the hand-written verdicts in `docs/vault-cleanup-verdicts.md`; the
second drafts one `wiki/rules/` page per `vault-facing` family from `decisions/` — a script that
writes into `wiki/`, run inside the librarian's dispatch on 2026-08-31. Both read
`job_hunt_ai_vault/authority.md` by its hard-coded name and `decisions/` under `wiki/`, which is
parked. Run by hand, called by nothing.

---

## 6. The vault — `job_hunt_ai_vault/`

**One writer, the librarian, for `wiki/` and the registers; the session writes the vault's
`CLAUDE.md` and the six `_schema.yaml` files, because those are what the gate reads as its own
input.** Retrieval is `ripgrep` plus `[[wikilinks]]`; the filename is the address and part of the
search surface; nothing is ever deleted, a replaced page is deprecated and moved.

### Folders under `wiki/` — the live ones, on 2026-09-07

| folder | pages | what belongs there |
|---|---|---|
| `entities/` | 44 | what exists and what it is like — a module, a script, a hook, an external system; a functional requirement |
| `rules/` | 35 | text delivered somewhere else rather than remembered: rendered into a file by `governs:`, or served by lookup on `authority:` |
| `lessons/` | 31 | what was learned the hard way — a failure class, a cost, a platform trap; a measurement lives here with `basis: measurement` |
| `proposals/` | 52 | what was raised or deferred and **not built**; never a record of something that exists |

**Parked on 2026-09-07 into `parked/`, schemas with them:** `decisions/` (218 — what was chosen,
when, why, what was rejected, what it obliges; a deferral is a decision too) and `concepts/` (147 —
how a mechanism is built and why; a non-functional requirement), plus three product entities and
one product rule.

### Frontmatter — the fields the gate reads

| field | where | values | meaning |
|---|---|---|---|
| `title` | all | free text, no measurable quantity, unbounded length | the claim |
| `type` | all | the folder's singular | must match the folder |
| `status` | all | `current`, `deprecated`, `archived`; proposals add `implemented`, `refused`, `idea`; rules add `repealed` | `deprecated` obliges the page to leave `wiki/`; `archived` is written by the archiver as it moves; the rest are causes a page leaves for |
| `authority` | required everywhere but `rules/`, optional there since 2026-08-30 | a slug, unique among `current` pages of one type | the question the page alone answers; the index looked up before a page is written |
| `basis` | all | `human`, `code`, `measurement`, `external`, `inference` | what the page rests on; ranks conflicts |
| `sources`, `sprint`, `created`, `tags` | all | paths or links; `S1`…; date; 2–4 registered tags | provenance; origin, not membership; date; subject |
| `decided`, `binding` | decisions | date; `prohibition`, `deferral`, `divergence` | when; what it does to a reader — absent reads as prohibition |
| `target_kind`, `target` | decisions from 2026-08-30 | `rule`, `proposal`, `action`, `repeal`, `none`; plain-text slug | the forward half of the handshake rule 17 checks |
| `decided_by` | required in rules, optional in proposals | exactly one wikilink to a decision | the decision that caused the page |
| `render` | rules | `region`, `whole`, `authority` | how the rule is delivered — see below |
| `governs`, `paths` | rules | a path from the repository root or an inline list; globs | where a region or whole file is written; the scope of a whole file |
| `supersedes`, `superseded_by`, `updated` | optional | wikilinks; date | supersession is a relation written both ways |

Body sections are schema too, from `lifecycle_from: 2026-08-30`: a decision carries `# Context`,
`# The question`, `# How it works after`, `# Recommendation`, `# Ratification`; a proposal carries
`# Decisions` with one checkbox per decision it must close.

### The three ways a rule is delivered

- **`render: region`** (15 pages) — the slice between `<!-- text -->` markers is written by the
  injector between `<!-- rule: slug -->` markers in every file `governs:` names. The file keeps its
  own skeleton; the page owns the text; the gate reads the two and calls a difference drift.
  28,178 bytes of slice today, 8,237 of them inside `CLAUDE.md`, which is 77 % of that file.
- **`render: whole`** (1 page today, 2 before the split) — the destination file is generated end
  to end under a banner and deleted when the page stops being current.
  `.claude/hooks/messages/pre-task.md` is the one left; the other was
  `.claude/rules/ast-boundaries.md`, gone with the product.
- **`render: authority`** (19 pages, minted 2026-08-30) — written into no file. The page carries
  `authority:` and no `governs:`; `serve-the-rule.ps1` names it when a `wiki/` page with the same
  slug is read. Eighteen were generated on 2026-08-31 from the eighteen `vault-facing` families of
  prohibitions, one clause per decision title, and 129 of those decisions went to `archive/`; the
  nineteenth is the rule about rules itself. Costs nothing until served.

### Top-level files

| file | what it is | writer |
|---|---|---|
| `CLAUDE.md` | the vault's schema in prose: who writes what, the layout, how to choose a category, every field, status and supersession, authority, binding, titles, tags, contradictions | the session; the owner reads the diff |
| `harness-map.md` | this page | the session, 2026-09-07 |
| `brief.md` | what a session starts from; printed by `session-brief.ps1`; regenerated at every ingest, never a source — hand-written on 2026-09-07 | the librarian; the session this once |
| `index.md` | map of the territory: categories, naming, hub pages; lists no pages | the librarian |
| `tags.md` | the tag dictionary with Russian aliases, which is how a question in one language reaches a page in another | the librarian |
| `authority.md` | the families of `authority:` slugs — which slugs answer the same question, which the tree cannot say | the librarian, by hand |
| `log.md` | the librarian's actions and the misses reported against it, append-only | the librarian, and the archiver's sweep |
| `sprint.md` | the open sprint and the closed ones; the frontier between sessions | the librarian, through `/sprint` |
| `pages.base` | an Obsidian base — a query over `wiki/`, evaluated when opened; only Obsidian reads it | Obsidian, when the owner filters |
| `wiki/*/_schema.yaml` | per-folder field sets and legal values, read by rule 2 | the session |

### Outside `wiki/`

- **`raw/`** — the inbox, immutable once written: `handoffs/` (empty — every compiled journal was
  archived), `notes/` (the owner's two notes of 2026-08-13 on the second brain, with sidecars),
  `plans/`, `specs/` (empty). Validated by no schema, swept for no links.
- **`archive/`** — history: `archive/<date>/<session>/<kind>/`, nineteen dated sessions from
  2026-08-12 to 2026-08-31, plus 29 flat retired pages from before the dated form. Link targets
  resolve into it; its `pages` are link-swept; the catalogue does not print it; `/pre-task` does not
  read it.
- **`parked/`** — since 2026-09-07: set aside, not retired. See section 8.

---

## 7. `Makefile`

| target | runs | status |
|---|---|---|
| `help` | lists the targets with their `##` comments | live |
| `gate` | `bash scripts/vault-check.sh` | off — red on links into `parked/` |
| `style` | `uv run ruff check scripts` | live, clean |
| `smoke` | `gate`, `style`, `hook-selftest.ps1`, `session-dialogue-selftest.py`, `vault-measure-selftest.py`, each with `< /dev/null`; `ONLY=<pattern>` adds a slice of the gate's selftest | off |
| `suite` | `smoke` plus the whole `vault-check-selftest.sh`, about an hour | off |

Every recipe closes its own stdin: a PowerShell child spawned from `make` with stdin inherited
hangs, measured at forty-nine minutes once. `test` left with the product on 2026-09-07.

---

## 8. State on 2026-09-07

- **Live and doing what it says:** all fifteen hook registrations; `/vault-ask`; `/grill-me`;
  `make style`; every script when invoked by hand.
- **Off — present, registered or callable, run by nobody:** the gate and the three selftests
  (`make gate`, `make smoke`, `make suite`); `/retro`, `/handoff`, `/ingest`, `/vault-lint`,
  `/sprint`; the four agents. The librarian is refused by `lock-the-librarian.ps1` while the gate is
  red, which it is on links into `parked/`.
- **Parked, under `$VAULT/parked/`:** `decisions/` (218), `concepts/` (147), three product
  entities, one product rule. `wiki/` holds 162 pages: entities 44, rules 35, lessons 31,
  proposals 52.
- **Left with the product in `job hunt ai`:** `src/`, `tests/`, the migrations and docker files,
  `.claude/rules/ast-boundaries.md`, two capture scripts, `make test`.
- **Known false and left so:** the product paragraph at the top of `CLAUDE.md` (rendered from a
  rule page, corrected there); the registers, which still list parked pages; every `[[wikilink]]`
  from `wiki/` into `parked/`.
- **The hooks will keep asking for the ritual.** `check-the-plan` at every plan, `ask-the-vault` at
  the first write, `remind-the-feedback` every three quiet prompts. Advisory, expected, and the
  owner's decision of 2026-09-07 is the answer to all of them until the new plan says otherwise.
