---
type: estimate
kind: QA
status: passed
target: rule-materialize
origin: raw/2026-09-10/ledger.md#case-31
sprint: migration
created: 2026-09-10
tags: [harness, workflow, ledger]
---

## Context

The yaml is the librarian's whole view of the session. An entry routed wrong, or a line dropped, is a decision that never becomes a page.

## Criterion

Against a temp vault: a ledger with timed and untimed lines, HTML comments, a create
with ref and tags, a Leaf create whose estimate sits nested in the Spec's then
block, an update with set, sections and replace, a delete, a defer without ref, a
supersedes chain, an estimate line for a page of this ledger and one for an earlier
page, a lesson line and one unparsable line yields a yaml with one entry per record
line in ledger order, each with case, kind, category, slug, origin, line, text and
the decision slug of its Case; the nested estimate is its own create entry; the
superseded entry carries superseded_by; the first estimate line is folded into its
create, the second is an estimate entry; the lesson entry carries root_cause and
origin #L<n>; the unparsable line is under unparsed; a create without a then block
is marked incomplete, a create whose page exists is marked exists; a Rule-class slug
routes to file with its path; one decision entry per Case carries case_text and
targets. An existing yaml gains only the entries of ledger lines it does not hold,
keeps its edited and applied entries, reports a text mismatch, gains superseded_by
from a later supersedes, and turns an estimate line for an applied create into an
estimate entry. Live: --date 2026-09-09 over the 85-line ledger yields no unparsed
line and every create marked exists; the reading records the counts per kind.

## Method

pytest in tests/test_materialize.py against a temp vault; the live reading once by hand

## Result

tests/test_materialize.py 12 green; live 2026-09-10: 67 entries (update 34, create 26, estimate 3, lesson 2, defer 2), 21 decision entries, no unparsed line, incomplete only on the two lessons (tags, source) and case 28 (no Spec text); live --date 2026-09-09: 87 record lines, 74 entries (create 34, update 32, lesson 7, delete 1) plus 13 estimate lines folded into their creates, 34 decision entries, no unparsed line, all 34 creates marked exists

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-31
- 2026-09-10 updated: criterion: an existing yaml gains only the entries of ledger lines it does not hold (the Criterion of case 31 already carries it) · raw/2026-09-10/ledger.md#case-41
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L70
