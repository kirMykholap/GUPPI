# Brief — 2026-10-31, librarian of session 0431

## Where things stand

- Session 0431 of the sprint `plugin`. Cases ratified: 956 (956.2, 956.3, 956.4, 956.5), 957, 959, 960 (960.1, 960.2, 960.3), 961 (961.1–961.5), 962, 963, 964, 965. Cases 956, 959, 960, 961 and 962 were built again on the findings of `/pre-spec` and ratified again; 964 and 965 were ratified in Work Mode. Case 958 was dropped with no decision line. Cases 961.6 and 956.1 are superseded by 964 and 965 (handoff).
- Code and tests: `.guppi/guppi/libreport.py` (new, the `SubagentStop` hook), `.guppi/guppi/cli.py` (the command `libreport`), `.guppi/tests/test_libreport.py` (new, 8 tests). `guppi test` 1822 passed, 6 skipped, 1 deselected at the baseline; 1830 passed, 6 skipped, 1 deselected after the tasks and at Retro; `guppi style` clean (handoff).
- By hand in Work Mode: the probe of Case 956.2 (a subagent's `Write` of `report.md` refused by its name, `close.md` written) and the trial of the hook on `vault/wiki/decisions/` with `ask-guppi` (handoff).
- Readings: L1 passed, L2 failed (at /hi); L36–L42 and L48 passed; L43–L47 failed. Lessons: L49 (knowledge), L50 (error) (handoff).
- `guppi materialize` printed `written with 50 entries` for `vault/raw/2026-10-31/0431/materialize.yaml` and `extended with 0 entries` for the yaml of `0128`. The ledger has 50 lines (`wc -l`); the yaml holds 47 entries for lines 1–38 and 42–50, and lines 39, 40 and 41 are folded into the `create` entries of lines 34, 14 and 18, so every line is accounted for. Kinds: 24 `update`, 7 `create`, 2 `defer`, 12 `estimate`, 2 `lesson`; the 4 superseded entries below are among the `update` and `create` counts.
- Marks: 66 `applied` lines (43 under `entries`, 23 under `decisions`); 2 `exists` (the `defer` entries of lines 13 and 29); 1 `incomplete` (line 4, superseded); no entry `failed`, `near`, `librarian` or `merged`; `unparsed: []`.
- Superseded and not applied, as the handoff asked: lines 3, 4 and 5 (Case 956.1, superseded by 965) and line 26 (Case 961.6, superseded by 964).
- `guppi generate` printed 61 pages written or changed for `0431` and 0 for `0128`; nothing on stderr. No unticked Spec line holds `guppi sprint-close --apply`. `guppi cleanup` printed `2 page(s) moved`, nothing on stderr. `guppi render`, `sprint`, `backlog` and `glossary` printed nothing on stderr.
- Pages created (28), from `git status`: decisions 21 live (`decision-case-956`, `956.2`, `956.3`, `956.4`, `956.5`, `957`, `959`, `960`, `960.1`, `960.2`, `960.3`, `961`, `961.1`–`961.5`, `962`, `963`, `964`, `965`) and 2 created and archived (`decision-case-956.1`, `decision-case-961.6`); rules 1 (`rule-librarian-report-copy`, `built`, `core: true`); estimates 4 (`estimate-sprint-keeps-one-live-page` `passed`, `estimate-estimates-schema-method-names-its-evidence` `passed`, `estimate-librarian-report-copy-writes-the-file` `passed`, `estimate-backlog-keeps-the-work-taken-out-of-a-built-page` `pending`); lessons 2 (`lesson-librarian-claude-code-refuses-a-report-file-of-a-subagent-by-its-name`, `lesson-spec-write-lifts-a-create-value-as-a-string`).
- Pages updated (31), from `git status`: rules 11 (`rule-backlog`, `rule-case-protocol`, `rule-close`, `rule-documentation`, `rule-estimates-schema`, `rule-handoff`, `rule-hook-registry`, `rule-search-leaves-out-decisions`, `rule-spec-box`, `rule-where-to-stop`, `rule-work-mode`); estimates 16; entities 3 (`entity-guppi`, `entity-sprint`, `entity-sprint-plugin`); insights 1 (`insight-plugin-cli-withholds-approval-of-a-long-plan`, deferred by Case 957).
- Defers: `insight-plugin-cli-withholds-approval-of-a-long-plan` (Case 957) and `rule-estimates-schema` (Case 963), both pages on disk (`exists`).
- Superseded and moved by `cleanup` to `vault/archive/plugin/2026-10-31/0431/decisions/`: `decision-case-956.1`, `decision-case-961.6`.
- Cascade (log): `entity-guppi` `draft → built`, `entity-sprint` `draft → built`, `rule-librarian-report-copy` `draft → built`, `rule-search-leaves-out-decisions` `draft → built`, `rule-where-to-stop` `draft → built`, `rule-work-mode` `draft → built`; `rule-backlog` `built → draft`, `rule-handoff` `built → draft`, `rule-spec-box` `built → draft`.
- The handoff's instructions, checked: `rule-librarian-report-copy` stands with `core: true` as a boolean and `parent: "[[rule-documentation]]"`, and the `children` of `rule-documentation` holds it; `.claude/settings.json` holds `guppi libreport` beside `guppi casecheck --subagent` in the `SubagentStop` entry (line 58); the render wrote `.claude/settings.json`, `.claude/agents/librarian-guppi.md`, `.claude/skills/handoff/SKILL.md`, `.claude/skills/box/SKILL.md`, `vault/wiki/estimates/schema.yaml` and `vault/wiki/case-schema.md` (`git status`); `guppi sprint` ran and left `vault/wiki/sprint.md` unchanged, since it does not read the `## Backlog` of the sprint page. The cascade set `entity-guppi`, `entity-sprint`, `rule-search-leaves-out-decisions` and `rule-where-to-stop` `built`, and `rule-backlog` `draft`.
- `backlog.md` went from 5 items to 8: `rule-estimates-schema` (Case 963), the two notes taken out of `rule-work-mode` and `rule-spec-box` (Case 962) and `rule-spec-box` entered it; `rule-work-mode` left it.
- This run ticked 37 boxes of `vault/raw/2026-10-31/0431/spec.md` (`git diff`); 7 boxes stay unticked (6 `read` boxes and the by-hand box of Case 956.3).
- Index check: the one `create` that is not an Estimate, `rule-librarian-report-copy` (line 32), compared by `^(purpose|deferred_by):` over `vault/wiki/rules/` (87 lines): no page holds the same purpose and none is near; the closest index lines, `rule-close` and `rule-hook-registry`, guard the librarian's commit and the registration of hooks. The 2 `lesson` entries compared by `^(root_cause|deferred_by):` over `vault/wiki/lessons/` (56 lines): none the same, none near.
- Synthesis: `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 56 lines; `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 13 lines.
  - `lesson-librarian-claude-code-refuses-a-report-file-of-a-subagent-by-its-name` — none: no lesson or Insight blames a refusal of Claude Code that judges a file name; the `SubagentStop` lessons record the payload and the handback, and `insight-plugin-cli-withholds-approval-of-a-long-plan` a limit of the plan dialog.
  - `lesson-spec-write-lifts-a-create-value-as-a-string` — none: no lesson or Insight blames how `put` of `ratified.py` lifts a scalar; `lesson-ratified-defer-only-case-wants-its-fence-in-the-reply` blames another function of the same file, a short-form Case read from the reply.

## Readings due

- `estimate-case-build-reads-the-readers-of-a-changed-step` — `failed`; target `rule-case-build` (`draft`); method: at Retro, the findings of `ask-guppi` at a `/pre-spec` read in its agent transcript. Result: 1 of 11 findings of the `/pre-spec` of session 0128 is a Case that missed a skill that does the same step (Case 952 and `.claude/skills/grill-me/SKILL.md`).
- `estimate-ask-query-before-a-create` — `failed`; target `rule-ask` (`draft`); method: at Retro, the builds of Cases 787.1 and 804.6 read in their transcripts. Result: in both builds vault searches came before the rules Grep `^(purpose|deferred_by):`, and in 804.6 no lessons or insights Grep ran.
- `estimate-orchestration-shows-the-built-case` — `failed`; target `rule-orchestration` (`draft`); method: at Retro, the showing of Cases 960 and 956 in the transcript of session 0431. Result: the answer of the `case-guppi` of 956 put `**Built:**` on its fourth line and the main agent showed it as a built Case.
- `estimate-orchestration-names-related-cases-in-the-dispatch` — `failed`; target `rule-orchestration` (`draft`); method: at Retro, the dispatch of Case 961 in the transcript of session 0431. Result: the sentence on the related Case 960 named its new Estimate and not the pages it changes.
- `estimate-case-build-reads-each-list-of-a-new-member` — `failed`; target `rule-case-build` (`draft`); method: at Retro, the build of Case 956.1 and the `/pre-spec` of session 0431. Result: the `case-guppi` ran no search for a hook already in the list and missed the docstring list of `.guppi/guppi/cli.py`.
- `estimate-backlog-keeps-the-work-taken-out-of-a-built-page` — `pending`; target `rule-backlog` (`draft`); read by its unticked `read` box in `vault/raw/2026-10-31/0431/spec.md` (Case 962): after the librarian's run of a session in which the Backlog of `entity-sprint-plugin` holds the notes, `vault/wiki/backlog.md` read in the session whose brief puts the reading under Work. This run: the `## Backlog` of `entity-sprint-plugin` holds the two notes (lines 34 and 35); `guppi backlog` wrote under `## Deferred` of `backlog.md` the lines `The rest of Work Mode past the skill /work: … taken out of rule-work-mode (case 962) · put off in 0 sessions` and `The Spec box, its second part: … taken out of rule-spec-box (case 962) · put off in 0 sessions`; `rule-work-mode` stands `built`, `rule-spec-box` `draft`.
- `estimate-close-reports-the-run` — `pending` (set by Case 956.2 after L2 read it `failed` at /hi); target `rule-close` (`draft`); read by its unticked `read` box in the 0431 Spec (Case 956.2): after the librarian's run of a session that starts with the hook of `rule-librarian-report-copy` registered and the new Render of `rule-close`, `report.md` beside the last output in the agent transcript. This run: it started on the frame whose Close step writes `report.md` by `Write`; its render wrote `.claude/settings.json` with `guppi libreport` and `.claude/agents/librarian-guppi.md` with the new Close step.
- `estimate-close-commits` — `pending`; target `rule-close` (`draft`); read by its unticked `read` box in the 0431 Spec (Case 956.5): `test_render.py -k paths`, and by hand after a librarian's run on the Render of `rule-close`, its commit, the paths and `git status`. This run: `guppi render --paths` printed 32 paths; the commit of this run follows this brief.
- `estimate-handoff-dispatches` — `pending`; target `rule-handoff` (`draft`); read by its unticked `read` box in the 0431 Spec (Case 956.3): after a `/handoff` on the Render of `rule-handoff` that commits `report.md`.
- `estimate-spec-box-runs-a-conserved-spec` — `pending`; target `rule-spec-box` (`draft`); read by its unticked `read` box in the 0431 Spec (Case 956.4): `guppi render --check`, and by hand after a session that runs a conserved Spec by `/box` on the Render that commits `report.md`.
- `estimate-ratification-ledger-line-form` — `pending`; target `rule-ratification` (`draft`); read by its unticked `read` box in the 0431 Spec (Case 961.5): after a lesson line that declares a new tag by a `newtag` block, with the marks in five archived ledgers and the take-up line of case 629.2.
- `estimate-orchestration-signs-items-taken-together` — `pending`; target `rule-orchestration` (`draft`); method: after the first batch of items taken up together in Plan Mode under the new Render in which a summary carries a line `Other Case`.
- `estimate-case-build-goes-on-after-a-live-compaction` — `pending`; target `rule-case-build` (`draft`); method: after the first compaction of a `case-guppi` in a working session.
- `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` — `pending`; target `rule-case-build` (`draft`); method: after the first Case built under the Render that names a test over a live file and changes a reader in code and the text it reads.
- `estimate-synthesis-keeps-actioned-by-the-mark` — `pending`; target `rule-synthesis` (`draft`); method: after a librarian's run that puts a lesson with `addressed_by` under an `actioned` Insight. This run: neither `lesson` entry carries `addressed_by`; the synthesis put neither under an Insight.
- `estimate-plugin-install-sets-aside-the-files-of-the-project` — `pending`, `deferred_by: decision-case-949`; target `rule-plugin-install` (`draft`); method: after the librarian's run of the session that sets this Criterion, with a tag `prod-x.y.z`, installs into three projects with files of their own. This run: `backlog.md` lists the Estimate.
- `estimate-morph-takes-in-the-set-aside-files` — `pending`; target `rule-morph` (`draft`); method: after the session whose Work Mode builds the setup skill of `rule-morph` and its step in `/hi`.
- `estimate-morph-sets-up-the-project-at-the-first-hi` — `pending`; target `rule-morph` (`draft`); method: after the session whose Work Mode builds the setup skill of `rule-morph`, its step in `/hi` and in `/sprint-open`.
- `estimate-hi-writes-frontier` — `pending`; target `rule-skill-hi` (`draft`); method: the person's answer in the session after the close of a sprint, at the reply that acknowledges the opening Case of `/sprint-open`.
- `estimate-skill-merge-main-joins-a-conflicted-page` — `pending`; target `rule-skill-merge-main` (`draft`); method: after the first `/merge-main` whose merge of main leaves a conflicted page.
- `estimate-skill-pr-review-takes-a-pull-request-whole` — `pending`; target `rule-skill-pr-review` (`draft`); method: after the first pull request from another account merged into main by `/pr-review` after the close of `plugin`.
- `estimate-sprint-plugin-ci-writes-a-clean-branch` — `pending`; target `entity-sprint-plugin` (`draft`, the live sprint page); method: `test_ship.py`, then after a run of `.github/workflows/prod.yml` on a tag `prod-x.y.z` that writes `prod`, before the close of `plugin`.
- `estimate-sprint-plugin-installs-as-a-plugin` — `pending`; target `entity-sprint-plugin` (`draft`, the live sprint page); method: in a session of the sprint before its close, a clean copy installed in an empty project and `/hi` typed.
- `estimate-sprint-plugin-pull-requests-reviewed-on-github` — `pending`; target `entity-sprint-plugin` (`draft`, the live sprint page); method: a pull request from a second account read on GitHub, before the close of the sprint.
- `estimate-sprint-plugin-readme-describes-the-project` — `pending`; target `entity-sprint-plugin` (`draft`, the live sprint page); method: the person's answer on `README.md` at the `/hi` after the session that writes it, before the close of the sprint.
- `estimate-sprint-plugin-close-steps-run-from-the-line` — `pending`; target `entity-sprint-plugin` (`draft`, the live sprint page); method: at the end of Work Mode of the session that closes `entity-sprint-plugin`.

## Flags

- `incomplete`: line 4, `estimate-librarian-report-copy-writes-the-file` of Case 956.1 lacked `criterion`; the entry is superseded by Case 965 and was not applied; the `create` of line 34 wrote the page with its Criterion. No entry marked `failed`, `near` or `unparsed`.
- Failed Estimates: 5 (above, first in Readings due).
- `estimate-close-reports-the-run` read `failed` at /hi (L2) and stands `pending`, since the `update` of Case 956.2 (line 8) set it `pending` with a new method and Criterion after the reading. The handoff counts it among six failed Estimates.
- `guppi check`: 16 lines, exit 1. 11 are pages with `core: true` that stand `draft`: `rule-ask`, `rule-backlog`, `rule-case-build`, `rule-close`, `rule-handoff`, `rule-morph`, `rule-orchestration`, `rule-ratification`, `rule-skill-hi`, `rule-spec-box`, `rule-synthesis`; 5 are `unread: failed` on the five failed Estimates. The handoff counted 13 lines at the baseline.
- `estimate-orchestration-signs-items-taken-together`: the ledger line L45 records a summary of Case 960 with a line `Other Case: Case 956` and both Cases shown and ratified again in one reply; the inputs do not say whether the items were taken up together as a batch; the reading stays in Readings due alone.
- Stale defer: `rule-spec-box` is put off in 8 sessions (`backlog.md`).
- Handoff observation: `ask-guppi` at `/pre-spec` reported two searches of its own that broke its frame, Greps of text over `vault/archive/` and a read of an archived sprint page, and said no finding rested on them.
- Handoff observation: in Work Mode the main agent showed Case 964 again with text of its own before the Case; the check noted it at the next message.
- No MOC candidate and no contradiction found.
- No read outside the frame.

## Next session

### Cases

- `estimate-case-build-reads-the-readers-of-a-changed-step` failed: a builder missed a skill that does the same step (handoff `## For the next session`).
- `estimate-ask-query-before-a-create` failed: the rules Grep did not come first (handoff `## For the next session`).
- `estimate-orchestration-shows-the-built-case` failed: a built Case shown from an answer whose first line was not `**Built:**` (handoff `## For the next session`).
- `estimate-orchestration-names-related-cases-in-the-dispatch` failed: the sentence on a related Case did not name the pages it changes (handoff `## For the next session`).
- `estimate-case-build-reads-each-list-of-a-new-member` failed: no search for a member already in the list; the docstring list of `.guppi/guppi/cli.py` was missed (handoff `## For the next session`).
- `estimate-close-reports-the-run` failed at /hi (L2): no `report.md` of session 0128; the handoff asks a Case for it; the page stands `pending` after Case 956.2.
- Whether the hook of `rule-spec-write` lifts a scalar of a `create` as YAML, or `case-schema.md` gives a form for a boolean (L50; handoff `## For the next session`).
- Case 963, the split of one-time Estimates from lasting ones, put off to the next session by the person (handoff `## For the next session`).

### Work

- `estimate-backlog-keeps-the-work-taken-out-of-a-built-page`, its `read` box in `vault/raw/2026-10-31/0431/spec.md` included.
- The unticked by-hand box of Case 956.3 in `vault/raw/2026-10-31/0431/spec.md`: after `/handoff` of session 0431, the main agent shows `report.md` and commits it alone.

### Ask the person

- none

## Readings at the close

- `uv run --project .guppi guppi test`: 1830 passed, 6 skipped, 1 deselected, exit 0.
- `uv run --project .guppi guppi check`: 16 lines, exit 1 (above).
- Pages under `vault/wiki/`: decisions 445, entities 5, estimates 336, insights 13, lessons 58, rules 87. Pages under `vault/archive/`: 3080 before and after `guppi archive`, which printed nothing and moved nothing: the units left in `raw/`, `2026-10-31/0128` and `2026-10-31/0431`, are dated the day of the run, and `guppi archive` looks only at units dated before it (`.guppi/guppi/archive.py`).
