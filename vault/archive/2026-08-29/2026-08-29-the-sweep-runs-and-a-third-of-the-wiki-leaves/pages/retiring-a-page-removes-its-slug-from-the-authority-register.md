---
title: "Retiring a page removes its slug from the authority register, and that step joins the supersession procedure"
type: decision
status: archived
authority: retirement-register-step
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-22
created: 2026-08-22
superseded_by: [[the-authority-register-step-is-repealed-and-an-archived-page-keeps-its-slug]]
sources: ["archive/2026-08-22/2026-08-22-the-strike-lands-and-a-quote-gets-a-verdict/handoffs/2026-08-22-the-strike-lands-and-a-quote-gets-a-verdict.md", "authority.md", "scripts/vault-authority.sh"]
tags: [vault, process, harness]
---

> [!WARNING] REPEALED 2026-08-29
> The owner struck this rule. A page goes to `archive/` keeping its slug and its `authority:`, and
> nothing removes a row from the register. Read
> [[the-authority-register-step-is-repealed-and-an-archived-page-keeps-its-slug]] instead. What is
> below is kept because "why did we change this" is a legitimate question later.

# The ruling, 2026-08-22

**Owner selected: a fourth step joins the supersession procedure.** Write the successor with
`supersedes:`; set the old page to `status: deprecated` with `superseded_by:`; move it into
`archive/`; **and remove its slug from `authority.md`**.

**Rejected: teaching `scripts/vault-archive.sh` to edit the register itself**, which would make it a
second writer of a file that has exactly one ([[the-librarian-writes-unattended]],
[[the-one-writer-clause-reaches-a-citation-and-not-only-a-register]]).

**Where it is written is the session's call and not the librarian's.** The three-step procedure lives
in the vault's own `CLAUDE.md`, which the gate reads as its own input
([[what-the-gate-reads-as-its-own-input-is-the-sessions-to-write]]).

# Why the step exists at all, and why it did not before

**`authority:` became required outside `wiki/rules/` on 2026-08-21**, and
`bash scripts/vault-authority.sh --check` compares the register against the tree in **both**
directions ([[authority-becomes-the-index-and-is-required-outside-rules]]). A slug that leaves
`wiki/` with its page leaves a register row no page carries, and rule 13 reddens on it.

**The ordering is the trap.** The move is the last of the old three steps, so the register goes stale
at exactly the moment the retirement looks finished, and the next thing that happens is a red gate on
a run the retirer believed was clean.

**It was met on the first retirement after the field became required.** Striking
`advisory-is-the-default-for-a-hook` left `hook-blocking-default` behind; **the failure surfaced
inside the archive script's own gate run**, so the slug was removed *before* the move rather than
after ([[the-archive-script-gains-a-pages-kind-and-a-retired-page-is-dated-by-its-session]],
[[vault-archive-sh]]).

# It is the one deletion this store's *nothing is ever deleted* clause does not reach

**What is taken out is a register row, and the page it named is intact in `archive/` with every word
it asserted.** A register is how a page is *found*, and how a page is found is live where what it
asserts is frozen ([[what-an-archived-page-asserts-is-frozen-and-how-it-is-found-is-live]]).

**The tool's own header prescribes exactly this repair for a stale row**, so the deletion is the
documented operation rather than a judgement about the corpus
([[a-field-with-no-register-produces-unique-values-by-default]]).

*(Compiled from `raw/handoffs/2026-08-22-the-strike-lands-and-a-quote-gets-a-verdict.md`.)*

# The ordering trap this creates, named — 2026-08-26

**The slug must leave `authority.md` *before* the move, and the move is the last of the three
supersession steps.** So the register goes stale **exactly when the retirement looks finished**, and
the next `bash scripts/vault-authority.sh --check` reddens on work that looked clean.

**The victim is the register rather than the page.** Nothing about the retired page is wrong; what is
wrong is a register naming a slug the tree no longer carries in `wiki/`.

**A plan that names four archive moves and no `authority.md` step reddens the check by construction**
— which is what a `/pre-task` found in the plan of 2026-08-26, against a register that was clean on
666 slugs ([[a-plan-can-be-factually-wrong-about-the-tree-and-the-pre-task-is-what-reads-the-tree]]).

**The order to write into any such plan: delete the slug, then move the page.**

**A supersession where the successor keeps the same slug needs no register edit at all**, because the
slug never leaves the tree — only the page carrying it changes. That is the ordinary ingest case and
it is why the trap is easy to forget.

*(Compiled from `raw/handoffs/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built.md`.)*
