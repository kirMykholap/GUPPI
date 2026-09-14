---
type: insight
pattern: A script of the pipeline assumes every entry of materialize.yaml carries the fields and the shapes it wrote itself; an entry written by another hand ends the whole run instead of failing alone.
status: actioned
children: ["[[lesson-generate-replace-mapping-crashes]]", "[[lesson-materialize-assumes-every-entry-has-a-line]]"]
severity: 0
addressed_by: "[[decision-case-142.3]]"
origin: raw/2026-09-10/ledger.md#L122
sprint: migration
created: 2026-09-10
tags: [harness, ledger, librarian]
---

## Pattern

Two lessons of one run share a cause.

`lesson-generate-replace-mapping-crashes`: the Spec wrote `replace` as a mapping, materialize lifted
it as written, and generate iterated it as a list. One entry stopped the whole run.

`lesson-materialize-assumes-every-entry-has-a-line`: the three entries the librarian appended at
synthesis carry no `line`, because no ledger line made them. Materialize builds its index over
`e["line"]` for every entry, and the run stopped before anything was written.

`materialize.yaml` has four writers: materialize itself, the Spec block it lifts, the librarian, and
generate's marks. Each script reads the file as if it alone had written it, so a shape from another
writer is not a rejected entry but a crashed run. Both cases were fixed one at a time, in the script
that crashed; nothing yet states the shape of an entry in one place for all four writers.

## Proposal

A suggestion, not a decision. Two things could hold this down.

One: state the shape of a yaml entry in one place — which fields a writer may add, which are optional,
which shapes a field takes — and have every script read an entry through that one description.
`case-schema.md` now pins `replace`; `rule-materialize` lists the marks. Neither is the whole shape.

Two: extend the rule of Case 47 — an entry fails alone whatever the cause — from generate to
materialize, so the file is never left unwritten because one entry is odd.

## Children

- [[lesson-generate-replace-mapping-crashes]]
- [[lesson-materialize-assumes-every-entry-has-a-line]]

## Addressed by

- [[decision-case-142.3]]

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#L122
- 2026-09-14 updated: actioned: materialize fails an entry alone and generate keeps its mark (142.1, 142.2); the field list of rule-materialize is the one place for the entry shape; no schema module in code (case 142.3) · [[decision-case-142.3]]
