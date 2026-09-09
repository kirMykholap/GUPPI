---
title: "The lock hook on the librarian dispatch, the first hook here that refuses"
type: entity
status: current
authority: librarian-dispatch-lock
basis: code
sprint: S2
created: 2026-08-20
supersedes: "[[a-lock-on-the-librarian-dispatch]]"
sources: ["archive/2026-08-20/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock/handoffs/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock.md", ".claude/hooks/lock-the-librarian.ps1", ".claude/settings.json", "scripts/hook-selftest.ps1"]
tags: [harness, agents, testing]
---

# What it is

`.claude/hooks/lock-the-librarian.ps1`, built 2026-08-20. A `PreToolUse` hook, matcher
`Agent|Task`, narrowed inside the script to `subagent_type: vault-librarian`. It runs
`scripts/vault-check.sh` and returns `permissionDecision: deny` while the gate exits non-zero,
carrying the gate's output as the reason.

**It is the first hook in this repository that refuses anything.** Everything before it reported
([[advisory-is-the-default-for-a-hook]], [[the-journal-gate-hook]]).

## The two questions its proposal left open are closed

Both on the owner's rule that a refusal states its condition or has no appeal
([[a-refusal-is-conditional-or-absolute-and-nothing-else]]):

- **A red check for an unrelated reason DOES block**, because the condition is named and clearable
  — which makes the refusal conditional rather than absolute.
- **The denial carrying the check's output is mandatory**, not optional.

## It allows when it cannot measure

If bash is not findable it prints `THE LOCK DID NOT RUN` and exits 0. Refusing on a measurement
that never happened is a refusal that can be wrong, which the default forbids
([[advisory-is-the-default-for-a-hook]]).

`Find-Bash` is the shared discovery function it calls, and moving it into `.claude/hooks/vault-path.ps1`
to get it is a recorded divergence ([[do-not-change-a-working-file-mid-work]]).

## What is proved, and the half that is not

`scripts/hook-selftest.ps1` went from 54 cases caught to **70 caught, 0 missed** — eleven cases
about the lock and one about its registration in `.claude/settings.json`. **The case that matters
is *lock allows the librarian on a green gate*, and it runs against the real tree on purpose**: a
lock that refuses unconditionally passes every red case and is worse than no lock, and the sandbox
vault cannot be green. Cost: one gate run inside that suite.

> **Unproven, and it is the half that matters: that the harness fires it at all.** Hooks are read
> at session start, so nothing in the session that built it could show the matcher matching. The
> logic is proved; the wiring is not.

**The acceptance test after a restart is one move**, and it is written into the hook's own header:
break something trivial in the vault, attempt a librarian dispatch, see the refusal. A lock that is
silently absent looks exactly like a lock with nothing to say
([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]).

## Why the matcher names both tool words

`Agent`, renamed from `Task`, with the old name kept as an alias
([[the-dispatch-tool-is-agent-and-subagent-start-cannot-block]]). The matcher was pinned by a
selftest case rather than widened to `.*`
([[the-locks-matcher-is-pinned-by-a-selftest-case-rather-than-widened]]).

## It fired, 2026-08-20, and the unproven half is now proved

**The wiring holds.** A real dispatch of `vault-librarian` against a genuinely red tree was denied,
and the refusal carried the gate's four lines. **Proved twice** — once before the message fix below
and once after, the second run free because the tree was still red. The block above says the logic
was proved and the wiring was not; the wiring is proved now, and the tree that proved it was broken
by the owner's own file move rather than by a planted offender
([[a-tree-broken-for-a-real-reason-is-a-better-fixture-than-a-planted-offender]]).

**And it announced a command that does not exist.** `` `bash scripts/vault-check.sh` `` reached the
caller as `ash scripts/vault-check.sh`, in **both** the deny branch and the cannot-measure branch: a
backtick inside a double-quoted PowerShell string is an escape
([[a-backtick-in-a-double-quoted-powershell-string-is-an-escape]]). **It fired that way the one time
it has ever fired**, and the selftest case guarding the refusal was green throughout, because it
pinned the sentence rather than the command
([[a-selftest-case-can-pin-the-announcement-while-the-thing-it-announces-is-broken]]). Fixed by
doubling the backticks.

