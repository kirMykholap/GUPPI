<!-- approved 22:16:18 · session 19b07bbc -->

# Spec — session L, 2026-09-13, hi 06:52

## Work without a decision

F1, F2, F3 of the Frontier: no Case, no ledger `decision` line; the readings are written as `estimate[...]` lines the moment they exist.

```tasks
- [x] F1: commit the three governed files `render --sync` wrote at session start — `.claude/settings.json`, `.claude/agents/librarian-guppi.md`, `.claude/skills/pre-task/SKILL.md` — `feat(harness): render of rule-settings, cases 89.1, 90.2, 90.3` (44e4e37)
- [x] F3: read `estimate-case-protocol-loaded` against this session start
- [x] F3: read `estimate-render-sync-reports` against this session start (three files reported and written, exit 0 at `render --check`)
- [ ] F2: read `estimate-settings` against the librarian's run of session K — waits for the next session start (the session-start line from the rendered file)
- [x] F2: read `estimate-permissions` — after the first tick of this Spec in Work Mode
- [x] F2: read `estimate-default-mode`
- [x] F2: read `estimate-hook-registry-rendered`
- [ ] F2: read `estimate-documentation-completes` — against this session's librarian run (89.1 took effect at this start)
- [ ] F2: read `estimate-close-commits` — against this session's librarian run
- [x] F2: read `estimate-render-harness-reproduces`
- [x] F2: read `estimate-claude-md-rendered`
```

## Case 100 — the archive of an applied `raw/`

> **context:**
> Case 95 (Slice 3c, deferred four times: 45, 63, 79, 95) is the lifecycle of `raw/`. Today `raw/` holds four dates: 4 ledgers (529 lines), 4 yamls (21 911 lines), the session folders. Every librarian run walks every date again: `materialize` reads 4 ledgers and every Spec, `generate` 4 yamls, and prints "extended with 0 entries", "0 pages". Case 95 bundles six things; this Case takes one, the archive of an applied unit of `raw/`, and leaves the tail `/hi` prints and `decided_by` to their own Cases. Shown again twice in the session: for the root `vault/archive/` (case 102) and for the ledger of a session (case 103).

> **problem:**
> Nothing says when a unit of `raw/` is done with, and nothing takes it away. The `origin` of every page (`raw/<date>/ledger.md#case-N`) points in, lint checks it, `rule-cleanup` and `index.md` §1 say "`raw/` stays". The migration plan meant a move "by run stamp with every path rewritten": 82 pages point at 2026-09-09 alone, plus History lines and `log.md`.

