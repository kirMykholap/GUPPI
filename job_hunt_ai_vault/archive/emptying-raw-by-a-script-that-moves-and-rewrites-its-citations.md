---
title: "Emptying `raw/` by a script that moves a compiled source and rewrites the citations pointing at it"
type: proposal
status: deprecated
superseded_by: \"[[vault-archive-sh]]\"
basis: human
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-19/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery/handoffs/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery.md", ".claude/skills/ingest/SKILL.md", "scripts/vault-coverage.sh"]
tags: [vault, process, harness]
---

# Designed 2026-08-19, and not built

**The decision this builds is [[raw-is-emptied-by-a-script-and-the-move-lives-inside-the-ingest]].**
This page carries what it would take. **Nothing here exists on disk**: `raw/` has no internal
structure, no script moves anything, and no mapping table is emitted anywhere.

# What the script does, and it is exactly three operations

| Step | What it is |
|---|---|
| **move** | the source travels from `raw/<kind>/<file>` to `archive/<date>/<session>/<kind>/<file>`, laid out as it lies in `raw/` ([[the-archive-gains-a-folder-per-session-inside-the-date]]) |
| **emit** | an old-path-to-new-path mapping table, which is the artefact the owner liked and asked to be automated |
| **rewrite** | every `sources:` line naming an old path, from that table — the one place a detector is complete ([[a-rewriter-must-be-paired-with-a-detector]]) |

**The condition it runs under is already a command**: `vault-coverage.sh` printing
`INGEST COMPLETE` ([[handoff-retires-only-when-every-unit-has-a-verdict]]). Deciding that a source
is compiled is the agent's part, and it is the one part a script cannot do.

**The destination folder needs no system data.** The journal's filename carries the date and a slug
unique to the session; the harness's own session id is a UUID and would name the folder something no
human can read.

# What it cannot do, and the eye pass is accepted for now

**A path in a body is one string with two jobs** — an address that must move and a quotation that
must not — and nothing in the text separates them
([[sed-cannot-tell-an-address-from-a-quotation]]). **23 prose mentions of `raw/handoffs` were
measured at `b6fc6d8`**, against 150 pages naming it in all.

> **owner:** «хочется полностью автоматизировать этот процесс».

**Not satisfiable, and recorded as a standing want rather than a closed question.** The eye pass is
accepted **for now**. The nearest thing to a mechanical help is
[[a-path-detector-for-prose-references]], which can only ever be an advisory.

# What is open

- **Whether the trigger is a hook, whether the check is a hook, or both.** The decided shape puts the
  move inside `/ingest`, and the two halves can be split: the ingest moves, and a hook afterwards
  asserts that nothing compiled is still sitting in `raw/`. **The owner's, and not settled.**
- **Whether the rewrite touches `log.md`.** Rules 4 and 5 of the gate do not read it, so it is
  outside the detector and was swept by hand at the filename renames
  ([[log-md-is-outside-the-link-set-the-check-reads]], [[a-page-rename-is-sed-and-verify]]).
- **What happens to an archived page's own citations.** What an archived page asserts is frozen and
  how it is found is live ([[what-an-archived-page-asserts-is-frozen-and-how-it-is-found-is-live]]),
  and a rewrite over `archive/` has not been argued either way.

# What not building it costs

**The number is monotonic.** Every session that does not do this makes the migration larger, and the
uncompiled set stays invisible except by running `vault-coverage.sh` over every file — which is the
want the whole design exists to serve ([[moving-raw-into-a-dated-archive]]).

**And `raw/` gains its internal structure first**, or the rewrite runs twice
([[raw-gains-its-internal-structure-before-the-move]]).

Retired with `superseded_by:` the day it is built or refused
([[a-built-proposal-retires-once-nothing-on-it-lives-only-there]]).

# Built 2026-08-20, and retired

`scripts/vault-archive.sh` performs the three operations named above and ran on its first cargo the
same day ([[vault-archive-sh]], [[the-probe-scaffolding-is-archived-whole-into-specs]]).

**Both open questions about reach are closed, in opposite directions**: `archive/` IS rewritten and
`log.md` never is ([[archive-is-rewritten-by-a-path-move-and-log-md-never-is]]).

**The eye pass over prose survives as designed** — the rewrite touches only lines beginning
`sources:`, so a quotation is spared by construction rather than by care
([[a-path-is-never-a-pattern]]). The detector for the residual is still unbuilt
([[a-path-detector-for-prose-references]]).

**The remaining open question is untouched by the build**: whether a hook afterwards asserts that
nothing compiled is still sitting in `raw/`. The script is a tool the ingest calls, not a trigger.
