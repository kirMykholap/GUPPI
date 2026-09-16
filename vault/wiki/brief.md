# Brief — 2026-09-16, after session 1651 (Slice 3d: the Spec of session 1034 repaired and built)

Written by the librarian from `raw/2026-09-16/1651/handoff.md`, the yamls of
`raw/2026-09-15/2225`, `raw/2026-09-16/1034` and `raw/2026-09-16/1651`, and the index Greps.

## Where things stand

- Cases 193–200 closed in session 1651: the Rule-class files of the Estimate model
  (`estimates/schema.yaml`, `estimates/schema.md`, `index.md` §1–§3, §5, §7, §10, §12,
  `glossary.md`, `rules/schema.md`, `case-schema.md`), the Purpose and Render texts for
  189/190.x, the recut of five Estimates, `/carry`'s Render, the allow list.
- Spec 1034 built: `guppi/spec.py` prints the fork (190.5) and its docstring carries the
  mechanism (200.4); `guppi/materialize.py` derives nothing, lifts the Criterion into
  `sections.Criterion`, keeps `purpose`/`method` as fields, ignores the old keys, passes a
  `carry.md` unit by (189, 194.1, 190.3); `guppi/generate.py` writes `## Deferred` (186.1);
  `guppi/lint.py` reports `deferred: N times since case M` (186.3); tests 385 → 397;
  `decision-case-182/183/185` migrated; `## How it works` dropped on three pages;
  `decisions/schema.*` with `## Deferred`.
- Readings taken in the session, 11 `passed`: `estimate-materialize-shows`,
  `-lifts-a-lesson`, `-marks-exists`, `-fails-alone`, `-finds-a-rule-class-item`,
  `-skips-a-carried-over-unit`, `-walks-dates`, `estimate-spec-capture-offers-the-fork`,
  `estimate-generate-writes` (186.1), `estimate-lint-catches` (186.3),
  `estimate-plan-mode-names-its-estimates`. One more, `estimate-retro-commit-gates`
  `passed`, in the 1034 ledger.
- Commit `9e77e59` on `migration`. Lint 70 → 64 before the librarian's run.
- Not done in the session: the recut of the three Estimates of 186 (case 191); the sentence
  on a written Criterion winning (next Plan Mode); the readings listed below.
- This run. `materialize` walked three units: 2026-09-15/2225 extended with 0 entries
  (four of its entries gained `superseded_by` from 188 and 191), 2026-09-16/1034 written with
  37 entries, 2026-09-16/1651 with 39. `generate`: 46 pages written or changed from 1034,
  42 from 1651; stderr empty. Counts of the yamls, applied entries:
  - 1034: `create` 13 estimates, 1 rule (`rule-carry-over`); `update` 5 estimates, 10 of
    rules (9 pages), 3 Rule-class files (by hand); `defer` 3 rules (191), 1 insight (192),
    all four `exists`; 1 estimate line.
  - 1651: `update` 6 estimates, 9 of rules (8 pages), 10 of Rule-class files (6 files, by
    hand); 1 lesson (`lesson-plan-mode-frontier-refused-on-the-client-text`, `new`); 11
    estimate lines; 2 entries `superseded_by` (195 → 200.1, 196.4 → 200.4), not applied.
  - Index check: `rule-carry-over` against the 53 lines of the rules Grep — no duplicate,
    no `near`. Synthesis: the lesson against 30 lesson lines and 12 insight lines — no
    shared root cause; `insight-session-vault-knowledge-not-loaded` opened and not
    clustered (its pattern is a fact that never reached the session; the lesson's cause is a
    loaded rule ranked below the client's text).
  - `cleanup`: 4 pages moved to `archive/migration/2026-09-16/1651/decisions/` —
    `decision-case-182`, `-185`, `-195`, `-196.4`. `render`: `CLAUDE.md`,
    `.claude/settings.json`, `.claude/skills/carry/SKILL.md` (new),
    `.claude/skills/pre-task/SKILL.md`, `.claude/agents/librarian-guppi.md`;
    `render --check` exit 0.
  - `deferred_by` now: `rule-page-generation`, `rule-lint`, `rule-pretask` by
    `decision-case-191`; `rule-work-mode`, `rule-subagent-guppi` by `decision-case-183`;
    `insight-ledger-hi-tied-to-its-session-by-position` by `decision-case-192`.
    `rule-plan-mode`, `rule-materialize`, `rule-case-protocol` carry none.
- `sprint.md` changed as the handoff instructed: the Slice 3d clause and the closing line.

## Readings due

Ten Estimates stand `pending`, none `failed`. Each is a recut page with its Criterion whole,
no `### case N` block; the target Rule stands `draft` in every case.

- `estimate-materialize-assembles` — `rule-materialize` (`draft`), Criterion of 194.1;
  read: pytest in `tests/test_materialize.py` and the live half by hand — this librarian
  run (1651 Spec, unticked `read estimate-materialize-assembles`).
- `estimate-materialize-marks-superseded` — `rule-materialize` (`draft`), Criterion of 189;
  read: the tests of the supersedes mark in `tests/test_materialize.py` plus one live
  reading of a librarian's run — this run marked 195 `superseded_by: 200.1` and 196.4
  `superseded_by: 200.4`, `generate` applied neither, `cleanup` archived both decision
  pages. No `- [ ] read` line in either Spec; the place is the page's `method`.
- `estimate-case-protocol-loaded` — `rule-case-protocol` (`draft`), Criterion of 188 as
  written in the Spec; read: one reading at a session start, by hand, plus the preview
  cases of `tests/test_ledger.py` — the first turn of the next session, after the render
  (1651 Spec, unticked).
- `estimate-case-protocol-case-form` — `rule-case-protocol` (`draft`), 188; read: one
  reading by hand of the Cases of a session, at its close (1034 Spec, unticked).
- `estimate-case-protocol-acknowledging-reply` — `rule-case-protocol` (`draft`), 188; read:
  one reading by hand of the first acknowledging reply of a session (1034 Spec, unticked).
- `estimate-case-protocol-ledger-line-form` — `rule-case-protocol` (`draft`), 188; read:
  one reading by hand of `case-schema.md`, `index.md` §4 and the ledger paragraph of the
  Render, at a session start (1034 Spec, unticked).
- `estimate-permissions` — `rule-permissions` (`draft`), 200.5; read: the nine entries in
  the rendered `.claude/settings.json` and the JSON case of `tests/test_render.py`; the live
  probe at the next `/hi` in Plan Mode — one edit of `frontier.md`, recorded as asked or not
  asked — or a live `/carry` (1651 Spec, unticked).
- `estimate-carry-over-writes` — `rule-carry-over` (`draft`), 196.1; read: pytest over the
  skill's render plus one live reading of a carried-over session — a live `/carry` (1651
  Spec, unticked).
