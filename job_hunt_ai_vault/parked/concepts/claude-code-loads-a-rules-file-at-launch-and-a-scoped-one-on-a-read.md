---
title: "How Claude Code loads `.claude/rules/`, as documented — and the one thing the documentation is silent about"
type: concept
status: current
authority: rules-file-loading
basis: external
sprint: S2
created: 2026-08-18
sources: ["archive/2026-08-18/2026-08-18-the-marker-carries-its-type-and-the-gate-was-blind/handoffs/2026-08-18-the-marker-carries-its-type-and-the-gate-was-blind.md"]
tags: [agents, harness, process]
---

# What the documentation says

| Shape | When it loads |
|---|---|
| a file in `.claude/rules/` with no `paths:` frontmatter | **at launch**, with `.claude/CLAUDE.md`'s priority |
| a file in `.claude/rules/` carrying `paths:` | **only when a matching file is read** |
| a `paths:`-scoped rule after `/compact` | **not re-injected** |
| a subagent | receives the `CLAUDE.md` hierarchy **including project rules** |
| the built-in Explore and Plan agents | **skip it** |

**This is `basis: external`** — read off vendor documentation, not measured here. It is written down
because it is the mechanism a planned move depends on
([[a-rule-moving-to-conditional-delivery-needs-its-page-first]],
[[moving-a-rule-into-claude-rules-with-a-paths-scope]]).

# The silence, and why it is the load-bearing gap

**Whether a `paths:`-scoped rule fires inside a subagent that reads a matching file is documented
nowhere.** The two facts above touch either side of the question and neither answers it: a subagent
gets project rules, and a scoped rule loads on a read — but nothing says whether the subagent's read
is a triggering read.

**Every task in this project is reviewed by a subagent.** So the readers most in need of a
boundary rule are exactly the ones whose delivery is undefined, and a move made on the documented
half alone would be a rule that silently does not arrive for the reviewer.

**It is answered by measurement, with the `InstructionsLoaded` hook**, and the measurement decides
what wiring the move needs rather than whether it happens.

## What the two loading facts already imply for this project

- **`/compact` drops a scoped rule and does not put it back.** A long session therefore loses a
  conditional rule mid-flight, silently, and the loss is invisible in the transcript — the same
  class as a change that is on disk and not in the running process
  ([[claude-code-config-loading]], [[app-restart-required]]).
- **Unconditional delivery is the current guarantee.** Nine rules render into the repository's
  `CLAUDE.md` and reach every session ([[wiki-rules-holds-the-rules-of-the-repository-claude-md]]);
  moving one is a downgrade of that guarantee in exchange for context, which is why it is a decision
  and not a refactor.

# What the tool contracts add, and how the silence is being measured — 2026-08-18

**The documentation's "reads" is narrower than what triggers the rule.** Edit requires the file to
have been read in the session and Write requires it for an existing file, so *touching* an existing
file triggers a scoped rule; creating a new file and running a Bash command do not
([[a-scoped-rule-fires-on-a-read-and-an-edit-implies-one]]). That table is `basis: human` — it is
the owner's reading of the tool contracts, not vendor text — and it is what makes exactly one rule
of the repository's `CLAUDE.md` movable.

**The silence above is now a laid measurement rather than an open question.** Probe 2 asks whether a
subagent's read triggers the rule, and probe 4 asks whether Edit demands a re-read after `/compact`
— which is the whole of whether compaction matters ([[the-conditional-delivery-probe]]). Both are
inert until the harness restarts.
