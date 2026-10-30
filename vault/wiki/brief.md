# Brief — 2026-10-30, librarian of session 2005

## Where things stand

- Session 2005 of the sprint `plugin`. Cases ratified: 936 (a defer); 937 (937.1, 937.2, 937.3); 938; 939; 942 (942.1, 942.2); 943 (943.1, 943.2, 943.3). Case 942 replaced Case 940 and Case 943 replaced Case 941 after `/pre-spec` (handoff).
- Code: `.guppi/guppi/generate.py` (`title_slugs`), `.guppi/guppi/prespec.py` (`decided_on_its_page` with `by_defer`, `check_backlog_defer_line`, `deferred_pages`), `.guppi/guppi/casecheck.py` (`check_backlog` with `by_defer`); the module docstrings of `conftest.py`, `ratified.py`, `recall.py`, `event.py`, `gate.py`, `archive.py`, `gitstate.py`, `tail.py`, `pageread.py` and `guard.py` took the facts of `## How it works`. Tests: `test_prespec.py` (five new), `test_casecheck.py`. `guppi test` 1819 passed, 6 skipped, 1 deselected; `guppi style` clean (handoff).
- In Work Mode the agent wrote the clean copy by `guppi ship --allow-draft` into `C:\tmp\guppi-2005\copy` and made five test projects; at the `stop:` task the person installed into them and answered A1 (handoff).
- Readings: L1 at `/hi`; L45–L55 at the end of Retro, ten `passed` and one `failed` (`estimate-case-build-reads-the-readers-of-a-changed-step`). Lesson: L56 (handoff).
- `guppi materialize` printed `written with 56 entries` for `vault/raw/2026-10-30/2005/materialize.yaml` and `extended with 0 entries` for the yamls of `0304` and `1713`. The ledger has 56 lines (`wc -l`); the yaml holds entries for lines 1–45 and 47–56 (55 entries), and line 46, the reading of `estimate-orchestration-closes-a-backlog-item-deferred-again`, is folded into the `create` of line 6, so every line is accounted for. Kinds: 39 `update`, 3 `create` (all estimates), 1 `defer`, 11 `estimate`, 1 `lesson`.
- 15 entries carry `superseded_by` (lines 10–24, Cases 940 and 941, superseded by 942.1/942.2 and 943.1–943.3), as the handoff asked: only the entries of the superseding Cases apply.
- Marks: 56 `applied` lines (40 under `entries`, 16 under `decisions`); one `exists: true` (line 2, the `defer` of `estimate-search-leaves-out-decisions-refuses-ask-guppi`); one `incomplete: [criterion]` (line 22, a superseded `create`); no entry `failed`, `near`, `merged` or `librarian`; `unparsed: []`.
- `guppi generate` printed 51 pages written or changed for `2005` and 0 for `0304` and `1713`. `guppi cleanup` printed `2 page(s) moved`. `guppi render`, `sprint`, `backlog` and `glossary` printed nothing on stderr. No unticked Spec line holds `guppi sprint-close --apply`.
- Pages created (19), from `git status`: decisions 16 (`decision-case-936`, `937`, `937.1`–`937.3`, `938`, `939`, `940`, `941`, `942`, `942.1`, `942.2`, `943`, `943.1`–`943.3`); estimates 2 (`estimate-orchestration-closes-a-backlog-item-deferred-again`, `passed`; `estimate-rules-schema-leaf-carries-no-how-it-works`, `pending`); lessons 1 (`lesson-plugin-install-steps-named-the-offline-variables-by-reference`, `new`).
- Pages updated (32), from `git status`: rules 18 (`rule-orchestration` by two entries, 937.2 and 938; `rule-skill-hi`, `rule-clean-branch`, `rule-rules-schema`, `rule-plugin-install`, `rule-guppi-package`, and the eleven Leaf pages of Case 942.1: `rule-tests-clock-pinned`, `rule-spec-write`, `rule-compact-recall`, `rule-event-log`, `rule-retro-commit`, `rule-raw-archive`, `rule-git-context`, `rule-ledger-tail`, `rule-page-read`, `rule-governed-files-hook`, `rule-internal-context`; `rule-guppi-config` by the cascade alone); estimates 14 (7 by `update` entries, 11 by readings, 4 of them both, 1 by the `defer`).
- Archived (2, under `vault/archive/plugin/2026-10-30/2005/decisions/`): `decision-case-940`, `decision-case-941`, superseded. 19 created, 32 updated make the 51 pages `generate` printed.
- Cascade (log): `rule-guppi-config` and `rule-guppi-package` `draft → built`; `rule-rules-schema` `built → draft`.
- Render wrote `vault/wiki/orchestration.md`, `.claude/skills/hi/SKILL.md` and `vault/wiki/rules/schema.yaml`; `backlog.md` went from 6 items to 7, `estimate-search-leaves-out-decisions-refuses-ask-guppi` added (Case 936).
- The handoff's instructions, checked: the Grep `^## How it works` over `vault/wiki/rules/` prints 4 pages, `rule-claude-md`, `rule-documentation`, `rule-session-start`, `rule-skill-hi`, each `kind: MOC`, so no Leaf holds the section; no entry is `failed`, so no `drop` item failed. Both updates of `rule-orchestration` applied (log).
- This run ticked 37 boxes of `vault/raw/2026-10-30/2005/spec.md` (4 of them render boxes), 3 `read` boxes of `vault/raw/2026-10-30/1713/spec.md` and 4 `read` boxes of `vault/raw/2026-10-30/0304/spec.md` (`estimate-synthesis-clusters`, `estimate-orchestration-states-a-subagent-fact-from-its-transcript`, `estimate-case-build-reads-the-readers-of-a-changed-step`, `estimate-case-build-reads-the-code-it-states`). 3 `read` boxes of the 2005 Spec stay unticked; the handoff named 40 boxes waiting (37 plus 3).
- Index check: the 3 `create` entries are Estimates and have no index; no Grep of a category ran for them.
- Synthesis: `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 54 lines (3 of them `[Omitted long matching line]`, read as line 4 of their pages); `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 12 lines. The synthesis added no entry.
  - `lesson-plugin-install-steps-named-the-offline-variables-by-reference` — none: its cause is install steps that wrote the offline variables out for one project and named them by reference for another; `lesson-hi-asks-a-reading-of-a-text-it-names-no-place-of` is a question of an Ask line that names no place of the text it asks about, and `lesson-shell-bang-commands-given-in-bash-syntax-ran-in-powershell` is commands written for the wrong shell; no Insight's pattern is on the steps the agent gives the person.

