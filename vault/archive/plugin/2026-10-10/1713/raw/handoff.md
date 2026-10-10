# Handoff — 2026-10-10, the opening of the sprint plugin

## Notes from memory

- The person gave the goals of the sprint `plugin` in their own words: the opening and the close of a sprint fixed, a final README, GitHub set up for pull requests from others, CI that writes a clean version to a branch of its own, and that clean version made into a Claude Code plugin. They took no backlog item into the sprint.
- The person said the opening of a sprint felt like one more Frontier item rather than a step of its own, and that the form may be discussed later; not a priority now.
- The person agreed to every recommended answer of every round, with no change of their own.
- At `/pre-spec` the person chose to leave the finding that the methods of the five Estimates of `entity-sprint-plugin` wait for a later session of the sprint; Case 756 records it in its context.
- The method of `estimate-brief-written` changed twice before ratification: from the rendered librarian file at Retro, which cannot be read before the librarian's render, to the person's answer at the `/hi` after the close of `plugin`.

## Direct instructions to the librarian

- Case 757 is superseded by Case 762 and Case 759 by Case 763. No page `estimate-skill-sprint-close-branch-merged-at-the-next-opening` is created; Case 763.1 carries the update of `estimate-sprint-close-settles-unread-estimates`.
- Case 756.1 creates `entity-sprint-plugin`; its `create` carries no `estimates` field. Check that the page lists the five Estimates that Case 756.2 to Case 756.6 create with `ref: entity-sprint-plugin`, and that each page written from this ledger carries `sprint: plugin`.
- Two Renders change: `.claude/agents/librarian-guppi.md` from `rule-brief` (Case 761) and `.claude/skills/sprint-close/SKILL.md` from `rule-skill-sprint-close` (Case 763.2). The brief this run writes may still follow the old text of `rule-brief`.

## What actually got done

- Cases ratified: 756 (756.1 to 756.6), 758 (the defer of `rule-morph`), 761, 762, 763 (763.1, 763.2).
- Work Mode: `main` moved to the last commit of `migration` by fast-forward; the branch `plugin` made from `main`; `migration` deleted; the merge line of `vault/raw/2026-10-10/1555/spec.md` ticked.
- Code and tests: none changed.
- `make test`: 1490 passed, 6 skipped, at the Baseline, on `plugin` after the switch and after the last task. `make style`: clean.
- Readings: L1 `estimate-sprint-close-runs-in-the-librarian-run` `passed`, L2 `estimate-brief-written` `failed`, L3 `estimate-hi-takes-a-conserved-spec` `passed`, L14 `estimate-hi-writes-frontier` `passed`, L20 `estimate-skill-sprint-close-migration-merged-into-main` `passed`, L21 `estimate-sprint-close-settles-unread-estimates` `passed`, L22 `estimate-sprint-close-takes-the-readings-in-groups` `passed`.
- Lessons: L23 `lesson-case-reading-moment-before-the-render-it-reads`, L24 `lesson-prespec-method-predicate-misses-a-sprint-session`.

## Debt

- No box is debt.
- 18 boxes wait for the librarian: the `create`, `update` and render lines of Cases 756, 761, 762 and 763, and the `read` lines whose readings stand in the ledger.
- `estimate-sprint-close-next-session-opens-the-sprint` — the librarian's run of this session, the session after the close of `migration`.
- `estimate-sprint-plugin-close-steps-run-from-the-line` — the end of Work Mode of the session that closes `plugin`.
- `estimate-sprint-plugin-readme-describes-the-project`, `estimate-sprint-plugin-pull-requests-reviewed-on-github`, `estimate-sprint-plugin-ci-writes-a-clean-branch`, `estimate-sprint-plugin-installs-as-a-plugin` — a session of the sprint `plugin` before its close.

## Observations

- `make lint` was red before the work, 7 lines (`work.md`, Baseline): `backlog: vault/wiki/backlog.md differs from its sources`, the stale defer of `rule-morph`, and five `unread: pending` lines.
- The five Estimates of `entity-sprint-plugin` are created by this session and not read. `/retro` sets such an Estimate `failed` with "Retro, not read"; Retro left them `pending`, as the ratified context of Case 756 says their read lines stay open and are carried until their moment. The two texts disagree.
- The preview of `guppi sprint-close` over the live vault cannot run while no sprint page is live, so the reading of `estimate-sprint-close-settles-unread-estimates` took the `pytest -k settle` run alone.
- The reading of `estimate-sprint-close-takes-the-readings-in-groups` passed on the close of `migration`, in which no Estimate outside the sprint page was read `failed`; the new line is first tested at the close of `plugin`.

## For the next session

- The Estimates of a sprint page are read in a later session of the sprint, while `case-schema.md` (case 670.4), `/retro` and `waits_for_another_session` of `guppi/lint.py` hold no exception for them; the opening and the close of a sprint need one rule for it. Work of the first milestone of `plugin`.
- A merge step at the opening of a sprint after a sprint with a branch of its own, and the brief giving the merge line under `Cases` while step 4 of `/sprint-close` says `Work`. Work of the first milestone of `plugin`.
- The form of the opening of a sprint, which the person may want to discuss.

## Ask the person

- `estimate-brief-written` — needs the person — at the `/hi` after the close of `plugin`, on the brief the librarian wrote in that run: does `Cases` of Next session hold each contradiction listed under Flags, one between archived pages too, and only once when a line of `## For the next session` already carries it?
