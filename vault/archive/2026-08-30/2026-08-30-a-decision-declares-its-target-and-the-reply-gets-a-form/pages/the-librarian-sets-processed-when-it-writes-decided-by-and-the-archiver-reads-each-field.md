---
title: "The librarian sets `processed` when it writes `decided_by:`, and the archiver reads each field"
type: decision
status: archived
superseded_by: [[the-archiver-marks-and-moves-a-decision-in-one-pass]]
authority: processed-writer
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-29
created: 2026-08-29
sources: ["archive/2026-08-29/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md", "scripts/vault-archive.sh", "wiki/decisions/_schema.yaml"]
tags: [vault, record-schema, process]
---

# The ruling, 2026-08-29

**owner:** «если у какой-либо страницы есть decided_by со ссылкой на decision - этот decision должен
стать processed и уйти в архив. То есть у библиотекаря должна быть инструкция при добавлении поля
decided_by - выставить processed у decision, на который ссылаемся. А уже архиватор проходит и по
decided_by и по processed(предохраянем себя от ошибок агента). processed по сути остается косметикой,
но далее мы его будем использовать»

**Two halves, and the second is the guard on the first:**

- **The librarian sets `status: processed` on the decision it points at**, in the same act as writing
  `decided_by:` on the page it produced.
- **The archiver selects on `decided_by:` *and* on `processed:`** — the second as insurance against
  the agent forgetting, not as a second criterion with its own meaning.

**`processed` stays cosmetic for now and will be used later.** His words, and it is why the mark
obliges nothing beyond being set.

**Rejected: the archiver selecting on `decided_by:` alone**, which would make an agent's omission
invisible; and **`processed` as the sole selector**, which would make the sweep depend entirely on an
agent having remembered.

# What it obliges

**A librarian instruction that does not exist yet.** It is named as a deferral in the journal that
recorded the ruling and needs an item of its own; nothing in `.claude/skills/ingest/SKILL.md` says it
today.

**A one-off back-fill over the decisions already named in a live `decided_by:`** — about 44 of them —
**asked of the librarian at the next `/ingest`**, which the owner selected in the same session
([[the-only-cases-live-in-the-hook-suite-and-the-expensive-pair-is-kept]]).

**It reaches nothing on its own.** `wiki/` held 757 `current`, 4 `implemented`, 1 `idea`, **0
`deprecated` and 0 `processed`** on 2026-08-28: the mark's criterion selects zero because no librarian
has ever been asked to apply it. That is the shortfall this ruling names, not a defect in the value
([[a-decision-is-processed-when-a-live-page-names-it-in-decided-by]]).

# What it corrects on the page that minted the mark

**That page says the librarian sets `processed`, and this session read it as the decisions agent's
mark.** The mechanical route is available today and reaches about 44 of 341 decisions; nothing carries
the mark only because nobody has been asked. The correction is recorded here rather than argued: the
page is right and the reading of it was wrong.

*(Compiled from `raw/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md`.)*

# The instruction exists now, and the back-fill is two decisions rather than about 44 — 2026-08-29

**The librarian instruction this page called for is step 3b of `.claude/skills/ingest/SKILL.md`**:
`status: processed` is set on the decision named, **in the same act** as writing `decided_by:` on the
page it produced. The deferral above is discharged by that step and by nothing else.

> [!CAUTION] THE FIGURE "ABOUT 44" IN *WHAT IT OBLIGES* IS FALSE AS OF 2026-08-29
> **The one-off back-fill is 2 decisions.** 60 live pages carry `decided_by:`, naming 45 distinct
> targets; **2 are live decisions and 43 are already in `archive/`**, and an archived target is kept as
> it stands rather than repaired. **The sweep of 2026-08-29 consumed the back-fill's subject** — the
> figure was true when it was written and the sweep ran between.

**`processed` is permanent where `decided_by:` is a pointer, and that is why the archiver reads both.**
A page whose `decided_by:` later moves to a newer decision would strand the earlier one — named by
nothing and retired by nothing. The mark survives the move; the pointer does not.

**And `processed` opens a state rather than naming a place.** The decision stays where it is until a
sweep moves it, and the gate judges the mark not at all — the same reading already settled for
`implemented` ([[processed-means-the-decisions-content-moved-on-and-the-mark-opens-a-state]]).

**One asymmetry the sweep leaves standing.** The successor check fires only on `status: deprecated`
(`scripts/vault-archive.sh:239`) and the sweep writes `status: archived`, so a **repeal** taken by the
`decided_by:` criterion is never asked for its `superseded_by:`. For a spent decision the absence is
correct; a repealed one owes a successor, and nothing distinguishes the two at the moment of the move
([[vault-archive-sh]]).

# Retired 2026-08-30, one day after it was written

**Superseded by [[the-archiver-marks-and-moves-a-decision-in-one-pass]].** The archiver checks the
criterion, sets the mark and moves the page in one pass; the librarian sets no mark at all.

**What removed this rule is that its ground was dissolved, not outweighed.** The split rested on the
mark being a **judgement** that only a reader could make. Case 2.3 of 2026-08-30 replaced that
judgement with a mechanical criterion — the two-way handshake, where the target names the decision
back ([[a-decision-declares-its-target-and-the-handshake-closes-it]]) — so there was nothing left for
a reader to decide and no reason for two actors.

**The mark this page is named for no longer exists either.** `processed` was repealed the same
evening, on a defect found while writing the archiver
([[processed-is-repealed-and-the-mark-it-carried-is-derived]]).

*(Compiled from `raw/handoffs/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds.md`.)*
