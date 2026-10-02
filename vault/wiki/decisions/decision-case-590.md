---
type: decision
case: "590"
status: current
children: ["[[decision-case-590.2]]", "[[decision-case-590.3]]"]
origin: raw/2026-10-02/1202/ledger.md#case-590
sprint: migration
created: 2026-10-02
tags: [session, hooks, harness, ledger, workflow]
---

## Problem

The person's message in a transcript is tested in three places in three ways. That breaks `rule-one-judgment-one-implementation`, and it already gives two answers on one record. The question was whether the turn and the stretch are one judgment, how they come to agree, whether the token counter joins, how the record is classified, where the decision is recorded and how it is checked.

## Recommend

- **How should the two hooks agree on the person's message?**
  - Recommended: (a) one shared function in `guppi/ledger.py` that names the kind of a user record. The Case check starts its turn at the person's message or a returned answer, and the ledger hook and `guppi/onward.py` start at the person's message only.
  - Answer: Agreed with the recommendations: (a).
- **Does the token counter join the shared function?**
  - Recommended: (a) yes. `guppi/context.py` uses the shared function with the turn boundary, and `is_prompt` is removed.
  - Answer: Agreed with the recommendations: (a).
- **Where is the decision recorded?**
  - Recommended: (a) delete the placeholder, which retires its defer, and record the decision in the docstrings and the How it works of the existing rule pages.
  - Answer: Agreed with the recommendations: (a).
- **Which test says that a line is the person's message?**
  - Recommended: (a) the source label: `origin.kind` `human` is the person's message, and `task-notification` is a returned answer.
  - Answer: Agreed with the recommendations: (a).
- **How is it checked that the fix is done?**
  - Recommended: (a) a new Estimate for the shared test under `rule-ledger-write`, and the Criterion of `estimate-context-size-shown-after-each-reply` rewritten, in two sub-cases.
  - Answer: Agreed with the recommendations: (a).
- **Is the Criterion of the round check rewritten too?**
  - Recommended: (a) a third sub-case replaces the Criterion of `estimate-case-check-refuses-text-before-a-round` whole. Its first line names the turn by the shared function, and every other line is carried word for word.
  - Answer: (a).
- **Change**
  - Asked: at `/pre-spec`, the person chose that `## How it works` leaves the Leaf pages this Case touches, as the schema of rule pages asks. What still holds moves into the docstrings of the modules, and Work Mode removes the section by hand as a one-off task. Case 589 takes the section of `rule-case-check`.
  - Taken: the How-it-works sentences of `rule-ledger-write` and `rule-context-size` are dropped. Each `update` carries only its History line, and a one-off task removes the section and moves what holds into `guppi/ledger.py` and `guppi/context.py`. The `update` of `rule-case-check` is dropped, and 590.1 names the case file of 589.

## History

- 2026-10-02 created · raw/2026-10-02/1202/ledger.md#case-590
- 2026-10-02 child decision-case-590.1 archived · cleanup
