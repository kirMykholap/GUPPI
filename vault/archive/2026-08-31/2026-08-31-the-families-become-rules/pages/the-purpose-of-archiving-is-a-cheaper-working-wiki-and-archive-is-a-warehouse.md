---
title: "The purpose of archiving is a cheaper working wiki, and `archive/` is a warehouse"
type: decision
status: archived
authority: archiving-purpose
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-28
created: 2026-08-28
sources: ["archive/2026-08-28/the-sprint-list-stops-lying-and-archiving-gets-a-predicate/handoffs/2026-08-28-the-sprint-list-stops-lying-and-archiving-gets-a-predicate.md"]
tags: [vault, process, retrieval]
---

# The ruling, 2026-08-28

> **owner:** «дешевеет то, что библиотекарь и vault-ask работают с Wiki, а не archive. Архив мы пока
> что не трогаем и это просто склад. Подметая рабочую wiki - мы упрощаем работу агентам, поиск и
> поддерживаем чистоту работы. Это экономит нам время и токены.»

**What archiving buys is measured on `wiki/`, never on `archive/`.** The librarian and `/vault-ask`
read the working wiki; the archive is a warehouse nobody sweeps, nobody checks and nothing reads by
default. So every archival criterion is judged by what it removes from the reader's path, and the
saving is agent time and tokens.

**Rejected: measuring the cost to a human reader in Obsidian.** That was the session's alternative
and he did not take it. A human opens a page he went looking for; an agent pays for every page the
folder contains.

# What follows from it, and what it forbids

**A criterion that does not shrink `wiki/` is not an archiving criterion.** This is the ground the
`decided_by:` predicate was accepted on and the ground the loose *cited by anything* predicate was
rejected on — the loose one leaves the folder essentially where it was
([[a-citation-is-not-a-test-in-a-corpus-this-densely-linked]],
[[a-decision-is-processed-when-a-live-page-names-it-in-decided-by]]).

**It forbids spending work on the archive itself.** *«Архив мы пока что не трогаем»* — no sweep,
no gate rule and no register covers what is in there, and the corpus already records that as a
deliberate property rather than a gap ([[what-an-archived-page-asserts-is-frozen-and-how-it-is-found-is-live]],
[[archive-is-dated-by-session-and-holds-what-left-the-working-set]]).

**And it is why nothing is deleted.** Cheapening the read path and destroying the record are
different operations, and this ruling asks for the first alone
([[the-lessons-cycle-is-the-owners-and-a-lesson-leaves-when-a-page-outside-lessons-cites-it]]).

# It is measured in tokens **and** in pages, and neither substitutes for the other — 2026-08-30

**owner, 2026-08-30: «Чистка меряется и токенами и страницами.»** Said against a fork the session had
framed as *tokens or pages*, and both halves are the answer.

**What that obliges: a session reporting one of the two has reported half.** Cutting 70,323 bytes off
the catalogue is a token saving with the page count untouched; archiving 250 decisions is a page
saving whose token effect on a dispatch is a different number. **Quoting either alone reads as
progress on the whole.**

**The tokens half was done on 2026-08-30 and the pages half was not.** `bash scripts/vault-catalogue.sh`
went from 201,927 bytes to 131,604 — about 17,500 tokens off every dispatch — and the corpus **grew**,
597 to 598 during the session and by roughly thirty more at its ingest
([[this-session-is-compiled-without-compressing-what-it-wrote]], [[vault-scripts]]).

**The other fixed cost the same day's measurements name, and no ruling touches it**:
`job_hunt_ai_vault/CLAUDE.md` is 25,020 bytes paid by every dispatched agent, and the two reading
agents of one `/ingest` cost 281,233 tokens between them. **A session start loads about 27 KB** —
the repository's `CLAUDE.md` at 10,735 and `brief.md` at 16,464 — and nothing else of the vault.

**The pages half has a unit now and no verdicts.** It is a family rather than a page — 99 verdicts
rather than 469 ([[the-authority-register-groups-the-corpus-and-the-family-is-the-unit-of-a-cleanup]])
— and the verdicts do not exist.

*(Extended 2026-08-30 from `raw/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md`.)*