## Readings due

- `estimate-case-build-reads-the-readers-of-a-changed-step` — `failed`; target `rule-case-build` (`draft`); read after the `/pre-spec` of the first session on the new Render of `rule-case-build`. Result: 1 of 8 findings of `ask-guppi` at the `/pre-spec` of 1713 is a Case that changes a step and misses a text that reads its output — Case 931 added `drop` and left line 30 of `case-schema.md` and the sentence of `rule-materialize` that lists the lifted keys (L54).
- `estimate-rules-schema-leaf-carries-no-how-it-works` — `pending`; target `rule-rules-schema` (`draft`); read by its unticked `read` box in `vault/raw/2026-10-30/2005/spec.md` (Case 942.1): at Retro the new docstrings and Purpose, and after the librarian's run of this session a Grep for `^## How it works` over `vault/wiki/rules/` and the kind of each page it prints. This run: that Grep prints 4 pages, `rule-claude-md`, `rule-documentation`, `rule-session-start`, `rule-skill-hi`, each `kind: MOC`.
- `estimate-rules-schema-checked` — `pending`; target `rule-rules-schema` (`draft`); read by its unticked `read` box in the 2005 Spec (Case 942.2): `test_schemas.py -k rules`, then after a librarian's run the live `vault/wiki/rules/schema.yaml` against the Criterion and `guppi check`. This run: `guppi render` wrote `vault/wiki/rules/schema.yaml` (1 line added, 14 removed in `git diff --stat`); `guppi check` printed 13 lines, none a `schema` line on `rules/`.
- `estimate-orchestration-names-related-cases-in-the-dispatch` — `pending`; target `rule-orchestration` (`draft`); read by its unticked `read` box in the 2005 Spec (Case 938): after the first dispatch of `case-guppi` under the new Render in which a Case of the session sets the form of a text a check reads and the Case of the item may write text of that kind.
- `estimate-plugin-install-sets-aside-the-files-of-the-project` — `pending`; target `rule-plugin-install` (`draft`); read by its unticked `read` box in `vault/raw/2026-10-30/1713/spec.md` (Case 932.1): after the librarian's run of 1713, with a tag `prod-x.y.z`, installs into three projects with files of their own, one started with `UV_OFFLINE=1` and an empty `UV_CACHE_DIR`. The handoff: three projects ran, the offline one ran online (L56), so the putting back after a failed `uv sync` was not seen.
- `estimate-morph-takes-in-the-set-aside-files` — `pending`; target `rule-morph` (`draft`); read by its unticked `read` box in the 1713 Spec (Case 932.2): after the session whose Work Mode builds the setup skill of `rule-morph` and its step in `/hi`.
- `estimate-morph-sets-up-the-project-at-the-first-hi` — `pending`; target `rule-morph` (`draft`); read by its unticked `read` box in the 1713 Spec (Case 932.5): after the session whose Work Mode builds the setup skill of `rule-morph`, its step in `/hi` and in `/sprint-open`.
- `estimate-ask-query-before-a-create` — `pending`; target `rule-ask` (`draft`); read by its unticked `read` box in `vault/raw/2026-10-30/0304/spec.md` (Case 920.2): after a `case-guppi` builds a Case with a `create` without a `ref`.
- `estimate-synthesis-keeps-actioned-by-the-mark` — `pending`; target `rule-synthesis` (`draft`); read by its unticked `read` box in the 0304 Spec (Case 920.3): after a librarian's run that puts a lesson with `addressed_by` under an `actioned` Insight. This run: the one `lesson` entry carries no `addressed_by`; the synthesis added no entry.
- `estimate-search-leaves-out-decisions-refuses-ask-guppi` — `pending`, `deferred_by: decision-case-936`; target `rule-search-leaves-out-decisions` (`draft`); read by its unticked `read` box in the 0304 Spec (Case 925.1): `test_grepguard.py`, then after the first `/pre-spec` once the librarian's run has rendered `.claude/settings.json`, each Read and Grep of `ask-guppi` on `vault/wiki/decisions/` refused.
- `estimate-close-reports-the-run` — `pending`; target `rule-close` (`draft`); method: after a librarian's run whose `librarian-guppi.md`, when the run starts, holds the Render of `rule-close` with no limit of lines, the person's answer on the report. This run: `.claude/agents/librarian-guppi.md` is not modified (`git status`), and its Render of `rule-close` names no limit of lines; the report goes to `/handoff` after the commit.
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

