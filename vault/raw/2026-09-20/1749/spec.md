<!-- approved 20:24:13 · session 92c68243 -->

# Spec — 2026-09-20, session 1749

## Case 278 — `estimate-case-protocol-loaded` without the line on the agent stating two rules

> **context:**
> `estimate-case-protocol-loaded` is an Estimate of `rule-case-protocol`: the Case schema is present in a session from the first turn. While the schema lived inside `CLAUDE.md`, the only way to check that was the agent's behaviour: in the reply to `/hi` the agent named the `LEDGER`-block rule and the one-Case-at-a-time rule by itself. Since case 273 the schema is the Render of `rule-case-protocol` in `case-schema.md`, and `/hi` brings its text into the context; the presence of the text is checked by `estimate-internal-context-loaded` (`passed` today). The Criterion line on the statement stayed, no instruction asks for that act, and today's reading gave `failed` on that line alone.
> The page stands `pending` since 273.1, `failed` today; in the old shape — `method` and `checked`, no `purpose`; lint counts it among the unmigrated. One Estimate of `rule-case-protocol` is touched; the other three (`case-form`, `acknowledging-reply`, `ledger-line-form`) are not.

> **problem:**
> The Criterion asks for a behaviour no instruction sets, and checks a second time what `estimate-internal-context-loaded` already checks. Either the instruction catches up with the Criterion, or the Criterion loses the line.

> **given:**
> A `full` page writes the whole file named by `governs`, without its outer markers; a child of a `full` page governs the same file as its parent, otherwise `render` errors (case 277).
> **＋** The `children` of a Rule MOC is an ordered list, set explicitly.
> **＋** `tests/test_render.py` fixes a `full` render into a file outside `.claude/`.
> **＋** The presence of the schema's text in the first turn is checked by `estimate-internal-context-loaded`, not by this Estimate.

> **when:**
> The first `uv run guppi render` after `rule-case-protocol` changed, and the `/hi` of the next session.

> **then:**
> `vault/wiki/case-schema.md` equals the Render of `rule-case-protocol`; `render --check` exits 0; the file is no longer edited by hand — the hook refuses.
> **＋** The schema holds one text: what stood in it, plus from the old Render — the Frontier `frontier.md` and the closing of its lines, Plan Mode not ending while a line is open; the acknowledging reply of four parts; the harness rendered from `rules/`, never by hand; `ask-guppi` before a `create` without a `ref`, the answer in `context`; the ledger mechanics — the `LEDGER` block, the `Stop` hook, `{tags}`, `{source}`, when each line is written, the refusal without `/hi`, a reply with the block ending in it, a block a tool call followed not lost before `Stop`.
> **＋** The tick sentence in the wording of 270.2; the Language section of the schema on the manner of the English of the vault, the language of the repository and the chat being `rule-language`.
> **－** Nothing of the schema is repeated in `CLAUDE.md`; `rule-case-protocol` is a child of `rule-plan-mode`, the last of its list.
> **－** The agent's reply to `/hi` does not have to restate the rules of the schema.

```then
update:
  - slug: estimate-case-protocol-loaded
    set: {status: pending, purpose: "The Case schema is present in a session from the first turn after /hi, as one text — the Render of rule-case-protocol — and nothing of it repeated in CLAUDE.md"}
    change: the Criterion replaced whole — the line on the agent stating two rules at /hi removed, the presence of the text checked by estimate-internal-context-loaded; purpose added (case 278)
```

```tasks
- [ ] update `estimate-case-protocol-loaded`: `set: {status: pending, purpose: ...}`, the Criterion replaced whole by the `given`, `when` and `then` of this Case
- [ ] read `estimate-case-protocol-loaded`: the `/hi` of the next session, by hand; `tests/test_ledger.py`
```

## Case 279 — the form of the `render` and `sprint` lines of the Spec, named where the agent writes it and refused by pre-spec