**Two properties it did not have on paper, both surfaced by that one firing:**

- **it deadlocks against the one-writer rule** when the gate is red *because of* `wiki/` content —
  the only sanctioned writer is refused by the one thing only it can clear
  ([[the-one-writer-clause-reaches-a-citation-and-not-only-a-register]]);
- **it hides the health of what it guards**, because it denies at `PreToolUse`, before the agent type
  is resolved ([[a-lock-on-a-red-tree-hides-the-health-of-what-it-guards]]).

**And one case of its suite is a hazard on a red tree**: `lock allows the librarian on a green gate`
prints `MISSED`, which reads as *the lock is broken*
([[the-green-gate-selftest-case-is-deferred-and-the-fixture-repair-cannot-reach-it]]).

# Its licence to refuse was re-argued when the rule behind it was struck — 2026-08-22

**This page took its licence from [[advisory-is-the-default-for-a-hook]] in the sentence naming it
the first hook here that refuses, and again in *It allows when it cannot measure*.** The owner
disowned that rule on 2026-08-21 and the page is retired
([[a-paraphrase-signed-owner-becomes-a-quote-and-is-reasoned-from-as-his-word]]). **Both stay as
written**; what follows is the argument redone, not the link swapped.

**Against the test that replaces it, the lock refuses and satisfies every condition**
([[a-hook-refuses-on-a-measured-condition-a-reliable-measurement-and-a-refusal-that-says-how-to-clear-it]]):

| the condition | this hook |
|---|---|
| the condition is measured rather than judged | `scripts/vault-check.sh` **exits a code**, and a code is not an opinion |
| the measurement is reliable where the hook stands | the hook runs the gate itself on `PreToolUse`, so the code is available at the moment of the dispatch |
| the refusal says how to clear it | the denial **carries the gate's own output**, which names each violation, so the caller is told what to fix |

**The allow-on-failure branch is this rule's own clause rather than a concession.** With bash not
findable the hook prints `THE LOCK DID NOT RUN` and exits 0 — *where it cannot measure, it allows
and says so aloud*. The struck page reached the same branch by a different argument, and **the
script is unchanged**: no case in `scripts/hook-selftest.ps1` turns over
([[a-refusal-is-possible-on-pretooluse-alone-and-the-register-is-a-test]]).

**What did not survive the re-argument is the word *irreversible*.** The section above prices a
librarian round trip to argue the act cannot simply be undone; that price is still true and is no
longer what licenses the refusal ([[agent-round-trip-cost]],
[[raw-holds-testimony-and-artefacts-are-frozen]]).

**The vocabulary a refusal is written in is a separate ruling and is untouched**
([[a-refusal-is-conditional-or-absolute-and-nothing-else]]): this lock is conditional, which is why
the denial carrying the gate's output is mandatory rather than optional. **That page is flagged for
the owner's ratification pass on its own grounds** — its `CONTRADICTION` block says the ruling it
states is not in the source it cites — and nothing here touches it.

# Its path scope is wider than the rule it enforces — 2026-08-29

**It fired on an `Edit` inside `archive/`, saying "you are writing to the vault's wiki".** The edit was
the one `sources:` citation rewritten during the archive-folder repair
([[the-archive-gains-a-folder-per-session-inside-the-date]]).

**The one-writer rule in `CLAUDE.md` names `wiki/` and the four registers, and does not name
`archive/`** — which `scripts/vault-archive.sh` writes mechanically on every move
([[the-one-writer-rule-covers-the-registers-too]]).

**So the hook guards a path the rule does not reach, and nothing says whether that is deliberate.** It
may be the right scope — an `archive/` edit by hand is worth a second look — but it is unstated, and an
unstated widening is how a hook's scope becomes the rule by default.

*(Compiled from `raw/handoffs/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds.md`.)*
