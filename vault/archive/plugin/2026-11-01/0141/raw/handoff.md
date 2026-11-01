# Handoff — 2026-11-01, the bare link of a ledger line and the failed readings of Case building

## Notes from memory

- The person took every recommended answer of every round ("ok"), with no own alternative.
- The person put off C1, the clean branch (push of `plugin` and a tag `prod-x.y.z`), as `[-] … · sprint · defer`: a push is not undone by git, and the last commit of `plugin` still holds draft pages with `core: true`, so the CI run would write nothing to `prod`.
- C3 closed as work, the person agreeing: `guppi check` printed `backlog.md differs from its sources` in the Baseline of session 2307 because `put_off_count` of `.guppi/guppi/backlog.py` counts the `[-]` lines of the live session's own `frontier.md`; a copy of commit `cdfeb988` printed exit 0 without the Frontier of 2307 and exit 1 with it, the diff being the three counts the librarian of 2307 then wrote. The same line will stand in the Baseline of any session that puts off a backlog item before Work Mode.
- At pre-spec, ask-guppi gave 9 findings on Cases 977, 978, 979 and 981; all were fixed by their `case-guppi` and confirmed closed, a leftover "never" in the `context` of 981 fixed on the person's word; the four Cases were ratified again with the same ledger lines.
- The reading of `estimate-orchestration-names-related-cases-in-the-dispatch` rests on a judgment: Case 977 counts as related to every later item, since it changes how `check_bare_links` reads the prose of a plan. Under a narrower reading of "related" the dispatches of 980 and 981 would pass.

## Direct instructions to the librarian

- The `update` of `rule-ledger-write` (Case 977) sets `implementation_ref` whole, with `.guppi/guppi/lint.py` and `.guppi/tests/test_lint.py` added to the eight paths it held.
- Case 978 changes `lesson-ledger-reading-writes-a-bare-wikilink` in both the `root_cause` field and `## Root cause`: `[[slug]]` in a code span, nothing else.
- Cases 979, 980 and 981.2 carry `{supersedes:case 971}{supersedes:case 976}`: the defers of those Cases leave `deferred_by` of `estimate-case-build-reads-each-list-of-a-new-member`, `estimate-orchestration-names-related-cases-in-the-dispatch` and `estimate-orchestration-shows-the-built-case`.
- Two readings of this Retro on Estimates of `rule-case-build` are `failed` (`estimate-case-build-reads-the-link-graph-of-what-it-changes`, `estimate-case-build-reads-the-readers-of-a-changed-step`), and one on `rule-orchestration` (`estimate-orchestration-names-related-cases-in-the-dispatch`).

## What actually got done

- Cases ratified: 977, 978, 979, 980, 981 (981.1, 981.2).
- Code: `.guppi/guppi/pages.py` (`page_paths`), `.guppi/guppi/lint.py` (`body_links`, `link_names`, `unknown_links`; `check_refs` judges a body link by the names), `.guppi/guppi/prespec.py` (`known_slugs` removed; `check_bare_links` by `link_names` and `unknown_links`), `.guppi/guppi/ledger.py` (`refused_links`, `link_message`, a docstring paragraph), `.guppi/guppi/casecheck.py` (`DROPPED_LABEL`, `is_dropped`, `summary_after_text`, a docstring paragraph).
- Tests: `test_ledger.py` (8 `bare_link`), `test_lint.py` (6 `bare_link`, one parametrized test), `test_casecheck.py` (8 `summary_after_text`).
- `uv run --project .guppi guppi test`: 1856 passed, 6 skipped, 1 deselected at the Baseline; 1878 passed, 6 skipped, 1 deselected at Retro. `uv run --project .guppi guppi style`: clean.
- Readings: L1 `estimate-rules-schema-checked` passed (at `/hi`); at Retro `estimate-ledger-write-refuses-a-bare-link-to-no-page` passed, `estimate-case-check-sends-back-a-summary-after-text` passed, `estimate-orchestration-names-related-cases-in-the-dispatch` failed, `estimate-orchestration-shows-the-built-case` passed, `estimate-ask-searches-at-prespec` passed, `estimate-case-build-reads-the-link-graph-of-what-it-changes` failed, `estimate-case-build-reads-the-readers-of-a-changed-step` failed.
- Lesson: `lesson-orchestration-closes-a-frontier-line-by-its-closer-alone` (error).

## Debt

- No box of code, test or command is unticked.
- 15 boxes wait for the librarian: the page lines, the render line of `.claude/agents/case-guppi.md` and the `read` lines of the Estimates read at Retro.
- `estimate-sprint-plugin-lesson-root-cause-holds-no-bare-link` — `pending`; waits for the librarian's run that applies the `update` of `lesson-ledger-reading-writes-a-bare-wikilink`.
- `estimate-case-build-reads-each-list-of-a-new-member` — `pending`; waits for the first build of `case-guppi` in a later session whose Case adds a member to a list.
- `estimate-sprint-plugin-ci-writes-a-clean-branch` — `pending`; waits for the push of `plugin` and a tag `prod-x.y.z`, put off this session.

## Observations

- Red before the work, in the Baseline of `work.md`: `guppi check` 15 lines, among them the `ref` finding on `lesson-ledger-reading-writes-a-bare-wikilink` that Case 978 fixes, and the three `unread: failed` lines of the Estimates Cases 979, 980 and 981.2 set back to `pending`.
- The ledger hook of Case 977 is code, not a render, so it is live from this session on: a reading or a lesson line with a bare link to no page is refused now.
- The three Work readings of the Estimates of `rule-ask` and `rule-case-build` were taken in Work Mode from the subagent transcripts of session 2307, as their `method` names; `/hi` reads no transcript of an earlier session.
- `.guppi/links.md` prints a block of up to 96 lines for `rule-case-build`; a Grep with `-A 40` prints part of it, as in the build of Case 974 of session 2307.

## For the next session

- `estimate-case-build-reads-the-link-graph-of-what-it-changes` failed: `case-guppi` greps the block of some of the pages and files it changes but not each one, and no `context` says that a page it creates has no block. What changes in `rule-case-build`, or whether the Criterion is too strict for a created page.
- `estimate-case-build-reads-the-readers-of-a-changed-step` failed: Case 972 of session 2307 missed the kept-method path of the wait check, which does the same step.
- `estimate-orchestration-names-related-cases-in-the-dispatch` failed again: the main agent named a related Case by its pages without its path. Whether the rule needs a guard, or whether a Case that only changes how pre-spec reads a link counts as related.
- C1, the clean branch: push `plugin` and a tag `prod-x.y.z`, and read the CI run.
- Whether `backlog --check` should leave out the Frontier of the live session, so the Baseline does not show `backlog.md differs from its sources` after a put-off; closed as work this session, with no change.

## Ask the person
