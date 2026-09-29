## Case 498 — Slice 3g: the Estimates of rendering and settings recut to one Criterion

> **context:**
> Each Estimate page holds one promise, its Criterion. A Criterion should hold only `When:`, the trigger and the input it acts on, and `Then:`, what must hold after. The page carries its promise as a `purpose` field and its way of checking as a `method` field. Twelve older Estimates still have the layout from before this model. They have no `purpose` and no `method` field. They have a `## Context` and a `## Method` section. Most of them also stack one `### case N` block under the Criterion for each Case that changed them. `make lint` counts these twelve as `unmigrated`. Here is where it goes wrong: `estimate-render-harness-reproduces` holds a unit-and-live paragraph and four blocks. One of those blocks, 139.1, is a probe that ran once in session O, to see whether an agent file written mid-session can be called. A new reading cannot tell which lines are the promise and which record an act that happened once.
> The person decided in the first round on this item. The twelve go in three Cases by area, all in this session: this Case takes rendering and settings, case 499 takes the end of a session, and case 500 takes the librarian's and the vault's tools. Each page gets one Criterion, and no page is split. The live half of each reading stays. The last Case replaces the Slice note with a note on removing the old-layout checks, so Slice 3g stays open until a later session removes them after lint counts zero (case 202). A Criterion that records a one-time act gets a Criterion of the repeating behaviour (case 485). This group holds five pages: `estimate-render-harness-reproduces`, `estimate-render-sync-reports`, `estimate-settings`, `estimate-default-mode` and `estimate-governed-files-hook-refuses`. None of them has `purpose` or `method`, so each `update` sets both from the page's own Criterion and `## Method`. Setting `method` also drops `## Context` and `## Method` (case 211). Each Criterion is replaced whole and goes back to `pending`, and its reading waits for a later session (case 428.1). Their rules `rule-settings`, `rule-default-mode` and `rule-governed-files-hook` go from `built` to `draft` until the reading. `rule-render-harness` is `draft` already. None of the five lost its Criterion to a tool fault like case 211.3. Their History shows only Criteria that cases 18.1, 36.2, 59.7, 66, 71.1, 85.1, 85.2, 85.4, 88.1, 89.3, 89.4, 91 and 139.1 wrote on purpose, so nothing is restored.
> What each new Criterion keeps and drops. The check of the answer notes every old line as not carried, because each new line is a whole statement and not the old wording. The content of the old lines is carried, except for the lines named here. "Unit, against a temp vault" and "Live:" name ways of reading, and they move into `method`. In 498.1, block 139.1 goes out as a one-time probe. Two more lines go out: the `－` line of 88.1 on how to read the clause, and the second half of the `－` line of 85.1, which follows from the first. The unit paragraph, 85.1, 88.1 and 89.4 become one list. The clause of 89.4 that `--sync` exits 0 on a JSON error also goes out of 498.1, because its `when` covers only the plain run and `--check`, and 498.2 promises the exit 0 of the sync on any render error. In 498.3 the line "Its Estimate reads the rendered file" becomes the lines it names. The page fields of `rule-settings` shrink to what the render does with them, and "that order is the order of the keys in the file" is kept. In 498.4, "the page" is named as `rule-default-mode` and its Purpose. In 498.5 the unit paragraph and block 91 join. The live probe on the file of `/hi` moves into `method`.
> The check of the answer also notes that the error line of 498.2 shares words with the line of 498.1 on a child without `enforcement: render`. This is expected. 498.1 promises that the plain render exits 1 and writes nothing on that fault. 498.2 promises that the sync at session start swallows any render error with exit 0, because a `SessionStart` hook cannot block. They are two promises, read by two different runs.
> The frame. Each kept line was read against `guppi/render.py`, `guppi/guard.py`, `tests/test_render.py`, `tests/test_guard.py`, the `Makefile` and the live `.claude/settings.json`, and none is contradicted. One sentence of the docstring of `guppi/render.py` calls "When Claude Code reads an agent file" "the reading of case 139.1 on `estimate-render-harness-reproduces`". After the recut the page no longer holds that reading, and the next reading overwrites its Result. So 498.1 has one task that writes the finding into the docstring in place of the pointer. That task changes no behaviour and no test. `estimate-render-harness-ticks-the-spec` promises the tick, not the render, and is left alone. `rule-settings` is a MOC, so its `method` names `make test-harness`. The render also fills the language placeholders, but no Estimate of this group promises that, and this Case adds no promise. The History line of 498.6 does not say the Slice note stands, because case 500.6 replaces that note in the same librarian's run. No behaviour changes, so no Render and no hook changes, and no reader keeps an old form. The Case creates no page, so no vault query was run. Not done: cases 499 and 500, the note of Slice 3g, and the removal of the old-layout checks.

