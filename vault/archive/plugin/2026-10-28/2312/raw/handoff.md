# Handoff — 2026-10-28, the procedure for a full case-guppi and the neutral texts of the clean copy

## Notes from memory

- The person answered most rounds with "Согласен", taking the recommended option. Q3 of Case 896 (the compaction size) had no single recommendation; the person's "Согласен" was read as (a), 400 000, after the main agent's text named (a) as the one that holds the limit, and `case-guppi` built it that way.
- Case 897 changed course at `/pre-spec`. Q8 first put the merge exception of the librarian frame in a bracket. The person's answer to the report (Q1) then widened it, with no skill name and no bracket, to any merge of `main` in the librarian frame, `rule-vault-layout`, `rule-page-generation` and the row `Librarian` of `entity-glossary`. The premise of Q8 fell: 897.2 tells a project without `/merge-main` to bring its branch up to `main`.
- The put-off of Case 839 on `rule-documentation` closes on the text of the librarian frame, not on a reading: `estimate-close-commits` stands `pending` and is itself put off by Case 885, as the `context` of Case 897 says.
- The size of 400 000 is not checked: the documentation gives no rule for how far below a set window a subagent compacts. In the test, at 100 000, it came at about three quarters. `estimate-case-build-goes-on-after-a-live-compaction` records the real point.
- C1 (the CI run of `rule-clean-branch` on a tag `prod-x.y.z`) was left for a later session: it needs the owner's push of `plugin` and a tag.

## Direct instructions to the librarian

- Case 896.2 and Case 897.5 both change pages of `rule-case-build`: 896.2 the rule and `estimate-case-build-writes-the-case`, 897.5 only the `method` of `estimate-case-build-reads-the-code-it-states`. The second pass found no shared page.
- Case 897.3 carries an `update` and a `defer` of `rule-page-generation` with `{supersedes:case 793}`: the old put-off is taken up and put off again with the same text, so `rule-page-generation` stays in `backlog.md`, now with `decision-case-897.3` in its `deferred_by`.
- Case 896.2 carries `{supersedes:case 884}` on `rule-orchestration`: the put-off on the growing context of `case-guppi` is taken up, and `rule-orchestration` leaves `backlog.md` unless another defer holds it.
- Case 897.3 carries `{supersedes:case 839}` on `rule-documentation`: the put-off closes, and `rule-documentation` leaves `backlog.md`.
- After the render, check that `.claude/agents/case-guppi.md` holds `autoCompactWindow: 400000` in its frontmatter, and that `guppi glossary` rewrote the row `Librarian`.
- The reading of `estimate-clean-branch-ships-neutral-texts` (failed, line 8) lists doubtful sentences and Criterion sentences that no Case of this session fixes; it is the list for later Cases.

## What actually got done

- Cases ratified: 896 (896.1–896.4), 897 (897.1–897.6). Both were built again on the findings of `/pre-spec` and ratified again.
- Code: `.guppi/guppi/casecheck.py` (`written_case_files` keeps only a file that `case_number` names; the module docstring and the function docstring say so), `.guppi/guppi/ratified.py` (the refusal of a file of `case-guppi` outside `cases/` says it writes only under `cases/` of a session folder). Tests: two new tests in `.guppi/tests/test_casecheck.py`, one for the note beside the Case file and one for a round after only the note, which also runs `cases_out` of `onward.py` over the note.
- `uv run --project .guppi guppi test`: 1792 passed, 6 skipped, 1 deselected. `uv run --project .guppi guppi style`: clean.
- Readings: L8 `estimate-clean-branch-ships-neutral-texts` failed (Plan Mode, five reading agents over the clean copy); L18 `estimate-permissions` passed (the person's word); the four readings of Retro, all passed: `estimate-case-build-goes-on-after-a-compaction`, `estimate-case-build-writes-the-case`, `estimate-case-check-sends-back-a-faulty-case`, `estimate-skill-sprint-open-merges-the-closed-sprint-branch`.
- Lessons, both `error`: `lesson-orchestration-claimed-a-reading-before-taking-it`, `lesson-case-build-judged-a-check-by-the-last-stretch-of-the-transcript`.
- C3 (whether a `Read` before the next `Edit` is enough after the guard wrote a case file) closed as work. In the two transcripts of `case-guppi`, each `Write` and `Edit` of a case file was written by the guard with exit 2, a `Read` came before each next `Edit`, and no other tool error stood. Whether an `Edit` with no `Read` before it would be refused was not seen.

## Debt

- No box is debt.
- Boxes that wait for the librarian: 31 (page, render and glossary lines and the four `read` lines that Retro took), but for the `read` line below.
- `estimate-case-build-goes-on-after-a-live-compaction` — waits for the first compaction of a `case-guppi` in a working session.
- `estimate-clean-branch-ships-neutral-texts` — waits for the librarian's run of session 2312: `guppi ship --allow-draft` into an empty folder, each sentence read whole.
- `estimate-sprint-plugin-ci-writes-a-clean-branch` — waits for the owner's push of `plugin` and a tag `prod-x.y.z`, before the close of `plugin`.

## Observations

- Red before the work, in `## Baseline` of `work.md`: `guppi check` exit 1 on the eleven core draft pages, the two `unread: failed` Estimates, `estimate-harness-make-runs-in-both-shells` (no Makefile target), and `backlog: vault/wiki/backlog.md differs from its sources`.
- The clean copy that `guppi ship --allow-draft` wrote holds `.github`, `.claude-plugin` and `skills/install`. One reading agent said it held no `.github`, which was wrong.
- `ask-guppi` at `/pre-spec` ran two Greps by content over `vault/wiki/estimates/` instead of reaching Estimates through the `estimates` field of a page, and gave no `## Problem` of `decision-case-793` though a finding named `rule-page-generation`. It reported both itself.
- A Python script run with `python -I` ignores `PYTHONIOENCODING` and prints in cp1252 on this machine. A script that prints transcript text needs `sys.stdout.reconfigure(encoding="utf-8")`.

## For the next session

- The doubtful sentences of the clean copy that the reading of `estimate-clean-branch-ships-neutral-texts` lists: `entity-guppi` naming `entity-guppi-repository`; `PLAIN_SPRINTS` with `migration` and `plugin` in `rule-ratification`; the `Makefile` and `guppi ship` in `rule-rules-schema`, `rule-entities-schema` and `rule-guppi-package`; and about ten `method`s that wait for "the new Render", "the session that changes it" or "the next session". Each needs the person's judgment, and a reading after this session's librarian may fail on one of them.
- The Criterion sentences of shipped Estimates that hold only in GUPPI, listed in the same reading, wait for a Case that rewrites them.

## Ask the person

- `estimate-guppi-package-is-ready-after-the-install` — needs the person — In an empty project on a machine with `uv`, after the librarian's render, does `/guppi:install` run `uv --version`, ask nothing about `uv`, build `.guppi/.venv/` by `uv sync` after the copy before it sends you to `/hi`, and do the hooks find that environment at the first `/hi`?
