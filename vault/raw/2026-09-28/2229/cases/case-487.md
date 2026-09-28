## Case 487 — A broken code fence is a finding of pre-spec and of lint

> **context:**
> A code block in a page opens on a line of three or more backticks and closes on a line of the same backticks with nothing after them. If text follows the backticks on that line, Markdown does not read it as a close. The block stays open and swallows the text after it. Today nothing checks this. `/pre-spec` applies each `replace` and `reword` pair of the plan to copies of the pages in memory, but it only counts how often each anchor is found. It never looks at what the pair leaves behind. `guppi lint` has no check of code blocks. `make style` runs ruff on Python only. So a pair whose `new` ends on a closing fence, anchored in the middle of a line, joins the rest of that line to the fence. Case 483 did this to `rule-retro`, and only the librarian found it, by eye. Case 486 of this session fixes that page.
> The person agreed on one judgment in one module, called from both sides. `fence_breaks` in `guppi/materialize.py` sits beside `fence_opening` and `closes_fence`, the one judgment of a fence since case 444.1. `/pre-spec` calls it on each section that a pair changes and reports only a break the pair adds. It also calls it on each section text that a `sections` value writes whole. `lint` calls it on every section of every live page. The person chose two promises, each with a new Estimate, and chose to check the pages only. A harness file is a copy of its Render, and `render --check` already reports any difference. The person also chose to drop the full trial run of `materialize`, `generate` and `render` in Work Mode: it would not have caught this break, and nothing about it is recorded.
> A grep of the live pages for a fence line with more than one word after its run found two lines. One is in `rule-retro` (line 73), which case 486 fixes. The other is in `rule-synthesis` (line 70), "``` One lesson without a pair": the sample entries of the librarian's synthesis run on into its instructions. The person chose to fix it here, as 487.3. At pre-spec, a third page came to light: `decision-case-13`. Its line 35 opens a `markdown` fence that no line closes, so the block swallows its `## History`. The person chose not to fix it here. It stays with the other old Decision pages of cases 1–28 and their 62 `schema` findings, which are debt of Slice 4 and 5.
> The vault's answer: both `create` items are Estimates with a `ref`, so no vault query ran. No live page speaks of a broken code fence. The frame:
> - `estimate-prespec-simulates-the-pairs` promises the anchor counts. It stands, and its `－` line on meaning stays true, because a fence is structure, not meaning.
> - `estimate-lint-catches` lists the classes of lint and the form of a finding line. The new class keeps that form, so it stands.
> - `estimate-case-check-sends-back-a-faulty-case` promises that the answer check runs `judge` of `guppi/prespec.py`, which calls `check_pairs`. So the new finding also sends a broken pair back to `case-guppi` before the person sees it, with no change to that Criterion.
> - The estimates of `rule-synthesis` speak of clustering, not of the layout of the file, so no Estimate is touched there.
> - At pre-spec, the vault query found that `estimate-materialize-judges-a-fence` speaks of the change. Its `When:` lists every reader of a fence but not the two new callers. Its line that "a word after its run stays inside the fence as content" is still true of the parsing, but that line is now what `fence_breaks` reports as a break. The person agreed to 487.4, which replaces that Criterion whole.
> - `lint` only goes red, so it keeps no old form. From Work Mode until the librarian's run writes the fixes of 486 and 487.3, `make lint` reports `rule-retro`, `rule-synthesis` and `decision-case-13` under the class `fence`. After that run it still reports `decision-case-13`, so `lint` stays red on `fence`. That red is a note for the handoff, by `rule-retro`.
> - The two new Estimates and the one set `pending` are read in a later session (case 428.1).
>
> The answer check noted that some `then` lines of 487.2 and 487.4 share words with 487.1. This is expected: 487.1 defines the judgment, 487.2 applies it, and 487.4 keeps the parsing lines of the old Criterion word for word. The check also noted that the old `When:` of `estimate-materialize-judges-a-fence` is not carried. That is on purpose: the new `When:` adds the two new readers.

> **problem:**
> A `replace` pair, or a section written whole, can leave a code fence broken in a page. Neither `/pre-spec` nor `lint` looks for this. So the break reaches the vault and the rendered harness files, and only someone reading by eye catches it.

> **recommend:**
> Four sub-cases. 487.1 adds `fence_breaks` beside the fence judgment in `guppi/materialize.py` and calls it from `check_pairs` in `/pre-spec`, as a finding. 487.2 adds the class `fence` to `guppi lint`, which imports the same function. 487.3 fixes the break that already stands in `rule-synthesis`. 487.4 brings the promise of the one fence judgment up to date with its two new readers and the new break. Each of 487.1 and 487.2 is its own promise with its own Estimate, because either can fail while the other passes, and the fix is then different. Folding them into the existing Estimates was rejected: it would put two promises under one Case and send a passed `lint` Estimate back to unread.

### Case 487.1 — Pre-spec reports a code fence that a pair or a written section breaks

