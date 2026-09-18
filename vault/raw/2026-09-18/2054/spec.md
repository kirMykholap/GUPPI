<!-- approved 22:50:13 · session 48a1357c -->

# Spec — 2026-09-18, session 2054

## Case 250 — `rule-sprint`: the `guppi sprint` lines of the Spec are ticked

> **context:**
> `rule-sprint` is the rule by which `guppi sprint` writes `vault/wiki/sprint.md` from the sprint page; the librarian runs it after `cleanup` and `render`. `rule-render-harness` since case 226.2 ticks the Spec lines that open with a code span holding `guppi render`, in every unit under `raw/` whose yaml is applied whole; `generate` ticks the page lines (226.1). The lines `- [ ] `uv run guppi sprint` at the librarian's run` — three in the Spec of session 1957 — are ticked by nobody: `guppi sprint` knows nothing of the Spec. A second finding: `render` counts a yaml applied whole when every entry carries `applied`; the entry of case 247 in the 1957 yaml carries `superseded_by` and no `applied`, so `render` would never touch that unit, while `guppi archive` (`rule-raw-archive`) counts such an entry closed. The Case touches `estimate-render-harness-ticks-the-spec` and no other Estimate of `rule-render-harness`; on `rule-sprint` it touches neither `estimate-sprint-renders-the-backlog` nor `estimate-sprint-checks-the-file` and creates a third; the slug `estimate-sprint-ticks-the-spec` is free in `wiki/` and in the archive.

> **problem:**
> A `guppi sprint` line of the Spec is work a script does, not the agent, and nobody ticks it: Retro counts it as debt in every session that changed the sprint page. Even with a ticking `sprint`, the unit of 1957 would stay untouched: a yaml with a superseded entry does not count as applied whole.

### Case 250.1 — applied whole counts a superseded entry

> **given:**
> `guppi render` without a flag writes every governed file and exits 0.
> **＋** `guppi archive` counts a unit done when every entry of `entries` carries `applied` or `superseded_by` (`rule-raw-archive`).
> **＋** `tests/test_render.py` fixes the behaviour on a temp vault.

> **when:**
> `guppi render` without a flag wrote the files and exits 0, and the yaml of a unit holds an entry with `superseded_by` and no `applied`.

> **then:**
> The yaml counts as applied whole: every entry carries `applied` or `superseded_by`, and none `failed`; the `guppi render` lines of the unit's `spec.md` are ticked.
> **－** An entry with neither mark, or with `failed` — the unit is not touched.

```then
update:
  - slug: estimate-render-harness-ticks-the-spec
    set: {status: pending}
    sections:
      Criterion: |
        Given:
        `guppi render` without a flag writes every governed file and exits 0, or writes nothing and exits 1.
        **＋** The units under `raw/` with a yaml are `units_with`; a yaml is applied whole when every entry carries `applied` or `superseded_by` and none `failed`, as `guppi archive` counts it (case 250.1).
        **＋** `tests/test_render.py` fixes the behaviour on a temp vault.

        When:
        `guppi render` without a flag wrote the files and exits 0.

        Then:
        In the `spec.md` of every unit under `raw/` whose yaml is applied whole, every unticked task line whose text opens with a code span holding `guppi render` becomes `- [x]`; nothing else changes.
        **－** A line where `guppi render` sits in a later code span — a `read `<slug>`` line, a line that names the command in its description — is not ticked.
        **－** `--check` and `--sync` tick nothing; exit 1 ticks nothing.
        **－** A unit without a yaml, with an entry that carries neither `applied` nor `superseded_by`, with a `failed` entry, or marked by `carry.md`, is not touched.
    change: the Criterion replaced whole — a yaml is applied whole when every entry carries applied or superseded_by and none failed, as guppi archive counts it (case 250.1)
```

```tasks
- [ ] update `estimate-render-harness-ticks-the-spec`: the Criterion replaced whole, `pending`
- [x] `guppi/render.py`: `applied_whole` counts `superseded_by`
- [x] `tests/test_render.py`: a yaml with a superseded entry is ticked; one with an unmarked entry is not
- [ ] read `estimate-render-harness-ticks-the-spec`
```

### Case 250.2 — `guppi sprint` ticks its lines

> **given:**
> `guppi sprint` without a flag writes `vault/wiki/sprint.md` and exits 0, or writes nothing and exits 1.
> **＋** The units under `raw/` with a yaml are `units_with`; a yaml is applied whole when every entry carries `applied` or `superseded_by` and none `failed` (case 250.1); `carry.md` marks a carried-over unit.
> **＋** `tests/test_sprint.py` fixes the behaviour on a temp vault.

