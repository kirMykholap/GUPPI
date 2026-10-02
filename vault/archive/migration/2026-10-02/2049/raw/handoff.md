# Handoff — 2026-10-02, the onward hook after a ledger refusal, joint ratification

## Notes from memory

- Case 598: in its first round the person chose to hold every ratification for a batch, then in the next round narrowed it in their own words: Frontier items one at a time, each ratified after discussion; Cases handled side by side (after the findings of /pre-spec, or when a new Case shows a ratified one must change) always wait and go out together. The Case holds the narrower rule; the first answer is recorded in its `recommend` as replaced.
- The person asked why 596 and 597 were ratified in separate replies; that question became Case 598.
- The person asked whether an Estimate becomes `pending` when a Case only names it or changes only its History. The main agent answered no, from `lift_criterion` of `guppi/materialize.py` (only a `create`, a Criterion written whole or an explicit `set.status` sets `pending`) and `rename`/`reword` of `guppi/generate.py`; the person accepted that nothing needs fixing. No test covers `rename` leaving the status alone.
- Case 597's round found that a line of ratified 596.1 (`--plan` keeps `stop_hook_active`) would turn false; 596 was rebuilt and ratified again before 597 was shown. The /pre-spec findings then rebuilt 596 (with a new sub-case 596.3), 597, 598 and 600, ratified together.
- 599 and 600 close two Insights by naming the decision that wrote the rule (`decision-case-561.13`, `decision-case-561.1`), not the closing Case.

## Direct instructions to the librarian

- `rule-prespec-onward` is updated by 597.1 (two `replace` pairs) and 597.2 (one `replace` pair and `set.implementation_ref`); the anchors do not overlap. 597.2 carries `{supersedes:case 575}`, which retires the `deferred_by` of `rule-prespec-onward`.
- `rule-orchestration` is updated by 598.1 (three pairs) and 598.2 (one pair) in one paragraph of `## Showing and signing a Case`, at anchors that do not overlap: 598.2's old text ends `one Frontier;`, 598.1's third old text is the sentence ending `(case 355.2).` after it. Render `orchestration.md` once after both.
- `rule-retro-onward` gets `set.implementation_ref` from 596.1; `rule-retro` and `.claude/skills/retro/SKILL.md` change by 596.2.
- 596.1, 596.2 (first lines) were ratified three times and 597, 598, 600 twice; the ledger holds each decision line once. The decision lines of 596.2 for `estimate-retro-runs-on-to-the-handoff` and of 596.3 stand only at the last ratification.
- 599 and 600 set two Insights `actioned`; their four `clustered` lessons go to the archive by the cascade. With the defer of 575 retired, `backlog.md` should drop from 24 to 21 items.
- The two lessons of this session are both about hooks that judge a reply: `lesson-case-check-question-line-without-colon-unseen` and `lesson-prespec-onward-re-ratification-out-after-its-stretch`. The second has the cause case 575 deferred and 597.2 only narrowed; check it against `insight-*` lines on the onward hook before clustering.
- Two `failed` readings, `estimate-skill-grill-me-asks-in-rounds` and `estimate-orchestration-shows-the-built-case`, rest on the one question line without its colon in the round on Case 599.

## What actually got done

- Cases ratified: 596 (596.1, 596.2, 596.3), 597 (597.1, 597.2), 598 (598.1, 598.2, 598.3), 599, 600.
- Code: `guppi/ledger.py` (`stretch` and `refusals`, `own_refusals` kept on top of them), `guppi/onward.py` (`spent`, `told` per command, `stretch_replies`, `last_decisions` over the replies of the stretch, the `--plan` run guarded by `spent`). Tests: `tests/test_ledger.py` (one test), `tests/test_onward.py` (twelve tests, thirteen cases, one test renamed).
- `make test`: 1088 passed, 6 skipped. `make style`: clean.
- Readings: ledger lines 1–7 (at /hi), 22–24, 28–30. Lessons: ledger lines 25 and 31.

## Debt

None: every box of code, test and command of the Spec is ticked.

- Boxes that wait for the librarian: 19.
- `read` lines whose slug this session creates or updates: `estimate-retro-onward-sends-the-agent-to-the-handoff`, `estimate-retro-runs-on-to-the-handoff`, `estimate-retro-onward-exits-2-on-an-error`, `estimate-prespec-onward-sends-the-agent-on`, `estimate-prespec-onward-reads-the-decisions-of-the-stretch`, `estimate-orchestration-signs-a-batch-together`, `estimate-orchestration-acknowledging-reply`, `estimate-prespec-gathers-the-answers-after-findings`.

## Observations

- Red before the work: `make lint` exit 2 at the Baseline, 54 lines of `guppi lint` (5 `deferred`, 49 `unread: pending`), as `work.md` holds them. No expected red.
- The unticked box of `raw/2026-10-02/1202/spec.md` line 930 was read again at /hi (`make lint` printed no `fence` line) and stays unticked: no step of /hi or of the librarian ticks a box of another session's Spec, so the brief carries it each time.
- The harness marked the answers of `case-guppi` and of `ask-guppi` as instruction-shaped (pattern `settings-json`) at each answer whose text named `.claude/settings.json`.
- Readings left open, their moment not come: `estimate-case-build-writes-the-case` (no `create` without a `ref`), `estimate-orchestration-defers-in-one-reply` (no short-form defer), `estimate-orchestration-forwards-a-discussion-question` (no such question), `estimate-orchestration-asks-in-the-grill-me-shape` (no question of the main agent's own outside the forms it exempts), `estimate-ratification-ledger-line-form`, `estimate-spec-capture-offers-the-fork` (no session took a conserved Spec), `estimate-ask-finds`, `estimate-carry-over-writes`, `estimate-case-check-refuses-text-before-a-round` and `estimate-case-check-requires-each-question-of-the-rounds` (no round after /pre-spec, no refusal), `estimate-compact-recall-reloads`, `estimate-end-of-work-order` and `estimate-handoff-dispatches` and `estimate-handoff-holds-each-fact-once` (read after this run), `estimate-event-log-records`, `estimate-generate-rewords`, `estimate-hi-takes-a-conserved-spec`, `estimate-ledger-write-lifts`, `estimate-lint-runs-every-step` (no red backlog step at the Baseline), `estimate-plan-mode-verified`, `estimate-retro-loads`, `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note`, `estimate-session-start-context`, `estimate-spec-box-runs-a-conserved-spec`, `estimate-spec-write-reaches-the-approved-spec`, `estimate-synthesis-clusters`, `estimate-where-to-stop-stops-only-on-its-conditions`, `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`, `estimate-work-mode-takes-the-work-readings` and the three of `entity-sprint-migration`.

## For the next session

- The close of the sprint (Slice 5), left on the sprint page again.
- Whether `guppi onward --plan` should count a re-ratification across the whole session, not only within its stretch, so that a Case ratified again with unchanged lines is not out for the rest of the session.
- Whether the round check of `rule-case-check` should refuse a question line that opens `❓ **Qn** - **…**` without the colon, instead of passing it as no question.
- Who ticks a `by hand` box of an earlier session's Spec that a later /hi reads, or whether such a box should leave the brief.

## Ask the person
