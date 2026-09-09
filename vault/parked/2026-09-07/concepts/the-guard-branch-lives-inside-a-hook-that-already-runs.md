---
title: "The guard branch is another trigger inside a hook that already runs, and it reads no marker"
type: concept
status: current
authority: guard-branch-mechanism
basis: code
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-19/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery/handoffs/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery.md", ".claude/hooks/ask-the-vault.ps1", "scripts/hook-selftest.ps1"]
tags: [harness, agents, process]
---

# What it does

**A branch in `.claude/hooks/ask-the-vault.ps1`**, a hook `.claude/settings.json` has registered
under `PreToolUse` on `Edit|Write` since 2026-08-13 ([[session-hooks]]). It:

1. scans `.claude/rules/*.md`;
2. parses each file's `paths:` in **both YAML spellings**, block and inline;
3. matches the payload's `file_path`, reduced to a repository-root-relative path;
4. emits the body as `additionalContext`.

**It is a trigger, not a reminder.** The hole it closes is a governed file read before a `/compact`
and edited after it — edited with no rule in context and no signal that one is missing
([[what-survives-a-compaction-is-whatever-has-something-that-runs-it-again]],
[[a-path-scoped-rule-is-delivered-by-a-read-and-by-nothing-else]]).

**It adds no process.** The script already spawns on every Edit and Write in this repository, so the
latency is sunk; measured, the branch itself costs 17–21 ms on top of 177 ms, and the count of rules
barely moves it.

# Four properties that are decisions rather than details

**It reads no marker.** A file in `.claude/rules/` that no vault page backs is somebody's
hand-written rule and is delivered like any other. The marker is the **injector's permission to
delete**, and delivering is not deleting
([[a-claude-rules-file-is-generated-whole-and-deleted-by-its-own-marker]]).

**Both YAML spellings of `paths:` are parsed.** The field is authored on a vault page whose other
list fields are inline, and synced into a file whose own were written in block form
([[paths-lives-on-the-vault-page-and-is-written-widest]]). A parser that knew one spelling would be
blind to half the rules and **silent about it**.

**It strips HTML comments outside fenced blocks**, because the native delivery does and the design
requires both triggers to hand out the same text
([[what-reaches-a-subagent-a-scoped-rule-does-and-an-html-comment-does-not]]). A fence is left
alone, deliberately: this corpus documents its own markers inside fenced blocks, so a rule
explaining a marker would otherwise lose the thing it explains
([[a-fenced-block-inside-a-slice-survives-into-the-destination]]).

**It is last in the chain**, so a rule scoped at a vault path or at `CLAUDE.md` is shadowed by an
earlier branch. Nothing scopes there today. A rule that did would need the chain to **accumulate**
its notes rather than pick one, and the selftest case *an earlier branch still wins its path* pins
the current behaviour so that change shows up as a case turning over.

# What it is not

**It does not block.** It never refuses and always exits 0, and that is now a ruling rather than a
choice this branch made for itself ([[advisory-is-the-default-for-a-hook]]).

**Its honest cost is duplication.** On a normal Read→Edit flow the rule arrives twice, and the hook
cannot see the context to know. That is a slice-sized text paid on every edit of a governed file,
and it is stated rather than discovered.

# What it was measured against

**`scripts/hook-selftest.ps1` went from 40 caught to 54 caught, 0 missed, exit 0.** Of the cases
added for the branch, **seven were proved to fail against the pre-change hook** — recovered with
`git show HEAD:...`, swapped into the real tree, run, and swapped back in one command, reporting
`caught 44, missed 7`. **The rest assert silence and pass against both scripts**, so on their own
they test nothing about the branch and are regression guards rather than evidence
([[a-case-that-passes-before-the-change-tests-nothing]]).

**The comment-stripping half was measured, not assumed**: the probe rule's body is 971 characters
and 22 lines on disk, the guard delivers 940 and 20, and a line-by-line diff shows exactly one line
missing — the comment itself. `<!--` is present in the source and absent from what is delivered
([[a-loss-measured-between-different-quantities-is-not-a-loss]] for the reading that had to be
corrected first).

# The rule behind *It does not block* was struck, and the disposition is re-argued — 2026-08-22

**The section *What it is not* says this branch never refuses and always exits 0, *"and that is now
a ruling rather than a choice this branch made for itself"*, citing
[[advisory-is-the-default-for-a-hook]].** The owner disowned that rule on 2026-08-21 and it is
retired ([[a-paraphrase-signed-owner-becomes-a-quote-and-is-reasoned-from-as-his-word]]). **The
section stays as written**: it records the moment a disposition here stopped being inherited from a
description of behaviour ([[no-rule-reads-a-harness-file]], [[session-hooks]]).

**It is still a ruling, and it is a different one**
([[a-hook-refuses-on-a-measured-condition-a-reliable-measurement-and-a-refusal-that-says-how-to-clear-it]]).
The branch's own question — *does a file in `.claude/rules/` scope a `paths:` pattern onto the path
being written* — **is** measured: it is a glob against a payload field, decided in the script and
pinned by cases. **What has no measurement is the condition a refusal here would have to rest on**,
which is whether the writer already holds the rule in context. The hook cannot see the context, and
this page already states that as its honest cost: on a normal Read→Edit flow the rule arrives twice
and the hook cannot tell.

**So it allows and says so aloud, which is the new rule's own clause** rather than a default this
branch falls back to. **Nothing in the script changes and no case in `scripts/hook-selftest.ps1`
turns over** ([[a-refusal-is-possible-on-pretooluse-alone-and-the-register-is-a-test]]).

**The write net appended after this chain speaks for a different reason, and it is the ledger's**: a
row cannot be written in plan mode, which is the exact moment the ritual is placed, so the
measurement is unreliable where that branch stands ([[the-pre-task-ledger]],
[[the-plan-check-hook]]).
