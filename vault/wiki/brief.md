# Brief — 2026-09-18, after session 1957 of 2026-09-18 (the sprint page names its deferred targets; the /hi Insight rejected; Slice 3b deferred)

Written by the librarian from `raw/2026-09-18/1957/handoff.md`, the yamls of
`raw/2026-09-18/1252` and `raw/2026-09-18/1957`, and the index Greps.

## Where things stand

- Ratified in session 1957: 245 (`update` `entity-sprint-migration`, the Slice 3b item of
  `rule-work-mode` names `insight-workflow-code-live-before-the-page-it-reads`), 246
  (`update` `insight-hi-skill-substitution-checked-by-a-model-call`, rejected: `actioned`,
  `addressed_by: [[decision-case-246]]`, `rule-skill-hi` unchanged), 247 (superseded by
  249), 249 (`update` `entity-sprint-migration`, the Slice 5 item of
  `estimate-sprint-migration-merges` names `rule-git-context` and `rule-github-issues`, read
  by `estimate-sprint-migration-leftovers-gone`); deferred 248 (`rule-work-mode`,
  `rule-subagent-guppi`, Slice 3b, a `purpose` per target). Readings `passed` in the ledger:
  `estimate-render-harness-ticks-the-spec`, `estimate-sprint-renders-the-backlog`. One
  lesson.
- Code: none. Tests 425 green, `make style` clean. Commit `e4f0351` on `migration`: the
  session folder and the two `read` lines of `raw/2026-09-18/1252/spec.md` ticked.
- Frontier of 1957: 7 items — F5, F4, F7 closed as `work`; F2, F3, F6 by Case; F1 (Slice
  3b) deferred by 248.