> **context:**
> The scripts tick three kinds of lines in the Spec: `generate` the page lines and the `read` lines, `render` and `sprint` the lines of their own commands. The schema names the form of the first two (`<kind> `<slug>``, `read `<slug>``) and not the form of the command lines; that form stands in `rule-render-harness` (case 235), a page the agent does not read when it writes the Spec. In session 1308 the agent wrote `render `<file>`` on the pattern of the page lines, and nine lines stood unticked after the librarian's run, the yaml applied whole. A sentence in the schema is instruction; what keeps it from repeating is a guard — `guppi prespec --check` already reads the `tasks` block of every Case (cases 59.3, 264.2).
> Case 278 of this session already replaced the Criterion of `estimate-case-protocol-loaded` whole; an `update` of the Render of `rule-case-protocol` touches the same Estimate (187), so 279.1 supersedes 278 and carries its text plus one line. `rule-case-protocol` `draft`; `estimate-case-protocol-loaded` touched, `case-form`, `acknowledging-reply` and `ledger-line-form` not. `rule-prespec` `built`, its three Estimates untouched; the new promise is its own Estimate with a `ref`, no vault query due. `rule-render-harness` and its Estimates do not change — the ticker is right.

> **problem:**
> The form of a line the scripts tick is written where the agent does not look, and nothing refuses a line of another form. Either the schema names the form and pre-spec refuses the rest, or the ticker accepts both — two forms of one line.

### Case 279.1 — the schema names the form; supersedes 278

> **given:**
> A `full` page writes the whole file named by `governs`, without its outer markers; a child of a `full` page governs the same file as its parent, otherwise `render` errors (case 277).
> **＋** The `children` of a Rule MOC is an ordered list, set explicitly.
> **＋** `tests/test_render.py` fixes a `full` render into a file outside `.claude/`.
> **＋** The presence of the schema's text in the first turn is checked by `estimate-internal-context-loaded`, not by this Estimate.
> **＋** The tickers of `render` and `sprint` match a line that opens with a code span holding the command (case 235); `tests/test_render.py` fixes it.

> **when:**
> The first `uv run guppi render` after `rule-case-protocol` changed, and the `/hi` of the next session.

> **then:**
> `vault/wiki/case-schema.md` equals the Render of `rule-case-protocol`; `render --check` exits 0; the file is no longer edited by hand — the hook refuses.
> **＋** The schema holds one text: what stood in it, plus from the old Render — the Frontier `frontier.md` and the closing of its lines, Plan Mode not ending while a line is open; the acknowledging reply of four parts; the harness rendered from `rules/`, never by hand; `ask-guppi` before a `create` without a `ref`, the answer in `context`; the ledger mechanics — the `LEDGER` block, the `Stop` hook, `{tags}`, `{source}`, when each line is written, the refusal without `/hi`, a reply with the block ending in it, a block a tool call followed not lost before `Stop`.
> **＋** The tick sentence in the wording of 270.2; the Language section of the schema on the manner of the English of the vault, the language of the repository and the chat being `rule-language`.
> **＋** The Spec paragraph of the schema names the form of the lines the command scripts tick: `- [ ] `uv run guppi render`: `<file>`` and `- [ ] `uv run guppi sprint`` — the command in the first code span; a line of another form stays debt at Retro.
> **－** Nothing of the schema is repeated in `CLAUDE.md`; `rule-case-protocol` is a child of `rule-plan-mode`, the last of its list.
> **－** The agent's reply to `/hi` does not have to restate the rules of the schema.

```then
update:
  - slug: rule-case-protocol
    replace:
      - old: "`render` and `sprint` the render and sprint lines (cases 226, 250, 270); Retro counts the unticked (case 59.3)."
        new: "`render` and `sprint` the render and sprint lines (cases 226, 250, 270); Retro counts the unticked (case 59.3). A render line is `- [ ] `uv run guppi render`: `<file>``, a sprint line `- [ ] `uv run guppi sprint`` — the command in the first code span is what the ticker matches (case 235); a line of another form stays debt at Retro (case 279.1)."
    change: the Spec paragraph names the form of the render and sprint lines the scripts tick (case 279.1)
  - slug: estimate-case-protocol-loaded
    set: {status: pending, purpose: "The Case schema is present in a session from the first turn after /hi, as one text — the Render of rule-case-protocol — and nothing of it repeated in CLAUDE.md"}
    change: the Criterion replaced whole — the text of 278 plus the form of the render and sprint lines; the line on the agent stating two rules at /hi removed; purpose added (case 279.1, supersedes 278)
```

