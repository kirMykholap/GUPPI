## Case 799 — Lint does not mark red a check whose reading waits for a later moment

> **context:**
> `make lint` prints one red line for each Estimate that stands `pending` or `failed`, whatever its reading waits for, and the run fails when any line is printed, on GitHub too. The Purpose of `rule-lint`, the rule that governs this, says that a `pending` Estimate is red until its reading (case 182). Under `## Flags` of `vault/wiki/brief.md`, the librarian's last run printed `make lint, 12 lines`. Ten of them are `unread: pending` lines of Estimates whose `method` names a later moment: an event, such as the first `/merge-main` that leaves a conflicted page, a session of the sprint `plugin` before its close, the session that closes it, or the session after a close. Most of these lines cannot be cleared before their moment, so the same lines come back in every brief. Lint never finds the event either. It judges the words of a `method`, not whether its moment has come. That is the brief's job. By `rule-brief`, the librarian lists every `pending` or `failed` Estimate under Readings due at each run, looks for the event a `method` waits for in `git log`, the ledger, the handoff and the files the `method` names, and puts the reading under `Work` once it sees the event. A reading of the live sprint page waits for the Retro of the session that finishes its work, or for the closing Case of `/sprint-close`, which puts each Estimate that is still unread to the person. The short brief that `carry` writes has no Readings due. The next run of the librarian writes the full list again, so this gap stands.
>
> By the person's answers, lint gives no `unread` finding for a `pending` Estimate when any part of its `method` waits for a later moment. It stays red for a `failed` Estimate and for a `pending` one whose `method` has no such part. A reading is recorded once, as a whole, so it cannot be taken before its latest part. Lint does not tell whether the moment has come. A reading whose event has come is put up by the `Work` list of the brief, not by lint. `estimate-ask-finds` is such a reading: its event has come, the brief puts it under `Work`, and lint leaves it out. The same holds for `estimate-hi-writes-frontier`, whose second part, a test, could run now, while its first part waits for the close of the sprint. A part of a `method` between two `;` waits for a later moment when it opens with `after`, or with `by hand, after`, and names its event before a colon, or when it names a later session, the next session, a session after another, a session of a sprint, the session that closes one, the librarian or `/hi`. Over the methods of the ten Estimates, as the pages hold them, each one has such a part. The Purpose of `rule-lint` changes its sentence on red. Its first sentence, on a reading that nobody took, stays true. Lint still marks a `pending` Estimate red when no part of its `method` waits for a later moment, and the `Work` list of the brief puts up a reading whose moment has come, so no such page sits unnoticed. The Criterion and the `purpose` of `estimate-lint-checks-the-statuses` state the old promise, so this Case replaces both, and the Criterion carries over its lines on `status` and `deferred` word for word. Two lines of the old Criterion are not carried, on purpose. Its `When` now names the `method` of each Estimate too, since the new judgment reads it. Its `unread` line, on every Estimate that is `pending` or `failed`, is replaced by the lines on a `failed` Estimate, on a `pending` one whose `method` has no part that waits for a later moment, and on a `method` that waits for a later moment. Its `method`, `uv run pytest tests/test_lint.py`, states no promise and stands. The Criteria of the other Estimates of `rule-lint` speak of other classes, so they stand.
>
> Two of the red lines are left to other Cases. The `orphan` line of `rule-github-repository` goes by Case 795.1 of this session, which changes pages and not the code of lint. The person chose to take up the line `rules/rule-morph: deferred: 4 times since case 239` as an item of its own, so this Case leaves it out. The person also chose to read `estimate-git-context-current` in Work Mode of this session. Its method waits for the first `/hi` after the first push to GitHub. The brief says that `main` and `plugin` were pushed in session 2349, so the `/hi` of this session is that moment, and a later session would miss it.
>
> One judgment. A Grep `ANOTHER_SESSION|waits_for_an_event|waits_for_another_session` over `guppi/` printed `guppi/lint.py` and `guppi/prespec.py`. In `guppi/lint.py`, `waits_for_an_event` judges a part that waits for an event it names, and `ANOTHER_SESSION` is the pattern of a later session. The new predicate of `guppi/lint.py` calls both, so it adds no second copy of either. `guppi/prespec.py` imports `waits_for_another_session`, which judges something else: whether a `method` breaks the limit to its own session. It is false for a part that names an event or the person, since those parts are allowed. The new predicate is true for both, since such a reading still waits. The two answer different questions on purpose, so neither stands for the other. The librarian makes its judgment of an event in prose, as an agent, so there is no code for a test to run beside lint. A Grep `waits for|later session` over `guppi/` printed `guppi/lint.py`, `guppi/ledger.py`, `guppi/box.py`, `guppi/gate.py`, `guppi/casecheck.py`, `guppi/prespec.py`, `guppi/generate.py` and `guppi/spec.py`. Outside `guppi/lint.py` and `guppi/prespec.py`, no hit judges the `method` of an Estimate.
>
> Tests and texts. A Grep `unread: (pending|failed)` over `tests/` printed `tests/test_lint.py` and `tests/test_generate.py`. Their Estimates carry the method `pytest tests/test_x.py`, which waits for nothing, so their `unread` lines stand. A Grep `rule-lint|estimate-lint-checks-the-statuses|estimate-git-context-current` over `tests/` printed `tests/test_lint.py`, whose only hit is its docstring. It seeds its pages under a temporary folder, so no test reads a page this Case changes. A Grep `\bunread\b|red until` over `vault/wiki/` and `.claude/` printed 19 files under `vault/wiki/` and `.claude/skills/sprint-close/SKILL.md`. `brief.md` and `log.md` were not read. `rule-lint` and `estimate-lint-checks-the-statuses` change here. The pages of the sprint close and their Estimates speak of an Estimate that a close carries or archives unread. That is a status, not a line of lint. The other hits stand in a Result or a History line. So the change makes none of them false.