- Not done in the session: every page change of the Spec (this run); Slice 3b (defer 248,
  the next session's first item); `estimate-carry-over-writes` (a live `/carry`, none yet);
  the three `estimate-sprint-migration-*` readings (the close); `estimate-hi-no-read-calls`
  stays in the old shape (untouched by choice).
- This run. `materialize` walked two units: 1252 extended with 0 entries (its line 8
  printed "changed since the yaml was written; entry left alone" — Flags), 1957 written with
  9 entries, `unparsed: []`, no `failed`, no `incomplete`, no synthesis entry appended.
  `generate`: 16 pages written or changed from 1957, 0 from 1252; stderr empty; exit 0;
  every entry of 1957 `applied` but 247 (`superseded_by: '249'`, not applied). Counts of
  the 1957 yaml:
  - `create`: 1 lesson (`lesson-defer-to-a-milestone-leaves-the-sprint-page-silent`, error,
    tags `sprint`, `workflow`, `session`, `new`); 5 Decision pages (245, 246, 247, 248, 249).
    No new tag.
  - `update`: 2 entity entries applied on `entity-sprint-migration` (245 on the Slice 3b
    line, 249 on the Slice 5 line; 247's `replace` of the same line superseded and not
    applied); 1 insight entry (`insight-hi-skill-substitution-checked-by-a-model-call`,
    `actioned`).
  - `defer`: 2 targets in 1 Case (248): `rule-work-mode`, `rule-subagent-guppi`, both
    `exists: true`, `deferred_by` now `decision-case-183`, `-206`, `-218`, `-231`, `-242`,
    `-248`.
  - `estimate`: 2 reading entries, both `passed`, `checked` 2026-09-18. `lesson`: 1.
  - Cascade: `rule-render-harness` and `rule-sprint` `draft` → `built` (no other Estimate
    of theirs `pending`); `lesson-hi-substitution-refused-when-the-permission-classifier-is-unavailable`
    and `lesson-hi-substitution-fails-when-the-login-has-lapsed` `clustered` → `archived`
    (children of an `actioned` Insight, case 104.2); `decision-case-247` `superseded`.
  - The Spec `raw/2026-09-18/1957/spec.md`: `generate` ticked 3 page lines (36, 69, 136);
    247's page line (102) stays `[ ]` by design; the three `- [ ] `uv run guppi sprint`
    at the librarian's run` lines (37, 103, 137) stay `[ ]` — `sprint` ticks no Spec line
    (case 226 names `generate` and `render`); the Spec holds no `- [ ] read` line.
  - `cleanup`: 3 pages moved to `archive/migration/2026-09-18/1957/` —
    `decisions/decision-case-247`, the two `/hi` lessons above. `render`: exit 0, stderr
    empty, no governed file changed (`CLAUDE.md` and `.claude/` clean after the run).
  - `guppi sprint` (step 5): exit 0, stderr empty; `sprint --check` exit 0.
    `vault/wiki/sprint.md`: Slice 3b whole — the `rule-work-mode` line carries the second
    wikilink `[[insight-workflow-code-live-before-the-page-it-reads]]` and six
    `deferred_by`, the `rule-subagent-guppi` line six `deferred_by`, both `draft`; Slice 4
    one line, one item; Slice 5 one line, four names — the new text of the `-merges` item
    is not visible until Slice 5 is current; the Backlog one line; the three Done-when
    lines `pending`.
  - `deferred_by` now: `rule-work-mode`, `rule-subagent-guppi` by six decisions (above);
    `rule-spec-box` by `-207`, `-219`, `-232`; `rule-git-context`, `rule-github-issues` by
    `-220`, `-243`; `rule-morph` by `-239`;
    `insight-workflow-code-live-before-the-page-it-reads` by `-238`.

## Readings due

Four Estimates stand `pending`, none `failed`. The 1957 Spec carries no `- [ ] read` line;
the place of each reading is the page's `method`.

- `estimate-carry-over-writes` — `rule-carry-over` (`draft`); read: pytest over the skill's
  render, plus one live reading of a carried-over session — a live `/carry`, none yet
  (`method`).
- `estimate-sprint-migration-lint-clean` — `entity-sprint-migration` (`draft`); read:
  `make lint`, exit 0 — or only `unread` lines on the Estimates of
  `entity-sprint-migration`; at the close of the sprint (`method`).
- `estimate-sprint-migration-leftovers-gone` — `entity-sprint-migration` (`draft`); read:
  one reading of the tree by hand at the close of the sprint, each path and decision named
  in the estimate line (`method`); the Slice 5 item of `-merges` names `rule-git-context`
  and `rule-github-issues` as read here (249).
- `estimate-sprint-migration-merges` — `entity-sprint-migration` (`draft`); read: `make
  test` on the last commit of `migration`, then `git log` of `main` after the merge
  (`method`).

Read this session and `passed` on their pages: `estimate-render-harness-ticks-the-spec`
(against the Spec of `archive/migration/2026-09-17/1119/raw/spec.md`, the five render lines
ticked, the read line 260 still `[ ]`) and `estimate-sprint-renders-the-backlog`; their
rules `rule-render-harness` and `rule-sprint` are `built`.

## Deferred

None. Every candidate is named by the sprint page (case 229.4) or is closed:

- Left out, the sprint page names them: `insight-workflow-code-live-before-the-page-it-reads`
  (`open`, severity 2, defer 238; since 245 in the text of the `rule-work-mode` item of
  Slice 3b — stood in 2 briefs); `rule-work-mode` and `rule-subagent-guppi` (defers 183,
  206, 218, 231, 242, 248; Slice 3b, the current milestone); `rule-git-context` and
  `rule-github-issues` (defers 220, 243; since 249 in the text of the
  `estimate-sprint-migration-merges` item of Slice 5 — stood in 3 briefs);
  `rule-spec-box` (defers 207, 219, 232; Slice 5); `rule-morph` (defer 239; Slice 5).
- Retired from the previous brief: `insight-hi-skill-substitution-checked-by-a-model-call`
  (item 2) — `actioned` by 246, rejected, `addressed_by: [[decision-case-246]]`; a third
  lesson with the same cause reopens it.

## Flags

- `materialize` on `raw/2026-09-18/1252/materialize.yaml`: "line 8 changed since the yaml
  was written; entry left alone" — the entry of line 8
  (`lesson-hi-substitution-fails-when-the-login-has-lapsed`, `applied` 19:22:57) stands as
  it is; the page was written by the run of 1252 and is archived by this one. No entry
  marked `incomplete`, `failed`, `near` or `unparsed` in either yaml; `unparsed: []` in both.
- The defer of 238 (`insight-workflow-code-live-before-the-page-it-reads`) still carries
  no `purpose` in the 1252 yaml (`incomplete: [purpose]`, applied); the handoff says it
  closes with Slice 3b.
- Index check: no `create` outside estimates but the lesson. Its `root_cause` against the
  Grep `^(root_cause|deferred_by):` over `wiki/lessons/` — 35 lines (33 live pages, 2
  schema examples): not the same page and not a near one. No page opened for it.
- Synthesis: `lesson-defer-to-a-milestone-leaves-the-sprint-page-silent` against the 35
  lesson lines and the Grep `^(pattern|deferred_by):` over `wiki/insights/` — 15 lines (13
  live pages, 1 `deferred_by`, 1 schema example). One candidate the line did not settle,
  `insight-workflow-contract-change-leaves-its-derived-text-stale` (`actioned`, severity
  0): opened; its pattern is one contract text in two places with only one changed and no
  pointer back (Estimate criteria quoting a rule, a Render paragraph); the lesson is a
  second decision never written — an `update` of the sprint page beside the defer — not a
  derived text. Not clustered. `insight-workflow-code-live-before-the-page-it-reads` is not
  it (the handoff said so; the pattern is code live before its page). The lesson stays
  `new`.
- The Spec lines `- [ ] `uv run guppi sprint` at the librarian's run` (37, 103, 137 of the
  1957 Spec) stand unticked: no script ticks a `sprint` line (case 226 covers `generate`
  and `render`); Retro counts them as unticked. The two task lines of 247 stay `[ ]` by
  design.
- The two Slice 5 items `rule-git-context` and `rule-github-issues` are read by
  `estimate-sprint-migration-leftovers-gone`, an item of Slice 4 — the place is the
  person's choice (handoff).
- F7 of 1957: the contradiction flag of the previous brief on
  `lesson-plan-mode-frontier-refused-on-the-client-text` against
  `lesson-permissions-reading-taken-by-the-agent-who-cannot-see-the-prompt` closed as
  `work` in the session: the lessons complement, 237 holds the promise; the handoff asks
  that it not be raised again unless a third lesson lands. Both lessons stand `new`, as
  they were.
- `estimate-hi-no-read-calls` (`rule-skill-hi`) stays in the shape before case 193 by
  choice (246 rejected the Render change that would recut it); one of the 29 `unmigrated`.
- Handoff flags, each a Case of the next Plan Mode:
  1. Slice 3b — `rule-work-mode`, `rule-subagent-guppi` (defer 248, the next session's
     first item), with the sentence of `insight-workflow-code-live-before-the-page-it-reads`
     written into `rule-work-mode`; nothing else is open from session 1957.
- `rule-spec-box` (placeholder): lint `schema: missing field kind`, `missing field
  estimates`, `orphan: no other live page names it in its frontmatter`.
- Stale defers: `rule-work-mode` and `rule-subagent-guppi`, `deferred: 18 times since case
  29` (lint), 22 briefs; on the sprint page, not in Deferred (229.4).
- MOC candidates: none new. Contradictions: none new.
- Lint at the close of the run, 73 findings (75 after the previous run):
  - 62 × `decisions/decision-case-<1–28>: schema: missing section ## Context` /
    `## Problem` (31 pages, the Cases 1–28 — `estimate-sprint-migration-lint-clean`).
  - `rules/rule-spec-box: schema: missing field kind`, `missing field estimates`,
    `orphan: no other live page names it in its frontmatter` (3).
  - `rules/rule-morph: deferred: 1 time since case 239`
  - `rules/rule-subagent-guppi: deferred: 18 times since case 29`
  - `rules/rule-work-mode: deferred: 18 times since case 29`
  - `estimates/estimate-carry-over-writes`, `-sprint-migration-leftovers-gone`,
    `-sprint-migration-lint-clean`, `-sprint-migration-merges`: `unread: pending` (4).
  - `estimates: unmigrated: 29 pages in the shape before case 193` (29 before this run).
  - No `render:` line and no `sprint:` line: the first two steps of `make lint` are green.

## Readings at the close

- `make test`: 425 passed.
- `make lint`: 73 findings, exit 1 (the list above).
- Live pages: rules 44, estimates 66, lessons 33, insights 13, decisions 343, entities 2.
  Archived this run: 1 decision page (`decision-case-247`), 2 lesson pages
  (`lesson-hi-substitution-refused-when-the-permission-classifier-is-unavailable`,
  `lesson-hi-substitution-fails-when-the-login-has-lapsed`).
