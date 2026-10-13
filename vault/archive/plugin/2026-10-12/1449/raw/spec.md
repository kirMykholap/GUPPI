<!-- approved 15:53:48 · session 126e4f76 -->

# Session 1449 — sprint plugin

## Case 776 — A superseded entry lists every Case that retires it

> **context:**
> When a decision line carries `{supersedes:case N}`, `guppi materialize` marks each yaml entry of Case N, and of its sub-cases, with `superseded_by`. `mark_superseded` in `guppi/materialize.py` writes that field as one value, so a second line that retires the same Case overwrites the first. The `decisions` record of the Case keeps a list and appends to it. In session 2350, ledger lines 3 and 5 both carry `{supersedes:case 771}` (cases 775.1 and 775.2). The archived 1913 yaml, `vault/archive/plugin/2026-10-10/1913/raw/materialize.yaml`, therefore holds `superseded_by: '775.2'` on both `defer` entries of case 771, at ledger lines 23 and 24, while its record of 771 lists `decision-case-775.1` and `decision-case-775.2`. A `{supersedes}` mark retires the whole Case, so each of the two Cases retired both entries. With this Case the entry field becomes a list in the order the lines are lifted, as the record already is. An older yaml with one value is read as a list of one, and the next mark appends to that list. The archived 1913 yaml stays as it is, since its record of 771 already names both Cases. A Grep of `superseded_by` over `guppi/` printed five files: `guppi/materialize.py`, `guppi/render.py`, `guppi/generate.py`, `guppi/archive.py` and `guppi/pages.py`. In `render.py`, `archive.py` and `generate.py` the entry field is only tested for presence. `pages.py` names the page field of a Decision page, not the yaml field. So no reader there needs the old form. The same Grep over `.claude/` printed nothing. A Grep of `def as_list|def cases_of` over `guppi/` printed `guppi/materialize.py`, `guppi/lint.py` and `guppi/generate.py`. `cases_of` in `materialize.py` already reads one value or a list for `supersedes`, so the new mark reads the old field through it, and the task adds no second copy of that judgment (`rule-one-judgment-one-implementation`). A Grep of `superseded_by` over `tests/` printed `tests/test_casecheck.py`, `tests/test_render.py`, `tests/test_materialize.py`, `tests/test_lint.py`, `tests/test_archive.py` and `tests/test_generate.py`. Only `tests/test_materialize.py` asserts the entry field equal to one value, so those assertions change. The other files set the field as input that is only tested for presence, name the page field, or hold the word in the name of a test in `tests/test_casecheck.py`. No test reads `rule-materialize` or `estimate-materialize-marks-superseded` live: a Grep of those slugs over `tests/` printed only two comment lines in `tests/test_materialize.py`. In `rule-materialize`, one sentence states the form of the mark: a one-off migration sets `superseded_by` to the number of a Case (case 427). That sentence changes to a list of one. The other sentences that name the mark (case 299.3) state no form, so they stand. `estimate-materialize-marks-superseded` checks the mark, so its Criterion is replaced whole. Its `method` waited for a librarian's run, so it is set anew to the test run alone.

> **problem:**
> The entry-level `superseded_by` of a yaml holds one Case. When two Cases retire the same Case, the yaml names only the last one on every entry. So an entry of `rule-skill-sprint-open` names a Case other than the one that set its page anew.

> **recommend:**
> - **What should the entry's mark hold when two Cases retire the same Case?**
>   - Recommended: (a) a list of every retiring Case, in ledger order; an older yaml with one value read as a list of one; a one-off migration that retires a reading writes a list of one; the tests that compare the field to one value compare it to a list.
>   - Answer: agreed, (a).
> - **Should the archived yaml of the earlier session be corrected?**
>   - Recommended: (a) leave it as it stands; its Decision record of the earlier Case already names both sub-cases.
>   - Answer: agreed, (a).
> - **How is the change checked?**
>   - Recommended: (a) replace the Criterion of `estimate-materialize-marks-superseded` whole and set its method anew to the `tests/test_materialize.py` tests of the mark, including a new test where two lines retire one Case, read at the Retro of this session.
>   - Answer: agreed, (a).

