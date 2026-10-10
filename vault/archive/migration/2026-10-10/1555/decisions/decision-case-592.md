---
type: decision
case: "592"
status: archived
create: ["[[estimate-ledger-write-names-the-kind-of-a-user-record]]"]
update: ["[[rule-ledger-write]]"]
delete: ["[[rule-turn-start-one-judgment]]"]
supersedes: ["[[decision-case-590.1]]", "[[decision-case-586]]"]
origin: raw/2026-10-02/1202/ledger.md#case-592
sprint: migration
created: 2026-10-02
tags: [session, hooks, harness, ledger]
---

## Problem

A ledger line of the first ratification of 590.1 has no item in the plan, so the exit from Plan Mode is refused, and only a supersede retires it. The question answered is how 590.1 stays in force without that line: re-issued whole under a new id that supersedes it.

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
  - Asked: at `/pre-spec`, the person chose that `## How it works` leaves the Leaf pages this Case touches. What still holds moves into the docstrings of the modules, and Work Mode removes the section by hand as a one-off task. Case 589 takes the section of `rule-case-check`.
  - Taken: the update of `rule-ledger-write` carries only its History line, a one-off task removes the section, and the update of `rule-case-check` is dropped.
- **Change**
  - Asked: the person refused a hand edit of the ledger, and chose to re-issue 590.1 as Case 592 with `{supersedes:case 590.1}`, with the same content.
  - Taken: this Case holds the `given`, `when`, `then` and `tasks` of 590.1 as last ratified, each decision line carries `{supersedes:case 590.1}`, and the delete line keeps `{supersedes:case 586}`.

## History

- 2026-10-02 created · raw/2026-10-02/1202/ledger.md#case-592
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
