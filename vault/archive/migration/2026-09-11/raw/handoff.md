# Handoff — 2026-09-11, session H: Decision pages, Estimates, the librarian's frame, the ledger hook, Retro

## Notes from memory

- The session began on 2026-09-10 and crossed midnight. Case 52 (four sub-cases) was
  ratified on the 10th and its 19 ledger lines are in `raw/2026-09-10/ledger.md`
  (20:50:18); its Cases were copied by hand into `raw/2026-09-10/spec.md` after the
  approval stamp of the 11th, with a comment saying so. Cases 53–57 are in the ledger and
  the Spec of the 11th. Materialize walks both dates.
- The owner ratified Case 54 (the four reasons of the librarian's frame) "not fully sure";
  the readings of `estimate-documentation-completes` and `estimate-synthesis-clusters`
  after your run decide it. Both criteria are `pending` again by that Case.
- Case 56 (Retro as an analysis) was ratified as "let us try it, we change it if needed".
  The short form of Retro — `## Case N` with `context`, `problem` and a `defer` block
  under `## Retro` in the Spec — was not used this session: the two observations of Retro
  that could have been defers (below) went into this handoff without a decision.
- The owner's `vault/pages.base` is their Obsidian Bases view and is gitignored now.
- 21 Estimate pages are deleted by ledger lines of 53.1 and 53.2 (the 17 paired with
  lessons, the four of Cases 47–48 folded into `estimate-generate-writes`). Their targets
  (lessons) no longer carry `estimates`: the one-off of Work Mode removed the field and
  the section from the 17 lesson pages. Cleanup will find nothing to unlink there; that is
  expected.
- The `update` entries of this session carry many `replace` pairs written from the page
  text of the 11th. A pair whose `old` no longer matches fails its entry alone; report it,
  do not repair it.

## Direct instructions to the librarian

- Your own frame (`rule-documentation`), `rule-synthesis`, `rule-brief`, `rule-retro`,
  `rule-ask`, `rule-pretask`, `rule-index-check` are updated by this session's entries.
  Your agent file is the old render; the next session renders and commits. Follow the
  frame you run under; the reasons of Case 54 are in this handoff for your report: name
  every page you open with the reason and the outcome, including a lesson opened to settle
  a candidate cluster and any page opened for a fact the brief needs.
- The indexes are four: `estimates-index.md` is gone by 53.4. Do not compare estimate
  creates at the index check; there are none this session anyway.
- Decision pages are in the new shape (`kind`, `target_slug`, sections Context, Problem,
  Given, When): the 65 old ones were migrated by script, yours are written by the new
  `generate`. The sub-case decision pages of 52.x, 53.x and 55.x will be marked
  `incomplete: context, problem, given` — those sections sit on the parent Case heading
  in the Spec and `materialize` does not inherit them. Known; flag it once, not per page.
- Case 52 was ratified on the 10th: `raw/2026-09-10/materialize.yaml` gains 19 entries and
  four decision groups on this walk. That is the second time the 10th is extended after
  its commit; expected.
- Lint before your run: 259 findings, all known-false — 89 `ref` to `decision-case-52…57`
  (written by your run), 20 `orphan` and 17 `status` on the 21 Estimates you archive, 132
  `schema` on the 2026-09-09 backfill and the four clustered lessons without `## Insight`,
  3 `orphan` placeholders (`rule-work-mode`, `rule-subagent-guppi`, `rule-ledger-tail`), 1
  `method`. After your run the first two groups should be gone; what is left is the list
  for the brief.
- `deferred_by` now sits on `rule-work-mode`, `rule-subagent-guppi` (Case 29),
  `rule-ledger-tail` (Case 45), `rule-retro` (Case 50) and `rule-ledger-write` (Case 51),
  set by the migration script. Cases 56 and 55.1 supersede 50 and 51: `generate` clears
  those two. The index line of each shows the field.
- Two lessons of this session may cluster with existing ones:
  `lesson-ledger-hook-hi-lost-at-midnight` and
  `lesson-ledger-hook-misses-a-reply-ending-in-a-tool-call` share the area (the ledger
  hook and its events); `lesson-tests-generate-history-date-unpinned` and
  `lesson-tests-cli-date-pinned` share a root cause (a test reading the real clock).
  `lesson-spec-then-items-unchecked-against-ledger-lines` is alone.
- `sprint.md`: do not close Slice 3. The readings of Case 54 come after your run, in the
  tail; the next session takes them.
- Brief, "What the next session does first": (1) `uv run guppi render` for the seven rule
  pages above, commit; (2) take the readings of `estimate-generate-writes` and
  `estimate-materialize-assembles` (live parts against your run), `estimate-retro-loads`
  (at its `/retro`), `estimate-spec-capture-appends`, `estimate-documentation-completes`
  and `estimate-synthesis-clusters` (against your report); (3) close Slice 3 if the last
  two pass; (4) Plan Mode over the two observations of Retro below, Slice 3c (raw
  lifecycle, Case 45), Slice 3b.
- Deferred, carried with counts +1: Slice 3b Work Mode (3), `/grill-me` (6), upstream
  `origin` (6), `gh` (6), `parked/` and the old `archive/` (5), archive in `ask-guppi` (3),
  Case 45 → Slice 3c (2). Cases 50 and 51 are closed by 56 and 55.1 and leave the list.
- Two observations of Retro without a decision, for the Frontier: (a) pre-task does not
  check that every decision line of the session has an item under its own Case heading in
  the Spec — three lines lacked one this session and were fixed at Retro; a candidate
  `update` of `rule-pretask` or `rule-spec-capture`. (b) `materialize` does not inherit a
  parent Case's `context`, `problem`, `given` into its sub-cases' decision entries; a
  candidate `update` of `rule-materialize`.

## What actually got done

- Commit `241523d`: the render of the librarian agent after Case 44; the ledger tail of
  session G (ten lines of 16:15:34); the Spec of session H; `.gitignore` for `pages.base`.
- Commit `5b6b0df`: Case 55 — `guppi/ledger.py` joins the event logs of every date back to
  the session's start (55.1) and reads every main-agent message of `transcript_path` back
  at each `Stop`, deduplicated against every `raw/*/ledger.md` (55.2); eleven tests. The
  run helper of `tests/test_generate.py` pins `now` (five tests failed on the clock).
- Commit `01f41cf`: Cases 52, 53, 56, 57 in code — `generate.py` (decision fields and
  body, `deferred_by` set and cleared, the Decision page first, History wikilinks, no
  paired estimate, a reading always lands, stale `failed` dropped), `materialize.py`
  (standalone estimate sections, the incomplete rule for a defer-only Case), `index.py`
  (four files, the `deferred_by` suffix), `cleanup.py` (`estimates` lists of entities and
  rules only), `lint.py` (the `decision` class, `deferred_by` as a ref, an estimate's
  target category, lessons never orphans); the six schema pairs; `make test` 158.
- Commit `df4cdcf`: `index.md` (§1, §3, §5, §7, §8, §10, §11), `glossary.md`,
  `case-schema.md`, `CLAUDE.md` by hand; the one-off migrations (65 decision pages, 17
  lessons, the two `*-walks-dates` estimates, the `old-harness` mark); Case 52 appended to
  the Spec of the 10th.
- Commit `833d3f0`: `estimates-index.md` removed; `deferred_by` on the four remaining
  targets of current defers.
- Commit `66f0c9b`: the Retro — four readings passed (`estimate-index-lists`,
  `estimate-lint-catches`, `estimate-cleanup-moves`, `estimate-ledger-write-lifts`, the
  last one live through a reply that ended in `/pre-task`), two lessons, the Spec items of
  53.3 and 55.1 added under their own Cases.
- Not done: the render of the seven rule pages (after your run); the readings named
  above; the close of Slice 3; the rest of the deferred list.
