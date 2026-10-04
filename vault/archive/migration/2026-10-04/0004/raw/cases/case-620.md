## Case 620 — A line put off by the conserved Spec it runs

> **context:**
> At `/hi` the person can take a conserved Spec: a plan that an earlier session ratified and saved with `/carry`, which this session runs whole by `/box`. `rule-skill-hi` then lets the agent ratify no Case but a short-form defer, and it must close each other open line under `## Cases` of `frontier.md` as put off. There are three marks for that: `[-] … · backlog · kept`, `[-] … · sprint · defer` and `[-] … · defer case N`. The third mark is checked by `check_frontier` of `guppi/prespec.py`. It looks for a `defer` item under Case N only in the plan of the current session. A session that runs a conserved Spec has a plan with one title line only. In session 1416 the Frontier line C4, the failed reading of `estimate-handoff-holds-each-fact-once`, came from the ledger Tail. Case 618 of the conserved Spec of 1341, which the session ran, already put off that Estimate. The agent closed the line `[-] … · ledger · defer case 618`, and `uv run guppi prespec --check` refused it with "frontier: C4 defers to case 618, no defer item under Case 618". The agent then closed the line `[x] … · ledger · work`, which `estimate-hi-takes-a-conserved-spec` does not allow, so that reading failed (1416 L8). The lesson `lesson-session-ledger-item-deferred-by-the-conserved-spec-closed-as-work` records it. The librarian grouped it with an older lesson into `insight-session-frontier-no-closer-for-an-item-ended-outside-the-plan`, which stands `open`.
>
> This Case keeps the mark `defer case N` and lets N be a Case of the conserved Spec that the title line of the plan names. Case 620.1 writes that into `rule-skill-hi` and replaces the Criterion of `estimate-hi-takes-a-conserved-spec`. It also names the close in `rule-orchestration`, in its list of the lines a reply closes with no ratification and no defer. Case 620.2 makes `guppi prespec` accept the mark. It finds the conserved Spec by `conserved_spec_named` of `guppi/box.py`, the function that `guppi/spec.py` already uses to read the same title line, so the judgment lives in one place. Case 620.1 also sets the insight `actioned`. The older lesson of that insight, an agenda item left on the sprint page, already has the mark `[-] … · sprint · defer` (cases 310.5, 356.2). By the cascade of `guppi generate` that `estimate-generate-cascades` checks, each `clustered` child of an `actioned` Insight becomes `archived` with History `archived · insight actioned`. So at the librarian's run both lessons of the insight are archived: `lesson-session-ledger-item-deferred-by-the-conserved-spec-closed-as-work` and `lesson-frontier-has-no-closer-for-a-milestone-item-left-on-the-sprint-page`. The insight stays live and reopens on a recurrence (`rule-insights-schema`). The Criterion of `estimate-generate-cascades` describes exactly this, so it stands. The lesson of 1416 is from another session, so no decision line carries `{addresses:...}` for it (case 284.2). This Case closes the brief item that names the cause (C3 of this session's Frontier) and the failed reading (C5). It adds no stop for a line that fits no mark (Q4).
>
> The frame. The only hook on `PreToolUse` `ExitPlanMode` in `.claude/settings.json` is `uv run guppi prespec`, and its rule is `rule-prespec-hook`. The code of `guppi prespec` changes in Work Mode and runs from the working tree at once. The text of `rule-skill-hi` reaches `.claude/skills/hi/SKILL.md` at the render. In between, the check accepts one more form and refuses nothing it accepted before, so no old form is kept. `conserved_spec_named` needs the folder to hold `carry.md`. `/box` deletes that file, but only after the exit from Plan Mode, which is when the check runs. The two sub-cases name the same marks from two sides: the agent that writes a line, and the check that reads it. Their `then` lines therefore share words, but they make two separate promises. Case 619, the only other Case of this session, touches none of these pages.
>
> The moment is a reply in Plan Mode that closes a Frontier line. The Grep `no ratification and no defer` over `vault/wiki/` printed 6 files: `orchestration.md`, `log.md`, `rule-case-protocol`, `rule-orchestration`, `estimate-orchestration-shows-the-frontier-after-a-closed-line` and `decision-case-547`. The hit in `rule-case-protocol` stands in History, and those in `log.md` and the Decision page were not read. The Render of `rule-orchestration` (rendered as `orchestration.md`) sets how a reply ends when it closes a line with no ratification and no defer. Its list of such closes names `sprint · defer` and `backlog · kept` but not a `defer case N` that a Case of the conserved Spec carries, so 620.1 adds that close to the list. The Criterion of `estimate-orchestration-shows-the-frontier-after-a-closed-line` gives its list as examples, and the reply that takes a conserved Spec ends as it says: the Frontier, then `/pre-spec`. So it stands. The short-form section of `rule-orchestration` describes the reply that carries a short-form defer the person asks for, with its line closed `[-] … · defer case N`. It does not say that every such close has a short Case of its own session, so it stays true. Its sentence giving `[-] … · defer case N` to a decision of any other source that is put off also stays true.
>
> Searches. The Grep `defer case` over `vault/wiki/` printed 42 files: `brief.md`, `orchestration.md`, `log.md`, the two lessons, the insight, `rule-skill-hi`, `rule-case-protocol`, `rule-prespec`, `rule-orchestration`, `estimate-hi-takes-a-conserved-spec`, `estimate-hi-writes-frontier`, `estimate-prespec-checks-the-frontier`, `estimate-orchestration-defers-in-one-reply`, `estimate-orchestration-acknowledging-reply`, and 27 Decision pages, which were not read. The hits in `rule-case-protocol` and `rule-prespec` stand in History and were not read. `rule-skill-hi` holds four hits on three lines. Two hits are on the Render line: one is the close this Case extends, and the other says a sprint item never closes `· defer case N`, which stays true. The other two lines are History. The hits in `brief.md` and `log.md` were not read. The Grep `defer case` over `.claude/` printed only `.claude/skills/hi/SKILL.md`, the render of `rule-skill-hi`. The Grep `runs the conserved Spec` over the repository outside `vault/raw/` printed `.claude/skills/hi/SKILL.md`, `tests/test_spec.py`, `tests/test_box.py`, `estimate-hi-takes-a-conserved-spec`, `rule-skill-hi` and files under `vault/archive/`, which were not read. The title line does not change. The Grep `conserved` over `guppi/` printed `backlog.py`, `box.py`, `materialize.py` and `spec.py`.
>
> Done means the following. Case 620.1 replaces the Criterion of `estimate-hi-takes-a-conserved-spec`. Its `purpose` and `method` still describe what it checks, so they stand. Case 620.2 replaces the Criterion of `estimate-prespec-checks-the-frontier`. Its `purpose` (a closer that agrees with its source) and its `method` (`uv run pytest tests/test_prespec.py`) stand. The Criterion of `estimate-hi-writes-frontier` says that a decision of any other source that is put off closes `[-] … · defer case N`. It does not say who holds Case N, so it stands. The Criteria of `estimate-orchestration-acknowledging-reply` and `estimate-orchestration-defers-in-one-reply` list the same marks, which do not change, so they stand.

