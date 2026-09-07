---
title: "A field's legal values live beside its legal keys, and are read in the same pass"
type: concept
status: current
authority: schema-value-parsing
basis: code
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-19/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery/handoffs/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery.md", "scripts/vault-check.sh", "job_hunt_ai_vault/wiki/lessons/_schema.yaml"]
tags: [record-schema, harness, vault]
---

# The mechanism

**`values:` in a folder's `_schema.yaml` names a field and the values it may carry**, standing
beside the `required:` and `optional:` blocks that name the keys
([[the-per-folder-frontmatter-schema]]).

```yaml
values:
  basis:
    - human
    - code
    - measurement
    - external
    - inference
```

**The gate builds the legal set in the same `awk` pass that reads the key set** and prints a red
verdict for a value outside it ([[a-value-outside-the-schemas-list-is-red]]). One pass, one read of
the file, and no second loader to keep in step with the first.

# A set that parses to nothing is red

**A `values:` header that yields no members is a red verdict in its own right**, for the reason the
missing-schema and empty-`required:` verdicts exist: **the failure to design around is the
permissive one.** A silent empty set passes every value, in the direction that hides a defect
([[a-denominator-is-walked-off-the-input-list]],
[[the-gate-learns-the-legal-key-set-from-a-yaml-per-folder]]).

**What it is not guarded against is a set that yields the *wrong* members.** A value misspelled
inside a schema would reject every page carrying the correct spelling — loud rather than silent, and
a confusing morning. That is the same known and accepted gap the key half carries, and it is named
so the first reader of a wall of red checks the yaml before the pages.

# The loader strips `\r`, and the ones beside it did not

**The value loader strips a trailing carriage return**, as the page pass does and says so in a
comment. **The `required:` and `optional:` loaders do not**, and they are pre-existing.

That asymmetry is invisible on this host and live in the container, which is why it was reported
rather than quietly assumed harmless
([[no-cr-reaches-awk-on-this-host-and-the-container-is-where-it-bites]]). With `*.yaml` now pinned
to LF the class cannot be reached from the checkout direction
([[the-yaml-class-is-pinned-to-lf]]) — **which is a reason to leave the other two rather than a
reason they are right.**
