---
title: "A file class is pinned to LF after it costs something, never before"
type: decision
status: current
authority: line-ending-widening
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-17
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-the-ritual-gets-a-retro/handoffs/2026-08-17-the-ritual-gets-a-retro.md", ".gitattributes", "archive/2026-08-19/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell/handoffs/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell.md"]
tags: [process, harness]
---

# Decided 2026-08-17: `*.ps1` and `*.json` join the pin, and the rule for joining is stated

`.gitattributes` now pins `*.sh`, `*.md`, `*.ps1` and `*.json` to LF. **Each pattern was added after
a specific cost, and none before:**

| pattern | what it cost first |
|---|---|
| `*.sh` | CRLF breaks a shebang in the container |
| `*.md` | `awk` and `bash` parse the vault's markdown ([[markdown-is-pinned-to-lf]]) |
| `*.ps1`, `*.json` | an edit script's LF anchors matched nothing in a CRLF file, 2026-08-17 |

**Rejected: pinning every text class up front.** That is the widening refused on 2026-08-16 on blast
radius, and the ground has not changed: `tests/` holds parser fixtures whose bytes are not changing
inside a commit about line endings.

## What the pin actually changes, which is not the repository

**The index already held LF for all of them.** So the pin changes nothing about the repository and
everything about the **working copy** — which is what a script editing those files reads. That
asymmetry is the reason a line-ending pin looks like a no-op in `git diff` and is not
([[the-stale-stat-cache-behind-git-status]],
[[line-endings-make-git-status-overstate-what-changed]]).

Measured the same day: four working copies converted, and `hook-selftest.ps1` re-run against them —
**40 of 40, unchanged**.

## Still unpinned, and named so the next edit has it in front of it

**`*.coverage.tsv`.** The sidecars have already been broken once by a CRLF rewrite — 317 of 411
verdicts turned into `BAD VERDICT` lines — and `vault-coverage.sh`'s own CR strip is the only thing
standing between that and a red gate. That is the weaker of the two places to fix it: the strip is
one script's defence, and the next tool to read a sidecar starts without it.

## `*.base` is the next class, and it is deliberately not pinned — 2026-08-17

`pages.base` arrived at the vault root ([[pages-base]]) and git warned **"LF will be replaced by
CRLF"** on the first `git add`, because `.gitattributes` says nothing about `*.base`.

**Left unpinned on purpose, by this page's own rule**: the class has cost nothing. Obsidian reads
either ending, and **no script reads the file at all** — the agent-facing list is printed by
`scripts/vault-catalogue.sh` instead. There is no byte comparison anywhere near it, which is what
made `*.md` and `*.ps1` earn their lines.

Recorded so the next reader meets that warning already explained rather than cold, and so that the
day something does read the file, the pin is a one-line decision with its reason already written.

## Two readings taken 2026-08-19, and neither changes the rule

**`*.yaml` is unpinned, and the six `_schema.yaml` files will convert to CRLF on the next checkout**
([[the-per-folder-frontmatter-schema]]). **Measured: the `awk` parse is CR-clean on this host and the
gate stays correct**, so by this page's own rule the class is not pinned. The measurement is what
makes the first failure answerable rather than a fresh investigation.

**`*.coverage.tsv` converts on every ingest now, by construction.** The warning named above fired
again on the very next one — *"LF will be replaced by CRLF the next time Git touches it"*, on the
sidecar of 2026-08-18 — and it still cost nothing: `vault-coverage.sh` read that sidecar and reported
`94 of 94 units, INGEST COMPLETE`, exit 0, with the file already written LF and about to be converted.
**So the rule still says do not pin it.** What has changed is the shape of the exposure: this is no
longer *"three files have been converted"* but *a class that converts on every single ingest*, and
**the first failure will therefore arrive on a sidecar nobody is watching.**

**A third reading belongs beside these, because it is the other half of what a pin does.** The pin
protects the committed blob and not the working copy, and `git status` reports nothing when they
differ — one file in `raw/` is CRLF in all 337 of its lines on disk against a clean LF blob
([[the-lf-pin-protects-the-blob-and-git-status-is-silent-about-the-working-copy]]).

## `*.yaml` re-read with the right instrument, and the rule still says do not pin — 2026-08-19

**The reading above was taken as a prediction; this one is taken after a `git checkout`.** Measured by
**counting CR bytes** rather than by `grep`, which this store has already recorded returning a line count
instead ([[grep-with-an-escaped-cr-returns-a-line-count-and-not-a-cr-count]]):

| what | CR bytes |
|---|---|
| each of the six `_schema.yaml` after `git checkout --` | **29–30** |
| the blob at HEAD | **0** |
| the files as written by a bash tool | **0** |

**`.gitattributes` pins `*.sh` and `*.md`, and names the exact reason for the second** — *"parsed by awk
and bash, on the host and in the container alike: a CR is a byte inside the field, not a line ending"* —
**and `_schema.yaml` is parsed by that same awk**, in `vault-check.sh`'s schema loop
([[the-per-folder-frontmatter-schema]]). That is the closest a class has come to this page's trigger
without meeting it.

**Reported and not acted on, because it has not cost anything yet.** Measured the same turn:
`bash scripts/vault-check.sh` exits 0 and prints `ok` with all six schemas in CRLF, so the parser
tolerates it today. **What it did cost is diagnosis time**, which is not the gate's correctness and is
explicitly not offered as the trigger — a class pinned for costing an investigation would pin every
class, since every class costs one the first time.

