---
type: decision
case: "601"
status: current
children: ["[[decision-case-601.1]]", "[[decision-case-601.2]]", "[[decision-case-601.3]]", "[[decision-case-601.4]]", "[[decision-case-601.5]]"]
origin: raw/2026-10-02/2300/ledger.md#case-601
sprint: migration
created: 2026-10-02
tags: [hooks, harness, workflow, session]
---

## Problem

No script reads the form of a round of `case-guppi`. A question whose title line lacks the colon is no question to the checks that look for questions. A round out of the grill-me form reaches the main agent and the person, and is found only by a hand reading after the session.

## Recommend

- **Where should a question title line without the colon be caught?**
  - Recommended: (a) send the round back to `case-guppi`. The `SubagentStop` check also reads an answer that holds no Case and does not open with `**Fact:**`. A line in it that opens with the question mark but is not a full title line sends it back, and the reason names the line. A round sent back once and returned with the same text is not sent back again.
  - Answer: agreed with the recommendation, (a).
- **How much of each question should the new catch read?**
  - Recommended: (a) the title line only. The rest of each question's form stays with the hand reading of `estimate-skill-grill-me-asks-in-rounds`.
  - Answer: (b) the title line and the fixed labels. Each question needs one `**Now:**` line, the `**Options:**` label alone on its line, at least one option marked with the diamond and with an `**After:**` item, and an arrow line.
- **Should the main agent's showing of a round get a check of its own?**
  - Recommended: (a) no. The answer is checked before the main agent sees it, and `estimate-orchestration-shows-the-built-case` keeps reading the showing by hand.
  - Answer: agreed with the recommendation, (a).
- **What should happen to the two failed readings?**
  - Recommended: (a) leave them failed and read them again in a later session, once the new catch is live. Their Criteria stay as they are.
  - Answer: agreed with the recommendation, (a).
- **How should done be checked for the new catch?**
  - Recommended: (a) a new Estimate for the round, `estimate-case-check-sends-back-a-faulty-round`, and the Criterion of `estimate-case-check-sends-back-a-faulty-case` replaced so that its last line no longer says that an answer without a Case heading goes unchecked. That makes two sub-cases.
  - Answer: agreed with the recommendation, (a).
- **Should the two checks that already find questions also see a title line without the colon?**
  - Recommended: (a) keep them as they are. Both keep the full title line, and their Estimates stay untouched.
  - Answer: agreed with the recommendation, (a). Replaced in part by the two questions below, after pre-spec showed that the new check and `is_round` cannot share one test as written.
- **How should the catch know a round was already sent back?**
  - Recommended: (a) from the agent's own transcript. A faulty round is not sent back when an earlier output in the transcript holds the same text. Nothing is stored, and the check runs with or without a plan file.
  - Answer: agreed with the recommendation, (a).
- **Which single test should decide that an answer is a round?**
  - Recommended: (a) one test, by the question mark at the start of a line. One function decides that an answer is a round: no Case, no `**Fact:**` opening, and a line that opens with the question mark. The new check and the end-of-reply check both import it, and the pass condition of `estimate-case-check-refuses-text-before-a-round` is rewritten in one more sub-case.
  - Answer: agreed with the recommendation, (a).
- **Which rounds should give the titles that the Case's `recommend` must hold?**
  - Recommended: (a) only rounds the new check finds in form. A round sent back gives no titles, and the pass condition of `estimate-case-check-requires-each-question-of-the-rounds` is rewritten in one more sub-case.
  - Answer: agreed with the recommendation, (a).

## History

- 2026-10-03 created · raw/2026-10-02/2300/ledger.md#case-601
