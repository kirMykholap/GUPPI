# Handoff — 2026-10-26, sprint plugin: the page of a replaced Case, the hook after a partial ratification, the check of a Case built again

## Notes from memory

- C4 of the Frontier, as the brief worded it ("the tags a retired Case writes are not taken back, so an earlier Case not yet applied would still be skipped"), the person judged no defect: once B replaced A, A must not apply even after C retires B, so the tags of `mark_superseded` stay. What Case 888 fixes is the other side of it, found in the code at `/hi`: the new Decision page of such an A stood `current` with no `superseded_by`. The brief should not carry the old wording of the gap forward.
- The person answered every round with the recommended options ("согласен", "a").
- The person put off C1 (sprint), C5 and C6 at the close of Plan Mode; C1 closed `· sprint · defer` with no Case.

## Direct instructions to the librarian

- Case 890.1 and 890.3 carry `{supersedes:case 887}` on `rule-case-check` and `rule-orchestration`: `decision-case-887` should end superseded, and `deferred_by` of both pages lose it; `rule-orchestration` keeps `decision-case-884` and stays in `backlog.md`.
- Cases 889 and 890 were built again on the findings of `/pre-spec` and ratified again with the same decision lines; the ledger holds each line once (L5–L14). The Spec holds their rebuilt texts; take the `then` blocks from the Spec.
- Case 891 defers `estimate-clean-branch-ships-neutral-texts` and `estimate-spec-write-writes-a-defer`; the second also carries a `passed` reading of this Retro (L24), so it may leave `backlog.md` by its status while `deferred_by` names 885 and 891 — check what `guppi backlog` lists for it.
- Case 888 changes the status text in `rule-decisions-schema` and `entity-glossary` with the same clause; `guppi render` and `guppi glossary` write `vault/wiki/decisions/schema.yaml` and `glossary.md`.

## What actually got done

- Cases ratified: 888, 889 (889.1, 889.2), 890 (890.1–890.4); short-form defer 891.
- Code: `.guppi/guppi/generate.py` (`Vault.decision` writes the new page of a record with `superseded_by` as `superseded`, naming each slug of it by `take_superseded_by`; docstring), `.guppi/guppi/materialize.py` (docstring), `.guppi/guppi/onward.py` (`cases_out` gives the ids, `case_out` asks it, `to_out` and `TO_OUT` the third reason, `ONLY_THE_PERSON` reworded; docstring), `.guppi/guppi/casecheck.py` (`other_blocks` takes a Case of the plan built again as the store holds it when its entry has no finding and its file holds its heading; docstrings).
- Tests: `test_generate.py` (2 new), `test_onward.py` (5 new, 7 rewritten and renamed where they asserted silence, 7 tightened to assert the reason), `test_casecheck.py` (4 `built_again_sibling`, 1 `session_clash`).
- `uv run --project .guppi guppi test`: 1780 passed, 6 skipped, 1 deselected. `uv run --project .guppi guppi style`: clean.
- Readings: L17–L24, all `passed`. No lesson.

## Debt

- No box of the Spec is debt; no patch.
- 25 boxes wait for the librarian (page, render, glossary and `read` lines).
- `estimate-clean-branch-ships-neutral-texts` — waits for `guppi ship --allow-draft` into an empty folder with a tag `prod-x.y.z`, read by hand; put off by Case 891.
- `estimate-clean-branch-writes-the-session-files`, `estimate-git-context-offers-git-init`, `estimate-plugin-install-offers-to-install-uv`, `estimate-plugin-install-undoes-the-copy-when-uv-sync-fails` — wait for an install from a tag `prod-x.y.z`, as before.

## Observations

- Red before the work: `guppi check` exit 1 with the 15 lines of `## Baseline` of `work.md`, among them `backlog: vault/wiki/backlog.md differs from its sources`, which the brief of 2307 did not list; the librarian's `guppi backlog` writes the file again.
- `.guppi/guppi/onward.py` is live in the working tree: the new `ONLY_THE_PERSON` text and the third reason already act on the next session's `/pre-spec`, while `orchestration.md` and `/pre-spec` take the matching texts of 890.3 and 890.4 only at this run's render.
- The one `ask-guppi` run of `/pre-spec` found eight findings in 889 and 890, among them a clash the two Cases built side by side made (the `**Waiting:**` line against `STOP:` for a `case-guppi` that has not answered); the second pass closed it in both.

## For the next session

- The frontier item C1 of the sprint (`rule-clean-branch`, `estimate-sprint-plugin-ci-writes-a-clean-branch`) stays the current milestone: the owner pushes `plugin` and a tag `prod-x.y.z`, and the CI run is read; the draft pages with `core: true` still stop a build of `prod`.
- The growing context of `case-guppi`, put off on `rule-orchestration` by Case 884, stays open.

## Ask the person

- `estimate-guppi-package-is-ready-after-the-install` — needs the person — In an empty project on a machine with `uv`, after the librarian's render, does `/guppi:install` run `uv --version`, ask nothing about `uv`, build `.guppi/.venv/` by `uv sync` after the copy before it sends you to `/hi`, and do the hooks find that environment at the first `/hi`?