> **given:**
> Ask-guppi: no live or archived page is about the archive of `raw/`; `rule-raw-archive` and `estimate-raw-archive` are free; the tags `harness`, `librarian`, `ledger` are registered.
> **＋** `rule-ledger-tail` (`draft`, placeholder, `deferred_by: decision-case-95`) is about the tail, not the archive; this Case takes 95 up (`{supersedes:case 95}` on 100.1); the tail is Case 101.
> **＋** Pointers into `raw/`: `origin: raw/<date>/ledger.md#case-N` on the pages of Cases, `#L<n>` on 48 lessons and readings, 318 History lines with `#L<n>`, `line`/`folded`/`unparsed` in the yaml — all by line number; §4 of `index.md`: a ledger line is never edited or deleted. So no file is cut and no pointer is rewritten: a ledger keeps its name, lint resolves it in `raw/` or in the archive (103.5).
> **＋** Readers: `materialize` and `generate` walk `vault/raw/` only — an archived unit leaves the walk by itself; `lint.check_origin` (`guppi/lint.py:289–314`) is the one place the path is resolved; `ledger.session_event_logs` walks `event_log.md` back to a `session-start`; `ledger.existing_bodies` (the dedupe) reads the ledgers under `raw/`; `pretask` reads the session folder of the day.
> **＋** A supersedes across dates goes through pages (`generate.py:601` sets `superseded_by` on `decision-case-N`), not through the earlier yaml; `materialize.mark_superseded` marks entries of its own yaml only.
> **＋** After case 103 the unit of `raw/` is the session folder `raw/<date>/<HHMM>/` with its own `ledger.md` and `materialize.yaml`; a date-level `raw/<date>/ledger.md` with its yaml (the shape before 103) is a unit of its own, with the `<HHMM>/` folders of that date that have no ledger of their own.
> **＋** In `raw/` today: 09-09, 09-10, 09-11, 09-12, all date-level — every yaml entry `applied`, no ledger line outside its yaml (checked 2026-09-13 with `parse_line`: 74/90, 157/151, 84/78, 244/210 entries/lines, 0 kept); 09-13 will hold both shapes. `raw/notes/`: four files of August (two owner's notes, two `.coverage.tsv`), referenced only by the handoffs of the old `vault/archive/2026-08-*` (removed by 102.1).
> **＋** The archive root is `vault/archive/` (case 102): `<sprint>/<date>/<HHMM>/<category>/<slug>.md` for pages, `<sprint>/<date>/<HHMM>/raw/` for a session's raw, `<sprint>/<date>/raw/` for a date-level ledger; `<sprint>` the first `## <id>` of `sprint.md` (`materialize.sprint_id`).
> **＋** `rule-cleanup` Purpose: "`raw/<date>/` stays where it is: every `origin` points into it and lint checks that path"; `rule-documentation` (`render_mode: full`): steps 1–4, the frame forbids the librarian to read the archive (90.3) — running a script is not a read.
> **－** `.gitignore` does not change: `event_log.md` does not move (the `hi` window of the hook across midnight); a `raw/<date>/` with one gitignored file is empty for git.
> **－** `rule-brief`, `rule-close`, `rule-materialize`, `rule-page-generation` do not change for the archive; `git add vault` picks the move up.
> **－** The session of the run never moves, nor any unit dated the day of the run: after the librarian's commit Retro and the readings still write into the session's ledger.
> **－** A failed entry is fixed by hand in `raw/` (the Spec or the yaml, in Plan Mode) or by a superseding Case; the librarian never repairs (90.3).

### Case 100.1 — `rule-raw-archive`, the script

> **when:**
> `uv run guppi archive` runs — the librarian's fifth step, or by hand.

> **then:**
> A unit is a session folder `raw/<date>/<HHMM>/` holding a `ledger.md`, or a date-level `raw/<date>/ledger.md` with its yaml. A unit is done when its yaml exists, every entry under `entries` carries `applied` or `superseded_by`, and the number of every line of its `ledger.md` that `materialize.parse_line` reads as a record is in the `line` or `folded` of some entry or under `unparsed`.
> **＋** Only units whose date is before the day of the run are looked at; the session of the run never — found as `cleanup` finds it, the latest `<HHMM>/` folder of the run day, else the nearest date back, and skipped even when dated before the run day.
> **＋** A done session moves whole to `vault/archive/<sprint>/<date>/<HHMM>/raw/`. A done date-level ledger moves with its yaml and everything else at the date root to `vault/archive/<sprint>/<date>/raw/`, and with it every `<HHMM>/` folder of the date that has no ledger of its own, each to `vault/archive/<sprint>/<date>/<HHMM>/raw/`. No file is cut.
> **＋** `event_log.md` stays in `vault/raw/<date>/`.
> **＋** Stdout, one line per unit: `archive: raw/<date>/<HHMM> → archive/<sprint>/<date>/<HHMM>/raw`, `archive: raw/<date> → archive/<sprint>/<date>/raw`, or `archive: raw/<date>[/<HHMM>] kept: <reason>` — `no yaml`, `N entries not applied`, `N ledger lines outside the yaml`.
> **＋** Exit 0; a name already taken in the archive or a move that fails is a line on stderr, exit 1, the other units still move. A rerun moves nothing and exits 0.
> **－** `origin`, History, `log.md` and the yaml are not rewritten.
> **－** A folder without `ledger.md` is not a unit; a date-level unit dated the day of the run is not looked at.
> **－** An entry that a supersedes from another unit did not mark keeps its unit in `raw/`; that gap is `rule-materialize`'s, not this rule's.

```then
create:
  - slug: rule-raw-archive
    type: rule
    kind: Leaf
    purpose: Keeps raw/ to the sessions not yet turned into pages, by moving an applied session whole into the archive
    enforcement: check
    implementation_ref: [guppi/archive.py, tests/test_archive.py]
    tags: [harness, librarian, ledger]
    sections:
      Purpose: |
        Keeps `raw/` to the sessions that are not yet fully turned into pages. A session
        whose `materialize.yaml` is applied to the last entry and whose `ledger.md` has no
        line outside the yaml is done; nothing reads it again, so it moves whole into the
        archive of its date. A session with an entry still to apply stays, and is named
        with the reason, so the debt is in view at every run until the entry is fixed in
        Plan Mode.
      How it works: |
        `uv run guppi archive` looks at every unit of `vault/raw/` whose date is before
        the day of the run: a session folder `raw/<date>/<HHMM>/` holding a `ledger.md`,
        or a date-level `raw/<date>/ledger.md` with its yaml (the shape before case 103).
        The session of the run is never looked at. A unit is done when its
        `materialize.yaml` exists, every entry under `entries` carries `applied` or
        `superseded_by`, and every line of its `ledger.md` that `materialize.parse_line`
        reads as a record has its number in the `line` or `folded` of an entry or under
        `unparsed`. A done session moves whole to
        `vault/archive/<sprint>/<date>/<HHMM>/raw/`; a done date-level ledger moves with
        its yaml and everything else at the date root to
        `vault/archive/<sprint>/<date>/raw/`, and with it every `<HHMM>/` folder of the
        date without a ledger of its own, each to
        `vault/archive/<sprint>/<date>/<HHMM>/raw/`. `<sprint>` is the first `## <id>`
        heading of `sprint.md`. `event_log.md` stays in `vault/raw/<date>/`: it is
        gitignored and the ledger hook walks it for the `hi` window. No file is cut and no
        pointer is rewritten: `raw/<date>/<HHMM>/ledger.md#case-N`, the date form and
        `#L<n>` stay the name of a ledger, which lint resolves in `raw/` or in the archive.

        Stdout carries one line per unit, `archive: raw/<date>/<HHMM> →
        archive/<sprint>/<date>/<HHMM>/raw`, `archive: raw/<date> →
        archive/<sprint>/<date>/raw`, or `archive: raw/<date>[/<HHMM>] kept: <reason>` —
        `no yaml`, `N entries not applied`, `N ledger lines outside the yaml`. A name
        already taken in the archive or a move that fails is a line on stderr and exit 1;
        the other units still move. A rerun moves nothing and exits 0. A folder without
        `ledger.md` is not a unit. An entry that a supersedes from another unit did not
        mark keeps its unit in `raw/`; that gap belongs to `rule-materialize`. The
        coverage of a line is the one function `guppi tail` uses ([[rule-ledger-tail]]).
    method: |
      Unit, `tests/test_archive.py`: a fixture vault with a date-level date applied to the
      last entry and fully covered, holding a `<HHMM>/` folder without a ledger; a session
      folder applied and covered; a session with a `failed` entry; a session with a record
      line outside its yaml; a session dated today; and a folder without `ledger.md`. One
      run moves the date-level unit to `<date>/raw/` and its session folder to
      `<date>/<HHMM>/raw/`, the done session to `<date>/<HHMM>/raw/`, leaves every
      `event_log.md` behind, keeps the other three with the reason on stdout, exits 0; a
      name already taken in the archive is a stderr line and exit 1 while the other units
      move; a rerun moves nothing and exits 0. Live, 2026-09-13: `uv run guppi archive`
      over the four date-level dates of `raw/`, then `make lint` — the four dates under
      `vault/archive/migration/<date>/raw/` with their session folders beside, `raw/`
      holding only today and the four `event_log.md`, lint's `origin` findings unchanged
      from before the move; a change in lint's count fails the reading and the move is
      reverted with `git checkout`.
```

```tasks
- [x] `guppi/archive.py`: `units(project_dir)` (session folders with a ledger, date-level ledgers), `uncovered_lines(unit) -> list[tuple[int, str]]` (record lines not named by the yaml — shared with `tail`), `done(unit)`, the whole-unit move with `event_log.md` left behind and the ledger-less `<HHMM>/` folders of a date-level unit, the stdout lines, stderr and exit 1 on a taken name or a failed move; reuse `materialize.load_yaml`, `materialize.parse_line`, `materialize.sprint_id`
- [x] `guppi/cli.py`: register `archive`
- [x] `tests/test_archive.py`: the fixture of six units, the checks of the method
- [x] `make style`, `make test`
- [x] read `estimate-raw-archive`: unit, then live over the four dates with `make lint` before and after; revert with `git checkout vault/raw vault/archive` on a changed lint count
```

### Case 100.2 — the fifth step of the librarian

> **when:**
> The librarian works by its frame (the Render of `rule-documentation`).

> **then:**
> A step between Brief and Close (shown again at pre-task: the brief reads the yamls the walk named, so the archive runs after it): "Archive. Run `uv run guppi archive`. Every line on its stderr is a flag; the units it moved and the units it kept, with the reason, go into the report." The brief is already written; the commit picks the move up.
> **＋** `rule-raw-archive` is the sixth child of `rule-documentation`, after `rule-cleanup`.
> **＋** The ban on reading `vault/archive/` stays.
> **＋** The session of the run is found as `cleanup` finds it — the latest `<HHMM>/` folder of the run day, else the nearest date back — and is skipped even when dated before the run day (a session across midnight).
> **＋** `estimate-documentation-completes` gets a `### case 100.2` block, `pending`.

```then
update:
  - slug: rule-documentation
    contract: changed
    set: {children: [rule-materialize, rule-index-check, rule-synthesis, rule-page-generation, rule-cleanup, rule-raw-archive, rule-brief, rule-close]}
    replace:
      - old: "<!-- rule-brief -->\n\n<!-- rule-close -->"
        new: "<!-- rule-brief -->\n\nArchive. Run `uv run guppi archive`. Every line on its stderr is a flag; the units it\nmoved and the units it kept, with the reason, go into the report. The session of the\nrun is never moved.\n\n<!-- rule-close -->"
    change: "the archive step between brief and close, after the brief has read the yamls; rule-raw-archive the sixth child (case 100.2)"
```

```tasks
- [ ] read `estimate-documentation-completes` (100.2): the librarian's run of this session, step 5 in the report and the brief
```

### Case 100.3 — lint resolves `origin` in the archive

Superseded by 103.5 in this session; the item below keeps the line's place, the wording is 103.5's.

> **when:**
> `uv run guppi lint` checks an `origin` of the form `raw/<date>/ledger.md#case-N` or `#L<n>`.

> **then:**
> The ledger of the date is looked for in `raw/`, then in the archive; see 103.5.

```then
update:
  - slug: rule-lint
    contract: changed
    change: "origin resolves in raw/ or the archive (case 100.3, superseded by 103.5 which carries the wording)"
```

```tasks
- [x] read `estimate-lint-catches` (100.3): covered by the reading of 103.5, which replaces this block
```

### Case 100.4 — `rule-cleanup` no longer says `raw/` stays

> **when:**
> Someone reads `rule-cleanup`.

> **then:**
> The sentence "`raw/<date>/` stays where it is: …" is replaced by "`raw/<date>/` is not this script's: `guppi archive` moves an applied session (`rule-raw-archive`)."
> **－** The behaviour of `cleanup` does not change; `contract: same`.

```then
update:
  - slug: rule-cleanup
    contract: same
    replace:
      - old: |-
          `raw/<date>/` stays
          where it is: every `origin` points into it and lint checks that path.
        new: |-
          `raw/<date>/` is not
          this script's: `guppi archive` moves an applied session ([[rule-raw-archive]]).
    change: "raw/ is guppi archive's, not cleanup's (case 100.4)"
```

```tasks
- [ ] check `rule-cleanup` after the librarian's run: the sentence replaced (100.4)
```

### Case 100.5 — `index.md` and the glossary

Superseded by 103.6 in this session, which holds the whole text of both files; the items below keep the lines' place.

> **when:**
> Someone reads `index.md` §1 or the glossary row `archived`.

> **then:**
> The text is 103.6's.

```then
update:
  - slug: index
    file: vault/wiki/index.md
    change: "superseded by case 103.6, which carries the text"
  - slug: glossary
    file: vault/wiki/glossary.md
    change: "superseded by case 103.6, which carries the text"
```

```tasks
- [x] nothing of its own: the edits of `index.md` and `glossary.md` are the tasks of 103.6
```

### Case 100.6 — `raw/notes/` removed

> **when:**
> Work Mode of this session.

> **then:**
> `vault/raw/notes/` is deleted with its four files; git history keeps them.
> **－** Impact: no live page, script or test refers to them; only the handoffs of the old `vault/archive/2026-08-*`, removed by 102.1.

```then
delete:
  - slug: raw-notes
    impact: "vault/raw/notes/, four files of 2026-08-13 — two owner's notes and two .coverage.tsv — referenced only by the handoffs under the old vault/archive/2026-08-*, removed by 102.1; no live page, script or test names them; git history keeps them (case 100.6)"
```

```tasks
- [x] `git rm -r vault/raw/notes` (100.6)
```

## Case 101 — the tail `/hi` prints

> **context:**
> What Case 95 held besides the archive of Case 100: the ledger tail and `decided_by`. Lines written after the librarian's commit — the readings of its run, the lessons of the close — reach the Frontier two sessions later: the next librarian materializes them, and only its brief names them (`lesson-readings-after-librarian-invisible-to-next-hi`, `insight-session-vault-knowledge-not-loaded`, severity 2). `/hi` reads the brief alone. Case 45 described `guppi tail`; deferred as 63, 79, 95.

> **problem:**
> `/hi` sees nothing of what was written after the librarian's commit; a failed reading and a lesson wait one session more. `rule-ledger-tail` cannot be taken up as a `create`: the placeholder page exists and `generate` (`guppi/generate.py:289`) answers with a collision; none of the three placeholders has a way to be filled.

> **given:**
> Ask-guppi (the first question of the session): `rule-ledger-tail` is a placeholder — `draft`, no `kind`, `estimates` or `tags`, `deferred_by: [decision-case-95]`, one of the three lint orphans; `estimate-ledger-tail` is free; the tags `session`, `harness`, `ledger` are registered.
> **＋** A placeholder is born in `generate.defer` without a `ref`: `type`, `purpose`, `status: draft`, `deferred_by`, `origin`, `sprint`, `created`, History `deferred, placeholder`; it has no `kind`, and every real Entity or Rule has one. That is the mark.
> **＋** `generate.create` (`generate.py:289`): `path.exists()` → "a page with this slug exists; a collision is an error, not a rename". `rule-page-generation` (`built`, two Estimates: `estimate-generate-writes`, `estimate-generate-walks-dates`) says the same in its Purpose.
> **＋** 100.1 (`{supersedes:case 95}`) takes `decision-case-95` out of the placeholder's `deferred_by` in the same run, before this create applies: the yaml keeps the ledger's order.
> **＋** `rule-skill-hi` (`built`, MOC, `render_mode: full`, children `rule-internal-context`, `rule-git-context`, `rule-github-issues`; `deferred_by: [decision-case-98]`, the render after the pull, F4): its Render holds one marker per child in `children` order; Estimates `estimate-hi-no-read-calls` (the context holds everything without a read call) and `estimate-hi-writes-frontier` (`### case 73.3`).
> **＋** `materialize.parse_line`, the yaml fields `line`, `folded`, `unparsed`, `load_yaml` — the same as 100.1; the coverage of a line is one function for both scripts. After case 103 the ledgers under `raw/` are the session ledgers and, until archived, the date-level ones.
> **＋** `sprint.md`, Slice 3c, lists `decided_by`, `origin` as a pointer, the archive by run stamp with paths rewritten, the tail, lint on both fields, the pages migrated by script; Done-when 1 says "`decided_by` or `origin`". `docs/migration/migration-plan.md` is a draft, not the vault.
> **＋** Glossary row `/hi, Frontier`: "the open items it assembles (brief, sprint, issues, an unfinished plan)".
> **－** `hi` goes to the event log, not the ledger: it is never in the tail.
> **－** A line outside the ledger grammar is not printed: it is either `unparsed` in the yaml or not a record.
> **－** `decided_by` is not made; `origin` stays the one pointer from a page to its Case: `#case-N` names `decision-case-N`, History carries the wikilink, lint checks `origin`. `estimate-tail-lists-unmaterialized` (the slug of Case 45) is not used; the Estimate is derived from the slug: `estimate-ledger-tail`.

### Case 101.1 — `generate` fills a placeholder on a `create`

> **when:**
> `uv run guppi generate` applies a `create` whose slug is a live page without `kind` and with `status: draft`.

> **then:**
> The page is filled from the entry: fields and sections as for a new page, `origin` the create's, `created` kept, `deferred_by` kept (empty after the supersedes), History gains `created over placeholder · [[decision-case-N]]`.
> **＋** The Estimate from `method` is created and written into `estimates`, as for any Leaf create.
> **＋** Any other existing page is a collision, as today.
> **＋** `estimate-generate-writes` gets a `### case 101.1` block, `pending`.

```then
update:
  - slug: rule-page-generation
    contract: changed
    estimate_slug: estimate-generate-writes
    replace:
      - old: "disagreeing silently. A slug collision is an error, never a rename."
        new: "disagreeing silently. A slug collision is an error, never a rename — with one exception: a `create` whose slug is a placeholder page, `status: draft` and no `kind`, fills that page (case 101.1)."
      - old: "without one it writes a placeholder page, `status: draft`, with only the fields the Case gave and `deferred_by`."
        new: "without one it writes a placeholder page, `status: draft`, with only the fields the Case gave and `deferred_by`. A later `create` of that slug fills the placeholder: fields and sections as for a new page, `origin` the create's, `created` and `deferred_by` kept, History `created over placeholder`; its Estimate is made from `method` as for any Leaf. Any other existing page is a collision (case 101.1)."
    change: "a create over a placeholder fills it; any other existing page stays a collision (case 101.1)"
```

```tasks
- [x] `guppi/generate.py`: `create` over a live page with `status: draft` and no `kind` fills it — `origin` from the entry, `created` and `deferred_by` kept, History `created over placeholder`; the Estimate from `method` as today
- [x] `tests/test_generate.py`: a create over a placeholder fills it; a create over a real page is still a collision
- [ ] read `estimate-generate-writes` (101.1): unit, then the librarian's run of this session fills `rule-ledger-tail`
```

### Case 101.2 — `rule-ledger-tail`, the script and its line

> **when:**
> `uv run guppi tail` runs — from the render of `/hi`, or by hand.

> **then:**
> For every `ledger.md` under `vault/raw/` — the date-level one of a date first, then its session ledgers in folder order, dates ascending — the script prints every line that `parse_line` reads as a record and whose number is neither in the `line` or `folded` of an entry nor under `unparsed` in the `materialize.yaml` beside that ledger, as `<date> L<n>: <the line>` or `<date>/<HHMM> L<n>: <the line>`.
> **＋** A ledger without a yaml beside it prints every record line it has.
> **＋** A ledger fully covered prints nothing; with an empty tail the output is empty.
> **＋** Exit 0 always; a read error on one ledger is a stderr line and the walk goes on.
> **＋** Render (`partial`, `.claude/skills/hi/SKILL.md`): between the markers `<!-- rule-ledger-tail -->` one line, `Tail: !`uv run guppi tail``.
> **－** The coverage of a line is the function `guppi archive` uses: the two scripts cannot disagree on what "named in the yaml" means.

```then
create:
  - slug: rule-ledger-tail
    type: rule
    kind: Leaf
    purpose: Shows at /hi every ledger line that no vault page holds yet, so a reading or a lesson written after the librarian's commit reaches the next session's Frontier
    enforcement: render
    governs: .claude/skills/hi/SKILL.md
    render_mode: partial
    implementation_ref: [guppi/tail.py, tests/test_tail.py]
    tags: [session, harness, ledger]
    sections:
      Purpose: |
        Shows at `/hi` every ledger line that no vault page holds yet. The readings of the
        librarian's own run and the lessons of the close are written after its commit and
        after its brief, so the next `/hi`, which reads the brief, would not see them until
        the librarian after next. The tail closes that gap for the Frontier: the page of a
        reading comes with the next librarian, the fact that it failed comes at once.
      Render: |
        <!-- rule-ledger-tail -->
        Tail: !`uv run guppi tail`
        <!-- /rule-ledger-tail -->
      How it works: |
        `uv run guppi tail` walks every `ledger.md` under `vault/raw/`: the date-level
        ledger of a date first (the shape before case 103), then the session ledgers
        `raw/<date>/<HHMM>/ledger.md` in folder order, dates ascending. For each it reads
        the `materialize.yaml` beside it and prints every line that
        `materialize.parse_line` reads as a record and whose number is neither in the
        `line` or `folded` of an entry nor under `unparsed`, as
        `<date> L<n>: <the line as in the ledger>` or `<date>/<HHMM> L<n>: <the line>`.
        A ledger without a yaml beside it prints every record line it has; a ledger fully
        covered prints nothing, and with an empty tail the output is empty. Exit 0 always;
        a ledger that cannot be read is a line on stderr and the walk goes on. `hi` is
        never in the tail: it goes to the event log. A line outside the ledger grammar is
        not printed — it is either `unparsed` in the yaml or not a record. The coverage of
        a line is the one function `guppi archive` uses to call a unit done
        ([[rule-raw-archive]]), so the two scripts cannot disagree; after the archive the
        walk holds only the sessions not yet done. The Render splices one line into the
        `/hi` skill, between the markers of this page, after `rule-github-issues`; the
        Frontier text of [[rule-skill-hi]] makes a `failed` reading or a lesson of the tail
        an item, and a decision line not.
    method: |
      Unit, `tests/test_tail.py`: a fixture with a date-level ledger whose yaml covers
      every record line, a session ledger with a yaml and two record lines outside it (an
      estimate and a lesson after the last entry), a session ledger with no yaml, and a
      ledger holding a line outside the grammar; one run prints exactly the two uncovered
      lines of the second in the `<date>/<HHMM> L<n>: ` form and every record line of the
      third, in order, nothing of the first, nothing for the ungrammatical line, exit 0; an
      unreadable yaml is one stderr line and the other ledgers still print. Live,
      2026-09-13, by hand: `uv run guppi tail` after the librarian's commit of this session
      prints the readings and lessons written after it and nothing else; the next `/hi`
      carries them under `Tail:`.
```

```tasks
- [x] `guppi/tail.py`: `run(argv, *, stdout, stderr, project_dir)` — the walk over `archive.units` plus ledgers without a yaml, `archive.uncovered_lines`, the two output forms, stderr on a read error, exit 0
- [x] `guppi/cli.py`: register `tail`
- [x] `tests/test_tail.py`: the fixture of four ledgers, the checks of the method
- [ ] read `estimate-ledger-tail`: unit, then live after the librarian's commit of this session
```

### Case 101.3 — `/hi` loads the tail

> **when:**
> The person invokes `/hi`.

> **then:**
> The Render of `rule-skill-hi` carries the marker `<!-- rule-ledger-tail -->` after `<!-- rule-github-issues -->`; `rule-ledger-tail` is the fourth child.
> **＋** After `/hi` the context holds the output of `guppi tail` without a read call.
> **＋** `estimate-hi-no-read-calls` gets a `### case 101.3` block, `pending`.

```then
update:
  - slug: rule-skill-hi
    contract: changed
    estimate_slug: estimate-hi-no-read-calls
    set: {children: [rule-internal-context, rule-git-context, rule-github-issues, rule-ledger-tail]}
    replace:
      - old: "<!-- rule-github-issues -->\n"
        new: "<!-- rule-github-issues -->\n<!-- rule-ledger-tail -->\n"
      - old: "Rendered in full into the skill file; the three children splice into the markers below"
        new: "Rendered in full into the skill file; the four children splice into the markers below"
    change: "rule-ledger-tail the fourth child; its marker after rule-github-issues, the tail in the context without a read call (case 101.3)"
```

```tasks
- [ ] read `estimate-hi-no-read-calls` (101.3): the next session's `/hi`, `Tail:` in the context
```

### Case 101.4 — the tail in the Frontier

> **when:**
> The agent assembles the Frontier from the text of `/hi`.

> **then:**
> The skill text: "A `failed` reading or a lesson in the Tail above is an item; a decision line of the tail is not — its page comes with the next librarian."
> **＋** `estimate-hi-writes-frontier` gets a `### case 101.4` block, `pending`.

```then
update:
  - slug: rule-skill-hi
    contract: changed
    estimate_slug: estimate-hi-writes-frontier
    replace:
      - old: "A failed pull or an unavailable `gh` is an item on that list, not a reason to stop."
        new: "A failed pull or an unavailable `gh` is an item on that list, not a reason to stop. A `failed` reading or a lesson in the Tail above is an item; a decision line of the tail is not — its page comes with the next librarian."
    change: "a failed reading or a lesson of the tail is a Frontier item, a decision line is not (case 101.4)"
```

```tasks
- [ ] read `estimate-hi-writes-frontier` (101.4): the next session's Frontier
```

### Case 101.5 — the glossary row and the sprint

> **when:**
> Someone reads the glossary row `/hi, Frontier` or Slice 3c in `sprint.md`.

> **then:**
> Glossary: "the open items it assembles (brief, sprint, issues, an unfinished plan, the ledger tail)".
> **＋** `sprint.md`, Slice 3c: "the archive of an applied session of `raw/` (case 100), the tail `/hi` prints (case 101), one archive root (102), the ledger of a session (103); `decided_by` dropped — `origin` is the one pointer"; Done-when 1: "`origin` as its schema says"; Slice 5 loses the old `vault/archive/` (102.1).
> **－** By hand in Work Mode; `sprint.md` is a working file, no ledger line.

```then
update:
  - slug: glossary
    file: vault/wiki/glossary.md
    change: "row /hi, Frontier: the ledger tail among the sources the Frontier is assembled from (case 101.5)"
```

```tasks
- [x] `vault/wiki/glossary.md` row `/hi, Frontier`, by hand (101.5)
- [x] `vault/wiki/sprint.md` Slice 3c, Done-when 1 and Slice 5, by hand (101.5)
```

## Case 102 — one root, `vault/archive/`

> **context:**
> Two archive roots in the vault. `vault/archive/`: 49 folders of August (`2026-08-12`…`2026-08-31`, 4.9 MB), the handoffs and pages of the model before the migration, whose fate sat in Slice 5. `vault/archived/`: the new one, where `cleanup` puts pages with `status: archived` — `migration/2026-09-11/estimates/` (21) and `migration/2026-09-12/lessons/` (1). `vault/wiki/archive/` is an empty folder git does not know. Case 100 puts the archive of `raw/` under the same root.

> **problem:**
> Two places for one notion, and the name that was wanted taken by what is not needed. Renaming now is cheap: three places in the code, five test files, four pages, one `git mv`. Later every `cleanup` run and every archived session add paths.

> **given:**
> Code reading `vault/archived`: `cleanup.py:29` (`archive_root`, writes and restores), `lint.py:207` (`archived_slugs`, `rglob` over the archive — a reference to an archived slug is not a finding), `materialize.py:339` (`page_exists`, the `exists` mark). Tests: `test_cleanup.py:1,37`, `test_lint.py:257,517,597,623`, `test_pretask.py:473` — path strings in fixtures.
> **＋** Pages naming the path: `rule-cleanup` (How it works: `vault/archived/<sprint>/<date>/<category>/<slug>.md`, "A page under `vault/archived/`"), `rule-documentation` (Render, the frame: "Never read … `vault/archived/`"), `index.md` §1 line 32, the glossary row `archived`. Neither `log.md` nor the History of pages carries a path — slugs only.
> **＋** The 22 archived pages hold no paths; their slugs sit in `decision-case-53.1`, `decision-case-70`, the `children` of `insight-ledger-hook-reads-only-the-final-text`. After the `git mv`, `lint.archived_slugs` finds them under the new root.
> **＋** The old `vault/archive/` is read by no script, test or Rule page; only its own handoffs and `raw/notes/` (100.6) point at it. `sprint.md` Slice 5 names it among the old folders.
> **＋** The layout under the root: `vault/archive/<sprint>/<date>/<HHMM>/` is the base — a session; inside, `raw/` (its ledger, yaml, Spec, Frontier, handoff) and `<category>/<slug>.md` (the pages its cleanup archived). `vault/archive/<sprint>/<date>/raw/` holds a date-level ledger of the shape before case 103. A date before 2026-09-12 held one session without a `<HHMM>/` folder (case 73.1); its pages sit at `<date>/<category>/`.
> **＋** `cleanup` learns the session of the run as the latest `<HHMM>/` folder under `raw/<day of the run>/`, and without one the latest of the nearest date back (a session across midnight).
> **－** `vault/parked/` (2 folders, Slice 4) and `docs/` are not touched.
> **－** `estimate-cleanup-moves` (`passed`) gets a block: the path is part of its criterion. `page_exists` in `materialize` is implementation; the `exists` contract does not change — a task without a line. 102.3 and 102.5 as first shown are folded into 103.5 and 103.6.

### Case 102.1 — the old archive removed

> **when:**
> Work Mode of this session, before `archived/` moves.

> **then:**
> `vault/archive/` is removed whole (`git rm -r`, 49 folders); `vault/wiki/archive/` is removed.
> **－** Impact: no live page, script, test or Rule refers to them; git history keeps them; Slice 5 of `sprint.md` loses the item (Work Mode, by hand, 101.5).

```then
delete:
  - slug: old-archive
    impact: "vault/archive/ — 49 folders of 2026-08-12…2026-08-31, the handoffs and pages of the model before the migration, 4.9 MB — and the empty vault/wiki/archive/; read by no script, test or Rule page, referenced only by their own handoffs and raw/notes/ (100.6); git history keeps them; Slice 5 of sprint.md loses the item (case 102.1)"
```

```tasks
- [x] `git rm -r vault/archive` and remove `vault/wiki/archive/` (102.1), first
```

### Case 102.2 — `cleanup` writes under the session

> **when:**
> `uv run guppi cleanup` moves or restores a page.

> **then:**
> A page with `status: archived` goes to `vault/archive/<sprint>/<date>/<HHMM>/<category>/<slug>.md`: `<date>` the day of the run, `<HHMM>` the latest session folder under `raw/<date>/`, and without one the latest of the nearest date back.
> **＋** A page under `vault/archive/` whose status is no longer `archived` comes back to `wiki/<category>/` from any depth.
> **＋** Migration in Work Mode, one commit: `archived/migration/2026-09-11/estimates/` → `archive/migration/2026-09-11/estimates/` (a date without a session); the lesson of 2026-09-12 → `2026-09-12/<HHMM>/lessons/` of the session whose cleanup moved it, by the time of its line in `log.md`. The History of the pages does not change.
> **＋** `estimate-cleanup-moves` gets a `### case 102.2` block, `pending`.
> **－** A date without `<HHMM>/` folders is one session; the page goes to `<date>/<category>/`.

```then
update:
  - slug: rule-cleanup
    contract: changed
    replace:
      - old: |-
          `uv run guppi cleanup` moves every live page with `status: archived` to
          `vault/archived/<sprint>/<date>/<category>/<slug>.md`. `sprint` is the first `## <id>`
          heading of `sprint.md`, `date` the day of the run.
        new: |-
          `uv run guppi cleanup` moves every live page with `status: archived` to
          `vault/archive/<sprint>/<date>/<HHMM>/<category>/<slug>.md`. `sprint` is the first
          `## <id>` heading of `sprint.md`, `date` the day of the run, `HHMM` the session of the
          run: the latest `<HHMM>/` folder under `raw/<date>/`, and without one the latest of the
          nearest date back (case 102.2).
      - old: "A page under `vault/archived/` whose status is no longer `archived` moves back to"
        new: "A page under `vault/archive/`, at any depth, whose status is no longer `archived` moves back to"
    change: "the root is vault/archive/, the page lands under the session of the run (case 102.2)"
```

```tasks
- [x] `git mv vault/archived/migration vault/archive/migration`; move `lesson-ledger-hook-drops-a-block-followed-by-tool-calls-in-the-turn.md` from `2026-09-12/lessons/` to `2026-09-12/<HHMM>/lessons/` by its `log.md` line (102.2)
- [x] `guppi/cleanup.py`: `archive_root` → `vault/archive`; the target `<sprint>/<date>/<HHMM>/<category>/`; `session_of_run(project_dir, date)` — the latest `<HHMM>/` folder under `raw/<date>/`, else the nearest date back; restore from any depth
- [x] `guppi/lint.py:207`, `guppi/materialize.py:339`: the root `vault/archive`, `raw/` folders excluded from the slug set
- [x] `tests/test_cleanup.py`, `tests/test_lint.py`, `tests/test_pretask.py`: the fixture paths; a cleanup test for the session folder and the fallback
- [ ] read `estimate-cleanup-moves` (102.2): unit, then `uv run guppi cleanup` in the librarian's run of this session — a rerun moves nothing
```

### Case 102.4 — the librarian's frame names the root

> **when:**
> The librarian reads its frame.

> **then:**
> "Never read … `vault/archive/`"; the ban of 100.2 is named with the same path.
> **－** The same ban, `contract: same`.

```then
update:
  - slug: rule-documentation
    contract: same
    replace:
      - old: "`vault/archived/`: what the scripts do with the yaml is written here."
        new: "`vault/archive/`: what the scripts do with the yaml is written here."
    change: "the frame names the archive root vault/archive/ (case 102.4)"
```

```tasks
- [ ] check the rendered frame after the librarian's run names `vault/archive/` (102.4)
```

## Case 103 — the ledger of a session

> **context:**
> The ledger, the yaml and `event_log.md` live at the date level (`raw/<date>/`); the session folder `raw/<date>/<HHMM>/` holds `spec.md`, `frontier.md`, `handoff.md` (case 73.1 left the ledger in place with a `－` line). A session across midnight writes into two ledgers; the three sessions of 2026-09-12 into one. The archive by session (102) on a date-level ledger comes out with an exception, "the ledger one level up".

> **problem:**
> The unit of work is the session: Plan Mode, Spec, Frontier, handoff, the librarian, the archive. The ledger is the one file of the session that does not sit with it. Every reader of the ledger is tied to the date: the hook's write path, the walks of `materialize` and `generate`, the window of `pretask`, the form of `origin` and its resolution in lint.

> **given:**
> `ledger.py`: `ledger_path` = `raw/<today>/ledger.md`; `session_dir` (`ledger.py:196`) already gives `raw/<hi date>/<hi HHMM>/` from the event logs and the session stamp — `guppi spec` writes there; `existing_bodies` (the dedupe) reads `raw/*/ledger.md`; the `hi` window is `session_event_logs` over `event_log.md` back across dates (55.1).
> **＋** `materialize.py`: `dates_with(ledger.md)` walks by date; `read_specs` reads `raw/<date>/spec.md` (before 73) and every `raw/<date>/<HHMM>/spec.md`; `origin` is built at lines 351, 566, 577, 654 as `raw/{date}/ledger.md#…`; the yaml is `yaml_path(date)`. `generate.py:795`: `dates_with(materialize.yaml)`. `pretask.window_lines` (`pretask.py:119`): the date-level ledgers from the `hi` date to today, on the `hi` date from the `hi` time; findings `raw/<day>/ledger.md:<n>`. `lint.py:57–58`: `ORIGIN_CASE`, `ORIGIN_LINE` — the date form only; `archived_slugs` — `rglob` over the archive.
> **＋** Pages: `rule-ledger-write` (Estimate `estimate-ledger-write-lifts`), `rule-materialize` (`estimate-materialize-assembles`, `estimate-materialize-walks-dates`), `rule-page-generation` (`estimate-generate-writes`, `estimate-generate-walks-dates`), `rule-pretask` (`estimate-pretask-reconciles`), `rule-lint` (`estimate-lint-catches`, the block of 100.3 from this session). `index.md` §1 (the tree of `raw/`), §4 ("`#case-N` in an `origin`"); glossary rows `Ledger`, `Working files`, `origin`, `archived`; `origin` in five `schema.md` (entities, rules, estimates, lessons, decisions) as prose — `schema.yaml` has no pattern; `decisions/schema.md:23`: "`raw/` stays in place; it is not archived with the session".
> **＋** Case 100.3 (line written) — `origin` resolved in the archive; 100.5 — `index.md`, the glossary. Their content is the Spec, not yet approved; 103.5 and 103.6 take them over with `{supersedes}`, so `estimate-lint-catches` holds one block and the files have one place.
> **＋** Case 102 as first shown loses 102.3 and 102.5 (folded into 103.5, 103.6).
> **－** `event_log.md`, `rule-event-log`, `rule-spec-capture`, `rule-skill-hi` do not change: the session folder, the log of the day and the window stay as they are.
> **－** The hook changes its write path the moment the code changes — in Work Mode of this session; the lines of this session written before that stay in the date-level ledger and are read in the old shape. Pre-task of this session runs on the old code.

### Case 103.1 — the hook writes into the session

> **when:**
> The `Stop` hook (`uv run guppi ledger`) writes record lines.

> **then:**
> The lines go to `raw/<hi date>/<hi HHMM>/ledger.md` — the session folder from `session_dir`, the same folder across midnight.
> **＋** The dedupe reads every `ledger.md` under `raw/` at any depth.
> **－** Without a `hi` the hook refuses as today; `event_log.md` stays per day as today.

```then
update:
  - slug: rule-ledger-write
    contract: changed
    replace:
      - old: "`vault/raw/<today>/ledger.md`, interpreting nothing: the text verbatim, the time of writing"
        new: "`vault/raw/<hi date>/<hi HHMM>/ledger.md` — the session's folder, the same across midnight (case 103.1) — interpreting nothing: the text verbatim, the time of writing"
    change: "the lines go to the session folder raw/<hi date>/<hi HHMM>/ledger.md; the dedupe reads every ledger under raw/ (case 103.1)"
```

```tasks
- [x] `guppi/ledger.py`: `ledger_path` → the session folder of `session_dir` (mkdir on append); `existing_bodies` over `raw/**/ledger.md`
- [x] `tests/test_ledger.py`: the lines land in `raw/<hi date>/<hi HHMM>/ledger.md`, across midnight too; a line already in a session ledger is not written twice
- [x] read `estimate-ledger-write-lifts` (103.1): unit, then the first LEDGER block after the code change lands in `raw/2026-09-13/0652/ledger.md`
```

### Case 103.2 — `materialize` walks sessions

> **when:**
> `uv run guppi materialize` runs, with `--date` or without.

> **then:**
> The unit of the walk is a session folder `raw/<date>/<HHMM>/` holding a `ledger.md`: its yaml `raw/<date>/<HHMM>/materialize.yaml`, its Spec `raw/<date>/<HHMM>/spec.md` alone, the `origin` of its entries `raw/<date>/<HHMM>/ledger.md#case-N` and `#L<n>`.
> **＋** A date-level `raw/<date>/ledger.md` (the shape before this Case) is walked as today: the Specs of the date, `raw/<date>/materialize.yaml`, the date form of `origin`; on a date with both shapes the date-level one goes first, then the sessions in folder order.
> **＋** `--date` walks the date-level ledger and every session of the date; stdout carries one line per yaml.
> **＋** `estimate-materialize-walks-dates` gets a `### case 103.2` block, `pending`.

```then
update:
  - slug: rule-materialize
    contract: changed
    estimate_slug: estimate-materialize-walks-dates
    replace:
      - old: "`uv run guppi materialize [--date YYYY-MM-DD]` reads `raw/<date>/ledger.md` and every Spec of the date — `raw/<date>/<HHMM>/spec.md` in folder order, and `raw/<date>/spec.md` when the date has one (dates before case 73) — and writes `raw/<date>/materialize.yaml`;"
        new: "`uv run guppi materialize [--date YYYY-MM-DD]` reads one unit at a time. A session folder `raw/<date>/<HHMM>/` holding a `ledger.md` is a unit (case 103.2): it reads that ledger and `raw/<date>/<HHMM>/spec.md` alone, and writes `raw/<date>/<HHMM>/materialize.yaml`, the `origin` of every entry `raw/<date>/<HHMM>/ledger.md#…`. A date-level `raw/<date>/ledger.md` (the shape before case 103) is a unit read as before: the ledger and every Spec of the date — `raw/<date>/<HHMM>/spec.md` in folder order, and `raw/<date>/spec.md` when the date has one (dates before case 73) — written to `raw/<date>/materialize.yaml` with the date form of `origin`; on a date with both shapes the date-level unit goes first;"
      - old: "walks every `raw/<date>/` that holds a `ledger.md`, in date order, and prints one\nline per date;"
        new: "walks every unit under `raw/` — dates ascending, the date-level ledger of a date first, then its sessions in folder order — and prints one\nline per unit;"
    change: "the unit of the walk is the session folder with its own ledger, yaml, Spec and origin; a date-level ledger is walked in the old shape (case 103.2)"
```

```tasks
- [x] `guppi/materialize.py`: `units(project_dir)` shared with `archive` — `(date, session or None)`; `yaml_path`, `read_specs`, the `origin` strings and the `ledger` field per unit; `--date` walks the units of the date; stdout one line per unit
- [x] `tests/test_materialize.py`: a session unit reads its own Spec and yaml with the session `origin`; a date with both shapes walks the date-level first; `--date`
- [ ] read `estimate-materialize-walks-dates` (103.2): unit, then the librarian's run walks `raw/2026-09-13/` in both shapes
```

### Case 103.3 — `generate` walks sessions

> **when:**
> `uv run guppi generate` runs, with `--date` or without.

> **then:**
> Every `materialize.yaml` under `raw/` is applied: the date-level one of a date first, then the sessions of the date in folder order, dates ascending.
> **＋** `estimate-generate-walks-dates` gets a `### case 103.3` block, `pending`.

```then
update:
  - slug: rule-page-generation
    contract: changed
    estimate_slug: estimate-generate-walks-dates
    replace:
      - old: "`uv run guppi generate [--date]` applies the entries of `raw/<date>/materialize.yaml` in order,"
        new: "`uv run guppi generate [--date]` applies the entries of every `materialize.yaml` under `raw/` — the date-level one of a date first, then `raw/<date>/<HHMM>/materialize.yaml` per session in folder order, dates ascending (case 103.3) — each in order,"
    change: "the walk covers the yaml of every session folder as well as the date-level yaml (case 103.3)"
```

```tasks
- [x] `guppi/generate.py`: the walk over every yaml under `raw/` in unit order
- [x] `tests/test_generate.py`: the walk applies a session yaml
- [ ] read `estimate-generate-walks-dates` (103.3): unit, then the librarian's run applies both yamls of 2026-09-13
```

### Case 103.4 — pre-task reads the session's ledger

> **when:**
> `uv run guppi pretask --check` gathers the lines of the window.

> **then:**
> The window is `raw/<hi date>/<hi HHMM>/ledger.md` whole, plus the date-level ledgers from the `hi` date to today from the `hi` time on, as today, while any exist.
> **＋** A grammar finding names the file: `raw/<date>/<HHMM>/ledger.md:<n>` or `raw/<date>/ledger.md:<n>`.
> **＋** `estimate-pretask-reconciles` gets a `### case 103.4` block, `pending`.

```then
update:
  - slug: rule-pretask
    contract: changed
    replace:
      - old: "It also runs every record line of the session's window through `materialize.parse_line` and prints one line for each that does not parse, with its date and line number (case 75.2)."
        new: "It also runs every record line of the session's window — `raw/<hi date>/<hi HHMM>/ledger.md` whole, plus the date-level ledgers from the `hi` date to today from the `hi` time on, while any exist (case 103.4) — through `materialize.parse_line` and prints one line for each that does not parse, with its file and line number (case 75.2)."
    change: "the window is the session's ledger plus the date-level ledgers of the window (case 103.4)"
```

```tasks
- [x] `guppi/pretask.py`: `window_lines` reads the session ledger whole plus the date-level window; findings name the file
- [x] `tests/test_pretask.py`: lines of the session ledger are in the window; a finding names `raw/<date>/<HHMM>/ledger.md:<n>`
- [ ] read `estimate-pretask-reconciles` (103.4): unit; live at the next session's pre-task
```

### Case 103.5 — lint resolves both forms of `origin`

> **when:**
> `uv run guppi lint` checks an `origin` and gathers the known slugs.

> **then:**
> `raw/<date>/ledger.md#…` is looked for at `vault/raw/<date>/ledger.md`, then at `vault/archive/*/<date>/raw/ledger.md`; `raw/<date>/<HHMM>/ledger.md#…` at `vault/raw/<date>/<HHMM>/ledger.md`, then at `vault/archive/*/<date>/<HHMM>/raw/ledger.md`; the `[case N]` or line-number check runs on the file found.
> **＋** In neither: the finding `no such ledger`; in both: the finding `two ledgers for <path>`.
> **＋** The archived slugs are every `*.md` under `vault/archive/` except those under a `raw/` folder.
> **＋** `estimate-lint-catches` gets a `### case 103.5` block; the block of 100.3 is removed.

```then
update:
  - slug: rule-lint
    contract: changed
    replace:
      - old: "`origin` as a grep target in `raw/`,"
        new: "`origin` as a grep target — `raw/<date>/ledger.md#…` at `vault/raw/<date>/ledger.md` or `vault/archive/*/<date>/raw/ledger.md`, `raw/<date>/<HHMM>/ledger.md#…` at `vault/raw/<date>/<HHMM>/ledger.md` or `vault/archive/*/<date>/<HHMM>/raw/ledger.md`; in neither place or in both a finding (case 103.5) —"
    change: "both forms of origin resolve in raw/ or vault/archive/; archived slugs come from vault/archive/ outside raw/ folders; supersedes case 100.3 (case 103.5)"
```

```tasks
- [x] `guppi/lint.py`: `ORIGIN_CASE`/`ORIGIN_LINE` accept the session form; `check_origin` resolves each form in `raw/` then `vault/archive/`; `two ledgers` finding; `archived_slugs` skips `raw/` folders
- [x] `tests/test_lint.py`: an origin of each form resolved in `raw/` and in the archive; both places; neither
- [x] read `estimate-lint-catches` (103.5): unit, then `uv run guppi lint` after the live archive — every `origin` of both forms resolved
```

### Case 103.6 — the map, the glossary, five schemas

> **when:**
> Someone reads `index.md`, the glossary, or the `origin` row of a category's `schema.md`.

> **then:**
> `index.md` §1 — the tree of `raw/<date>/`: `event_log.md` of the day; `<HHMM>/` with `ledger.md`, `materialize.yaml`, `spec.md`, `frontier.md`, `handoff.md`; the line "dates before 2026-09-13 hold the ledger and the yaml at the date root, and the scripts read that shape until the date is archived"; `archive/` — the tree of 102: `<sprint>/<date>/<HHMM>/raw/` and `<category>/`, `<sprint>/<date>/raw/` for a date-level ledger, moved by `guppi archive` and `guppi cleanup`; §4 — both forms of `origin`, resolved in `raw/` or `archive/`.
> **＋** Glossary: `Ledger` — "`raw/<date>/<HHMM>/ledger.md`"; `Working files` — "`raw/`: `event_log.md` of the day and one folder per session with its ledger, yaml, Spec, Frontier, handoff; moved into the archive once applied"; `archived` — "`guppi cleanup` moves the file to `vault/archive/<sprint>/<date>/<HHMM>/<category>/`"; `origin` — "`raw/<date>/<HHMM>/ledger.md#case-N`, the date form on older pages".
> **＋** `entities`, `rules`, `estimates`, `decisions` `schema.md`: `origin` = `raw/YYYY-MM-DD/HHMM/ledger.md#case-N` (older pages: the date form); `lessons/schema.md`: `…#L<n>`; `decisions/schema.md:23` — "the `raw/` of a session is archived with it once applied"; `decisions/schema.md` `status` row — "`archived` the moment a later Case supersedes it" (104.1).
> **－** By hand in Work Mode.

```then
update:
  - slug: index
    file: vault/wiki/index.md
    change: "§1: the tree of raw/<date>/ with the session folder holding ledger, yaml, Spec, Frontier, handoff, event_log.md of the day, the date-level shape before 2026-09-13; the tree of archive/ — <sprint>/<date>/<HHMM>/raw/ and <category>/, <sprint>/<date>/raw/; §4: both forms of origin, resolved in raw/ or archive/ (case 103.6, supersedes 100.5)"
  - slug: glossary
    file: vault/wiki/glossary.md
    change: "rows Ledger, Working files, archived, origin: the session ledger raw/<date>/<HHMM>/ledger.md, the archive root vault/archive/<sprint>/<date>/<HHMM>/, both forms of origin (case 103.6, supersedes 100.5)"
  - slug: entities-schema
    file: vault/wiki/entities/schema.md
    change: "origin row: raw/YYYY-MM-DD/HHMM/ledger.md#case-N, the date form on older pages (case 103.6)"
  - slug: rules-schema
    file: vault/wiki/rules/schema.md
    change: "origin row: raw/YYYY-MM-DD/HHMM/ledger.md#case-N, the date form on older pages (case 103.6)"
  - slug: estimates-schema
    file: vault/wiki/estimates/schema.md
    change: "origin row: raw/YYYY-MM-DD/HHMM/ledger.md#case-N, the date form on older pages (case 103.6)"
  - slug: lessons-schema
    file: vault/wiki/lessons/schema.md
    change: "origin row: raw/YYYY-MM-DD/HHMM/ledger.md#L<n>, the date form on older pages (case 103.6)"
  - slug: decisions-schema
    file: vault/wiki/decisions/schema.md
    change: "origin row: raw/YYYY-MM-DD/HHMM/ledger.md#case-N, the date form on older pages; line 23: the raw/ of a session is archived with it once applied; status row: archived the moment a later Case supersedes it (cases 103.6, 104.1)"
```

```tasks
- [x] `vault/wiki/index.md` §1 (the tree, line 20 "and stay here" and line 32) and §4 (line 176 `raw/<date>/ledger.md`, line 212 the grep target), by hand (103.6)
- [x] `vault/wiki/glossary.md` rows `Ledger`, `Working files`, `archived`, `origin`, by hand (103.6)
- [x] `vault/wiki/{entities,rules,estimates,lessons,decisions}/schema.md` `origin` rows, and the `status` row of `decisions/schema.md`, by hand (103.6, 104.1)
- [x] `make style`, `make test` after every code task of 103
```

## Case 104 — status cascades over the archive

> **context:**
> The outcome of the talk on the archive: a page leaves when it stops describing the present. Today `generate.cascade` (after all entries) computes two things: `built`/`draft` of an Entity or Rule from its Estimates, and the `severity` of an Insight from its live children. `archived` is set by `delete` alone. A Decision a later Case superseded stays `superseded` for good (24 pages); a lesson stays `clustered` after its Insight is `actioned` — the schema promises the archive, nothing does it; an Insight whose children are all withdrawn (case 97: `insight-ledger-hook-reads-only-the-final-text` after case 70) hangs `open`.

> **problem:**
> Three status transitions follow from facts already ratified and must be made by the script, not by hand: superseded → archived, the children of an actioned Insight → archived, an Insight with no live child → archived. Until then the archive is a promise.

> **given:**
> `generate.py:596–605`: a supersedes sets `status: superseded`, `superseded_by`, History `superseded by [[X]]`, clears `deferred_by`. `generate.cascade` (`generate.py:610–655`): `built`/`draft`, the recount of `severity` over children whose status is not `archived`. Statuses: Decision `current | superseded | archived` (`decisions/schema.md`); Lesson `new | clustered | archived`, "Archived when its Insight is `actioned`" (`lessons/schema.md:16`); Insight `open | actioned | archived`, `severity` = live children, `actioned` is not an end — a new lesson returns it to `open`, the older children stay `archived` (`insights/schema.md:17–34`). `rule-synthesis:22–23`: "a lesson is archived only when its Insight was actioned, and that Insight stays live".
> **＋** `cleanup` moves everything with `status: archived` (102.2: under the session of the run); lint counts archived slugs as known (`lint.py:451`), `deferred_by` and `[[decision-…]]` in History are refs like any other (`lint.py:21`). A superseded decision is never in a `deferred_by`: the supersedes takes it out.
> **＋** Today: 24 decisions `superseded`, 0 Insights `actioned`, 20 lessons `clustered`, `insight-ledger-hook-reads-only-the-final-text` at severity 2 with one archived child (the recount of brief K).
> **＋** `rule-page-generation` (two Estimates; 101.1 already puts a block on `estimate-generate-writes`); the text "After all entries: …" (`rule-page-generation.md:59–61`).
> **－** A `current` Decision is not touched before the close of the sprint (Slice 5). An `actioned` Insight is not archived. The `## Insight` section of a lesson is case 96, not this one.
> **－** `decisions/schema.md`: the `status` row gains "`archived` the moment a later Case supersedes it" — in the `decisions-schema` item of 103.6, no new line.

### Case 104.1 — a superseded decision is archived

> **when:**
> `uv run guppi generate` sets `superseded` on a decision page, or meets a decision with `status: superseded` in the cascade.

> **then:**
> The page's status is `archived`; `superseded_by` and the History `superseded by [[X]]` as today, plus the History `archived · superseded`; `cleanup` takes it under the session of the run.
> **＋** The cascade walks every decision page: the 24 `superseded` of today leave at the first run.
> **＋** `estimate-generate-writes` gets a `### case 104.1` block, `pending`.
> **－** `deferred_by`, the History wikilinks and the `supersedes` chain do not change: the slug is known in the archive.

```then
update:
  - slug: rule-page-generation
    contract: changed
    estimate_slug: estimate-generate-writes
    replace:
      - old: "History line; the `severity` of every insight is recounted."
        new: "History line; a decision page with `status: superseded` — the one a supersedes just set, or any met in the walk — becomes `archived` with the History `archived · superseded`, its `superseded_by` and `deferred_by` untouched (case 104.1); the `severity` of every insight is recounted."
    change: "a superseded decision is archived by the cascade (case 104.1)"
```

```tasks
- [x] `guppi/generate.py`: `cascade` — decisions `superseded` → `archived`, History `archived · superseded` (104.1)
- [x] `tests/test_generate.py`: a superseded decision is archived by the cascade; its `superseded_by` kept
- [ ] read `estimate-generate-writes` (104.1): unit, then the librarian's run of this session — the 24 superseded decisions archived and moved
```

### Case 104.2 — the lessons of an actioned Insight are archived

> **when:**
> In the cascade `generate` meets an Insight with `status: actioned`.

> **then:**
> Every child of it with `status: clustered` gets `status: archived`, History `archived · insight actioned`; the Insight's `children` does not change.
> **＋** A lesson synthesis adds later, returning the Insight to `open`, stays live; the children archived before stay archived.
> **＋** `estimate-generate-writes` gets a `### case 104.2` block, `pending`.

```then
update:
  - slug: rule-page-generation
    contract: changed
    estimate_slug: estimate-generate-writes
    replace:
      - old: "the `severity` of every insight is recounted."
        new: "the `severity` of every insight is recounted; every `clustered` child of an `actioned` insight becomes `archived` with the History `archived · insight actioned`, the insight's `children` unchanged (case 104.2)."
    change: "the clustered lessons of an actioned Insight are archived by the cascade (case 104.2)"
```

```tasks
- [x] `guppi/generate.py`: `cascade` — the `clustered` children of an `actioned` insight → `archived`, History `archived · insight actioned` (104.2)
- [x] `tests/test_generate.py`: the children of an actioned insight are archived; a lesson added to a reopened insight stays live
- [ ] read `estimate-generate-writes` (104.2): unit; live — no Insight is actioned today, nothing archived by this cascade in the librarian's run
```

### Case 104.3 — an Insight with no live child is archived

> **when:**
> In the cascade `generate` recounts the `severity` of an Insight with `status: open`.

> **then:**
> `severity` 0 — every child `archived` — gives `status: archived`, History `archived · no live child`; `children` keeps the slugs.
> **＋** `severity` 1 or more: as it is; the Insight stands on one live child.
> **＋** `estimate-generate-writes` gets a `### case 104.3` block, `pending`.
> **－** An `actioned` Insight with `severity` 0 is not archived: it is kept for the recurrence.

```then
update:
  - slug: rule-page-generation
    contract: changed
    estimate_slug: estimate-generate-writes
    replace:
      - old: "the insight's `children` unchanged (case 104.2)."
        new: "the insight's `children` unchanged (case 104.2); an `open` insight whose recounted `severity` is 0 becomes `archived` with the History `archived · no live child`, its `children` kept; an `actioned` one at 0 stays, kept for the recurrence (case 104.3)."
    change: "an open Insight with no live child is archived by the cascade; supersedes case 97 (case 104.3)"
```

```tasks
- [x] `guppi/generate.py`: `cascade` — an `open` insight at severity 0 → `archived`, History `archived · no live child`; an `actioned` one stays (104.3)
- [x] `tests/test_generate.py`: an open insight at 0 is archived; an actioned one at 0 stays; an open one at 1 stays
- [ ] read `estimate-generate-writes` (104.3): unit, then the librarian's run — `insight-ledger-hook-reads-only-the-final-text` unchanged at severity 1
```

## Case 105 — the slug is checked against the archive

> **context:**
> Case 94 (`rule-ask`, deferred as 65, 80, 94): `ask-guppi` reads the four live indexes and never `vault/archive/`; the slug of an archived page comes back as free. The talk of this session gave the rule: the archive is searched by slug, never by meaning. An archived slug is taken — decision pages, the `children` of Insights and History point at it. The main agent has two ways out: another slug, or restore the page and fix it at once.

> **problem:**
> Three places do not know that an archived slug is taken. `ask-guppi` answers "free". `materialize.page_exists` (`materialize.py:335`) marks such a `create` `exists` and `generate` skips it in silence — the page of the new Case is not made, the data is lost. `generate.find` (`generate.py:229`) looks in `wiki/<category>/` only: an `update` of an archived page — the one way to bring it back (`cleanup` restores a page whose status is no longer `archived`) — fails with "no such page".

> **given:**
> Ask-guppi (the first question of the session): 94 is the one defer on `rule-ask`; `rule-ask` (`built`, `render_mode: full`, `governs: .claude/agents/ask-guppi.md`, `tools: Read, Grep, Glob`, Estimate `estimate-ask-finds`, `deferred_by: [decision-case-94]`). Its Render: "You search the vault at `vault/wiki/` for the caller", the answer line "tags/slug: tags that fit, existing first; whether the named slug is free".
> **＋** `materialize.page_exists`: a live page of the category or any `<slug>.md` under the archive → `exists: true` (lines 380–384, and 513–514 for the derived Estimate). A page carries `origin` with `#case-N`; a placeholder carries the case of its defer (101.1 fills it through a `create` — not `exists`, since the Case differs).
> **＋** `generate.find` walks `CATEGORIES` under `wiki/`; `update`, `estimate`, `delete` and `defer` go through it. `cleanup.restore` (`cleanup.py:105`) already brings back a page under the archive whose status is not `archived`.
> **＋** `rule-materialize` has two Estimates (`estimate_slug: estimate-materialize-assembles`); `rule-page-generation` two (`estimate-generate-writes`, its fourth block of the session after 101.1 and 104.x).
> **＋** The glossary row `Index, ask-guppi` — "the search agent over them, one entry point" — gains one phrase; `index.md` §3 "query the vault before a create" stays.
> **－** The archive is not searched by meaning: no `exists` or `near` on an archived page; the librarian's index check and the synthesis do not change.
> **－** The agent never reads the `raw/` of the archive; `rule-pretask` does not change — it checks the slug through the answer of `ask-guppi`.

### Case 105.1 — `ask-guppi` names an archived slug

> **when:**
> A question to `ask-guppi` names a slug.

> **then:**
> The `tags/slug` line says one of three: `free`; `live` (with the category); `archived at <path> by [[decision-case-N]]` — by a Glob `vault/archive/**/<slug>.md`, `N` from the `origin` of the page found.
> **＋** The agent opens an archived page only when the question names its slug and asks what it said or why it was withdrawn; it answers from its Result, `origin` and History.
> **＋** `estimate-ask-finds` gets a `### case 105.1` block, `pending`.
> **－** The archive is not searched by meaning: the `exists` and `near` lines are live pages only.

```then
update:
  - slug: rule-ask
    contract: changed
    replace:
      - old: "You search the vault at `vault/wiki/` for the caller and answer in five lines."
        new: "You search the vault at `vault/wiki/` for the caller and answer in five lines. The archive, `vault/archive/`, is searched by slug alone, never by meaning: a named slug is checked there with a Glob `vault/archive/**/<slug>.md`, and an archived page is opened only when the question names its slug and asks what it said or why it was withdrawn (case 105.1)."
      - old: "- tags/slug: tags that fit, existing first; whether the named slug is free"
        new: "- tags/slug: tags that fit, existing first; the named slug — `free`, `live` (with its category), or `archived at <path> by [[decision-case-N]]`, N from the page's `origin`"
    change: "the named slug is checked against vault/archive/ by Glob and answered as free, live or archived at a path; the archive is never searched by meaning; supersedes case 94 (case 105.1)"
  - slug: glossary
    file: vault/wiki/glossary.md
    change: "row Index, ask-guppi: the archive answered by slug alone — free, live or archived at a path — never by meaning (case 105.1)"
```

```tasks
- [x] `vault/wiki/glossary.md` row `Index, ask-guppi`, by hand (105.1)
- [ ] read `estimate-ask-finds` (105.1): the next dispatch of `ask-guppi` with an archived slug (`estimate-agents-at-import-not-expanded`) answers `archived at … by [[decision-case-53.1]]`
```

### Case 105.2 — `exists` only for the same Case

> **when:**
> `uv run guppi materialize` reads a `create` line whose slug is already on disk — live or archived.

> **then:**
> The entry is marked `exists` only when the `origin` of the page carries the `#case-N` of this line; a derived Estimate the same way, by the `origin` of the Estimate page.
> **＋** Otherwise the entry stays an ordinary `create`; `generate` answers with a collision on stderr, the entry is `failed`, the unit stays in `raw/`.
> **＋** `estimate-materialize-assembles` gets a `### case 105.2` block, `pending`.
> **－** A placeholder (no `kind`) is not a collision: 101.1 fills it.

```then
update:
  - slug: rule-materialize
    contract: changed
    estimate_slug: estimate-materialize-assembles
    replace:
      - old: "`exists`\n(a create whose page is on disk),"
        new: "`exists`\n(a create whose page is on disk with an `origin` carrying this line's `#case-N`; a page of another Case, live or archived, leaves the entry a create for `generate` to refuse as a collision, case 105.2),"
    change: "exists only when the page on disk was born of the same Case; another Case's page is a collision (case 105.2)"
```

```tasks
- [x] `guppi/materialize.py`: `page_exists` → `page_of_case(project_dir, category, slug, case)` — the page on disk (live, or under `vault/archive/` outside `raw/`) whose `origin` carries `#case-<case>`; `exists` from it at lines 380–384 and 513–514
- [x] `tests/test_materialize.py`: a create re-read for its own page is `exists`; a create of a slug held by another Case's page, live or archived, is not
- [ ] read `estimate-materialize-assembles` (105.2): unit, then the librarian's run of this session — every create of this Spec applied, no `exists` on a new slug
```

### Case 105.3 — `update` reaches an archived page

> **when:**
> `uv run guppi generate` applies an `update` (or `estimate`, `delete`, `defer`) to a slug that is not under `wiki/`.

> **then:**
> `find` looks for `<slug>.md` under `vault/archive/`, `raw/` folders excluded, and edits the page there: `set`, `sections`, `replace`, History — as for a live page.
> **＋** `set: {status: <not archived>}` in the same entry — `cleanup` then brings the page back to `wiki/<category>/` with the History `restored · cleanup`.
> **＋** `estimate-generate-writes` gets a `### case 105.3` block, `pending`.
> **－** A slug in neither place: "no such page", as today.

```then
update:
  - slug: rule-page-generation
    contract: changed
    estimate_slug: estimate-generate-writes
    replace:
      - old: "An entry that fails — a collision, a `ref` naming no page,"
        new: "An `update`, `estimate`, `delete` or `defer` whose slug is not under `wiki/` reaches the page under `vault/archive/` (`raw/` folders excluded) and edits it there; with a `status` other than `archived` in the same entry, `cleanup` brings it back (case 105.3). An entry that fails — a collision, a `ref` naming no page,"
    change: "an update reaches an archived page in the archive, so a restore and its fix are one entry (case 105.3)"
```

```tasks
- [x] `guppi/generate.py`: `find` falls back to `vault/archive/**/<slug>.md` outside `raw/`; `update` on such a page saves it in place
- [x] `tests/test_generate.py`: an update of an archived page edits it in the archive; with `status: current` set, `cleanup` restores it; a create of a taken slug is a collision
- [x] read `estimate-generate-writes` (105.3): unit
- [x] `make style`, `make test` — the close of Work Mode
```

## Case 109 — the readers of the ledger path the check found

> **context:**
> Pre-task of Case 103: two Renders and one schema name the date-level ledger or do not know the cascade. `rule-retro` (`draft`, Render → `.claude/skills/retro/SKILL.md`): line 39 `Ledger of today: !`cat "vault/raw/$(date +%F)/ledger.md"``, line 58 the revert patch at `raw/<date>/patch-<slug>.diff`. `rule-claude-md` (`draft`, Render → `CLAUDE.md`): line 59 "the `Stop` hook writes them into `vault/raw/<date>/ledger.md`". `insights/schema.md`: `archived` in the status list with no rule for when it is set (104.2 and 104.3 bring one); `lessons/schema.md` already says "Archived when its Insight is `actioned`".

> **problem:**
> After 103.1 Retro reads a file the hook no longer writes; `CLAUDE.md` misstates the path; the Retro patch lands at the date level, which 100.1 moves with the date-level ledger and which future dates do not have. Renders are not edited by hand (`rule-governed-files-hook`).

> **given:**
> `rule-retro`: Estimate `estimate-retro-loads` (`pending`); the Render is a skill, `$(date +%F)` a shell substitution; only the hook knows the session folder (`session_dir`), a shell does not — `vault/raw/$(date +%F)/*/ledger.md` reads the ledgers of every session of the day, and the date-level one while it exists; a session across midnight reads its own through the same glob on its `hi` date.
> **＋** `rule-claude-md`: Estimate `estimate-claude-md-rendered` (`pending`); the Migration paragraph, line 59; the criterion of the Estimate is about the render reproducing the file, not about the text: `contract: same`.
> **＋** `insights/schema.md` is a Rule-class file, slug `insights-schema`; its `status` row (17) and "The archive is not searched" (30) agree with 104.
> **－** `rule-handoff`, `rule-spec-capture`, `rule-event-log` do not name the date-level ledger — checked by ask-guppi.

### Case 109.1 — Retro reads the session's ledger

> **when:**
> The person invokes `/retro`.

> **then:**
> The Render: `Ledger of today: !`cat vault/raw/$(date +%F)/ledger.md vault/raw/$(date +%F)/*/ledger.md 2>/dev/null``; the text "a line of today's ledger" becomes "a line of this session's ledger".
> **＋** The revert patch goes to `raw/<hi date>/<hi HHMM>/patch-<slug>.diff`, the session folder.
> **＋** `estimate-retro-loads` gets a `### case 109.1` block, `pending`.

```then
update:
  - slug: rule-retro
    contract: changed
    replace:
      - old: "Ledger of today: !`cat \"vault/raw/$(date +%F)/ledger.md\"`"
        new: "Ledger of today: !`cat vault/raw/$(date +%F)/ledger.md vault/raw/$(date +%F)/*/ledger.md 2>/dev/null`"
      - old: "traces to a line of today's ledger."
        new: "traces to a line of this session's ledger."
      - old: "with `git diff` into `raw/<date>/patch-<slug>.diff`, revert it, and write a short"
        new: "with `git diff` into `raw/<hi date>/<hi HHMM>/patch-<slug>.diff`, the session's folder, revert it, and write a short"
    change: "Retro reads the session ledgers of the day (and the date-level one while it exists); the revert patch goes to the session folder (case 109.1)"
```

```tasks
- [ ] read `estimate-retro-loads` (109.1): the `/retro` of this session after the librarian's render — the `Ledger of today:` line holds the session ledger
```

### Case 109.2 — `CLAUDE.md` names the session ledger

> **when:**
> Someone reads the Migration paragraph of `CLAUDE.md`.

> **then:**
> "…the `Stop` hook writes them into `vault/raw/<date>/<hi HHMM>/ledger.md`, the session's folder, each prefixed with the time of writing".
> **－** `contract: same`; the librarian's render rewrites the file.

```then
update:
  - slug: rule-claude-md
    contract: same
    replace:
      - old: "in the reply and the `Stop` hook writes them into `vault/raw/<date>/ledger.md`, each"
        new: "in the reply and the `Stop` hook writes them into `vault/raw/<date>/<hi HHMM>/ledger.md`, the session's folder (case 103.1), each"
    change: "the Migration paragraph names the session ledger (case 109.2)"
```

```tasks
- [ ] check `CLAUDE.md` after the librarian's render names `vault/raw/<date>/<hi HHMM>/ledger.md` (109.2)
```

### Case 109.3 — the insights schema names the cascades

> **when:**
> Someone reads the `status` row of `insights/schema.md`.

> **then:**
> "`archived` when the cascade of `generate` finds an `open` Insight with no live child (case 104.3); an `actioned` Insight is never archived by the cascade"; line 30 gains "its `clustered` children are archived by the cascade (case 104.2)".
> **－** By hand in Work Mode.

```then
update:
  - slug: insights-schema
    file: vault/wiki/insights/schema.md
    change: "status row: archived when the cascade finds an open Insight with no live child, never an actioned one; line 30: the clustered children of an actioned Insight are archived by the cascade (cases 104.2, 104.3, 109.3)"
```

```tasks
- [x] `vault/wiki/insights/schema.md` `status` row and line 30, by hand (109.3)
```

## Deferred

## Case 106 — a render inside `/hi`, after the pull

> **context:**
> `git pull` lives inside `/hi`, which runs after the `SessionStart` hooks, so a change the pull brings is rendered only at the following session start. Case 89 puts the render in the librarian's phase and leaves this half open. Deferred as 98 in session K.

> **problem:**
> The render has to run once more after the pull, inside `/hi`. It waits for the pull itself, which has no upstream to pull from yet (sprint, Slice 5).

```then
defer:
  - slug: rule-skill-hi
    type: rule
    purpose: A render inside /hi after the pull, so what arrives from outside the session reaches its files in the same session
```

## Case 107 — Slice 3b: Work Mode

> **context:**
> `rule-work-mode` and `rule-subagent-guppi` have stood as placeholders since case 29, then 64, 78, 93, without `kind`, `estimates` or `tags`; two of lint's three orphans. The draft in `docs/migration/` still has to be reconciled with case 59.3 — no separate `plan.md`, the `tasks` blocks of the Spec — and with the fork clause. Case 101.1 now gives a placeholder a way to be filled.

> **problem:**
> The phase the harness spends most of its time in is the one phase with no ratified rule. It needs a Plan Mode of its own; this session's went to the archive.

```then
defer:
  - slug: rule-work-mode
    type: rule
    purpose: The rule of Work Mode — the Spec as tasks with code, the ticked boxes, what a subagent may do, and the fork that comes back as a Case
  - slug: rule-subagent-guppi
    type: rule
    purpose: Governs Work Mode's subagents — they execute the Spec's tasks, never decide, and return a fork as a Case
```

## Case 108 — the `## Insight` section of a clustered lesson

> **context:**
> Twenty `clustered` lessons carry no `## Insight` section. The synthesis sets the `insight` field in the frontmatter, and nothing writes the section `lessons/schema.md` requires. They are 20 of lint's 125 schema findings. Deferred as 96 in session K, with its `purpose` cut short in the yaml and on `decision-case-96`.

> **problem:**
> Either the synthesis entry carries the section, or the schema stops asking for it. Both are a change of what a synthesis entry holds.

```then
defer:
  - slug: rule-synthesis
    type: rule
    purpose: A synthesis entry carries the `## Insight` section of the lesson it clusters, or the lessons schema stops requiring it
```
