---
title: "`decided_by:` is legal in `wiki/proposals/` and `wiki/rules/` alone, and required in `wiki/rules/`"
type: decision
status: archived
authority: decided-by-legal-folders
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-23
created: 2026-08-23
sources: ["scripts/vault-check.sh", "job_hunt_ai_vault/sprint.md", "[[decided-by-is-a-field-of-its-own-and-not-a-line-in-sources]]", "[[the-unknown-key-verdict-orders-a-schema-change-ahead-of-the-page-that-uses-the-field]]", "archive/2026-08-23/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands/handoffs/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands.md"]
tags: [record-schema, vault, harness]
---

# The ruling, 2026-08-23

**`decided_by:` is legal in `wiki/proposals/` and `wiki/rules/` and in no other folder.** In
`wiki/rules/` it becomes **required**; in `wiki/proposals/` it stays **optional**. The four
remaining folders — `decisions/`, `concepts/`, `entities/`, `lessons/` — declare the key in neither
block, which is the spelling that makes it red there
([[the-unknown-key-verdict-orders-a-schema-change-ahead-of-the-page-that-uses-the-field]]).

**Attribution, and it is the same shape S3's own criteria carry.** The owner took this by
**approving a plan he read in Russian**, on 2026-08-23. That is a decision and not an utterance: the
ruling is his, the wording on this page is the session's, and none of it is a quotation or is signed
as his words
([[the-retro-records-a-ruling-chosen-from-a-menu-and-ratifies-decisions-not-utterances]],
[[the-plan-the-owner-reads-to-approve-it-is-written-in-russian]]). The plan itself lives outside the
repository and is therefore in no `sources:` line here.

# The ground: a decision produces a proposal or a rule, and nothing else

**The chain is causal and it is short.** A decision is taken; what it produces is either a proposal
— what we would build — or a rule — text the harness renders somewhere. Nothing else in this store
is *caused by* a decision in the sense the field means. A concept describes a mechanism, an entity
describes a thing, a lesson records what burned us; each of those **descends** from something and
names what it descends from in `sources:`.

**So the chain stays traceable link by link without a fourth field.** A lesson names the journal and
the pages it was compiled from; those pages name theirs; a proposal or a rule names the decision
that caused it in `decided_by:`. The walk is the same length either way, and only the last hop —
the one that is genuinely a *cause* rather than a *provenance* — needs a field of its own. Putting
the key into all six folders would have obliged four of them to answer a question they do not have.

# Why `wiki/rules/` is the folder where it is required

**`authority:` is forbidden there**, because a rule answers with `governs:` and the two fields on one
page would make the decision and the rule stating it share a slug
([[authority-beside-governs-is-forbidden-on-any-page]],
[[governs-is-a-property-of-wiki-rules-alone]]). `decided_by:` is therefore the **only** field by
which a rule can name the decision behind it, and a field that is the sole carrier of a link is not
one a page may omit — the same argument that made `authority:` required outside `rules/` on
2026-08-21 ([[authority-becomes-the-index-and-is-required-outside-rules]]).

**What the fifteen rule pages do today, measured 2026-08-23 rather than assumed.** Every one of them
puts whatever it cites into `sources:`, mixed with the file it governs, with hooks and scripts, with
handoffs, and with pages from four other folders. Ten of the fifteen name at least one `decisions/`
page there — [[a-retrospective-is-a-sessions-end-not-a-sprints-ritual]],
[[a-session-ends-with-retro-then-handoff-then-ingest]],
[[an-ast-boundary-test-is-fixed-at-its-cause-not-in-the-test]],
[[ask-before-weakening-or-working-around-a-rule]],
[[english-in-the-repository-russian-with-the-owner]],
[[our-javascript-does-not-choose-which-rows-are-on-screen]],
[[the-map-in-claude-md-is-the-vault-its-librarian-and-the-sprint]],
[[the-owner-decides-how-a-slice-is-executed]],
[[the-suite-never-runs-against-the-production-database]] and
[[write-the-miss-into-vault-feedback-before-the-turn-ends]]. **Five name none at all** —
[[a-block-attributed-to-the-owner-is-written-in-his-own-russian]],
[[a-pre-task-runs-between-the-plan-and-its-approval]],
[[dispatch-librarians-in-parallel-only-for-reading]],
[[no-new-entity-where-an-existing-one-can-carry-the-claim]] and
[[the-shared-reading-discipline-renders-into-every-agent-that-reads-the-vault]], whose `sources:`
carry skills, agents, hooks, a journal, and pages from `lessons/`, `concepts/` and `proposals/`.

**The defect is worse than the ruling's own statement of it, and in the same direction.** Where a
decision *is* cited, no reader — human or script — can tell which entry of `sources:` is the cause;
where it is not cited, the cause is not recorded on the page at all. A required field answers both
halves. Two of the ten reach their decision only through `archive/`, which the sweep of live pages
does not see either.

# What this overturns, and it was decided earlier the same day

