---
title: "The archiver checks the criterion, marks and moves a decision in one pass, and the librarian sets no mark"
type: decision
status: archived
authority: processed-writer
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-30
created: 2026-08-30
target_kind: action
target: the-sweep-reads-the-handshake-before-it-releases-a-decision
supersedes: [[the-librarian-sets-processed-when-it-writes-decided-by-and-the-archiver-reads-each-field]]
sources: ["archive/2026-08-30/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md", "scripts/vault-archive.sh", ".claude/skills/ingest/SKILL.md"]
tags: [vault, process, harness]
---

# Context

**The two-step rule of 2026-08-29 split the mark from the move**: the librarian set `processed` when
it wrote `decided_by:`, and the archiver read each field
([[the-librarian-sets-processed-when-it-writes-decided-by-and-the-archiver-reads-each-field]]). **Its
ground was that the mark is a judgement** — someone had to decide that the decision's content had
moved on, and only a reader could.

**Case 2.3 replaced that judgement with a mechanical criterion.** The handshake decides carriage: the
decision names its target forward, the target names it back
([[a-decision-declares-its-target-and-the-handshake-closes-it]]). Nothing left for a reader to judge.

# The question

**Who writes the mark, now that the criterion is mechanical?**

# How it works after

**`scripts/vault-archive.sh` checks the criterion itself, sets the mark and moves the page in ONE
pass. The librarian no longer sets any mark.**

**The ground of the two-step rule is gone rather than outweighed**, which is why this is a
supersession and not a compromise. A rule whose reason has been removed is not a rule that has been
overruled.

**The instruction that told the librarian to set `processed` left `.claude/skills/ingest/SKILL.md` on
2026-08-30**, in the same session.

# Recommendation

**One pass**, against keeping the split for safety. The session put the ground of the older rule and
showed that Case 2.3 had already dissolved it.

# Ratification

**The owner said it**: «Case 2.4 - ратифицирую».

**And the consequence he was told about was wrong, which is recorded rather than quietly repaired.**
Case 2.4 was ratified on the ground that `processed` and `archived` stay distinguishable — a decision
released by the refused-proposal route leaving **without** `processed`. In one pass they are two
values of the **same field**, so `processed` is written and overwritten in the same act and no reader
ever observes it. That was found while writing the archiver, by neither the session nor `/pre-task`,
and it is what repealed the value ([[processed-is-repealed-and-the-mark-it-carried-is-derived]]).

**This decision depends on a ruling that is recorded and not executed.** If `/vault-lint` does not
run, the pass does not run, nothing is marked and nothing moves
([[vault-lint-runs-every-session-so-the-sweep-fires]]).

*(Compiled from `raw/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md`.)*
