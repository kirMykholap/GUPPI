# Brief — 2026-11-25, librarian of session 2003

## Where things stand

- Session 2003 of the sprint `plugin`, 2026-11-25. Cases ratified: 1058, 1059, 1061, 1063 (1063.1, 1063.2, 1063.3). Case 1060 is superseded by 1063.1 (handoff).
- Code: `.guppi/pyproject.toml`, the build line `requires = ["uv_build>=0.11,<0.14"]` and its comment. No test changed. `guppi test` 1994 passed, 6 skipped, 2 deselected; `guppi style` clean (handoff).
- Readings: L20 `estimate-sprint-plugin-uv-build-range-holds-the-uv-of-the-machine` passed; L21 `estimate-case-protocol-case-form` passed. Lesson: L22 `lesson-orchestration-case-built-again-in-another-shape-under-its-old-number` (handoff).
- `guppi materialize` printed `written with 22 entries` for `vault/raw/2026-11-25/2003/materialize.yaml`, and `extended with 0 entries` for the yaml of 0605 and of 0816. The ledger has 22 lines (`wc -l`). The yaml holds 21 entries under `entries`, for lines 1 to 19, 21 and 22; line 20 is folded into the `create` entry of line 2, and `log.md` shows it applied with `#L20` as origin. Every line is accounted for; `unparsed: []`.
- Entries by kind: 4 `create` (all Estimates), 15 `update`, 1 `estimate`, 1 `lesson`; 8 entries under `decisions`. The 6 entries of Case 1060 (lines 3–8) carry `superseded_by: ['1063.1']` and no `applied`; the other 15 carry `applied`. No entry carries `failed` or `exists`; one carries `incomplete` (Flags).
- Index check: the four `create` entries are Estimates, so no Grep ran for them. The `lesson` entry: `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 72 lines; neither same nor near. No yaml edit.
- `guppi generate` printed 22 pages written or changed for 2003 and 0 for 0605 and 0816, and no error line. With the render it ticked 21 lines of `vault/raw/2026-11-25/2003/spec.md` (`git diff --stat`: 21 changed); 3 `read` lines stand unticked (158, 260, 351). No unticked Spec line holds `guppi sprint-close --apply`.
- `guppi cleanup` printed `1 page(s) moved`: `decision-case-1060`, superseded by 1063.1, into `vault/archive/plugin/2026-11-26/2003/decisions/`.
- Pages created (`git status`, `log.md`): decisions 8 (`decision-case-1058`, `-1059`, `-1060`, `-1061`, `-1063`, `-1063.1`, `-1063.2`, `-1063.3`; `-1060` archived, 7 live); estimates 3 (`estimate-sprint-plugin-uv-build-range-holds-the-uv-of-the-machine` `passed`; `estimate-work-mode-runs-the-style-check-before-a-stop` and `estimate-sprint-plugin-passed-one-off-estimate-is-not-read-again` `pending`); lessons 1 (`lesson-orchestration-case-built-again-in-another-shape-under-its-old-number`, `new`).
- Pages updated (`git status`, `log.md`): rules 6 (`rule-work-mode` by 1061, then `built` → `draft` by the cascade; `rule-case-protocol`, `rule-case-build`, `rule-prespec`, `rule-estimates-schema` by 1063.1; `rule-skill-merge-main` by 1063.3); estimates 2 (`estimate-case-protocol-case-form`, Criterion replaced whole by 1063.2, then `pending → passed` by L21; `estimate-skill-merge-main-joins-a-conflicted-page`, Criterion replaced whole by 1063.3, `pending`); entities 1 (`entity-sprint-plugin`: its `## Backlog` line on a passed one-off Estimate removed by 1063.1, two Estimates added); lessons 1 (`lesson-plugin-install-writes-a-project-settings-file`, `source` set by 1058).
- Handoff instructions: the decision lines of Case 1060 were not applied, and `decision-case-1060` stands superseded by `decision-case-1063.1` (`log.md`) and archived. Frontier line C4 of `vault/raw/2026-11-25/2003/frontier.md` closes `· case 1063`. The `guppi check` line on `lesson-plugin-install-writes-a-project-settings-file` no longer prints. The updates of 1063.2 and 1063.3 replaced the Criterion and set `pending`; `estimate-case-protocol-case-form` was then read `passed` by L21 (`log.md` order). The render wrote the six files the handoff names (`git status`). `guppi backlog` did not count one item fewer (Flags).
- `guppi render`, `sprint`, `backlog` and `glossary` printed nothing on stderr. The render changed `.claude/skills/work/SKILL.md`, `vault/wiki/case-schema.md`, `.claude/agents/case-guppi.md`, `.claude/skills/pre-spec/SKILL.md`, `vault/wiki/estimates/schema.yaml` and `.claude/skills/merge-main/SKILL.md`. `guppi glossary` left `glossary.md` unchanged.
- `guppi sprint`: `sprint.md` gained two Done-when lines, `estimate-sprint-plugin-uv-build-range-holds-the-uv-of-the-machine` `- [x] · passed` and `estimate-sprint-plugin-passed-one-off-estimate-is-not-read-again` `- [ ] · pending`. `guppi backlog`: 10 items, as before. Out: the Backlog line of Case 1057.1 on a passed one-off Estimate. In: `rule-work-mode`, `put off in 31 sessions`.
- `guppi archive` moved `raw/2026-11-25/0605` and `raw/2026-11-25/0816` to `vault/archive/plugin/2026-11-25/<HHMM>/raw`; `raw/2026-11-25/2003` is the session of the run.