> **given:**
> `rule-prespec` — its Render, the text of `/pre-spec` on the pairs of the plan
> **＋** `.claude/skills/pre-spec/SKILL.md` — the skill rendered from `rule-prespec`
> **＋** `guppi/materialize.py` — the one judgment of a fence; `fence_breaks` joins it
> **＋** `guppi/prespec.py` — `check_pairs` and the docstring of the checks; owned by `rule-prespec-hook`
> **＋** `tests/test_materialize.py` — the cases of `fence_breaks`
> **＋** `tests/test_prespec.py` — the cases of the pre-spec finding
> **＋** `estimate-prespec-catches-a-broken-fence` — the new promise

> **when:**
> `uv run guppi prespec --check <plan> --session <id>` applies the `replace` and `reword` pairs of the plan to copies of the pages in memory, and reads the `sections` values of the `create` and `update` items of its `then` blocks.

> **then:**
> `fence_breaks` of `guppi/materialize.py` takes the text of one section and gives each break in it: a line inside an open code fence that starts with a run of the fence's character at least as long as the fence and has text after the run, and a fence still open at the end of the section.
> **＋** For each section a `replace` or `reword` pair changes, each break the section holds after the pair and did not hold before it gives one line: the Case, the page's slug, the section, and "a pair leaves a code fence with text after it" with the line, or "a pair leaves a code fence open at the end of the section".
> **＋** Each break in the text of a `sections` value gives one line of the same form, with "a sections value leaves" in place of "a pair leaves".
> **＋** Each such line is a finding: the check exits 1.
> **－** A break that the section held before the pair gives no line.
> **－** A run shorter than the fence it stands in, or a run of the other character, is content of the fence and no break.
> **－** No page is written, and a `sections` value is judged on its own and not applied to the copies, so the anchors are judged as before.

> **tasks:**
> - [ ] update `rule-prespec`
>   - old: `not as it stands today (case 351).`
>   - new:
>     ````
>     not as it stands today (case 351). It also judges, by `fence_breaks` of `guppi/materialize.py` — the one judgment of a broken code fence, which `guppi lint` runs too — each section a `replace` or `reword` pair changes, before and after the pair, and prints one line for each break the pair adds: a line inside an open fence that starts with a run of the fence's character at least as long as the fence and has text after it, or a fence still open at the end of the section, with its Case, the page's slug, the section and the line; a break the section held before the pair is not printed. It prints one such line too for each break in the text of a `sections` value of a `create` or an `update`, judged on its own and not applied to the copies (case 487.1).
>     ````
>   - change: `pre-spec reports a code fence that a pair or a written section breaks, by fence_breaks of guppi/materialize.py (case 487.1)`
> - [ ] create `estimate-prespec-catches-a-broken-fence`
>   - type: `estimate`
>   - ref: `rule-prespec`
>   - kind: `QA`
>   - purpose: `Whether pre-spec reports a code fence that a replace or reword pair breaks, or that a sections value leaves broken, and stays silent on a break the page already held`
>   - method: `uv run pytest tests/test_materialize.py tests/test_prespec.py -k fence`
>   - tags: `[harness, workflow]`
> - [ ] `guppi/materialize.py` — `fence_breaks(text)` beside `fence_opening` and `closes_fence`, built on them; the docstring paragraph on the fence names it and its callers
> - [ ] `guppi/prespec.py` — `check_pairs` judges each section a pair changes before and after the pair, and each `sections` value on its own, by `fence_breaks`; the module docstring names the finding
> - [ ] `tests/test_materialize.py` — `-k fence_breaks`: a closing run with text after it is flagged, a fence open at the end is flagged; a normal fence, an opening with a tag, and a shorter run inside a longer fence are not flagged
> - [ ] `tests/test_prespec.py` — `-k fence`: a pair that joins text to a closing fence gives the finding; a pair on a section that already held the break gives none; a `sections` value with an open fence gives the finding; a clean pair gives none; the page on disk is unchanged
> - [ ] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
> - [ ] read `estimate-prespec-catches-a-broken-fence`

> **ratification:**
> ```
> - decision[case 487.1][update][rule-prespec]{ref:rule-prespec}
> - decision[case 487.1][create][estimate-prespec-catches-a-broken-fence]{ref:rule-prespec}{tags:harness,workflow}
> ```

### Case 487.2 — Lint reports a broken code fence in a live page

> **given:**
> `rule-lint` — the checks of the live pages; the classes live in the docstring of `guppi/lint.py`
> **＋** `guppi/lint.py` — the new class `fence` and its place in the docstring
> **＋** `guppi/materialize.py` — `fence_breaks`, the one judgment lint imports
> **＋** `vault/wiki/<category>/` — the live pages lint reads
> **＋** `tests/test_lint.py` — the cases of the class `fence`
> **＋** `estimate-lint-catches-a-broken-fence` — the new promise

> **when:**
> `uv run guppi lint` reads the sections of the live pages under `vault/wiki/<category>/`.

> **then:**
> Lint reports each live page that `fence_breaks` of `guppi/materialize.py` judges broken with one `fence` finding per break, naming the page, its heading and the faulty line or the open end.
> **＋** A `fence` finding sets exit 1, like any other finding.
> **＋** `guppi/lint.py` imports the judgment and holds no second copy of the pattern.
> **－** A harness file on disk is not read for fences: `render --check` compares it with its Render.
> **－** Nothing is written.

