# Brief — 2026-10-30, librarian of session 2345

## Where things stand

- Session 2345 of the sprint `plugin`. Cases ratified: 944, 945, 946 (946.1, 946.2), 947, 948 (948.1, 948.2), and the defer 949. Case 944, 945, 947 and 948 were built again after the findings of `ask-guppi` at `/pre-spec` and ratified again; only Case 944 gained a decision line, the `update` of `rule-documentation` (handoff).
- Code: `.guppi/guppi/prespec.py` (`conserved_decisions`; `check_frontier` passes the decision lines of the conserved ledger to `check_backlog_defer_line`), and the module docstrings of `.guppi/guppi/guard.py`, `.guppi/guppi/ratified.py` and `.guppi/guppi/shellwrite.py`. Tests: `.guppi/tests/test_prespec.py`, three new. `guppi test` 1822 passed, 6 skipped, 1 deselected; `guppi style` clean (handoff).
- Readings: L1–L3 at `/hi` (L1 `failed`, L2 and L3 `passed`); L18–L20 at the end of Retro, three `passed`. No lesson (handoff, ledger).
- The person put off C1 of the sprint, the push of `plugin` with a tag `prod-x.y.z` and the read of the CI run, with no reason given (handoff).
- `guppi materialize` printed `written with 20 entries` for `vault/raw/2026-10-30/2345/materialize.yaml` and `extended with 0 entries` for the yamls of `0304`, `1713` and `2005`. The ledger has 20 lines (`wc -l`) and the yaml has 20 entries, one per line, so every line is accounted for. Kinds: 11 `update`, 2 `create` (both estimates), 1 `defer`, 6 `estimate`.
- Marks: 30 `applied` lines (20 under `entries`, 10 under `decisions`); one `exists: true` (line 16, the `defer` of `estimate-plugin-install-sets-aside-the-files-of-the-project`); no entry `failed`, `incomplete`, `near`, `merged` or `librarian`; `unparsed: []`.
- `guppi generate` printed 25 pages written or changed for `2345` and 0 for `0304`, `1713` and `2005`. `guppi cleanup` printed `0 page(s) moved`. `guppi render`, `sprint`, `backlog` and `glossary` printed nothing on stderr. No unticked Spec line holds `guppi sprint-close --apply`.
- Pages created (12), from `git status`: decisions 10 (`decision-case-944`, `945`, `946`, `946.1`, `946.2`, `947`, `948`, `948.1`, `948.2`, `949`); estimates 2 (`estimate-where-to-stop-writes-each-step-whole`, `estimate-case-build-reads-each-list-of-a-new-member`, both `pending`).
- Pages updated (13), from `git status`: rules 6 (`rule-close`, `rule-documentation` by two entries, 946.2 and 944; `rule-where-to-stop`, `rule-shell-write-check`, `rule-case-build`; `rule-rules-schema` by the cascade alone); estimates 7 (`estimate-close-reports-the-run`, `estimate-rules-schema-leaf-carries-no-how-it-works`, `estimate-shell-write-check-repairs-and-reports` and `estimate-prespec-checks-the-frontier` by an `update` and readings; `estimate-case-build-reads-the-readers-of-a-changed-step` by an `update`; `estimate-rules-schema-checked` by a reading; `estimate-plugin-install-sets-aside-the-files-of-the-project` by the `defer`). 12 created and 13 updated make the 25 pages `generate` printed.
- Cascade (log): `rule-rules-schema` `draft → built`; `rule-where-to-stop` `built → draft`.
- Statuses after generate: `estimate-close-reports-the-run` `pending` (L3 `passed`, then Case 944 set it `pending`); `estimate-rules-schema-leaf-carries-no-how-it-works`, `estimate-shell-write-check-repairs-and-reports`, `estimate-prespec-checks-the-frontier` and `estimate-rules-schema-checked` `passed`; `estimate-case-build-reads-the-readers-of-a-changed-step` `pending` (Case 948.2).
- Render wrote `.claude/agents/librarian-guppi.md` (step 1 and the close, Cases 944 and 946.2), `.claude/agents/case-guppi.md` (Case 948.1) and `vault/wiki/where-to-stop.md` (Case 945). `backlog.md` went from 7 items to 8, with `estimate-plugin-install-sets-aside-the-files-of-the-project` added (Case 949, `deferred_by`).
- This run ticked 19 boxes of `vault/raw/2026-10-30/2345/spec.md` (3 of them render boxes) and 2 `read` boxes of the 2005 Spec (`estimate-rules-schema-leaf-carries-no-how-it-works`, `estimate-rules-schema-checked`). `guppi archive` then moved the folders of 0304, 1713 and 2005 to `vault/archive/plugin/2026-10-30/<HHMM>/raw/`; the folder of 2345 stays. 4 `read` boxes of the 2345 Spec stay unticked; the handoff named 23 boxes waiting (19 plus 4).
- The handoff's instructions, checked: both updates of `rule-documentation` applied (log, and the diff of `.claude/agents/librarian-guppi.md`); this run writes no `report.md`; Case 949 entered `backlog.md` through `deferred_by`.
- Index check: the 2 `create` entries are Estimates and have no index; no Grep of a category ran for them.
- Synthesis: `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 55 lines; `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 12 lines. The yaml holds no `lesson` entry, so the synthesis added no entry.

