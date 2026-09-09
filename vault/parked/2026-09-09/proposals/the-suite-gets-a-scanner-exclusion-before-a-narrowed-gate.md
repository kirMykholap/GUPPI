---
title: "The suite gets a scanner exclusion before a narrowed gate"
type: proposal
status: current
authority: suite-cost-reduction
basis: human
sprint: S3
created: 2026-08-23
sources: ["archive/2026-08-23/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands/handoffs/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands.md", "scripts/vault-check-selftest.sh", "scripts/vault-check.sh"]
decided_by: [[the-suite-gets-a-narrowed-fast-mode-and-one-full-run-at-the-end]]
tags: [testing, harness, vault]
---

# The order is the proposal, and the first step is not a change

**Exclude the suite's sandbox path from the virus scanner before anything is rebuilt.** It costs
nothing, it is reversible, and it is a **measurement** rather than a change: the suite's `sys` time
exceeds its `user` time and eleven workers reach only a 1.7x speedup, which says the workers contend
on disk ([[the-gates-cost-grows-with-the-corpus-and-rule-pages-are-the-minor-term]],
[[the-parallel-floor-bounds-any-further-speedup]]).

**Do it first because it tells you whether the second step is worth doing.** If the file I/O is the
scanner, the redesign below buys much less than the arithmetic suggests, and it will have been
designed against the wrong bottleneck ([[measure-before-optimising-and-count-processes-not-pages]]).

# The second step, and what it costs

**Give `scripts/vault-check.sh` a way to run one rule.** Counted 2026-08-23: 102 of the cases break
exactly one thing and evaluate all twenty rules, so most of every run is spent re-deciding questions
the case is not about ([[the-selftest-is-a-mutation-test-of-the-gate]]).

**The thirty `run_clean` cases must keep running the whole gate.** *Nothing anywhere went red* has no
single rule to narrow to; narrowing one would change what it asserts
([[a-clean-case-built-on-a-helper-that-plants-a-red-tree-can-never-be-green]]).

# The cost, stated now rather than discovered later

**Running all twenty rules gives every case incidental coverage that nobody designed and nobody
watches.** A case about rule 10 has been quietly proving that rules 1 through 20 stay quiet on its
fixture; narrowing removes that, silently, on the day it lands.

**This store has already paid for a silent loss of coverage once** — a case that passed for a reason
nobody chose ([[a-case-that-fails-for-its-own-reason-tests-nothing-either]]). Naming the price here
is the whole reason the second step is written down rather than done.

# What is open

- **how a narrowed case declares which rule it wants**, and whether the flag is a rule number, which
  this corpus deliberately writes in prose rather than in a title
  ([[a-retired-rule-number-is-never-reused]]);
- **whether the incidental coverage is worth replacing** with a small number of cases that
  deliberately run everything, or worth letting go;
- **what the exclusion actually buys**, which is unknown until step one is run.

# Step one was applied on 2026-08-24 and the measurement failed — this stays a proposal

**The owner applied the antivirus exclusions.** **What they bought is still unknown**, and this page
does not become `implemented`: its second step is untouched and all three open questions stand.

**Why the measurement says nothing.** Three runs of `bash scripts/vault-check.sh` on an unchanged
tree gave **25.3, 16.2 and 19.3 seconds real** — a spread larger than the effect being looked for —
and `vault-check.sh` was the wrong subject from the start, because it reads the vault and builds no
sandbox. The suite run that *was* the right subject had the hook selftest twice, the gate three
times, the injector twice and two commits against the same disk while it ran
([[a-measurement-taken-while-other-work-runs-against-the-same-disk-measures-nothing]]).

**The one surviving reading is a ratio that did not move**: `sys`/`user` was 2.16 before and 2.19
after, which is what you would expect if the exclusion did nothing — **and it is not evidence**,
because concurrent work inflates both terms.

**A clean re-measurement costs 34 minutes at full idle** and is takeable at the start of any
session. It has not been taken.

# The second step is ordered rather than proposed — owner, 2026-08-24

> **owner: стоит все таки уменьшить время его работы**

**About `scripts/vault-check-selftest.sh`, which now costs 34m8s at 562 files against 27m15s at
543.** This page's second step is already *a narrowed gate*, so **a new proposal was rejected**: it
would duplicate the argument this one carries
([[no-new-entity-where-an-existing-one-can-carry-the-claim]]).

**It is raised for discussion in the next session**, on his instruction — the narrowing's price is
already written above, and the discussion is about paying it
([[the-selftest-is-a-mutation-test-of-the-gate]]).

# The owner answered the objection this page records, 2026-08-24

**This page names the loss of incidental coverage as a flat cost of its second step and offers no way
to get it back.** He supplied one: **a fast narrowed run inside the loop, and one full end-to-end run
at the end**, so the price becomes *you find out later* rather than *you never find out*
([[the-suite-gets-a-narrowed-fast-mode-and-one-full-run-at-the-end]]).

**Step one is taken and step two waits for a measurement** — which now exists and points against it:
the gate is one shared pass over the corpus plus two delegated scripts, and the shared pass is two
thirds of the cost, so narrowing to one rule cannot buy what the rule count suggests
([[the-gate-is-a-shared-pass-over-the-corpus-plus-the-scripts-it-delegates-to]]).

**And the page's cost paragraph is left as it was written.** It was right about what narrowing
loses; what it lacked was the recovery.

# Carried again, 2026-08-25

> **owner:** «пока что не трогаем, обсудим на следующей сессии»

**The suite's 37m44s reading and the forty-per-cent machine drift stay untouched.** Nothing was
measured, narrowed or excluded on this date.

**The reading that stands beside it**: the suite runs the gate about 171 times against a 34m8s total,
so anything added to the gate is multiplied by that
([[the-gate-flag-fork-is-recorded-and-nothing-is-built]],
[[a-control-nothing-touched-separates-a-change-from-the-machine]]).

# The owner says the exclusion measurement is done and gave nothing — 2026-08-26

**The owner said the measurement had already been done and had given nothing.** *(Recorded in the
journal as the session's English rather than as his words, so it is not signed as a quotation* —
[[a-block-attributed-to-the-owner-is-written-in-his-own-russian]].*)*

**So this page's ordering — *exclusion and measurement first, then narrowing* — no longer describes
anything that is waiting.** Step one is not pending; it is spent.

**The result is on no page**, which is how a session of 2026-08-26 came to build a caveat about the
ordering on this page and have the caveat be false. **The next session would have proposed the
measurement a third time**
([[a-negative-measurement-that-is-not-written-down-gets-proposed-again]]).

**What this page already carried is a *failed* measurement — 25.3, 16.2 and 19.3 seconds, a spread
larger than the effect.** A failed measurement and a settled negative are different states, and only
the first was written here.

**The second step is what remains**, and it is now the smoke runner's blocker rather than an
optimisation of the suite: `scripts/vault-check-selftest.sh` needs a narrowing flag that does not
exist ([[the-smoke-runner-is-built-first-thing-next-session]],
[[the-suite-gets-a-subset-mode-that-issues-no-verdict]]).

**And the frame has moved under it.** The suite no longer runs every session
([[the-suite-stops-running-every-session]]), so the cost this page is about is paid once a sprint —
which changes what narrowing is worth ([[a-proposal-must-be-rechecked-when-the-frame-changes]]).

*(Compiled from `raw/handoffs/2026-08-26-the-gate-hangs-on-a-store-stub-and-the-checks-get-their-names.md`.)*