> **given:**
> `guppi/materialize.py`: `mark_superseded` writes the mark and `cases_of` reads one value or a list.
> **＋** `tests/test_materialize.py`: the tests of the `{supersedes}` mark.
> **＋** `rule-materialize`: the rule of the yaml, which names the mark of a one-off migration.
> **＋** `estimate-materialize-marks-superseded`: its Criterion is replaced whole and its method set anew.
> **＋** `rule-one-judgment-one-implementation`: the old field is read through `cases_of`, never a second copy.
> **＋** `guppi/ratified.py`: `remove_case` imports `in_family`.
> **＋** `guppi/prespec.py`: imports `in_family`.
> **＋** `guppi/casecheck.py`: its clash check imports `in_family`.

> **when:**
> `uv run guppi materialize` lifts a decision line that carries one `{supersedes:case N}` block or several, and the entries of each Case N, or of its sub-cases, stand in this unit's `materialize.yaml` or in the `materialize.yaml` of another unit.
> **＋** A later decision line lifted in the same run, or in a later run, carries a `{supersedes:case N}` block for the same Case N.

> **then:**
> For each Case N that a block of the line names, every entry with `case: N` gets `superseded_by`, whatever its kind, and the `decisions` record of that Case gets it too.
> **＋** The `superseded_by` of an entry is a list that holds each Case whose line retires the entry, in the order the lines are lifted, with no Case twice.
> **＋** So does every entry and every `decisions` record of a sub-case of Case N at any depth. A block that names Case N.M marks N.M and its own sub-cases, and leaves its parent and its other sub-cases.
> **＋** The entry of the line carries `supersedes` as a list with one Case per block, in the order of the blocks. The `decisions` record of its Case lists under `supersedes` every Case that its lines name.
> **＋** The `materialize.yaml` of another unit is written with that mark only.
> **＋** An entry marked while no heading of its own Case stands in the unit's `spec.md` carries no `incomplete: [then]`, and its `decisions` record no `case_text` and no `incomplete` for a section.
> **＋** Whether a block covers a Case is judged by `in_family` of `guppi/materialize.py`; `remove_case` of `guppi/ratified.py`, `guppi/prespec.py` and `guppi/casecheck.py` import it.
> **－** An entry without `case` — an `estimate` or a `lesson` entry — gets no mark.
> **－** An entry of an existing `materialize.yaml` whose `supersedes` is one value, not a list, is read as a list of one.
> **－** An entry of an existing `materialize.yaml` whose `superseded_by` is one value, not a list, is read as a list of one, and a new mark is appended to that list.

```then
update:
- slug: rule-materialize
  replace:
  - old: whose one-off migration sets `superseded_by` to the number of that Case on the entry
    new: whose one-off migration sets `superseded_by` on the entry to a list that holds the number of that Case
  change: the superseded_by of an entry is a list, one Case per line that retires it (case 776)
- slug: estimate-materialize-marks-superseded
  set:
    status: pending
    method: pytest in tests/test_materialize.py, the tests of the supersedes mark, a test where two decision lines retire one Case among them
  change: the Criterion replaced whole — the superseded_by of an entry lists every Case that retires it; the method is the test run alone (case 776)
```

```tasks
- [x] `guppi/materialize.py`: `mark_superseded` reads the entry's `superseded_by` through `cases_of` and appends the superseding Case when the list does not hold it; the docstring of `cases_of` names both fields; the module docstring names `superseded_by` of an entry as a list, one value in a yaml written before case 776, and the one-off migration of case 427 as writing a list of one.
- [x] `tests/test_materialize.py`: each assertion that compares an entry's `superseded_by` to one value compares it to a list; one new test where two decision lines each carry `{supersedes:case N}` for the same Case, and every entry of that Case lists both Cases in ledger order; one new test where an entry holds one value and a new mark appends to it, and a mark of a Case already listed adds nothing.
- [x] update `rule-materialize`
- [x] update `estimate-materialize-marks-superseded`
- [x] read `estimate-materialize-marks-superseded`
```

## Case 778 — A waiting reading of the sprint page makes no Cases line at /hi

