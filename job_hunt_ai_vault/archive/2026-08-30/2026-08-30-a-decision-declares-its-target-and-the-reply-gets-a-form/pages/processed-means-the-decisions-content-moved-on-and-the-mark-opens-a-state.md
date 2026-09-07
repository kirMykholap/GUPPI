---
title: "`processed` means the decision's content moved on, and the mark opens a state rather than naming a place"
type: decision
status: archived
superseded_by: [[processed-is-repealed-and-the-mark-it-carried-is-derived]]
authority: processed-status-mint
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-28
created: 2026-08-28
sources: ["archive/2026-08-28/the-sprint-list-stops-lying-and-archiving-gets-a-predicate/handoffs/2026-08-28-the-sprint-list-stops-lying-and-archiving-gets-a-predicate.md", "job_hunt_ai_vault/wiki/decisions/_schema.yaml", "scripts/vault-check.sh"]
tags: [vault, record-schema, process]
---

# What the word means, in his own ground — 2026-08-28

> **owner:** «Если решением было "внести предложение и создать новый модуль", то как? Если создан
> proposal, где описывается модуль, но не иплементирован, то выполнен ли decision? Я считаю что да,
> потому что он передал управление на следующий слой, где мы его и словим. А если следить за
> полноценным выполнением (то есть полностью созданный модуль), то это решение может висеть вечно.»

**`processed` means the decision's content has been carried forward onto another page, so the
decision is no longer the thing to read.** *(the owner selected it, from three readings the session
offered.)*

**Rejected: "the obligation is discharged".** A decision tracked to full implementation can hang
for ever — his own argument, and the reason the mark is about *where the content went* rather than
about *whether the work is done*.

**Rejected: "an agent has read it".** Reading is not a state of the corpus.

# It is a `status` value, and it frees the page's `authority:` slug deliberately

*(the owner selected it, 2026-08-28, from a proposal that named the consequence first.)*

**Rule 3 of the gate compares `authority:` between `current` pages only**, so a page that stops
being `current` stops colliding with anything. That is right here — **a processed decision is no
longer the sole answer to its question, because the answer left with the page it produced** — and it
is written down because the alternative is a reader meeting two answers to one question later and
concluding the gate is broken.

**Rejected: a field of its own beside `status:`.** It is a state of the page, and this store already
has the field that carries one.

# It opens a state and does not name a place

*(the owner selected it, 2026-08-28.)* **The librarian sets the mark, the page stays in `wiki/`, and
the sweep moves it as a separate step at `/vault-lint`.** The gate judges the value not at all.

**This is the shape `implemented` was given on 2026-08-23 and it is deliberate reuse**
([[implemented-joins-the-legal-status-values-and-the-status-block-enters-every-schema]]).
**Setting the mark is a judgement and moving the page is mechanics, and they fail differently**:
one step instead of two makes an error of judgement immediately irreversible.

# Where it is legal, and where it is red

**`wiki/decisions/_schema.yaml` alone.** It is red in the other five folders, which is the
protection rather than an oversight — the same arrangement `implemented` has in `wiki/proposals/`
([[the-legal-value-list-lives-in-each-folders-schema]]).

**The value landed in the schema on 2026-08-28 and no sweep writes it yet.** The predicate that
decides when a page earns it is on its own page
([[a-decision-is-processed-when-a-live-page-names-it-in-decided-by]]), and the agent that applies
that predicate is unbuilt ([[the-decisions-agent-reads-only-and-runs-at-every-ingest]]).

# Overturned 2026-08-30, on the owner's own word

**Superseded by [[processed-is-repealed-and-the-mark-it-carried-is-derived]].** He said it:
«решение от 28 августа, которым processed был заведён - отменяется».

**What killed it is arithmetic, not a change of mind about what it meant.** Case 2.4 of 2026-08-30
made the archiver mark and move in **one pass**
([[the-archiver-marks-and-moves-a-decision-in-one-pass]]), and `processed` and `archived` are two
values of the same field — so in a single pass the second overwrites the first in the same act and no
reader ever observes the first. A mark that cannot be observed distinguishes nothing.

**The value stays legal in the schema while one live page still carries it**, and comes out with the
sweep entry when the corpus is empty of it
([[processed-is-struck-from-the-schema-once-no-page-carries-it]]). The page is not wrong about what
`processed` was intended to mean; it is wrong that the state is reachable.