> **when:**
> `guppi sprint` without a flag wrote the file and exits 0.

> **then:**
> In the `spec.md` of every unit under `raw/` whose yaml is applied whole, every unticked task line that opens with a code span holding `guppi sprint` becomes `- [x]`; nothing else changes.
> **－** A line where `guppi sprint` sits in a later code span — a `read` line, a description — is not ticked.
> **－** `--check` ticks nothing; exit 1 ticks nothing.
> **－** A unit without a yaml, with an unapplied or `failed` entry, or marked by `carry.md`, is not touched.

```then
update:
  - slug: rule-sprint
    replace:
      - old: "`make lint` runs it after `render --check` (case 227)."
        new: "`make lint` runs it after `render --check` (case 227). Once the plain `guppi sprint` wrote the file and exits 0, it ticks every unticked task line that opens with a code span holding `guppi sprint` — never a `read` line that names the command later — in the `spec.md` of every unit under `raw/` whose yaml is applied whole; `--check` and an exit 1 tick nothing (case 250.2)."
    change: sprint, once it wrote sprint.md and exits 0, ticks the guppi sprint lines of every applied Spec under raw/ (case 250.2)
create:
  - slug: estimate-sprint-ticks-the-spec
    type: estimate
    ref: rule-sprint
    kind: QA
    purpose: sprint, once it wrote sprint.md and exits 0, ticks the guppi sprint lines of every Spec under raw/ whose yaml is applied whole
    method: pytest tests/test_sprint.py, plus one reading of this session's spec.md and the 1957 Spec after the librarian's run
    tags: [harness, sprint]
```

```tasks
- [ ] update `rule-sprint`: one sentence on the tick in Purpose
- [ ] create `estimate-sprint-ticks-the-spec`
- [x] `guppi/render.py`, `guppi/sprint.py`: one shared helper that ticks the lines of a command in every applied Spec; `sprint` calls it after the write
- [x] `tests/test_sprint.py`: the tick, `--check`, a later code span, an unapplied unit, a carried-over unit
- [ ] `uv run guppi sprint` at the librarian's run
- [ ] read `estimate-sprint-ticks-the-spec`
```

## Case 253 — a third ticker: the Case protocol and Retro know `sprint`

> **context:**
> Since case 226 three texts name who ticks the lines of a Spec: the Render of `rule-case-protocol` (in `CLAUDE.md`), `case-schema.md` and §1 of `index.md` — "`generate` and `render` tick the page and render lines"; the Criterion of `estimate-case-protocol-loaded` repeats it in one line. `rule-retro` (case 233.2) lists at `/retro` the `create`, `update` and `defer` lines and a `guppi render` line as waiting for the librarian, not debt; `estimate-retro-loads` holds that in its Criterion. With case 250.2 the tickers are three: a `guppi sprint` line waits for the librarian too. The Case touches `estimate-case-protocol-loaded` and `estimate-retro-loads` — one line of the Criterion in each — and no other Estimate of `rule-case-protocol`. Found by pre-task (`ask-guppi`).

> **problem:**
> Without the change `CLAUDE.md` and `index.md` name two tickers of three, and Retro counts a `guppi sprint` line as debt although the librarian ticks it.

### Case 253.1 — `rule-case-protocol`: three tickers

> **given:**
> `CLAUDE.md` is the Render of `rule-case-protocol`; `case-schema.md` is imported into it; §1 of `index.md` describes `spec.md`.
> **＋** The reading of `estimate-case-protocol-loaded` is the first turn of a session, without a read call.

> **when:**
> A session starts with `CLAUDE.md`.

> **then:**
> The Case protocol says Work Mode ticks the boxes on code, tests, migrations and readings; `generate`, `render` and `sprint` tick the page, render and sprint lines (cases 226, 250).
> **＋** `case-schema.md` and `index.md` say the same.