```tasks
- [ ] update `rule-case-protocol`: `replace` in the Render — the sentence on the form after the tick sentence
- [ ] update `estimate-case-protocol-loaded`: `set: {status: pending, purpose: ...}`, the Criterion replaced whole (the text of 278 plus one line)
- [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
- [x] by hand, a one-off: `[x]` on the nine render lines of `raw/2026-09-20/1308/spec.md` — 97, 131, 187, 258, 312, 366, 575, 626, 692
- [ ] read `estimate-case-protocol-loaded`: the `/hi` of the next session, by hand; `tests/test_ledger.py`
```

### Case 279.2 — pre-spec refuses a `render` or `sprint` line of another form

> **given:**
> `guppi prespec --check <plan>` reads the `tasks` block of every Case of the plan and prints one finding per line, exit 1 on any (cases 59.3, 264.2).
> **＋** The tickers of `render` and `sprint` match a line that opens with a code span holding the command (case 235).
> **＋** `tests/test_prespec.py` fixes the behaviour on a temp plan.

> **when:**
> `/pre-spec` — `guppi prespec --check` on the plan of this Plan Mode.

> **then:**
> A `tasks` line whose text after the box opens with the word `render` or `sprint`, or with `guppi render`, `guppi sprint`, `uv run guppi render` or `uv run guppi sprint` outside a code span, is a finding `case N: render line off form: <line>`; the form the ticker knows is `- [ ] `uv run guppi render`: …` and `- [ ] `uv run guppi sprint``.
> **－** A line that opens with a code span holding the command is no finding; a `read` line that names the command in a later span is no finding (235).
> **－** Nothing else in pre-spec changes.

```then
update:
  - slug: rule-prespec
    replace:
      - old: "nor a hub file of `wiki/` (case 264.2); an Estimate has its own line and its own item (case 189)."
        new: "nor a hub file of `wiki/` (case 264.2), and for every `tasks` line that opens with the bare word `render` or `sprint`, or with the command outside a code span — the tickers of `render` and `sprint` match the command in the first code span, and a line of another form stays debt (case 279.2); an Estimate has its own line and its own item (case 189)."
    change: pre-spec flags a render or sprint task line the tickers would not match (case 279.2)
create:
  - slug: estimate-prespec-catches-a-command-line-off-form
    type: estimate
    ref: rule-prespec
    kind: QA
    purpose: A tasks line that names render or sprint outside the first code span is a finding of prespec --check; the ticker's form passes
    method: pytest tests/test_prespec.py on a temp plan; the live reading /pre-spec of this session on its own plan
    tags: [harness, workflow]
```

```tasks
- [ ] update `rule-prespec`: the sentence in the Render on the form of the command lines
- [ ] create `estimate-prespec-catches-a-command-line-off-form`, `ref: rule-prespec`
- [x] `guppi/prespec.py`: the check in `check_tasks`, the module docstring — one item in the list of findings
- [x] `tests/test_prespec.py`: `render `X`` — a finding; `uv run guppi render` as a bare word — a finding; `- [ ] `uv run guppi render`: …` — clean; a `read` line with `guppi render` in a later span — clean
- [ ] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
- [ ] read `estimate-prespec-catches-a-command-line-off-form`: pytest; live — `/pre-spec` of this session on its own plan
```

## Case 280 — a reading does not close the `read` line of a Case ratified after it

> **context:**
> `generate`, once it applied an `estimate` entry of the yaml, ticks the first unticked line `- [ ] read `<slug>`` — in the Spec beside the yaml first, then in the Specs of the other sessions of `raw/`, oldest first (270.1). "Own Spec first" is right when the reading came after the Case that set the Estimate `pending`. It goes wrong when the reading stands earlier in the ledger: in 1308 the reading of `estimate-documentation-completes` was line 8, Case 271 of the same session later replaced the Criterion and added its own `read` line (188) — and `generate` ticked that one, not 0958:308, the line the reading was made for. The Estimate stayed `pending` by 271 and line 308 open: the count held, but the ticked line belongs to a Case whose Criterion nobody read, and the debt left the Retro of 1308 for another session's Spec. This session repeats it: the reading of `estimate-case-protocol-loaded` (`failed`, ledger line 6) precedes 279.1, and the Spec beside the yaml carries the `read` line of 279.1 — today's run would tick it instead of 1308:98.
> `rule-page-generation` `draft` (`estimate-generate-rewords` pending); `estimate-generate-ticks-the-spec` (`passed`) touched, the other seven Estimates of the rule not. A yaml entry carries `line` — the number of its ledger line — and a decision entry `case`; an `update` with a `ref`, no vault query due.

