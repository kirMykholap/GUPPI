## Case 988 — The form of a ledger line is read without waiting for a new tag

> **context:**
> `rule-ratification` is `draft` for one reason. The cascade of `.guppi/guppi/generate.py` (the method `cascade` of its generator) sets a rule `built` only when each Estimate in its `estimates` stands `passed`, and `estimate-ratification-ledger-line-form` stands `pending`. Its `method`, set by case 961.5, waits for a lesson line that declares a new tag by a `{newtag:...}` block. A Grep for `\{newtag:` over every `ledger.md` under `vault/` printed nothing, so no session has written such a line. While the page is `draft`, `drafts` of `.guppi/guppi/ship.py`, through `is_draft_core` of `.guppi/guppi/pages.py`, gives a line for it, and `guppi ship` writes no clean version without `--allow-draft`. The brief of the last librarian's run (`vault/wiki/brief.md`, `## Flags`) reports that `guppi check` printed 13 lines, `rule-ratification` among the 10 lines `status: a page with core: true that is draft`. The other lines of the Criterion can be read now: a Grep for `\{addresses:|\{addressed_by:` over the ledgers under `vault/archive/plugin/` printed a count of 8 matches in five files, the five files the `method` names, and `vault/archive/migration/2026-10-04/1439/raw/ledger.md` stands. The new-tag block is checked from the side of the ledger hook by `estimate-ledger-write-refuses-a-lesson-with-an-unlisted-tag` of `rule-ledger-write`, which stands `passed`: the hook writes no lesson line whose tag `vault/wiki/tags.md` does not hold unless a `{newtag:...}` block declares it, so no line of another form reaches a ledger. This Case writes the Criterion again without the new-tag line, and its `method` reads the archived ledgers at Retro. The rule that governs the `method` is `rule-estimates-schema`: a reading by hand names the place of its evidence, the transcript of a session under `~/.claude/projects/` included, which the new `method` keeps. The sentence of the Render of `rule-ratification` on the `{newtag:...}` block stays true, and the hook's Estimate checks it. The put-off of `decision-case-907`, the removal of `PLAIN_SPRINTS` from `.guppi/guppi/caseid.py` after the sprint `plugin` closes, stays as it stands, so this Case carries no `{supersedes:case 907}`: `next_id` of that file gives a sprint that `is_plain` does not accept a number such as `plugin-1`, so the removal before the close would break the plain numbers of the open sprint, and the put-off sets no status of the page. A Grep for `ratification-ledger-line-form` over `vault/wiki/`, `.claude/`, `.guppi/guppi/` and `.guppi/tests/` printed `vault/wiki/brief.md`, `vault/wiki/log.md` and `vault/wiki/rules/rule-ratification.md`; the rule page lists the Estimate in `estimates`, which stands, and no test reads the Estimate's live file. The `estimates` of `rule-ratification` hold two more Estimates: `estimate-ratification-loaded` speaks of the loading of `ratification.md`, and `estimate-ratification-case-id-carries-the-sprint` of Case ids, so neither changes. The session's ledger holds no `lesson[error]` line, so this Case adds no mark.

> **problem:**
> `rule-ratification` stays `draft`, and blocks the clean version, because its check of the ledger-line form waits for a lesson line with a new tag that no session has written, while the rest of that check can be read now and the new-tag form is already checked from the side of the hook.

> **recommend:**
> - **What happens to the put-off removal of the sprint list**
>   - Recommended: (a) leave it waiting: the put-off stays, and the removal waits for the first session after `plugin` closes.
>   - Answer: agreed, (a).
> - **How the check of the ledger-line form gets its reading**
>   - Recommended: (a) drop the new-tag line from this check and read the rest at Retro, from the archived ledgers and their transcripts; the new-tag form stays checked by the hook's Estimate.
>   - Answer: agreed, (a).

> **given:**
> `estimate-ratification-ledger-line-form`: its Criterion is replaced whole and its `method` changes.
> **＋** `rule-ratification`: the rule it checks, rendered into `vault/wiki/ratification.md`.
> **＋** `estimate-ledger-write-refuses-a-lesson-with-an-unlisted-tag`: the check of the new-tag block from the side of the ledger hook.
> **＋** `rule-estimates-schema`: the form of a `method`.

> **when:**
> The agent writes the ledger lines of a session — the decision lines in the reply that acknowledges a ratification, a lesson line the moment the lesson exists — with `vault/wiki/ratification.md` rendered from `rule-ratification`.

> **then:**
> A decision line is `- decision[case N][kind][slug]` with `{ref:...}` when the target has a ref, `{tags:...}` on a `create`, and `{supersedes:case N}` when it applies.
> **＋** A line that supersedes more than one Case carries one `{supersedes:case N}` block per Case, side by side, never a list inside one block.
> **＋** A Case that takes up a deferred decision carries, on one of its decision lines, one `{supersedes:case N}` block for each Case in the page's `deferred_by`.
> **＋** When a Case of this session closes the root cause of a lesson of this session, the line written second carries the mark: `{addresses:<lesson slug>}` on the decision line when the lesson line stands first, `{addressed_by:case N}` on the lesson line when the decision lines stand first; one mark per lesson.
> **＋** For a Case with sub-cases, the `N` of `{addressed_by:case N}` is the sub-case whose decision line closes the cause, never the parent, which has no decision line.
> **＋** The mark stands in the preview of the ledger lines the person ratifies, or in the `LEDGER` block of the lesson line.
> **－** A lesson whose fix is ratified in another session gets no mark.

> **tasks:**
> - [ ] update `estimate-ratification-ledger-line-form`
>   - set:
>     ```
>     status: pending
>     method: "by hand, at Retro: the decision and lesson lines that carry an addresses or addressed_by mark in vault/archive/plugin/2026-10-14/0232/raw/ledger.md, vault/archive/plugin/2026-10-14/1536/raw/ledger.md, vault/archive/plugin/2026-10-16/2104/raw/ledger.md, vault/archive/plugin/2026-10-17/2307/raw/ledger.md and vault/archive/plugin/2026-10-29/2341/raw/ledger.md, and the line in vault/archive/migration/2026-10-04/1439/raw/ledger.md that takes up a page with two Cases in its deferred_by, each with its preview in the transcript of its session under ~/.claude/projects/, read against the Criterion, all recorded in one estimate line (the take-up line is that of case 629.2)"
>     ```
>   - change: `the Criterion replaced whole — the new-tag block of a lesson line is left to the check of the ledger hook; the method reads the archived ledgers and waits for no new tag`
> - [ ] read `estimate-ratification-ledger-line-form`

> **ratification:**
> ```
> - decision[case 988][update][estimate-ratification-ledger-line-form]{ref:rule-ratification}
> ```
