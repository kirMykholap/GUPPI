---
title: "A teardown clause cannot see that it has become the thing it guards"
type: lesson
status: archived
authority: teardown-clause-inversion
basis: measurement
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-19/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery/handoffs/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery.md", "archive/2026-08-20/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock/specs/RUNBOOK.md", "scripts/vault-check.sh"]
tags: [vault, harness, process]
---

# The inversion

**`probe/RUNBOOK.md` makes the deletion of the probe scaffolding conditional on probe 4's answers
reaching `wiki/`.** They reached it — **and the reaching is what forbids the deletion.** Pages
compiled from those files now cite them in `sources:`, and rule 5 of the gate reddens on a
`sources:` path that does not exist.

**Measured at `6bb9a12`:** `probe/RUNBOOK.md` on seven pages, `.claude/rules/_probe-paths.md` on
three, `.claude/hooks/instructions-loaded.ps1` on two — twelve citations.

**Proved rather than argued**: `probe/RUNBOOK.md` was moved aside, `bash scripts/vault-check.sh`
returned **exit 1** naming all seven pages with *"sources names a path that does not exist"*, and the
file was restored in the same command
([[a-new-verdict-is-proved-in-the-real-tree-because-the-check-cannot-see-a-sandbox]]).

# Why no instrument could have caught it

**The condition was correct when it was drafted**, on 2026-08-18, when those files were scaffolding
and nothing pointed at them. **The ingest turned them into evidence.** A teardown clause is a
sentence in a document; it cannot observe that the world around it has changed the meaning of its
own predicate.

**This is the day's recurring shape**: an instruction that was correct when written and silently
stopped being ([[no-rule-reads-a-harness-file]],
[[a-mechanisms-first-use-outside-its-home-is-where-it-drifts]]). What is specific here is that the
mechanism which invalidated the clause is **the one the clause was waiting for**.

# What was safely executed, and what stays

**Executed 2026-08-19**, with `bash scripts/vault-check.sh` at exit 0 and 21 advisories before and
after, **byte-identical output**: `probe/probe-target.md` and `probe/instructions-loaded.log`, both
cited in prose and in **no** `sources:` line, and the `InstructionsLoaded` block in
`.claude/settings.json`, which is a settings key rather than a cited path.

**Still blocked, and it is the librarian's**: `probe/RUNBOOK.md`, `.claude/rules/_probe-paths.md`
and `.claude/hooks/instructions-loaded.ps1` are named in `sources:` and cannot go until those lines
are rewritten. **`.claude/hooks/instructions-loaded.ps1` is inert and on disk**, which is the honest
state.

**Whoever reads either of the surviving runbooks is told to do what the tree forbids**, and that is
the live cost of leaving it.

# What it needs, which is a ruling and then a rewrite

**Where a machine artefact lives is the owner's.** `raw/` holds testimony and freezes artefacts
([[raw-holds-testimony-and-artefacts-are-frozen]]), and neither `raw/handoffs/` nor `raw/notes/` is
a home for a hook log. **Then twelve `sources:` lines are rewritten**, which is not a session's to
make ([[the-librarian-writes-unattended]]).

# The general form

**A cleanup instruction should name what may cite its targets, not only what must be true before
deletion.** The condition *"once the knowledge has landed"* is the condition under which the files
acquire citations, so it is precisely the wrong trigger to hang a deletion on.
