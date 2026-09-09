---
title: "The staleness checks run at different times and ask different questions — and none subsumes another"
type: concept
status: current
authority: staleness-timing
basis: code
sprint: S0
created: 2026-08-14
sources: ["archive/2026-08-14/2026-08-14-acceptance-and-the-shortened-claude-md/handoffs/2026-08-14-acceptance-and-the-shortened-claude-md.md", ".claude/skills/ingest/SKILL.md", ".claude/hooks/session-brief.ps1"]
tags: [vault, process]
---

# Two checks, and they are not redundant

| | Step 8 of `/ingest` | The `SessionStart` hook |
|---|---|---|
| When | at the end of a session, **before the brief is written** | at the start of the next session, before anything is done |
| Question | *does this journal match the tree right now?* | *have commits landed since the one carrying `brief.md`?* |
| Asked of | `git log` over the journal's `commits:` range, and `git status --short` | git history, with the commit carrying `brief.md` as the zero point |
| What it protects | the brief about to be written | the reader about to trust the brief |

**Neither uses a file's mtime**, and that is a decision with two scars behind it —
[[the-brief-is-stamped-with-its-commit]] and [[session-hooks]].

**Step 8's `git status` half needs one caution**, and it is measured: a bare count of modified
files overstates a session's work here, because a line-ending churn flags files whose content is
byte-identical. Quote `git diff --numstat` beside it —
[[line-endings-make-git-status-overstate-what-changed]].

## Why both

The first one exists because **a journal is testimony about a tree that has since moved.** A
session writes `commits: none` in good faith and something lands after it; the librarian compiles
from the journal but must state the measured tree beside what the journal claims, and never edit
the journal to agree ([[journal-vault-brief-each-artefact-has-one-owner]]).

The second exists because **the brief is fine when written and rots afterwards.** Nothing in its
text distinguishes a brief overtaken by six commits from one generated a minute ago.

They fail in opposite directions and neither can see the other's failure: a perfectly current
journal can produce a brief that six commits then overtake, and a brief committed seconds ago can
have been compiled from a journal that was already wrong when it was written. **Two checks, because
there are two moments.**

## A third one arrived on 2026-08-15, and this page did not have it

**Rule 9 of `vault-check.sh` is a staleness check too**, added in `b58ec48` with
`scripts/vault-catalogue.sh`: *is `catalogue.md` still what the generator produces?* Its moment is
a third one — **after every write under `wiki/` or `archive/`**, not at a session's end and not at
the next session's start — and it asks about a derived file against its own source rather than
about a testimony against a tree. It obeys the property the table above turns on: it compares by
**regenerating and diffing, never by mtime**, and the reason it gives is this project's own first
staleness check firing on every fresh clone ([[vault-scripts]],
[[the-catalogue-is-generated-not-maintained]]).

**The title and the table still say two.** Whether the catalogue check belongs inside
`authority: staleness-timing` — a third row here — or outside it as a different subject is a
judgement about the store's shape, so it is named and left: found by the first `/vault-lint`,
2026-08-15, and the outcome is the owner's.

**Formally deferred the same day**, as one of six findings owed to him:
[[the-audits-findings-are-owed-to-the-owner]]. Retitling this page is supersession, not an
edit, and **the run that falsified a title is the wrong one to erase it** — the retired page is the
record of why the claim was ever made. So this page stays `current` with a title that is false
today, and says so here rather than quietly.

---

**Its title and its filename are both false, and the retitle is undecided.** There are three checks,
not two, and this page says so in its own text. Unlike the other outstanding retitle, **the owner
has not decided this one** — and the filename is false too, so the cost is higher: a rename moves
the search surface as well as the claim ([[filenames-carry-no-category-prefix]],
[[a-title-names-what-is-counted-instead-of-counting-it]]). Row and consequence:
[[structure-work-agreed-and-not-executed]].

## Closed 2026-08-19, in both halves and two days apart

**The title was corrected in place at `b6fc6d8`, on 2026-08-17** — it names the question the checks
differ on instead of counting them — so *"the title and the table still say two"*, *"a title that is
false today"* and *"the retitle is undecided"* describe a state that had already ended when the
paragraphs above were last read. They stand as written, because the run that falsified a claim is
the wrong one to erase it ([[a-title-corrected-in-place-is-not-a-supersession]]).

**The filename was renamed on 2026-08-19**, in the sweep of sixteen names that closed the address
half of the rule ([[the-title-rule-extends-to-filenames]], [[a-page-rename-is-sed-and-verify]]).
That is what *"the filename is false too, so the cost is higher"* was waiting on, and the cost was
paid once for all sixteen rather than per page.

**What is not closed is the table.** It still lists two checks and rule 9's catalogue check is
still a third one with a moment of its own. Whether it is a third row of
`authority: staleness-timing` or a different subject is the judgement named above, and it is the
owner's — nothing here decides it.