> **context:**
> When `/hi` writes the Frontier, it takes each open `W` reading whose method runs now. For each other open `W` line it writes a Cases line that asks to fix the method, replace the Criterion or archive the page (case 670.6). The one exception is a `W` line whose `method` names the session that closes a sprint, or the session after it, which stays open under `## Work` (case 670.5). An Estimate whose `target` is the live sprint page waits by design: since case 772 the brief leaves it out of `Work` and `Ask the person` until its moment, and Retro neither reads it nor sets it `failed` while its work is not done; the Retro of the session that finishes its work, or the closing Case of `/sprint-close`, reads it. The `/hi` step got no such exception. At the `/hi` of session 2350 it wrote four Cases lines for Estimates of `entity-sprint-plugin` whose work belongs to later milestones, and the person closed them `· work` (`lesson-hi-unread-sprint-reading-made-a-case-line`, ledger line 13 of session 2350). Today's brief lists no such reading under `Work`, but the short brief of `carry` copies each open `W` line of the Frontier into `Work` (`rule-carry-over`), so such a line can still reach `/hi`. The person chose that such a line stays open under `## Work` and makes no Cases line, judged from the `target` of the Estimate's page, with no judgment of whether the work is done: a reading that runs now is still taken, and one that cannot waits for the Retro or the close that `rule-retro` names. The Render of `rule-skill-hi` has the reading step open only the page of each Estimate it reads, and a `W` line of the short brief of `carry` is a slug alone, since that brief leaves out Readings due (`rule-carry-over`), so neither the method nor the `target` of a reading that cannot run is at hand; pre-spec found this, and the Case has the reading step open the page of the Estimate of each open `W` line and judge from it both whether the reading runs now and its `target`. So two lines of the Criterion of `estimate-hi-takes-its-readings` are not carried on purpose: the `＋` line that the agent opens the page of each Estimate it reads, and the `－` line that only the reading step opens the pages of the Estimates it reads. Both are replaced by lines that name the page of the Estimate of each open `W` line. The person asked whether such Estimates stay visible: the brief's Readings due lists every `pending` Estimate with where it is read, `make lint` prints one `unread: pending` finding per such Estimate (`check_unread` in `guppi/lint.py`), and the handoff names each Estimate whose reading cannot be taken yet with its moment. The person chose to leave out of this Case Estimates that wait for any other event, since the rule on methods in `rule-case-protocol` has pre-spec report a `method` that waits for a later session, a session of a sprint, the session that closes one, the librarian or a `/hi` (case 670.4), with one exception, an Estimate whose target is a sprint page (case 772.4); the wait of a `W` line whose `method` names the close of a sprint stands in `rule-skill-hi` (case 670.5) and `rule-brief` (case 772.1). In the Render of `rule-skill-hi`, four sentences state this step: the Cases source of an open `W` line whose reading cannot run now, which stands, since such a line is still written by the reading step; the sentence on which pages the step opens, which the Case rewrites; the sentence that makes the Cases line, which the new exception bounds; and the exception of the close of a sprint, after which the new sentence stands. The Criterion of `estimate-hi-takes-its-readings` speaks of this step, so it is replaced whole with one more `－` line, and its `purpose`, which names the Cases line for each other open `W` line, is set anew; its `method` reads the new Render in the Spec at the Retro of the session that changes it and stands. The Criterion of `estimate-hi-writes-frontier` names that source as written by the reading step, which stays true, so it stands. A Grep for the pattern ``open `W` line|W` line`` over `vault/wiki/rules/`, `.claude/` and `vault/wiki/orchestration.md` printed `.claude/skills/work/SKILL.md`, `.claude/skills/hi/SKILL.md`, `.claude/skills/retro/SKILL.md`, `vault/wiki/orchestration.md`, `.claude/agents/librarian-guppi.md`, `.claude/skills/carry/SKILL.md`, `vault/wiki/rules/rule-skill-hi.md`, `vault/wiki/rules/rule-retro.md`, `vault/wiki/rules/rule-brief.md`, `vault/wiki/rules/rule-orchestration.md`, `vault/wiki/rules/rule-work-mode.md` and `vault/wiki/rules/rule-carry-over.md`: Work Mode takes a `W` reading only when its work is built and its moment has come, Retro and the brief already wait for an Estimate of the live sprint page, `carry` copies open `W` lines, and `orchestration.md` lets a `W` line stay open through Plan Mode, so none of them is made false. Case 777 reads `.claude/skills/hi/SKILL.md` at this session's Retro for the opening of a sprint, a moment this Case does not touch.

> **problem:**
> `/hi` makes a Cases line for an open `W` reading of an Estimate of the live sprint page that waits by design, so the person closes a line that needed no decision.

