# Brief — 2026-10-10, after the librarian run of session 1713

## Where things stand

- Session 1713 opened the sprint `plugin` and ratified Cases 756 (756.1 to 756.6), 758 (the defer of `rule-morph`), 761, 762 and 763 (763.1, 763.2); Case 757 is superseded by Case 762 and Case 759 by Case 763.1 (handoff, What actually got done).
- Work Mode moved `main` to the last commit of `migration` by fast-forward, made the branch `plugin` from `main`, deleted `migration` and ticked the merge line of `vault/raw/2026-10-10/1555/spec.md`. No code or test changed (handoff).
- Readings of the session: `estimate-sprint-close-runs-in-the-librarian-run` passed, `estimate-brief-written` failed, then set `pending` with a new Criterion and method by Case 761, `estimate-hi-takes-a-conserved-spec` passed, `estimate-hi-writes-frontier` passed, `estimate-skill-sprint-close-migration-merged-into-main` passed, `estimate-sprint-close-settles-unread-estimates` passed, `estimate-sprint-close-takes-the-readings-in-groups` passed (ledger lines 1, 2, 3, 14, 20, 21, 22).
- The yaml `vault/raw/2026-10-10/1713/materialize.yaml`: 24 entries from a 24-line ledger (line 20 folded into the entry of case 762), 2 entries added by the synthesis; 24 entries `applied`, the entries of case 757 and case 759 `superseded_by`; `unparsed: []`. `guppi generate` wrote or changed 36 pages.
- Created: decisions 15 (756, 756.1 to 756.6, 757, 758, 759, 761, 762, 763, 763.1, 763.2), entities 1 (`entity-sprint-plugin`), estimates 6 (the five `estimate-sprint-plugin-*` and `estimate-skill-sprint-close-migration-merged-into-main`), lessons 2.
- Updated: estimates 6, rules 4 (`rule-brief`, `rule-morph` deferred by case 758, `rule-skill-sprint-close`, `rule-skill-hi` draft → built by the cascade), entities 1 (`entity-sprint`, child `entity-sprint-plugin`), insights 1, lessons 1 (the new lesson clustered).
- Archived by `guppi cleanup`: `decision-case-757` and `decision-case-759`, superseded, to `vault/archive/migration/2026-10-10/1713/decisions/`.
- Rendered: `.claude/agents/librarian-guppi.md` (Case 761) and `.claude/skills/sprint-close/SKILL.md` (Case 763.2). `guppi sprint` wrote `vault/wiki/sprint.md` with the sprint `plugin`; `guppi backlog` rewrote `vault/wiki/backlog.md`; `guppi glossary` changed nothing.
- `guppi archive` printed no line: both units under `vault/raw/2026-10-10/` are dated the day of the run, and 1713 is the session of the run.
- Synthesis: Grep `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 27 lines; Grep `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 1 line.
  - `lesson-case-reading-moment-before-the-render-it-reads` joined `insight-workflow-code-live-before-the-page-it-reads` (open, severity 2 now), beside its child `lesson-prespec-preview-expected-before-generate-applies-the-readings`: both set a moment or an expected output from the end state of the session, with no check of the order of generate and render or close.
  - `lesson-prespec-method-predicate-misses-a-sprint-session` joined none: no index line names the `waits_for_another_session` predicate of `guppi/lint.py` or the Estimates of a sprint page; it stays `new`.

## Readings due

- `estimate-brief-written` · pending · target `rule-brief` (draft) · read by the person at the `/hi` after the close of `plugin` (`- [ ] read` line 356 of `vault/raw/2026-10-10/1713/spec.md`; method: by hand, the person's answer at the /hi after the librarian's run of the session that closes a sprint, on vault/wiki/brief.md of that run).
- `estimate-sprint-close-next-session-opens-the-sprint` · pending · target `rule-sprint-close` (draft) · no read line in the 1713 spec; method: pytest tests/test_ledger.py -k sprint and tests/test_materialize.py -k sprint; by hand, at the librarian's run of the session after the close of a sprint: the brief before it, its frontier.md, the refusals of guppi ledger in its transcript, its ledger and the sprint field of the pages written from that ledger. This run: the yaml of 1713 holds `sprint: plugin`; the 22 pages created from the ledger of 1713 (13 live decisions, 1 entity, 6 estimates, 2 lessons) carry `sprint: plugin`; the 10 pages it updated (6 estimates, 3 rules, 1 insight) keep `sprint: migration`, as do `entity-sprint` (child added by case 756.1) and `rule-skill-hi` (changed by the cascade); `guppi cleanup` moved `decision-case-757` and `decision-case-759` to `vault/archive/migration/2026-10-10/1713/`; `make test` 1490 passed, 6 skipped.
- `estimate-sprint-plugin-close-steps-run-from-the-line` · pending · target `entity-sprint-plugin` (draft) · `- [ ] read` line 134 of the 1713 spec; method: by hand, at the end of Work Mode of the session that closes entity-sprint-plugin.
- `estimate-sprint-plugin-readme-describes-the-project` · pending · target `entity-sprint-plugin` (draft) · `- [ ] read` line 171 of the 1713 spec; method: the person's answer on README.md, in a session of the sprint plugin before its close.
- `estimate-sprint-plugin-pull-requests-reviewed-on-github` · pending · target `entity-sprint-plugin` (draft) · `- [ ] read` line 203 of the 1713 spec; method: a pull request from a second account read on GitHub, in a session of the sprint plugin before its close.
- `estimate-sprint-plugin-ci-writes-a-clean-branch` · pending · target `entity-sprint-plugin` (draft) · `- [ ] read` line 241 of the 1713 spec; method: a CI run on GitHub and the clean branch it wrote, in a session of the sprint plugin before its close.
- `estimate-sprint-plugin-installs-as-a-plugin` · pending · target `entity-sprint-plugin` (draft) · `- [ ] read` line 277 of the 1713 spec; method: an install of the clean branch into an empty project, in a session of the sprint plugin before its close.

