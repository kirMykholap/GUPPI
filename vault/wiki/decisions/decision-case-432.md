---
type: decision
case: "432"
status: current
update: ["[[rule-prespec]]", "[[estimate-prespec-requires-a-task-line]]", "[[insight-workflow-case-schema-silent-on-what-the-scripts-accept]]"]
origin: raw/2026-09-25/1654/ledger.md#case-432
sprint: migration
created: 2026-09-25
tags: [session, workflow, harness]
---

## Context

The Insight `insight-workflow-case-schema-silent-on-what-the-scripts-accept` describes this mechanism. The Case schema does not say how the scripts read the text of a Case. The agent writes a form the scripts do not accept, and only pre-spec finds it. Case 383 first closed the Insight: the schema named the limits for a `replace` pair and for the `given` of a sub-case. Then `addressed_by` went to `decision-case-393`. The librarian of session 1228 added the lessons `lesson-prespec-read-line-of-a-renamed-estimate` and `lesson-prespec-wikilink-to-a-decision-page-not-yet-written` to the Insight, and the Insight became `open` again. The `Stop` hook found both faults after the ratification. The `SubagentStop` hook did not run yet then.
Case 419 changed the place where such a form is found. `case-guppi` builds each Case. `guppi casecheck --subagent` builds a Spec in memory from its answer and runs `judge` of `guppi/prespec.py` on it. `judge` is the same checks as at pre-spec. When there is a finding, the agent is sent back, and the person does not see that Case. `judge` holds `check_bare_links` and `check_tasks`. So the part "only pre-spec finds it" of the Insight is no longer true. `check_bare_links` refuses a link `[[decision-case-N]]` to a decision page that does not exist yet before the showing. A working form already exists: the slug without brackets under `set`. Case 419.3 wrote it so, and the link appeared on the page of `insight-case-form-chat-form-read-by-no-script`.
The lesson on the rename has another cause: two scripts decide in different ways which slug stands on a read line. `estimates_to_read` takes the slug of the `then` item, that is the old slug. The ticker `tick_read` in `guppi/generate.py` ticks a line by the slug of the reading entry. After `generate` the page lives under the new slug, and the reading names the new slug. The check before the showing makes `case-guppi` write the old slug, and the ticker never ticks such a line. That happened in the Spec of session 1228: no reading of W1 and W2 ticks the read lines of `estimate-case-protocol-checks-its-frame` and `estimate-frame-check-finds-a-contradiction`. So the early check does not close this lesson: it asks for the wrong form.
The proposal of the Insight is to write the limit beside each form in the schema. That is a second copy of a judgment that already stands in `judge`. By the rule "one judgment, one implementation" such a copy is a defect from its first day.
The frame check showed the following. The Render of `rule-prespec` describes the read line in one place, and the Case adds one `replace` pair there. The Criterion of `estimate-prespec-requires-a-task-line` speaks exactly of the read line, so the Criterion is replaced whole by the `when` and `then` of this Case. The Criterion of `estimate-generate-ticks-the-spec` speaks of the ticker, and the ticker does not change. The Criterion of `estimate-case-check-sends-back-a-faulty-case` speaks of the findings of `judge` in general. The Criterion of `estimate-prespec-checks-the-plan` speaks of the session, the window and the parse of lines. None of them is touched. `vault/wiki/case-schema.md` asks for a read line for an Estimate "by its slug". After this Case that is the new slug, so the phrase stays true, and no Estimate of `rule-case-protocol` is touched. There is no `create` in the Case, so no vault query is due.
What the Case does not do. It does not write the limits of the scripts into the schema. It changes neither `check_bare_links` nor the ticker.

## Problem

The Insight is `open` again and must be closed: actioned, rejected, or its proposal taken as it stands. The pattern "only pre-spec finds the form" is no longer true after Case 419. But one of the new lessons shows that the check before the showing asks, for a renamed Estimate, for a read line the ticker does not tick.

## Given

`rule-prespec` and its render `.claude/skills/pre-spec/SKILL.md` — its Render names the task line of a reading
**＋** `estimate-prespec-requires-a-task-line` — the promise that each Estimate to read has a read line of its own
**＋** `guppi/prespec.py` — `estimates_to_read` and `check_tasks`, run by `judge`
**＋** `tests/test_prespec.py` — the tests of the task line
**＋** `guppi/generate.py` — `tick_read`, which ticks a read line by the slug of a reading
**＋** `insight-workflow-case-schema-silent-on-what-the-scripts-accept` — the Insight this Case actions
**＋** `raw/2026-09-25/1228/spec.md` — the Spec of session 1228, which holds read lines of renamed Estimates

## History

- 2026-09-25 created · raw/2026-09-25/1654/ledger.md#case-432
