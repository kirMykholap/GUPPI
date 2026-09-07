---
title: "The vault's CRLF files are renormalised, no new rule is written, and `/vault-lint` gains a count step"
type: decision
status: current
authority: vault-crlf-renormalisation
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-26
created: 2026-08-26
sources: ["archive/2026-08-26/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built/handoffs/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built.md", ".claude/skills/vault-lint/SKILL.md"]
tags: [vault, harness, process]
---

# The ruling, 2026-08-26

*(the owner selected it, against doing nothing and against writing a new rule.)*

**The CRLF files in the vault are renormalised to LF.** **No new rule is written**, because
`*.md` is already pinned ([[markdown-is-pinned-to-lf]]) and the pin protects the committed blob
rather than the working copy
([[the-lf-pin-protects-the-blob-and-git-status-is-silent-about-the-working-copy]]).

**`/vault-lint` gains a step that prints the count** of vault `.md` files that are CRLF in the
working copy — the instrument that would have made the number visible without anyone going looking.

**The count is not `grep -c $'\r'`**, which returns a line count and has already been used here to
contradict a correct claim ([[grep-with-an-escaped-cr-returns-a-line-count-and-not-a-cr-count]],
[[a-cr-byte-census-of-the-working-copy-behind-lint]]).

# The number moved and nobody measured it in between

**Measured 2026-08-26 with `file` over `git ls-files`: five CRLF files in the vault.** The recorded
figure of 2026-08-22 was eight. **Nothing measured it between those dates and the cause of the fall
is unknown.**

**That is the argument for the count step rather than against the measurement**: a number that moves
unobserved is a number nobody can reason from
([[a-stated-count-drifts-from-the-list-it-heads]]).

# Rejected

**Rejected: leaving them.** Line-ending churn makes `git status` overstate a session's diff, which
has already cost a reading here ([[line-endings-make-git-status-overstate-what-changed]]).

**Rejected: a new rule.** A file class is pinned after it costs something, and this class is already
pinned ([[a-file-class-is-pinned-after-it-costs-something]]). What was missing was not a rule but an
instrument.

# What it obliges, and neither half is done

- **The renormalisation itself** — four of the five files are under `wiki/`, and the fifth is under
  `raw/handoffs/`, **which is immutable and therefore not renormalised**.
- **The count step in `.claude/skills/vault-lint/SKILL.md`**, which is a harness file the librarian
  does not write.

Both moved to the next session with the rest of the plan's third phase
([[the-plans-remaining-phase-moves-to-s3-and-the-ritual-runs-whole]]).

# The population moved again between the ruling and its execution, and nobody measured that either — 2026-08-26

**The figure of five above is the reading of the day the ruling was taken and it is not patched.**
Measured again the same day, immediately before the renormalisation, over
`git ls-files` with `tr -dc '\r' | wc -c` per file: **two CRLF files in the vault, not five.**
**Three renormalised themselves between the two readings**, with nothing deciding it and nothing
observing it — the same silent movement the section above records between 2026-08-22 and 2026-08-26,
now inside the single day between the ruling and its execution.

**Eight on 2026-08-22, five on 2026-08-26, two later that same day, and no cause is known for either
fall.** **It strengthens the count step rather than the renormalisation**: what the ruling bought was
a file list, and the list was already wrong by the time anyone acted on it
([[a-stated-count-drifts-from-the-list-it-heads]],
[[a-figure-measured-before-the-tree-moved-is-not-a-measurement-of-this-tree]]).

**One `wiki/` file was renormalised** —
[[a-hook-refuses-on-a-measured-condition-a-reliable-measurement-and-a-refusal-that-says-how-to-clear-it]],
122 lines and 122 CR bytes, rewritten with LF and nothing else changed:
`git diff --ignore-cr-at-eol` over it is empty.

**After it there is exactly one CRLF file left in the vault, and it is there on purpose.**

# An archived journal is not renormalised, and archiving is not what makes a file mutable — 2026-08-26

*(the owner ruled it, against a recommendation this session had made and he had provisionally
accepted.)*

