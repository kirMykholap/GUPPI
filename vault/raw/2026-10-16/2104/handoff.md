# Handoff — 2026-10-16, the sprint plugin: defers of records, the close command, and the five Insights of case-guppi

## Notes from memory

- C3, the false sentence in the Context of `decision-case-855`: the person chose no Case (option c). Case 864 was dropped and its file emptied; no decision line. The defer of Case 863 on `decision-case-855` stays a History line that no backlog line tracks; Case 865 changes only what a defer does from now on.
- Case 865 Q3: the person asked why the refusal waits until `/pre-spec` and chose to refuse a short defer at the reply that ratifies it, in both `Stop` hooks; so Case 865 has four parts.
- The batch of the five Insights (Cases 868–872): the person said that a separate round only to ask whether information passes between Cases is bad, and the agent should handle it itself. The main agent took that as a yes to its own question 869.Q4 and passed the finished files of 868 and 869 to 870, 871 and 872 without asking again; the words went into Case 872 as 872.3 and 872.5.
- The five Cases of the batch were built in parallel and `/pre-spec` sent all five back on fourteen findings of `ask-guppi`; each was built again, `ask-guppi` confirmed every finding closed, and the person ratified them again. Cases 872.6, 872.7 and 872.8 are new in that second build.
- The person put off C1 (the sprint item of the clean branch), C2 (Case 873) and C7 (Case 874) at the close of Plan Mode with "Откладываем и идём дальше".

## Direct instructions to the librarian

- Seven Cases change `rule-case-build` by `replace` pairs (868, 869, 870, 871 twice, 872.1, 872.3) and five change `rule-orchestration` (865.3, 872.2 twice, 872.3 twice, 872.5). At Retro a script applied every pair in Spec order to the live pages: each `old` was found exactly once and no two pairs overlap. Apply them in Spec order.
- Ledger lines L39–L41 (872.6, 872.7, 872.8) were written after the short defers L37–L38 though they belong to Case 872; the Spec holds them under Case 872.
- The re-ratification of Cases 868–872 repeated their decision lines in the transcript; the ledger holds each line once.
- Case 867 carries `{supersedes:case 829}`: the `deferred_by: decision-case-829` of `estimate-page-schemas-one-file-per-rule` should clear, and the page should leave `backlog.md`.
- Case 869 carries `{supersedes:case 835}` on `insight-case-build-claims-what-code-does-without-reading-it`.

## What actually got done

- Cases ratified: 865 (865.1–865.4), 866, 867, 868, 869, 870, 871, 872 (872.1–872.8); short defers 873 (`rule-estimates-schema`) and 874 (`estimate-clean-branch-ships-neutral-texts`).
- Code: `.guppi/guppi/materialize.py` — `DEFERRABLE` moved here, `defers_a_record` and `DEFER_OF_A_RECORD` new, the routing table line of `defer existing`; `.guppi/guppi/generate.py` fails such a defer first; `.guppi/guppi/prespec.py` reports it in `check_form`; `.guppi/guppi/ratified.py` refuses the short Case in `deferred_section`; `.guppi/guppi/ledger.py` refuses the line by `refused_defers`. Tests: `test_generate.py`, `test_prespec.py`, `test_ratified.py`, `test_ledger.py`; the module docstring of `test_guppi_package.py` (Case 868).
- `uv run --project .guppi guppi test`: 1748 passed, 6 skipped, 1 deselected. `uv run --project .guppi guppi style`: clean after `ruff format` of `test_ledger.py` and `test_ratified.py`.
- Readings at `/hi`: L1 `estimate-rules-schema-checked` passed, L2 `estimate-clean-branch-ships-neutral-texts` failed (read whole by seven agents over a `guppi ship --allow-draft` copy).
- Readings at Retro: `estimate-generate-writes`, `estimate-prespec-checks-the-form-of-an-item`, `estimate-spec-write-writes-a-defer`, `estimate-ledger-write-refuses-a-defer-of-a-record`, `estimate-case-build-writes-the-case`, `estimate-case-build-checks-a-fact-of-an-outside-tool`, `estimate-case-build-reads-by-need-and-in-parts`, `estimate-case-build-checks-the-finished-case`, `estimate-orchestration-asks-in-the-grill-me-shape`, `estimate-orchestration-signs-a-batch-together`, all passed. One lesson: `lesson-case-build-parallel-cases-clash-on-one-page`, marked `{addressed_by:case 872.1}`.

## Debt

- No box of code, test or command is unticked.
- Boxes that wait for the librarian: every `update`, `create`, `render` and `read` line of the Spec.
- `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` — after the first Case built under the new Render of `rule-case-build` that names a test over a live file.
- `estimate-case-build-reads-the-code-it-states` — after the first `/pre-spec` of a session whose Cases `case-guppi` built under the new Render.
- `estimate-case-build-reads-no-sibling-file-mid-send` — after the first send of two or more Cases to `case-guppi` at the same time under the new Render.
- `estimate-orchestration-rechecks-a-sibling-after-a-joint-send` — after the first such send under the new Render of `rule-orchestration`.
- `estimate-orchestration-shows-the-built-case` — after the first summary in Plan Mode that carries a line `**Other Case:**` under the new Render.
- `estimate-orchestration-signs-items-taken-together` — after the first batch in Plan Mode under the new Render in which a summary carries a line `**Other Case:**`.
- `estimate-clean-branch-writes-the-session-files` — an install session from a copy with a tag `prod-x.y.z`: an empty folder with no git, `/hi` until `git init -b main`, the next `/hi`, and the three `--check` commands.

## Observations

- `guppi check` at the baseline of `/work` printed `backlog: vault/wiki/backlog.md differs from its sources`, which the check at `/hi` did not print; red before the work. The other lines of the baseline are the eleven of the brief.
- The bash guard refused two heredocs whose body held a backslash; the code changed by Edit instead.
- The shipped `CLAUDE.md` holds English and Russian, the values of `rule-guppi-config` the render filled in; `rule-language` itself names the languages by role.
- `estimate-orchestration-signs-a-batch-together` keeps a clause that `rule-case-check` refuses no `**Waiting:**` reply, which the new Render of `rule-orchestration` does not state; the Retro reading passed it as carried from the old Criterion.
- The two Lessons deferred by Case 836 (`lesson-case-build-agent-context-grows-on-every-resume`, `lesson-ledger-window-stops-at-a-resume-on-the-next-day`) stay as History lines that no backlog line tracks; Case 865 left them, as its context says.
- The session passed 400 000 tokens of context during Retro.

## For the next session

- The rewrite of the sentences of the clean version true only in the repository of GUPPI, put off by Case 874: eight rules and about forty shipped Estimates, listed in the reading of `estimate-clean-branch-ships-neutral-texts`.
- The MOC form of a `method` that names `guppi test` alone, put off by Case 873 on `rule-estimates-schema`.
- The milestone item `rule-clean-branch`, `estimate-sprint-plugin-ci-writes-a-clean-branch`: the draft pages with `core: true` still stop every build of `prod`; this session's Cases set `rule-close` and others `draft` again at the cascade.
- The defer of Case 863 on `decision-case-855` and the two defers of Case 836 on Lessons reach no backlog line; Case 865 stops new ones only.

## Ask the person

- `estimate-guppi-package-is-ready-after-the-install` — needs the person — In an empty project on a machine with `uv`, after the librarian's render, does `/guppi:install` run `uv --version`, ask nothing about `uv`, build `.guppi/.venv/` by `uv sync` after the copy before it sends you to `/hi`, and do the hooks find that environment at the first `/hi`?