## Flags

- `incomplete`: the entry of case 757 (`estimate-skill-sprint-close-branch-merged-at-the-next-opening`) lacks `criterion`; it is `superseded_by: '762'` and no page was written. No entry is marked `failed`, `near` or `unparsed`.
- Failed Estimates: none after `generate`. `estimate-brief-written` was read `failed` (ledger line 2: the contradiction on the `－` line of `estimate-sprint-migration-merges`, a Flag of the brief of run ab8be60f, stood in no line of `Cases`), then set `pending` by Case 761.
- MOC candidates: none.
- Stale defer: `rule-morph` — `deferred: 4 times since case 239` (lint); `backlog.md` reads "put off in 7 sessions".
- Contradiction (handoff, Observations): `/retro` sets an unread Estimate `failed` with "Retro, not read", while the ratified context of Case 756 says the read lines of the five Estimates of `entity-sprint-plugin` stay open; Retro left them `pending`. Carried by the first line of `## For the next session`.
- Contradiction (handoff, For the next session): the brief gives the merge line under `Cases` while step 4 of `/sprint-close` says `Work`. Carried by the second line of `## For the next session`.
- Defect: `guppi cleanup` took the sprint id from the first heading of `vault/wiki/sprint.md`, still `## migration — closed` before `guppi sprint` ran, and moved `decision-case-757` and `decision-case-759` of session 1713 to `vault/archive/migration/2026-10-10/1713/`, while `guppi materialize` set the yaml of 1713 to `sprint: plugin` (`opened_sprint`, case 628.3) (`guppi/cleanup.py`, `sprint_id`).
- Handoff check (Direct instructions): `entity-sprint-plugin` lists the five Estimates of Cases 756.2 to 756.6 in `estimates`, each with `target: entity-sprint-plugin`; the pages created from the 1713 ledger carry `sprint: plugin`; the pages it updated keep their own `sprint: migration`. No page `estimate-skill-sprint-close-branch-merged-at-the-next-opening` exists.
- Handoff note: the render of this run wrote the new text of `rule-brief` (Case 761) into `.claude/agents/librarian-guppi.md`; this run's librarian worked from the text before it.
- `make lint`, exit 2, 8 lines:
  - `rules/rule-morph: deferred: 4 times since case 239`
  - `estimates/estimate-brief-written: unread: pending`
  - `estimates/estimate-sprint-close-next-session-opens-the-sprint: unread: pending`
  - `estimates/estimate-sprint-plugin-ci-writes-a-clean-branch: unread: pending`
  - `estimates/estimate-sprint-plugin-close-steps-run-from-the-line: unread: pending`
  - `estimates/estimate-sprint-plugin-installs-as-a-plugin: unread: pending`
  - `estimates/estimate-sprint-plugin-pull-requests-reviewed-on-github: unread: pending`
  - `estimates/estimate-sprint-plugin-readme-describes-the-project: unread: pending`
- Read outside the frame: a Grep `^sprint:` over the 13 Decision pages of this run in `vault/wiki/decisions/` (the `sprint` field only), for the handoff check and the Readings due line of `estimate-sprint-close-next-session-opens-the-sprint`; the handoff asked for it (Direct instructions, second line).

## Next session

**Cases**
- One rule for the Estimates of a sprint page read in a later session of the sprint: `case-schema.md` (case 670.4), `/retro` and `waits_for_another_session` of `guppi/lint.py` hold no exception for them (handoff, For the next session; work of the first milestone of `plugin`).
- A merge step at the opening of a sprint after a sprint with a branch of its own, and the brief giving the merge line under `Cases` while step 4 of `/sprint-close` says `Work` (handoff, For the next session; work of the first milestone of `plugin`).
- The form of the opening of a sprint, which the person may want to discuss (handoff, For the next session).
- `guppi cleanup` files the pages of the session that opens a sprint under the archive folder of the closed sprint, since `sprint.md` is rewritten only at the later step `guppi sprint` (`vault/archive/migration/2026-10-10/1713/`, `guppi/cleanup.py`).

**Work**
- `estimate-sprint-close-next-session-opens-the-sprint` (its `- [ ] read` line in `vault/raw/2026-10-10/1555/spec.md`).
- `estimate-sprint-plugin-close-steps-run-from-the-line`.
- `estimate-sprint-plugin-readme-describes-the-project`.
- `estimate-sprint-plugin-pull-requests-reviewed-on-github`.
- `estimate-sprint-plugin-ci-writes-a-clean-branch`.
- `estimate-sprint-plugin-installs-as-a-plugin`.

**Ask the person**
- `estimate-brief-written` — needs the person — at the `/hi` after the close of `plugin`, on the brief the librarian wrote in that run: does `Cases` of Next session hold each contradiction listed under Flags, one between archived pages too, and only once when a line of `## For the next session` already carries it?

## Readings at the close

- `make test`: 1490 passed, 6 skipped.
- `make lint`: exit 2, 8 lines (above).
- Live pages: decisions 18, entities 4, estimates 263, insights 1, lessons 29, rules 79; `vault/archive/` holds 2579 `.md` files.