> **problem:**
> A session that runs a conserved Spec has no valid mark for a Frontier line whose target that Spec already puts off. `rule-skill-hi` gives `defer case N`, but `guppi prespec` looks for Case N only in the session's own plan, which holds no Case. So the agent closed the line `work` by its own judgment, and `estimate-hi-takes-a-conserved-spec` failed.

> **recommend:**
> - **Fix the failed check together with its cause, or on its own?**
>   - Recommended: (a) one Case for both items. The check failed only because the rule has no mark for this line, so it cannot pass until the rule changes.
>   - Answer: (a) one Case for both items.
> - **Which mark closes a line whose put-off is already in the saved plan?**
>   - Recommended: (a) keep `defer case N` and let N point into the conserved Spec that the plan's title line names. `guppi prespec` looks there through the function `/box` already uses.
>   - Answer: Agreed with the recommendation.
> - **Does this Case also close the pattern that groups the two lessons?**
>   - Recommended: (a) mark the insight `actioned` and addressed by this Case, since both of its cases then have a mark.
>   - Answer: Agreed with the recommendation.
> - **Should the agent also stop when a line fits no mark?**
>   - Recommended: (b) leave the stop out of this Case. Every known case has a mark, and a recurrence reopens the insight.
>   - Answer: Agreed with the recommendation.

### Case 620.1 — `/hi` closes a line that the conserved Spec puts off by that Spec's Case

