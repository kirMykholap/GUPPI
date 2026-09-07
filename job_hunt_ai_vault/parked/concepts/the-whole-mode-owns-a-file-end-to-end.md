---
title: "The `whole` mode owns a file end to end, and its form is defined once in the writer"
type: concept
status: current
authority: whole-delivery-mode
basis: code
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-19/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery/handoffs/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery.md", "scripts/vault-inject.sh", "scripts/vault-check.sh"]
tags: [harness, vault, testing]
---

# The two modes, and what separates them

**`render: region` writes a slice between paired markers in a file that has its own life.**
**`render: whole` writes the whole file**, which has none
([[render-is-reinstated-and-required-now-that-another-mode-has-a-writer]]).

A generated file is, in order: the page's `paths:` copied **verbatim** into frontmatter, a blank
line, the generated marker naming the page in the same `type: slug` form a region marker uses
([[a-marker-with-its-type-is-a-complete-address]]), a blank line, the slice.

**`paths:` is copied rather than reformatted.** The field is authored on the page and synced, and a
script that rewrote the YAML would make two spellings of one list differ for no visible reason —
which the guard's parser then has to tolerate anyway
([[paths-lives-on-the-vault-page-and-is-written-widest]]).

# The form is defined once, in the writer

**For the reason the rendered region is**: the writer and the comparison must never be able to
disagree about what *generated* means
([[the-rendered-form-is-defined-once-and-read-by-the-writer-and-the-comparison]]). **The check
regenerates and compares byte for byte**, which is the question rule 12 already asks by running the
writer it checks ([[a-check-asks-by-running-the-writer-it-checks]]), and the comparison is not made
through a command substitution ([[a-command-substitution-strips-the-newline-a-gate-compares]]).

**A hand edit is red** ([[a-hand-edit-to-a-generated-rules-file-is-red]]), and a write run is the
repair.

# A missing file and a missing directory are different states

**A missing destination file is the normal first state** — the page exists, nothing has been
generated yet, and the writer creates it.

**A missing destination *directory* is a problem**, and the script refuses. A path whose directory
does not exist is a typo in `governs:` far more often than a directory somebody meant the script to
invent, and inventing it would put a rule where nothing reads it
([[governs-is-a-path-from-the-repository-root]]).

# What was probed by hand before any suite case existed

**Eight probes, in a sandbox rather than the real `wiki/`**, since a session may not write there
([[hand-probe-a-new-mechanism-before-running-the-suite]]): the file is created; a run generates 0 and
is idempotent; `--check` is clean; a hand edit is red and a write run restores it; and each of
`render: whole` with no `paths:`, a `governs:` into a directory that does not exist, `render: banana`
and a destination deleted behind the script produces its own message and exits 1.

**And the chain closes end to end**: the generated file plus the guard delivers the rule on an edit
to `tests/unit/test_boundary.py`, is silent on `tests/unit/test_other.py`, and the *do not edit*
marker is **absent from what is delivered** — so the banner costs nothing in practice and not only
in principle, which is what the decision assumed and nobody had shown.

# One thing about the delivered text is unmeasured

**What the native delivery does with an HTML comment inside a fenced block is not measured.** The
guard keeps a fence intact and strips comments only outside one; the conservative side of the
question is the side taken, and it is written here rather than left as an assumption. It is worth a
probe if it ever matters ([[the-conditional-delivery-probe]]).

# What is owed

**Suite cases for the mode itself.** The probes above are hand-run and nothing re-runs them; the
selftest cases that exist cover deletion and the mirror verdict
([[deletion-keys-on-the-marker-and-nothing-else]]).