> **recommend:**
> - **What should `/hi` do with a waiting sprint-page check**
>   - Recommended: (a) it stays open in Work, as the close-of-sprint checks do.
>   - Answer: not answered; replaced by the question on which readings skip the decision item at `/hi`.
> - **How should `/hi` tell that a sprint check's work is not done**
>   - Recommended: (a) no judgment of done at `/hi`: any open Work line of a check of the live sprint page that cannot be read now stays open in Work.
>   - Answer: agreed, (a).
> - **Which check confirms the change**
>   - Recommended: (a) add one exception line to `estimate-hi-takes-its-readings` and set its purpose anew; its method stands.
>   - Answer: agreed, (a).
> - **Which readings should skip the decision item at `/hi`**
>   - Recommended: (a) only the checks of the live sprint page; any other reading `/hi` cannot take still becomes a decision item.
>   - Answer: agreed, (a). The person first proposed that every reading `/hi` cannot take stays in Work, is flagged by the librarian, and goes to the backlog by a defer at the next `/hi`, and asked whether such checks stay visible; after the answer the person agreed with the recommendation.
> - **Should a check be allowed to wait for some event**
>   - Recommended: (a) not in this Case; checks that wait for another event stay not allowed, and a wider rule is an item of its own.
>   - Answer: agreed, (a).

> **given:**
> `rule-skill-hi`: the rule of `/hi`, rendered into `.claude/skills/hi/SKILL.md`, whose reading step changes.
> **＋** `estimate-hi-takes-its-readings`: its Criterion is replaced whole and its `purpose` set anew.
> **＋** `entity-sprint-<id>`: the live sprint page, the `target` of the Estimates that wait.
> **＋** `rule-retro`: sets when an Estimate of the live sprint page is read.
> **＋** `vault/wiki/brief.md` and `raw/<date>/<hi HHMM>/frontier.md`: the brief whose readings `/hi` takes and the Frontier it writes.

> **when:**
> The person types `/hi` of `.claude/skills/hi/SKILL.md` on `UserPromptSubmit`, and the agent writes `raw/<date>/<hi HHMM>/frontier.md`, whose `## Work` holds the `pending` readings of `vault/wiki/brief.md` and whose `## Ask` holds its readings that only the person can take.

> **then:**
> Once it writes `raw/<date>/<hi HHMM>/frontier.md`, and before the reply that shows that Frontier asks the question on the order, the agent takes each reading of an open `W` line whose whole method runs now.
> **＋** It reads what the method names from `vault/wiki/brief.md`, `git log`, `git status` and the files and commands the method names.
> **＋** It opens the page of the Estimate of each open `W` line, judges from that page whether its reading runs now, and judges each reading it takes against its `## Criterion`.
> **＋** It closes the `W` line of each reading taken `[x] … · work` in `raw/<date>/<hi HHMM>/frontier.md`, then writes one `estimate[...]` line per reading in a `LEDGER` block of the reply that shows that Frontier, which ends in text.
> **＋** For each other open `W` line, whose reading cannot run now, it writes one line under `## Cases` of `raw/<date>/<hi HHMM>/frontier.md` that names the Estimate by slug and asks to fix its method, replace its Criterion or archive it; the `W` line closes `· case N` when that Case is ratified.
> **＋** In the reply that shows that Frontier, before the question on the order, it puts each open `A` line to the person as a question: the Estimate by slug and its question.
> **＋** When the person answers one, the agent closes its `A` line `[x] … · work` in `raw/<date>/<hi HHMM>/frontier.md` first, then writes its `estimate[...]` line, the answer as its result, in a `LEDGER` block of the reply, which ends in text.
> **－** It reads no transcript of an earlier session.
> **－** A `W` line of an Estimate whose `method` names the session that closes a sprint, or the session after that close, stays open under `## Work` and is no Cases line.
> **－** A `W` line of an Estimate whose `target` is the live sprint page `entity-sprint-<id>` and whose reading cannot run now stays open under `## Work` and is no Cases line. It waits for the moment that `rule-retro` sets for it. The agent judges this from the `target` of the page of that Estimate, with no judgment of whether the work is done.
> **－** An `A` line whose question names the session that closes a sprint, or the session after that close, stays open under `## Ask` and is not put to the person. It is put at the `/hi` whose `vault/wiki/brief.md` opens the `Cases` of its Next session with `open the next sprint`, or in the session the person names as the one that closes the sprint. The agent judges this from the line as `vault/wiki/brief.md` gives it, with no page opened.
> **－** The Frontier is still assembled with no page opened. Only the reading step opens pages: the page of the Estimate of each open `W` line.
> **－** At `/hi` the agent changes no page and no file except `raw/<date>/<hi HHMM>/frontier.md`.