> **problem:**
> `make lint` marks red every Estimate that is not yet read, also one whose reading cannot be taken before a later event or session. The same red lines are carried from session to session, and lint stays red on GitHub, though most of them cannot be cleared before their moment.

> **recommend:**
> - **What should lint do with a pending check that waits for a later event?**
>   - Recommended: (a) lint leaves out a check whose reading waits for a later moment; the brief still lists it under Readings due and moves it to Work when its event comes, and the sprint close still puts each one left to the person.
>   - Answer: agreed, (a), after the person asked how such an event is found later and what shows that an Estimate has not passed.
> - **Should the check of the git context be read in this session?**
>   - Recommended: (a) read it in this session's Work Mode.
>   - Answer: agreed, (a).
> - **What happens to `rule-morph`, the decision that keeps being put off?**
>   - Recommended: (a) take it up as its own item in this session; this Case leaves it out.
>   - Answer: (a), added as a separate item.
> - **Must every part of a check's method wait before lint leaves it out, or is one waiting part enough?**
>   - Recommended: (b) one waiting part is enough, since a check is read once as a whole; the brief's Work list, not lint, puts up a reading whose moment has come.
>   - Answer: agreed, (b).
> - **Change**
>   - Asked: rewrite the two places of `context` that still spoke of a reading that is due, to the rule as it works.
>   - Taken: `context` now says that lint marks a `pending` Estimate red only when no part of its `method` waits, and that the `Work` list of the brief puts up a reading whose moment has come.