Synthesis. Greps: `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 72 lines; `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 19 lines. 0 entries added.
- `lesson-orchestration-case-built-again-in-another-shape-under-its-old-number` — none: its cause is that `orchestration.md`, which the main agent loads, lacks the rule of the Splitting section of `case-schema.md` that a Case back in another shape takes a new number, so the main agent sent a correct rebuild back. `insight-case-build-opens-a-new-case-where-one-was-named` (`actioned`, `decision-case-870`) names `case-guppi` putting a new number where the main agent named a Case to change: another agent, the other direction. No lesson names the gap between those two texts. It stays `new`.

## Readings due

27 Estimates: 0 `failed`, 27 `pending`. The session's `spec.md` holds 3 unticked `read` lines (158, 260, 351).

- `estimate-work-mode-runs-the-style-check-before-a-stop` — `rule-work-mode` (draft) — `read` line 158 — method: by hand, after the first `/work` that loads after the librarian's render of `.claude/skills/work/SKILL.md` and reaches a task that opens with `stop:`, its transcript.
- `estimate-sprint-plugin-passed-one-off-estimate-is-not-read-again` — `entity-sprint-plugin` (draft), `once: true` — `read` line 260 — method: by hand, after the librarian's run of session 2003, `vault/wiki/case-schema.md`, `.claude/agents/case-guppi.md`, `.claude/skills/pre-spec/SKILL.md` and `vault/wiki/estimates/schema.yaml`. This run: the render rewrote the four files, and each holds one line with `case 1063.1` (`grep -c`); the `## Backlog` of `entity-sprint-plugin` lost the line on whether a passed one-off Estimate is never read again (`git diff`), and `backlog.md` lost that item.
- `estimate-skill-merge-main-joins-a-conflicted-page` — `rule-skill-merge-main` (draft) — `read` line 351 — method: by hand, after the first `/merge-main` whose merge of `main` leaves a conflicted page.
- `estimate-ask-query-before-a-create` — `rule-ask` (draft) — method: by hand, after the first build of `case-guppi` whose Case proposes a create without a ref, on the Render of `rule-ask` that runs every category.
- `estimate-case-build-goes-on-after-a-live-compaction` — `rule-case-build` (draft) — method: by hand, after the first compaction of a `case-guppi` in a working session.
- `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` — `rule-case-build` (draft) — method: by hand, after the first Case built under the Render that names a test over a live file.
- `estimate-case-build-names-a-stale-line-of-another-case` — `rule-case-build` (draft) — method: by hand, after the first build on the new Render in which the note of `rule-case-check` lists the Case file of another Case of the session.
- `estimate-case-build-offers-a-page-for-code-no-page-covers` — `rule-case-build` (draft) — method: by hand, at the Retro of the session whose Render asks `context` for why the page was chosen; by hand, after a session in which `case-guppi` settles a page for code that no page covers.
- `estimate-case-build-runs-the-vault-query-first` — `rule-case-build` (draft) — method: by hand, after the first build whose Case proposes a create without a ref.
- `estimate-case-build-settles-form-by-itself` — `rule-case-build` (draft) — method: by hand, at the Retro of the session that sets this Criterion, the new Render in the Spec; by hand, after a session whose `case-guppi.md` holds that Render, each round in its transcript.
- `estimate-clean-branch-prod-commits-only-a-tested-copy` — `rule-clean-branch` (draft) — method: by hand, `.github/workflows/prod.yml` read against the Criterion; by hand, after a run of `prod.yml` on GitHub whose step `guppi ship` exits 0, `gh run view --log`. The last commit of `origin/prod` is of 2026-11-03 (`git log`).
- `estimate-hi-writes-frontier` — `rule-skill-hi` (draft) — method: by hand, after the reply that acknowledges the opening Case of `/sprint-open` in the session after the close of a sprint, the person's answer.
- `estimate-orchestration-acknowledging-reply-opens-with-stop-after-prespec` — `rule-orchestration` (draft) — method: by hand, after an acknowledging reply after `/pre-spec` that waits for the person's word, its transcript. The handoff says the reply after `/pre-spec` in session 2003 acknowledged every Case and waited for nothing.
- `estimate-orchestration-dispatches-case-guppi-at-a-level` — `rule-orchestration` (draft) — method: by hand, at the Retro of the session that sets this Criterion, the new Render in the Spec; by hand, after a session whose `orchestration.md` holds that Render, each Agent call of `case-guppi` in its transcript.
- `estimate-orchestration-signs-items-taken-together` — `rule-orchestration` (draft) — method: by hand, after the first batch taken up together in Plan Mode in which a summary carries a line Other Case naming a Case of the session.
- `estimate-retro-loads-on-a-red-command` — `rule-retro` (draft), `deferred_by` Case 1007 — method: by hand, after the librarian's render that writes `.claude/skills/retro/SKILL.md` with `--exit-zero`, and the first load of `/retro` after it. This run: the render left `.claude/skills/retro/SKILL.md` unchanged.
- `estimate-skill-pr-review-takes-a-pull-request-whole` — `rule-skill-pr-review` (draft) — method: by hand, after the first pull request from another account merged by `/pr-review` after the close of `plugin`.
- `estimate-sprint-close-takes-the-readings-in-groups` — `rule-sprint-close` (draft) — method: by hand, after the Work Mode of a session that closed a sprint, its closing Case and ledger.
- `estimate-sprint-plugin-case-guppi-level-trial-decided` — `entity-sprint-plugin` (draft), `once: true` — method: by hand, in the session that closes the sprint `plugin`, the output of `guppi agents` and the findings of `ask-guppi`, the person's answer.
- `estimate-sprint-plugin-close-steps-run-from-the-line` — `entity-sprint-plugin` (draft) — method: by hand, at the end of Work Mode of the session that closes `entity-sprint-plugin`.
- `estimate-sprint-plugin-done-counts-a-one-off-reading` — `entity-sprint-plugin` (draft), `once: true` — method: by hand, after the librarian's run of session 0816, the Purpose of `vault/wiki/entities/entity-sprint-plugin.md`. This run: the diff of that page changes its `estimates`, one `## Backlog` line and its History, not its Purpose.
- `estimate-sprint-plugin-frontierguard-build-read-its-folders-readers` — `entity-sprint-plugin` (draft), `once: true` — method: by hand, after a `case-guppi` build of the sprint `plugin` whose Case adds a file outside `vault/wiki/`, its agent transcript and case file.
- `estimate-sprint-plugin-lesson-root-cause-holds-no-bare-link` — `entity-sprint-plugin` (draft), `once: true` — method: by hand, after the librarian's run that applies the update of `lesson-ledger-reading-writes-a-bare-wikilink`. This run applied no update of that lesson.
- `estimate-sprint-plugin-link-graph-is-gone` — `entity-sprint-plugin` (draft), `once: true` — method: by hand, after the librarian's run that applies the delete of `entity-link-graph`. This run applied no delete.
- `estimate-sprint-plugin-pull-requests-reviewed-on-github` — `entity-sprint-plugin` (draft) — method: by hand, a pull request from a second account read on GitHub, before the close of the sprint.
- `estimate-sprint-plugin-readme-describes-the-project` — `entity-sprint-plugin` (draft) — method: by hand, the person's answer on `README.md` at the `/hi` of the session after the one whose Work Mode writes it, before the close of the sprint.
- `estimate-synthesis-keeps-actioned-by-the-mark` — `rule-synthesis` (draft), `deferred_by` Case 1009 — method: by hand, after a librarian's run that puts a lesson with `addressed_by` under an Insight that stands `actioned`, the yaml and the brief. This run: the yaml held 1 `lesson` entry, with no `addressed_by`; the synthesis put it under no Insight and added no entry.

