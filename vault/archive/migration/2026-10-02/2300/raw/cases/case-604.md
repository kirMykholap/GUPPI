## Case 604 — `guppi onward --plan` counts a re-ratification for the whole session

> **context:**
> At the end of each reply in Plan Mode, the `Stop` hook `uv run guppi onward --plan` decides whether to send the agent on to `/pre-spec` or to the exit. It holds back while a Case is still out, meaning a file under `cases/` was written after that Case's last decision line. Today it finds that time in three places: the timed lines of `ledger.md`, the replies since the person's last message (the stretch, case 597.2), and the reply that ended. The ledger hook does not write a line it already holds. So when a Case is built again and ratified again with the same decision lines, `ledger.md` keeps the time of the first ratification. Only the reply that ratified it again shows the later time. Once the person writes another message, that reply falls out of the stretch, and the Case counts as out for the rest of the session. In session 2049, Case 596 was ratified again with unchanged lines. At the last ratification of the Frontier, the hook stayed silent and the person had to ask the agent to go on. That session recorded this as `lesson-prespec-onward-re-ratification-out-after-its-stretch`.
>
> By the person's answers, the hook now reads the decision lines of every reply of the main agent in the transcript, each at the time of its record. It uses `transcript_records` of `guppi/ledger.py`, the reading the ledger hook already makes when it collects lines. Case numbers are never reused, so a reply of an earlier session in the same transcript cannot name a Case of this one. The judgment of refusals (`spent`, `told`, `refusals`) stays on the stretch. The Criterion of `estimate-prespec-onward-reads-the-decisions-of-the-stretch` is replaced whole. Its `purpose` and `method` both state the old limit, so they are set anew. The page is renamed `estimate-prespec-onward-reads-the-decisions-of-the-session`, and a Glob of `vault/**/*reads-the-decisions-of-the-session*.md` found no file. The Estimate has not been read since case 597.2, and it stays `pending`. `estimate-prespec-onward-sends-the-agent-on` stands: its Criterion speaks of a Case still out only "as `rule-prespec-onward` judges it", and of refusals in the stretch, which do not change. The Case creates no page, so the vault query was not run. Only the hook's code changes; its registration in `.claude/settings.json` does not. That file registers six hooks on `Stop`: `uv run guppi ledger`, `uv run guppi ratified`, `uv run guppi casecheck`, `uv run guppi context`, `uv run guppi onward` and this one. None of them reads the judgment this hook makes. No text that the hook reads changes form, so no old form is kept. The lesson stands in the ledger of session 2049, not this one, so no decision line carries `{addresses}` (`ratification.md`). `rule-ledger-line-withdrawn-on-re-ratification`, deferred by case 594, deals with a line dropped on re-ratification, not with its time, and it is not taken up. `insight-spec-write-parent-body-kept-on-re-ratification` deals with the Spec hook and is not named. Cases 601, 602 and 603 of this session change neither `rule-prespec-onward` nor the `Stop` judgment of this hook.
>
> The check of this answer gave four notes, one for each line of the old Criterion that is not carried word for word. Each of those lines changes on purpose:
> - The line on the sources now says "the transcript" in place of "the stretch".
> - The line that defined the stretch is dropped, because the reading of decision lines no longer uses it. The new last line keeps the stretch for the refusals.
> - The line on the time of a record now speaks of a reply of the transcript.
> - The line on the outcome now reaches every later reply of the session, after a later message of the person too.
>
> Frame checks:
> - A Grep of `estimate-prespec-onward-reads-the-decisions-of-the-stretch` over the repository outside `vault/raw/` printed five files: `brief.md`, `log.md`, `rule-prespec-onward.md`, `decision-case-597.2.md` and `decision-case-597.md`. The only live hit is the `estimates` field of the rule, and the rename moves that link.
> - A Grep of `rule-prespec-onward` over the repository outside `vault/raw/` and `vault/archive/` printed 20 files. The live hits outside the rule, its Estimates, `decisions/`, `brief.md` and `log.md` were read around their lines: `orchestration.md`, `rule-orchestration.md`, `rule-prespec.md`, `rule-plan-mode.md`, `.claude/skills/pre-spec/SKILL.md`, `guppi/prespec.py`, `guppi/onward.py`, three Estimates of `rule-orchestration` and `estimate-retro-onward-sends-the-agent-to-the-handoff`. Each says that the hook sends the agent on, or names it as a child. None says which replies it reads.
> - A Grep of the pattern `(still out|is out|decision lines?).{0,200}(stretch|person's last message)|(stretch|person's last message).{0,200}(still out|decision line)` over the repository outside `vault/raw/` and `vault/archive/` printed six files: `log.md`, `rule-prespec-onward.md`, the lesson, the Estimate replaced here, `decision-case-597.md` and `guppi/onward.py`. This Case changes the rule, the Estimate and the module. The lesson and the Decision page are history.
> - The docstring of `stretch` in `guppi/ledger.py` says that `guppi onward` calls it. That stays true, because the refusals are still judged by the stretch.

> **problem:**
> When a Case is ratified again with the decision lines the ledger already holds, `guppi onward --plan` sees that re-ratification only until the person's next message. After that, the Case counts as out for the rest of the session. The hook then stays silent at the last ratification, and the person has to send the agent on by hand.

