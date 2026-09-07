---
title: "`processed` is struck from the schema once no page carries it, and the condition is a command"
type: decision
status: current
authority: processed-removal-condition
binding: deferral
basis: human
sprint: S3
decided: 2026-08-30
created: 2026-08-30
target_kind: action
target: strike-processed-from-the-schema
sources: ["archive/2026-08-30/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md", "wiki/decisions/_schema.yaml", "scripts/vault-archive.sh"]
tags: [vault, record-schema, harness]
---

# Context

**`processed` was repealed on 2026-08-30 and could not be struck in the same act**
([[processed-is-repealed-and-the-mark-it-carried-is-derived]]). **One live page carries it** —
[[every-question-put-to-the-owner-carries-context-and-a-recommendation]] — and a value not declared in
the folder's `_schema.yaml` is red on any page carrying it.

**A red gate is a refusal to dispatch the only writer permitted to clear it**
([[a-lock-on-a-red-tree-hides-the-health-of-what-it-guards]]), so striking the value while the page
still holds it would lock the store rather than tidy it.

# The question

**When does the value actually come out, and who decides that the moment has arrived?**

# How it works after

**The condition is a command and it is written into the schema itself**, so nobody has to remember it
or judge it:

```
grep -rl '^status:[ \t]*processed' wiki/
```

**When that returns nothing, two things come out together**: the `processed` entry from
`wiki/decisions/_schema.yaml`, and the `pages_with_status decisions processed` line in
`sweep_candidates()` in `scripts/vault-archive.sh`. Removing one without the other leaves a sweep
hunting a value the schema forbids, or a schema declaring a value nothing writes.

**Nothing new acquires the mark meanwhile.** The instruction that told the librarian to set it left
`.claude/skills/ingest/SKILL.md` on 2026-08-30.

# Recommendation

**Leave the value legal and write the removal condition as a command**, against striking it now and
against leaving the removal to a future reader's judgement.

# Ratification

**The session understood it** from the tree, and the owner ratified the repeal that makes it owed.

**This is the fill order run backwards** — legal, then empty the corpus, then remove — where this
store's usual order is legal, then fill, then promote. **Nothing in the vault states that shape**, and
it is written here so the next reader meets it as a decision rather than as an inconsistency.

**Not built.**

*(Compiled from `raw/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md`.)*
