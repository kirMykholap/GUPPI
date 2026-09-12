<!-- approved 10:48:13 · session 763dd08e -->

# Spec — 2026-09-12, session I

Plan Mode over the Frontier of `brief.md` and the uncommitted ledger tail of session H.
Cases in the order ratified. The `then` blocks are what `guppi materialize` reads.

Before Work Mode, outside any Case (ratified earlier, Case 54 and the Retro of session H):
`uv run guppi render` on the five files `guppi render --check` names (`ask-guppi.md`,
`librarian-guppi.md`, `pre-task/SKILL.md`, `retro/SKILL.md`, `CLAUDE.md`), `make style`,
`make test`, then one commit with the six uncommitted lines of `raw/2026-09-11/ledger.md`.
`vault/Untitled.canvas` (an empty `{}` left by Obsidian) is not committed. `CLAUDE.md` is
restored from HEAD after the render: its Case protocol paragraph carries the Retro sentence
of case 56 by hand, and the Render of `rule-case-protocol` does not yet (case 59.5 puts it
there; the librarian generates, the next session renders); `guppi render --check` stays
red on that one file until then, and the brief flags it. The live reading
of `estimate-spec-capture-appends` is taken on this approval: a rejected plan of 04:58 wrote
nothing (no `raw/2026-09-12/spec.md`, no hook line in the event log); the approved plan lands
by the hook, with its stamp, once.

The fix of `check_decision` (an archived target counted as missing, the lesson of
2026-09-11) folds into the rewrite of case 59.4.

## Work Mode order

Every task is a box in the `tasks` block of its Case; ticked in `vault/raw/2026-09-12/spec.md`
as it finishes (case 59.3). The order between Cases:

1. `vault/raw/2026-09-12/frontier.md` from the list of `/hi`, every line closed (59.2);
   the estimate line of `estimate-spec-capture-appends` on the approval.
2. Render, restore `CLAUDE.md`, `make style`, `make test`, commit with the ledger tail.
3. Code, test-first, `make test` green and `make style` clean after each: `guppi/pretask.py`
   `--check` (59.1, 59.2, 59.3, 59.6); `guppi/guard.py` (59.6); `guppi/render.py` `--sync`
   (59.7); `guppi/generate.py` and `guppi/lint.py` (59.4); `guppi/materialize.py` (59.8,
   60, 61). One commit per Case or per script.
4. Rule-class files by hand, each named by a `file` item: `index.md` (§1 59.2, 59.3; §5
   59.4; §9 59.3), `glossary.md` (59.4, 59.8), `case-schema.md` (59.3, 59.5, 59.8, 60, 62),
   `decisions/schema.yaml` and `schema.md` (59.4). No governed file is touched by hand.
5. One-offs, scratchpad scripts run once: the 78 decision pages (59.4); `## Given` on ten
   pages (60). `sprint.md`: the four Slice-5 items (59.5); Slice 3 closed if 58 passes.
6. Readings, each an `estimate[...]` line the moment it exists: `estimate-documentation-completes`
   (58) from the event log of session H; `estimate-pretask-reconciles` and
   `estimate-hi-writes-frontier` at this session's `/pre-task` run of the new command;
   `estimate-generate-writes`, `estimate-lint-catches`, `estimate-materialize-assembles`
   (unit). `estimate-retro-loads` at `/retro`. Named in the handoff for the next session:
   the live probes of 59.6, 59.7, 59.8 and the live half of `estimate-generate-writes`.
7. The four memory files deleted (62). `/retro`, commit, `/handoff`, the librarian.

## Verification

- `make test` green, `make style` clean, `uv run guppi pretask --check <this plan>` prints
  nothing after the code of 59.1–59.3 and 59.6 exists.
- `guppi lint`: 0 findings of class `decision` after the migration of 59.4; no `## Given`
  finding on the ten pages of 60.
- `git status` clean before `/handoff` but for `vault/Untitled.canvas`.

## Case 59 — the artifacts of Plan Mode hold together mechanically

> **context:**
> Plan Mode leaves four things behind: the Frontier it opened with, the ledger lines the
> Stop hook wrote at each ratification, the Spec the human approved, and the Decision pages
> the librarian generates from both. In sessions G and H the four drifted: three decision
> lines had no item under their Case in the Spec (`lesson-spec-then-items-unchecked-against-
> ledger-lines`); the Frontier lived in the agent's memory and a plan was closed on one item
> of it (`lesson-plan-mode-exited-per-frontier-item`); a Decision page shows its targets as
> two lists aligned by position, unreadable; the items left over at the end of a session are
> carried by the brief's counter, not by a decision.

> **problem:**
> Each drift has a mechanical check or a form that removes it, and none is written. The
> sub-cases below fix one each; they share this context and are ratified apart. In Work
> Mode a fork is not a return to Plan Mode: the subagent stops, the fork is written as a
> Case in the short form, shown at Retro, appended to the Spec with a `defer`, and the plan
> stays unfinished until the next session (the owner, 2026-09-12; a clause of
> `rule-work-mode`, Slice 3b).

### Case 59.1 — pre-task checks every decision line of the session against the plan

> **recommend:**
> A command `uv run guppi pretask --check <plan file>` in `guppi/pretask.py`: it reads every
> decision line written since this session's `hi` (the window the ledger hook uses, across
> midnight), parses the plan by the Case headings and `then` blocks of `materialize`, and
> prints one finding per decision line whose slug has no item of its kind under its own
> Case heading, and one per item that has no decision line; exit 1 on a finding, 0 when the
> two sets match. The `/pre-task` skill runs it before dispatching `ask-guppi`; a finding is
> fixed in the plan, not raised as a Case. The `PreToolUse` payload of `ExitPlanMode`
> carries no plan (`tool_input` is `{}`), so the hook cannot do this; the skill runs before
> approval and the agent knows the plan file's path.

> **given:**
> `rule-pretask` (Leaf, `built`, `render`, governs `.claude/skills/pre-task/SKILL.md`, no
> `implementation_ref`) lists the decisions and dispatches `ask-guppi`; its Estimate
> `estimate-pretask-reconciles` (`passed`) reads "the event log gains a `pretask` line, the
> `ask-guppi` agent is dispatched once … every finding raised as a Case or named as known".
> **＋** `rule-pretask-hook` (`built`, `hook`, `guppi/pretask.py`) gates `ExitPlanMode` on
> the `pretask` line; its payload has no plan (`lesson-hooks-exitplanmode-payload`).
> **＋** `guppi/materialize.py` has `split_cases`, `then_blocks` and `find_item`, the
> parsers the check reuses; `guppi/ledger.py` has `session_event_log`, the `hi` window.
> **＋** The decision lines of this session are in `raw/<date>/ledger.md` before approval:
> the Stop hook writes them at the reply that acknowledges ratification.
> **－** `rule-spec-capture` and `guppi/spec.py` are not touched; the check runs before the
> plan exists as a Spec.
> **－** An `estimate` or `lesson` line is not checked: it has no item in the Spec.

> **when:**
> The person or the agent invokes `/pre-task` in a working session with a plan file.

> **then:**
> `uv run guppi pretask --check <plan file>` runs first and prints its findings.
> **＋** Every decision line since the session's `hi` finds an item with its slug under the
> key of its kind in a `then` block under its own `## Case N` or `### Case N.M` heading; a
> `defer` line finds a `defer` item; a Rule-class `file` line finds an item with that `file`.
> **＋** Every item in a `then` block of the plan has a decision line of its Case.
> **＋** A mismatch is one line on stdout naming the Case, the kind and the slug; exit 1. No
> mismatch: exit 0, nothing printed.
> **＋** The skill tells the agent to fix the plan for every finding before `ask-guppi` is
> dispatched, and to run the check again.
> **－** A session without a `hi` is not checked: exit 0, one line on stderr.
> **＋** `estimate-pretask-reconciles` gains the clause and goes `pending`; the live reading
> is the `/pre-task` of this session, after the code exists.

> **ratification:**
> Ratified by the owner in chat, 2026-09-12.
>
> ```
> - decision[59.1][update][rule-pretask]{ref:rule-pretask}
> - decision[59.1][update][estimate-pretask-reconciles]{ref:estimate-pretask-reconciles}
> ```

```then
update:
  - slug: rule-pretask
    replace:
      - old: "Recorded: !`uv run guppi event pretask --session \"${CLAUDE_SESSION_ID:-}\"`\n\nList every decision ratified in this Plan Mode"
        new: "Recorded: !`uv run guppi event pretask --session \"${CLAUDE_SESSION_ID:-}\"`\n\nRun `uv run guppi pretask --check <the plan file of this Plan Mode>`. It prints one line\nfor every decision line of this session that has no item under its own Case in the plan,\nand for every item that has no line. Fix the plan for each, then run it again until it\nprints nothing.\n\nList every decision ratified in this Plan Mode"
    change: the skill runs guppi pretask --check on the plan file before ask-guppi; every decision line since hi has its item under its own Case, every item its line (the command lives in guppi/pretask.py under rule-pretask-hook, case 66)
  - slug: estimate-pretask-reconciles
    replace:
      - old: "One live run before a plan approval: the event log gains a `pretask` line, the `ask-guppi`\nagent is dispatched once"
        new: "Unit: `guppi pretask --check <plan>` against a temp vault — a decision line with its item\nunder its own Case passes; a line without an item, an item without a line, and an item\nunder another sub-case's heading are each one finding, exit 1; a `defer` line matches a\n`defer` item and a `file` line an item with that `file`; no `hi`, exit 0 with a line on\nstderr. One live run before a plan approval: the check runs first and its findings are\nfixed in the plan; the event log gains a `pretask` line, the `ask-guppi`\nagent is dispatched once"
    set: {status: pending}
    change: the mechanical check of the plan against the session's decision lines joins the criterion; pending for the reading at this session's pre-task (case 59.1)
```

```tasks
- [x] guppi/pretask.py: `--check <plan>` — the decision lines since this session's hi (ledger.session_event_log for the window, the ledger files of its dates) against the then items under their own Case heading (materialize.split_cases, then_blocks, find_item); one line per mismatch, exit 1; no hi → exit 0, one line on stderr; the CLI entry
- [x] tests/test_pretask.py: a line with its item passes; a line without an item; an item without a line; an item under another sub-case; defer↔defer; file↔file; no hi
- [ ] take the reading of estimate-pretask-reconciles at this session's /pre-task, with the checks of 59.2, 59.3 and 59.6 in the same command; write the estimate line
```

### Case 59.2 — the Frontier is a file: `raw/<date>/frontier.md`, written at `/hi`, checked at pre-task

> **recommend:**
> The agent writes the Frontier it assembles at `/hi` to `raw/<date>/frontier.md`, one item
> per line in a fixed grammar, and closes each line as its item ends. `guppi pretask --check`
> reads the file of the session's `hi` date and fails on every open line, so "Plan Mode does
> not end while a Frontier item is neither ratified nor deferred" becomes a check, not a
> memory. A Markdown task list, not YAML frontmatter: one grammar per line as in the ledger,
> one `Edit` per item, Obsidian renders the boxes, a regex parses them.
>
> ```
> - [ ] F3 — Slice 3: documentation-completes failed on the Makefile · brief next 3
> - [x] F3 — Slice 3: documentation-completes failed on the Makefile · brief next 3 · case 58
> - [x] F1 — render five files, commit the ledger tail · brief next 1 · work
> - [-] F7 — Slice 3c raw lifecycle · brief deferred 7 · defer case 63
> ```
>
> `[ ]` open; `[x]` closed by `case N` (ratified) or `work` (no decision, one line in the
> Work Mode order); `[-]` deferred by `defer case N`. After the first `·` the source: a
> brief section and number, `ledger tail`, `retro H`, `owner`. Ids `F1…Fn` live in the
> session only. An item the owner adds mid-session is a new line with the next id.

> **given:**
> `rule-skill-hi` (MOC, `built`, `render`, governs `.claude/skills/hi/SKILL.md`) says
> "Assemble the Frontier from the above and present it as a list … Wait for the human to
> pick the order or defer items"; its Estimate `estimate-hi-no-read-calls` (`passed`) checks
> the loading and the `hi` line, not what the agent writes.
> **＋** `rule-case-protocol` (Render in `CLAUDE.md`) says "Plan Mode does not end while a
> Frontier item is neither ratified nor deferred" and names no file.
> **＋** `rule-pretask` gains `guppi pretask --check <plan>` by case 59.1; `guppi/pretask.py`
> already reads the session's window from the event log.
> **＋** `index.md` §1 lists the files of `raw/<date>/`: `ledger.md`, `event_log.md`,
> `spec.md`, `plan.md`, `handoff.md`, `materialize.yaml`; no `frontier.md`.
> **＋** The date of the file is the date of the session's `hi`, as for the ledger across
> midnight (case 55.1).
> **－** A Work Mode fork does not reopen Plan Mode (case 59, the owner): the file is written
> once per session and only closed afterwards; no second-entry clause.
> **－** The librarian does not read `frontier.md`; it is not one of its four inputs.

> **when:**
> The person invokes `/hi`, and later the agent or the person invokes `/pre-task`.

> **then:**
> After `/hi` the agent writes `raw/<date>/frontier.md`: the same items it presented, one
> line each, all `[ ]`, in the grammar above.
> **＋** When a Case is ratified or deferred, or a mechanical item goes into the Work Mode
> order, the agent closes its line in the same reply.
> **＋** `guppi pretask --check <plan>` reads the file of the `hi` date: no file is one
> finding; every `[ ]` line is one finding; a `[x] … case N` line whose `## Case N` or
> `### Case N` heading is not in the plan is one finding; a `[-] … defer case N` line
> without a `defer` item under Case N is one finding; `work` is not checked. Exit 1 on any,
> with the findings of 59.1.
> **＋** `CLAUDE.md` names the file: the Frontier is `raw/<date>/frontier.md`, closed line by
> line as the session goes.
> **＋** `index.md` §1 lists `frontier.md` under `raw/<date>/`.
> **＋** A new Estimate `estimate-hi-writes-frontier` (QA) under `rule-skill-hi` reads the
> file after this session's `/hi` and the check at its `/pre-task`; `estimate-hi-no-read-calls`
> stays as it is.

