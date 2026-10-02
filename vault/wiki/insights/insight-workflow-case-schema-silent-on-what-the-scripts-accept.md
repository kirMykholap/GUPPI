---
type: insight
pattern: The Case schema does not say how the scripts read the text a Case writes — which forms they resolve, how far an edit pair reaches — so the agent writes a form the scripts do not handle, and only the pre-spec check finds it.
status: open
children: ["[[lesson-sub-case-given-the-parents-plus-lines-has-no-form]]", "[[lesson-generate-replace-anchor-stays-in-one-section]]", "[[lesson-spec-write-sub-point-opening-with-a-code-span-unpadded]]", "[[lesson-prespec-read-line-of-a-renamed-estimate]]", "[[lesson-prespec-wikilink-to-a-decision-page-not-yet-written]]", "[[lesson-case-build-closes-a-sprint-item-without-the-sprint-page]]", "[[lesson-case-build-splits-a-case-whose-line-stands]]", "[[lesson-case-showing-ratification-fence-outside-the-blockquote]]"]
severity: 3
addressed_by: "[[decision-case-432]]"
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
- 2026-09-24 updated: lesson-spec-write-sub-point-opening-with-a-code-span-unpadded added to children by the librarian's synthesis; addressed_by moves to decision-case-393 (later than 383), status kept · raw/2026-09-24/1303/ledger.md#L15
- 2026-09-25 updated: reopened: children lesson-prespec-read-line-of-a-renamed-estimate and lesson-prespec-wikilink-to-a-decision-page-not-yet-written added · raw/2026-09-25/1228/ledger.md#L16
- 2026-09-25 updated: actioned: a form the scripts refuse is found by judge on SubagentStop before the Case is shown (case 419.3); a renamed Estimate is read under its new slug (case 432); the limits are not copied into the Case schema · [[decision-case-432]]
- 2026-09-29 updated: children lesson-case-build-closes-a-sprint-item-without-the-sprint-page and lesson-case-build-splits-a-case-whose-line-stands added, reopened (synthesis) · raw/2026-09-29/1432/ledger.md#L32
- 2026-10-02 updated: child lesson-case-showing-ratification-fence-outside-the-blockquote added (synthesis) · raw/2026-10-02/1834/ledger.md#L40
