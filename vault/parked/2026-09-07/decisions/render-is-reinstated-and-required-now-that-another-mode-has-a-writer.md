---
title: "`render:` is reinstated and required on a rule page, now that another delivery mode has a writer"
type: decision
status: current
authority: delivery-mode-field
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-19
created: 2026-08-20
sources: ["archive/2026-08-19/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery/handoffs/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery.md", "job_hunt_ai_vault/wiki/rules/_schema.yaml", "scripts/vault-inject.sh"]
tags: [harness, vault, record-schema]
supersedes: [[render-was-not-introduced]]
---

# The ruling, 2026-08-19

> **owner: `render:` is reinstated and required.**

**It is required in `wiki/rules/_schema.yaml`**, and every rule page that existed on that day was
stamped `render: region` by the librarian.

**Rejected: selecting the mode from the shape of `governs:`** — reading a destination path and
inferring *whole* from the directory it lands in. That hides a rule inside a directory name: the
delivery guarantee would then change when a file moves, with nothing on the page saying so.

## Why the refusal of 2026-08-17 is spent rather than overturned

[[render-was-not-introduced]] refused the field **and named its own re-entry condition** — *"the day
a second delivery mode is built. At that point the field has a writer, a reader and at least two
values, which is the admission test this store already uses for a field"*
([[the-frontmatter-core-is-fixed-and-updated-joins-it]],
[[a-field-earns-its-place-by-being-read-or-by-being-a-checksum]]).

**The `whole` mode is that day** ([[the-whole-mode-owns-a-file-end-to-end]]). The field now has a
writer — the injector branches on it — a reader, and the values `region` and `whole`. The condition
was met and the page is retired on its own terms, which is the shape a refusal is supposed to have.

## What is still owed, and it is a trap while it stands

**The injector defaults an absent `render:` to `region`**, and the default is a trap for a reader:
the field is required where it can discriminate and absent where it cannot, so a page outside
`wiki/rules/` renders with a mode nothing on it names.

**Removing the default takes three moves in one order**, and doing part of it is worse than doing
none:

1. `render` becomes **optional** in `concepts/_schema.yaml`;
2. the two `concepts/` pages that carry `governs:` gain `render: region`;
3. **only then** does the injector stop defaulting.

The first is the session's file and the third is code
([[what-the-gate-reads-as-its-own-input-is-the-sessions-to-write]]), so this is not an ingest's to
perform alone. It is deferred here with its order rather than left in a brief.

**Until it lands, the reach of the default is bounded and stated**: the field is a `rules/` field,
absent means `region`, and both concept pages that carry `governs:` do render into a region — so the
default is currently correct everywhere it applies and is a trap only for the next page written.

# The section above is discharged, and its text went false on 2026-08-20

**All three moves landed, in the order stated.** `render` is `optional:` in
`wiki/concepts/_schema.yaml` with its `values:` list copied; the two `concepts/` pages carrying
`governs:` are stamped `render: region` at line 6; and `scripts/vault-inject.sh` no longer defaults
the field.

**Two sentences of `## What is still owed` describe a state that no longer exists**, and they are
corrected here rather than in place: *"The injector defaults an absent `render:` to `region`"* and
*"absent means `region` … so the default is currently correct everywhere it applies and is a trap
only for the next page written."* **Neither holds.** Absent is now a verdict:
[[an-absent-render-is-red-on-a-page-that-renders]], on the owner's ruling of 2026-08-20 — the
verdict this page did **not** name, which is the gap `/pre-task` surfaced before any code was
written.

**Measured after the change: this page is the only place left in `scripts/`, `.claude/`, `wiki/` or
`CLAUDE.md` that still claims the default.** Everything else moved with the code. **A page that
ordered work is the last place anyone looks for a stale claim about it**, which is why the reading
was taken rather than assumed ([[the-date-of-a-correction-note-is-the-date-the-text-became-false]],
[[a-copied-list-drifts-and-a-sweep-cannot]]).

**And the order this page prescribed was load-bearing for a reason it did not state**: the gate
builds its `allowed` key set from `required:` and `optional:` and nothing else, so move 2 before
move 1 is red on both pages
([[the-unknown-key-verdict-orders-a-schema-change-ahead-of-the-page-that-uses-the-field]]).

# A third value was minted on 2026-08-30, and the text above naming two is left as it stands

**owner, 2026-08-30: «render получает новое свойтсво - authority.»**

**`render: authority` names a rule written into no file.** It is found by a lookup on its
`authority:` slug rather than injected, so such a page carries a slug and **no** `governs:` — which is
why `governs:` moved from `required:` to `optional:` in `wiki/rules/_schema.yaml` in the same change,
with the obligation moving into the gate's `nogoverns` verdict rather than into the schema
([[a-rule-under-render-authority-is-written-into-no-file-and-found-by-its-slug]]).

**Two verdicts came with it**: `authoritygoverns` reddens a lookup rule that also names a destination,
`authoritynoslug` reddens one with no slug to be found by.

**The re-entry condition this page's predecessor named is met again.**
[[render-was-not-introduced]] refused the field while one delivery mode existed, and named the day a
second mode is built as its re-entry. `whole` was that day; `authority` is the third, and the
same argument admits it.

**Read off the tree on 2026-08-30: fifteen pages carry `region`, two carry `whole`, and none carries
`authority`.** So the value's discriminating power is prospective for the third time.

**The admission test the schema comment asserts it passes is not passed yet.** A value has a reader
and a writer from the day it is minted — the test `status: repealed` failed. The gate branches on
`render: authority` in three places, so the reading half is real; **the delivering half does not
exist**, because the hook that is supposed to serve such a page has no `authority:` matching branch
([[the-hooks-authority-branch-is-not-written-and-the-read-matcher-is-downstream]]).

*(Extended 2026-08-30 from `raw/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md`.)*