> **ratification:**
> Ratified by the owner in chat, 2026-09-12.
>
> ```
> - decision[59.2][update][rule-skill-hi]{ref:rule-skill-hi}
> - decision[59.2][create][estimate-hi-writes-frontier]{ref:rule-skill-hi}{tags:session,harness,workflow}
> - decision[59.2][update][rule-pretask]{ref:rule-pretask}
> - decision[59.2][update][estimate-pretask-reconciles]{ref:estimate-pretask-reconciles}
> - decision[59.2][update][rule-case-protocol]{ref:rule-case-protocol}
> - decision[59.2][update][index]{ref:index}
> ```

```then
create:
  - slug: estimate-hi-writes-frontier
    type: estimate
    ref: rule-skill-hi
    kind: QA
    tags: [session, harness, workflow]
    context: |
      The Frontier lived in the agent's memory; a plan was closed on one item of it
      (lesson-plan-mode-exited-per-frontier-item). The file makes the rule checkable.
    criterion: |
      After `/hi`, `raw/<date>/frontier.md` exists with one line per item the agent presented,
      each `- [ ] F<n> — <title> · <source>`. At `/pre-task` of the same session every line is
      `[x] … · case N`, `[x] … · work` or `[-] … · defer case N`, and `guppi pretask --check`
      prints no frontier finding; unit: a missing file, an open line, a `case N` without its
      heading, a `defer case N` without its item are each one finding, exit 1.
    method: |
      pytest in `tests/test_pretask.py` against a temp plan and frontier; the live reading at
      this session's `/hi` (the file written by hand from the presented list) and `/pre-task`.
update:
  - slug: rule-skill-hi
    set: {estimates: [estimate-hi-no-read-calls, estimate-hi-writes-frontier]}
    replace:
      - old: "Assemble the Frontier from the above and present it as a list: tasks, problems, debt\ncarried over, where the sprint stands; on a plan branch the unfinished plan comes first.\nA failed pull or an unavailable `gh` is an item on that list, not a reason to stop. Wait\nfor the human to pick the order or defer items."
        new: "Assemble the Frontier from the above and present it as a list: tasks, problems, debt\ncarried over, where the sprint stands; on a plan branch the unfinished plan comes first.\nA failed pull or an unavailable `gh` is an item on that list, not a reason to stop. Write\nthe same list to `vault/raw/<date>/frontier.md`, one line per item:\n`- [ ] F<n> — <title> · <source>`. Close a line when its item ends: `[x] … · case N`\nwhen ratified, `[x] … · work` when it needs no decision, `[-] … · defer case N` when\ndeferred; an item the person adds is a new line. `/pre-task` fails on an open line. Wait\nfor the human to pick the order or defer items."
    sections:
      Estimates: |
        - [[estimate-hi-no-read-calls]]
        - [[estimate-hi-writes-frontier]]
    change: the Frontier is written to raw/<date>/frontier.md and closed line by line; estimate-hi-writes-frontier added
  - slug: rule-pretask
    replace:
      - old: "Run `uv run guppi pretask --check <the plan file of this Plan Mode>`. It prints one line\nfor every decision line of this session that has no item under its own Case in the plan,\nand for every item that has no line. Fix the plan for each, then run it again until it\nprints nothing."
        new: "Run `uv run guppi pretask --check <the plan file of this Plan Mode>`. It prints one line\nfor every decision line of this session that has no item under its own Case in the plan,\nfor every item that has no line, and for every line of `raw/<date>/frontier.md` still\nopen or closed by a Case the plan does not hold. Fix the plan or the frontier for each,\nthen run it again until it prints nothing."
    change: the check also reads the session's frontier.md — an open line or a closing Case absent from the plan is a finding (case 59.2)
  - slug: estimate-pretask-reconciles
    replace:
      - old: "no `hi`, exit 0 with a line on\nstderr."
        new: "no `hi`, exit 0 with a line on\nstderr; the frontier of the `hi` date: a missing file, an open line, a `case N` without\nits heading and a `defer case N` without its item are each one finding."
    change: the frontier findings join the criterion (case 59.2)
  - slug: rule-case-protocol
    replace:
      - old: "Never move to the next Case until this\none is ratified or deferred. Plan Mode does not end while a Frontier item is neither\nratified nor deferred."
        new: "Never move to the next Case until this\none is ratified or deferred. The Frontier is `raw/<date>/frontier.md`, written at `/hi`;\nclose its line in the reply that ends the item. Plan Mode does not end while a line is\nopen; `/pre-task` checks it."
    change: the Frontier is a file, closed line by line (case 59.2)
  - file: vault/wiki/index.md
    change: "§1: `frontier.md` listed under `raw/<date>/` — the Frontier of the session, one line per item, closed as the session goes"
```

```tasks
- [x] vault/raw/2026-09-12/frontier.md written from the list of this session's /hi, first action of Work Mode; every line closed with its case, work or defer
- [x] guppi/pretask.py: the frontier findings — no file, an open line, `case N` without its heading, `defer case N` without its item; the file of the hi date
- [x] tests/test_pretask.py: the four frontier findings and a clean file
- [x] vault/wiki/index.md §1: frontier.md under raw/<date>/ (by hand, Rule-class)
- [ ] take the reading of estimate-hi-writes-frontier at this session's /pre-task; write the estimate line
```

### Case 59.3 — the Spec is written as ratified: five sections, a `then` block and a `tasks` block per Case

