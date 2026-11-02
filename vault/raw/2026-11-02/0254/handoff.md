# Handoff — 2026-11-02, rule-morph off core until built

## Notes from memory

- The person typed `/hi` twice outside plan mode from the phone app and saw no refusal. The person added an item to show the refusal in the chat; Case 1000 was built, and after the round showed that a blocked prompt never reaches the agent, the person dropped it: the refusal stays as it is. Lesson L9 records the fact.
- On Case 1001 the person first wanted `rule-skill-approve-spec` cleared by the CLI trial in this session's Work Mode. Work Mode does not stop for a reading by hand without a `stop:` task, so the trial was left to the person, outside this session; it did not happen in this session.
- `/pre-spec` widened Case 1001 by two pages, `rule-permissions` and `rule-guppi-config`, on the person's word. `case-guppi` noted that the rewording of their Purposes is checked by another Estimate than the rest of the Case and could have been a sub-case; it stayed one Case.

## Direct instructions to the librarian

- Case 1001 sets `core: null` on `rule-morph`. Check that the page carries no `core:` line after `generate`, as `rule-skill-merge-main` and `rule-skill-pr-review` carry none after case 822.8.
- Check that each `replace` of Case 1001 found its `old` once: in Work Mode a Grep found each of the four `old` texts once, in `entity-sprint-plugin`, `rule-permissions` and `rule-guppi-config` (two in the last).
- After the run, `guppi check` should print one line fewer: no `status: a page with core: true that is draft` on `rule-morph`; the line on `rule-skill-approve-spec` stays.

## What actually got done

- Case ratified: 1001 (ledger L1–L3, L6–L7). Case 1000 was built and dropped before ratification; it has no ledger line.
- Code and tests: none changed.
- `uv run --project .guppi guppi test`: 1891 passed, 6 skipped, 1 deselected. `uv run --project .guppi guppi style`: clean.
- Readings: L4 `estimate-orchestration-acknowledging-reply` `failed`; the Work reading of `estimate-close-reports-the-run` `passed`, in the block that ends Retro. Lessons: L5 `lesson-orchestration-acknowledging-reply-leaves-the-frontier-heading-untranslated` (error); `lesson-hook-block-reason-is-not-shown-in-the-phone-app` (knowledge), in the block that ends Retro.

## Debt

- No box is debt.
- 6 boxes wait for the librarian: the five page lines of Case 1001 and its `guppi sprint` line.
- `estimate-clean-branch-refuses-a-draft-core-page` — waits for the librarian's run that applies the update of `rule-morph`: its Grep of `^core:` in the three pages. The pytest part of its `method` passed in Retro: 16 passed, 164 deselected.
- `estimate-sprint-plugin-ci-writes-a-clean-branch` — the live sprint page; waits for the tag `prod-x.y.z` and its CI run, which wait for `rule-skill-approve-spec` to be `built`.

## Observations

- The lint lines on `rule-morph` and `rule-skill-approve-spec` were red before the work (`## Baseline` of `work.md`).
- The title line of the plan, and so of `spec.md`, names the dropped Case 1000: "a refused /hi tells the person in the chat to turn plan mode on". The agent writes the title line before the first `guppi caseid`, from the first item taken, and may not edit it after; the Spec holds only Case 1001.
- `estimate-orchestration-acknowledging-reply` failed on the agent's own reply: the heading `## Frontier` stood in English. The rule is clear; the cause is in L5.

## For the next session

- `estimate-orchestration-acknowledging-reply` is `failed`: whether the rule needs a change, or only a new reading once the agent keeps the heading translated.
- With `rule-morph` off `core`, the only page that blocks the clean build is `rule-skill-approve-spec`; its CLI trial is the way to the tag `prod-x.y.z`.

## Ask the person

- `estimate-skill-approve-spec-takes-the-spec` — needs the person — on a copy of the repository, in the Claude Code CLI in a standalone terminal: does `/approve-spec`, typed after Esc and Shift+Tab, append the plan to `spec.md`, and is it blocked when typed in Plan Mode?
- `estimate-orchestration-names-the-typed-approval` — needs the person — in the same CLI trial: does the reply that calls `ExitPlanMode` hold, before the call, the conditional line on Esc, Shift+Tab and `/approve-spec`?
- `estimate-spec-box-runs-a-conserved-spec` — needs the person — on a copy of the repository, one session saves a small Spec by `/carry` and a second runs it by `/box`: does it come out as the Criterion says?