**The fifth file of the list above is
`archive/2026-08-17/2026-08-17-a-rule-is-written-once-and-rendered/handoffs/2026-08-17-a-rule-is-written-once-and-rendered.md`,
337 CR bytes, and it stays exactly as it is.** It was under `raw/handoffs/` when the ruling was
taken and it is under `archive/` now, because `raw/handoffs/` was swept whole that day
([[raw-handoffs-is-swept-whole-today-and-the-forward-only-clause-is-overturned]]).

**The session read the move as lifting the exemption** — the clause above says *`raw/handoffs/`,
which is immutable*, and the file had left `raw/handoffs/`. **The owner refused that reading.
Archiving does not make a file mutable: an archived journal is the same artefact moved, and what
protects it is what it is rather than where it sits** ([[raw-holds-testimony-and-artefacts-are-frozen]],
[[what-an-archived-page-asserts-is-frozen-and-how-it-is-found-is-live]]).

**So the exemption is a property of the journal and not of the path**, and the clause above should be
read that way wherever the file has been moved to. **The `/vault-lint` count step therefore counts a
file it must never propose to fix**, which is a thing its brief has to say rather than a defect in
the census ([[a-cr-byte-census-of-the-working-copy-behind-lint]]).

## The ruling stands in substance, and line endings were never part of what it protects — the owner's correction, 2026-08-26

*(the owner ruled it, against restoring CRLF to the working copy and against narrowing the wording of
the section above.)*

**The section above was not implementable as stated, and this note says so rather than editing it.**

**Measured 2026-08-26, on the file the section names**: the blob carries **0 CR at HEAD and 0 CR at
`1cf0ec3`, the commit that placed it in `archive/`**; `.gitattributes` has pinned `*.md text eol=lf`
since `5e864f1` on **2026-08-16**, ten days before the ruling. **So any checkout of that path
produces LF.** The 337 CR survived only because that one working copy had never been refreshed —
which is precisely what this vault already records about what a pin does and does not reach
([[the-lf-pin-protects-the-blob-and-git-status-is-silent-about-the-working-copy]]).

**The session then renormalised it anyway.** It went into a bulk pass over 115 CRLF working copies
and nobody noticed it was in the list — **a divergence against a direct instruction, recorded as
one.** There is no commit behind it and `git diff` reports the content identical to the blob, so what
was lost is the working copy's bytes and nothing the repository holds.

**The owner's correction is in two halves and only the second is new.**

- **The ruling stands in substance: an archived page is not edited.** *What* the journal asserts is
  frozen, and archiving does not make it mutable
  ([[raw-holds-testimony-and-artefacts-are-frozen]],
  [[what-an-archived-page-asserts-is-frozen-and-how-it-is-found-is-live]]).
- **Line endings were never part of what it protected.** A CR is not testimony. A checkout would
  have changed those bytes without anybody deciding anything, which is what makes them the wrong
  thing for an immutability rule to range over.

**He chose that against two alternatives**: restoring CRLF to the working copy, which would recreate
a state git will undo on the next checkout; and narrowing the wording above, which would make a
correction look like a rule that had always said this
([[the-date-of-a-correction-note-is-the-date-the-text-became-false]]).

**What this does not license.** It says nothing about editing an archived journal's *text*, which is
still refused. The distinction it draws is between the bytes a version-control system normalises on
its own and the bytes an author wrote.

# Both obligations are discharged — 2026-08-26, later the same day

**The count step exists in `.claude/skills/vault-lint/SKILL.md`**, written by the session as a harness
file the librarian does not write. **It counts files over the vault, not bytes over the repository** —
chosen against a repository-wide byte census, which is a different instrument on a different page
([[a-cr-byte-census-of-the-working-copy-behind-lint]]).

**The renormalisation ran, and it ran far wider than this ruling's five files**: 115 tracked files
across the repository, of which the vault's were a part
([[the-lf-pin-protects-the-blob-and-git-status-is-silent-about-the-working-copy]]).

**One of the 115 was the archived journal this ruling had exempted that morning**, swept without the
list being checked against the ruling
([[divergence-a-bulk-renormalisation-swept-a-file-the-owner-had-ruled-untouched]]).

**And the class-level fix landed with it** — `* text=auto eol=lf` as a default, so a per-extension
list stops being the mechanism ([[a-file-class-is-pinned-after-it-costs-something]]).
