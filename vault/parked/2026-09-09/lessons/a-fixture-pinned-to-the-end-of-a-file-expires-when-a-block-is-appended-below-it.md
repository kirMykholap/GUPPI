---
title: "A fixture pinned to the end of a file expires when a block is appended below it"
type: lesson
status: current
authority: fixture-positional-dependency
basis: code
sprint: S3
created: 2026-08-30
sources: ["archive/2026-08-30/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md", "scripts/vault-check-selftest.sh", "job_hunt_ai_vault/wiki/decisions/_schema.yaml"]
tags: [testing, vault, record-schema]
---

# The incident, 2026-08-30

**The `lc_key_not_allowed` case appended its line to the end of `wiki/decisions/_schema.yaml`** and
depended, silently, on `required_from:` being the last block in that file. The case is about a key
listed in `required_from:` that appears in neither `required:` nor `optional:`.

**A block was added below it that day** — `sections_when_target_kind_rule:` — and the appended line
landed inside the new block instead. **The case stopped testing its subject and did not go red.** It
reported a different reason, and the suite called it a miss only because the reported message did not
match the expected one. Had the messages happened to agree, the case would have passed while
asserting nothing about `required_from:`.

**Repaired by inserting under the heading** the case is about, rather than at the end of the file.

# What is actually wrong with it

**"The end of the file" is not an address of anything.** It names a position that every future edit
may move, and no reader of the fixture can see what it depends on: the dependency is on the absence
of a block that has not been written yet.

**The failure direction is the dangerous one.** It does not go red when it expires — it silently
changes subject, and the only thing standing between that and a green pass is whether the message the
gate prints happens to differ from the message expected.

# The class

**A fixture that locates its material by position expires the next time the material is reordered.**
The repair is always the same: name the thing, not the place. Insert under the heading, match on the
key, anchor on the identifier.

**It is a different cause from the one this store already had.**
[[a-test-can-be-green-on-placeholders-its-own-setup-created]] is a setup fabricating what the subject
was supposed to find; here the setup materialises the right thing in the wrong place, which is a
positional dependency rather than a fabricated one.

**How many other cases in the suite carry a positional dependency is unmeasured**, and that number
decides whether the repair is a note or a sweep.

*(Compiled from `raw/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md`.)*