> **given:**
> `rule-skill-hi` — its Render lists the closers of a Frontier line and how a conserved Spec is taken
> **＋** `.claude/skills/hi/SKILL.md` — the skill rendered from `rule-skill-hi`
> **＋** `rule-orchestration` — its Render lists the lines a reply closes with no ratification and no defer
> **＋** `vault/wiki/orchestration.md` — the file rendered from `rule-orchestration`
> **＋** `raw/<date>/<hi HHMM>/frontier.md` — the Frontier whose lines the agent closes
> **＋** `# Session <hi HHMM> — runs the conserved Spec vault/raw/<date>/<HHMM>/spec.md` — the title line of the plan file of a session that runs a conserved Spec
> **＋** `vault/wiki/backlog.md` — names the `spec.md` of each conserved Spec
> **＋** `rule-spec-box` — `/box` runs the conserved Spec
> **＋** `rule-prespec` — `/pre-spec` checks the plan and the Frontier
> **＋** `estimate-hi-takes-a-conserved-spec` — the check whose Criterion this sub-case replaces
> **＋** `insight-session-frontier-no-closer-for-an-item-ended-outside-the-plan` — the pattern this sub-case marks addressed

> **when:**
> In a session that `/hi` opened from `.claude/skills/hi/SKILL.md` as rendered from `rule-skill-hi`, the person takes a conserved Spec of `## Cases` of `raw/<date>/<hi HHMM>/frontier.md`.

> **then:**
> The agent takes the Spec whole, to be run by `/box`, only while the session's ledger holds no decision line other than a `defer`, and after it ratifies no Case but a short-form defer.
> **＋** It closes the line of that Spec `[x] … · work`.
> **＋** It creates the plan file with one title line, `# Session <hi HHMM> — runs the conserved Spec vault/raw/<date>/<HHMM>/spec.md`, the path that `vault/wiki/backlog.md` names for that Spec.
> **＋** It closes each other open line under `## Cases` as left — `[-] … · backlog · kept`, `[-] … · sprint · defer` or `[-] … · defer case N` — and goes on to `/pre-spec`.
> **＋** A line whose target a `defer` item of that Spec puts off closes `[-] … · defer case N`, N being the Case of that Spec that holds the item, and the session writes no short-form Case and no ledger line for it.
> **－** No other line under `## Cases` of `raw/<date>/<hi HHMM>/frontier.md` closes `[x]`.
> **－** No Case of the conserved Spec is built again or ratified again in this session.
> **－** `.claude/skills/hi/SKILL.md` equals the Render of `rule-skill-hi` and is not edited by hand.

> **tasks:**
> - [ ] update `rule-skill-hi`
>   - old: `` a short-form Case and its ledger line, and its target enters `backlog.md` through `deferred_by` (case 451.1); ``
>   - new: `` a short-form Case and its ledger line, and its target enters `backlog.md` through `deferred_by` (case 451.1), or a Case of the conserved Spec the session takes, as below (case 620.1); ``
>   - old: `` close the other open lines under `## Cases` as left, and go on to `/pre-spec`. ``
>   - new: `` close the other open lines under `## Cases` as left — a line whose target a `defer` item of that Spec puts off closes `[-] … · defer case N`, N being the Case of that Spec that holds the item, with no short-form Case and no ledger line of this session (case 620.1) — and go on to `/pre-spec`. ``
>   - change: `a line whose target a defer item of the conserved Spec puts off closes defer case N with that Spec's Case (case 620.1)`
> - [ ] update `rule-orchestration`
>   - old: `` an item closed `[-] … · sprint · defer` or `[-] … · backlog · kept` — ``
>   - new: `` an item closed `[-] … · sprint · defer` or `[-] … · backlog · kept`, a line closed `[-] … · defer case N` by a Case of the conserved Spec the session takes (case 620.1) — ``
>   - change: `a line closed defer case N by a Case of the conserved Spec is a close with no ratification and no defer (case 620.1)`
> - [ ] update `estimate-hi-takes-a-conserved-spec`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a line put off by a defer of the conserved Spec closes defer case N with that Spec's Case`
> - [ ] update `insight-session-frontier-no-closer-for-an-item-ended-outside-the-plan`
>   - set: `{status: actioned, addressed_by: decision-case-620.1}`
>   - change: `actioned: a line put off by a defer of the conserved Spec closes defer case N, and a sprint item left closes sprint defer (cases 356.2, 620.1)`
> - [ ] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
> - [ ] `uv run guppi render`: `vault/wiki/orchestration.md`
> - [ ] read `estimate-hi-takes-a-conserved-spec`