> **given:**
> `guppi/lint.py`: `check_unread`, and the new predicate of a `method` that waits for a later moment.
> **＋** `tests/test_lint.py`: the tests of the class `unread`.
> **＋** `rule-lint`: the rule of lint, whose Purpose says when a `pending` Estimate is red.
> **＋** `estimate-lint-checks-the-statuses`: its Criterion and `purpose` are replaced.
> **＋** `rule-brief`: the brief lists every `pending` Estimate under Readings due and puts a reading under `Work` once its event comes.
> **＋** `estimate-git-context-current`: read by its method in Work Mode of this session.
> **＋** `vault/wiki/`: the live pages that lint reads.
> **＋** `/hi`: the skill that opens a session, a moment that a `method` may name.

> **when:**
> `uv run guppi lint` reads the `status` of the live pages under `vault/wiki/` and the `method` of each Estimate.

> **then:**
> `status`: a `built` entity or rule with an Estimate not `passed`, a `draft` one with every Estimate `passed`; a page without Estimates is not judged.
> **＋** `status`: an Estimate `passed` or `failed` without `## Result`; an Estimate whose `target` is not an entity or a rule, or does not list it in `estimates`.
> **＋** `unread`: every Estimate `failed`, and every Estimate `pending` whose `method` does not wait for a later moment, one finding each, `unread: <status>`.
> **＋** A `method` waits for a later moment when a part of it between two `;` opens with `after`, or with `by hand, after`, and names its event before a colon, or names a later session, the next session, a session after another, a session of a sprint, the session that closes one, the librarian or `/hi`.
> **＋** `deferred`: a placeholder — a rule or entity with `deferred_by` and none of `kind`, `estimates`, `tags` — earns one finding `deferred: <N> times since case <M>` in place of its `schema` findings on those fields and of `orphan`; a page with `deferred_by` whose fields are in place earns none.
> **－** A `pending` Estimate whose `method` waits for a later moment earns no `unread` finding.
> **－** A `failed` Estimate earns its `unread` finding whatever its `method` says.

> **tasks:**
> - [ ] `guppi/lint.py`: a new predicate, `waits_for_a_later_moment`, is true when a part of a `method` between two `;` waits for an event by `waits_for_an_event`, or names a later moment by `ANOTHER_SESSION`; `check_unread` gives no finding for a `pending` Estimate whose `method` it holds; the docstring of the class `unread` says so.
> - [ ] `tests/test_lint.py`: tests whose names hold `unread`: a `pending` Estimate whose method waits for an event before a colon, one whose method names a session of a sprint before its close and one whose method names the session after a close give no finding; a `pending` one whose method is a reading at the Retro of its own session, and a `failed` one whose method waits for an event, each give `unread`.
> - [ ] update `rule-lint`
>   - old: `` a `pending` Estimate is red until its reading (case 182, point 13), and a placeholder is red ``
>   - new: `` a `pending` Estimate is red until its reading, but for one whose `method` waits for a later moment — an event it names, a later session, a session of a sprint, the session that closes one, the librarian or `/hi` — since the brief lists it under Readings due and puts it under Work once its moment comes, and a `failed` one is red until it is read again (cases 182, 799); a placeholder is red ``
>   - change: `a pending Estimate whose method waits for a later moment is no longer red; a failed one still is (case 799)`
> - [ ] update `estimate-lint-checks-the-statuses`
>   - set:
>     ```
>     status: pending
>     purpose: A status its Estimates do not support, a failed Estimate, a pending Estimate whose reading does not wait for a later moment, and a placeholder are findings of lint
>     ```
>   - change: `the Criterion and purpose replaced whole — a pending Estimate whose method waits for a later moment earns no unread finding (case 799)`
> - [ ] read `estimate-lint-checks-the-statuses`
> - [ ] by hand, in Work Mode of this session: `estimate-git-context-current` read by its method — the context of the first turn of this session's `/hi`, the output of `git remote -v` and `.claude/skills/hi/SKILL.md` against its Criterion; the main agent writes the estimate line.

> **ratification:**
> ```
> - decision[case 799][update][rule-lint]{ref:rule-lint}
> - decision[case 799][update][estimate-lint-checks-the-statuses]{ref:rule-lint}
> ```
