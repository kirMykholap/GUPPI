# Brief — 2026-09-23, after the librarian's run on session 0034

Written by the librarian from `vault/raw/2026-09-23/0034/handoff.md`, the two `materialize.yaml`
the walk named (`2026-09-22/2046`, extended with 0 entries; `2026-09-23/0034`, 64 entries from the
ledger and 3 appended by the librarian's synthesis) and `tags.md`.

## Where things stand

- Plan Mode of session 0034 ratified Cases 354–362 (354.1–354.4, 355.1–355.2, 356.1–356.2, 357,
  358, 359, 360, 361, 362.1–362.2), 56 decision lines and one lesson (L42). Defer 352 was taken up
  by 356.1; the 2046 yaml marks its entry `superseded_by: '356.1'` and `rule-skill-hi` carries no
  `deferred_by` now.
- Work Mode, commit `f71b821`: the move of Case 354 in `guppi/generate.py`, `sprint.milestone_blocks`,
  `check_frontier` of Case 356 in `guppi/prespec.py`, `properties.single` of Case 362.1 in
  `guppi/lint.py`, with tests. The session's readings L57–L63: five passed
  (`estimate-generate-cascades`, `estimate-prespec-binds-a-sprint-line`, `estimate-harness-pipeline`,
  `estimate-case-protocol-ledger-line-form`, `estimate-prespec-reconciles`), two failed
  (`estimate-generate-fails-alone`, `estimate-sprint-migration-index-dissolved`).
- Not done by the session: every page, render and `read` line of the Spec — the pages and renders
  were written by this run, the `read` lines wait for the next session.
- This run: all 67 entries of the 0034 yaml applied; none `failed`, `incomplete`, `near` or
  `exists`; `unparsed` empty in both yamls. The ledger has 64 lines and the yaml accounts for all 64.
- Pages created: 15 decisions (354.1–362.2), 1 rule (`rule-one-judgment-one-implementation`, child
  of `rule-claude-md`), 3 estimates (`estimate-sprint-moves-a-passed-over-item`,
  `estimate-sprint-drops-an-emptied-milestone`, `estimate-one-judgment-one-implementation-followed`),
  2 lessons, 1 insight by synthesis (`insight-workflow-ratified-content-changed-on-the-agents-own-finding`).
- Pages updated: 12 rules, 24 estimates (17 by Cases, 7 by readings), 1 decision (`decision-case-347`,
  a History line by Case 358, applied with no error), 2 insights (`actioned` by 359 and 360),
  2 lessons (clustered by synthesis), 1 entity (`entity-sprint-migration`, by the move of `generate`).
- Synthesis: `lesson-spec-text-repaired-after-ratification-without-a-showing` (L64) and
  `lesson-work-mode-check-widened-the-list-and-the-agent-acted` (session 1308) clustered into the
  new Insight, `open`, `severity` 2. `lesson-ledger-ratification-with-a-new-item-lost-its-block`
  (L42) found no pair and stays `new`.
- Cleanup moved 5 pages to the archive: `decision-case-352` (superseded by 356.1) and the four
  clustered lessons of the two Insights actioned by 359 and 360.
- Renders: `CLAUDE.md` holds the marker of `rule-one-judgment-one-implementation` after
  `rule-agent-writing`; `vault/wiki/insights/schema.yaml` parses and holds `single: [addressed_by]`;
  lint gives no finding on `insights/schema`.

## Readings due

Two Estimates stand `failed` and 29 stand `pending`. Every target stands `draft`:
`entity-sprint-migration` and each rule named below.

Failed:

- `estimate-generate-fails-alone` — `rule-page-generation` — read L58: the Criterion expects "an
  update with no content in the Spec; applied by hand", the code prints "…; nothing applied" since
  case 320.
- `estimate-sprint-migration-index-dissolved` — `entity-sprint-migration` — read L63: two live
  pointers at `index.md` stand, `guppi/materialize.py:11` and the Given of
  `estimate-case-protocol-case-form` (its line 18, unchanged by this run).

From an unticked `- [ ] read …` line of `vault/raw/2026-09-23/0034/spec.md`:

- `estimate-sprint-moves-a-passed-over-item` — `rule-sprint` — L63.
- `estimate-sprint-drops-an-emptied-milestone` — `rule-sprint` — L112.
- `estimate-hi-writes-frontier` — `rule-skill-hi` — L148, L377, L446.
- `estimate-brief-written` — `rule-brief` — L187.
- `estimate-case-protocol-loaded` — `rule-case-protocol` — L240, L296, L379, L448.
- `estimate-case-protocol-case-form` — `rule-case-protocol` — L241, L297.
- `estimate-case-protocol-acknowledging-reply` — `rule-case-protocol` — L298.
- `estimate-prespec-checks-the-plan` — `rule-prespec` — L378, L447.
- `estimate-documentation-completes` — `rule-documentation` — L491.
- `estimate-decisions-schema-checked` — `rule-decisions-schema` — L541, L802.
- `estimate-agent-writing-followed` — `rule-agent-writing` — L587.
- `estimate-one-judgment-one-implementation-followed` — `rule-one-judgment-one-implementation` — L678.
- `estimate-claude-md-rendered` — `rule-claude-md` — L679.
- `estimate-insights-schema-checked` — `rule-insights-schema` — L721, L805, L845.
- `estimate-lint-catches` — `rule-lint` — L801.
- `estimate-entities-schema-checked` — `rule-entities-schema` — L803.
- `estimate-estimates-schema-checked` — `rule-estimates-schema` — L804.
- `estimate-lessons-schema-checked` — `rule-lessons-schema` — L806.
- `estimate-rules-schema-checked` — `rule-rules-schema` — L807.
- `estimate-page-schemas-one-file-per-rule` — `rule-page-schemas` — L808.

No read line in the session's Spec; the place is the page's `method`:

- `estimate-carry-over-writes` — `rule-carry-over` — pytest over the skill's render, plus one live
  reading of a carried-over session; its read line L326 of the 2046 Spec moved to the archive
  with that unit in this run.
- `estimate-generate-ticks-the-spec` — `rule-page-generation` — pytest with a Spec beside the yaml,
  plus one reading of the session's `spec.md` after the librarian's run.
- `estimate-atomicity-rendered` — `rule-atomicity` — `make lint`, `render --check` exit 0, the text
  between the markers of `case-schema.md` read by hand after the render.
- `estimate-session-phases-in-order` — `rule-session` — by hand at the close of a session.
- `estimate-synthesis-keeps-actioned-by-the-mark` — `rule-synthesis` — the yaml and the brief after
  a librarian's run on the first marked lesson clustered under an `actioned` Insight.
- `estimate-sprint-migration-leftovers-gone` — `entity-sprint-migration` — the tree by hand at the
  close of the sprint.
- `estimate-sprint-migration-lint-clean` — `entity-sprint-migration` — `make lint` exit 0, or only
  unread lines on the sprint page's own Estimates.
- `estimate-sprint-migration-merges` — `entity-sprint-migration` — `make test` on the last commit
  of `migration`, then `git log` of `main` after the merge.
- `estimate-sprint-migration-rule-class-files-dissolved` — `entity-sprint-migration` — the four
  commands of its `method`, `make lint` exit 0 among them.

## Deferred

One item. The two Insights of the previous brief went `actioned` by Cases 359 and 360, and the
defer 352 of `rule-skill-hi` was retired by 356.1. The 0034 yaml has no `defer` entry, and every `defer` entry of the 2046 yaml is
`superseded_by`.
`rule-work-mode`, `rule-subagent-guppi`, `rule-morph`, `rule-spec-box` and
`insight-workflow-code-live-before-the-page-it-reads` are named by the sprint page and are not
listed here (case 229.4).

1. `insight-workflow-ratified-content-changed-on-the-agents-own-finding` — `severity` 2, standing
   in 1 brief. Pattern: after ratification the agent finds a gap, an error or a wider scope in what
   the person signed and repairs it itself, naming the repair after the fact, instead of showing the
   changed Case for a new sign. Proposal: `rule-case-protocol` could say that any change of a
   ratified Case's text or scope found by the agent is a changed Case, shown again and ratified
   before it is written or acted on.

## Flags

- No entry of the 0034 yaml is marked `incomplete`, `failed`, `near` or `unparsed`. The 2046 yaml
  keeps the five `incomplete: [criterion]` entries of the previous run (lines 2, 4, 6, 9, 20), all
  `superseded_by`; no page was written from them.
- Two Estimates stand `failed`: `estimate-generate-fails-alone` and
  `estimate-sprint-migration-index-dissolved` (Readings due).
- The move of Case 354, by the stdout of `generate` and the History of `entity-sprint-migration`
  (case 354.4):
  - `rule-work-mode`, milestone Slice 3b — Work Mode, moved to the Backlog: passed over in 29
    sessions in a row — 0034, 2046, 1121, 0014, 1853, 1315, 0019, 2106, 1749, 1308, 0958, 0740,
    0527, 2253, 2054, 1957, 1252, 1119, 2238, 1955, 2225, 1809, 1448, 1110, 1633, 1229, 1029,
    0747, 0652.
  - `rule-subagent-guppi`, milestone Slice 3b — Work Mode, moved to the Backlog: the same 29
    sessions.
  - Slice 3b — Work Mode left the Milestones; Slice 4 is the current milestone of `sprint.md`.
  The three History lines end `· generate`, as the handoff expected.
- Contradictions named as known at pre-spec, not repaired: the `writes nothing else` sentence of
  `rule-page-generation`; the `needs nothing` line of `estimate-prespec-binds-a-sprint-line`; the
  archive paths — all 33 archived Frontiers sit under `<date>/<HHMM>/raw/`; the render guard of
  Case 360, as for `rule-agent-writing`.
- `estimate-sprint-migration-rule-class-files-dissolved` needs `make lint` exit 0 by its `method`,
  which `estimate-sprint-migration-lint-clean` expects only at the close of the sprint. From the
  handoff.
- The handoff counts 22 Estimates whose Criterion this session replaces; the 0034 yaml changes 20
  distinct Estimates by Cases (17 updates, 3 creates), and 20 Estimates have a read line in the
  0034 Spec.
- The handoff reports CRLF warnings in five files after Edit calls, normalized to LF with `sed`;
  the cause was not established.
- Two lessons of the session name one pattern: the agent changed ratified Spec text without
  showing it again (L64), the same pattern Case 358 signed after the fact for Case 347. Synthesis
  made it an Insight (Deferred).
- Stale defers, from lint: `rule-work-mode` and `rule-subagent-guppi` 31 times since case 29,
  `rule-morph` 1 time since case 239. All three are on the sprint page, the first two now in its
  Backlog.
- `rule-spec-box`: three findings — missing `kind`, missing `estimates`, orphan. A placeholder of
  Slice 5 on the sprint page.
- No MOC candidate: no input this run names a threshold crossed.
- `guppi archive` moved the unit 2046 of 2026-09-22 to `vault/archive/migration/2026-09-22/2046/raw`
  and kept 0034, the session of the run.
- `make lint`: 100 findings, exit 1 — 62 on 31 legacy decision pages (`missing section ## Context`
  / `## Problem`), 31 `unread` (29 `pending`, 2 `failed`), 3 on `rule-spec-box`, 3 `deferred`
  counters, 1 `unmigrated: 23 pages in the shape before case 193`. The previous brief had 92; the
  growth is the `unread` lines of the Estimates this run made due.

## Next session

Cases — what needs a decision:

- `estimate-generate-fails-alone` failed: its Criterion expects "applied by hand", the code prints
  "nothing applied" since case 320. From the handoff and the reading L58.
- `estimate-sprint-migration-index-dissolved` failed: the pointers at `index.md` in
  `guppi/materialize.py:11` and in the Given of `estimate-case-protocol-case-form`. From the
  handoff and the reading L63.
- The conflict between the `method` of `estimate-sprint-migration-rule-class-files-dissolved`
  (`make lint` exit 0) and `estimate-sprint-migration-lint-clean` (exit 0 only at the close of the
  sprint). From the handoff.
- The `writes nothing else` sentence of `rule-page-generation`, a contradiction named known at
  pre-spec. From the handoff.
- The `needs nothing` line of `estimate-prespec-binds-a-sprint-line`, a contradiction named known
  at pre-spec. From the handoff.
- The archive paths of the Frontiers under `<date>/<HHMM>/raw/`, a contradiction named known at
  pre-spec. From the handoff.
- The render guard of Case 360, a contradiction named known at pre-spec. From the handoff.

Work — what is done without a decision:

- Take the pending readings of Readings due, by slug: `estimate-sprint-moves-a-passed-over-item`,
  `estimate-sprint-drops-an-emptied-milestone`, `estimate-hi-writes-frontier`,
  `estimate-brief-written`, `estimate-case-protocol-loaded`, `estimate-case-protocol-case-form`,
  `estimate-case-protocol-acknowledging-reply`, `estimate-prespec-checks-the-plan`,
  `estimate-documentation-completes`, `estimate-decisions-schema-checked`,
  `estimate-agent-writing-followed`, `estimate-one-judgment-one-implementation-followed`,
  `estimate-claude-md-rendered`, `estimate-insights-schema-checked`, `estimate-lint-catches`,
  `estimate-entities-schema-checked`, `estimate-estimates-schema-checked`,
  `estimate-lessons-schema-checked`, `estimate-rules-schema-checked`,
  `estimate-page-schemas-one-file-per-rule`, `estimate-carry-over-writes`,
  `estimate-generate-ticks-the-spec`, `estimate-atomicity-rendered`,
  `estimate-session-phases-in-order`, `estimate-synthesis-keeps-actioned-by-the-mark`,
  `estimate-sprint-migration-leftovers-gone`, `estimate-sprint-migration-lint-clean`,
  `estimate-sprint-migration-merges`, `estimate-sprint-migration-rule-class-files-dissolved`.
- The unticked boxes of the Specs are their `read` lines alone: 30 in
  `vault/raw/2026-09-23/0034/spec.md`. The four read lines of the 2046 Spec (L54, L119, L326,
  L374) are now at `vault/archive/migration/2026-09-22/2046/raw/spec.md`; nothing will tick them,
  and three of their Estimates have a read line in the 0034 Spec.
- No ledger line of 0034 was left unapplied. The tree at the close of this run holds only the
  librarian's own writes; this brief's commit covers `vault`, `CLAUDE.md` and `.claude`.

## Readings at the close

- `make test`: 581 passed, 2 skipped.
- `make lint`: 100 findings, exit 1.
- Pages: 59 rules, 104 estimates, 50 lessons, 19 insights, 496 decisions, 4 entities.
