## Case 672 — A decision that closes an Estimate ticks its read lines

> **context:**
> After a session, the librarian runs `guppi generate`, which writes the pages and ticks the boxes of the Specs. It ticks the `read` lines of an Estimate across the live Specs of `vault/raw/` only for a reading, a `create` with a folded reading, or a `delete` (cases 270.1, 463). Case 669 of session 1831 set fifteen Estimates `passed` by the person's decision, through `update` items that set `status` and write the Criterion back (case 669.16). No reading of them stands in a ledger after the Cases that wrote their open `read` lines, so `generate` ticked none of their `read` lines, and nothing ever will. The brief lists such lines among the unticked boxes of the Specs, so they come back at every session.
> A Grep of the pattern that opens with `^- \[ \] read`, a space and a backtick, followed by the fifteen slugs of Cases 669.1 to 669.15 as alternatives in one group and a backtick, over `vault/raw/` printed eleven lines in two files: `vault/raw/2026-10-05/1616/spec.md` and `vault/raw/2026-10-05/0311/spec.md`. The person chose two things. First, `generate` ticks the `read` lines of an Estimate when it applies an `update` that sets the Estimate `passed` or `failed`, by the walk and the skips of a reading. Second, Work Mode of this session ticks the eleven lines once by hand, since the 669 entries are already applied and no run applies them again. A ticked line stays a plain `- [x]`: the `## Result` of each page already opens with the person's decision. The code judges the entry by its `set.status` alone. By `case-schema.md`, only an `update` by the person's decision sets an Estimate `passed` or `failed`. An `update` that sets `pending` keeps its `read` line open for its reading, as today.
> The promise is `estimate-generate-ticks-the-spec`. Its Criterion lists the entries that tick a `read` line, so this Case replaces it whole. The new Criterion keeps every old line as it stood, but for the lines that name the entries that tick a `read` line, the skip by `line`, the page and `read` lines of a `delete`, a repeat and a failed entry, which add the `update`. The `when` names `rule-page-generation` besides. Its `purpose` states the old list, so the same `update` sets a new one. Its `method` adds a reading of the Spec after the librarian's run, which `case-schema.md` no longer allows (case 670.4), so the new `method` is the tests alone, read at Retro of this session. By the person's answer, the one-time ticking has no Estimate. A `by hand` box of Work Mode checks it: the same Grep, over the two Specs alone, prints nothing. It runs over those two files because Case 674.2 of this session writes a `read` line of one of the fifteen slugs into this session's Spec, which stays open until Retro. The person judged that whether these boxes are ticked is not critical. At pre-spec the person called the hand ticking a one-time exception to the rule that Work Mode ticks no `read` line, and asked that it not be documented, so no rule changes for it.
> The pages. The Purpose of `rule-page-generation` names the entries that tick `read` lines, and the skip of a Case ratified after the reading or the `delete`. Two pairs add the `update`. A Grep of `ticks? (the |every |each |its )?(unticked )?`?read`? (line|box)|read` lines? whose|reading stands in the ledger` over `vault/wiki/`, `.claude/`, `guppi/` and `CLAUDE.md` printed `vault/wiki/orchestration.md`, `vault/wiki/log.md`, `.claude/skills/retro/SKILL.md`, `guppi/prespec.py`, `vault/wiki/rules/rule-retro.md`, `guppi/generate.py`, `vault/wiki/rules/rule-page-generation.md`, `vault/wiki/rules/rule-orchestration.md` and `vault/wiki/estimates/estimate-generate-ticks-the-spec.md`. The hits in `log.md` and in History lines are records. The Render of `rule-orchestration`, rendered to `orchestration.md`, says that `generate` ticks the `read` lines whose reading stands in the ledger. That would be false, so a pair rewrites it and the render follows. `estimate-orchestration-loaded` promises that the file equals the Render, is loaded, holds what the main agent alone does and is repeated by no other loaded file, none of which this sentence changes, so its Criterion stands (case 378.5). The docstring of `guppi/generate.py` changes with the code. The docstring of `estimates_to_read` in `guppi/prespec.py` says that `tick_read` ticks the `read` line of a renamed Estimate, which stays true. The Render of `rule-retro`, rendered to `.claude/skills/retro/SKILL.md`, counts as debt a `read` line with no reading in the Tail. A Case that closes an Estimate by decision writes no `read` line, so only a `read` line of an earlier Case of the same session meets this. Retro counts that line as debt, and the librarian's run then ticks it. Its text stays true, so it stands and is not changed here.
> A Grep of `rule-page-generation` over `vault/wiki/`, `guppi/`, `tests/`, `.claude/` and `CLAUDE.md` printed 17 files. The hits outside `log.md`, `brief.md` and History are the `target` of its Estimates, the `children` of `rule-documentation`, the backlog line, the pointer of `guppi/generate.py` to the page, and an exception of `estimate-sprint-items-move-only-by-a-case` on the moves of a sprint line. None speaks of ticking, so all stand. A Grep of `tick` over `vault/wiki/estimates/` with the glob `estimate-generate-*.md` printed only `estimate-generate-ticks-the-spec.md`, so no other Estimate of `rule-page-generation` speaks of the change. The defer of decision 469 on `rule-page-generation` concerns a supersede of an archived Decision. This Case does not take it up, and it stands. The Frontier line of this item has the source `brief`, not `backlog`, so no supersede mark is due.

> **problem:**
> When the person closes an Estimate as passed or failed by decision, `generate` leaves its `read` lines open in every Spec, and no later run ticks them. Eleven such lines stand open now in two Specs of earlier sessions, and the brief brings them back as work at every session.

> **recommend:**
> - **Whether the script ticks a read line when a decision sets the state of a check**
>   - Recommended: (a) a change that sets a check `passed` or `failed` ticks every open `read` line of that check in every live plan under `vault/raw/`, by the walk and the skips of a reading; a change that sets `pending` ticks nothing.
>   - Answer: agreed, (a).
> - **What happens to the eleven lines open now**
>   - Recommended: (a) Work Mode of this session ticks them once by hand, and no other line changes.
>   - Answer: agreed, (a).
> - **Whether a ticked line shows that no reading was taken**
>   - Recommended: (a) a plain tick; the page of the check records the decision.
>   - Answer: agreed, (a).
> - **How the one-time ticking of the eleven lines is checked**
>   - Recommended: (a) a new check, read in Work Mode of this session by one search that must print nothing.
>   - Answer: (b): no new checks are needed; whether the boxes are ticked or not is not critical. A `by hand` box in Work Mode runs the search.
> - **Change**
>   - Asked: at pre-spec the hand ticking was found to break the rule that Work Mode ticks no `read` line; the person answered that it is a one-time exception that needs no documenting.
>   - Taken: the hand-ticking task stays, no rule or Estimate of Work Mode is named or changed, and `context` records the exception; the `by hand` search now runs over the two Specs alone, with the backtick before each slug.

> **given:**
> `estimate-generate-ticks-the-spec`: the check of the ticks of `generate`, its Criterion, `purpose` and `method` replaced.
> **＋** `rule-page-generation`: the rule of `generate`, whose Purpose names the entries that tick `read` lines.
> **＋** `guppi/generate.py`: `Vault.tick`, `tick_read` and the docstring of the module.
> **＋** `tests/test_generate.py`: the tests of the ticks.
> **＋** `rule-orchestration`: its Render says who ticks which box.
> **＋** `vault/wiki/orchestration.md`: the file rendered from `rule-orchestration`.
> **＋** `vault/raw/2026-10-05/0311/spec.md` and `vault/raw/2026-10-05/1616/spec.md`: the Specs with open `read` lines of Estimates closed by decision.
> **＋** `vault/archive/`: the archive, whose Specs `generate` does not read.

> **when:**
> `uv run guppi generate` of `rule-page-generation` marks an entry of `materialize.yaml` `applied`. Either it applied the entry, or it found the entry to be a repeat: a `create`, `update`, `delete` or `defer` entry whose `case`, `kind` and `slug` match those of an entry of the same `materialize.yaml` already marked `applied`.

> **then:**
> For a `create`, `update`, `delete` or `defer` entry that was applied, in the `spec.md` of the same unit, the first unticked line `` - [ ] <kind> `<slug>` `` in the section of the entry's Case becomes `- [x]`. Nothing else in the file changes.
> **＋** For an `estimate` entry, a `create` entry with `folded`, a `delete` entry and an `update` entry whose `set` gives `status` the value `passed` or `failed`, every unticked line `` - [ ] read `<slug>` `` of every `spec.md` under `vault/raw/` becomes `- [x]`. The Spec beside the yaml comes first, then the Specs of the other session folders, oldest first.
> **＋** In the Spec beside the yaml, for an `estimate` entry, a `delete` entry or such an `update` entry, a `read` line in the section of a Case whose first decision entry carries a `line` greater than the entry's `line` is not the entry's line, and the search goes on.
> **＋** In any Spec, a `read` line in the section of a Case whose entries are marked `superseded_by` is not the entry's line. For the Spec beside the yaml, the marks come from the run's entries. For another Spec, they come from the `materialize.yaml` beside it. With no yaml beside a Spec, nothing is skipped there.
> **＋** A `create` entry with `folded` ticks both its page line and its `read` line. The filter by `line` does not apply to it, and the filter by `superseded_by` does.
> **＋** A `delete` entry, and an `update` entry whose `set` gives `status` the value `passed` or `failed`, tick both the page line in their own Case and the `read` lines of their slug.
> **－** An `update` entry whose `set` gives no `status`, or the value `pending`, ticks no `read` line.
> **－** A repeat ticks no line in any `spec.md`. A second line `` - [ ] <kind> `<slug>` `` in the section of its Case stays unticked, and a repeated `delete` or `update` leaves the `read` lines of its slug as they stand.
> **－** A line, a section or a Spec not found raises no error and prints nothing on stderr. The entry is `applied` all the same.
> **－** A `lesson` entry and an entry marked `failed` tick no line. A `delete` or an `update` that fails leaves the `read` lines of its slug as they stand.
> **－** A `spec.md` under `vault/archive/` is not read.

> **tasks:**
> - [ ] `guppi/generate.py`: `Vault.tick` ticks the `read` lines of an applied `update` entry whose `set` gives `status` the value `passed` or `failed`, by `tick_read` with the skips of an `estimate` entry; the docstring of the module and of `Vault.tick` say so.
> - [ ] `tests/test_generate.py`: an `update` that sets `passed`, and one that sets `failed`, tick the `read` lines of their slug beside the yaml and in an older Spec; one that sets `pending` or no status ticks none; one skips the `read` line of a Case ratified after it and of a superseded Case; a repeated one and a failed one tick none.
> - [ ] update `rule-page-generation`
>   - old: `` an `estimate` entry, a `create` with a folded reading, or a `delete`, whose Estimate no reading will ever reach (case 463), every unticked ``
>   - new: `` an `estimate` entry, a `create` with a folded reading, a `delete`, whose Estimate no reading will ever reach (case 463), or an `update` that sets an Estimate `passed` or `failed` by the person's decision, which no reading follows (case 672), every unticked ``
>   - old: `` stands after the reading or the `delete` in the ledger, a Case ratified after it ``
>   - new: `` stands after the reading, the `delete` or the `update` in the ledger, a Case ratified after it ``
>   - change: `an update that sets an Estimate passed or failed by the person's decision ticks its read lines across the live Specs, with the skips of a reading (case 672)`
> - [ ] update `rule-orchestration`
>   - old: `` `generate` ticks the page lines and the `read` lines whose reading stands in the ledger, ``
>   - new: `` `generate` ticks the page lines and the `read` lines of an Estimate that a reading in the ledger, a `delete` or an `update` that sets it `passed` or `failed` by the person's decision closes (case 672), ``
>   - change: `generate ticks the read lines of an Estimate a delete or a decision closes too (case 672)`
> - [ ] `uv run guppi render`: `vault/wiki/orchestration.md`
> - [ ] update `estimate-generate-ticks-the-spec`
>   - set:
>     ```
>     status: pending
>     purpose: "generate ticks the page line of a Case in the Spec beside its yaml, and the read line of a reading, of a deleted Estimate or of an Estimate an update sets passed or failed, across the Specs of raw/ — never a line of a later or a superseded Case"
>     method: uv run pytest tests/test_generate.py
>     ```
>   - change: `the Criterion replaced whole — an update that sets passed or failed ticks the read lines of its slug, with the skips of a reading; the method the tests alone (case 672)`
> - [ ] `vault/raw/2026-10-05/0311/spec.md` and `vault/raw/2026-10-05/1616/spec.md`: each open `read` line of an Estimate that Cases 669.1 to 669.15 set `passed` becomes `- [x]`; no other line changes.
> - [ ] by hand: a Grep of the pattern that opens with `^- \[ \] read`, a space and a backtick, followed by the fifteen slugs of Cases 669.1 to 669.15 as alternatives in one group and a backtick, over `vault/raw/2026-10-05/0311/spec.md` and `vault/raw/2026-10-05/1616/spec.md` prints nothing.
> - [ ] read `estimate-generate-ticks-the-spec`

> **ratification:**
> ```
> - decision[case 672][update][estimate-generate-ticks-the-spec]{ref:rule-page-generation}
> - decision[case 672][update][rule-page-generation]{ref:rule-page-generation}
> - decision[case 672][update][rule-orchestration]{ref:rule-orchestration}
> ```