> **problem:**
> The five Estimates of rendering and settings still have the layout from before case 193. They have no `purpose` or `method` field, they carry `## Context` and `## Method`, and four of them stack `### case N` blocks, one of them a probe that ran once. Lint counts them as `unmigrated`, and a reading of them cannot tell the promise from the record of past acts.

> **recommend:**
> Replace each Criterion whole with one `When:` and `Then:` of the repeating behaviour. Set `purpose` and `method` from the page's own text. Drop the one-time probe and write its finding into the docstring of `guppi/render.py`. Splitting the JSON check of 89.4 into its own Estimate was rejected: one pytest file already checks it with the rest.

### Case 498.1 — The renderer writes each governed file from its Rule pages

> **given:**
> `estimate-render-harness-reproduces` — the promise, its Criterion replaced whole
> **＋** `rule-render-harness` — the rule it promises for
> **＋** `guppi/render.py` — `run`, `render_full`, `render_partial`, `check_json` and `differing`; its docstring points at the probe
> **＋** `vault/wiki/rules/` — the Rule pages with `enforcement: render`
> **＋** `tests/test_render.py` — the tests the reading runs

> **when:**
> `uv run guppi render` runs without a flag or with `--check`, and reads the Rule pages under `vault/wiki/rules/` that carry `enforcement: render`.

> **then:**
> The Render of a `full` page becomes the whole file its `governs` names, without the page's outer markers. Each `<!-- child -->` line is replaced by that child's text in the order of `children`, and the child's markers are kept.
> **＋** A file that cannot hold a comment, a `.json` target, takes each child's text without the child's markers.
> **＋** A `partial` page whose file no `full` page owns is spliced between its markers in the existing file, and the markers stay. A target without those markers gives exit 1, and nothing is written.
> **＋** A child without `enforcement: render` contributes nothing and needs no marker. A marker line for it in the parent's text gives exit 1, and nothing is written.
> **＋** Every `.json` target is parsed before anything is written. One that does not parse stops the whole write, stderr names the file and the page that owns it, and the run exits 1.
> **＋** `--check` names each file that differs, exits 1 and writes nothing. When every file is identical, it exits 0.
> **＋** Against the live vault, after `uv run guppi render`, `git diff --stat` names only the governed files whose Rule page changed since the last render. The diff of each is the text of that page's Render, and `uv run guppi render --check` then exits 0.
> **－** No file type other than `.json` is parsed.

> **tasks:**
> - [ ] update `estimate-render-harness-reproduces`
>   - set: `{status: pending, purpose: "guppi render writes each governed harness file from its Rule pages, parses every json target before it writes, and --check names a file that differs", method: "pytest tests/test_render.py, plus by hand on the live vault after a later librarian's render: git diff --stat, then guppi render --check"}`
>   - change: `the Criterion replaced whole — the unit paragraph and the blocks 85.1, 88.1 and 89.4 into one When and Then, the one-time probe of 139.1 out; purpose and method set, Context and Method out (case 498.1)`
> - [ ] `guppi/render.py` — the docstring sentence that points at "the reading of case 139.1 on `estimate-render-harness-reproduces`" states the finding instead: Claude Code reads the agent files at session start, so an agent the librarian renders can be called from the next session (case 139.1)
> - [ ] read `estimate-render-harness-reproduces` — `pytest tests/test_render.py`, then by hand on the live vault after a later librarian's render

> **ratification:**
> ```
> - decision[case 498.1][update][estimate-render-harness-reproduces]{ref:estimate-render-harness-reproduces}
> ```

### Case 498.2 — The sync at session start shows and writes back a parted file

