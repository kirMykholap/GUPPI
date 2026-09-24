---
type: insight
pattern: The Case schema does not say how the scripts read the text a Case writes — which forms they resolve, how far an edit pair reaches — so the agent writes a form the scripts do not handle, and only the pre-spec check finds it.
status: actioned
children: ["[[lesson-sub-case-given-the-parents-plus-lines-has-no-form]]", "[[lesson-generate-replace-anchor-stays-in-one-section]]"]
severity: 0
addressed_by: "[[decision-case-383]]"
origin: raw/2026-09-23/1355/ledger.md#L36
sprint: migration
created: 2026-09-23
tags: [harness, session, workflow]
---

## Pattern

The Case schema does not say how the scripts read the text a Case writes — which forms they resolve, how far an edit pair reaches — so the agent writes a form the scripts do not handle, and only the pre-spec check finds it. In session 1853 of 2026-09-21 the four sub-cases of 299 wrote `given` as "The parent's." plus their own lines, a pointer materialize does not resolve; the schema gives a sub-case two forms of given and says nothing of a third (`lesson-sub-case-given-the-parents-plus-lines-has-no-form`). In session 1355 of 2026-09-23 the first pair of Case 381 opened its `old` with a section heading; generate applies a replace pair inside one section, and the schema does not say so (`lesson-generate-replace-anchor-stays-in-one-section`). Both were caught by pre-spec, not by the text the agent wrote from.

## Proposal

A suggestion, not a decision: the Case schema of `rule-case-protocol` could state, beside each form a Case writes, the limit the scripts put on it — a replace pair acts inside one section of a page, a sub-case's given is its own or none — so the limit is read before the Case is written, not learned from the check.

## History

- 2026-09-23 created · raw/2026-09-23/1355/ledger.md#L36
- 2026-09-24 updated: actioned: the Case schema names, beside each form, the limit the scripts put on it — a replace pair inside one section, a sub-case's given taken as it stands (case 383) · [[decision-case-383]]