## Readings due

- `estimate-close-reports-the-run` — `pending`; target `rule-close` (`draft`); read by its unticked `read` box in `vault/raw/2026-10-30/2345/spec.md` (Case 944): after a librarian's run whose `librarian-guppi.md`, when the run starts, holds the Render of `rule-close` that writes `report.md`, its `report.md` read by `git show` against the Criterion. This run: it started on the old frame; `guppi render` rewrote the close of `.claude/agents/librarian-guppi.md` to the Render that writes `report.md`; this run wrote no `report.md`.
- `estimate-where-to-stop-writes-each-step-whole` — `pending`; target `rule-where-to-stop` (`draft`); read by its unticked `read` box in the 2345 Spec (Case 945): after the first stop of Work Mode under the new `vault/wiki/where-to-stop.md` whose reply asks the person to run commands by hand.
- `estimate-case-build-reads-each-list-of-a-new-member` — `pending`; target `rule-case-build` (`draft`); read by its unticked `read` box in the 2345 Spec (Case 948.1): at the Retro of the session that changes it, then after the `/pre-spec` of the first session whose `case-guppi` runs on the new Render of `rule-case-build`.
- `estimate-case-build-reads-the-readers-of-a-changed-step` — `pending`; target `rule-case-build` (`draft`); read by its unticked `read` box in the 2345 Spec (Case 948.2): after the same `/pre-spec`.
- `estimate-orchestration-names-related-cases-in-the-dispatch` — `pending`; target `rule-orchestration` (`draft`); read by its unticked `read` box in `vault/archive/plugin/2026-10-30/2005/raw/spec.md` (Case 938): after the first dispatch of `case-guppi` under the new Render in which a Case of the session sets the form of a text a check reads and the Case of the item may write text of that kind.
- `estimate-plugin-install-sets-aside-the-files-of-the-project` — `pending`, `deferred_by: decision-case-949`; target `rule-plugin-install` (`draft`); read by its unticked `read` box in `vault/archive/plugin/2026-10-30/1713/raw/spec.md` (Case 932.1): after the librarian's run of 1713, with a tag `prod-x.y.z`, installs into three projects with files of their own, one started with `UV_OFFLINE=1` and an empty `UV_CACHE_DIR`. This run: the `defer` of Case 949 is marked `exists: true`, and `backlog.md` lists the Estimate.
- `estimate-morph-takes-in-the-set-aside-files` — `pending`; target `rule-morph` (`draft`); read by its unticked `read` box in the 1713 Spec (Case 932.2): after the session whose Work Mode builds the setup skill of `rule-morph` and its step in `/hi`.
- `estimate-morph-sets-up-the-project-at-the-first-hi` — `pending`; target `rule-morph` (`draft`); read by its unticked `read` box in the 1713 Spec (Case 932.5): after the session whose Work Mode builds the setup skill of `rule-morph`, its step in `/hi` and in `/sprint-open`.
- `estimate-ask-query-before-a-create` — `pending`; target `rule-ask` (`draft`); read by its unticked `read` box in `vault/archive/plugin/2026-10-30/0304/raw/spec.md` (Case 920.2): after a `case-guppi` builds a Case with a `create` without a `ref`.
- `estimate-synthesis-keeps-actioned-by-the-mark` — `pending`; target `rule-synthesis` (`draft`); read by its unticked `read` box in the 0304 Spec (Case 920.3): after a librarian's run that puts a lesson with `addressed_by` under an `actioned` Insight. This run: the yaml holds no `lesson` entry; the synthesis added no entry.
- `estimate-search-leaves-out-decisions-refuses-ask-guppi` — `pending`, `deferred_by: decision-case-936`; target `rule-search-leaves-out-decisions` (`draft`); read by its unticked `read` box in the 0304 Spec (Case 925.1): `test_grepguard.py`, then after the first `/pre-spec` once the librarian's run has rendered `.claude/settings.json`, each Read and Grep of `ask-guppi` on `vault/wiki/decisions/` refused. This run: `guppi render` left `.claude/settings.json` unmodified (`git status`).
- `estimate-orchestration-shows-the-built-case` — `pending`; target `rule-orchestration` (`draft`); method: after the first summary of `case-guppi` in Plan Mode with a line `Other Case` naming a Case of the session under the new Render.
- `estimate-orchestration-signs-items-taken-together` — `pending`; target `rule-orchestration` (`draft`); method: after the first batch taken up together under the new Render in which a summary carries a line `Other Case` naming a Case of the session.
- `estimate-case-build-goes-on-after-a-live-compaction` — `pending`; target `rule-case-build` (`draft`); method: after the first compaction of a `case-guppi` in a working session.
- `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` — `pending`; target `rule-case-build` (`draft`); method: after the first Case built under the Render that names a test over a live file and changes both.
- `estimate-ratification-ledger-line-form` — `pending`; target `rule-ratification` (`draft`); method: after a session whose ledger holds a lesson with the Case that closes its cause, a Case taking up a decision with more than one Case in `deferred_by`, and a lesson line declaring a new tag.
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — `pending`; target `rule-work-mode` (`draft`); method: after the first `/work` on the rendered skill in which a Case is ratified in Work Mode.
- `estimate-hi-writes-frontier` — `pending`; target `rule-skill-hi` (`draft`); method: the person's answer in the session after the close of a sprint, at the reply that acknowledges the opening Case of `/sprint-open`.
- `estimate-skill-merge-main-joins-a-conflicted-page` — `pending`; target `rule-skill-merge-main` (`draft`); method: after the first `/merge-main` whose merge of main leaves a conflicted page.
- `estimate-skill-pr-review-takes-a-pull-request-whole` — `pending`; target `rule-skill-pr-review` (`draft`); method: after the first pull request from another account merged into main by `/pr-review` after the close of `plugin`.
- `estimate-sprint-plugin-ci-writes-a-clean-branch` — `pending`; target `entity-sprint-plugin` (`draft`, the live sprint page); method: `test_ship.py`, then after a run of `.github/workflows/prod.yml` on a tag `prod-x.y.z` that writes `prod`, before the close of `plugin`.
- `estimate-sprint-plugin-installs-as-a-plugin` — `pending`; target `entity-sprint-plugin` (`draft`, the live sprint page); method: in a session of the sprint before its close, a clean copy installed in an empty project and `/hi` typed.
- `estimate-sprint-plugin-pull-requests-reviewed-on-github` — `pending`; target `entity-sprint-plugin` (`draft`, the live sprint page); method: a pull request from a second account read on GitHub, before the close of the sprint.
- `estimate-sprint-plugin-readme-describes-the-project` — `pending`; target `entity-sprint-plugin` (`draft`, the live sprint page); method: the person's answer on `README.md` at the `/hi` after the session that writes it, before the close of the sprint.
- `estimate-sprint-plugin-close-steps-run-from-the-line` — `pending`; target `entity-sprint-plugin` (`draft`, the live sprint page); method: at the end of Work Mode of the session that closes `entity-sprint-plugin`.