**One bullet of [[decided-by-is-a-field-of-its-own-and-not-a-line-in-sources]] went false with this
ruling, hours after it was written**: the one obliging the key to be declared in every folder's
`_schema.yaml`. That page is
**not superseded** — its claim is *which field carries the cause*, and that claim is untouched. The
folder set is a different question, which is why it is a page of its own and why the correction is
written there as a dated note rather than as a retirement
([[a-title-corrected-in-place-is-not-a-supersession]],
[[the-date-of-a-correction-note-is-the-date-the-text-became-false]]).

## And the argument that bullet was grounded in is false, which is the part worth keeping

**The bullet reasoned from the `values:` mechanism and applied it to a key.** Its words:

> the same all-six obligation that the `status:` block carries, and for the same reason: the gate
> iterates the fields a folder **declares**, so a folder left out loses the verdict silently and in
> the direction of passing

**That reason is correct for `values:` and false for a key**, and it was transplanted from
[[implemented-joins-the-legal-status-values-and-the-status-block-enters-every-schema]], where it is
about legal *values* and is right. The `badvalue` pass genuinely iterates the fields a folder
declares values for, so a folder carrying no `status:` block loses its status verdict entirely, and
the gate stays green.

**A key fails the other way.** `scripts/vault-check.sh:382`, read against the tree on 2026-08-23:

```awk
if (kk[i] != "" && !((folder SUBSEP kk[i]) in allowed)) print "unknownkey|" f "|" kk[i]
```

`allowed` is built from `required:` and `optional:` and nothing else, and `unknownkey` runs through
`note()`, which sets `fail=1`
([[the-unknown-key-verdict-orders-a-schema-change-ahead-of-the-page-that-uses-the-field]]). **So a
folder left out of a key declaration fails towards refusing** — a page carrying `decided_by:` in
`concepts/` is red, loudly, and the verdict names the page. The two obligations are **different in
kind**: a `values:` block must go into all six because omission is silent; a key goes only where it
is legal, because there omission is a refusal.

**The narrowing is therefore mechanically safe**, and the argument the wider set was defended with
was wrong on its own terms. Recording that is the point: a false argument left standing is inherited
by the next reader, who has no reason to re-derive it
([[a-command-that-is-false-only-in-its-documentation-fails-nothing]]).

**The `Links:` field is the other case and it goes the other way.** It is legal everywhere, so it
enters all six declarations
([[a-links-field-carries-the-bodys-wikilinks-and-sources-keeps-provenance]],
[[links-is-filled-by-a-script-from-the-bodys-wikilinks]]). All-six is a property of the field, never
of the mechanism.

# Rejected alternatives

| the alternative | why it lost |
|---|---|
| **the key in all six folders**, as obliged earlier the same day | four folders would declare a field for a question they do not have; the causal chain reaches them through `sources:` already, one hop at a time |
| **required in `wiki/proposals/` as well** | a proposal can be raised with no decision behind it — an idea written down before anyone ruled on it — so there the field is a fact when it exists and not an obligation |
| **narrow the field and leave the false sentence standing** | the narrowing would be right and the reason recorded for it would be wrong, and the next reader would inherit the argument rather than the ruling |

# It is not built, and this page makes no claim that it is

**No `_schema.yaml` declares the key, no page carries it, and nothing counts the shortfall.** The
schemas are the session's file and not the librarian's
([[what-the-gate-reads-as-its-own-input-is-the-sessions-to-write]]), and the forced order is already
recorded: the folder's schema admits the key first, and only then may a page in it carry the field.

**Required in `wiki/rules/` has a sequencing cost that the `authority:` and `binding:` promotions
both paid.** A key promoted to `required:` before the pages carry it reddens every page in the folder
at once, and a red gate locks the librarian out of the store it maintains
([[a-lock-on-a-red-tree-hides-the-health-of-what-it-guards]]). Both earlier promotions went
legal-and-optional first, filled, then promoted. Nothing here says which order this one takes; it
says where the field ends up required.

# What is still open

- **What a page does when its cause is not a decision page.** Narrowed by this ruling and not
  closed: a proposal raised from nothing has no deciding page, and whether the field is then absent
  or names something else was not asked. In `wiki/rules/` the question does not arise, because a
  rule the harness renders is text somebody ruled should be rendered.
- **Whether the field is checked beyond its presence.** That its target is a page in
  `wiki/decisions/` is verified by nothing, and rule 4's broken-wikilink sweep proves only that the
  page exists.

# It is built, and both of the open questions above are answered — 2026-08-23, later the same day

**The two schemas declare the key.** `wiki/proposals/_schema.yaml` carries it under `optional:`;
`wiki/rules/_schema.yaml` carries it under `required:`, promoted **after** every rule page carried
it and not before. The order was legal-and-optional, then the back-fill, then promote — the order
this page said it did not choose, taken by the session that built it
([[the-unknown-key-verdict-orders-a-schema-change-ahead-of-the-page-that-uses-the-field]]).

