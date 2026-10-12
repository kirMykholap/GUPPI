---
type: estimate
kind: QA
status: passed
target: "[[rule-case-build]]"
purpose: Whether case-guppi, on an item that reports a defect, judges each option of its round against the rule the defect breaks over the whole text the option leaves, and names in the After line of an option the part it leaves breaking the rule, without recommending it
method: "by hand at the Retro of this session: the new Render of rule-case-build in raw/<date>/<hi HHMM>/spec.md read against the Criterion, recorded in the estimate line"
origin: raw/2026-10-12/1604/ledger.md#case-780
sprint: plugin
created: 2026-10-12
tags: [session, workflow, harness]
---

## Criterion

When:
`case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case on a Frontier item that reports a defect: a text that breaks a rule.

Then:
Before it writes its round, it finds the rule the defect breaks and reads the passage of that rule.
**＋** It judges each option of the round against that rule over the whole text the option leaves; for a Criterion, each line of its `When` and `Then` and its `method`, not only the words the item quotes.
**＋** An option that leaves a part of that text breaking the rule may stand in the round; its `**After:**` line names that part, and `case-guppi` does not recommend that option.
**－** The `**After:**` line keeps the form of `.claude/skills/grill-me/SKILL.md`: the part left is a plain sentence inside its text.

## Result

2026-10-12, by hand at the Retro of session 1604: the new Render of rule-case-build in raw/2026-10-12/1604/spec.md (Case 780, the replace pair after "what is left not done.") read against the Criterion — it tells case-guppi, on an item that reports a defect, to find the rule it breaks and read its passage, to judge each option over the whole text it leaves (each When and Then line and the method of a Criterion), and to name in the After line, in a plain sentence, the part an option leaves breaking the rule and not recommend it.

## History

- 2026-10-12 created · [[decision-case-780]]
- 2026-10-12 status: pending → passed · raw/2026-10-12/1604/ledger.md#L20