> **recommend:**
> - **How far back the hook reads the replies for decision lines**
>   - Recommended: (a) every reply of the main agent in the transcript, each counted at the time of its record, the way the ledger hook reads it.
>   - Answer: agreed with the recommendation, (a).
> - **What happens to the Estimate that checks the reading of the decision lines**
>   - Recommended: (a) replace the Criterion, set anew the `purpose` and `method`, and rename it `estimate-prespec-onward-reads-the-decisions-of-the-session`.
>   - Answer: agreed with the recommendation, (a).

> **given:**
> `rule-prespec-onward` — the rule of the hook, its `Purpose` section changed
> **＋** `estimate-prespec-onward-reads-the-decisions-of-the-stretch` — the promise of the reading of decision lines, its Criterion replaced whole and renamed `estimate-prespec-onward-reads-the-decisions-of-the-session`
> **＋** `guppi/onward.py` — the hook, its `stretch_replies`, `last_decisions` and `case_out`
> **＋** `guppi/ledger.py` — `transcript_records`, the reading of the transcript the ledger hook makes, and `refusals`, the judgment of the stretch; unchanged
> **＋** `guppi/casecheck.py` — `moment`, the time of a record; unchanged
> **＋** `tests/test_onward.py` and `tests/test_ledger.py` — the tests of the hook and of the readings it imports
> **＋** `transcript_path` of the `Stop` payload — the transcript the hook reads
> **＋** `raw/<date>/<hi HHMM>/ledger.md` — the session's ledger, whose timed decision lines the hook reads
> **＋** `raw/<date>/<hi HHMM>/cases/` — the files of the Cases, whose times the hook compares

> **when:**
> The `Stop` hook `uv run guppi onward --plan` judges, at the end of a reply of the main agent, whether a Case is still out.

> **then:**
> A Case N is still out when a file `case-<N>.md` under `raw/<date>/<hi HHMM>/cases/` was written after the last decision line of Case N or of a sub-case of N.
> **＋** The decision lines it reads are the timed lines of `raw/<date>/<hi HHMM>/ledger.md`, the lines inside a `LEDGER` block of each reply of the main agent in the transcript at `transcript_path`, and those of the reply that ended.
> **＋** The replies of the transcript are its `assistant` records of the main agent, read by `transcript_records` of `guppi/ledger.py`, the reading the ledger hook makes. A reply before the person's last message counts like one after it.
> **＋** A line of a reply of the transcript counts at the time of its record, read by `moment` of `guppi/casecheck.py`. A line of the reply that ended counts as written now.
> **＋** A line of `ledger.md` counts at its time on the `hi` date, rolled to the next date when the time runs backwards.
> **＋** So a Case built again and ratified by a reply whose decision lines the ledger already held is not out after that reply, and not at any later reply of the session, after a later message of the person too. This includes the reply that writes again a line the ledger hook refused.
> **－** A file of a Case with no decision line is out.
> **－** A record whose time cannot be read counts none of its lines. A transcript that cannot be read leaves `ledger.md` and the reply that ended as the only sources.
> **－** Its own refusals and those of the ledger hook are still judged in the stretch, by `refusals` of `guppi/ledger.py`.

> **tasks:**
> - [ ] update `rule-prespec-onward`
>   - old: `` and in the replies since the person's last message, each at the time of its record in the transcript, the reply that ended counted as now (case 597.2) ``
>   - new: `` and in every reply of the main agent in the transcript, each at the time of its record, the reply that ended counted as now (cases 597.2, 604) ``
>   - change: `a Case is judged out by the decision lines of every reply of the transcript, not only of the stretch, so a re-ratification with unchanged lines counts for the rest of the session (case 604)`
> - [ ] update `estimate-prespec-onward-reads-the-decisions-of-the-stretch`
>   - rename: `estimate-prespec-onward-reads-the-decisions-of-the-session`
>   - set: `{status: pending, purpose: "Whether guppi onward --plan judges a Case out by the decision lines of ledger.md and of every reply of the main agent in the transcript, each at the time of its record, so that a re-ratification with lines the ledger already held counts at every later reply of the session", method: "uv run pytest tests/test_onward.py; by hand at the first Case ratified again with unchanged decision lines in Plan Mode after the change, at the reply that closes the last line under Cases after a later message of the person: the transcript, ledger.md and the times of the files under cases/, recorded in the estimate line"}`
>   - change: `renamed; the Criterion, purpose and method replaced — the decision lines of every reply of the transcript count, not only those of the stretch (case 604)`
> - [ ] `guppi/onward.py`: the replies whose decision lines count are every `assistant` record of `transcript_records` of `guppi/ledger.py`, each at its `moment`, not the records of `stretch`. `spent` and `told` are unchanged. The module docstring and the docstrings of the changed functions say so, with case 604.
> - [ ] `tests/test_onward.py`: a Case whose ratifying reply stands before the person's last message in the transcript, its file written before that reply and after its line in `ledger.md`, is not out and the hook exits 2. The existing tests of the stretch replies stay green.
> - [ ] `uv run pytest tests/test_onward.py tests/test_ledger.py`
> - [ ] read `estimate-prespec-onward-reads-the-decisions-of-the-session`

> **ratification:**
> ```
> - decision[case 604][update][rule-prespec-onward]{ref:rule-prespec-onward}
> - decision[case 604][update][estimate-prespec-onward-reads-the-decisions-of-the-stretch]{ref:rule-prespec-onward}
> ```
