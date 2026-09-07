---
title: "A refusal is possible on `PreToolUse` alone, and the register of which hook refuses is a test"
type: concept
status: current
authority: refusal-event-bound
basis: code
sprint: S2
created: 2026-08-22
sources: ["archive/2026-08-21/2026-08-21-a-rule-the-owner-never-gave-is-struck-and-governs-learns-a-list/handoffs/2026-08-21-a-rule-the-owner-never-gave-is-struck-and-governs-learns-a-list.md", "scripts/hook-selftest.ps1", ".claude/settings.json"]
tags: [harness, agents, testing]
---

# The event bounds the question, and that is the finding

**`PostToolUse` fires after the act and `SessionStart` injects context into a session that has
already begun.** An exit code from either changes nothing that has not already happened, so neither
is a candidate for refusing however good its case
([[a-gate-that-refuses-work-without-an-open-sprint]],
[[the-dispatch-tool-is-agent-and-subagent-start-cannot-block]]).

**So the conversation the owner scheduled twice is smaller than it looked.** It is a decision about
the registrations on `PreToolUse` and about nothing else — not a policy for every hook in the tree
([[the-system-naming-which-hooks-block]], [[a-conversation-the-owner-scheduled-is-displaced-by-the-work-beside-it]]).

# What the register says, read from `.claude/settings.json` at this ingest

| event | matcher | script | disposition |
|---|---|---|---|
| `SessionStart` | `startup\|resume\|clear\|compact` | `session-brief.ps1` | speaks |
| `PreToolUse` | `Edit\|Write` | `ask-the-vault.ps1` | speaks |
| `PreToolUse` | `Agent\|Task` | `lock-the-librarian.ps1` | **refuses** |
| `PreToolUse` | `ExitPlanMode` | `check-the-plan.ps1` | speaks |
| `PostToolUse` | `ExitPlanMode` | `check-the-plan.ps1` | speaks |
| `PostToolUse` | `Write\|Edit` | `check-the-journal.ps1` | speaks |

**Exactly one refuses**, via `permissionDecision = 'deny'`, and it allows and says so aloud when its
measurement cannot run ([[the-librarian-lock-hook]]).

**The journal this was compiled from states the size of that table twice and the two readings
disagree** — *six registrations across two events, four scripts* in one section and *five hook
registrations across two events, four scripts* in another. **Measured against the file at this
ingest: the rows above, across three events, and one script is registered twice.** The journal is
not edited; `raw/` is immutable and what a session believed is data
([[fidelity-to-a-source-and-fidelity-to-the-tree]],
[[a-stated-count-drifts-from-the-list-it-heads]]).

# The register is a test, and the disposition is read off the script

**It lives in `scripts/hook-selftest.ps1`, on the owner's ruling of 2026-08-21, and never in prose
alone.** A sentence saying *no hook in this repository blocks* went false the day the lock landed
and stood for a further day, on a `decisions/` page and on [[session-hooks]] at once, because
checking it meant opening every script by hand ([[no-rule-reads-a-harness-file]],
[[a-copied-list-drifts-and-a-sweep-cannot]]).

The cases, and each asks a question the others do not:

- **the registered set matches the list in both directions** — a registration removed and a
  registration added are different failures, and this repository has met the first;
- **each hook refuses or speaks as listed**, decided by matching `permissionDecision = 'deny'` in
  the script rather than by asserting it in the list;
- **exactly one refuses and it is named**, so a second refuser arriving is a failure with a name;
- **no refusal is listed on an event that cannot deny**, which is the half that bounds the question
  above and is asserted rather than left as a thing everyone knows.

**Two of the four printed `MISSED` on their first run, both for real defects in the case code** — an
invalid character class, and a scalar indexed as an array while printing the right answer beside
itself. Both directions were therefore observed on the real tree
([[a-tree-broken-for-a-real-reason-is-a-better-fixture-than-a-planted-offender]]).

# What the test cannot decide

**Only the first condition of the refusal test is mechanical.** Whether a measurement is reliable
where the hook stands, and whether the refusal says how to clear itself, are judgements — so this
block asserts the disposition and never the reasoning
([[a-hook-refuses-on-a-measured-condition-a-reliable-measurement-and-a-refusal-that-says-how-to-clear-it]]).

*(Compiled from `raw/handoffs/2026-08-21-a-rule-the-owner-never-gave-is-struck-and-governs-learns-a-list.md`.)*

# The register gained a row, and the shape of the table is unchanged — 2026-08-22

**A row was added and nothing was removed.** Read from `.claude/settings.json` on this date:

| event | matcher | script | disposition |
|---|---|---|---|
| `PostToolUse` | `Agent\|Task` | `record-the-dispatch.ps1` | speaks — and cannot do otherwise |

**So the register stands at seven registrations across three events and six scripts**, with
`check-the-plan.ps1` still the one script registered twice. **Exactly one refuses**, and that is
unchanged: the new hook is on `PostToolUse`, which fires after the act
([[the-dispatch-record-hook]]).

**The number above is this date's reading and is not patched into the table further up this page** —
a figure is dated where it stands ([[the-region-coverage-figure-is-dated-where-it-stands]]). The
reading is `.claude/settings.json` and `bash`/PowerShell over it, never a sentence here
([[a-copied-list-drifts-and-a-sweep-cannot]]).

## It is the first row this page's own test admitted rather than described

**The register is a test in `scripts/hook-selftest.ps1`**, and the list there gained the new
registration in the same change as the hook. That is the property the test was built for: a
registration added and a registration removed are different failures, and the first had never been
met until this date.

**Nine cases were added and the suite reports `caught 123, missed 0`, from 114.** Read on a green
tree; a run taken while the vault gate is red reports one `MISSED` for the case that asserts the
librarian lock allows on a green gate, which is the known defect of that case and not a finding about
these ([[a-clean-run-cannot-test-an-advisory-exemption]] is the neighbouring shape; the green-gate
case is carried on `sprint.md` as an open item).

**The new hook's own cases assert what it may not do as well as what it does**: that the row names
the returned type, that it carries `-` rather than `no` in the pre-task column, that a dispatch with
no type is still recorded, that a row is written while the permission mode is `plan`, and that a
dispatch of any other agent type discharges nothing.

# The register-as-test shape earned its second payment inside a week — 2026-08-22

**The hook table went red the moment a registration was added without being listed.**
`.claude/hooks/record-the-dispatch.ps1` was registered on `PostToolUse` and the table inside
`scripts/hook-selftest.ps1` did not know about it, so the suite said so before anybody looked
([[the-dispatch-record-hook]]).

**That is what the shape was ratified for on 2026-08-21** — a list that is also a test cannot drift
from what it describes, where a sentence in prose can and does
([[a-copied-list-drifts-and-a-sweep-cannot]], [[a-stated-count-drifts-from-the-list-it-heads]]).

**And the prose about this register was the half that was wrong.** A journal stated the registration
count twice and differently, and both readings were wrong; **the table had all its rows**. The
argument the register was built on, turned against its own description.

# The same shape is now owed for the readers of `governs:` — 2026-08-22

**The count of parsers reading that field becomes a selftest case rather than a sentence on a page**,
on the owner's ruling of this date. Three exist, and the third was found by a red tree rather than by
anything that names them ([[the-count-of-a-fields-readers-lives-nowhere]],
[[the-governs-list-is-expanded-at-the-walk-and-the-address-verdict-asks-membership]]).

**Rejected: writing the number down.** A page arguing that separate parsers beat one shared copy is
unauditable while nothing says how many there are, and a stated count is the next thing to drift
([[a-rule-comparing-a-stated-count-against-its-list]]).