## Flags

- `incomplete`: the entry of line 8, the `create` of `estimate-sprint-plugin-passed-one-off-estimate-is-not-read-again` by Case 1060, carries `incomplete: [criterion]`; it is superseded by 1063.1 and not applied, and the page was written from line 16 with its Criterion.
- No entry `failed`, `near` or `unparsed`. No failed Estimate.
- Lint (`guppi check`, exit 0): no line. The baseline line of the handoff on `lesson-plugin-install-writes-a-project-settings-file` (missing `source`) no longer prints.
- `guppi materialize` printed 22 entries for 2003; the yaml holds 21 under `entries` and line 20 folded into the entry of line 2.
- `guppi backlog` counts 10 items before and after this run, not one fewer as the handoff expected: the Backlog line of Case 1057.1 left, and `rule-work-mode` came in, `put off in 31 sessions`. The cascade set `rule-work-mode` `built` → `draft` when its new `pending` Estimate was added; the `## Backlog` of the archived `entity-sprint-migration` names it, and `guppi backlog` passes over a line of a closed sprint only when its page is finished (`.guppi/guppi/backlog.py`, `finished`, case 743.4).
- `log.md` holds two lines `decisions/decision-case-1060 archived`, one `· superseded · generate` and one `· cleanup`.
- Handoff observation: `guppi prespec --check` printed notes that two Criterion lines of the Estimates of 1063.2 and 1063.3 are not carried; the handoff says each is the line its sub-case qualifies on purpose.
- Handoff observation: the `ask-guppi` run at `/pre-spec` had no web tool and did not check the uv docs claims of Case 1059.
- Handoff note: the number 1062 was used by `case-guppi` and never held by `guppi caseid`; `cases/case-1062.md` stands empty.
- Read outside the frame: `vault/raw/2026-11-25/2003/spec.md` read whole, past its unticked lines, for Readings due and Next session; the handoff did not ask for it.
- Read outside the frame: a search of the text of the pages under `vault/archive/` (a `grep -l` of `rule-work-mode` over archived `entity-sprint-*.md`), to say why `guppi backlog` did not count one item fewer, as instruction 2 of the handoff expected; the handoff did not ask for the read.
- No MOC candidate, no stale defer and no contradiction printed by `guppi check`, `guppi backlog` or this run.

