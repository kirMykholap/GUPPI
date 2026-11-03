---
type: estimate
kind: QA
status: passed
target: "[[rule-orchestration]]"
purpose: Whether the list of the rounds of a batch marks where each Case's round begins by a horizontal rule, by its Context label, which names the Case and its item, and by its question numbers, with no heading of the main agent's own, and whether the Cases of a batch shown for one ratification stand apart by a horizontal rule
method: "by hand: the Render of rule-orchestration in vault/wiki/orchestration.md read against the Criterion, recorded in the estimate line"
checked: 2026-10-09
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow]
core: true
---

## Criterion

When:
In Plan Mode before `/pre-spec`, the main agent shows in one list the rounds of `case-guppi` that came back for a batch of Cases, or shows every Case of a batch in one reply for one ratification, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

Then:
The `**Context:**` paragraph of each first round on an item opens with a label that names its Case id and its item of `raw/<date>/<hi HHMM>/frontier.md`, translated, such as `**Context — Case 7 (C2):**`.
**＋** A later round, which has no Context paragraph, is marked by its question numbers `<Case id>.Q<n>`.
**＋** One horizontal rule stands between the last question of one Case and the round of the next Case: the rule after one reply of `case-guppi` is the rule before the next.
**＋** One horizontal rule stands between the showings of two Cases of the batch in the reply that shows them for one ratification: the rule after one showing is the rule before the next.
**＋** No heading, and no line of the main agent's own other than a horizontal rule, stands before a round to mark where it begins: a rule stands before the first round of the list, and one rule between two rounds.
**－** A round shown alone, outside a batch, keeps its `**Context:**` label as `case-guppi` gave it, translated.

## Result

2026-10-09, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
