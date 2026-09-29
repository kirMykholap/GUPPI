## Case 492 — Slice 3g: the Estimates of the text every context loads recut to `When:` and `Then:`

> **context:**
> Each Estimate page holds one promise, its Criterion. A Criterion should hold only `When:`, the trigger and the input it acts on, and `Then:`, what must hold after. Older Estimates also open with `Given:`, a set of lines that describe the code and the cases as they stood on the day the promise was written. This group holds three such pages. Each promises a text that the agent reads when it acts: `CLAUDE.md` from `rule-claude-md`, the atomicity rule in `vault/wiki/case-schema.md`, and the one-judgment rule inside `CLAUDE.md`. Their `Given:` repeats how a Render is written and how the hook refuses a hand edit, and it also keeps history. For example, `estimate-claude-md-rendered` still lists each item of the old "Migration mode" section and the Rule it became, and `estimate-one-judgment-one-implementation-followed` names the three functions that case 351 lifted into one module.
> The person decided in the first round on this item. The item goes in seven Cases by area, one group per Case. History and the lines on the bounds of an edit leave the Criterion. A lost ratified text is restored, and a page with no `purpose` gets one. This group is the fifth, after cases 488 to 491. None of these pages lost its Criterion to a tool fault like case 211.3. Their History shows only Criteria that cases 73.10, 88.2, 272.1, 273.3, 288.3, 317, 360 and 374 changed on purpose, so nothing is restored and no commit needs to be read. All three pages already have `purpose` and `method`, so no field is set but `status`. Each Criterion is replaced whole and goes back to `pending`. Its reading waits for a later session (case 428.1). The note of Slice 3g stays as it is until the last group.
> What each new Criterion keeps and drops. The check of the answer notes every old line as not carried, because each new line is a whole statement and not the old wording. The content of the old lines is carried, except for the lines named here. Each `Given:` goes out. A `Given:` line that states lasting behaviour moves into `When:` or `Then:`: where a `partial` Render lands, that the governed-files hook refuses a hand edit, and that every session and subagent loads `CLAUDE.md`. In 492.2 the list of the "Migration mode" items and the Rules they became goes out as history, and so does the line that the glossary and the schema arrive with `/hi`, which `estimate-internal-context-loaded` promises. The first `then` line of 492.2 quotes the paragraph of `CLAUDE.md` in plain quotation marks, in place of the old summary in code spans. The quote keeps every word of the paragraph but drops the code spans around the vault folder, the glossary path and the skill that opens a session. A span with a `/` reads as a path that `given` must name, and the paragraph is text of the file, not a frame of the Case. So the check notes that line as not carried, while its content is the same. In 492.3 the functions that case 351 lifted go out as history. In 492.1 the `Given:` line on the refusal of `pre-spec` described the form before case 472.3, "two Estimate items and no written `sections: Criterion`". The `－` line keeps only that the refusal stays with `rule-prespec`, as the Purpose of `rule-atomicity` says today, so the stale form is not signed again.
> The check also notes that 492.1, 492.2 and 492.3 share a line on `render --check` and the governed-files hook. This is expected. Each promise guards a rendered text by the same two means, but each names its own file or its own markers, and a drift in one fails one reading alone.
> The frame. Each kept line was read against `CLAUDE.md`, the Render of `rule-claude-md` and its `children`, the Render of `rule-atomicity` and its marker line in `rule-case-protocol` (a MOC with the one child `rule-atomicity`), and the Render of `rule-one-judgment-one-implementation`. None is contradicted. The Render of `rule-atomicity` has since gained a last sentence on two behaviours and two angles. The new Criterion names the parts it named before and does not sign that sentence. The file equals the Render in any case, and `render --check` holds the rest. No behaviour changes, so no code, test, Render or hook changes, and no reader keeps an old form. `rule-claude-md`, `rule-atomicity` and `rule-one-judgment-one-implementation` have no other Estimates. The Case creates no page, so no vault query was run. Not done: the other two groups (10 pages).

