# A run asserts what it expected to have happened, or its green is about nothing

**Draft proposal, prepared by the lessons agent on 2026-08-31 from `wiki/lessons/` as it stands.
Not written into the vault. The librarian decides whether it becomes a `wiki/proposals/` page and
what its `authority:` is.**

**The group, in one sentence:** eight live lessons are the same failure — a check, a suite or a
measurement reported a result while asserting nothing, and every one of the eight names the same
repair without any of them being obliged to build it.

## The group

| page | how the green was empty |
|---|---|
| `the-gate-can-stop-checking-and-go-on-exiting-zero` | the frontmatter pass never ran; the gate exited 0; the selftest scored `caught 162, missed 49` |
| `a-statement-starting-with-a-bare-word-is-a-command-call-in-powershell` | five cases never executed; neither counter moved; the suite printed `caught 169, missed 0` |
| `a-test-can-be-green-on-placeholders-its-own-setup-created` | the setup created the paths the assertion asked about; passed for six days |
| `a-planted-offender-is-proved-by-reading-it-back` | two plants silently did not plant; the run proved the tree was still green |
| `a-rule-with-no-instrument-behind-it-is-a-rule-a-fixture-can-violate-for-a-week` | nothing read the field, so the fixture violated the rule since 2026-08-22 |
| `a-fixture-pinned-to-the-end-of-a-file-expires-when-a-block-is-appended-below-it` | the case silently changed subject when a block was appended below its anchor |
| `measuring-a-copy-of-a-script-placed-somewhere-else-measures-nothing` | the copy found no destination, did nothing, and finished in 0.8 s |
| `a-process-is-measured-with-the-stdin-it-will-have` | measured without the stdin it always has; the figures were six times too small |

**All eight fail towards success.** Not one of them goes red when it breaks.

**Five of the eight already name the same instrument** —
`an-assertion-inside-a-measurement-harness-catches-a-broken-instrument`, which is in `archive/` and
therefore reachable by nothing that enumerates.

## What it would be

**A harness contract with three clauses, applied to every suite and every measurement wrapper in
`scripts/`:**

1. **A run asserts a positive total.** Not a fixed number — this store repairs a drifting count by
   deleting it, not by extending it — but a floor: *this run executed at least one case per
   dispatcher*, or *this run rewrote at least one file*. Zero is a broken instrument, never a
   result.
2. **A setup asserts that its setup took effect.** A plant is read back; a fixture that
   materialises a path declares which paths it created, and no assertion in the case may be about
   one of them.
3. **A run asserts its own channels are clean.** `vault-check.sh` already gained the case that
   stderr is empty; that clause generalises to every wrapper, and it is what catches the next tool
   that fails by printing to stderr and exiting 0.

## What it would take

- **`scripts/vault-check-selftest.sh`** — the floor assertion and the stderr assertion exist here
  already; what is missing is that they are a contract rather than two cases somebody wrote.
- **`scripts/hook-selftest.ps1`** — has the `$Error` binding-failure guard, which is clause 1 in a
  different disguise, and has no floor.
- **`scripts/session-dialogue-selftest.py`, `scripts/vault-measure-selftest.py`** — report
  `caught 52` and `caught 59`; whether either can distinguish a case that did not run from one that
  passed is unmeasured.
- **One `wiki/rules/` page** carrying the three clauses, with a `governs:` destination. That is a
  harness change and it is named plainly here rather than implied.

## What is open

- **Whether clause 1 can be written without a number in a file.** The store has ruled twice against
  an expected-total assertion, because a number in the file is a number every new case has to update
  (`a-statement-starting-with-a-bare-word-is-a-command-call-in-powershell`, its own repair section).
  A *floor per dispatcher* is derived rather than typed, but nobody has built it.
- **Which suites actually lack each clause.** The table above is what each page recorded on its own
  day; nothing has read the four suites against the three clauses in one pass, and that reading is
  what decides whether this is a note or a week.
- **Whether a rule page is the right carrier.** `every-rule-in-wiki-rules-owes-a-mechanical-instrument`
  means writing the page obliges an instrument for it, and the instrument for "every suite asserts a
  floor" is itself a sweep over `scripts/` that does not exist.
- **How many other cases carry a positional dependency.** `fixture-positional-dependency` says
  outright that the number is unmeasured and that it decides whether the repair is a note or a sweep.

## What it would oblige

- **A reading per suite, dated**, of whether it can tell a case that did not run from one that
  passed. That is the acceptance criterion and it is cheap.
- **The archived `an-assertion-inside-a-measurement-harness-catches-a-broken-instrument` gets a live
  carrier**, or five live lessons go on citing a page that nothing enumerating can reach.

## What it would retire

**All eight, on the narrow predicate** — a `rules/` page naming each slug is what
`scripts/lessons-queue.py` counts as `LANDED`, and today that number is 1 of 28.

**Two of the eight should be kept live rather than retired, and the draft says so:**

- `a-rule-with-no-instrument-behind-it-is-a-rule-a-fixture-can-violate-for-a-week` is cited from
  outside `lessons/` ten times, more than any other lesson in the folder. It is load-bearing prose
  and retiring it moves ten inbound citations into `archive/`.
- `a-process-is-measured-with-the-stdin-it-will-have` carries the 750–930 ms figure that the hook
  measurements of 2026-08-31 contradict. It is an open measurement, not a closed lesson.