- `estimate-end-of-work-order` — `rule-end-of-work` (`draft`), 196.2; read:
  `make test-end-of-work` over `tests/test_gate.py` and the live reading of the order by
  hand — the order of session 1651: retro, handoff, this librarian run (1651 Spec, unticked).
- `estimate-brief-written` — `rule-brief` (`draft`), 197; read: one reading by hand after
  the first librarian run, recorded in the estimate line — this brief (1651 Spec, unticked).

Not `pending`, named by the handoff as due: `estimate-pretask-reconciles` (`passed`) — the
pre-task skill after the render of this run.

## Deferred

1. **`insight-ledger-hi-tied-to-its-session-by-position`** — `open`, severity 1, case 192.
   Pattern: the event log ties a `hi` line to its session by the `session-start` lines around
   it, not by an id; any start missing from the window or added to it sends the `hi` to the
   wrong session and the ledger writer refuses. Proposal: Case 111 already writes a stamped
   `<stamp> hi` line from the `UserPromptSubmit` hook and reads the window by that stamp
   with the old rule as a fallback; the readings of `estimate-event-log-records` and
   `estimate-ledger-write-lifts` at the next `/hi` decide whether the binding by position can
   be retired. The defer of 192: "Retire the binding by position: `pretask.resolve_session`
   resolves the session from the stamped `hi` and walks back to the date of that `hi`,
   instead of falling back to the last `session-start` of today's event log; the ledger hook's
   window is checked against it so the two readers do not disagree at midnight. Closes all
   four children of the Insight. Needs its own Estimate and one live reading across
   midnight." In Plan Mode a Case whose `recommend` starts from that Proposal, ending in an
   `update` of the Insight (`status: actioned`, `addressed_by`), a rejection written the same
   way, or a `defer` with the Insight as its target. (stood in 3 briefs)
2. **`rule-work-mode`** — case 183, Slice 3b: the Spec as tasks with code, the ticked boxes,
   the test of each Estimate written first and turned green; after Slice 3d and before Slice
   4. Placeholder, `draft`; lint: `deferred: 13 times since case 29`. (stood in 17 briefs)
3. **`rule-subagent-guppi`** — case 183, Slice 3b: what a subagent may do in Work Mode, and
   the fork that comes back to the main agent as a Case; with `rule-work-mode`. Placeholder,
   `draft`; lint: `deferred: 13 times since case 29`. (stood in 17 briefs)
4. **`rule-page-generation`** — case 191 (supersedes 182), Slice 3d. "`generate` without
   Criterion blocks and without `remove_criterion`; the Criterion replaced whole; the fields
   `purpose`, `method`, `checked`; the recut of `estimate-generate-writes` and
   `estimate-generate-walks-dates` at this touch. The change of case 186.1 — the
   `## Deferred` section on a decision page — is not part of this defer and stands ratified."
   `deferred_by: decision-case-191`. (stood in 4 briefs)
