---
type: estimate
kind: QA
status: passed
target: "[[rule-case-build]]"
purpose: Whether case-guppi, on every item, finds the rule that governs what each option of its round changes, the rule a defect breaks where the item reports one, judges each option against it over the whole text the option leaves, names in the After line of an option the part it leaves breaking the rule without recommending it, and names that rule in context
method: "by hand: the Render of rule-case-build in .claude/agents/case-guppi.md read against the Criterion, recorded in the estimate line"
checked: 2026-10-13
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow, harness]
core: true
---

## Criterion

When:
`case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case on a Frontier item and writes a round with options.

Then:
Before it recommends an option, it finds the rule that governs what each option changes, or the rule the defect breaks where the item reports a defect, and reads the passage of that rule, which it names in the `context`.
**＋** It judges each option of the round against that rule over the whole text the option leaves; for a Criterion, each line of its `When` and `Then` and its `method`, not only the words the item quotes.
**＋** An option that breaks that rule, or leaves a part of that text breaking it, may stand in the round; its `**After:**` line names that part, and `case-guppi` does not recommend that option.
**－** The `**After:**` line keeps the form of `.claude/skills/grill-me/SKILL.md`: the part left is a plain sentence inside its text.

## Result

2026-10-13, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
