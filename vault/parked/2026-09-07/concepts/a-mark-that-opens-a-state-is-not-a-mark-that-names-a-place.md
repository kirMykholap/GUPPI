---
title: "A mark that opens a state is not a mark that names a place, and the gate may only judge an address"
type: concept
status: current
authority: mark-state-versus-address
basis: human
sprint: S3
created: 2026-08-23
sources: ["archive/2026-08-23/2026-08-23-the-archive-becomes-history-and-three-refusals-land/handoffs/2026-08-23-the-archive-becomes-history-and-three-refusals-land.md", "job_hunt_ai_vault/CLAUDE.md", "scripts/vault-check.sh"]
tags: [vault, record-schema, harness]
---

# The distinction

**Some frontmatter values are addresses and some are stages, and the two are read by different
parties.**

- **An address** says where the page belongs *now*. `status: deprecated` is one: the page was
  replaced because it went false, there is nothing to wait for, and a `deprecated` page still
  sitting in `wiki/` is a violation the gate prints. Rule 7 has said so since the beginning.
- **A stage** says what is being done to the page. `status: implemented` is one: the page has
  been realised, and it now waits in `wiki/` while it is tested for having someone who points at
  it. It moves when it passes ([[an-implemented-proposal-moves-to-archive-and-the-successor-carries-its-claim]]).

**The gate may enforce an address and may not enforce a stage.** An address is a claim about the
tree, comparable against the tree in one pass. A stage is a claim about a process, and the tree
cannot say whether the process has finished — only the instrument that performs it can, at the one
moment it decides something.

# Where the distinction was learned, and it cost a verdict written and removed in one day

**On 2026-08-23 a gate verdict named `realised` was built.** It reddened any page carrying
`status: implemented` while still under `wiki/`, and its message said the page was not `deprecated`
on the way out and carried no `superseded_by:`. **It existed for about an hour and is not in the
tree.**

**What was wrong was the reading, not the mechanism.** `implemented` had been read as an address —
*this page belongs in `archive/`* — and it is a stage. The owner said so in as many words:

> **owner: метка несет показатель, что ее должны проверить (наверно lint или кто-то еще) явялется
> ли файл сиротой. Если ниодно запись не ссылается на запись с меткой "implemented" - Значит это
> ошибка. Любая запись с меткой "implemented" должна иметь того, кто на нее ссылается, хотя бы
> одного.**

> **owner: запись с меткой "implemented" лежит в wiki до тех пор, пока она не проверится на
> сиротство. Как только она проходит этот тест - запись отправляется в архив, и сама ссылка на нее
> переписывается у всех, кто на нее ссылался.**

**So the gate judges `implemented` not at all**, and a page carrying it inside `wiki/` is legitimate
and expected. The test lives in `scripts/vault-archive.sh`, which refuses the move while no live
page names the slug — the one place in this harness that decides whether the stage has been passed
([[vault-archive-sh]]).

# Why the reading is the reusable half rather than the verdict

**A verdict removed the same day it was written costs an hour. Reading every mark as an address
costs one of these per mark.** The question to ask of a new value, before any check is written, is
*does this say where the page is, or what is happening to it* — and only the first kind has a
mechanical reader in the gate.

**The two failure directions are not symmetric.** Reddening a stage locks out the party doing the
work: the page cannot legally exist in the state the process requires, so the process cannot run at
all. Failing to redden an address leaves a page in the wrong folder, which the next sweep finds.
**Prefer leaving a mark unjudged over reddening the interval a process needs**, which is the same
reasoning that made the filename verdict an advisory while the title verdict stayed red
([[the-filename-verdict-is-an-advisory-while-the-title-verdict-is-red]]).

**The stage still owes an instrument, and its absence is the known gap.** Nothing today lists the
pages waiting in `implemented`, so a page that will never pass the orphan test looks exactly like
one that has not been tested yet. The owner named the shape — *наверно lint или кто-то еще* — and
it is not built.
