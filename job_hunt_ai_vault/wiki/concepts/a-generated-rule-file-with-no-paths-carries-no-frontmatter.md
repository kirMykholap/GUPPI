---
title: "A generated rule file with no `paths:` carries no frontmatter block at all"
type: concept
status: current
authority: generated-file-without-paths
basis: code
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact/handoffs/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact.md", "scripts/vault-inject.sh"]
tags: [harness, vault, process]
---

# The generated form gained a shape

**With `paths:`, a `render: whole` file is a frontmatter block, the marker, and the slice**
([[a-claude-rules-file-is-generated-whole-and-deleted-by-its-own-marker]],
[[paths-lives-on-the-vault-page-and-is-written-widest]]).

**Without it, the file is the marker plus the slice, and no frontmatter at all.** `---` followed by
`---` is a frontmatter that says nothing, and every reader of the file would then have to decide
what an empty one means — a question with no right answer that would be asked separately by the
hook, the injector's comparison and any human opening the file.

# What the shapes have in common is the property that matters

**Both are defined in one place**, in the injector, and the writer and the comparison read the same
string. Defining the form in the writer alone makes the check report a difference for ever; defining
it in the comparison alone means the form is never written
([[the-injector-walks-pages-to-files-and-the-check-walks-files-to-pages]]).

**The marker still leads in both**, which keeps the one property the deletion path keys on: a
generated file is recognised by its marker and by nothing else.

# The reader strips what is not the rule

**`Get-PreTaskMessage` in `.claude/hooks/pre-task-state.ps1` drops a leading frontmatter block if
there is one and drops the marker line**, reusing what the scoped-rule guard already does. Stripping
happens at read time rather than at generation time **because the generated form is defined once**;
a second writer of that form is exactly what the injector's own comment forbids.

**When the file is missing the hook says so loudly** and names the path, the injector and the repair.
A guard that is silently absent is worse than none, and this repository has shipped that once
([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]).