**This is a third class arriving at this rule and not being pinned**, after `*.base` and `*.coverage.tsv`.

# The policy fired on a fourth class — 2026-08-19

**`*.yaml` was the one extension left out of the pin**, and it was left out for a dateable reason:
`.gitattributes` pinned `*.sh`, `*.md`, `*.ps1` and `*.json` on 2026-08-17, and the six
`_schema.yaml` files were created on 2026-08-19.

**It cost the same debugging pass the file's own comment describes.** A `git stash push` / `pop`
round-trip turned all six schemas CRLF, and an edit script's LF anchors then matched nothing.

**Pinned the same day, and ratified by the owner afterwards** — which is the wrong order and is
recorded as a divergence ([[the-yaml-class-is-pinned-to-lf]],
[[the-yaml-pin-was-written-before-the-owner-ratified-it]]).

**One reading of this policy needed correcting.** The schemas' entity page had recorded on the same
day that the class was **not** pinned because *"the awk parse is CR-clean on this host"* — a true
measurement that is not a safety argument, because the host is not the container
([[no-cr-reaches-awk-on-this-host-and-the-container-is-where-it-bites]]). **This policy is about
what a class has cost, not about whether the current host can see the defect.**

## `*.tsv` joined the pin at `6fe25cd`, and the pin was proved on a new file rather than assumed

**What it governs is the working copy on checkout**, which is the half the scripts read. Measured at
byte level: a planted `.tsv` carrying two CR bytes in the working copy enters the index with **zero**.

**The existing coverage sidecars needed nothing** — `core.autocrlf` had normalised them on the way
in, which is what this file's own `.ps1`/`.json` reasoning already says about that class.

**The alarm that produced the pin was a broken instrument talking.** `LC_ALL=C grep -c $'\r'`
reported 97 CR bytes in a sidecar and 81 in a `_schema.yaml`; both are zero, and the escaped CR had
not survived into the grep, so the pattern matched every line and returned a **line count**
([[grep-with-an-escaped-cr-returns-a-line-count-and-not-a-cr-count]]). **The pin is still correct,
and the cost that justified it was real** — `vault-coverage.sh` carries its own CR strip because git
once rewrote every sidecar to CRLF and turned 317 of 411 verdicts into `BAD VERDICT` lines. **What
was false was the report that it had happened again.**

# The list stops being the mechanism: `* text=auto eol=lf` becomes the default — owner, 2026-08-26

*(the owner ruled it, against extending the class list a fifth time.)*

**`.gitattributes` gains `* text=auto eol=lf` at the top, and every block below it stays exactly as
written.** They stop being the mechanism and become the record of what each class cost — deleting
them would delete the only evidence for the new line.

**This is a departure from this page's rule and it was taken deliberately, not by oversight.** The
principle here is written against pinning **one** class speculatively. A default is the other shape:
it inverts the question from *which classes to pin* into *which to exempt*, and its own cost is on
the counter four times over — `*.ps1`, the six `_schema.yaml`, `*.tsv`, and `Makefile`, each found the
expensive way. **The defect was never a missing class. It was that a per-extension list has holes by
construction and nothing enumerates them.**

**Measured 2026-08-26, before the line landed:**

- **40 tracked files carried no eol attribute at all.** Two of them are the same class the first block
  of this file was written for: **`Dockerfile`**, whose `RUN` lines execute in a Linux container, and
  **`docker-compose.yml`**, which `*.yaml` does not reach because `.yml` is a different extension.
  Neither had cost anything yet and both were one checkout from costing what that block names.
- **115 files were CRLF in the working copy against a clean LF index** — including a `.ps1`, whose
  class has been pinned since 2026-08-17. **So the pin has only ever protected the blob**, which this
  store already knew and had never seen at this scale
  ([[the-lf-pin-protects-the-blob-and-git-status-is-silent-about-the-working-copy]]).
- **After the renormalisation: zero.**

**`text=auto` and not a bare `text`**, so git decides by looking for a NUL byte and images, fonts and
anything else binary stay untouched. Verified with `git ls-files --eol` across the tree rather than
assumed.

## The command that does the rewrite is not the obvious one

**`git checkout-index -a -f` does not perform the conversion.** It writes files that are already
present without re-applying the eol filter, so a working copy full of CRLF stays CRLF and the command
reports success.

**`rm` the files and then `git checkout -- .` does.** The path has to be absent for git to write it
through the filter.

**This is the same family as the stat cache**: a git command that reports having done the thing
without having done it, and no diff to say otherwise
([[the-stale-stat-cache-behind-git-status]], [[line-endings-make-git-status-overstate-what-changed]]).
It is written down because the next person to renormalise a tree will reach for the first command.

## What survives this ruling and what does not

**Survives:** every block below the default line, and the reason each was added. **Survives:** the
rule for a class that needs something *other* than LF — an exemption is still a decision with a cost
behind it, and none exists today.

**Does not survive:** the practice of waiting for a class to cost something before it is covered.
That was this page's title and it is now the exception rather than the rule
([[the-python-class-is-pinned-to-lf-before-it-cost-anything-in-this-repository]] was the first
departure, on 2026-08-24; `Makefile` was the second, earlier on 2026-08-26; this is the third and it
generalises them).

**The title above is left as it is.** It names what the policy was for nine days and what every block
in `.gitattributes` was decided under; a title rewritten to match today's rule would make the record
below it unreadable ([[the-date-of-a-correction-note-is-the-date-the-text-became-false]]).
