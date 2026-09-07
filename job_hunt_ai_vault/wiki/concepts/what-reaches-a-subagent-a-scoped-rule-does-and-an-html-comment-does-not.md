---
title: "What reaches a subagent, measured: a path-scoped rule does, and the HTML comment in it does not"
type: concept
status: current
authority: scoped-rule-delivery-measured
basis: measurement
sprint: S2
created: 2026-08-19
sources: ["archive/2026-08-19/2026-08-19-the-corpus-stops-counting-and-the-gate-learns-its-keys/handoffs/2026-08-19-the-corpus-stops-counting-and-the-gate-learns-its-keys.md", "archive/2026-08-20/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock/specs/RUNBOOK.md", "archive/2026-08-20/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock/specs/_probe-paths.md"]
tags: [harness, agents, testing]
---

# The answers, measured on 2026-08-19

Three of the probe's four questions are answered and the answers are recorded in `probe/RUNBOOK.md`.
The instrument, its nonces and what each outcome decides are [[the-conditional-delivery-probe]].

**Does the mechanism work at all — PASS.** Both instruments agree, which is the point of there being
two. `probe/instructions-loaded.log` took a line naming `"load_reason":"path_glob_match"` and the
trigger file, and the rule's text arrived in the session's context attached to the tool result.

**Does it reach a subagent — PASS.** A subagent was given a brief naming **no nonce and no rules
file**. It made one tool call, opened nothing else, and returned the whole rule file verbatim,
reporting that it had not opened it. That is delivery on a read by a subagent, with the observable
uncontaminated ([[a-runbook-that-carries-the-nonce-cannot-be-read-by-what-it-measures]]).

**Is an HTML comment stripped — STRIPPED.** On disk the rule file's line 6 is an HTML comment; in
what reached either reader, the frontmatter and the comment are both absent. So **a *generated, do
not edit* banner is free**, which is what the question was asked for
([[a-claude-rules-file-is-generated-whole-and-deleted-by-its-own-marker]]). It matches what this
corpus already measured on `CLAUDE.md` region markers.

**Does compaction demand a re-read — not run.** It needs `/compact`, and it is sequenced after the
ingest ([[the-compaction-probe-runs-after-the-ingest-and-the-ast-move-waits-on-it]]).

# The consequence, and it is narrower than it first read

**Delivery to a subagent needs no wiring**, so the AST rule's move proceeds as designed rather than
needing a line in every subagent brief. That was the fork the probe was built to settle
([[the-ast-rule-moves-to-prove-the-mechanism]]).

**It does not unblock the move on its own.** The move was said to be unblocked when this probe
passed; that statement was narrower than the truth, because the compaction probe's own stated
consequence gates the move as well.

# Instructions a subagent inherits that nobody wrote into its brief

**Session-level instruction reaches a subagent too, and it can contradict the brief.** The `auto
mode` instruction — *prefer Bash for reading and editing where it can do the job* — arrived at a
subagent whose brief **required the Read tool**. It followed the brief and **reported the conflict
rather than resolving it silently**, which is the behaviour worth knowing about before a brief
depends on which tool a subagent reaches for.

**The general point is the inheritance, not the one instruction.** A brief is not the whole of what a
subagent is told, and a brief written as though it were will occasionally be arguing with something
its author cannot see ([[a-skill-is-a-mask-and-a-subagent-is-a-body]]).

# The Edit half is still unmeasured, and it stopped being load-bearing — 2026-08-20

**Only `Write` was ever measured.** Whether the guard reaches a subagent's `Edit` as well is open,
and the consequence is now bounded: it stopped mattering when the owner chose path-narrowing over
subagent detection, so the rule's delivery no longer rests on which tool a subagent reaches for
([[a-guard-branch-in-the-edit-hook-delivers-a-path-scoped-rule]],
[[a-deferred-check-must-be-run-when-its-condition-arrives]]).
