---
title: "The `ruleclaim` verdict widens to any page carrying `authority:` beside `governs:`, and `nogoverns` stays rules-only"
type: decision
status: archived
authority: rules-folder-gate
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-19
created: 2026-08-19
sources: ["archive/2026-08-19/2026-08-19-the-corpus-stops-counting-and-the-gate-learns-its-keys/handoffs/2026-08-19-the-corpus-stops-counting-and-the-gate-learns-its-keys.md", "scripts/vault-check.sh"]
tags: [record-schema, harness, vault]
supersedes: [[the-governs-branch-widens-and-the-others-stay-rules-only]]
---

# Decided by the owner on 2026-08-19

> **owner: `ruleclaim` widens to any page carrying `authority:` beside `governs:`.**

The branch now reads `if ((f in claim) && (f in destination) && destination[f] != "")` and no longer
asks what folder the page is in. **Rules are unchanged in practice** — `governs:` is required there
and a rule carrying an `authority:` always carried both — so what the widening reaches is the pages
outside `wiki/rules/` that render.

# The predecessor's own argument is what retired it

[[the-governs-branch-widens-and-the-others-stay-rules-only]] kept this branch narrow on a stated
ground, and the ground was true when it was written:

> *"Whether a `concepts/` page may own an `authority:` AND render is a shape nothing in the vault
> rules on, and leaving the gate narrow is what preserves that question instead of answering it by
> accident from inside a script."*

**The vault ruled on it the next day** ([[authority-beside-governs-is-forbidden-on-any-page]]), and
the comment kept the gate narrow for a reason that had expired. **So the ruling was wider than the
gate enforcing it** — the exact shape this harness exists to make impossible
([[knowing-a-rule-is-not-a-mechanism]], [[no-rule-reads-a-harness-file]]) — and the verdict follows
the ruling.

**The alarm this discharges had a concrete instance and it was the vault's own schema file.** The
frontmatter example in `job_hunt_ai_vault/CLAUDE.md` carries `authority:` beside `governs:` under
`type: concept`, so a page copied from it landed outside the old branch. The example is a field
catalogue rather than a page and the gate does not read it; what it demonstrated is that the prose
prohibition was reachable by an honest copy.

# The three branches now, and only one of them moved

| Branch | Reach | Why |
|---|---|---|
| `nogoverns` — a rule naming no destination | **rules-only, unchanged** | widening it would demand `governs:` on every page in the corpus, and most of it delivers nothing by design |
| `governs` — collect the field, build the slug-to-destination pairs | **any page**, since 2026-08-18 | it builds the pair table rule 11 joins against, so the address verdict is blind outside `wiki/rules/` without it |
| `ruleclaim` — `authority:` may not sit beside `governs:` | **any page**, from 2026-08-19 | the vault ruled on the shape, so the gate stops being narrower than the rule |

**The predecessor's general shape survives and is not superseded**: *a gate named in the singular
can hold several rules*, and the page that priced this work counted three branches as one thing
([[a-stated-count-drifts-from-the-list-it-heads]],
[[a-proposal-misprices-by-overcharging-one-row-and-undercharging-another]]).

# What it cost, and where the cost showed up

**Changing the message this branch prints broke an existing selftest case**, because a case greps the
wording. That was caught before the commit by grepping the suite rather than by reasoning about it
([[a-cosmetic-change-is-load-bearing-when-a-test-greps-the-output]]). The verdict was proved by
planting an offending page in the real tree and reverting in the same command
([[a-new-verdict-is-proved-in-the-real-tree-because-the-check-cannot-see-a-sandbox]]).

# The general finding, which outlives this branch

**A general mechanism retired two specific verdicts that had each been queued.** The
`authority:`-beside-`governs:` alarm closed here; a returning `quantity:` closed by the key-set gate
the same night ([[the-gate-learns-the-legal-key-set-from-a-yaml-per-folder]]). **The next "this rule
has no mechanism" finding is worth checking against the general gate before a verdict is written for
it.**