> **recommend:**
> The Spec and the plan are one artifact, written into the plan file as the conversation
> goes: at each ratification the agent appends the Case with `context`, `problem`, `given`,
> `when`, `then`, its `then` block (the pages in full, by their templates) and a block
> tagged `tasks`: one box per file to change, test to write, command to run, migration to
> run once, and one per Estimate the Case creates or sets `pending` ("take the reading of
> `estimate-x` by its method"). `recommend` and `ratification` stay in the chat. Code is not
> in the Spec; it is Work Mode. The hook copies the file to `raw/<date>/spec.md`; Work Mode
> ticks the boxes there, in the reply that finishes a task; Retro counts the unticked. The
> separate executable plan of the Work Mode draft (`plan.md`, `to-executable-plan`) is
> dropped: the human sees at approval what will be done, and a subagent executes a task,
> it does not transcribe a Spec.

> **given:**
> `rule-case-protocol` (Render in `CLAUDE.md`) says the page content is the `then` block
> under the Case in the Spec and names no `tasks`; `case-schema.md` says the same under "The
> `then` block lives in the Spec".
> **＋** `index.md` §1 lists `plan.md — executable plan` under `raw/<date>/` and §9 draws
> the chain "→ executable plan → branch + baseline commit → subagents → harness tests";
> `rule-work-mode` is a `draft` placeholder (Slice 3b), its draft in `docs/migration/`
> derives `plan.md` from the Spec by the skill `to-executable-plan`.
> **＋** `rule-retro` Render says "what got done and what did not, against the Spec" with
> nothing to count; `estimate-retro-loads` (`pending`) reads "done against the Spec" and
> still holds.
> **＋** `rule-spec-capture` names two writers of `spec.md`: the hook at approval and the
> agent at Retro under `## Retro`.
> **＋** `guppi materialize` reads the quoted sections and the `then` blocks by heading; a
> `tasks` block is a fenced block with another tag, which it ignores today.
> **＋** `guppi pretask --check` (59.1, 59.2) parses the plan by the same headings.
> **－** The Spec of this session is written this way from Case 58 on; the Specs of earlier
> dates are not rewritten.
> **－** The Work Mode draft (`docs/migration/rule-work-mode.md`) is a draft, not a page; it
> is reconciled when Slice 3b forms its Cases.

> **when:**
> A Case is ratified in Plan Mode; later the plan is approved, worked and reviewed at Retro.

> **then:**
> The agent appends the Case to the plan file in the same reply as its ledger lines: the
> five sections, the `then` block, the `tasks` block.
> **＋** A `tasks` block is a fenced block tagged `tasks`, one `- [ ] <what>` per line: a
> file and what changes in it, a test and what it pins, a command, a one-off migration, a
> reading of an Estimate by its method. One line per Estimate the Case creates or sets
> `pending`, naming its slug.
> **＋** `guppi pretask --check` reports a Case that has decision lines and no `tasks` block,
> and a `tasks` block without a line for an Estimate its `then` block creates or sets
> `pending`, one finding each.
> **＋** Work Mode ticks a box in `raw/<date>/spec.md` in the reply that finishes the task;
> a box for a reading is ticked in the reply that writes the `estimate[...]` line.
> **＋** Retro opens with the count of unticked boxes per Case of `raw/<date>/spec.md`, each
> ending as a reading, a lesson, a short defer or a handoff note, as `rule-retro` says.
> **＋** `CLAUDE.md`, `case-schema.md` and `index.md` say so; `plan.md` leaves §1 and the
> chain of §9 reads "→ the tasks of the Spec → branch + baseline commit → subagents →
> harness tests".
> **＋** `rule-spec-capture` names the third writer: Work Mode, ticking boxes only.

> **ratification:**
> Ratified by the owner in chat, 2026-09-12.
>
> ```
> - decision[59.3][update][rule-case-protocol]{ref:rule-case-protocol}
> - decision[59.3][update][case-schema]{ref:case-schema}
> - decision[59.3][update][index]{ref:index}
> - decision[59.3][update][rule-retro]{ref:rule-retro}
> - decision[59.3][update][rule-spec-capture]{ref:rule-spec-capture}
> - decision[59.3][update][rule-pretask]{ref:rule-pretask}
> - decision[59.3][update][estimate-pretask-reconciles]{ref:estimate-pretask-reconciles}
> ```

```then
update:
  - slug: rule-case-protocol
    replace:
      - old: "materialize` reads it, and what is not in that block was signed by nobody."
        new: "materialize` reads it, and what is not in that block was signed by nobody.\n\nThe Spec is the plan file, written as each Case is ratified, in the reply that\ncarries its ledger lines: `context`, `problem`, `given`, `when`, `then`, the `then`\nblock and a block tagged `tasks` — one `- [ ] <what>` per file, test, command and\none-off migration, and one per reading of an Estimate the Case creates or sets\n`pending`, by its slug; no `recommend`, no `ratification`, no code. Work Mode ticks\nthe boxes in `raw/<date>/spec.md` in the reply that finishes the task; Retro\ncounts the unticked."
    change: the Spec is written as ratified, with a tasks block per Case; boxes ticked in Work Mode, counted at Retro (case 59.3)
  - file: vault/wiki/case-schema.md
    change: "under 'The `then` block lives in the Spec': the Spec is written into the plan file at each ratification — the five sections, the `then` block and a `tasks` block, one box per file, test, command, migration and per reading of an Estimate created or set pending; `recommend` and `ratification` stay in the chat; code is Work Mode; boxes are ticked in `raw/<date>/spec.md`, the unticked are Retro's count"
  - file: vault/wiki/index.md
    change: "§1: `plan.md` removed from `raw/<date>/`; `spec.md` described as the Cases, their `then` blocks and their `tasks`, ticked in Work Mode. §9: the chain reads '→ the tasks of the Spec → branch + baseline commit → subagents → harness tests'; the Work Mode row no longer names an executable plan"
  - slug: rule-retro
    replace:
      - old: "by Case, one line per Case); what got done and what did not, against the Spec; what"
        new: "by Case, one line per Case); the `tasks` of `raw/<date>/spec.md`, the unticked boxes\nper Case; what"
    change: Retro counts the unticked tasks of spec.md instead of judging done against the Spec (case 59.3)
  - slug: rule-spec-capture
    replace:
      - old: "The file has\na second writer: at Retro the agent appends the short-form Cases under a `## Retro`\nheading, before their ledger lines (`rule-retro`)."
        new: "The file has\ntwo more writers: in Work Mode the agent ticks the boxes of the `tasks` blocks, and\nnothing else; at Retro the agent appends the short-form Cases under a `## Retro`\nheading, before their ledger lines (`rule-retro`)."
    change: Work Mode is the third writer of spec.md, ticking boxes only (case 59.3)
  - slug: rule-pretask
    replace:
      - old: "for every item that has no line, and for every line of `raw/<date>/frontier.md` still\nopen or closed by a Case the plan does not hold."
        new: "for every item that has no line, for every line of `raw/<date>/frontier.md` still\nopen or closed by a Case the plan does not hold, for every ratified Case without a\n`tasks` block, and for every Estimate a `then` block creates or sets `pending` that no\ntask names."
    change: a Case without tasks and an Estimate without its reading task are findings (case 59.3)
  - slug: estimate-pretask-reconciles
    replace:
      - old: "a `defer case N` without its item are each one finding."
        new: "a `defer case N` without its item are each one finding; a Case with decision lines and\nno `tasks` block, and an Estimate created or set `pending` by a `then` block that no\ntask names, are each one finding."
    change: the tasks findings join the criterion (case 59.3)
```

```tasks
- [x] guppi/pretask.py: a Case with decision lines and no tasks block; an Estimate a then block creates or sets pending that no task line names
- [x] tests/test_pretask.py: both findings and a Case that passes
- [x] vault/wiki/index.md §1 (plan.md out, spec.md described) and §9 (the chain) by hand
- [x] vault/wiki/case-schema.md: the paragraph under "The then block lives in the Spec" by hand
- [x] tick the boxes of this Spec in vault/raw/2026-09-12/spec.md as each task finishes
```

### Case 59.4 — a Decision page names its targets by kind: `create`, `update`, `delete`, `defer` lists

> **recommend:**
> Replace the two aligned lists with one list per kind present: `create: [a, b]`,
> `update: [c]`, `delete: [...]`, `defer: [...]`; a kind with no line is absent. No repeated
> word, the kind of each target visible, Obsidian renders it, lint checks each list. One
> page per Case stays: a Case is atomic by construction, so its context holds for every
> target; a target that needed its own context would have split into a sub-case with its own
> page. The 78 live pages are migrated once by script, each with one History line. Case
> 52.1 stays `current`: its body sections hold, only the field shape changes.
>
> ```
> ---
> type: decision
> case: "59.4"
> status: current
> update: [decisions-schema-yaml, decisions-schema, rule-page-generation, estimate-generate-writes, rule-lint, estimate-lint-catches, index, glossary]
> ...
> ```

> **given:**
> `decisions/schema.yaml` requires `kind` and `target_slug`, "two lists aligned by position,
> one position per ledger line of the Case" (case 52.1); `schema.md` shows the example
> `kind: [create, create]` / `target_slug: [entity-cart, estimate-cart-render-time]`.
> **＋** `rule-page-generation` (`draft`, `guppi/generate.py`) writes the two lists in
> `decision()` and reads them in `clear_deferred_by()` to find the `defer` targets of a
> superseded decision; `estimate-generate-writes` (`pending`) says "kind and target_slug
> aligned by position".
> **＋** `rule-lint` (`built`, `guppi/lint.py`) checks "kind and target_slug of equal length;
> every target_slug with a category prefix an existing page" in `check_decision`;
> `estimate-lint-catches` (`passed`) seeds "decision lists of unequal length, a target_slug
> naming no page". `check_decision` looks a slug up among live pages only; the fix outside
> any Case (the lesson of 2026-09-11) folds into this rewrite.
> **＋** `index.md` §5 and the glossary row "Routing Table, Decision page" describe the two
> lists.
> **＋** 78 live decision pages carry the two lists, 9 of them `superseded`; no decision page
> is archived.
> **＋** A Rule-class file is named by its slug in a list, as in a ledger line: `index`,
> `glossary`, `case-schema`, `decisions-schema-yaml`.
> **－** `deferred_by` on target pages, `superseded_by`, `source`, `supersedes` and the body
> sections do not change.
> **－** `materialize.yaml` does not change: its `targets` already carry `kind` and `slug`
> per line; `generate` regroups them.

> **when:**
> `guppi generate` writes a Decision page; `guppi lint` reads one; the migration runs once.

> **then:**
> The page has one list per kind present among the Case's ledger lines, `create`, `update`,
> `delete`, `defer`, in that order, each the slugs of those lines in ledger order; `kind`
> and `target_slug` are not written.
> **＋** `clear_deferred_by` reads the `defer` list of the superseded page.
> **＋** `guppi lint`: a decision page with none of the four lists is a finding; a slug with a
> category prefix that names neither a live nor an archived page is a finding; `kind` or
> `target_slug` present on a decision page is a finding.
> **＋** `schema.yaml` requires none of the four and lists them as optional with the rule in a
> comment; `schema.md` shows the new example.
> **＋** The migration folds the two lists of every live decision page into the four, drops
> the two fields, appends `- <date> fields kind and target_slug folded into create, update,
> delete, defer · [[decision-case-59.4]]` to History, and runs once under this Case; `guppi
> lint` is 0 findings of class `decision` after it.
> **＋** `index.md` §5 and the glossary describe the four lists.
> **＋** `estimate-generate-writes` and `estimate-lint-catches` carry the new wording and go
> `pending`; their readings are taken at this session's tests and the librarian's run.

> **ratification:**
> Ratified by the owner in chat, 2026-09-12.
>
> ```
> - decision[59.4][update][decisions-schema-yaml]{ref:decisions-schema-yaml}
> - decision[59.4][update][decisions-schema]{ref:decisions-schema}
> - decision[59.4][update][rule-page-generation]{ref:rule-page-generation}
> - decision[59.4][update][estimate-generate-writes]{ref:estimate-generate-writes}
> - decision[59.4][update][rule-lint]{ref:rule-lint}
> - decision[59.4][update][estimate-lint-catches]{ref:estimate-lint-catches}
> - decision[59.4][update][index]{ref:index}
> - decision[59.4][update][glossary]{ref:glossary}
> ```

```then
update:
  - file: vault/wiki/decisions/schema.yaml
    change: "`kind` and `target_slug` leave `required`; `create`, `update`, `delete`, `defer` join `optional` with the comment: one list per kind present among the Case's ledger lines, the slugs of those lines; at least one of the four; lint checks every page slug names a live or archived page (case 59.4)"
  - file: vault/wiki/decisions/schema.md
    change: "the field table and the example show `create: [entity-cart, estimate-cart-render-time]` in place of `kind` and `target_slug`; the prose says one list per kind present, in the order create, update, delete, defer"
  - slug: rule-page-generation
    replace:
      - old: "`kind` and `target_slug` (two lists aligned by position, one position per ledger line of the Case; the category is derived from the slug prefix or the Rule-class map, never written)"
        new: "one list per kind present among the Case's ledger lines — `create`, `update`, `delete`, `defer`, in that order, each the slugs of those lines in ledger order (the category is derived from the slug prefix or the Rule-class map, never written)"
      - old: "removes the earlier decision's slug from the `deferred_by` of every target it deferred"
        new: "removes the earlier decision's slug from the `deferred_by` of every target in its `defer` list"
    change: a decision page names its targets by kind — one list per kind present — instead of two lists aligned by position (case 59.4)
  - slug: estimate-generate-writes
    replace:
      - old: "one decision page per Case with kind and target_slug\naligned by position and the sections"
        new: "one decision page per Case with one list per kind present —\ncreate, update, delete, defer, the slugs in ledger order — and the sections"
    set: {status: pending}
    change: the decision page's four lists replace the aligned pair in the criterion (case 59.4)
  - slug: rule-lint
    replace:
      - old: "A decision page: `kind` and `target_slug` of equal length; every `target_slug` with a category prefix an existing page;"
        new: "A decision page: at least one of `create`, `update`, `delete`, `defer`, each a list of slugs, and neither `kind` nor `target_slug`; every slug with a category prefix a live or archived page;"
    change: decision pages checked on the four kind lists; a target resolves against live and archived pages (case 59.4)
  - slug: estimate-lint-catches
    replace:
      - old: "decision lists of unequal length, a target_slug naming no page,"
        new: "a decision page with none of the four kind lists or with kind or target_slug still present, a slug in one of the lists naming neither a live nor an archived page,"
    set: {status: pending}
    change: the decision classes of case 59.4 replace those of 52.1 in the criterion
  - file: vault/wiki/index.md
    change: "§5: 'one page in wiki/decisions/ (decision-case-<N>) recording the decision — one list per kind present, create, update, delete, defer, the slugs of its ledger lines (case 59.4) —' in place of the two aligned lists"
  - file: vault/wiki/glossary.md
    change: "row 'Routing Table, Decision page': 'one list per kind present: create, update, delete, defer' in place of 'kind and target_slug aligned by position'"
```

```tasks
- [x] guppi/generate.py: decision() writes create/update/delete/defer lists in that order, no kind or target_slug; clear_deferred_by reads the defer list
- [x] guppi/lint.py: check_decision on the four lists — none present, kind or target_slug present, a slug naming neither a live nor an archived page (the lesson of 2026-09-11 folds in)
- [x] tests/test_generate.py, tests/test_lint.py: the new shape, the archived target, the old fields as findings
- [x] vault/wiki/decisions/schema.yaml and schema.md by hand
- [x] one-off, scratchpad script, not kept: the 78 live decision pages folded into the four lists, kind and target_slug dropped, one History line each; guppi lint → 0 decision findings
- [x] vault/wiki/index.md §5 and vault/wiki/glossary.md row by hand
- [x] take the readings of estimate-generate-writes (unit now; live at the librarian's run of this session, read next session) and estimate-lint-catches (unit and the live vault after the migration); write the estimate lines
```

### Case 59.5 — the deferred decisions: a `## Deferred` section of the Spec, one short-form Case per decision

The owner's variant, 2026-09-12, replacing the first ratified form (one Case for every item
left): each deferred decision keeps its own context and its own Decision page; the Spec
gathers them under one `## Deferred` heading, at the close of Plan Mode and at Retro alike;
a deferred decision taken up later is built into a full Case from what its page holds.

> **given:**
> `case-schema.md` ("The short form of Retro") and `rule-case-protocol` allow the short
> form at Retro only; `rule-retro` appends such a Case under `## Retro`.
> **＋** `index.md` §5: a `defer` with an existing target appends `deferred_by`; without one
> the librarian creates a placeholder born with `deferred_by`; `guppi generate` does both
> (case 52.3). Not changed.
> **＋** `guppi materialize` marks a Case `incomplete` for a missing `given` or `when` only
> when a kind other than `defer` is among its lines (case 56). Not changed.
> **＋** `rule-brief` Render: "Deferred: at most seven items. Rank by the `severity` of a
> related Insight, then by the number of times the item was postponed. Take that number from
> the previous brief and add one." The source of the items is not named; the librarian
> takes them from the handoff today.
> **＋** The brief of 2026-09-11 carries seven deferred items; four of them are no page: item
> 2 (`/grill-me` without a page), 3 (`git pull` without upstream, owner's decision 11.1),
> 4 (`gh` not logged in, 11.2), 5 (the fate of `vault/parked/`, `vault/archive/`,
> `docs/superpowers/`, `docs/HANDOFF.md`, `docs/migration/rule-*.md`, the 2026-08 docs).
> All four are "Slice 5" by the brief or the owner.
> **＋** `sprint.md` is not a page and has no schema; the librarian changes it only when the
> handoff says; nothing forbids Work Mode under a ratified Case.
> **＋** The frontier grammar of 59.2 closes a deferred item as `[-] … · defer case N`, each
> with the number of its own Case.
> **＋** `rule-retro` and `rule-spec-capture` name the `## Retro` heading for the short-form
> Cases of Retro; `materialize` reads Cases by their `## Case N` headings wherever they sit.
> **＋** Two pages deferred by one decision under one context stay one Case (case 29:
> `rule-work-mode` and `rule-subagent-guppi`).
> **－** The items this session defers are chosen at its close, not here.

> **when:**
> The owner closes the discussion of Plan Mode with items left open, or Retro ends an item
> in a defer; later a deferred decision is taken up; later still the librarian writes the
> brief.

> **then:**
> Every deferred decision is its own Case in the short form — `context`, `problem`, a `then`
> block with `defer` — under one `## Deferred` heading of the Spec, one ledger line per
> target; its frontier line closes with that Case's number. Retro appends its short-form
> Cases under the same heading, which replaces `## Retro`.
> **＋** Two or more pages share one Case only when one context and one problem hold for all
> of them; otherwise they split.
> **＋** When a deferred decision is taken up, the agent builds the full Case from its page:
> `context` and `problem` as they stand, then `recommend`, `given` (the vault asked),
> `when`, `then`; the line carries `{supersedes:case N}`.
> **＋** `case-schema.md`, `CLAUDE.md`, `rule-retro` and `rule-spec-capture` say so.
> **＋** `rule-brief`: the Deferred list is built from the `defer` entries of the yamls the
> walk named, one item per target, its count from the previous brief plus one; a target of
> no defer entry this session that the previous brief listed keeps its line and its count
> plus one until a `supersedes` retires it.
> **＋** The four Slice-5 items of the brief go to `sprint.md` under Slice 5 in Work Mode of
> this session and leave the Deferred list; the handoff says so to the librarian.
> **－** An item that is a page or will be one is never moved to `sprint.md`; it is deferred.

> **ratification:**
> Ratified in the first form 2026-09-12; ratified again the same day in the owner's variant.
> The first three lines were written at the first ratification; the last two at the second.
>
> ```
> - decision[59.5][update][case-schema]{ref:case-schema}
> - decision[59.5][update][rule-case-protocol]{ref:rule-case-protocol}
> - decision[59.5][update][rule-brief]{ref:rule-brief}
> - decision[59.5][update][rule-retro]{ref:rule-retro}
> - decision[59.5][update][rule-spec-capture]{ref:rule-spec-capture}
> ```

```then
update:
  - file: vault/wiki/case-schema.md
    change: "section 'The short form of Retro' renamed 'The short form — deferred decisions': a deferred decision is its own Case — `context`, `problem`, a `then` block with `defer` — under the `## Deferred` heading of the Spec, at the close of Plan Mode or at Retro; two pages share one Case only under one context and one problem; a deferred decision taken up is built into a full Case from its page, `recommend`, `given`, `when`, `then` added, its line with `supersedes`; a page-less Slice task goes to `sprint.md`, not into a defer"
  - slug: rule-case-protocol
    replace:
      - old: "recommend, given, when, then, ratification. Never move to the next Case until this\none is ratified or deferred."
        new: "recommend, given, when, then, ratification. That is the form of Plan Mode. A deferred\ndecision — an item left open when the person closes Plan Mode, or an item Retro ends\nin a defer — is its own Case in the short form: context, problem, a `defer` block with\n`purpose`, under the `## Deferred` heading of `raw/<date>/spec.md`, before its ledger\nline (cases 56, 59.5); a page-less Slice task goes to `sprint.md` instead. Taking a\ndeferred decision up means building its full Case from its page — recommend, given,\nwhen, then added — and writing `{supersedes:case N}` on the line. Never move to the\nnext Case until this one is ratified or deferred."
    change: a deferred decision is its own short-form Case under ## Deferred, at the close of Plan Mode or at Retro; taken up, it becomes a full Case (case 59.5); the Retro sentence of case 56, written into CLAUDE.md by hand, joins the Render it belongs to
  - slug: rule-retro
    replace:
      - old: "under a `## Retro` heading before its ledger line: `## Case N`, `context`, `problem`,"
        new: "under the `## Deferred` heading before its ledger line: `## Case N`, `context`, `problem`,"
    change: the short-form Cases of Retro go under ## Deferred, the heading the closing defers of Plan Mode use (case 59.5)
  - slug: rule-spec-capture
    replace:
      - old: "at Retro the agent appends the short-form Cases under a `## Retro`\nheading, before their ledger lines (`rule-retro`)."
        new: "at the close of Plan Mode and at Retro the agent appends the short-form Cases\nunder the `## Deferred` heading, before their ledger lines (`rule-retro`)."
    change: the Deferred heading, written at the close of Plan Mode and at Retro (case 59.5)
  - slug: rule-brief
    replace:
      - old: "- Deferred: at most seven items. Rank by the `severity` of a related Insight, then\n  by the number of times the item was postponed. Take that number from the previous\n  brief and add one."
        new: "- Deferred: at most seven items, one per target of a `defer` entry in the yamls the\n  walk named, plus every item of the previous brief's list whose decision no\n  `supersedes` retired. Rank by the `severity` of a related Insight, then by the\n  number of times the item was postponed. Take that number from the previous brief\n  and add one."
    change: the Deferred list comes from the defer entries of the yamls and the previous brief, not from the handoff (case 59.5)
```

```tasks
- [x] vault/wiki/case-schema.md: "The short form", two moments, by hand
- [x] vault/wiki/sprint.md: the four Slice-5 items of the brief (/grill-me without a page; git pull without upstream, 11.1; gh not logged in, 11.2; the fate of vault/parked/, vault/archive/, docs/superpowers/, docs/HANDOFF.md, docs/migration/rule-*.md, the 2026-08 docs) under Slice 5; the handoff tells the librarian they left the Deferred list
- [x] Cases 63–65 under `## Deferred` are this session's deferred decisions; their frontier lines close with `defer case 63`, `64`, `65`
- [x] vault/wiki/case-schema.md: `## Retro` → `## Deferred` wherever named, by hand
```

### Case 59.6 — a governed harness file is never edited by hand: a hook refuses, pre-task checks, `CLAUDE.md` says so

The owner, 2026-09-12: no harness file has a hand-written part, `CLAUDE.md` included (it
becomes a full Render in case 59.8); the hook refuses every governed path whole. Cases 59.6,
59.7 and 59.8 are the three parts of that decision.

> **recommend:**
> Three things, one Case. (1) A hook `uv run guppi guard` on `PreToolUse` of `Edit`, `Write`
> and `MultiEdit`: it reads the `governs` field of every live Rule page; a tool call on a
> governed path exits 2 with the rule's slug and "change the Rule page through a decision".
> No exception: `CLAUDE.md` is governed whole by case 59.8. `guppi render` runs through
> Bash, not the edit tools, so the renderer passes; a subagent inherits no project hook, but
> the librarian writes only `wiki/`. (2) `guppi pretask --check`: a `file` item whose path a
> Rule page governs is a finding — such a file has no `file` route any more. (3) One
> sentence in the Render of `rule-case-protocol`, always in `CLAUDE.md`: the harness is
> rendered from `rules/`, a harness file changes through an `update` of its Rule page, a
> hook refuses the edit. A new Leaf under `rule-harness`, enforcement `hook`, with its
> Estimate.

> **given:**
> `rule-harness` (MOC, `built`, children `rule-render-harness`, `rule-hook-registry`,
> `rule-lint`, `rule-index`) holds the harness tools; `rule-render-harness` (`check`,
> `guppi/render.py`) keeps a Rule page and its file one text, and its live criterion says
> "no change to `CLAUDE.md`" after a render.
> **＋** Sixteen Rule pages carry `governs`: `.claude/skills/hi/SKILL.md` (four pages),
> `.claude/agents/librarian-guppi.md` (six), `.claude/agents/ask-guppi.md`,
> `.claude/skills/pre-task/SKILL.md`, `.claude/skills/retro/SKILL.md`,
> `.claude/skills/handoff/SKILL.md`, `.claude/settings.json` (`rule-hook-registry`),
> `CLAUDE.md` (`rule-case-protocol`).
> **＋** `rule-hook-registry` (`render`, governs `.claude/settings.json`) lists the hooks:
> `PreToolUse` has `ExitPlanMode` → `guppi pretask` and `Skill` → `guppi gate`; a new hook
> is an `update` of its Render (case 18.2).
> **＋** `guppi/pretask.py` reads the payload with `read_payload` and exits 2 to block;
> `tool_input` of `Edit` carries `file_path` and `old_string`, of `Write` `file_path` and
> `content` (the Slice 1 probes).
> **＋** Case 56 wrote the Retro sentence into `CLAUDE.md` by hand; `render --check` names
> the file; `lesson-render-governed-file-updated-as-rule-class-file` records it.
> **＋** The slug `rule-governed-files-hook` names no page; `guppi guard` names no command.
> **－** A path no Rule page governs is not touched: `vault/`, `guppi/`, `tests/`, the plan
> file, `docs/`.
> **－** The librarian, `ask-guppi` and any subagent are not gated: they inherit no project
> hook, and the librarian's own hook logs only.

> **when:**
> The agent calls `Edit`, `Write` or `MultiEdit` on a path some Rule page governs; `/pre-task`
> runs; a session starts with `CLAUDE.md`.

> **then:**
> The hook exits 2 naming the governing rule and the file; the tool does not run.
> **＋** Any other tool, or a path governed by no page, or a payload the hook cannot read:
> exit 0, the last with one line on stderr.
> **＋** `.claude/settings.json` registers the hook through the Render of `rule-hook-registry`.
> **＋** `guppi pretask --check` reports a `file` item on a governed path.
> **＋** `CLAUDE.md` carries the sentence in its Case protocol section.
> **＋** `estimate-governed-files-hook-refuses` reads: unit, the exits above against a temp
> vault; live, one probe in this session after the render, an `Edit` on
> `.claude/skills/hi/SKILL.md` refused with the rule named, in the event log.
> **－** Until case 59.8 is generated and rendered, `CLAUDE.md` keeps its hand-written
> sections; the hook refuses them all the same, since `rule-case-protocol` governs the file.

> **ratification:**
> Ratified by the owner in chat, 2026-09-12.
>
> ```
> - decision[59.6][create][rule-governed-files-hook]{ref:rule-harness}{tags:hooks,harness,render}
> - decision[59.6][update][rule-hook-registry]{ref:rule-hook-registry}
> - decision[59.6][update][rule-case-protocol]{ref:rule-case-protocol}
> - decision[59.6][update][rule-pretask]{ref:rule-pretask}
> - decision[59.6][update][estimate-pretask-reconciles]{ref:estimate-pretask-reconciles}
> ```

```then
create:
  - slug: rule-governed-files-hook
    type: rule
    kind: Leaf
    enforcement: hook
    implementation_ref: [guppi/guard.py, tests/test_guard.py, .claude/settings.json]
    purpose: Prevents a harness file rendered from a Rule page from being edited by hand
    tags: [hooks, harness, render]
    sections:
      Purpose: |
        Prevents a harness file rendered from a Rule page from being edited by hand. The
        renderer makes the page and the file one text; an edit to the file alone is lost at
        the next render, and what it carried was ratified for the page, not the file
        (case 56, `lesson-render-governed-file-updated-as-rule-class-file`).
      How it works: |
        `uv run guppi guard` on `PreToolUse` of `Edit`, `Write` and `MultiEdit`. It reads
        the `governs` field of every live Rule page under `vault/wiki/rules/`. A call whose
        `file_path` is a governed path exits 2 with the rule's slug and the file, which
        blocks the tool. No governed file has a hand-written part; `CLAUDE.md` is a full
        Render (case 59.8). Any other tool, an ungoverned path, or a payload the hook cannot
        read: exit 0, the last with one line on stderr. `guppi render` writes through Bash
        and passes; subagents inherit no project hook.
    estimate:
      slug: estimate-governed-files-hook-refuses
      kind: QA
      criterion: |
        Unit, against a temp vault with one governing page per file: an `Edit`, `Write` or
        `MultiEdit` on a governed path exits 2 naming the rule and the file; another tool,
        an ungoverned path and an unreadable payload exit 0. Live: one probe in the session
        that registers the hook —
        an `Edit` on `.claude/skills/hi/SKILL.md` refused, the rule named, the call in the
        event log.
      method: |
        pytest in `tests/test_guard.py` with piped payloads; the live probe once by hand,
        written into the estimate line.
update:
  - slug: rule-hook-registry
    replace:
      - old: "      { \"matcher\": \"Skill\",\n        \"hooks\": [ { \"type\": \"command\", \"command\": \"uv run guppi gate\", \"timeout\": 30 } ] }\n    ],"
        new: "      { \"matcher\": \"Skill\",\n        \"hooks\": [ { \"type\": \"command\", \"command\": \"uv run guppi gate\", \"timeout\": 30 } ] },\n      { \"matcher\": \"Edit|Write|MultiEdit\",\n        \"hooks\": [ { \"type\": \"command\", \"command\": \"uv run guppi guard\", \"timeout\": 30 } ] }\n    ],"
    change: guppi guard registered on PreToolUse of Edit, Write and MultiEdit (case 59.6)
  - slug: rule-case-protocol
    replace:
      - old: "Before a `create` without a `ref`, ask the vault first:"
        new: "The harness — hooks, skills, agents, `settings.json`, this section of `CLAUDE.md` —\nis rendered from `rules/`. A harness file changes through an `update` of its Rule\npage, never by hand; a hook refuses the edit.\n\nBefore a `create` without a `ref`, ask the vault first:"
    change: the harness changes through Rule pages, never by hand — one sentence always in CLAUDE.md (case 59.6)
  - slug: rule-pretask
    replace:
      - old: "for every ratified Case without a\n`tasks` block, and for every Estimate a `then` block creates or sets `pending` that no\ntask names."
        new: "for every ratified Case without a\n`tasks` block, for every Estimate a `then` block creates or sets `pending` that no\ntask names, and for every `file` item on a path a Rule page governs."
    change: a file item on a governed path is a finding — a rendered file has no file route (case 59.6)
  - slug: estimate-pretask-reconciles
    replace:
      - old: "that no\ntask names, are each one finding."
        new: "that no\ntask names, and a `file` item on a path a Rule page governs, are each one finding."
    change: the governed-file finding joins the criterion (case 59.6)
```

```tasks
- [x] guppi/guard.py and the CLI entry: PreToolUse payload of Edit, Write, MultiEdit; the governs set from the live rule pages; exit 2 naming the rule and the file; other tools, ungoverned paths, unreadable payloads exit 0
- [x] tests/test_guard.py: the refusals and the passes
- [x] guppi/pretask.py: a file item on a governed path is a finding; a test
- [ ] no hand edit of .claude/settings.json, the skills or CLAUDE.md in this session: the pages change at the librarian's run, the files at the next session's render; the live probe of estimate-governed-files-hook-refuses is taken then and named in the handoff
```

### Case 59.7 — `guppi render --sync` at `SessionStart`: the harness is rendered before the first turn, and what it overwrote is shown

> **recommend:**
> A `--sync` mode of `guppi render`, registered as a `SessionStart` hook after
> `guppi event session-start`: for every governed file that differs from its Rule page it
> prints a unified diff, current file to rendered text, on stdout, then writes the rendered
> text; nothing differs, nothing printed; a render error goes to stderr, exit 0 always, since
> `SessionStart` cannot block (`lesson-hooks-sessionstart-cannot-block`) and its stdout is
> added to the agent's context. So at the first turn the agent sees both the normal case —
> the librarian changed pages, the files caught up — and the other one — someone wrote into
> a rendered file by hand, and what they wrote — and can turn the second into a Case. The
> Frontier item "render, commit" disappears: the hook renders, the Retro commit carries it.
> One open fact: whether Claude Code reads `CLAUDE.md` before or after the `SessionStart`
> hooks. The new Estimate records it from a probe in this session.

> **given:**
> `rule-render-harness` (Leaf, `built`, enforcement `check`, `guppi/render.py`,
> `tests/test_render.py`, parent `rule-harness`) has `--check` and the plain write; its
> Estimate `estimate-render-harness-reproduces` (`passed`) reads the unit cases and one live
> reading of 2026-09-09.
> **＋** `guppi/render.py` has `plan`, `differing` and `write_all`; a diff is `difflib` of the
> standard library, no dependency.
> **＋** `rule-hook-registry` Render lists one `SessionStart` hook, `uv run guppi event
> session-start`.
> **＋** `lesson-hooks-sessionstart-cannot-block`: exit 2 is a no-op there. The stdout of a
> `SessionStart` hook is added to the context, by Claude Code's hook contract; not yet
> measured here.
> **＋** The brief of every session since Slice 2 opened with "run `guppi render` for the
> pages the librarian changed, then commit"; the files lag the pages for a whole session.
> **＋** `guppi gate` refuses `/handoff` on a dirty tree; the rendered files are committed at
> Retro with the session's work.
> **－** The librarian's run changes pages after the hook ran; the files lag until the next
> `SessionStart`, and `make lint` at the brief still reports them. Not changed here.
> **－** `--check` stays as it is for `make lint`.

> **when:**
> A session starts; later the agent reads its first turn.

> **then:**
> `uv run guppi render --sync` runs as the second `SessionStart` hook: for each differing
> governed file, a unified diff from the file to its rendered text on stdout, then the write;
> exit 0; a render error on stderr, nothing written.
> **＋** With no difference it prints nothing and writes nothing.
> **＋** `rule-render-harness` stays enforcement `check` (one value; `make lint` rests on it)
> and gains `.claude/settings.json` in `implementation_ref`; `rule-hook-registry` registers
> the hook (pre-task, case 66).
> **＋** `estimate-render-sync-reports` (QA) reads: unit, a differing file yields its diff and
> is written, an identical one nothing, a render error exit 0 with stderr; live, at the next
> session start the diff of this session's librarian changes is in the agent's first turn,
> and the probe records whether the `CLAUDE.md` the session loaded is the one the hook
> wrote.
> **＋** `rule-skill-hi` and the brief no longer ask for a render at the start.

> **ratification:**
> Ratified by the owner in chat, 2026-09-12.
>
> ```
> - decision[59.7][update][rule-render-harness]{ref:rule-render-harness}
> - decision[59.7][create][estimate-render-sync-reports]{ref:rule-render-harness}{tags:harness,render,hooks}
> - decision[59.7][update][rule-hook-registry]{ref:rule-hook-registry}
> - decision[59.7][update][rule-skill-hi]{ref:rule-skill-hi}
> ```

```then
create:
  - slug: estimate-render-sync-reports
    type: estimate
    ref: rule-render-harness
    kind: QA
    tags: [harness, render, hooks]
    context: |
      A rendered file lagged its page for a session at a time, and a hand edit to one was
      invisible until `render --check` named the file (case 56). The sync at session start
      closes both gaps if its output reaches the agent.
    criterion: |
      Unit: `guppi render --sync` against a temp vault prints a unified diff for a governed
      file that differs and writes the rendered text; prints and writes nothing for an
      identical one; on a render error prints to stderr, writes nothing, exits 0. Live: at
      the first session start after this one, the diff of the pages the librarian changed
      is in the agent's first turn, the files match their pages, `render --check` exits 0;
      the reading records whether the `CLAUDE.md` loaded by that session is the text the
      hook wrote (a marker sentence added by the librarian's run), or the text before it.
    method: |
      pytest in `tests/test_render.py`; the live reading by hand at the next session's
      first turn, written into the estimate line.
update:
  - slug: rule-render-harness
    set: {implementation_ref: [guppi/render.py, tests/test_render.py, .claude/settings.json], estimates: [estimate-render-harness-reproduces, estimate-render-sync-reports]}
    sections:
      How it works: |
        `uv run guppi render` writes every governed file from its Rule page; `--check`
        renders in memory and names the files that differ, for `make lint`; `--sync`, the
        `SessionStart` hook, prints a unified diff for each differing file — the file as it
        is, then the rendered text — and writes it, so the agent's first turn shows what
        the render changed: the pages the librarian updated, or a hand edit that is now
        gone and may deserve a Case. It exits 0 always; `SessionStart` cannot block, and a
        render error goes to stderr. The rendered files are committed at Retro.
      Estimates: |
        - [[estimate-render-harness-reproduces]]
        - [[estimate-render-sync-reports]]
      Implementation: |
        - `guppi/render.py`
        - `tests/test_render.py`
        - `.claude/settings.json`
    change: render --sync at SessionStart — diff on stdout, then the write; enforcement hook (case 59.7)
  - slug: rule-hook-registry
    replace:
      - old: "    \"SessionStart\": [\n      { \"hooks\": [ { \"type\": \"command\", \"command\": \"uv run guppi event session-start\", \"timeout\": 30 } ] }\n    ],"
        new: "    \"SessionStart\": [\n      { \"hooks\": [ { \"type\": \"command\", \"command\": \"uv run guppi event session-start\", \"timeout\": 30 },\n                   { \"type\": \"command\", \"command\": \"uv run guppi render --sync\", \"timeout\": 60 } ] }\n    ],"
    change: guppi render --sync registered as the second SessionStart hook (case 59.7)
  - slug: rule-skill-hi
    replace:
      - old: "Assemble the Frontier from the above and present it as a list: tasks, problems, debt\ncarried over, where the sprint stands; on a plan branch the unfinished plan comes first."
        new: "Assemble the Frontier from the above and present it as a list: tasks, problems, debt\ncarried over, where the sprint stands; on a plan branch the unfinished plan comes first;\nwhat `guppi render --sync` printed at session start is an item when it shows a hand edit."
    change: a hand edit shown by render --sync at session start is a Frontier item (case 59.7)
```

```tasks
- [x] guppi/render.py: `--sync` — for each differing governed file a unified diff (difflib) on stdout, then the write; nothing when identical; a render error on stderr, exit 0
- [x] tests/test_render.py: a differing file, an identical one, a render error
- [ ] the hook registers at the next session's first manual `uv run guppi render` (settings.json is governed); the live reading of estimate-render-sync-reports is taken at the session after that and named in the handoff
```

### Case 59.8 — `CLAUDE.md` is rendered whole from `rule-claude-md`; it leaves the Rule-class files

> **recommend:**
> A MOC `rule-claude-md` under `rule-harness`, `render_mode: full`, `governs:
> CLAUDE.md`, `children: [rule-case-protocol]`. Its Render is today's `CLAUDE.md` verbatim
> — the header, "What is loaded here" with the two `@` imports, "Migration mode" as it
> stands (it leaves with the migration), "Language", "Style", "Commands" — with the Case
> protocol section replaced by the marker line `<!-- rule-case-protocol -->`, which the
> renderer fills. `CLAUDE.md` leaves the Rule-class files: no `file` item, no `claude-md`
> in the Rule-class map; it changes only through an `update` of this page or of
> `rule-case-protocol`. Case 56's hand edit was the last of its kind.

> **given:**
> `CLAUDE.md` is hand-written except the Case protocol section, which `rule-case-protocol`
> (`partial`, parent `rule-plan-mode`) splices between its markers; `guppi render --check`
> names it (the finding of this session).
> **＋** `case-schema.md` lists `CLAUDE.md` among the Rule-class files changed by a `file`
> item; the glossary row "`CLAUDE.md`, `index.md`" calls it the system prompt; `index.md`
> §1's Rule-class table does not list it.
> **＋** `guppi/materialize.py` maps the slug `claude-md` to `CLAUDE.md` in `RULE_CLASS`;
> `decision-case-56` and `decision-case-52` name `claude-md` in their lists.
> **＋** The renderer: a full page's text becomes the whole file; a lone marker line is
> replaced by the child's text, markers kept; a partial whose file a full page owns must be
> in that page's `children`, else an error (`guppi/render.py`).
> **＋** `rule-case-protocol` keeps `parent: rule-plan-mode` and stays in that MOC's
> `children`; it is listed in the `children` of `rule-claude-md` too, for the renderer.
> Lint does not compare `parent` with `children`.
> **＋** The slug `rule-claude-md` names no page.
> **－** The text of `CLAUDE.md` is not changed by this Case; the Case moves it. The
> "Migration mode" section is carried as it is (the owner, 2026-09-12).
> **－** The `@` imports are text to the renderer and to Claude Code alike.

> **when:**
> `guppi render` runs; a Case names `CLAUDE.md`.

> **then:**
> `CLAUDE.md` is written whole from the Render of `rule-claude-md`, the Case protocol
> section from `rule-case-protocol` between its markers; `git diff` after the first such
> render is empty but for the marker lines.
> **＋** A `file` item on `CLAUDE.md` is a finding of `guppi pretask --check` (59.6); the slug
> `claude-md` leaves `RULE_CLASS`; `case-schema.md` and the glossary say `CLAUDE.md` is
> rendered from `rule-claude-md`.
> **＋** `decision-case-52` and `decision-case-56` keep `claude-md` in their lists as
> history; lint treats a slug of no category as outside the vault, as today.
> **＋** The MOC has one Estimate of its own, `estimate-claude-md-rendered`: the file equals
> the Render with the child spliced, the first render diffs by marker lines only, `--check`
> exits 0 (pre-task, case 66: an Estimate has one target).
> **＋** `rule-case-protocol` moves under this page (`parent: rule-claude-md`) and leaves the
> `children` of `rule-plan-mode` (case 66).

> **ratification:**
> Ratified by the owner in chat, 2026-09-12, with the slug renamed from rule-system-prompt.
>
> ```
> - decision[59.8][create][rule-claude-md]{ref:rule-harness}{tags:harness,render}
> - decision[59.8][update][case-schema]{ref:case-schema}
> - decision[59.8][update][glossary]{ref:glossary}
> ```

```then
create:
  - slug: rule-claude-md
    type: rule
    kind: MOC
    enforcement: render
    governs: CLAUDE.md
    render_mode: full
    children: [rule-case-protocol]
    purpose: Prevents the system prompt from holding a line nobody ratified
    estimate:
      slug: estimate-claude-md-rendered
      kind: QA
      criterion: |
        After `uv run guppi render`, `CLAUDE.md` equals the Render of `rule-claude-md` with
        the text of `rule-case-protocol` between its markers; the first such render leaves
        a `git diff` of marker lines only; `guppi render --check` then exits 0; every
        session after it loads the same text, the two `@` imports expanded.
      method: |
        the live reading at the first render after the page exists, by hand, written into
        the estimate line; `tests/test_render.py` already pins a full page with a partial
        child.
    tags: [harness, render]
    sections:
      Purpose: |
        Prevents the system prompt from holding a line nobody ratified. `CLAUDE.md` is the
        one file every session reads first; until this page it was hand-written around one
        rendered section, and a ratified sentence went into the file instead of the page
        (case 56). Now the file is the Render of this page, whole, with the Case protocol
        spliced from `rule-case-protocol`; a change to it is an `update` of one of the two.
      Render: |
        <!-- rule-claude-md -->
        # GUPPI

        A Claude Code harness governed by ratified decisions, and the Obsidian vault it compiles into.
        The vault is `vault/`; its map is `vault/wiki/index.md`. Nothing in the vault or the codebase
        changes without a Decision ratified by the human. You have full autonomy over *how* to
        implement something once its contract is ratified, and none over the contract itself. When you
        are unsure whether something needs ratification: it does.

        ## What is loaded here

        The glossary and the Case schema arrive through the imports below, so the terms and the shape
        of a Case are present from the first turn without a read.

        @vault/wiki/glossary.md

        @vault/wiki/case-schema.md

        `vault/wiki/index.md` is not imported: it is the map of the vault and the rules that hold in
        every phase, read section by section when a section is needed (§0 the one rule, §1 layout,
        §2 Case protocol, §3 decisions, §4 ledger, §5 routing, §6 splitting, §7 estimates, §8 lessons
        and insights, §10 librarian, §11 indexes, §12 where content comes from).

        ## Migration mode, since 2026-09-09

        This repository is being moved from its earlier model onto the one in `index.md`. Until the
        move closes:

        - **The state a session starts from is `vault/wiki/brief.md`.** Read it first; nothing prints
          it yet. `vault/wiki/sprint.md` names the slices and what closes the sprint.
        - **The ledger hook exists since Slice 1.** Lines are emitted in a ```` ```LEDGER ```` block
          in the reply and the `Stop` hook writes them into `vault/raw/<date>/ledger.md`, each
          prefixed with the time of writing. The lines of 2026-09-09 written by hand before it
          carry no time; that is how the two are told apart.
        - **The rituals of the new model exist since Slice 3.** `/retro` (the person), `/handoff` (the
          agent, refused by `guppi gate` while the tree is dirty), then the `librarian-guppi` agent:
          `materialize`, index check, synthesis, `generate`, `cleanup`, brief, commit. Pages are no
          longer written by hand; `brief.md` is written by the librarian. `docs/migration/` still
          holds the drafts of Work Mode and the plan of the move.
        - **Each slice is its own Plan Mode and its own approval.** The approved plan is copied to
          `vault/raw/<date>/spec.md` by the `PostToolUse ExitPlanMode` hook `guppi spec` since
          Slice 2; the Specs of Slices 0–2 were copied by hand.

        <!-- rule-case-protocol -->

        ## Language

        English for everything written into the repository: code, identifiers, comments, pages,
        commit messages, documents. Russian for chat with the owner, and for the plan he reads in
        order to approve it. English technical terms are not transliterated into Cyrillic.

        ## Style

        Keep the facts and remove the sales pitch. Name a real source or remove the claim. Short
        sentences, active voice, a common word over a term. Give the answer first. Say what is done
        and what is not done; never leave the not-done implied.

        ## Commands

        `make help` lists the targets. `make style` must be clean before every commit. Add no new
        dependencies, Python or otherwise.
        <!-- /rule-claude-md -->
      How it works: |
        Rendered in full into `CLAUDE.md`; `rule-case-protocol` splices into its marker. The
        `@` lines are text here and imports for Claude Code. The section "Migration mode"
        is carried from the hand-written file as it stood on 2026-09-12 and leaves with the
        migration, by an `update` of this page. `rule-case-protocol` keeps its parent
        `rule-plan-mode`; it is listed here for the renderer only.
update:
  - file: vault/wiki/case-schema.md
    change: "the Rule-class list in 'The `then` block lives in the Spec' reads `index.md`, `glossary.md`, this file, a schema — `CLAUDE.md` is rendered from `rule-claude-md` and `rule-case-protocol`, and changes by an `update` of one of them"
  - file: vault/wiki/glossary.md
    change: "row '`CLAUDE.md`, `index.md`': `CLAUDE.md` is the Render of `rule-claude-md`, whole, with the Case protocol from `rule-case-protocol`; the `@path` sentence stays; row 'Rule-class files' unchanged"
```

```tasks
- [x] guppi/materialize.py: `claude-md` leaves RULE_CLASS; a test that a file item on CLAUDE.md has no route
- [x] vault/wiki/case-schema.md and vault/wiki/glossary.md by hand
- [ ] after the next session's render: git diff of CLAUDE.md is the marker lines only — named in the handoff as a check for that session
- [ ] take the reading of estimate-claude-md-rendered at the next session's render — named in the handoff
```

## Case 60 — `materialize` reads a sub-case's missing `given` from its parent; the ten pages get theirs

> **context:**
> Sub-cases share what their parent states once. `materialize` inherits `context`,
> `problem` and `recommend` from the parent Case but not `given`; ten decision groups of
> sessions H (52.1–52.4, 53.1–53.4, 55.1, 55.2) carry `incomplete: given`, and their ten
> Decision pages have no `## Given` section, though the parent's `given` sits in the Spec.
> The Retro of session H named it; the brief carries it as observation (b).

> **problem:**
> The rule says a sub-case has "its own `given`, `when`, `then` and `ratification`", and
> practice puts a shared `given` on the parent when it is the same for every child. Either
> the rule bends or the Spec does; and the ten pages need their Given either way.

> **recommend:**
> The rule bends, one section: `given` may be the parent's; `when`, `then` and
> `ratification` stay the sub-case's own. `materialize` reads a sub-case's missing
> `context`, `problem`, `recommend` or `given` from the parent and marks `incomplete` only
> when neither has it. A one-off under this Case inserts `## Given` on the ten pages from
> the parent's `given` in the Spec of its date, with a History line; the yaml groups keep
> their `incomplete: given` marks as history.

> **given:**
> `guppi/materialize.py` (`assemble`): "a sub-case shares context, problem and recommend
> with its parent" — `given` is not in that tuple; `decision_record` marks `incomplete` for
> a missing `given` or `when` when a kind other than `defer` is among the lines.
> **＋** `rule-materialize` (Leaf, `draft`) says one decision entry per Case with
> `case_text`; `estimate-materialize-assembles` (`passed` by the line of 2026-09-11) reads
> "marked incomplete for a missing given or when only when a kind other than defer is among
> its lines".
> **＋** `rule-case-protocol` Render: "A sub-case is `### Case N.M — name` under its parent,
> with its own `given`, `when`, `then` and `ratification`; the sections the children share
> live on the parent." `case-schema.md` says the same under Splitting.
> **＋** No Decision page exists for a parent Case without lines of its own (`decision-case-52`
> does not exist); the parent's `given` is only in `raw/<date>/spec.md`.
> **＋** The ten pages: `decision-case-52.1` … `52.4` (Spec of 2026-09-10), `53.1` … `53.4`,
> `55.1`, `55.2` (Spec of 2026-09-11); each has `## Context`, `## Problem`, `## When`, no
> `## Given`.
> **＋** The yaml is extended, never rewritten: the ten groups are `applied`; `generate`
> skips an existing decision page.
> **－** `when` is never inherited: it is the trigger of the sub-case's own criterion.
> **－** The Spec of this session puts `given` on every sub-case of 59; nothing there to
> inherit.

> **when:**
> `guppi materialize` assembles a sub-case's decision entry; the one-off runs once.

> **then:**
> A sub-case's `context`, `problem`, `recommend` and `given` are its own when present and
> the parent's otherwise; `incomplete` names a section only when neither has it; `when`
> stays the sub-case's own.
> **＋** `rule-case-protocol` and `case-schema.md` say: a sub-case has its own `when`, `then`
> and `ratification`; `given` too, unless it is the parent's word for word.
> **＋** The one-off writes `## Given` before `## When` on the ten pages from the parent's
> `given` in the Spec of the page's date, and appends `- 2026-09-12 Given inherited from the
> parent Case · [[decision-case-60]]` to History; `guppi lint` reports no `## Given` finding
> on them.
> **＋** `estimate-materialize-assembles` carries the clause and goes `pending`; its reading
> is the unit test of this session.

> **ratification:**
> Ratified by the owner in chat, 2026-09-12.
>
> ```
> - decision[60][update][rule-materialize]{ref:rule-materialize}
> - decision[60][update][estimate-materialize-assembles]{ref:estimate-materialize-assembles}
> - decision[60][update][rule-case-protocol]{ref:rule-case-protocol}
> - decision[60][update][case-schema]{ref:case-schema}
> ```

```then
update:
  - slug: rule-materialize
    replace:
      - old: "a Case whose text lacks `given` or `when` is marked `incomplete` only when a kind other than `defer` is among its lines, since the short form of Retro has neither."
        new: "a sub-case's `context`, `problem`, `recommend` and `given` are its own when present and its parent's otherwise, `when` never; a Case whose text lacks `given` or `when`, its parent's included, is marked `incomplete` only when a kind other than `defer` is among its lines, since the short form has neither."
    change: a sub-case inherits a missing given from its parent, as context, problem and recommend; when stays its own (case 60)
  - slug: estimate-materialize-assembles
    replace:
      - old: "is marked incomplete for a missing given or when only when a kind other than defer is among its lines;"
        new: "takes a missing context, problem, recommend or given from its parent Case, never when, and is marked incomplete for a section neither has, or a missing when, only when a kind other than defer is among its lines;"
    set: {status: pending}
    change: the parent's given is inherited by a sub-case; pending for the unit reading (case 60)
  - slug: rule-case-protocol
    replace:
      - old: "A sub-case is\n`### Case N.M — name` under its parent, with its own `given`, `when`, `then` and\n`ratification`; the sections the children share live on the parent."
        new: "A sub-case is\n`### Case N.M — name` under its parent, with its own `when`, `then` and\n`ratification`, and its own `given` unless it is the parent's word for word; the\nsections the children share live on the parent, and `materialize` reads them there."
    change: a sub-case's given may be the parent's; when, then and ratification are its own (case 60)
  - file: vault/wiki/case-schema.md
    change: "under Splitting: a sub-case has its own `when`, `then` and `ratification`, and its own `given` unless it is the parent's; `context`, `problem`, `recommend` and a shared `given` live on the parent, and `materialize` reads a missing one there"
```

```tasks
- [x] guppi/materialize.py: `given` joins the inherited sections; incomplete only when neither has it; a test
- [x] one-off, scratchpad script, not kept: `## Given` before `## When` on the ten pages (52.1–52.4 from raw/2026-09-10/spec.md, 53.1–53.4, 55.1, 55.2 from raw/2026-09-11/spec.md), History line `· [[decision-case-60]]`; guppi lint → no `## Given` finding on them
- [x] vault/wiki/case-schema.md, Splitting, by hand
- [x] take the reading of estimate-materialize-assembles (unit, with 61); write the estimate line
```

## Case 61 — the tag `tests` is registered; a tag a lesson brought is declared at the next Plan Mode

> **context:**
> `guppi generate` reported one line in session H: the tag `tests` is used and not in
> `tags.md`. It came from two ledger lessons of that session and the Insight the librarian
> made over them. A tag enters `tags.md` only through a Case that declares it under
> `new_tags`; a lesson is written by the hook, without a Case, so a tag it brings has no
> way in.

> **problem:**
> `materialize` collects `new_tags` only from the `then` block of a Case that has decision
> lines; a Case whose only content is a tag declaration is never read. So the way in has to
> be a Case with some line, or `materialize` reads every Case block for `new_tags`.

> **recommend:**
> `materialize` reads `new_tags` from every `## Case` block of the Spec, lines or none; the
> declaration is ratified by the Case's heading and block, as any `then` block is. This Case
> declares `tests` and changes `rule-materialize` in one, so it has a line either way.

> **given:**
> `guppi/materialize.py` (`assemble`) walks `by_case`, the Cases that have decision entries,
> and appends each block's `new_tags` to the yaml's top-level list; `generate` registers
> them and reports a tag used without registration on stderr.
> **＋** `tags.md` holds nine tags; `tests` is on `lesson-tests-generate-history-date-unpinned`
> and `insight-tests-clock-not-pinned`; `lesson-tests-cli-date-pinned` carries `harness`
> only.
> **＋** `rule-materialize` says nothing of `new_tags`; `estimate-materialize-assembles` is
> `pending` by case 60 and reads "new_tags are kept" in its unit test only.
> **－** The librarian never invents a tag (`rule-documentation`); it reported and left it.

> **when:**
> `guppi materialize` reads a Spec; `guppi generate` runs after it.

> **then:**
> Every `## Case` and `### Case` block of the Spec contributes its `new_tags`, lines or
> none; duplicates are kept once.
> **＋** `tags.md` gains `tests` — the harness's own test suite, its fixtures and clocks —
> with the alias «тесты»; `generate` prints no tag line at the next librarian run.
> **＋** `rule-materialize` says so; `estimate-materialize-assembles` carries the clause.

> **ratification:**
> Ratified by the owner in chat, 2026-09-12.
>
> ```
> - decision[61][update][rule-materialize]{ref:rule-materialize}
> - decision[61][update][estimate-materialize-assembles]{ref:estimate-materialize-assembles}
> ```

```then
update:
  - slug: rule-materialize
    replace:
      - old: "A line the grammar does not\nparse goes under `unparsed`; the script continues."
        new: "A line the grammar does not\nparse goes under `unparsed`; the script continues. `new_tags` declared in the `then`\nblock of any Case of the Spec, with decision lines or without, go to the yaml's\n`new_tags` once each, so a tag a lesson brought can be declared at the next Plan Mode."
    change: new_tags are collected from every Case block, lines or none (case 61)
  - slug: estimate-materialize-assembles
    replace:
      - old: "An existing yaml gains only the entries of ledger lines it does not hold,"
        new: "The new_tags of a Case with no decision line reach the yaml once. An existing yaml gains only the entries of ledger lines it does not hold,"
    change: new_tags of a line-less Case join the criterion (case 61)
new_tags:
  - tag: tests
    meaning: the harness's own test suite, its fixtures and clocks
    aliases: тесты
```

```tasks
- [x] guppi/materialize.py: new_tags collected from every Case block of the Spec; a test with a line-less Case
- [x] the reading of estimate-materialize-assembles covers this (task of case 60)
```

## Case 62 — `rule-case-protocol`: no picker, a changed Case shown again without `recommend`

> **context:**
> Three habits the owner set in sessions G to I live only in the agent's memory files: the
> owner answers a Case in plain chat and rejected the AskUserQuestion picker twice (session
> G); when the owner changes a Case's conditions or verdict, the Case is shown again with
> the sections that changed and without `recommend`, since the variant is theirs (today,
> Case 58); a Frontier item with no decision in it is one line in the Work Mode order
> (today, `lesson-plan-mode-exited-per-frontier-item`). Memory is for personal notes; a
> rule of the dialogue belongs in the Render every session reads.

> **problem:**
> The Case protocol names the `ratification` section and its ledger preview, and nothing of
> how the sign-off is asked for, nor what happens when the owner answers with a variant.

> **recommend:**
> Two sentences in the Render of `rule-case-protocol` and one row in `case-schema.md`. The
> Frontier habit is already covered by case 59.2 (`work` closes such a line). The three
> memory files are deleted in Work Mode.

> **given:**
> `rule-case-protocol` Render: "The `ratification` section ends with a preview of the ledger
> lines in an untagged fence."; `case-schema.md` row `ratification`: "The human's sign-off,
> question, or their own alternative. Ends with a preview of the ledger lines in an untagged
> fence."
> **＋** The memory files `feedback-no-askuserquestion-in-cases`,
> `feedback-one-plan-per-plan-mode`, `bash-heredoc-escapes-interpreted` and
> `session-f-unmaterialized-tail` sit in the agent's memory directory outside the
> repository; two of them are now lessons in the ledger.
> **－** `recommend` is still required in the first showing of a Case; the schema table is
> not changed on that.

> **when:**
> The agent ends a Case turn; the owner answers with a change.

> **then:**
> The turn ends with the `ratification` section and a plain question in the chat; no picker
> tool.
> **＋** When the owner changes conditions or verdict, the next turn shows the Case again:
> `context` and `problem` if they changed, always `given`, `when`, `then` and
> `ratification`, and no `recommend`.
> **＋** The four memory files and their index lines are deleted; memory holds nothing of the
> project's rules.

> **ratification:**
> Ratified by the owner in chat, 2026-09-12.
>
> ```
> - decision[62][update][rule-case-protocol]{ref:rule-case-protocol}
> - decision[62][update][case-schema]{ref:case-schema}
> ```

```then
update:
  - slug: rule-case-protocol
    replace:
      - old: "The\n`ratification` section ends with a preview of the ledger lines in an untagged\nfence."
        new: "The\n`ratification` section ends with a preview of the ledger lines in an untagged\nfence, and the turn ends with a plain question in the chat, never a picker tool.\nWhen the person answers with a change, show the Case again: `context` and\n`problem` if they changed, always `given`, `when`, `then` and `ratification`, and\nno `recommend` — the variant is theirs."
    change: the sign-off is asked in plain chat; a changed Case is shown again without recommend (case 62)
  - file: vault/wiki/case-schema.md
    change: "row `ratification`: the turn ends with a plain question in the chat, never a picker; a Case the person changed is shown again with `context` and `problem` if changed, `given`, `when`, `then`, `ratification`, and no `recommend`"
```

```tasks
- [x] vault/wiki/case-schema.md row `ratification` by hand
- [x] delete the four memory files and their lines in MEMORY.md
```

## Case 66 — pre-task findings: the pages the Cases forgot

> **context:**
> `/pre-task` sent the list of this Plan Mode's decisions to `ask-guppi` once. It returned
> findings against `rules/schema.md`, `estimates/schema.md`, `index.md` §10 and the
> criteria of five Estimates that quote wording the Cases change (the lesson
> `lesson-estimates-criterion-stale-after-contract-change` names the pattern). Each is
> settled here, as case 57 did, by a line under this Case; the `then` blocks of the Cases
> concerned were corrected in place where no new line was needed.

> **problem:**
> Six findings hold: (1) 59.8 lists `rule-case-protocol` in two MOCs' `children` while
> `parent` is one slug; (2) 59.8 gave the MOC another page's Estimates, and an Estimate has
> one `target`; (3) 59.7 set `enforcement: hook` on a `check` rule that `make lint` and
> `estimate-harness-pipeline` rest on; (4) 59.1 set `implementation_ref` on a `render`
> rule, which the schema forbids; (5) `index.md` §10 still says "not the code" against
> case 58; (6) `rule-harness` says its four children run together in `make lint` and 59.6,
> 59.8 add two that do not; and the criteria of `estimate-retro-loads`,
> `estimate-spec-capture-appends` (`## Retro`) and `estimate-render-harness-reproduces`
> ("no change to `CLAUDE.md`") quote wording 59.5 and 59.8 change. Four findings do not
> hold: `rule-pretask-hook` gates on the `pretask` line and the check is content, not a
> duplicate; `estimate-brief-written`'s clause on `sprint.md` binds the librarian, and 59.5
> has the agent edit it in Work Mode; 59.3 and 62 replace different sentences of the Render;
> the Render of `rule-claude-md` carries the whole present text of `CLAUDE.md` in its block.

> **recommend:**
> Corrected in place (no line): 59.7 keeps `enforcement: check`; 59.1 drops
> `implementation_ref` from `rule-pretask`; 59.8's MOC gets its own nested Estimate
> `estimate-claude-md-rendered`. Lines under this Case: `rule-case-protocol` parent →
> `rule-claude-md` and out of `rule-plan-mode`'s children; `rule-pretask-hook` names the
> `--check` command its module serves the skill with; `index.md` §10; `rule-harness`
> Purpose; the three stale criteria.

> **given:**
> `rules/schema.md`: `parent` is one slug; `implementation_ref` and `## Implementation` for
> `hook` and `check` only; a MOC's `estimates` are cross-cutting. `estimates/schema.md`:
> one `target`.
> **＋** `rule-plan-mode` `children: [rule-case-protocol, rule-ask, rule-pretask-hook,
> rule-pretask, rule-spec-capture]`; `rule-case-protocol` `parent: rule-plan-mode`.
> **＋** `rule-pretask-hook` (`hook`, `guppi/pretask.py`, `.claude/settings.json`) gates
> `ExitPlanMode` on the `pretask` line.
> **＋** `rule-harness` Purpose: "Four rules belong to no phase of the session: the renderer,
> the hook registry, lint and the indexes. They run together in `make lint`…";
> `estimate-harness-pipeline` reads `make lint`'s three commands in order — unchanged.
> **＋** `index.md` §10: "Not `ledger.md`, not `spec.md`, not `plan.md`, not
> `wiki/decisions/`, not the archive, not the code".
> **＋** `estimate-retro-loads` (pending): "a short defer with its Case under ## Retro in
> spec.md"; `estimate-spec-capture-appends` (pending): "A `## Retro` section appended by
> the agent stays intact"; `estimate-render-harness-reproduces` (passed): "no change to
> `CLAUDE.md`".

> **when:**
> The librarian generates the pages of this session; the next session renders and reads.

> **then:**
> `rule-case-protocol` has `parent: rule-claude-md` and sits in that MOC's `children` only;
> `rule-plan-mode` lists four children.
> **＋** `rule-pretask-hook` says its module also serves `/pre-task` with `guppi pretask
> --check <plan>`.
> **＋** `index.md` §10 reads: the Makefile, `guppi/` and `tests/` may be read; the ban keeps
> the session artifacts, the archive and the wiki beyond the four reasons.
> **＋** `rule-harness` Purpose names six children: the four of `make lint` in their order,
> the guard hook and the `CLAUDE.md` page, which run in no pipeline.
> **＋** The three criteria say `## Deferred` and "`CLAUDE.md` differs by its marker lines
> only after the first render"; `estimate-render-harness-reproduces` goes `pending` for the
> next session's render.

> **ratification:**
> Ratified by the owner in chat, 2026-09-12.
>
> ```
> - decision[66][update][rule-case-protocol]{ref:rule-case-protocol}
> - decision[66][update][rule-plan-mode]{ref:rule-plan-mode}
> - decision[66][update][rule-pretask-hook]{ref:rule-pretask-hook}
> - decision[66][update][index]{ref:index}
> - decision[66][update][rule-harness]{ref:rule-harness}
> - decision[66][update][estimate-retro-loads]{ref:estimate-retro-loads}
> - decision[66][update][estimate-spec-capture-appends]{ref:estimate-spec-capture-appends}
> - decision[66][update][estimate-render-harness-reproduces]{ref:estimate-render-harness-reproduces}
> ```

```then
update:
  - slug: rule-case-protocol
    set: {parent: rule-claude-md}
    sections:
      Parent: |
        - [[rule-claude-md]]
    change: parent is rule-claude-md, the page CLAUDE.md is rendered from (case 66)
  - slug: rule-plan-mode
    set: {children: [rule-ask, rule-pretask-hook, rule-pretask, rule-spec-capture]}
    sections:
      Children: |
        1. [[rule-ask]]
        2. [[rule-pretask-hook]]
        3. [[rule-pretask]]
        4. [[rule-spec-capture]]
    change: rule-case-protocol moved under rule-claude-md (case 66)
  - slug: rule-pretask-hook
    replace:
      - old: "ordinary session, one without `/hi`, is not gated: no governance applies there."
        new: "ordinary session, one without `/hi`, is not gated: no governance applies there. The\nsame module serves the skill: `uv run guppi pretask --check <plan>` compares the plan\nwith the session's ledger lines and frontier (cases 59.1–59.3, 59.6); `/pre-task` runs\nit, the hook does not."
    change: guppi pretask --check lives here and serves /pre-task (case 66)
  - file: vault/wiki/index.md
    change: "§10 Reads: 'not the code' replaced — the Makefile, guppi/ and tests/ are the scripts' own files and may be read; not ledger.md, spec.md, plan.md, wiki/decisions/, the archive, nor a wiki page beyond the four reasons (case 58)"
  - slug: rule-harness
    replace:
      - old: "them. Four rules belong to no phase of the session: the renderer, the hook\nregistry, lint and the indexes. They run together in `make lint`, in this order, and\nthe order is the content: the harness files are checked against their pages before\nthe indexes, the indexes before the pages."
        new: "them. Four rules belong to no phase of the session: the renderer, the hook\nregistry, lint and the indexes. They run together in `make lint`, in this order, and\nthe order is the content: the harness files are checked against their pages before\nthe indexes, the indexes before the pages. Two more belong here and run in no\npipeline: the hook that refuses a hand edit of a rendered file, and the page\n`CLAUDE.md` is rendered from (cases 59.6, 59.8)."
    change: two children outside the make lint pipeline — the guard hook and the CLAUDE.md page (case 66)
  - slug: estimate-retro-loads
    replace:
      - old: "a short defer with its Case under ## Retro in"
        new: "a short defer with its Case under ## Deferred in"
    change: the Deferred heading (cases 59.5, 66)
  - slug: estimate-spec-capture-appends
    replace:
      - old: "A `## Retro` section appended by the agent stays intact under a later approval's separator"
        new: "A `## Deferred` section appended by the agent stays intact under a later approval's separator"
    change: the Deferred heading (cases 59.5, 66)
  - slug: estimate-render-harness-reproduces
    replace:
      - old: "dropped marker lines of `.claude/skills/hi/SKILL.md` and no change to `CLAUDE.md`, and"
        new: "dropped marker lines of `.claude/skills/hi/SKILL.md`; after `rule-claude-md` exists, the\nfirst render changes `CLAUDE.md` by its marker lines only (case 59.8); and"
    set: {status: pending}
    change: CLAUDE.md is a full render target; pending for the next session's render (cases 59.8, 66)
```

```tasks
- [x] vault/wiki/index.md §10 by hand
- [ ] the reading of estimate-render-harness-reproduces at the next session's render — named in the handoff
```

## Deferred

The decisions left open when the owner closed Plan Mode on 2026-09-12, one Case each
(case 59.5). Retro appends its own under this heading.

## Case 63 — Slice 3c, the raw lifecycle, deferred again

> **context:**
> Case 45 (2026-09-10) deferred `rule-ledger-tail`: the ledger lines written after the
> librarian's commit — readings, lessons — reach the next session's Frontier only two
> sessions later, because `/hi` reads `brief.md` alone. Slice 3c grew around it in
> `sprint.md`: `decided_by` on pages born of a Case, `origin` as a ledger pointer,
> `raw/<date>/` of a fully applied date archived by run stamp with its paths rewritten, a
> fresh ledger as the tail `/hi` prints, lint on both fields, the pages migrated by script.
> Session I spent its Plan Mode on the artifacts of Plan Mode itself (case 59); the render
> at session start (59.7) and the Frontier file (59.2) take part of the ground.

> **problem:**
> The tail of session H reached this session through the agent's memory file, not the
> harness; the memory is deleted by case 62. Until Slice 3c, `/hi` still shows nothing of
> what was written after the librarian's commit. Postponed three times now.

```then
defer:
  - slug: rule-ledger-tail
    type: rule
    purpose: Shows at /hi every ledger line that no vault page holds yet, so a reading or a lesson written after the librarian's commit reaches the next session's Frontier
```

> **ratification:**
> Deferred by the owner in chat, 2026-09-12.
>
> ```
> - decision[63][defer][rule-ledger-tail]{ref:rule-ledger-tail}{supersedes:case 45}
> ```

## Case 64 — Slice 3b, Work Mode, deferred again

> **context:**
> Case 29 (2026-09-10) deferred `rule-work-mode` and `rule-subagent-guppi` together: Work
> Mode as ratified rules — the plan, the branch and baseline, the subagent that executes
> and never decides, the four hooks of the draft in `docs/migration/rule-work-mode.md`.
> Since then case 59.3 dropped the separate executable plan (`plan.md`,
> `to-executable-plan`): the `tasks` blocks of the Spec are what a subagent executes. The
> owner's clause of case 59 belongs here: a fork in Work Mode is not a return to Plan
> Mode — the subagent stops, the fork is written as a short-form Case under `## Deferred`,
> shown at Retro, worked next session.

> **problem:**
> Work Mode runs on the draft and on habit; `rule-work-mode` and `rule-subagent-guppi` are
> placeholders and lint orphans. The draft has to be reconciled with 59.3 and the fork
> clause before its Cases are formed. Postponed four times now.

```then
defer:
  - slug: rule-work-mode
    type: rule
    purpose: Prevents implementation starting before the plan, branch and baseline exist
  - slug: rule-subagent-guppi
    type: rule
    purpose: Prevents implementation drifting from the ratified plan while it is being executed
```

> **ratification:**
> Deferred by the owner in chat, 2026-09-12.
>
> ```
> - decision[64][defer][rule-work-mode]{ref:rule-work-mode}{supersedes:case 29}
> - decision[64][defer][rule-subagent-guppi]{ref:rule-subagent-guppi}{supersedes:case 29}
> ```

## Case 65 — `ask-guppi` and the archive, deferred

> **context:**
> Case 31 (2026-09-10) discussed and did not decide: `ask-guppi` answers from the four
> indexes, which list live pages only; a slug named in a question that was archived is
> reported as missing. `vault/archived/migration/2026-09-11/estimates/` holds 21 pages
> since the librarian's run of session H, and `guppi cleanup` brings a page back on an
> `update` of `status`.

> **problem:**
> A Case may propose a `create` of a slug the archive already holds, and pre-task passes
> it. The fix is small — a named slug checked against `vault/archived/` — but it is an
> `update` of `rule-ask` with its Estimate, and no session has reached it. Postponed four
> times now.

```then
defer:
  - slug: rule-ask
    type: rule
    purpose: Prevents a create from being proposed without the vault having been asked whether it already holds the thing, or forbids it
```

> **ratification:**
> Deferred by the owner in chat, 2026-09-12.
>
> ```
> - decision[65][defer][rule-ask]{ref:rule-ask}
> ```

## Case 58 — the librarian may read the repository's own files; only the vault is rationed

Owner's variant, 2026-09-12: keep `make lint` and the Makefile; the frame's ban exists to
stop the librarian from opening wiki pages at will, since there are many and each costs
context. The scripts' own files, the Makefile and the tests are not that problem.

> **context:**
> Slice 3 closes when `estimate-documentation-completes` passes. It failed three times,
> each time on a read outside the librarian's frame. In session H the one read was the
> Makefile: `make lint` stopped at its first step (`render --check` red), the brief needs
> the lint output, and the agent opened the Makefile to learn the three steps and run them
> apart.

> **problem:**
> The frame's ban on reads names the wrong set. Its purpose is to keep the librarian out of
> the wiki, where a page opened at will costs context and there are many. It also names
> `guppi/` and `tests/`, and the criterion counts the Makefile as a read outside the frame.
> The scripts' own files are not the problem the ban solves, and the reading fails on them.

> **given:**
> `rule-documentation` (MOC, `draft`, Render is the librarian's frame) says: "Never read
> `ledger.md`, `spec.md`, `plan.md`, `wiki/decisions/`, `vault/archived/`, or any file under
> `guppi/` or `tests/`: what the scripts do with the yaml is written here."
> **＋** `estimate-documentation-completes` (`pending` on the page, `failed` by the ledger
> line of 2026-09-11 12:24:05, applied at the next materialize before this Case) says in its
> Criterion "and no ledger, Spec, plan, Decision page, archive file, or file under guppi/ or
> tests/".
> **＋** The librarian's run of session H (event log 12:10–12:21) read the Makefile once and
> no other file outside the frame; every other clause of the criterion passed, as the
> `failed` line records.
> **＋** `rule-brief` keeps `make lint`; its Render and `estimate-brief-written` are not
> changed.
> **－** The ban on the session artifacts and the vault stays: `ledger.md`, `spec.md`,
> `plan.md`, `wiki/decisions/`, `vault/archived/`, and wiki pages beyond the four reasons.

> **when:**
> The librarian runs, and the reading of `estimate-documentation-completes` is taken against
> its event log.

> **then:**
> A read of the `Makefile`, of a file under `guppi/` or under `tests/` is not a finding.
> **＋** A read of `ledger.md`, `spec.md`, `plan.md`, a Decision page, an archive file, or a
> wiki page without one of the four reasons named in the report, still fails the reading.
> **＋** `estimate-documentation-completes` is set `pending` by this Case; the run of session
> H is then read again against the new criterion from its event log, in Work Mode, and the
> result written as an estimate line. If it passes, Slice 3 closes in `sprint.md` in this
> session.

> **ratification:**
> Ratified by the owner in chat, 2026-09-12, in their own variant.
>
> ```
> - decision[58][update][rule-documentation]{ref:rule-documentation}
> - decision[58][update][estimate-documentation-completes]{ref:estimate-documentation-completes}
> ```

```then
update:
  - slug: rule-documentation
    replace:
      - old: "Never read `ledger.md`, `spec.md`, `plan.md`, `wiki/decisions/`,\n`vault/archived/`, or any file under `guppi/` or `tests/`: what the scripts do with\nthe yaml is written here."
        new: "Never read `ledger.md`, `spec.md`, `plan.md`, `wiki/decisions/` or\n`vault/archived/`: what the scripts do with the yaml is written here. The `Makefile`,\n`guppi/` and `tests/` are the scripts' own files, not the vault; read them when a\ncommand's output is not enough."
    change: the Makefile, guppi/ and tests/ may be read; the ban keeps the session artifacts and the wiki beyond the four reasons
  - slug: estimate-documentation-completes
    replace:
      - old: "and the outcome, and no ledger, Spec, plan, Decision page, archive file, or file under guppi/\nor tests/;"
        new: "and the outcome, and no ledger, Spec, plan, Decision page or archive file (the Makefile,\nguppi/ and tests/ are the scripts' own and may be read);"
    set: {status: pending}
    change: the Makefile, guppi/ and tests/ leave the forbidden set; pending for the reading against the new criterion (case 58)
```

```tasks
- [x] take the reading of estimate-documentation-completes: the librarian run of session H (raw/2026-09-11/event_log.md 12:10–12:21, the report in the ledger line of 12:24:05) against the new criterion; write the estimate line
- [x] if it passes: vault/wiki/sprint.md — Slice 3 closed 2026-09-12, one line
```

## Case 67 — the ledger line grammar shown as it is written

> **context:**
> Every decision line of session I up to 10:09 was written `decision[58][update][slug]`;
> `materialize.parse_line` reads `decision[case 58][update][slug]` only. The agent took the
> placeholder `decision[case_id][kind][slug]` of the table "What a Case produces" in
> `case-schema.md` literally, and the Render of `rule-case-protocol` shows the line only as
> `- decision[...]`. The lines were written again in the right form; the 33 wrong ones stay
> (`lesson-ledger-decision-line-written-without-the-case-word`).

> **problem:**
> Nothing the agent reads at session start shows a decision line as the ledger holds it.
> The table of `case-schema.md` and the ledger paragraph of `rule-case-protocol` should show
> `- decision[case N][kind][slug]{ref:…}{tags:…}` with a real number, as every earlier
> ledger writes it. An `update` of both; the next Plan Mode.

```then
defer:
  - slug: rule-case-protocol
    type: rule
    purpose: Prevents a decision from being acted on before it is ratified, or ratified without its content in view
```

## Case 68 — `rule-pretask`: a Case with work, not a Case with lines

> **context:**
> Case 59.3 says `guppi pretask --check` reports "a Case that has decision lines and no
> `tasks` block". At the first live run the three deferred decisions of the session (Cases
> 63–65) were reported: a defer has lines and no work, so no `tasks` block. The code exempts
> a Case whose lines are all `defer` (commit 2b7dd42); the ratified wording does not.

> **problem:**
> The Render of `rule-pretask` and the criterion of `estimate-pretask-reconciles` will be
> generated from the wording of 59.3 and say "a Case with decision lines". One word: "a Case
> with a line other than `defer`". An `update` of both; the next Plan Mode.

```then
defer:
  - slug: rule-pretask
    type: rule
    purpose: Prevents a set of ratified decisions from reaching the Spec with a contradiction between them or with the vault
```

## Case 69 — `guppi materialize` needs a mode that shows and does not write

> **context:**
> In Work Mode the agent ran `uv run guppi materialize --date 2026-09-12` to see how the
> day's ledger lines would parse. The command has one mode: it wrote
> `raw/2026-09-12/materialize.yaml`, the librarian's artifact, which the agent deleted at
> once. Nothing was committed.

> **problem:**
> The only way to see what the ledger and the Spec will become is to write the yaml. A
> `--check` or `--show` mode — the entries, the unparsed lines and the incomplete marks on
> stdout, nothing written — would let the agent and pre-task look before the librarian
> runs. An `update` of `rule-materialize` with its Estimate; the next Plan Mode (the owner,
> 2026-09-12).

```then
defer:
  - slug: rule-materialize
    type: rule
    purpose: Prevents the librarian from reading the ledger and the Spec itself, or from routing a decision by guesswork
```
