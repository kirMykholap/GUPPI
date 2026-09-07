---
title: "Advisory is the default for a hook, and refusing needs an irreversible action and a refusal that cannot be wrong"
type: decision
status: deprecated
authority: hook-blocking-default
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-19
created: 2026-08-20
sources: ["archive/2026-08-19/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery/handoffs/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery.md", ".claude/hooks/ask-the-vault.ps1"]
tags: [harness, agents, process]
superseded_by: [[a-hook-refuses-on-a-measured-condition-a-reliable-measurement-and-a-refusal-that-says-how-to-clear-it]]
---

> [!CAUTION] CONTRADICTION
> Also answered by
> [[a-hook-refuses-on-a-measured-condition-a-reliable-measurement-and-a-refusal-that-says-how-to-clear-it]],
> which states a different test on the owner's ruling of 2026-08-21 that this page's rule was never
> his. Unresolved: retiring this page and re-pointing the pages that cite it is a scheduled step and
> was deliberately not performed at the ingest that marked this.

# The ruling, 2026-08-19

> **owner: advisory is the default for a hook.** A hook may refuse an operation only where the
> action is **irreversible** *and* the refusal **cannot be wrong** — both conditions at once.

**No hook in this repository meets both today**, so every one of them speaks and none blocks
([[session-hooks]], [[the-journal-gate-hook]]).

**Rejected: leaving it to whoever writes the next hook.** That is what had been happening. The
guard built on 2026-08-19 chose advisory with nothing behind the choice — no `decisions/` page
ruled on it, and what existed was `entities/session-hooks.md` recording *"Advisory: it never blocks
and always exits 0"* with `basis: code`, which says what a script does and not what was decided.
**A description of behaviour cannot be inherited as a policy**, and the session's own choice was
reported as unbacked before this ruling closed it.

## Why the test has both halves

**Irreversibility alone would license a refusal that is sometimes wrong**, which is the alarm this
project already knows not to read: a gate that fires when nothing is wrong is one a reader learns to
step around, and stepping around it is how the guard stops being a guard.

**A refusal that cannot be wrong is not on its own worth the machinery** if the operation can simply
be undone. Both together name a narrow class, and the store's only designed refuser —
[[a-lock-on-the-librarian-dispatch]] — is the one candidate that has ever been drawn.

## What is deferred, and it is deliberate

**The precise system naming which hooks block is a separate conversation**, and the owner asked for
it to be written down rather than settled in passing: «нужно будет обсудить что блокирует а что
нет. Запишем на будущее» — 2026-08-19. **The conversation is owed, not the answer.** What it has to
cover is which hooks refuse an operation and which only speak, and **on what test the difference is
decided**.

**Not doing it leaves every hook's blocking behaviour a per-hook choice made by whoever writes it** —
which is the state this ruling narrows rather than ends. The design sits in
[[the-system-naming-which-hooks-block]].

## What it obliges

- **A new hook is advisory unless its page argues both conditions.** The argument is on a page, not
  in the script's header ([[no-rule-reads-a-harness-file]]).
- **`entities/session-hooks.md` keeps recording behaviour**, and this page is where the policy is
  read from. The two answer different questions and the entity page says so.

## The first hook that refuses was built 2026-08-20, and it meets both conditions

**`.claude/hooks/lock-the-librarian.ps1`** denies a librarian dispatch while `vault-check.sh` exits
non-zero ([[the-librarian-lock-hook]]).

**The act is irreversible enough**: a librarian round trip costs fifteen to thirty minutes and
writes sidecars keyed by line number, so an ingest against a broken input cannot simply be re-run
([[agent-round-trip-cost]], [[raw-holds-testimony-and-artefacts-are-frozen]]).

**And the refusal cannot be wrong**, because the condition is *measured* rather than *inferred* —
and where it cannot be measured the hook allows: if bash is not findable it prints
`THE LOCK DID NOT RUN` and exits 0. **Refusing on a measurement that never happened is exactly what
this page forbids**, so the allow-on-failure branch is this rule's own consequence rather than a
concession.

**The vocabulary a refusal is written in was ruled the same day**
([[a-refusal-is-conditional-or-absolute-and-nothing-else]]): conditional, naming its condition, or absolute with no
appeal. This lock is conditional, and it is the reason the denial carrying the check's output is
mandatory.

**What is still not enumerated is the system**: which hooks refuse, on what test, recorded where
([[the-system-naming-which-hooks-block]]).

# Applied to the pre-task surfaces — 2026-08-20

**`.claude/hooks/check-the-plan.ps1` and the write net in `.claude/hooks/ask-the-vault.ps1` are both
advisory, decided by this page** ([[the-plan-check-hook]]).

**The test fails on its first half.** Exiting plan mode is **reversible** — you can plan again — so
`irreversible` is not satisfied and the second condition never gets its turn.

**Rejected: denying `ExitPlanMode`, on the argument that this particular refusal costs nothing.** A
plan is cheap to re-present, so the price of a wrong refusal here is a minute. **Cheapness is a
temptation rather than an argument**: the `irreversible` clause is a limit on what a hook may
decide, not a price to be weighed against the benefit. Accepting the cheap case would leave the
default with no boundary except the size of the inconvenience.

**No hook in this repository blocks, and the set has grown since this page was written.** What
enumerates it is still nothing ([[the-system-naming-which-hooks-block]]).

# The owner disowned this rule and struck the page — 2026-08-21

> **owner: не было такого правила. Это правило неправильное.**

**The quote block above is not a quotation.** Its words are the English paraphrase a session wrote
into `raw/handoffs/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery.md`
under `owner:`, compiled here as his testimony and stamped `basis: human`
([[a-paraphrase-signed-owner-becomes-a-quote-and-is-reasoned-from-as-his-word]]).

**Nothing on this page is edited and nothing is removed.** What it decided, it decided, and three
pages took their disposition from it while it stood; that history is the reason it is kept whole
([[what-an-archived-page-asserts-is-frozen-and-how-it-is-found-is-live]]).

**The replacement is
[[a-hook-refuses-on-a-measured-condition-a-reliable-measurement-and-a-refusal-that-says-how-to-clear-it]]**,
ratified the same day and giving the same answers on the tree for grounds that can be checked.

**A second sentence on this page went false before the strike, and by measurement.** *"No hook in
this repository blocks"*, at the foot, stood against this page's own preceding section naming
`.claude/hooks/lock-the-librarian.ps1` as built and refusing. It went false the day the lock landed,
2026-08-20, and stood for a day. **What made it uncheckable was that nothing enumerated the hook
set** — the enumeration is now a test
([[a-refusal-is-possible-on-pretooluse-alone-and-the-register-is-a-test]]).

**The retirement itself is owed and is not this note.** Setting `status: deprecated`, writing
`superseded_by:`, moving the page to `archive/` and re-pointing [[the-plan-check-hook]],
[[the-librarian-lock-hook]], [[session-hooks]] and
[[the-guard-branch-lives-inside-a-hook-that-already-runs]] is the first step of an approved plan and
belongs to the session that executes it.

*(Marked at the ingest of `raw/handoffs/2026-08-21-a-rule-the-owner-never-gave-is-struck-and-governs-learns-a-list.md`.)*
