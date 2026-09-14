# Handoff — 2026-09-13, Slice 3c: the archive of raw/, the ledger of a session

## Notes from memory

- The owner opened the session on the archive of `raw/` and drove it to its end: the
  archive by whole unit rather than by cut lines (he proposed cutting the ledger, then
  agreed cutting breaks the line-number pointers), one archive root `vault/archive/` in
  place of the old August folder and of `vault/archived/`, and the ledger of a session
  (Case 103) once he saw that a date-level ledger splits a session across midnight and
  makes "the ledger one level up" an exception in the archive layout. He chose to keep
  an `actioned` Insight live (104.3 archives only an `open` one with no live child) and
  to archive a `superseded` Decision at once (104.1). `decided_by` was dropped for good:
  `origin` is the one pointer, resolved in `raw/` or in the archive, never rewritten.
- Case 100.2 was shown again at pre-task: the archive step runs after the brief, not
  after the render, because the brief reads the yamls the walk named and the archive
  moves them. The librarian's frame rendered at this session's start does not yet carry
  the step; the render of this run adds it, so this run itself has no step 5 — the
  first live archive was run by hand in Work Mode and is recorded in
  `estimate-raw-archive`.
- Two forms coexist on 2026-09-13: the date-level `raw/2026-09-13/ledger.md` (the lines
  of Cases 100–109 and the readings up to 22:18) and the session ledger
  `raw/2026-09-13/0652/ledger.md` (from 22:36 on). Both units read the same Spec,
  `0652/spec.md`. `guppi materialize` walks `2026-09-13` first, then `2026-09-13/0652`.
- Two lessons of the session sit on the same Insight,
  `insight-session-vault-knowledge-not-loaded`: the heredoc trap hit twice with its lesson
  live. The transcript lesson (`lesson-transcript-omits-text-emitted-before-tool-calls`)
  reopens what case 70 withdrew: the loss is the transcript's, not the hook's; it may
  cluster with `insight-ledger-hook-reads-only-the-final-text`, whose archived child
  described the same loss with the wrong cause.
- Case 100.3 and 100.5 are superseded within the same Spec by 103.5 and 103.6; their
  entries carry a `change` only. After 104.1 the cascade archives `decision-case-100.3`
  and `decision-case-100.5` in this same run, together with the 24 `superseded` decisions
  of earlier sessions. That is expected, not a flag.
- `estimate-cleanup-moves` keeps a prose criterion (before case 72) that names
  `vault/archived/`; the `### case 102.2` block is the criterion that holds now. Nothing
  to repair.

## Direct instructions to the librarian

- `Materialize 2026-09-13.` The walk covers two units of the date: the date-level yaml
  `raw/2026-09-13/materialize.yaml` and the session yaml
  `raw/2026-09-13/0652/materialize.yaml`. The four earlier dates are in
  `vault/archive/migration/<date>/raw/` and are no longer walked.
- Two entries are `incomplete: [category]`: the deletes outside the vault, `raw-notes`
  (100.6) and `old-archive` (102.1). `generate` applies them with a stdout line, as it
  did for `old-harness` of case 6. Not a repair.
- The create of `rule-ledger-tail` (101.2) lands on a placeholder page; `generate` fills
  it (101.1) with the History line `created over placeholder`. Check that the page
  carries `kind: Leaf`, `estimates: [estimate-ledger-tail]`, `deferred_by` empty or
  absent after the supersedes of 95 by 100.1.