```then
update:
  - slug: rule-case-protocol
    replace:
      - old: "`generate` and `render` tick the page and render lines (case 226)"
        new: "`generate`, `render` and `sprint` tick the page, render and sprint lines (cases 226, 250)"
    change: sprint is the third ticker of the Spec — the sprint lines (case 253.1)
  - slug: estimate-case-protocol-loaded
    set: {status: pending}
    sections:
      Criterion: |
        When:
        A session starts with `CLAUDE.md`.

        Then:
        The agent states the LEDGER-block rule and the one-Case-at-a-time rule without a read
        call.
        **＋** The Case protocol says the Spec is `raw/<date>/<hi HHMM>/spec.md` — the
        `## Deferred` heading, the ticked boxes — and the Frontier
        `raw/<date>/<hi HHMM>/frontier.md`.
        **＋** A reply with a `LEDGER` block ends in that text; no tool call follows in the
        same reply — the text before a tool call waits for the next `Stop` of the session,
        and the last reply of a session has none.
        **＋** A block a tool call did follow the agent does not call lost before the `Stop`
        of that turn; at the next `Stop` it checks the ledger, and only a line missing there
        is a lesson.
        **＋** The Case protocol says Work Mode ticks the boxes on code, tests, migrations and
        readings, and `generate`, `render` and `sprint` tick the page, render and sprint lines
        (cases 226, 250).
        **－** A reply whose ledger lines sit outside a `LEDGER` block — bare, or in a fence
        with another tag or none — adds nothing to the session's ledger.
    change: one line of the Criterion — sprint is the third ticker (case 253.1)
  - file: vault/wiki/case-schema.md
    change: "the sentence of the Spec paragraph: `generate`, `render` and `sprint` tick the page, render and sprint lines (cases 226, 250)"
  - file: vault/wiki/index.md
    change: "§1, the `spec.md` line: the page, render and sprint lines by `generate`, `render` and `sprint` (cases 59.3, 226, 250)"
```

```tasks
- [ ] update `rule-case-protocol`: `replace` in the Render
- [ ] update `estimate-case-protocol-loaded`: one line of the Criterion, `pending`
- [x] `vault/wiki/case-schema.md`: the same sentence, by hand
- [x] `vault/wiki/index.md` §1: the `spec.md` line, by hand
- [ ] `uv run guppi render` at the librarian's run
- [ ] read `estimate-case-protocol-loaded` — the first turn of the next session
```

### Case 253.2 — `rule-retro`: a `guppi sprint` line waits for the librarian

> **given:**
> Retro runs before the librarian; `generate`, `render` and `sprint` tick the page, render and sprint lines after it (cases 226, 250).

> **when:**
> The person invokes `/retro`, and the agent counts the unticked `tasks` of the Spec.

> **then:**
> A `create`, `update` or `defer` line of a page, a `guppi render` line and a `guppi sprint` line are listed as waiting for the librarian and end in none of the four ways; every other unticked line is debt, as today.
> **－** Nothing else in Retro changes.

```then
update:
  - slug: rule-retro
    replace:
      - old: "a `create`, `update` or `defer` line of a page and a `guppi render` line listed as waiting for the librarian, who ticks them (case 226), not as debt"
        new: "a `create`, `update` or `defer` line of a page, a `guppi render` line and a `guppi sprint` line listed as waiting for the librarian, who ticks them (cases 226, 250), not as debt"
    change: a guppi sprint line of the Spec waits for the librarian and is not debt at Retro (case 253.2)
  - slug: estimate-retro-loads
    set: {status: pending}
    change: the Criterion replaced whole — a guppi sprint line waits for the librarian too (case 253.2)
```

```tasks
- [ ] update `rule-retro`: `replace` in the Render
- [ ] update `estimate-retro-loads`: the Criterion replaced whole, `pending`
- [ ] `uv run guppi render` at the librarian's run
- [ ] read `estimate-retro-loads` — the first live `/retro`
```

## Deferred

## Case 252 — `rule-work-mode`, `rule-subagent-guppi`: Slice 3b to the next session

> **context:**
> `rule-work-mode` and `rule-subagent-guppi` are the two items of Slice 3b, the current milestone, both placeholders in `draft`, deferred by 183, 206, 218, 231, 242 and 248; the draft of Work Mode stands in `docs/migration/rule-work-mode.md`. Since case 245 the item of `rule-work-mode` also names `insight-workflow-code-live-before-the-page-it-reads`, whose sentence enters the rule; the defer of 238 on that Insight, without a `purpose`, closes with the Slice. This session took F2 (Case 250) and closed F3 as `work`; Plan Mode closes for a live reading of `/carry` — the Spec is conserved, Work Mode on 250 runs in the next session.

> **problem:**
> Slice 3b is a whole session's work: the body of two rules, their Estimates, the code of Work Mode. The session closes on the reading of `/carry` with one Case in the Spec; Slice 3b stays the first item of the next session, after Work Mode on 250.

```then
defer:
  - slug: rule-work-mode
    type: rule
    purpose: Slice 3b, the first item of the next session after Work Mode on case 250 — the body of Work Mode with the sentence of the Insight on a check that reads a page the same Spec changes
  - slug: rule-subagent-guppi
    type: rule
    purpose: Slice 3b, with rule-work-mode — what a subagent may do in Work Mode, and the fork that comes back as a Case
```
