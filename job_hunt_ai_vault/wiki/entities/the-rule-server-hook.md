---
title: "`serve-the-rule.ps1` — the hook that hands over the rule governing the file being written"
type: entity
status: current
authority: rule-server-hook
basis: code
sprint: S3
created: 2026-08-30
sources: [".claude/hooks/serve-the-rule.ps1", ".claude/settings.json", ".claude/hooks/pre-task-state.ps1", "archive/2026-08-30/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md"]
tags: [harness, agents, vault]
---

# What it is

**Appeared 2026-08-30**, registered on `PreToolUse` with the matcher `Edit|Write`. 198 lines of
PowerShell, like every hook here ([[session-hooks]]). It prints a note naming the rule pages that
govern the file about to be written, with the path of each page, and **it never refuses**: an edit is
reversible and a rule that merely governs a file is not a reason to stop one.

**What it replaces:** until this day a prohibition reached a reader only if that reader ran
`/pre-task` and read `wiki/decisions/` whole. This is the other delivery — the rule arrives when the
file it governs is touched, and nothing has to be remembered or enumerated to get it
([[a-rule-differs-from-a-prohibition-by-having-an-address-and-by-nothing-else]]).

# How it decides what to say

**One pass over `wiki/rules/`, reading only the first thirty lines of each file.** Seventeen files
today and perhaps seventy after the family rules land. Reading them whole was measured at roughly
200 ms of the run, and everything it needs is in the frontmatter.

**A generated table was rejected** — a second artefact that can disagree with the tree is the drift
this store repairs rather than creates. The owner reads the same list as a `pages.base` view; the
hook reads the folder.

**A page whose `status:` is not `current` is skipped.** A `deprecated` or `repealed` rule is the text
that *was* true, and handing it over as current is worse than handing over nothing.

**It says a thing once per file per session.** The ledger carries a `ServedRuleFiles` field and the
hook appends a `served-rule` event ([[the-pre-task-ledger]]). **The folder is scanned before the
ledger is opened, and that order was measured rather than chosen**: deriving the ledger state costs
more than reading seventeen file heads and would be paid on every write, including the majority that
govern nothing. If the ledger cannot be read the note is said again, which is the safe direction.

# The one silence, and it is by path

**A write inside `wiki/` or `archive/`, or to any of the six registers, produces nothing.** That is
the librarian doing its job, and serving it a rule about the page it is writing is noise on every page
of an ingest.

**It is scoped by path because it cannot be scoped by agent.** Hooks declared in `settings.json` do
reach subagents — proved in this repository on 2026-08-20
([[hooks-in-the-settings-file-apply-inside-subagents]]) — and there is no documented way to exclude
one. An agent's own frontmatter can add hooks and cannot remove them. The pre-task net already uses
the same shape to stay out of the vault ([[the-vault-is-excluded-from-the-pre-task-net]]).

# The `authority:` half is not written, and the journal says otherwise

**The hook's own header describes a second matcher — by `authority:`, for pages under `wiki/`, "the
half that covers 580 pages no mechanism reached before" — and calls it "implemented here and
DORMANT", waiting only on a `Read` matcher.**

**Read off the file: `$slug` is assigned at line 123 and never read again.** The only match is a path
equality test against `governs:` at line 145, and the record it appends carries `Kind = 'governs'`.
There is no second branch to be dormant.

**Two consequences follow, and both matter:**

- **a page under `render: authority` cannot be served by this hook at all**, because the only matcher
  it has keys on `governs:` and such a page is forbidden to carry one
  ([[a-rule-under-render-authority-is-written-into-no-file-and-found-by-its-slug]]);
- **the silence above would swallow the half anyway** — every path under `wiki/` exits at line 86, so
  a `Read` matcher wired today would serve nothing for any page in the store.

**This section is `basis: code` and it disagrees with the journal it was compiled beside.** What is
owed is the branch, and the `Read` matcher is downstream of it
([[the-hooks-authority-branch-is-not-written-and-the-read-matcher-is-downstream]]).

# What it costs

**750–930 ms through a pipe**, against 941 ms for the existing `ask-the-vault.ps1` under the same
load, and 359 ms for a bare spawn. **The 99 ms and 141 ms figures the design was decided on are
void** — they were taken without stdin, which is a shape this hook never runs in
([[a-process-is-measured-with-the-stdin-it-will-have]]).

**The write path fires 71 to 108 times in a working session.** How often `Read` fires has never been
measured by anyone, which is why that matcher is deferred rather than added.

# Why a file of its own

**`ask-the-vault.ps1` is a chain that picks exactly one note, by its own design**, and this mechanism
must be able to speak on the same edit that trips one of those. It also needs a `Read` matcher that
script does not have, so it is a separate `settings.json` entry whatever happens. And if the lookup
breaks, the pre-task net keeps working ([[the-rule-server-is-a-hook-of-its-own]]).

# What changed on 2026-08-31: the dormant half is written, and every section above is dated

**198 lines became 297.** The sections above describing a single `governs:` matcher, a silence by path
alone, and an `authority:` half that "is not written" were true on 2026-08-30 and are false from this
day. They stand as the record of a mechanism whose journal and whose code disagreed.

**It reads two things it never read: `render:` and `tool_name`.** A page under `render: authority` is
matched on the `authority:` slug of the file being touched, **exactly, with no resolution through
`job_hunt_ai_vault/authority.md`** — the owner refused that resolution, so the family register stays an
instrument of the cleanup rather than a runtime dependency
([[the-hook-matches-the-exact-slug-and-resolves-nothing-through-the-register]]). **`paths:` was removed
from the file entirely**, having been the field the refused matcher would have keyed.

**The silence is scoped by mode as well as by path.** Silent on `Edit|Write` inside `wiki/`, speaking
on `Read` there, silent in `archive/` and on the six registers in both directions, and exiting at once
on a `Read` outside the vault — so each half fires on exactly one mode. The write silence exists so the
librarian is not served a rule about every page of an ingest; the read speech exists because a slug
lives only where the write path is silent. **The owner's own ground**: one almost always searches first
and acts afterwards, so the search is where a rule can catch you.

**`.claude/settings.json` registers it on `Read`**, a second entry beside the `Edit|Write` one. That
registration is what makes the `authority:` half reachable at all.

**The note it prints branches by delivery kind** — a `governs:` hit says the text is rendered into this
file and the page is where it is changed; an `authority:` hit says the opposite, because a lookup rule
renders nowhere.

## The cost did not rise when the folder doubled, and this entity cannot say why

**389–478 ms on the write path and 392–450 ms on the read path, with 36 pages in `wiki/rules/`**,
measured through a pipe on 2026-08-31. The figure recorded above for 17 pages is **750–930 ms**. The
plan had predicted roughly a doubling at seventy pages and the folder doubled with no rise at all.
**One of the two readings was taken in conditions the other was not, and this session did not find out
which** ([[a-process-is-measured-with-the-stdin-it-will-have]]).

**And `Read` is not the most frequent tool call, which is the premise the matcher was deferred on.**
Counted across every transcript this project has: Bash 5088, Edit 1102, Read 490, Agent 395, Write 392,
Grep 49. It is the fourth and about a third of the `Edit|Write` path, because this repository reads with
`cat` and `grep` ([[the-hooks-authority-branch-is-not-written-and-the-read-matcher-is-downstream]]).

**Five cases in `scripts/hook-selftest.ps1` cover the new branch**, and the suite with its registration
census reports `caught 229, missed 0`.

*(Compiled from `raw/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md` and from the file itself, and extended at the ingest of `raw/handoffs/2026-08-31-the-families-become-rules.md`.)*
