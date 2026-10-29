---
type: insight
pattern: case-guppi changes what a step or a line does from the one step in front of it and does not read the other steps that read or repeat what it changes — the next step of the Render, the other skill that does the same step, the new path its own Case adds — so the change holds for the step it looked at only and /pre-spec finds the rest after the person ratified the Case
status: open
children: ["[[lesson-case-build-claims-a-page-stands-without-reading-the-path-it-changes]]", "[[lesson-case-build-changes-a-step-without-reading-what-reads-it]]"]
severity: 2
origin: raw/2026-10-29/1930/ledger.md#L26
sprint: plugin
created: 2026-10-29
tags: [case-build, prespec]
---

## Pattern

Two lessons share one cause. In Case 851 case-guppi claimed that the readers of the `Branch:` line stand, judging them by the old path alone, while its own Case added a new path on which the line read `none: …`. In Cases 903.2 and 905 it named only /box as the step that shows the librarian's report though /handoff shows it too, and left step 5 of the Render of rule-plugin-install checking a file that its new step 4 no longer copies. Each time the change was written from the step in front of it, and the steps that read or repeat its output were not read; /pre-spec found the fault after the person had ratified the Case.

## Proposal

A suggestion: when a Case changes what a step writes, copies or shows, case-guppi lists the steps and skills that read that output or do the same step — by a Grep of the step's output or of its name — and reads each before it writes the summary, naming them in `context`.

## History

- 2026-10-29 created · raw/2026-10-29/1930/ledger.md#L26