**The shortfall is counted.** `bash scripts/vault-check.sh --lint` prints the count of pages in
those two folders carrying no `decided_by:` and names each one. Read at this ingest, every page it
names is a `proposals/` page.

## The second open question is closed and the first is not

**"Whether the field is checked beyond its presence" — it is.** The gate resolves the wikilink,
reads the target's `type:`, and reddens anything that is not a `decisions/` page, naming the type it
found. **A target that resolves to nothing was already caught**, because rule 5 sweeps a wikilink in
frontmatter exactly as it sweeps one in the body — measured before the verdict was written, in a
scratch tree, in both directions. **Only the wrong-type case was new**, so only the wrong-type case
got a verdict: a second existence check would be a second reader of a fact rule 5 already reads.

**"What a page does when its cause is not a decision page" is still open**, and it is now the live
question for the `wiki/proposals/` back-fill rather than a hypothetical
([[the-idea-and-decided-by-pair-is-ordered-built-and-the-back-fill-goes-first]]).

## What the field found, which nine days of reading had not

**The fill was a mechanical pass and it turned up a rule with no decision behind it at all.**
`ask-before-weakening-or-working-around-a-rule` had been enforced since 2026-08-14 and was accounted
for nowhere; the librarian refused to point the field at the nearest plausible page and reported it,
and the owner ratified the rule at the retro
([[the-ask-before-weakening-rule-is-ratified-after-being-enforced-without-a-decision]]).

**That is the argument for the field being required rather than encouraged.** A required link is an
audit that runs itself: it asks a page to *name* its foundation, and a page that cannot is visible
in a way careful reading never made it. Ten of fifteen rule pages named a decision inside `sources:`
and no reader — human or script — could tell which entry was the cause, because `sources:` also
holds the governed file and every other citation.

# The causal chain was challenged by the owner and re-affirmed by him — 2026-08-24

**He widened it himself and then withdrew the widening.** Having challenged one of the session's
claims and been shown the count that refuted it, he widened the causal chain to *a decision produces
everything except lessons*; four places carrying his own narrower ruling were put in front of him,
and he withdrew it:

> **owner: "a decision produces a proposal or a rule and nothing else" - это правильно, я согласен.
> Мой предыдущий текст был неправильный, а ты поймал меня и это просто отличный результат работы
> инструмента.**

**So the narrowing this page rests on is ratified twice**, and the second time against his own
counter-proposal. **Nothing in the schema or the folder set moves as a result** — the value of the
exchange is the ratification, not a change.

**It is also a reading of what the store is for.** The instrument that caught him is the corpus
answering back, which is the property the whole apparatus is measured on
([[the-measurement-is-whether-the-vault-changed-what-a-session-did]]).

# The narrowing was ratified a fourth time, against a widening he had already accepted — 2026-08-29

**owner:** «Если решение породило другую сущность - оно уходит в архив. Мы ничего не теряем. Мы всегда
ищем по сущностям и найдем это решение в другом виде. Если это proposal - Значит нужно строить.»

> [!IMPORTANT] «сущность» HERE IS **NOT** THE `entities/` FOLDER
> He is saying a decision that has produced its page is spent and goes to `archive/`, and that where
> the thing produced is a proposal the answer is to build the proposal. **Compiled as "entity" this
> sentence would re-open the very widening it closes.** The field stays legal in `wiki/proposals/` and
> `wiki/rules/` and in no other folder.

**The session had designed the widening, recommended it, and he had accepted it** — `decided_by:` legal
but not required in `entities/` and `concepts/`, on the ground that requiring it would redden 181 pages
at once. **`/pre-task` then found that he had ratified the narrowing three times**: approving it
2026-08-23, challenging and withdrawing his own widening 2026-08-24, and stating on 2026-08-28 that a
decision cannot produce an entity, only a proposal that watches the criteria for producing one.

**Rejected: the session's widening**, one step before it was built.

**The cost the design named only on one side.** Widening the field opens a route by which a **live**
prohibition is archived because an entity page pointed at it, and `/pre-task` does not read `archive/`.
The design named the benefit and not that.

**Nothing in `wiki/` ever asserted the widening.** Neither `wiki/entities/_schema.yaml` nor
`wiki/concepts/_schema.yaml` declares the key, and `scripts/vault-check.sh:422` reports `unknownkey` for
any key a folder's schema does not list — so the field is **red today on those pages** and would go
legal only by a schema change, with no script change needed. **The one false carrier is outside the
vault**: `docs/who-reads-the-vault.md` and the artifact published from it
([[who-reads-the-vault-and-who-writes-it]]).

**One cardinality note this ruling leaves standing.** `scripts/vault-check.sh` reads `decided_by:` with
a greedy `s/.*\[\[//`, so it resolves only the **last** wikilink on the line; a second is not rejected,
it is not read at all. With the field documented as exactly one that is consistent, and it is the thing
any future widening would inherit.

*(Compiled from `raw/handoffs/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds.md`.)*