> **given:**
> `estimate-render-sync-reports` — the promise, its Criterion replaced whole
> **＋** `rule-render-harness` — the rule it promises for
> **＋** `guppi/render.py` — `sync` and `run` with `--sync`
> **＋** `.claude/settings.json` — the `SessionStart` hook that runs the sync
> **＋** `tests/test_render.py` — the tests the reading runs

> **when:**
> A session starts, and the `SessionStart` hook of `.claude/settings.json` runs `uv run guppi render --sync` over the governed files.

> **then:**
> For each governed file that differs from its render, stdout holds a unified diff, the file as it is and then the rendered text, and the rendered text is written. The diff reaches the agent's first turn.
> **＋** An identical file is neither printed nor written.
> **＋** On a render error, one line goes to stderr, nothing is written, and the exit is 0.
> **＋** At a session start after a librarian's run that rendered, the hook prints nothing and writes nothing, and `uv run guppi render --check` then exits 0.
> **＋** At a session start after a governed file and its page have parted, the diff of that file is in the first turn, and the page's text is written back.

> **tasks:**
> - [ ] update `estimate-render-sync-reports`
>   - set: `{status: pending, purpose: "At session start guppi render --sync shows the diff of each governed file that parted from its page and writes the page's text back, and is silent when every file matches", method: "pytest tests/test_render.py, plus by hand at the first turn of a later session"}`
>   - change: `the Criterion replaced whole — the unit and live paragraph as When and Then; purpose and method set, Context and Method out (case 498.2)`
> - [ ] read `estimate-render-sync-reports` — `pytest tests/test_render.py`, then by hand at the first turn of a later session

> **ratification:**
> ```
> - decision[case 498.2][update][estimate-render-sync-reports]{ref:estimate-render-sync-reports}
> ```

### Case 498.3 — The settings file rendered whole from its MOC

> **given:**
> `estimate-settings` — the promise, its Criterion replaced whole
> **＋** `rule-settings` — the MOC it promises for, the `full` owner of the file
> **＋** `rule-default-mode` — its first child
> **＋** `rule-permissions` — its second child
> **＋** `rule-hook-registry` — its third child
> **＋** `.claude/settings.json` — the file rendered
> **＋** `vault/raw/<date>/event_log.md` — the day's event log with the `session-start` line
> **＋** `Makefile` — the target `test-harness`

> **when:**
> `uv run guppi render` writes `.claude/settings.json` from `rule-settings` and its children, and the next session starts from that file.

> **then:**
> The file is the Render of `rule-settings`, and the text of each child replaces its `<!-- child -->` line in the order of `children`: `rule-default-mode`, `rule-permissions`, `rule-hook-registry`. That order is the order of the keys in the file.
> **＋** The file parses as JSON, and `uv run guppi render --check` exits 0.
> **＋** The next session start writes its `session-start` line into `vault/raw/<date>/event_log.md`, from the hooks of the rendered file.
> **－** `rule-settings` holds no rule of its own about what a hook or a permission may be.

> **tasks:**
> - [ ] update `estimate-settings`
>   - set: `{status: pending, purpose: "The settings file is rendered whole from rule-settings and its three children, parses as JSON and loads at session start", method: "make test-harness, then by hand at a later session start: json.load on the rendered file, guppi render --check, and the session-start line in the day's event log"}`
>   - change: `the Criterion replaced whole — the block 85.2 as When and Then, the line on its own reading into the lines it names; purpose and method set, Context and Method out (case 498.3)`
> - [ ] read `estimate-settings` — `make test-harness`, then by hand at a later session start

> **ratification:**
> ```
> - decision[case 498.3][update][estimate-settings]{ref:estimate-settings}
> ```

### Case 498.4 — A session opens in Plan Mode

> **given:**
> `estimate-default-mode` — the promise, its Criterion replaced whole
> **＋** `rule-default-mode` — the rule it promises for, a child of `rule-settings`
> **＋** `rule-settings` — the MOC that renders the file
> **＋** `.claude/settings.json` — the file that carries the mode
> **＋** `tests/test_render.py` — the tests the reading runs

> **when:**
> A session starts with `.claude/settings.json` as `guppi render` wrote it from `rule-settings`.