> **tasks:**
> - [ ] create `estimate-lint-catches-a-broken-fence`
>   - type: `estimate`
>   - ref: `rule-lint`
>   - kind: `QA`
>   - purpose: `Whether lint reports a code fence with text after its closing run, or left open at the end of a section, in a live page, by the judgment pre-spec runs`
>   - method: `uv run pytest tests/test_lint.py -k fence`
>   - tags: `[harness, workflow]`
> - [ ] `guppi/lint.py` — the class `fence` after `markers`, over each section of each live page by `fence_breaks` imported from `guppi/materialize.py`; the docstring names the class in its order
> - [ ] `tests/test_lint.py` — `-k fence`: a page with a closing run and text after it, and a page with a fence left open, each give one `fence` finding; a page with normal fences gives none
> - [ ] read `estimate-lint-catches-a-broken-fence`

> **ratification:**
> ```
> - decision[case 487.2][create][estimate-lint-catches-a-broken-fence]{ref:rule-lint}{tags:harness,workflow}
> ```

### Case 487.3 — The synthesis sample closes its code block on its own line

> **given:**
> `rule-synthesis` — its Render: the closing fence of the sample entries and the sentence after it
> **＋** `.claude/agents/librarian-guppi.md` — the agent file rendered from `rule-synthesis`

> **when:**
> The librarian loads `.claude/agents/librarian-guppi.md` and reads the form of the synthesis entries.

> **then:**
> The sample of the synthesis entries is a code block that closes on a line that holds the fence alone.
> **＋** The sentence "One lesson without a pair stays `new`" and the instructions after it stand after the block as their own paragraph, with their words unchanged.
> **－** The text of the sample and of the instructions does not change.

> **tasks:**
> - [ ] update `rule-synthesis`
>   - old: ```` ``` One lesson without a pair ````
>   - new:
>     ````
>     ```
>
>     One lesson without a pair
>     ````
>   - change: `the closing fence of the sample entries stands alone on its line, and the sentence after it follows as its own paragraph (case 487.3)`
> - [ ] `uv run guppi render`: `.claude/agents/librarian-guppi.md`

> **ratification:**
> ```
> - decision[case 487.3][update][rule-synthesis]{ref:rule-synthesis}
> ```

### Case 487.4 — The one fence judgment names its new readers and the break

> **given:**
> `estimate-materialize-judges-a-fence` — the promise of the one fence judgment; its Criterion replaced whole
> **＋** `guppi/materialize.py` — the functions of the judgment, `fence_breaks` among them
> **＋** `guppi/ratified.py` — `fenced_value`, a reader
> **＋** `guppi/prespec.py` — `plan_prose` and `check_pairs`, readers
> **＋** `guppi/casecheck.py` — the check of `ratification`, a reader
> **＋** `guppi/ledger.py` — `ledger_lines`, a reader
> **＋** `guppi/lint.py` — the class `fence`, a reader

> **when:**
> A hook or a script reads a text that holds a fence: `then_blocks`, `tagged_blocks`, `quoted_sections` and `criterion_text` of `guppi/materialize.py`, `fenced_value` of `guppi/ratified.py`, `plan_prose` and `check_pairs` of `guppi/prespec.py`, the check of `ratification` in `guppi/casecheck.py`, `ledger_lines` of `guppi/ledger.py`, or the class `fence` of `guppi/lint.py`.

> **then:**
> A line opens a fence when, after at most three spaces of indent inside the block it stands in (a quote, a sub-point of `tasks`), it starts with a run of three or more backticks or three or more tildes.
> **＋** The fence closes only on a line of the same character whose run is at least as long as the opening run, with nothing after the run but spaces.
> **＋** A line with a shorter run, a run of the other character, or a word after its run stays inside the fence as content.
> **＋** `fence_breaks` is built on `fence_opening` and `closes_fence`, so each break it reports is a line these readers keep as content, or an end of section they reach inside a fence.
> **＋** A fenced value under a sub-point of `tasks` that holds a shorter fence of the same character is read whole, together with the inner fence.
> **＋** Every one of these readers takes the judgment from the functions of `guppi/materialize.py`, and they all give the same answer for the same text.
> **－** No reader keeps a fence pattern of its own: the `FENCE` of `guppi/ledger.py`, the `OPEN_FENCE` of `guppi/ratified.py`, and the tests on three backticks in `guppi/ratified.py` and `guppi/casecheck.py` are removed.

> **tasks:**
> - [ ] update `estimate-materialize-judges-a-fence`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — check_pairs of guppi/prespec.py and the class fence of guppi/lint.py join the readers, and fence_breaks, built on the same functions, reports a word after a full run inside a fence, and a fence open at the end of a section, as a break (case 487.4)`
> - [ ] read `estimate-materialize-judges-a-fence`

> **ratification:**
> ```
> - decision[case 487.4][update][estimate-materialize-judges-a-fence]{ref:estimate-materialize-judges-a-fence}
> ```