> **ratification:**
> ```
> - decision[case 620.1][update][rule-skill-hi]{ref:rule-skill-hi}
> - decision[case 620.1][update][rule-orchestration]{ref:rule-orchestration}
> - decision[case 620.1][update][estimate-hi-takes-a-conserved-spec]{ref:estimate-hi-takes-a-conserved-spec}
> - decision[case 620.1][update][insight-session-frontier-no-closer-for-an-item-ended-outside-the-plan]{ref:insight-session-frontier-no-closer-for-an-item-ended-outside-the-plan}
> ```

### Case 620.2 — `guppi prespec` finds Case N in the conserved Spec the plan names

> **given:**
> `guppi/prespec.py` — `check_frontier` judges the closers of the Frontier
> **＋** `guppi/box.py` — `conserved_spec_named` finds the conserved Spec that the title line of a plan names
> **＋** `tests/test_prespec.py` — the tests of the Frontier check
> **＋** `rule-prespec` — `/pre-spec` runs `uv run guppi prespec --check`, and its docstring says what the check compares
> **＋** `rule-prespec-hook` — the `PreToolUse` hook on `ExitPlanMode` runs the same judgment
> **＋** `vault/raw/<date>/<HHMM>/frontier.md` — the Frontier of the session that the check reads
> **＋** `vault/raw/<date>/<HHMM>/spec.md` — the Spec of a conserved Spec, a folder that holds `carry.md`
> **＋** `estimate-prespec-checks-the-frontier` — the check whose Criterion this sub-case replaces

> **when:**
> `uv run guppi prespec --check <plan>` reads the session's `vault/raw/<date>/<HHMM>/frontier.md`, and the title line of `<plan>` may name the `vault/raw/<date>/<HHMM>/spec.md` of a folder that holds `carry.md`.

> **then:**
> A missing file is the finding `frontier: <path> is missing`.
> **＋** An open line under `## Cases` is a finding. An open line under `## Work` or `## Ask` is not.
> **＋** A closed line whose last segment after ` · ` is none of `case N`, `work`, `defer`, `kept` and `defer case N` is a finding.
> **＋** These pairings of box and closer are findings: `[x]` with `defer`, `kept` or `defer case N`, and `[-]` with `case N` or `work`.
> **＋** `defer` is clean only after the source segment `sprint`, the segment before the closer. `kept` is clean only after the source `backlog`. After any other source, each one is a finding.
> **＋** `defer case N` after the source `sprint` or `backlog` is a finding. After another source, it is a finding when there is no `defer` item under Case N in the plan, and none under Case N of the `vault/raw/<date>/<HHMM>/spec.md` that the title line of the plan names.
> **＋** A line closed `case N` is a finding when the plan has no heading of Case N.
> **－** A title line that names no folder holding `carry.md` adds no Case: `defer case N` is then judged against the plan alone.
> **－** A line that is not a box line, such as `Backlog: N items` or an indented `- near` line, is not read. No line of another session's Frontier file is read.

> **tasks:**
> - [ ] update `rule-prespec`
>   - change: `the Frontier check takes defer case N from a defer Case of the conserved Spec that the plan's title line names (case 620.2)`
> - [ ] update `estimate-prespec-checks-the-frontier`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — defer case N is found in the plan or in the conserved Spec its title line names`
> - [ ] `guppi/prespec.py`: when Case N has no `defer` item in the plan, `check_frontier` reads the `defer` items of the conserved Spec that `conserved_spec_named` of `guppi/box.py` finds in the plan's title line, by `split_cases` and `then_blocks` of `guppi/materialize.py`; the module docstring and the docstring of `check_frontier` say so
> - [ ] `tests/test_prespec.py`: a `defer case N` line is clean when N holds a `defer` item in the conserved Spec that the title line names; it is a finding when that Case holds no `defer` item; it is a finding when the named folder holds no `carry.md`
> - [ ] `make test`
> - [ ] read `estimate-prespec-checks-the-frontier`

> **ratification:**
> ```
> - decision[case 620.2][update][rule-prespec]{ref:rule-prespec}
> - decision[case 620.2][update][estimate-prespec-checks-the-frontier]{ref:estimate-prespec-checks-the-frontier}
> ```