## Next session

Cases
- Whether `orchestration.md` should say that a ratified Case that comes back in another shape is built under a new number with `{supersedes:case N}`, in Plan Mode too, as `case-schema.md` sets it; `lesson-orchestration-case-built-again-in-another-shape-under-its-old-number` records the cause (handoff).
- The sprint item `rule-clean-branch`, `estimate-sprint-plugin-ci-writes-a-clean-branch` (The clean branch), put off in session 2003 (handoff).
- `rule-work-mode` came back into `backlog.md`, `put off in 31 sessions`, from the `## Backlog` of the archived `entity-sprint-migration`, once the cascade set it `draft` for its new `pending` Estimate (`guppi backlog`, `.guppi/guppi/backlog.py`).

Work
- `estimate-orchestration-dispatches-case-guppi-at-a-level`: session 2003 ran on the `orchestration.md` that the librarian's render of session 0816 wrote.
- `estimate-case-build-settles-form-by-itself`: session 2003 ran on the `case-guppi.md` that the librarian's render of session 0816 wrote.

Ask the person
- `estimate-sprint-plugin-readme-describes-the-project` — needs the person — does `README.md` at the root of the branch `plugin` describe GUPPI as it stands, with its Why, Is it for you, how a session goes, its parts, its install and its use?

## Readings at the close

- `uv run --project .guppi guppi test`: exit 0, 1994 passed, 6 skipped, 2 deselected.
- `uv run --project .guppi guppi check`: exit 0, no line.
- Live pages (`find vault/wiki/<category> -name "*.md"`): decisions 638, rules 90, entities 5, estimates 379, lessons 73, insights 19; 11 files at the root of `vault/wiki/`. Files under `vault/archive/` (`find -name "*.md"`): 3434 after `guppi archive`.
