---
title: "The `authority.md` rows are written in the same pass as the rule pages, or the gate locks out the only party who may write them"
type: decision
status: current
authority: authority-rows-same-pass
binding: deferral
basis: code
sprint: S3
decided: 2026-08-30
created: 2026-08-30
target_kind: none
target: none
sources: ["archive/2026-08-30/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md", "scripts/vault-authority.sh", "job_hunt_ai_vault/authority.md"]
tags: [vault, harness, process]
---

# Context

**`scripts/vault-authority.sh:244` builds the tree side of its comparison from every page carrying an
`authority:` field, with no folder filter** — `corpus()` walks `find "$VAULT/wiki"` and nothing
narrows it. `cmd_orphans` excludes `rules/`; `cmd_check`, which rule 13 of the gate reads, does not.

**`authority:` became legal in `wiki/rules/` on 2026-08-30**
([[authority-uniqueness-becomes-a-per-type-question]]), so the family rules will carry slugs that this
comparison sees.

**The lock this produces was walked into on one page the same day.** A slug in the tree and not in the
register reddens the gate; `lock-the-librarian.ps1` reads a red gate as a refusal to dispatch; the
librarian is the only writer of `authority.md`
([[one-page-written-into-the-wiki-reaches-the-register-deadlock]]).

# The question

**Are the 53 family rules and their 53 register rows one act or two?**

# How it works after

**One act.** The rule pages and their `authority.md` rows land in the same pass, written by the
librarian, or the gate is red between the two halves and the party permitted to close it cannot be
called.

**Writing the pages alone produces 53 ungrouped slugs and a red rule 13** — the deadlock of 2026-08-29
at fifty-three times the size of the one that happened on one page this day.

**The exception granted on 2026-08-30 does not reach it.** The owner permitted the session to write
**one** line into the register ([[the-session-writes-one-authority-row-and-the-one-writer-clause-stands]]);
fifty-three is a different question and has not been asked. **Which of the two applies is the first
thing the next session settles.**

**No sprint is named.**

# Recommendation

**Write them together, and do not treat the one-line permission as precedent.** The alternative — pages
first, rows after — is the exact sequence that has already deadlocked this store twice, once on a
sweep of 239 pages and once on a single page.

**Rejected: writing the pages and dispatching the librarian afterwards for the rows.**

# Ratification

**The session understood it from the tree**, having read `scripts/vault-authority.sh:244` and traced
what it selects. The owner ruled the mechanism the rules come from and did not rule on this ordering;
it follows from the code.

# The premise under this deferral is false, and the deferral has no subject — 2026-08-31

**This page rests on "writing the pages alone produces 53 ungrouped slugs and a red rule 13".** Under
slug inheritance it produces **none**.

**`bash scripts/vault-authority.sh --check` computes `ungrouped = tree − register`**, and a slug a rule
page inherited from a member of its own family is **already grouped**. Nineteen rule pages were written
on 2026-08-31 and **zero rows were added to `job_hunt_ai_vault/authority.md`**; `--check` agrees, and
the register stands untouched at 63 families.

**Its stale direction widens to `archive/`**, so the 129 pages that moved that day do not strand their
rows either ([[a-register-row-is-stale-only-when-no-page-anywhere-carries-the-slug]]).

**The ordering the page rules on is still right and still binding** — a slug in the tree and not in the
register reddens the gate and locks out the only party who may write it. **What is false is that the
family rules were an instance of it.** The deferral is left standing rather than struck, because the
next thing that mints a slug will meet exactly the condition this page describes, and the convergence
pass will mint some ([[the-convergence-pass-over-the-live-non-decision-pages]]).

*(Compiled from `raw/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md`, and extended at the ingest of `raw/handoffs/2026-08-31-the-families-become-rules.md`.)*