- Line 22 of the yaml (`create` of `estimate-rules-schema-leaf-carries-no-how-it-works`, Case 940) is marked `incomplete: [criterion]`; it carries `superseded_by` and was not applied; the page was written from line 38 (Case 942.1) with its Criterion.
- No entry marked `failed`, `near` or `unparsed`. Line 2 (`defer` of `estimate-search-leaves-out-decisions-refuses-ask-guppi`) carries `exists: true`.
- Failed Estimate: `estimate-case-build-reads-the-readers-of-a-changed-step` (L54).
- `guppi check`: 13 lines, exit 1 — 12 pages with `core: true` stand `draft`: `entity-sprint`, `rule-ask`, `rule-case-build`, `rule-close`, `rule-morph`, `rule-orchestration`, `rule-ratification`, `rule-rules-schema`, `rule-search-leaves-out-decisions`, `rule-skill-hi`, `rule-synthesis`, `rule-work-mode`; and `estimate-case-build-reads-the-readers-of-a-changed-step: unread: failed`. The handoff counted 13 lines before the work, each a `core: true` page that stands `draft`; `rule-guppi-config` and `rule-guppi-package` went `draft → built` and `rule-rules-schema` `built → draft` by the cascade of this run.
- Stale defer: `rule-work-mode` is put off in 31 sessions (`backlog.md`).
- No MOC candidate and no contradiction found.
- No read outside the frame.

## Next session

### Cases

- The failed reading of `estimate-case-build-reads-the-readers-of-a-changed-step`: at the `/pre-spec` of session 1713, Case 931 added `drop` to the update items and missed two texts that list those keys (handoff).
- The finding of `/pre-spec` the person left: a backlog line closed `defer case N` by a Case of a conserved Spec in a session of `/box` is a finding of `guppi prespec --check`, before Case 937 and after it, since such a Case has no decision line in the session's window (handoff).
- The two facts of the dropped `## How it works` sections that today's code does not bear out — "subagents inherit no project hook" in `rule-governed-files-hook`, and the condition under which the parent is removed in `rule-spec-write`: which text is right, and whether a docstring or a page should say it (handoff).
- The install steps that the agent gives at a stop: each project's start command written out whole, the offline variables included (L56, handoff).
- `estimate-plugin-install-sets-aside-the-files-of-the-project` — defer into `backlog.md`: its event, the librarian's run of 1713, came, but its session did not take its reading; the offline install of a project with files of its own ran online (handoff `## Debt`).

### Work

- `estimate-rules-schema-leaf-carries-no-how-it-works`
- `estimate-rules-schema-checked`

### Ask the person

- `estimate-close-reports-the-run` — needs the person — Did the report that `/handoff` showed after the librarian's run of 2026-10-30 give each part the Criterion names — the pages created and updated per category, the entries marked incomplete or failed, the pages archived, the flags, the lint total and each part another step of the frame sends to the report — and no test result and no list of files?

## Readings at the close

- `uv run --project .guppi guppi test`: 1819 passed, 6 skipped, 1 deselected, exit 0.
- `uv run --project .guppi guppi check`: 13 lines, exit 1 (above).
- Pages under `vault/wiki/`: decisions 408, entities 5, estimates 326, insights 12, lessons 55, rules 86. Pages under `vault/archive/`: 2998.