> **problem:**
> The three Estimates of the text every context loads still open with a `Given:` that repeats the render and keeps history, and one of them states an old form of the refusal of `pre-spec`. So their promises carry lines that go stale beside the text they guard.

> **recommend:**
> Replace each Criterion whole with only `When:` and `Then:`. Move the lasting lines of `Given:` into `Then:`, and drop the history and the stale form of the `pre-spec` refusal. Writing the current `pre-spec` form into 492.1 was rejected, because that refusal is a promise of `rule-prespec` and a copy here would sign it twice.

### Case 492.1 — The atomicity rule in the Case schema

> **given:**
> `estimate-atomicity-rendered` — the promise, its Criterion replaced whole
> **＋** `rule-atomicity` — the rule it promises for; its Render is the text
> **＋** `rule-case-protocol` — the MOC that renders the file, with the marker line of its child
> **＋** `vault/wiki/case-schema.md` — the file the text lands in
> **＋** `guppi/render.py` — writes the file and `render --check`
> **＋** `rule-governed-files-hook` — the hook that refuses a hand edit
> **＋** `.claude/skills/hi/SKILL.md` — the skill `/hi`, which loads the file
> **＋** `rule-prespec` — the rule that holds the one mechanical refusal

> **when:**
> `guppi render` writes the governed files, and `/hi` loads `vault/wiki/case-schema.md` at the start of a working session.

> **then:**
> `vault/wiki/case-schema.md` holds the text of `rule-atomicity` between its markers: the statement, the pair test — list the conditions of "done", and for each pair ask whether one could fail while the other passes and needs a different fix — and the scope: Case, Entity, Rule, Estimate; not a Lesson, a recorded fact does not split; not an Insight, which is born by clustering, the same rule in reverse; depth is not fixed in advance.
> **＋** `render --check` after the render exits 0, and the hook of `rule-governed-files-hook` refuses a hand edit of the file.
> **＋** `rule-case-protocol` is a MOC with the child `rule-atomicity` and a marker line for it in its Render.
> **－** The rule has no refusal of its own in substance: the refusal of two promises in one Case stays with `rule-prespec`.

> **tasks:**
> - [ ] update `estimate-atomicity-rendered`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — When and Then only, Given out, the old form of the pre-spec refusal out (case 492.1)`
> - [ ] read `estimate-atomicity-rendered` — `uv run guppi render --check`, then by hand on the text between the markers after a later librarian's render

> **ratification:**
> ```
> - decision[case 492.1][update][estimate-atomicity-rendered]{ref:estimate-atomicity-rendered}
> ```

### Case 492.2 — `CLAUDE.md` is the Render of its page

> **given:**
> `estimate-claude-md-rendered` — the promise, its Criterion replaced whole
> **＋** `rule-claude-md` — the MOC it promises for; its Render is the whole file
> **＋** `rule-language` — a child spliced into its markers
> **＋** `rule-agent-writing` — a child spliced into its markers
> **＋** `rule-one-judgment-one-implementation` — a child spliced into its markers
> **＋** `CLAUDE.md` — the file written and loaded
> **＋** `guppi/render.py` — writes the file and `render --check`
> **＋** `rule-governed-files-hook` — the hook that refuses a hand edit

> **when:**
> `guppi render` writes `CLAUDE.md` from `rule-claude-md` and its children, and a session or a subagent starts and loads the file.

> **then:**
> `CLAUDE.md` is: `# GUPPI`; one paragraph, "A Claude Code harness governed by ratified decisions, and the Obsidian vault it compiles into. The vault is vault/; its terms are vault/wiki/glossary.md. A working session opens with /hi.", whose words the file holds with the folder, the path and the skill in code spans; then the text of `rule-language`, `rule-agent-writing` and `rule-one-judgment-one-implementation` in their markers.
> **＋** `render --check` after the render exits 0, and the hook of `rule-governed-files-hook` refuses a hand edit of the file.
> **＋** Every session and every subagent loads this text.
> **－** No `@` import, no "What is loaded here", no paragraph on `index.md`, no "Migration mode", no "Commands", no one rule and no sentence on memory — the one rule is in the schema; the `children` of `rule-claude-md` are `rule-language`, `rule-agent-writing` and `rule-one-judgment-one-implementation`.

