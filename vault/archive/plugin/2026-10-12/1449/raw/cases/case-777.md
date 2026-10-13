## Case 777 — The opening of the next sprint is checked without a transcript

> **context:**
> `estimate-sprint-close-next-session-opens-the-sprint` checks what happens after a sprint closes: the brief opens the next sprint, `/hi` starts `/sprint-open`, `guppi ledger` refuses decision lines until a sprint page is created, and the pages written that session carry the new sprint id. Its Criterion says that someone reads the refusals of `uv run guppi ledger` in the transcript of the session after the close, but its `method` reads no transcript: case 769.5 left the method without one and copied the old `When` unchanged (handoff of session 2350, For the next session). A method may not wait for a later session (case 670.4), so that reading can never run; the refusals stay checked by the second `When` line, the tests over a made-up vault. The person chose to drop only the transcript words from the `When`; the `Then` stands word for word. A Criterion replaced whole sets the page `pending`, and its `method` names the Retro of the session of case 769, which is past, so the method is set anew to run at the Retro of this session: the two test files, and by hand the live skill files of `/hi` and `/sprint-open` and the step of `.claude/agents/librarian-guppi.md` that writes the first line of the brief, read against the Criterion. The method names that step as the Render of `rule-brief`, which governs `.claude/agents/librarian-guppi.md`, since the check of a method (`lint.waits_for_another_session`, case 670.4) reads the word for the librarian as a wait for another session; the text read is the same. The first line of the `When` is replaced, and the page's old line is not carried on purpose. The `purpose` names no transcript and stands. A Grep for `estimate-sprint-close-next-session-opens-the-sprint` over the repository with the glob `!vault/archive/**` printed `vault/wiki/brief.md`, `vault/wiki/log.md`, `vault/wiki/rules/rule-sprint-close.md`, `vault/raw/2026-10-12/1449/frontier.md`, `vault/raw/2026-10-12/1449/cases/case-777.md`, `vault/raw/2026-10-10/2350/handoff.md` and `vault/raw/2026-10-10/2350/frontier.md`: no code and no test names the page; the hit of `rule-sprint-close` is its History line and its `estimates` list, which stand; the brief and the Frontier carry this item.

> **problem:**
> The Criterion of `estimate-sprint-close-next-session-opens-the-sprint` names a transcript reading that its method does not take and cannot take, and its method names a Retro that has passed.

> **recommend:**
> - **How far the trigger of the Criterion changes**
>   - Recommended: (a) drop only the transcript words; the test line on the ledger refusals and the `Then` stand.
>   - Answer: agreed, (a).
> - **How the new check runs in this session**
>   - Recommended: (a) the ledger and materialize tests for sprints, and at the Retro of this session `.claude/skills/hi/SKILL.md`, `.claude/skills/sprint-open/SKILL.md` and the step of `.claude/agents/librarian-guppi.md` that writes the brief's first line, read by hand against the Criterion.
>   - Answer: agreed, (a).

> **given:**
> `estimate-sprint-close-next-session-opens-the-sprint`: its Criterion is replaced whole and its `method` set anew.
> **＋** `estimate-hi-writes-frontier`: sets where the opening line stands on the Frontier.
> **＋** `entity-sprint-<id>` and `entity-sprint-<new id>`: the sprint page the session closes and the one the next session creates.
> **＋** `/hi` and `/sprint-open`, rendered into `.claude/skills/hi/SKILL.md` and `.claude/skills/sprint-open/SKILL.md`: the skills that open the next session and its sprint.
> **＋** `vault/wiki/brief.md`, written by the step that `rule-brief` renders into `.claude/agents/librarian-guppi.md`: the brief, whose first line of `Cases` opens the next sprint.
> **＋** `vault/wiki/sprint.md` and `vault/raw/<date>/<hi HHMM>/frontier.md`: the rendered sprint and the Frontier of the session.
> **＋** `guppi ledger`, `guppi materialize`, `tests/test_ledger.py` and `tests/test_materialize.py`: the refusal of decision lines and the `sprint` field of the pages.

> **when:**
> The librarian's run of the session that closes `entity-sprint-<id>` ends with no live sprint page, and the next session opens with `/hi`; someone reads `vault/wiki/brief.md`, that session's `vault/raw/<date>/<hi HHMM>/frontier.md`, its ledger, and the pages of its librarian's run.
> **＋** Or `tests/test_ledger.py` and `tests/test_materialize.py` run `guppi ledger` and `guppi materialize` over a made-up vault with no live sprint page.

> **then:**
> The first line of the `Cases` of Next session in `vault/wiki/brief.md` is `open the next sprint — no sprint is open since the close of <id>`.
> **＋** `/hi` starts `/sprint-open` and writes no `frontier.md` before the opening Case is ratified; then `frontier.md` holds that line first under `## Cases`, closed `[x] … · case N` by the opening Case, and no item of `vault/wiki/sprint.md`, as `estimate-hi-writes-frontier` sets it.
> **＋** While no live `entity-sprint-` page stands, `guppi ledger` refuses each decision line of the session but a `defer`, with one stderr line, until the session's ledger or the same reply holds a `create` decision line of an `entity-sprint-` slug.
> **＋** Each page that the librarian's run writes from the ledger of that session, which holds the `create` decision line of `entity-sprint-<new id>`, carries `sprint: <new id>`.
> **－** An `estimate` or `lesson` line is not refused for this reason.
> **－** The error of `guppi sprint` in the closing run is a flag of the brief, not a failure of this promise.

> **tasks:**
> - [ ] update `estimate-sprint-close-next-session-opens-the-sprint`
>   - set:
>     ```
>     status: pending
>     method: "pytest tests/test_ledger.py -k sprint and tests/test_materialize.py -k sprint; by hand, at the Retro of the session of case 777, .claude/skills/hi/SKILL.md, .claude/skills/sprint-open/SKILL.md and the step of the Render of rule-brief that writes the first line of the brief's Cases read against the Criterion"
>     ```
>   - change: `the Criterion replaced whole — the When reads no transcript; the method runs in the session of case 777`
> - [ ] read `estimate-sprint-close-next-session-opens-the-sprint`

> **ratification:**
> ```
> - decision[case 777][update][estimate-sprint-close-next-session-opens-the-sprint]{ref:rule-sprint-close}
> ```