```then
update:
- slug: rule-skill-hi
  replace:
  - old: A `W` line of an Estimate whose `method` names the session that closes a sprint, or the session after that close, stays open under `## Work` and waits for that session (case 670.5).
    new: 'A `W` line of an Estimate whose `method` names the session that closes a sprint, or the session after that close, stays open under `## Work` and waits for that session (case 670.5). A `W` line of an Estimate whose `target` is the live sprint page `entity-sprint-<id>` and whose reading cannot run now stays open under `## Work` too and makes no Cases line: it waits for the Retro of the session that finishes its work or for the closing Case of `/sprint-close`, as `rule-retro` sets it; judge this from the `target` of its page, with no judgment of whether its work is done (case 778).'
  - old: this step opens the page of each Estimate it reads and judges the reading against its `## Criterion`.
    new: this step opens the page of the Estimate of each open `W` line, judges from it whether its reading runs now, and judges each reading it takes against its `## Criterion` (case 778).
  change: an open W line of an Estimate of the live sprint page whose reading cannot run now stays open under Work and makes no Cases line (case 778)
- slug: estimate-hi-takes-its-readings
  set:
    status: pending
    purpose: Whether /hi takes, once it writes the Frontier and before the reply that shows it asks the order, each open W reading whose whole method runs now from files and commands, reads no transcript, writes a Cases line for each other open W line but those of the close of a sprint and those of an Estimate of the live sprint page, puts each open Ask line to the person but one that waits for the close of a sprint or the session after it, writes the answer as its reading line, and opens no page but the Estimates of its open W lines
  change: the Criterion replaced whole — an open W line of an Estimate of the live sprint page whose reading cannot run now stays open under Work and is no Cases line
