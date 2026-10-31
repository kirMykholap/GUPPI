# Handoff — 2026-10-31, the core pages that stand draft and the Estimates that wait

## Notes from memory

- The person took the recommended answer on almost every round. Two answers went their own way: in Case 956 the person pictured the route the hook takes (the librarian returns its report, a hook copies it, the main agent shows and commits the file), which became option (c) of a later round; in Case 962 the person agreed to a one-time Estimate and raised whether one-time Estimates should be told apart from lasting ones, which Case 963 puts off.
- The person said Claude Code's withheld approval of a long plan is a bug of Claude Code and has been reported to Anthropic; Case 957 puts the fix off.
- The person's rule for pages with `core: true` that wait for the close of a sprint ("take core off until the close") was dropped when the round showed that `rule-skill-hi` writes `/hi` and must ship; `prod` waits for the close of `plugin` in any case.
- The person called an Estimate whose evidence stands only in a chat a bad Estimate; Case 960 answered it by naming the transcript as the place to read.
- The session was long: the context passed 400 000 tokens before Retro.

## Direct instructions to the librarian

- Cases 961.6 and 956.1 are superseded in this session by Cases 964 and 965 (`{supersedes:case 961.6}`, `{supersedes:case 956.1}`). Materialize the work of the superseding Cases only.
- Case 965 creates `rule-librarian-report-copy` with no `core` in the `create` and sets `core: true` by an `update` with `set` right after it; check that the page is born with `core: true` as a boolean and with `parent: rule-documentation`, and that `rule-documentation` gains it in `children`.
- Case 965 updates `rule-hook-registry` by one `replace` pair on the `SubagentStop` entry; after the render, `.claude/settings.json` holds `guppi libreport` beside `guppi casecheck --subagent`. That hook may fire for your own run in this session and write `vault/raw/2026-10-31/0431/report.md`; a one-off task of Case 956.3 has the main agent commit it after `/handoff`.
- Renders due: `.claude/settings.json` (Case 965), `.claude/agents/librarian-guppi.md` (956.2), `.claude/skills/handoff/SKILL.md` (956.3), `.claude/skills/box/SKILL.md` (956.4), `vault/wiki/estimates/schema.yaml` and `vault/wiki/case-schema.md` (960.1), and `guppi sprint` for `entity-sprint-plugin` (962).
- Six Estimates read `failed` at /hi and Retro (`estimate-close-reports-the-run` at /hi, and five at Retro); they enter the backlog of Cases as debt.
- The cascade should set `entity-guppi` and `entity-sprint` `built` if their Estimates now all pass, and `rule-search-leaves-out-decisions` and `rule-where-to-stop` too; `rule-backlog` turns `draft` by the new `estimate-backlog-keeps-the-work-taken-out-of-a-built-page`.

## What actually got done

- Cases ratified: 956 (956.2, 956.3, 956.4, 956.5), 957, 959, 960 (960.1, 960.2, 960.3), 961 (961.1–961.5), 962, 963, 964, 965. Cases 956, 959, 960, 961 and 962 were built again on the findings of `/pre-spec` and ratified again; 964 and 965 were ratified in Work Mode. Case 958 was dropped with no decision line.
- Code and tests: `.guppi/guppi/libreport.py` (new, the `SubagentStop` hook), `.guppi/guppi/cli.py` (the command `libreport`), `.guppi/tests/test_libreport.py` (new, 8 tests).
- `uv run --project .guppi guppi test`: 1822 passed, 6 skipped, 1 deselected at the baseline; 1830 passed, 6 skipped, 1 deselected after the tasks and at Retro. `uv run --project .guppi guppi style`: clean.
- By hand in Work Mode: the probe of Case 956.2 (a subagent's `Write` of `report.md` refused by its name, `close.md` written), and the trial of the hook on `vault/wiki/decisions/` with `ask-guppi`.
- Readings: L1 passed, L2 failed (at /hi); L36–L42 and L48 passed; L43–L47 failed. Lessons: L49 (knowledge), L50 (error).

## Debt

- No box of the Spec is debt, and no test was reverted.
- The page, render, sprint and read lines of the Spec wait for the librarian.
- `estimate-close-reports-the-run` — after the librarian's run of a session that starts with the hook of `rule-librarian-report-copy` registered and the new frame of the librarian.
- `estimate-handoff-dispatches` — after a `/handoff` on the Render of `rule-handoff` that commits `report.md`.
- `estimate-spec-box-runs-a-conserved-spec` — after a session that runs a conserved Spec by `/box` on the new Render of `rule-spec-box`.
- `estimate-close-commits` — after a librarian's run on the new frame, with the commit of `report.md` after it.
- `estimate-ratification-ledger-line-form` — after a lesson line that declares a new tag by a `newtag` block.
- `estimate-backlog-keeps-the-work-taken-out-of-a-built-page` — after the librarian's run of this session, in the session whose brief puts it under Work.
- `estimate-sprint-plugin-ci-writes-a-clean-branch` — the close of the sprint `plugin`, since `rule-skill-hi` stands `draft` until the `/hi` after that close and `guppi ship` writes nothing to `prod` before.
- The other Estimates of the live sprint page — the Retro of the session that finishes their work, or the close of `plugin`.
- `estimate-case-build-keeps-the-old-form-until-the-writer-is-live`, `estimate-case-build-goes-on-after-a-live-compaction`, `estimate-orchestration-signs-items-taken-together`, `estimate-synthesis-keeps-actioned-by-the-mark` — their events, as their methods name them; Case 961 left them as they stand.

## Observations

- Red before the work: `uv run --project .guppi guppi check` exit 1 with 13 lines, each a page with `core: true` that stands `draft`; `## Expected red` of `work.md` is empty.
- The hook of `rule-spec-write` lifts every value of a `create` as a string unless it opens with `[` or `{` (L50); `/pre-spec` printed no finding on the string `'true'`.
- Claude Code refuses a subagent's `Write` of a file named `report.md` by its name (L49); the librarian's `report.md` of session 0128 was lost to it.
- The answer of a `case-guppi` that fixed its Case opened with prose and put `**Built:**` on its fourth line, and the main agent showed it as a built Case (L45).
- `ask-guppi` at `/pre-spec` reported two searches of its own that broke its frame: Greps of text over `vault/archive/` and a read of an archived sprint page; it said no finding rested on them.
- In Work Mode the main agent showed Case 964 again with text of its own before the Case; the check noted it at the next message.

## For the next session

- The five failed Estimates of Retro and the one of /hi each need a Case: `estimate-case-build-reads-the-readers-of-a-changed-step` (a builder missed a skill that does the same step), `estimate-ask-query-before-a-create` (the rules Grep did not come first), `estimate-orchestration-shows-the-built-case` (a built Case shown from an answer whose first line was not `**Built:**`), `estimate-orchestration-names-related-cases-in-the-dispatch` (the sentence on a related Case did not name the pages it changes), `estimate-case-build-reads-each-list-of-a-new-member` (no search for a member already in the list; the docstring list of `.guppi/guppi/cli.py` was missed).
- Whether the hook of `rule-spec-write` lifts a scalar of a `create` as YAML, or `case-schema.md` gives a form for a boolean (L50).
- Case 963, the split of one-time Estimates from lasting ones, put off to the next session by the person.

## Ask the person