> **then:**
> `.claude/settings.json` carries `"defaultMode": "plan"` under `permissions`, the text of `rule-default-mode`, and the session opens in Plan Mode.
> **＋** The Purpose of `rule-default-mode` says why: nothing is written before a Case is ratified.
> **－** The Render of `rule-default-mode` holds no other permission field.

> **tasks:**
> - [ ] update `estimate-default-mode`
>   - set: `{status: pending, purpose: "A session opens in Plan Mode: the settings file carries defaultMode plan from rule-default-mode", method: "pytest tests/test_render.py, plus by hand at a later session start: the session opens in Plan Mode and nothing outside the plan file is edited without a sign-off"}`
>   - change: `the Criterion replaced whole — the block 85.4 as When and Then, the page named; purpose and method set, Context and Method out (case 498.4)`
> - [ ] read `estimate-default-mode` — `pytest tests/test_render.py`, then by hand at a later session start

> **ratification:**
> ```
> - decision[case 498.4][update][estimate-default-mode]{ref:estimate-default-mode}
> ```

### Case 498.5 — The guard refuses a hand edit of a governed file

> **given:**
> `estimate-governed-files-hook-refuses` — the promise, its Criterion replaced whole
> **＋** `rule-governed-files-hook` — the rule it promises for
> **＋** `guppi/guard.py` — the hook `guppi guard`
> **＋** `.claude/settings.json` — the `PreToolUse` matcher of `Edit`, `Write` and `MultiEdit`
> **＋** `vault/wiki/rules/` — the live Rule pages whose `governs` the hook reads
> **＋** `vault/raw/<date>/event_log.md` — the day's event log
> **＋** `tests/test_guard.py` — the tests the reading runs

> **when:**
> Claude Code runs `uv run guppi guard` on `PreToolUse` of a tool call, and the hook reads the `governs` field of the live Rule pages under `vault/wiki/rules/`.

> **then:**
> An `Edit`, `Write` or `MultiEdit` on a governed path exits 2. Stderr names the file and the slug of the rule that governs it, and the client blocks the call.
> **＋** Before it exits 2, the hook appends one line to `vault/raw/<date>/event_log.md` with the time, the session, the tool, the path and the slug of the rule.
> **＋** Another tool or an ungoverned path exits 0.
> **＋** A payload the hook cannot read exits 0 with one line on stderr.
> **－** A call the hook lets through writes no event line: `PostToolUse` logs it.
> **－** A log the hook cannot write does not change the refusal: the exit stays 2, and the reason still goes to stderr.

> **tasks:**
> - [ ] update `estimate-governed-files-hook-refuses`
>   - set: `{status: pending, purpose: "guppi guard refuses a hand edit of a governed harness file, names its rule and logs the refusal", method: "pytest tests/test_guard.py, plus by hand in a later session: one Edit of a governed file refused, the rule named, the line in the day's event log"}`
>   - change: `the Criterion replaced whole — the unit paragraph and the block 91 into one When and Then, the live probe into method; purpose and method set, Context and Method out (case 498.5)`
> - [ ] read `estimate-governed-files-hook-refuses` — `pytest tests/test_guard.py`, then by hand on one refused `Edit` in a later session

> **ratification:**
> ```
> - decision[case 498.5][update][estimate-governed-files-hook-refuses]{ref:estimate-governed-files-hook-refuses}
> ```

### Case 498.6 — The sprint page records the group of rendering and settings

> **given:**
> `entity-sprint-migration` — the sprint page whose History records the recut
> **＋** `rule-render-harness` — a rule whose Estimates this Case recuts
> **＋** `rule-settings` — a rule whose Estimate this Case recuts
> **＋** `rule-default-mode` — a rule whose Estimate this Case recuts
> **＋** `rule-governed-files-hook` — a rule whose Estimate this Case recuts

> **when:**
> The librarian's run applies the `update` of `entity-sprint-migration`.

> **then:**
> The History of `entity-sprint-migration` says that the Estimates of rendering and settings are recut.

> **tasks:**
> - [ ] update `entity-sprint-migration`
>   - change: `Slice 3g: the Estimates of rule-render-harness, rule-settings, rule-default-mode and rule-governed-files-hook recut to one Criterion (case 498)`

> **ratification:**
> ```
> - decision[case 498.6][update][entity-sprint-migration]{ref:entity-sprint-migration}
> ```