5. **`rule-lint`** — case 191, Slice 3d. "The finding `unread` on every `pending` and `failed`
   Estimate; the Estimate schema without `## Context` and without the `## Method` section; the
   `unmigrated` counter for the transition, and the removal of the old shape when it reaches
   zero. The change of case 186.3 — the `deferred` finding on a placeholder — is not part of
   this defer." `deferred_by: decision-case-191`. (stood in 3 briefs)
6. **`rule-pretask`** — case 191, Slice 3d. "Pre-task checks the Estimates of the rule named
   in `context` and asks `ask-guppi` whether an unnamed one speaks of the same thing; the
   checks of the old model are removed — `method` on a Leaf `create`, `contract` on a Leaf
   `update`, and the split of a Case with two Leaf contracts. The change of case 186.2 is not
   part of this defer." `deferred_by: decision-case-191`. (stood in 3 briefs)

Retired from the previous brief: none. Cases 182 and 185 are superseded (by 191 and 188) and
their decision pages archived; their targets stand on the list under 191 or carry no
`deferred_by` (`rule-plan-mode`, `rule-materialize`, `rule-case-protocol`).

## Flags

- No entry of the three yamls is marked `incomplete`, `failed`, `near`, `unparsed` or
  `merged`. Four `defer` entries of 1034 (191, 192) are `exists` — the targets were live
  pages, `deferred_by` set. Two entries of 1651 (195, 196.4) carry `superseded_by` and were
  skipped, as the handoff said.
- `generate` did not print "an update with no content in the Spec; applied by hand" for the
  `change`-only updates of 189, 190.2, 190.3, 190.4, which the handoff expected; the entries
  are `applied` and each wrote a History line on `rule-materialize`, `rule-end-of-work`,
  `rule-brief`. The Rule-class file entries printed "a Rule-class file, applied by hand"
  13 times (3 from 1034, 10 from 1651).
- The Estimates `estimate-materialize-assembles`, `-walks-dates`, `estimate-end-of-work-order`,
  `estimate-brief-written` were updated twice, by 189/190.x and then by 194.x/196.2/197;
  the 1651 text is the final one, as the handoff said.
- A caveat no rule text carries yet: an Estimate `update` whose item writes
  `sections: Criterion` keeps the written text (188's `estimate-case-protocol-loaded`), while
  194.1's `then` says the entry carries the Case's text. A sentence for `rule-materialize`
  and the Criterion of `estimate-materialize-assembles` in the next Plan Mode (handoff).
- `lesson-plan-mode-frontier-refused-on-the-client-text` (`new`, `error`): nothing in the
  harness blocks writing `frontier.md` in Plan Mode; the allow list in `settings.json` exists
  for it. The flag "Plan Mode blocks it" in the brief of 1034 was wrong (handoff).
- The wider question — conserving Specs "in a box" to run in other sessions — was named in
  the session and left; no defer written for it (handoff).
- `guppi pretask --check` prints five `update … has no contract` on the 1651 plan until
  `rule-pretask` of case 191 (handoff).
- The examples of `rules/schema.md` still show Leaf pages with `## How it works` (handoff).
- `generate` still applies `criterion_block` and `remove_criterion` from old yamls (191).
- The three task lines of 186 on the recut of `estimate-generate-writes`,
  `-pretask-reconciles`, `-lint-catches` wait for 191.
- Unticked `- [ ] read` lines stand in the Specs for Estimates already `passed`: in 1034
  `estimate-generate-writes`, `-pretask-reconciles`, `-lint-catches`,
  `estimate-plan-mode-names-its-estimates`, `estimate-materialize-walks-dates`,
  `-skips-a-carried-over-unit`, `estimate-spec-capture-offers-the-fork`; in 1651
  `estimate-materialize-walks-dates`.
- Stale defers: `rule-work-mode` and `rule-subagent-guppi`, `deferred: 13 times since case
  29` (lint), 17 briefs.
- Contradiction named by lint: `estimates/estimate-claude-md-rendered: method: says by hand
  while estimate-case-protocol-case-form names a test file`.
- Lint at the close of the run, 67 findings (64 before it per the handoff):
  - 62 × `decisions/decision-case-<1–28>: schema: missing section ## Context` / `## Problem`
    (31 pages, the Cases 1–28 — the sprint's closing item).
  - `estimates/estimate-generate-writes: ref: body names slug, which no live or archived page
    carries`
  - `rules/rule-subagent-guppi: deferred: 13 times since case 29`
  - `rules/rule-work-mode: deferred: 13 times since case 29`
  - `estimates/estimate-claude-md-rendered: method: says by hand while
    estimate-case-protocol-case-form names a test file`
- `entities/` holds no live page.

## Readings at the close

- `make test`: 397 passed.
- `make lint`: 67 findings, exit 1 (the list above).
- Live pages: rules 41, estimates 55, lessons 28, insights 10, decisions 271, entities 0.
  Archived this run: 4 decision pages.
