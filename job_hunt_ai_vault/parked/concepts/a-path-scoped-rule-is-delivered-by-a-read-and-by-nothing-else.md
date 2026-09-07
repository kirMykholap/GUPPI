---
title: "A path-scoped rule is delivered by a read and by nothing else, so an edit needs a guard"
type: concept
status: current
authority: scoped-rule-trigger
basis: measurement
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-19/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery/handoffs/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery.md", "archive/2026-08-19/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell/handoffs/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell.md", "archive/2026-08-20/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock/specs/RUNBOOK.md", ".claude/hooks/ask-the-vault.ps1"]
tags: [agents, harness, process]
supersedes: [[a-scoped-rule-fires-on-a-read-and-an-edit-implies-one]]
---

# What delivers a scoped rule, measured

**The Read tool delivers it. Nothing else does.**

| action on a matching path | does the rule arrive | how that is known |
|---|---|---|
| reading the file | **yes** | the documented case ([[claude-code-loads-a-rules-file-at-launch-and-a-scoped-one-on-a-read]]) |
| editing an existing file | **no** | measured — the Edit produced no hook line at all, so the mechanism never fired |
| writing over an existing file | **assume no** | same reasoning, not separately measured |
| creating a new file | **no** | there is nothing to have read |
| a Bash command touching the path | **no** | no read tool is involved |

**The Edit tool's read gate is *session*-scoped, not context-scoped.** It survives a `/compact`, so
after one the Edit sails through: the tool remembers the read, the model does not hold the rule, and
nothing reports the gap ([[what-survives-a-compaction-is-whatever-has-something-that-runs-it-again]]).

**And a scoped rule does reach a subagent that reads a matching file**, measured, with no wiring
owed ([[what-reaches-a-subagent-a-scoped-rule-does-and-an-html-comment-does-not]]).

# Why this page replaces the one before it, rather than correcting it

**The page this supersedes stated the editing row as *yes, by implication*** — reasoning that Edit
requires the file to have been read in this session, so the read the rule needs is the one the
editing tool already demands. **That reasoning confuses a tool's precondition with a delivery
trigger**, and the measurement separated them.

**It was corrected in place first and superseded whole afterwards, on the owner's ruling of
2026-08-19** — the in-place correction was the narrower of the options and the wider one was taken
([[a-title-corrected-in-place-is-not-a-supersession]]). The retired page is where to read what was
believed and why it looked sound; nothing here re-argues it.

**And the basis changed with the claim.** The retired page was `basis: human`, recording the owner's
reading; this one rests on probe measurements and says so.

# What it decides, which is which rules may move at all

**The criterion is that the dangerous action requires reading a matching file first.** It survives
the correction intact, and it still separates the rules of the repository's `CLAUDE.md`
([[moving-a-rule-into-claude-rules-with-a-paths-scope]]):

- **the AST boundary rule moves** — its dangerous action is editing an existing boundary test, and
  it has moved ([[the-guard-is-built-and-the-ast-move-went-ahead-behind-it]]);
- **the JavaScript rule does not** — the dangerous action is writing a *new* file, which matches no
  read ([[the-javascript-rule-leaves-claude-md-and-is-not-yet-removed]]);
- **the test-database rule does not** — `uv run pytest` is a command, and a command reads nothing
  ([[the-suite-never-runs-against-the-production-database]]).

**Those failures are the same failure**: the rule is scoped to the artefact and the danger is in an
action that never opens it.

**What fails is not the criterion but its sufficiency.** The dangerous action does require a read,
and the read does deliver — **but only until something clears the context, and nothing re-delivers
after that.** So a move of this kind goes behind a guard rather than on the strength of *whoever
edits it will have read it* ([[the-guard-branch-lives-inside-a-hook-that-already-runs]]).

# What is settled that this page's predecessor left open

- **Whether compaction closes on a demanded re-read** — it does not.
- **Whether a scoped rule reaches a subagent** — it does, and no wiring is owed.
- **Whether losing a rule to a `/compact` is acceptable for a rule of this weight** — **it is not**,
  which is why there is a guard in front of the move instead of a judgement call behind it.