> **problem:**
> A reading recorded before a Case closes the line of that Case. `generate` needs a mark by which it tells the line of a Case ratified after the reading.

> **given:**
> A yaml entry of kind `estimate` carries `slug`, `status`, `result`, `line` and no `case`; a decision entry carries `case` and `line`, the number of its line in the ledger.
> **＋** The Spec of the unit lies beside the yaml — `raw/<date>/<HHMM>/spec.md`; the Specs of the other sessions are the `spec.md` of their folders under `raw/`.
> **＋** A Case heading in the Spec is `## Case N — …` or `### Case N.M — …`; its section runs to the next such heading.
> **＋** A reading line of the Spec is `- [ ] read `<slug>`` with text after it, in any Case.
> **＋** `tests/test_generate.py` fixes the behaviour on a temp vault with a Spec beside the yaml and a second Spec in another session folder.
> **－** A Rule-class file entry `generate` does not apply — "applied by hand".

> **when:**
> `guppi generate` applied an entry and marked it `applied`.

> **then:**
> For a `create`, `update`, `delete` or `defer` entry, in the `spec.md` of the same unit the first unticked line `- [ ] <kind> `<slug>`` in the section of the entry's Case becomes `- [x]`; nothing else in the file changes.
> **＋** Two entries of one kind and slug in one Case tick two lines, in order.
> **＋** For an `estimate` entry, and for a `create` entry with `folded`, the first unticked line `- [ ] read `<slug>`` becomes `- [x]` — in the Spec beside the yaml first, then in the `spec.md` of the other session folders of `raw/`, oldest first; one line per entry.
> **＋** In the Spec beside the yaml, a `read` line in the section of a Case whose first decision entry of the yaml carries a `line` greater than the `line` of the `estimate` entry is not the reading's line — the Case was ratified after it; the search goes on to the next line, then to the other sessions.
> **＋** A `create` entry with `folded` ticks both lines: the page line and the reading line; its Case is the reading's Case, the filter does not apply to it.
> **－** A line not found, a section not found, no Spec — no error and no stderr line; the entry is `applied` all the same.
> **－** `lesson` and Rule-class file entries, and an entry marked `failed`, tick no line; the lines on code, tests, migrations and `by hand` are the agent's.
> **－** A Spec under `vault/archive/` is not read; the Specs of the other sessions are not filtered by `line`.

```then
update:
  - slug: rule-page-generation
    replace:
      - old: "in the Spec beside the yaml first and then in the `spec.md` of the other session folders of `raw/`, oldest first — so the Spec's page lines and reading lines are closed by the one who did the work, and a line not found is no error (cases 226.1, 270.1)."
        new: "in the Spec beside the yaml first — skipping the section of a Case whose first decision entry stands after the reading in the ledger, a Case ratified after it — and then in the `spec.md` of the other session folders of `raw/`, oldest first — so the Spec's page lines and reading lines are closed by the one who did the work, and a line not found is no error (cases 226.1, 270.1, 280)."
    change: a reading does not tick the read line of a Case ratified after it in the same session (case 280)
  - slug: estimate-generate-ticks-the-spec
    set: {status: pending}
    change: the Criterion replaced whole — the read line of a later Case of the same unit is skipped by the ledger line numbers (case 280)
```

```tasks
- [ ] update `rule-page-generation`: the tick sentence of the Purpose — the section of a Case ratified after the reading is skipped
- [ ] update `estimate-generate-ticks-the-spec`: the Criterion replaced whole, `pending`
- [x] `guppi/generate.py`: `tick_read` skips, in the Spec beside the yaml, the sections of the Cases whose first decision entry carries a `line` greater than the `estimate` entry's; the docstring
- [x] `tests/test_generate.py`: a reading before the Case's decision line — its line skipped, the older Spec's line ticked; a reading after — the Case's line ticked; `folded` unfiltered
- [ ] read `estimate-generate-ticks-the-spec`: pytest; live — the librarian's run of this session: the reading of `estimate-case-protocol-loaded` ticks 1308:98, the line of 279.1 stays open, 0958:308 closed by the reading of `estimate-documentation-completes`
```

## Case 282 — the lines of a superseded Case are not debt at Retro

