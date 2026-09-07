---
title: "`processed` is repealed, and what it distinguished is derived from the tree instead"
type: decision
status: current
authority: processed-status-mint
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-30
created: 2026-08-30
target_kind: repeal
target: processed-means-the-decisions-content-moved-on-and-the-mark-opens-a-state
supersedes: [[processed-means-the-decisions-content-moved-on-and-the-mark-opens-a-state]]
sources: ["archive/2026-08-30/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md", "wiki/decisions/_schema.yaml", "scripts/vault-archive.sh"]
tags: [vault, record-schema, process]
---

# Context

**`processed` was minted on 2026-08-28** to say that a decision's content had moved on
([[processed-means-the-decisions-content-moved-on-and-the-mark-opens-a-state]]). Case 2.4 of
2026-08-30 then ratified that the archiver marks and moves in **one pass**
([[the-archiver-marks-and-moves-a-decision-in-one-pass]]) — and it was ratified partly on the ground
that `processed` and `archived` would stay distinguishable.

# The question

**Can `processed` survive a single archiving pass?**

# How it works after

**No, and the reason is arithmetic rather than judgement.** `processed` and `archived` are two values
of the **same field**. In one pass the page takes `archived`, so `processed` is written and
overwritten in the same act and **no reader ever observes it**. It cannot distinguish anything,
because it does not exist for any length of time.

**The value is repealed and the decision of 2026-08-28 that minted it is overturned.**

**What it distinguished is derived from the tree instead**: a discharged decision has a target that
names it back; one dropped with a refused proposal does not
([[a-refused-proposal-releases-every-decision-in-its-list]]).

**The value could not be struck in the same act**, and that is the fill order run backwards. **One
live page carries it** — [[every-question-put-to-the-owner-carries-context-and-a-recommendation]] —
and striking the schema entry would redden the gate on that page, while a red gate is what
`lock-the-librarian.ps1` reads as a refusal to dispatch the only writer permitted to clear it
([[a-lock-on-a-red-tree-hides-the-health-of-what-it-guards]]). **So the value stays legal until the
corpus is empty of it**, and the removal condition is written into the schema as a command:
`grep -rl '^status:[ \t]*processed' wiki/` returns nothing
([[processed-is-struck-from-the-schema-once-no-page-carries-it]]).

**The instruction that CREATED the mark left `/ingest` on 2026-08-30.** So no new page acquires it
while the old one waits.

# Recommendation

**Repeal**, against keeping a value nobody can observe. The session recommended it after finding the
defect while writing the archiver.

# Ratification

**The owner said it**: «archived выглядит честнее, чем processed. По сути его ставит архиватор, а не
"обрабатывает агент". Ратифицирую твою рекомендацию. решение от 28 августа, которым processed был
заведён - отменяется».

**This is one of two rulings of 2026-08-29 and 2026-08-28 overturned on 2026-08-30, both knowingly
and both his.**

# What this repeal cannot do, and it is named rather than left to be found

**`status: repealed` is legal in `wiki/rules/` alone**, and the page this decision cancels is a
**decision** ([[a-cancelled-page-takes-a-status-of-its-own]]). So the cancelled page is retired by the
only route open to it — `deprecated` and `superseded_by:` naming this page, which does carry the
successor claim. **That sits close to the owner's own ruling that a repeal is not recorded by
supersession**, and the difference is that a successor claim exists here and did not in the case he
ruled on. **It is raised rather than settled by the librarian.**

*(Compiled from `raw/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md`.)*