```

```tasks
- [x] update `rule-skill-hi`
- [x] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
- [x] update `estimate-hi-takes-its-readings`
- [x] read `estimate-hi-takes-its-readings`
```

## Case 779 — The opening of the next sprint is checked by what runs in one session

> **context:**
> `estimate-sprint-close-next-session-opens-the-sprint` checks what happens after a sprint closes: the brief opens the next sprint, `/hi` starts `/sprint-open`, `guppi ledger` refuses decision lines until a sprint page is created, and the pages written that session carry the new sprint id. Its Criterion says that, in the session after the close, someone reads the brief, the Frontier, the refusals of `uv run guppi ledger` in the transcript, the ledger and the pages of the librarian's run; its `method` reads none of these. It runs two test files and reads skill texts (case 769.5; handoff of session 2350, For the next session). A method holds only what runs in the Case's own session (case 670.4), and the exception for an Estimate of a sprint page (case 772.4) does not apply here, since the target is `rule-sprint-close`, so those live readings can never run. Case 777 dropped only the transcript words; a finding of `/pre-spec` showed that the rest of that first `When` line keeps the same defect, and the person chose to rewrite the trigger to name what the check reads. This Case replaces Case 777. The first `When` line of the page is not carried on purpose: its new first line names the reading of the skill texts and the brief step, and the line of the tests stands. The `Then` stands word for word. A Criterion replaced whole sets the page `pending`, and its `method` names the Retro of the session of case 769, which is past, so the method is set anew to run at the Retro of this session. The method names the brief step as the Render of `rule-brief`, which governs `.claude/agents/librarian-guppi.md`, since the check of a method (`lint.waits_for_another_session`, case 670.4) reads the word for the librarian as a wait for another session; the text read is the same. The `purpose` names no transcript and stands. A Grep for `estimate-sprint-close-next-session-opens-the-sprint` over the repository with the glob `!vault/archive/**` printed `vault/wiki/brief.md`, `vault/wiki/log.md`, `vault/wiki/rules/rule-sprint-close.md`, `vault/raw/2026-10-12/1449/frontier.md`, `vault/raw/2026-10-12/1449/ledger.md`, `vault/raw/2026-10-12/1449/cases/case-777.md`, `vault/raw/2026-10-12/1449/cases/case-779.md`, `vault/raw/2026-10-10/2350/handoff.md` and `vault/raw/2026-10-10/2350/frontier.md`: no code and no test names the page; the hit of `rule-sprint-close` is its History line and its `estimates` list, which stand; the brief and the Frontier carry this item, and the ledger the decision line of Case 777.

> **problem:**
> The Criterion of `estimate-sprint-close-next-session-opens-the-sprint` names readings of a later session that its method does not take and cannot take, and its method names a Retro that has passed.

> **recommend:**
> - **How far the trigger of the Criterion changes**
>   - Recommended: (a) drop only the transcript words; the test line on the ledger refusals and the `Then` stand.
>   - Answer: agreed, (a); replaced by the change below.
> - **How the new check runs in this session**
>   - Recommended: (a) the ledger and materialize tests for sprints, and at the Retro of this session `.claude/skills/hi/SKILL.md`, `.claude/skills/sprint-open/SKILL.md` and the step of `.claude/agents/librarian-guppi.md` that writes the brief's first line, read by hand against the Criterion.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: on a finding of `/pre-spec`, the person chose to rewrite the trigger to name what the check reads — the ledger and materialize tests over a made-up vault, and the skill texts of `/hi` and `/sprint-open` and the brief step of `rule-brief` read against the expected results — the expected results kept.
>   - Taken: the first `When` line names that reading in place of the readings of the session after the close; the line of the tests and the `Then` stand; the Case is built again as Case 779, which replaces Case 777.

> **given:**
> `estimate-sprint-close-next-session-opens-the-sprint`: its Criterion is replaced whole and its `method` set anew.
> **＋** `estimate-hi-writes-frontier`: sets where the opening line stands on the Frontier.
> **＋** `entity-sprint-<id>` and `entity-sprint-<new id>`: the sprint page the session closes and the one the next session creates.
> **＋** `/hi` and `/sprint-open`, rendered into `.claude/skills/hi/SKILL.md` and `.claude/skills/sprint-open/SKILL.md`: the skills that open the next session and its sprint.
> **＋** `vault/wiki/brief.md` and `rule-brief`, which renders into `.claude/agents/librarian-guppi.md` the step that writes the brief: the brief, whose first line of `Cases` opens the next sprint.
> **＋** `vault/wiki/sprint.md` and `vault/raw/<date>/<hi HHMM>/frontier.md`: the rendered sprint and the Frontier of the session.
> **＋** `guppi ledger`, `guppi materialize`, `tests/test_ledger.py` and `tests/test_materialize.py`: the refusal of decision lines and the `sprint` field of the pages.

> **when:**
> Someone reads `.claude/skills/hi/SKILL.md`, `.claude/skills/sprint-open/SKILL.md` and the step of the Render of `rule-brief` that writes the `Cases` of Next session in `vault/wiki/brief.md`, for the session that opens after the librarian's run of the session that closes `entity-sprint-<id>` ends with no live sprint page.
> **＋** Or `tests/test_ledger.py` and `tests/test_materialize.py` run `guppi ledger` and `guppi materialize` over a made-up vault with no live sprint page.

> **then:**
> The first line of the `Cases` of Next session in `vault/wiki/brief.md` is `open the next sprint — no sprint is open since the close of <id>`.
> **＋** `/hi` starts `/sprint-open` and writes no `frontier.md` before the opening Case is ratified; then `frontier.md` holds that line first under `## Cases`, closed `[x] … · case N` by the opening Case, and no item of `vault/wiki/sprint.md`, as `estimate-hi-writes-frontier` sets it.
> **＋** While no live `entity-sprint-` page stands, `guppi ledger` refuses each decision line of the session but a `defer`, with one stderr line, until the session's ledger or the same reply holds a `create` decision line of an `entity-sprint-` slug.
> **＋** Each page that the librarian's run writes from the ledger of that session, which holds the `create` decision line of `entity-sprint-<new id>`, carries `sprint: <new id>`.
> **－** An `estimate` or `lesson` line is not refused for this reason.
> **－** The error of `guppi sprint` in the closing run is a flag of the brief, not a failure of this promise.

```then
update:
- slug: estimate-sprint-close-next-session-opens-the-sprint
  set:
    status: pending
    method: pytest tests/test_ledger.py -k sprint and tests/test_materialize.py -k sprint; by hand, at the Retro of the session of case 779, .claude/skills/hi/SKILL.md, .claude/skills/sprint-open/SKILL.md and the step of the Render of rule-brief that writes the first line of the brief's Cases read against the Criterion
  change: the Criterion replaced whole — the When names what the check reads, with no reading of a later session; the method runs in the session of case 779
```

```tasks
- [x] update `estimate-sprint-close-next-session-opens-the-sprint`
- [x] read `estimate-sprint-close-next-session-opens-the-sprint`
```