> **context:**
> Retro counts the unticked `tasks` lines of the Spec: the page lines, the `render`, `sprint` and `read` lines with their reading in the ledger wait for the librarian, the rest is debt (233.2, 253.2, 270.3). When a Case of the session is superseded by another (`{supersedes:case N}` in the ledger), its yaml entries are marked `superseded_by` and never applied, its lines in the Spec stay `[ ]` for good — and Retro counts them as debt: the 1308 handoff passed line 783 of the superseded 274.2 to the next session as a check. In this session the same waits for 278.
> `rule-retro` `draft`, `estimate-retro-loads` `pending` by 270.3 and read at this session's Retro — the reading covers the new line too; the other Estimates of `rule-retro` untouched; an `update` with a `ref`, no vault query due. Found by pre-spec of this session.

> **problem:**
> The lines of a Case whose work moved into the superseding Case are counted as a debt that does not exist.

> **given:**
> Retro runs before the librarian; `generate` after it ticks the page lines and the `read` lines whose reading stands in the ledger, `render` and `sprint` the render and sprint lines (cases 226, 250, 270.1).
> **＋** A ledger line `{supersedes:case N}` marks every entry of Case N `superseded_by`; `generate` neither applies nor ticks them (200.2).

> **when:**
> The person invokes `/retro`, and the agent counts the unticked `tasks` of the Spec.

> **then:**
> A `create`, `update` or `defer` line of a page, a `guppi render` line, a `guppi sprint` line and a `read` line whose `estimate[...]` stands in the ledger of this session are listed as waiting for the librarian and end in none of the four ways; every other unticked line is debt, as today.
> **＋** The lines of a Case a `{supersedes:case N}` line of this session's ledger names are not counted: its work stands under the superseding Case.
> **－** A `read` line without its line in the ledger is debt: the reading was not done.
> **－** Nothing else in Retro changes.

```then
update:
  - slug: rule-retro
    replace:
      - old: "not as debt — a `read` line without its line in the Tail is debt;"
        new: "not as debt — a `read` line without its line in the Tail is debt, and the lines of a Case a `{supersedes:case N}` line of the Tail names are not counted at all, its work stands under the superseding Case (case 282);"
    change: the lines of a superseded Case are not debt at Retro (case 282)
  - slug: estimate-retro-loads
    set: {status: pending}
    change: the Criterion replaced whole — the lines of a superseded Case are not counted (case 282)
```

```tasks
- [ ] update `rule-retro`: `replace` in the Render — the sentence on a superseded Case
- [ ] update `estimate-retro-loads`: the Criterion replaced whole, `pending`
- [ ] `uv run guppi render`: `.claude/skills/retro/SKILL.md`
- [ ] read `estimate-retro-loads`: the first `/retro` after the render, by hand — this session, the lines of 278 out of the count
```

## Deferred

## Case 281 — Slice 3b: `rule-work-mode`, `rule-subagent-guppi`

> **context:**
> Slice 3b is the current milestone of the sprint: `rule-work-mode` — Work Mode, the Spec as tasks with code, the ticked boxes, the test of each Estimate first, the sentence of `insight-workflow-code-live-before-the-page-it-reads`; `rule-subagent-guppi` — what a subagent may do and the fork that comes back as a Case. Both are `draft` placeholders, deferred twelve times, the last by 276. This session took the readings due of 1308, the recut of `estimate-case-protocol-loaded` (278, 279.1), the form of the render and sprint lines with its pre-spec guard (279), and the read line of a Case ratified after the reading (280) ahead of it.

> **problem:**
> The person closes this Plan Mode with three Cases and goes to pre-spec; Slice 3b waits for the next session, the thirteenth defer. One line of 279.1 bears on it: the form of the render and sprint lines of the Spec is named in the schema — the rule is written with that.

```then
defer:
  - slug: rule-work-mode
    type: rule
    purpose: Work Mode as a rule — the Spec as tasks with code, the ticked boxes on code, tests, migrations and by-hand checks in spec.md (the readings are generate's since case 270, the render and sprint lines in the form of case 279.1), the test of each Estimate written first and turned green, the sentence of insight-workflow-code-live-before-the-page-it-reads on a check that reads a page the same Spec changes; the first item of the next session
  - slug: rule-subagent-guppi
    type: rule
    purpose: what a subagent may do in Work Mode, and the fork that comes back to the main agent as a Case; with rule-work-mode, the first item of the next session
```