> **tasks:**
> - [ ] update `estimate-claude-md-rendered`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — When and Then only, Given and the history of Migration mode out (case 492.2)`
> - [ ] read `estimate-claude-md-rendered` — `uv run guppi render --check`, then by hand on `CLAUDE.md` at the start of a later session

> **ratification:**
> ```
> - decision[case 492.2][update][estimate-claude-md-rendered]{ref:estimate-claude-md-rendered}
> ```

### Case 492.3 — One judgment, one implementation

> **given:**
> `estimate-one-judgment-one-implementation-followed` — the promise, its Criterion replaced whole
> **＋** `rule-one-judgment-one-implementation` — the rule it promises for; its Render is the text
> **＋** `rule-claude-md` — the MOC that renders the file, with the marker line of its child
> **＋** `CLAUDE.md` — the file the text lands in, loaded in every context
> **＋** `guppi/render.py` — writes the file and `render --check`
> **＋** `rule-governed-files-hook` — the hook that refuses a hand edit
> **＋** `guppi/` — the code of the pipeline whose diff the reading reads

> **when:**
> The agent writes code in `guppi/` that judges a text another part of the pipeline already judges, such as a check beside a writer, a ticker or another check.

> **then:**
> The pattern or the predicate lives in one module, and both sides import it.
> **＋** Where the two sides cannot share the code, one test runs both over the same input and asserts they answer alike.
> **＋** `CLAUDE.md`, which every session and every subagent loads, holds this text between the markers of `rule-one-judgment-one-implementation`; `render --check` keeps it equal to the page, and the hook of `rule-governed-files-hook` refuses a hand edit.
> **－** No script refuses a second copy: the guard is the text in the file every context reads, and the reading of the session's diff.

> **tasks:**
> - [ ] update `estimate-one-judgment-one-implementation-followed`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — When and Then only, Given and the functions lifted by case 351 out (case 492.3)`
> - [ ] read `estimate-one-judgment-one-implementation-followed` — `uv run guppi render --check`, then by hand on the diff of the Work Mode of a later session

> **ratification:**
> ```
> - decision[case 492.3][update][estimate-one-judgment-one-implementation-followed]{ref:estimate-one-judgment-one-implementation-followed}
> ```

### Case 492.4 — The sprint page records the group of the text every context loads

> **given:**
> `entity-sprint-migration` — the sprint page; its Slice 3g holds the note on every other Estimate
> **＋** `vault/wiki/sprint.md` — the render of the sprint page
> **＋** `/hi` — builds the Frontier from `vault/wiki/sprint.md`
> **＋** `rule-claude-md` — a rule whose Estimate this Case recuts
> **＋** `rule-atomicity` — a rule whose Estimate this Case recuts
> **＋** `rule-one-judgment-one-implementation` — a rule whose Estimate this Case recuts

> **when:**
> The librarian's run applies the `update` of `entity-sprint-migration`.

> **then:**
> The History of `entity-sprint-migration` says that the Estimates of `rule-claude-md`, `rule-atomicity` and `rule-one-judgment-one-implementation` are recut.

> **tasks:**
> - [ ] update `entity-sprint-migration`
>   - change: `Slice 3g: the Estimates of rule-claude-md, rule-atomicity and rule-one-judgment-one-implementation recut to When and Then; the note on every other Estimate stands (case 492)`

> **ratification:**
> ```
> - decision[case 492.4][update][entity-sprint-migration]{ref:entity-sprint-migration}
> ```
