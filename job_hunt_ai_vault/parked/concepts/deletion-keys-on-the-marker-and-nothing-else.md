---
title: "Deletion keys on the marker and nothing else, and an orphan is found by a cheap way and a dear one"
type: concept
status: current
authority: generated-file-deletion
basis: code
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-19/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery/handoffs/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery.md", "scripts/vault-inject.sh", "scripts/vault-check-selftest.sh"]
tags: [harness, vault, testing]
---

# The one fact the deleting branch may read

**The injector removes a generated file by exactly one fact: that it carries the writer's own
marker.** A file in `.claude/rules/` with no marker is somebody's hand-written rule and is never
touched, whatever the vault knows about it — *"the vault does not know about this file"* and *"this
file is mine to remove"* are different statements, and only the one licenses a delete
([[a-claude-rules-file-is-generated-whole-and-deleted-by-its-own-marker]]).

**A selftest case pins it**: an unmarked file that is never removed, which is the one shape the
deleting branch may never take.

# An orphan is found by a cheap way and a dear one

**Cheap: a page that went `deprecated` still names its file.** That case matters more than it looks.
Under `region` a retired rule disappears because the successor overwrites the same region; **under
`whole` the file *is* the rule**, so merely skipping the page leaves the retired text on disk and
the guard goes on delivering it ([[a-deprecated-rule-does-not-render]]).

**Dear: a page deleted outright names nothing**, so the destination directories are swept. **They
are read off the destinations pages name, never written into the script**, which keeps
`.claude/rules/` an ordinary destination rather than a name the script knows
([[the-vault-directory]], [[the-governed-set-is-swept-and-markdown-by-property]]).

# The residual is in the code rather than in anybody's head

**When the last whole-mode page generating into a directory goes, that directory stops being swept
and a marked file in it turns invisible.** The alternative was a recursive grep on every run of a
script the gate runs about ninety times per selftest
([[measure-before-optimising-and-count-processes-not-pages]],
[[the-selftest-cost-scales-with-the-rule-pages-it-renders]]).

**Accepted by the owner, and the trade is written beside the sweep in the code** — which is its
destination, not a plan. It is named here so a reader of this page is not the one to discover it.

# The mirror verdict needed no new rule in the gate

`vault-check.sh` **already** turns any `vault-inject:` line other than *every rule agrees* into a
`note`, so a leftover generated file reddens the gate through the channel rule 12 already uses
([[the-address-verdict-catches-the-leftover-copy-not-the-wrong-file]],
[[the-address-verdict-joins-an-existing-rule-instead-of-becoming-its-own]]). Proved by the suite
case, which asserts the **gate** exits 1 rather than asserting the injector printed something.

# One cause arrived as two, and that was fixed in the same probe

**A verdict printed twice**: the deprecated branch and the sweep both reached the same file. A
reader who fixed the first report would have gone looking for a second cause that never existed —
the same class as an advisory that names one file per line where the fix is one act
([[an-advisory-prints-one-line-and-sorts-what-it-names]]).

**`scripts/vault-check-selftest.sh`: 130 caught, 0 missed**, with cases for a file not generated
yet, a hand-edited one, `whole` with no `paths:`, one left by a deprecated page, one whose page is
gone entirely, and the unmarked file that survives.
