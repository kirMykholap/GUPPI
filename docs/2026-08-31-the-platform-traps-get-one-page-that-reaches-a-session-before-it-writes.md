# The platform traps get one page that reaches a session before it writes

**Draft proposal, prepared by the lessons agent on 2026-08-31 from `wiki/lessons/` as it stands and
from `raw/handoffs/2026-08-31-the-families-become-rules.md`.
Not written into the vault. The librarian decides whether it becomes a `wiki/proposals/` page and
what its `authority:` is.**

**This proposes a change to files that instruct an agent** — a new `wiki/rules/` page with a
`governs:` destination in the harness — and it says so plainly rather than describing the effect
and leaving the mechanism implied.

**The group, in one sentence:** five live lessons are properties of the interpreter or the
operating system that no reading of the source reveals, that every one of them cost a session or a
day, and that a reader only meets if he happens to grep `lessons/` before writing the line that
walks into one.

## The group

- `a-script-must-not-be-edited-while-it-is-running` — bash reads a script lazily by byte offset, so
  appending a comment to a backgrounded suite killed the run at a line the edit never touched.
- `backgrounding-a-task-that-reads-standard-input-is-what-hangs-it` — two PowerShell processes
  lived 330 minutes on under half a second of CPU; the same suite with `< /dev/null` finished in
  seven minutes. **The owner lost most of a day to it, twice.**
- `grep-q-on-the-right-of-a-pipeline-under-pipefail-inverts-the-test` — `grep -q` exits on its
  first match, the upstream process dies of `SIGPIPE`, and under `pipefail` the test comes back
  false exactly when the pattern matched. `shellcheck` does not warn.
- `a-statement-starting-with-a-bare-word-is-a-command-call-in-powershell` — `LedgerText -match "x"`
  is a command invocation, not a comparison; five cases never executed and the suite reported
  `missed 0`.
- `an-assertion-anchored-at-end-of-line-fails-against-platform-newlines` — an end-of-line anchor in
  a CRLF file sits after the carriage return, so a correct mechanism was reported as a miss.

**And a sixth, from the journal of 2026-08-31**, which this draft assumes the librarian is
compiling: `pathlib.write_text` on Windows translates `\n` to `\r\n` unless given `newline="\n"`,
so a generated list of paths carried the carriage return **inside each filename** and
`scripts/vault-archive.sh` refused the first item with `no such file`.

**That sixth is wider than `write_text`.** Preparing this draft, the lessons agent piped
`scripts/lessons-queue.py --slugs` into `comm` and got an empty intersection where five entries
exist — Python's stdout on this host is CRLF and `comm` compared `slug\r` against `slug`. Same
platform fact, third mechanism, and it produced a **false negative that read as a clean result**.

## What it would be

**One `wiki/rules/` page, `governs:` a harness file, carrying the traps as clauses a session meets
before it writes rather than after.**

The candidate destination is the repository's own `CLAUDE.md`, which already carries four rendered
regions. The alternative is `.claude/rules/`, alongside `ast-boundaries.md`. **This draft does not
pick**, because which file a rule is rendered into is a decision with a target, and
`a-decision-declares-its-target` applies.

**What travels is the trap and the one-line avoidance, never the incident.** Five clauses of two
lines each. The measurements, the citations and the story stay on the lesson pages, which is what
the `<!-- text -->` slice is for.

## What it would take

- **One `wiki/rules/` page** with `governs:`, a marked slice, and `decided_by:` naming the decision
  that caused it — required in `rules/` and refused by the gate without it.
- **One `wiki/decisions/` page** naming the destination.
- **A row in `authority.md` in the same pass**, or rule 13 reddens and
  `lock-the-librarian.ps1` locks out the only party who may write the row.
- **An instrument, or a page saying why there cannot be one.**
  `every-rule-in-wiki-rules-owes-a-mechanical-instrument` is live and reaches this.

## What is open

- **Whether a rendered rule is the right carrier for a trap.** A rule reaches a file whether anyone
  came looking or not, which is exactly the property these five need — and the cost is startup
  budget on a corpus already measured at ~13,000 tokens loaded before the first prompt
  (`the-corpus-is-mostly-about-itself-and-the-owner-noticed-before-any-instrument-did`). Five
  clauses is small; the precedent is not.
- **Whether any of the five can have a mechanical instrument instead.** Three plausibly can:
  a `PreToolUse` refusal on a background launch without a redirected stdin; a `shellcheck`-style
  sweep for `grep -q` at the right of a pipeline under `pipefail`; a sweep for `write_text` without
  `newline=`. A rule with an instrument behind it is worth more than a rule a reader must remember.
- **Whether the CRLF clause belongs here or on the existing CRLF lesson.** This draft's own
  recommendation, stated in the return to the librarian, is that the writing side extends
  `an-assertion-anchored-at-end-of-line-fails-against-platform-newlines` rather than becoming a page.
  If it extends, the rule renders one clause from a page it does not retire.
- **Whether the group is five or nine.** `powershell-backtick-escape`, `msys-signal-reach`,
  `console-encoding` and `exit-code-through-a-pipe` are the same kind and are not in `lessons/`.
  Nobody has read the shell family whole.

## What it would oblige

- **A dated startup-cost reading before and after.** The one number this store has about its own
  overhead is a total, and adding to what loads before the first prompt without measuring it is the
  shape the corpus-self-reference lesson exists to prevent.
- **The rule renders, and the gate's rules 11 and 12 read both ends** — so the page cannot be
  edited without `vault-inject.sh` running, and a session that forgets leaves the gate red.

## What it would retire

**All five, and the sixth if it becomes a page rather than an extension.**

**One of the five should be checked before it goes.** `a-script-must-not-be-edited-while-it-is-running`
carries a dated negative half added 2026-08-30 — that editing a repository file *while the selftest
runs* is safe, because the suite snapshots the tree into `$PRISTINE` at line 165. A two-line clause
that keeps the prohibition and drops the correction would re-file the false claim the page exists to
have struck.
