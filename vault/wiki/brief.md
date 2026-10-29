# Brief — 2026-10-29, librarian of session 2312

## Where things stand

- Session 2312 of the sprint `plugin`. Cases ratified: 896 (896.1–896.4), 897 (897.1–897.6); both built again on the findings of `/pre-spec` and ratified again (handoff).
- Code: `.guppi/guppi/casecheck.py` (`written_case_files` keeps only a file that `case_number` names), `.guppi/guppi/ratified.py` (the refusal of a file of `case-guppi` outside `cases/` says it writes only under `cases/`). Two new tests in `.guppi/tests/test_casecheck.py`. `guppi test` 1792 passed, 6 skipped, 1 deselected; `guppi style` clean (handoff).
- Readings: L8 `estimate-clean-branch-ships-neutral-texts` `failed`; L18 `estimate-permissions` `passed` (the person's word); L24–L27 `passed`: `estimate-case-build-goes-on-after-a-compaction`, `estimate-case-build-writes-the-case`, `estimate-case-check-sends-back-a-faulty-case`, `estimate-skill-sprint-open-merges-the-closed-sprint-branch`. Lessons L28–L29, both `error` (handoff, ledger).
- C3 (whether a `Read` before the next `Edit` is enough after the guard wrote a case file) closed as work; whether an `Edit` with no `Read` before it is refused was not seen (handoff).
- `guppi materialize` printed `written with 29 entries` for `vault/raw/2026-10-28/2312/materialize.yaml` and `extended with 0 entries` for the yaml of `1907`. The ledger has 29 lines; the yaml holds an entry for each of lines 1–29 and 12 records under `decisions`, `unparsed: []`. Kinds: 19 `update` (11 rules, 7 estimates, 1 entity), 1 `create` (estimate), 1 `defer` (rule, marked `exists`), 6 `estimate`, 2 `lesson`. The librarian added 2 entries (synthesis). All entries are marked `applied`; none `failed`, `incomplete`, `near` or `merged`.
- `guppi generate` printed 40 pages written or changed for `2312` and 0 for `1907`.
- Pages created (15): decisions 12 (`decision-case-896`, `896.1`–`896.4`, `897`, `897.1`–`897.6`); estimates 1 (`estimate-case-build-goes-on-after-a-live-compaction`, `pending`); lessons 2 (`lesson-orchestration-claimed-a-reading-before-taking-it`, `new`; `lesson-case-build-judged-a-check-by-the-last-stretch-of-the-transcript`, `clustered`).
- Pages updated (25): rules 12 (`rule-case-build`, `rule-orchestration`, `rule-case-check`, `rule-spec-reconcile`, `rule-skill-sprint-open`, `rule-skill-sprint-close`, `rule-where-to-stop`, `rule-documentation`, `rule-case-protocol`, `rule-vault-layout`, `rule-page-generation`, and `rule-permissions` `draft → built` by the cascade); entities 1 (`entity-glossary`); estimates 8 (`estimate-case-build-goes-on-after-a-compaction`, `estimate-case-build-writes-the-case`, `estimate-case-check-sends-back-a-faulty-case`, `estimate-skill-sprint-open-merges-the-closed-sprint-branch` — Criterion replaced and read `passed`; `estimate-permissions` `pending → passed`; `estimate-clean-branch-ships-neutral-texts` — `method` set, `failed` kept; `estimate-ledger-write-keeps-the-window-past-a-later-resume`, `estimate-case-build-reads-the-code-it-states` — `method` set); insights 1 (`insight-case-build-claims-what-code-does-without-reading-it`, child added, `actioned → open`, severity 1); decisions 3 (`decision-case-884` superseded by 896.2, `decision-case-839` and `decision-case-793` superseded by 897.3, all three archived).
- The handoff's instructions, checked: `rule-page-generation` carries `deferred_by: [decision-case-897.3]` and `guppi backlog` lists it (put off in 1 session); `rule-orchestration` and `rule-documentation` carry no `deferred_by` and are gone from `backlog.md`; `.claude/agents/case-guppi.md` holds `autoCompactWindow: 400000` in its frontmatter (line 8); `guppi glossary` rewrote the row `Librarian` of `vault/wiki/glossary.md`.
- This run ticked 32 boxes of `vault/raw/2026-10-28/2312/spec.md` (21 page lines, 4 `read` lines, 6 render lines, 1 glossary line) and the `read estimate-permissions` line of `vault/raw/2026-10-28/1907/spec.md`. One task line stays unticked: `read estimate-case-build-goes-on-after-a-live-compaction`. No `guppi sprint-close --apply` line stands in the Spec.
- `guppi cleanup` printed `3 page(s) moved`: `decision-case-793`, `decision-case-839`, `decision-case-884`, into `vault/archive/plugin/2026-10-29/2312/decisions/`. `guppi render` printed nothing and changed `.claude/agents/case-guppi.md`, `.claude/agents/librarian-guppi.md`, `.claude/skills/sprint-open/SKILL.md`, `.claude/skills/sprint-close/SKILL.md`, `vault/wiki/where-to-stop.md`, `vault/wiki/case-schema.md`. `guppi sprint` left `vault/wiki/sprint.md` unchanged. `guppi backlog`: 17 items → 16 (`rule-orchestration` and `rule-documentation` gone; `insight-case-build-claims-what-code-does-without-reading-it` added). `guppi glossary` changed one row (`Librarian`).
- `guppi archive` printed `raw/2026-10-28/1907 → archive/plugin/2026-10-28/1907/raw`; `raw/2026-10-28/2312` is the session of the run and stays; `raw/2026-10-14/1907` holds no `ledger.md` (only `cases/` and `frontier.md`), so it is no unit. No `pending` Estimate's `method` names the archive step.
- Index check: the one `create` entry is an Estimate, so no Grep of the index check ran.
- Synthesis. `^(root_cause|deferred_by):` over `vault/wiki/lessons/`: 49 lines. `^(pattern|deferred_by):` over `vault/wiki/insights/`: 10 lines.
  - `lesson-orchestration-claimed-a-reading-before-taking-it` — none: it is the main agent stating a fact about subagents' tool calls from their summaries; the lines of `case-guppi` claiming what code, a tool or a page does are another agent and another source, and no lesson line names the main agent's claims on transcripts.
  - `lesson-case-build-judged-a-check-by-the-last-stretch-of-the-transcript` — joined `insight-case-build-claims-what-code-does-without-reading-it`: `case-guppi` described what `written_case_files` does without following its loop. The Insight stood `actioned` by `decision-case-869`; the lesson entry carries no `addressed_by`, so the `update` set it `open`, its `addressed_by` standing.

## Readings due

- `estimate-clean-branch-ships-neutral-texts` (failed) — `rule-clean-branch` (draft) — result (2026-10-29, Plan Mode of 2312): `guppi ship --allow-draft` exit 0; it fails on sentences true only in the repository of GUPPI (`/merge-main` and `/pr-review` in `rule-documentation`, `rule-skill-sprint-close`, `rule-skill-sprint-open`, `rule-where-to-stop`; `rule-case-protocol`; the purpose or method of three Estimates), with doubtful sentences and Criterion sentences listed besides. Read by its `method`: by hand, after the librarian's run of session 2312, with a tag `prod-x.y.z` in the history of HEAD: `guppi ship --allow-draft` into an empty temporary folder, each sentence read whole. This run: the page changes of Case 897 applied to `rule-skill-sprint-open`, `rule-skill-sprint-close`, `rule-where-to-stop`, `rule-documentation`, `rule-case-protocol`, `rule-vault-layout`, `rule-page-generation`, `entity-glossary`, `estimate-ledger-write-keeps-the-window-past-a-later-resume`, `estimate-case-build-reads-the-code-it-states`; `guppi render` wrote the six files named above; no step ran `guppi ship`; `git tag --merged HEAD` prints `prod-0.2.0`, `prod-1`, `prod-2`; the commit of this run comes after this brief.
- `estimate-case-build-goes-on-after-a-live-compaction` (pending) — `rule-case-build` (draft) — read by the unticked `read estimate-case-build-goes-on-after-a-live-compaction` of the Spec of 2312; its `method`: by hand, after the first compaction of a `case-guppi` in a working session; not seen in `git log`, the ledger or the handoff of 2312.
- `estimate-close-commits` (pending, `deferred_by` case 885) — `rule-close` (draft) — by its `method`: `test_render.py -k paths`, then by hand after the librarian's run of the next session whose `.claude/agents/librarian-guppi.md` holds the new Render of `rule-close`: `git log`, `git status` and the report. This run: `guppi render` changed `.claude/agents/librarian-guppi.md`; the close commit of this run comes after this brief.
- `estimate-clean-branch-writes-the-session-files` (pending, `deferred_by` case 885) — `rule-clean-branch` (draft) — by its `method`: `test_ship.py -k skeleton`, then by hand after the librarian's run of the session that set the `method`, with a tag `prod-x.y.z`: an install in an empty folder with no git. This run: no install.
- `estimate-git-context-offers-git-init` (pending, `deferred_by` case 862) — `rule-git-context` (draft) — by its `method`: by hand after the librarian's run, an install into an empty folder with no git, `/hi` three times. This run: no install.
- `estimate-plugin-install-offers-to-install-uv` (pending, `deferred_by` case 862) — `rule-plugin-install` (draft) — by its `method`: after the librarian's run of the session that set the Criterion, with a tag `prod-x.y.z`: an install from a terminal with no `uv`. This run: no install.
- `estimate-plugin-install-undoes-the-copy-when-uv-sync-fails` (pending, `deferred_by` case 862) — `rule-plugin-install` (draft) — by its `method`: after the librarian's run of the session that set the Criterion, with a tag `prod-x.y.z`: an install offline with an empty cache of `uv`. This run: no install.
- `estimate-guppi-package-is-ready-after-the-install` (pending, `deferred_by` case 862) — `rule-guppi-package` (draft) — by its `method`: after a tag `prod-x.y.z`, an install in an empty project with `uv`, `/hi`, and the person's answer.
- `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` (pending) — `rule-case-build` (draft) — by its `method`: after the first Case built under the Render of `rule-case-build` that names a test over a live file; not seen in the handoff or the ledger of 2312.
- `estimate-orchestration-shows-the-built-case` (pending) — `rule-orchestration` (draft) — by its `method`: after the first summary of `case-guppi` in Plan Mode with a line `Other Case` under the new Render; not seen in the handoff or the ledger of 2312.
- `estimate-orchestration-signs-items-taken-together` (pending) — `rule-orchestration` (draft) — by its `method`: after the first batch taken up together in Plan Mode in which a summary carries a line `Other Case`; not seen in the handoff or the ledger of 2312.
- `estimate-hi-writes-frontier` (pending) — `rule-skill-hi` (draft) — by its `method`: the person's answer in the session after the close of a sprint.
- `estimate-morph-sets-up-the-project-at-the-first-hi` (pending) — `rule-morph` (draft) — by its `method`: after the session whose Work Mode builds the setup skill of `rule-morph`; not seen.
- `estimate-ratification-ledger-line-form` (pending) — `rule-ratification` (draft) — by its `method`: after a session whose ledger holds a lesson with the Case that closes its cause, a Case that takes up a decision with more than one Case in its `deferred_by`, and a lesson line that declares a new tag; not seen in the ledger of 2312.
- `estimate-skill-merge-main-joins-a-conflicted-page` (pending) — `rule-skill-merge-main` (draft) — by its `method`: after the first `/merge-main` that leaves a conflicted page; not seen.
- `estimate-skill-pr-review-takes-a-pull-request-whole` (pending) — `rule-skill-pr-review` (draft) — by its `method`: after the first pull request from another account merged by `/pr-review` after the close of `plugin`; not seen.
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` (pending) — `rule-work-mode` (draft) — by its `method`: after the first `/work` on the rendered skill in which a Case is ratified in Work Mode; not seen in the handoff or the ledger of 2312.
- `estimate-sprint-plugin-ci-writes-a-clean-branch` (pending) — `entity-sprint-plugin` (draft) — by its `method`: a run of `.github/workflows/prod.yml` on a tag `prod-x.y.z` of a commit of `plugin`, before the close of `plugin`; it waits for the owner's push of `plugin` and a tag (handoff, Debt).
- `estimate-sprint-plugin-close-steps-run-from-the-line` (pending) — `entity-sprint-plugin` (draft) — by its `method`: at the end of Work Mode of the session that closes `entity-sprint-plugin`.
- `estimate-sprint-plugin-installs-as-a-plugin` (pending) — `entity-sprint-plugin` (draft) — by its `method`: in a session of `plugin` before its close, an install of the clean version into an empty project.
- `estimate-sprint-plugin-pull-requests-reviewed-on-github` (pending) — `entity-sprint-plugin` (draft) — by its `method`: a pull request from a second account, before the close of `plugin`.
- `estimate-sprint-plugin-readme-describes-the-project` (pending) — `entity-sprint-plugin` (draft) — by its `method`: the person's answer on `README.md` at the `/hi` after the session that writes it.

## Flags

- No entry is marked `incomplete`, `failed`, `near` or `unparsed`. The `defer` entry of `rule-page-generation` (line 22) is marked `exists: true`.
- Failed Estimates: `estimate-clean-branch-ships-neutral-texts`.
- `log.md` holds `estimates/estimate-clean-branch-ships-neutral-texts status: failed → failed` for the reading of L8.
- The handoff counts 31 boxes that wait for the librarian; this run ticked 32 in the Spec of 2312 (21 page, 4 `read`, 6 render, 1 glossary), and one more in the Spec of 1907.
- `insight-case-build-claims-what-code-does-without-reading-it` stands `open` with `addressed_by: decision-case-869`, reopened by the synthesis of this run.
- MOC candidates: none seen.
- Stale defers (`backlog.md`): `rule-work-mode` put off in 31 sessions, `rule-clean-branch` in 10, `estimate-spec-write-writes-a-defer` in 4.
- Contradictions: none seen.
- Lint (`guppi check`, exit 1, 12 lines): 10 lines `status: a page with core: true that is draft` (`entity-sprint`, `rule-case-build`, `rule-close`, `rule-git-context`, `rule-guppi-package`, `rule-morph`, `rule-orchestration`, `rule-ratification`, `rule-skill-hi`, `rule-work-mode`); `estimate-clean-branch-ships-neutral-texts: unread: failed`; `estimate-harness-make-runs-in-both-shells: method: the Makefile has no target with`.
- Reads the frame says the job does not need: none.

## Next session

### Cases

- The doubtful sentences of the clean copy that the reading of `estimate-clean-branch-ships-neutral-texts` lists: `entity-guppi` naming `entity-guppi-repository`; `PLAIN_SPRINTS` with `migration` and `plugin` in `rule-ratification`; the `Makefile` and `guppi ship` in `rule-rules-schema`, `rule-entities-schema` and `rule-guppi-package`; and about ten `method`s that wait for "the new Render", "the session that changes it" or "the next session"; each needs the person's judgment (handoff, For the next session).
- The Criterion sentences of shipped Estimates that hold only in GUPPI, listed in the same reading, wait for a Case that rewrites them (handoff, For the next session).
- `estimate-clean-branch-ships-neutral-texts` stands `failed`; its `method` waits for the librarian's run of session 2312 with a tag `prod-x.y.z` in the history of HEAD, and `prod-0.2.0` stands there.

### Work

- none

### Ask the person

- `estimate-guppi-package-is-ready-after-the-install` — needs the person — In an empty project on a machine with `uv`, after the librarian's render, does `/guppi:install` run `uv --version`, ask nothing about `uv`, build `.guppi/.venv/` by `uv sync` after the copy before it sends you to `/hi`, and do the hooks find that environment at the first `/hi`?

## Readings at the close

- `uv run --project .guppi guppi test`: 1792 passed, 6 skipped, 1 deselected.
- `uv run --project .guppi guppi check`: 12 lines (exit 1), as in Flags.
- Pages under `vault/wiki/`: decisions 316, entities 5, estimates 313, insights 10, lessons 51, rules 86.
