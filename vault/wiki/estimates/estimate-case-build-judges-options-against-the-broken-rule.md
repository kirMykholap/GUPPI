---
type: estimate
kind: QA
status: passed
target: "[[rule-case-build]]"
purpose: Whether case-guppi, on every item, finds the rule that governs what each option of its round changes, the rule a defect breaks where the item reports one, judges each option against it over the whole text the option leaves, names in the After line of an option the part it leaves breaking the rule without recommending it, and names that rule in context
method: "by hand at the Retro of this session: the new Render of rule-case-build in raw/<date>/<hi HHMM>/spec.md read against the Criterion, recorded in the estimate line"
checked: 2026-10-13
origin: raw/2026-10-12/1604/ledger.md#case-780
sprint: plugin
created: 2026-10-12
tags: [session, workflow, harness]
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

2026-10-13, Retro of session 1426, the new Render sentence of rule-case-build in raw/2026-10-13/1426/spec.md (case 798.1) read against the Criterion: on every item it finds the rule that governs what each option changes, or the rule a defect breaks, reads its passage and names it in context; judges each option over the whole text it leaves, each line of a Criterion's When, Then and method; an option that breaks the rule may stand, its After line names the part in a plain sentence, and it is not recommended; the old text of the replace stands once on the page

## History

- 2026-10-12 created · [[decision-case-780]]
- 2026-10-12 status: pending → passed · raw/2026-10-12/1604/ledger.md#L20
- 2026-10-13 updated: the Criterion and purpose replaced whole — the rule that governs what an option changes is read on every item, not only on an item that reports a defect (case 798.1) · [[decision-case-798.1]]
- 2026-10-13 status: pending → passed · raw/2026-10-13/1426/ledger.md#L27
