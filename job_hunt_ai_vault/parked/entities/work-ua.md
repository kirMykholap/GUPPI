---
title: "work.ua — a promo block that ignores filters, and no container at all on an empty query"
type: entity
status: current
authority: work-ua-source
basis: code
sprint: S0
created: 2026-08-13
sources: ["archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md"]
tags: [collection, data]
---

# work.ua

**Its promotional block arrives past any filter we send.** That is the concrete reason the local
re-check is the truth rather than the source's own filtering — see
[[collection-modes-and-why-source-filters-do-not-decide]].

**On a query that finds nothing it does not render `#pjax-jobs-list` at all** — verified live,
`/jobs-zqxwcvbnmlkjhgfd/` answers HTTP 200 with 140 KB and no container. The consequence is larger
than it looks: see [[empty-listing-silences-deactivation]].

It is also the only source that can fetch a full description, through
`WorkUaParser.fetch_description` — a method outside the `BaseParser` contract that nothing in
production calls. See [[description-is-full-has-no-producer]].

## «вакансія від» is an **update** date, not a first publication

Measured on the live first page for «менеджер»: the first 7 cards are the promo block and are not
ordered by date; the rest descend strictly. But among the cards dated *today* sit identifiers
`5549009` and `6068175`, markedly older than their neighbour `8379984`.

**So the depth filter cuts by "when it was last touched", not by "when it first appeared".** For
job-hunting that is arguably the more useful of the two — what gets refreshed is what someone is
actually recruiting for — but it must not be read as a publication date anywhere else.

## A broad tag hits a ceiling, and the ceiling silences deactivation

Live, 2026-08-04, with the tag «менеджер»: work.ua **claimed 13 342** vacancies, handed over **350**,
and ran into the **25-page limit** → the run was marked `truncated` with `ids_incomplete=true`, so
**both the miss marking and the tag-link rebuild were skipped for that source**, with a warning.
dou.ua on the same tag: 1416 claimed, 1416 collected, the set complete.

Two things follow. The reconnaissance numbers in the spec were right (it predicted ~13 000 and
~1400). And an incomplete identifier set forbids marking misses at all — that is rule four of
[[deactivation-cycle]], reached here by volume rather than by failure, and it is the same silencing
that [[empty-listing-silences-deactivation]] reaches from the empty end.