## Flags

- No entry marked `incomplete`, `failed`, `near` or `unparsed`. Line 16 (`defer` of `estimate-plugin-install-sets-aside-the-files-of-the-project`) carries `exists: true`.
- No Estimate stands `failed`. The `failed` reading L1 of `estimate-rules-schema-leaf-carries-no-how-it-works` was followed by the `passed` reading L18 on the Criterion of Case 946.1.
- `guppi check`: 12 lines, exit 1, each a page with `core: true` that stands `draft`: `entity-sprint`, `rule-ask`, `rule-case-build`, `rule-close`, `rule-morph`, `rule-orchestration`, `rule-ratification`, `rule-search-leaves-out-decisions`, `rule-skill-hi`, `rule-synthesis`, `rule-where-to-stop`, `rule-work-mode`. The handoff counted 13 lines before the work. The line `estimate-case-build-reads-the-readers-of-a-changed-step: unread: failed` is gone. `rule-rules-schema` left the list (`draft → built`) and `rule-where-to-stop` entered it (`built → draft`) by the cascade of this run.
- Stale defer: `rule-work-mode` is put off in 31 sessions (`backlog.md`).
- The handoff says the decision lines of Case 944, 945, 947 and 948 stand twice in the ledger; `vault/raw/2026-10-30/2345/ledger.md` holds each of them once (20 lines, lines 4–17), and the yaml applied each once.
- `estimate-case-build-reads-each-list-of-a-new-member`: the handoff (`## Debt`) says its Retro part matched each line of the Criterion at this Retro; its `method` asks for that part to be recorded in the estimate line, and the ledger holds no `estimate` line for it, so the page carries no record of it.
- Handoff observation: `ask-guppi` at `/pre-spec` did not read the code of `remove_superseded` and its helpers, so the claim of Case 946 that the two wordings of the parent removal give the same result rests on `case-guppi` alone.
- No MOC candidate and no contradiction found.
- No read outside the frame.

## Next session

### Cases

- `estimate-case-build-reads-each-list-of-a-new-member`: the Retro reading the handoff reports has no `estimate` line in the ledger of 2345, so the page holds no record of it (handoff `## Debt`, ledger).

### Work

- none

### Ask the person

- none

## Readings at the close

- `uv run --project .guppi guppi test`: 1822 passed, 6 skipped, 1 deselected, exit 0.
- `uv run --project .guppi guppi check`: 12 lines, exit 1 (above).
- Pages under `vault/wiki/`: decisions 418, entities 5, estimates 328, insights 12, lessons 55, rules 86. Pages under `vault/archive/`: 3059, after `guppi archive` (2998 before it).
