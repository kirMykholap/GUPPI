---
type: decision
case: "494.3"
status: current
update: ["[[estimate-sprint-migration-merges]]"]
origin: raw/2026-09-28/2229/ledger.md#case-494.3
sprint: migration
created: 2026-09-28
tags: [sprint, git, tests]
---

## Context

Each Estimate page holds one promise, its Criterion. A Criterion should hold only `When:`, the trigger and the input it acts on, and `Then:`, what must hold after. Older Estimates also open with `Given:`, a set of lines that describe the code and the cases as they stood on the day the promise was written. This last group holds the five done-conditions of `entity-sprint-migration` that still carry `Given:`: lint clean, the leftovers gone, the branch merged, the Rule-class files dissolved, and `index.md` gone. `estimate-sprint-migration-file-route-gone` has no `Given:` and is not touched. Their `Given:` describes the vault of September: the 62 findings of Cases 1–28, the list of the leftover folders, the scripts of the old `file` route, the map `index.md`. The one on `estimate-sprint-migration-merges` is not its own: it describes the cascade, the guard and `sprint_id` from the parent Case 209.
The person decided in the first round on this item. The five are recut like the rest: `Given:` out, `When:` and `Then:` kept as the condition at the close. What becomes of them after the close stays with the open item of Slice 5 (case 478.2). A lost ratified text is restored, and a page with no `purpose` gets one. None of the five lost its Criterion to a tool fault like case 211.3. Their History shows only Criteria that cases 209, 229.1, 233.5, 244, 301, 306.7, 310.3, 318, 321, 329 and 367 wrote on purpose, so nothing is restored and no commit needs to be read. All five have `purpose` and `method`, so no field is set but `status`. Each Criterion is replaced whole and goes back to `pending`. Its reading waits for the close of the sprint, or for a later session (case 428.1).
What each new Criterion keeps and drops. The check of the answer notes every old line as not carried, because each new line is a whole statement and not the old wording. The content of the old lines is carried, except for the lines named here. Each `Given:` goes out. In 494.1 the line that the page `entity-sprint-migration` exists with its sections, and the `－` line on item F7 and "today's `sprint.md`", record the one-time build of the page in case 209.2, so they go out (case 485). In 494.3 "the render shows the three Done-when lines `[x]`" is a count that went stale, because the page now lists six Estimates. It becomes "every Done-when line". In 494.4 the pointer "`make lint` is the reading of `estimate-sprint-migration-lint-clean`" goes out. The two `－` lines on what Slice 3f did not do, the Renders `case-schema.md` and `CLAUDE.md` and the template engine, go out as bounds of an edit, and the template engine stays in the Backlog. The edge of `rule-sprint` to `entity-sprint` is named in words, "the sprint's rule to the sprint MOC", so that `given` stays within its frame. In 494.5 the old `When:`, "The last Case of theme 4 is applied by the librarian", is a one-time trigger. It becomes the reading its `method` names, the tree read for `§N` and `index.md`. Paths inside the promises are named in `given` or written in words, because a code span with a `/` reads as a path that `given` must name.
The check also notes that 494.5 shares words with 494.4, since both say that `index.md` does not exist. This is expected. They were ratified as two done-conditions of the sprint by cases 301 and 310.3. 494.4 promises that no Rule-class file stands at the close of Slice 3f, and 494.5 promises that no pointer to the map remains in the tree. The recut keeps both as the person signed them.
The note. Every item of the current milestone decides the Frontier: `guppi sprint` shows a line with no `[[slug]]` before its first ` — ` as a note, `- [ ] <text>`, and never ticks it. It leaves only by the `update` of the Case that ends it (case 313). This is the last group of the item, so 494.6 removes the line from `## Milestones` of `entity-sprint-migration` with one `replace` pair, and `uv run guppi sprint` writes the new `vault/wiki/sprint.md` at the librarian's run. The anchor of the pair runs from the note to the start of the next line, since a line break matches any whitespace, and its `new` keeps that start. So the pair removes one line and hits the page once. The other note of Slice 3g, on the old shape, stays word for word. Its "until lint counts no `unmigrated` page" keeps `estimate-end-of-work-order` on the Frontier, since its `## Context` and `## Method` sections count as `unmigrated`, and the first round left its `Given:` to that item. Slice 3g stays current with that one note, and no line goes to `## Closed` until the Slice closes.
The frame. Each kept line was read against the sprint page, the `Makefile` and the tree. The sprint page lists six Estimates in `estimates`. No behaviour changes, so no code, test, Render or hook changes, and no reader keeps an old form. `rule-sprint` and `guppi/sprint.py` read a note as it is described here. The Case creates no page, so no vault query was run. Not done: the fate of a sprint's done-conditions after the close (case 478.2), and the old-layout item C2.

## Problem

The five done-conditions of the sprint still open with a `Given:` of the vault as it stood in September, and some lines record the build of the page or a count that went stale. The item that asks for this recut also stands as an unticked note in Slice 3g, and nothing but a Case removes it.

## Given

`estimate-sprint-migration-merges` — the promise, its Criterion replaced whole
**＋** `entity-sprint-migration` — the sprint page it is a done-condition of
**＋** `Makefile` — the target `test`
**＋** `guppi/generate.py` — the cascade that sets the page `built`
**＋** `vault/wiki/sprint.md` — the render that shows the Done-when lines

## History

- 2026-09-29 created · raw/2026-09-28/2229/ledger.md#case-494.3