- Index check: `rule-raw-archive` ("Keeps raw/ to the sessions not yet turned into
  pages…") may read near `rule-cleanup`; they are different scripts over different
  things (pages vs the raw of a session). `rule-ledger-tail` is the placeholder filled,
  not a new page.
- `estimate-generate-writes` gets four blocks in this run (101.1, 104.1, 104.2, 104.3,
  105.3 — five); `estimate-lint-catches` loses the block of 100.3 (`remove_criterion`)
  and gains 103.5; `estimate-materialize-walks-dates`, `estimate-generate-walks-dates`,
  `estimate-pretask-reconciles`, `estimate-materialize-assembles`,
  `estimate-cleanup-moves`, `estimate-documentation-completes`, `estimate-hi-no-read-calls`,
  `estimate-hi-writes-frontier`, `estimate-ask-finds`, `estimate-retro-loads` each gain
  one. The readings of `estimate-raw-archive`, `estimate-lint-catches` and
  `estimate-ledger-write-lifts` are in the session ledger and fold into their pages.
- The render of this run writes: `.claude/agents/librarian-guppi.md` (the archive step
  between brief and close, `vault/archive/` in the ban), `.claude/agents/ask-guppi.md`
  (105.1), `.claude/skills/hi/SKILL.md` (the `Tail:` line of `rule-ledger-tail` after
  `rule-github-issues`, the Frontier sentence), `.claude/skills/retro/SKILL.md`
  (109.1), `CLAUDE.md` (109.2). Every stderr line of the render is a flag.
- `cleanup` now writes under `vault/archive/migration/2026-09-13/0652/<category>/`; the
  24 superseded decisions and the two of this Spec go there. Report the count.
- Do not run `guppi archive` yourself: the frame you run under has no such step, and
  today's units are the session's and the day's.
- Brief: the Deferred list holds 106 (`rule-skill-hi`, the render after the pull), 107
  (`rule-work-mode`, `rule-subagent-guppi`), 108 (`rule-synthesis`, the `## Insight`
  section). Name in "What the next session does first": the readings that wait for the
  next session start — `estimate-settings`, `estimate-hi-no-read-calls`,
  `estimate-hi-writes-frontier`, `estimate-pretask-reconciles` (live), `estimate-ask-finds`
  (dispatch `ask-guppi` with the archived slug `estimate-agents-at-import-not-expanded`),
  `estimate-retro-loads` — and the readings against this run: `estimate-documentation-completes`,
  `estimate-close-commits`, `estimate-generate-writes`, `estimate-cleanup-moves`,
  `estimate-materialize-walks-dates`, `estimate-generate-walks-dates`,
  `estimate-materialize-assembles`, `estimate-ledger-tail` (live: `guppi tail` after your
  commit shows the readings written after it and nothing else).
- The next session's `/hi` carries a `Tail:` line for the first time; the first `guppi
  archive` in a librarian's run happens at the next session, moving `2026-09-13` (date
  level) and `2026-09-13/0652` if both are applied and covered.

## What actually got done

- Ratified and coded: Cases 100 (the archive of an applied unit, `guppi archive`),
  101 (`guppi tail`, the placeholder fill, the `/hi` tail), 102 (one root
  `vault/archive/`, `cleanup` under the session of the run), 103 (the ledger of a
  session: hook, materialize, generate, pretask, lint, the map and five schemas),
  104 (the three cascades), 105 (the slug against the archive: `ask-guppi`, `exists`
  by Case, `find` into the archive), 109 (rule-retro, rule-claude-md, insights schema).
  Deferred: 106, 107, 108.
- Code: `guppi/archive.py`, `guppi/tail.py` new; `ledger.py`, `materialize.py`,
  `generate.py`, `pretask.py`, `lint.py`, `cleanup.py`, `cli.py` changed; tests
  `test_archive.py`, `test_tail.py` new, six others extended: 299 green (267 before),
  `make style` clean.
- Files: the old `vault/archive/` (August, 49 folders) and `vault/raw/notes/` removed;
  `vault/archived/migration/` moved to `vault/archive/migration/`, the lesson of
  2026-09-12 under `2026-09-12/1156/lessons/`; the four dates 09-09…09-12 archived
  live by `guppi archive` under `vault/archive/migration/<date>/raw/` with the session
  folders of 09-12 beside as `<HHMM>/raw/`. `guppi lint` 133 findings before and after,
  `render --check` 0, `index --check` 0.
- By hand: `index.md` §1 and §4, glossary (six rows), `schema.md` of entities, rules,
  estimates, lessons, decisions, insights, `sprint.md` (Slice 3c rewritten, Done-when 1,
  Slice 5).
- Readings taken: `estimate-case-protocol-loaded`, `estimate-render-sync-reports`,
  `estimate-default-mode`, `estimate-hook-registry-rendered`, `estimate-permissions`,
  `estimate-render-harness-reproduces`, `estimate-claude-md-rendered` (the date-level
  ledger); `estimate-raw-archive`, `estimate-lint-catches`, `estimate-ledger-write-lifts`
  (the session ledger). Lessons: the transcript, the heredoc trap.
- Commits: `44e4e37` (the three governed files of the start), `c08c878` (the code and
  the vault moves), `57d68e2` (Retro), `5c4ea2a` (the last reading).
- Not done: 21 tasks of the Spec, all readings — 12 against this librarian run, 6
  against the next session start, plus the two render checks (`rule-cleanup` sentence,
  `CLAUDE.md` path) that this run's render answers.
