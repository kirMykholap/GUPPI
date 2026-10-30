## Case 913 — The librarian's report gives each part its frame sends to it, with no limit of lines

> **context:**
> At the end of its run the librarian returns a short report, and `/handoff` or `/box` shows it to the person unchanged. The Render of `rule-close` in `.claude/agents/librarian-guppi.md` lists what the report gives, caps it at twenty lines and ends with "Nothing else". `estimate-close-reports-in-twenty-lines` checks the counts, the flags, the lint total and the twenty lines. Its reading at the start of this session was `failed` on the numbers 15, 25 and 12. `case-guppi` read the report at its source, the last message of the saved chat of the previous session (`7f200512-38a4-43be-9723-2cbf3756ed67.jsonl`, the message after the librarian's hand-back). That report gives 24 pages created, 23 updated, the `incomplete` mark of Case 905, a Flags list with the stale defer of `rule-clean-branch`, a lint of 11 lines and 19 lines in all. A Grep `12 lines|\(15\)|\(25\)` over that chat printed nothing, and the person then said they had looked at another report; the main agent writes the new reading before this Case is ratified. `brief.md` gives 23 created while its own list adds up to 24; the main agent records that as a lesson line (Q2). The report's own rule is still at fault. Other steps of the same frame send more to the report: each Grep of the index check with the number of lines it printed, each page opened for a duplicate, a cluster or a script error, the one read of `ledger.md`, a refused instruction or call, and what `guppi archive` moved or kept. So "Nothing else" is false beside them. Three Estimates set those parts, and the pointer of the new list to them leaves each Criterion true, so each stands: `estimate-index-check-merges` (each Grep and its number of lines, each page opened), `estimate-synthesis-clusters` (each page opened at the synthesis) and `estimate-documentation-completes` (each page opened, the read of `ledger.md`, the units of `guppi archive`, a refused call, a refused instruction of the handoff). `estimate-spec-box-runs-a-conserved-spec` says that `/box` shows the librarian's report unchanged with the exit code of `uv run --project .guppi guppi test`. That exit code is a line `/box` adds beside the report, not a part of the report, so that Criterion stands, and the new `then` says so. The report also held a `Tests` line and a list of files, which no step asks for. The person chose to drop the twenty-line limit, since they see no point in it. This Case rewrites the list of `rule-close`: the report gives the parts the list names and each part that another step of the frame sends to it, holds no test result and no list of files, and has no limit of lines. It replaces the Criterion, the `purpose` and the `method` of the Estimate, since all three state the old promise. The old line on the counts, the flags and the lint total is not carried word for word: the first line of the new `then` names those parts and the marks and archived pages beside them. The old line on twenty lines or fewer is dropped, as the person chose. The Case also renames the Estimate `estimate-close-reports-the-run`; a Glob `vault/**/estimate-close-reports-the-run*.md` printed nothing, so the slug is free. `estimate-close-commits`, the other Estimate of `rule-close`, speaks of the commit, not of the report, so its Criterion stands. The failure of the commit command that the report names is a Frontier item of its own (Q4). The librarian applies the ledger entries in their order (`apply` in `.guppi/guppi/generate.py`), and `Vault.estimate` there replaces the status and the Result of the page. So the new reading, written before this Case's decision lines, lands on the old Criterion before this update sets the page `pending`. The `method` waits for a librarian's run that starts with the new Render. The run of this session starts with the old one, since its render step comes later, so Retro leaves the Estimate `pending`. A Grep `twenty` (case-insensitive) over `vault/wiki/` and `.claude/` printed `brief.md`, `log.md`, `rules/rule-close.md`, `estimates/estimate-close-reports-in-twenty-lines.md`, `estimates/estimate-close-commits.md` and `.claude/agents/librarian-guppi.md`. brief.md and log.md are not read. In `estimate-close-commits.md` the word stands only in the slug on a History line. The other three are the texts this Case changes. A Grep of the slug `estimate-close-reports-in-twenty-lines` over the repository outside `vault/raw/` printed `vault/wiki/brief.md`, `vault/wiki/log.md`, `vault/wiki/rules/rule-close.md` and `vault/wiki/estimates/estimate-close-commits.md`. The hit in `estimate-close-commits.md` is a History line, brief.md and log.md are not read, and the rename takes the `estimates` link of `rule-close`. A Grep `librarian-guppi\.md|"librarian-guppi"|'librarian-guppi'` over `.guppi/tests/` printed `test_grepguard.py`, which names the agent type and reads no file. `rule-close` has `core: true`, and the live build test of `.guppi/tests/test_ship.py` judges its pointers, so the new sentence keeps its pointer in a bracket at its end.

> **problem:**
> The report of the librarian follows a list in `rule-close` that the other steps of its own frame contradict. That list ends with "Nothing else" and a twenty-line limit, while those steps send more parts to the report. The report then adds parts that no step asks for, such as test results and a list of files. The Estimate that checks the report checks neither those parts nor their absence.

> **recommend:**
> - **What the reading of the report stands on**
>   - Recommended: (a) a new reading from the report as shown, written by the main agent; no Case for it.
>   - Answer: agreed, (a); the person then said they had looked at another report.
> - **The created count in the brief**
>   - Recommended: (a) an error lesson line by the main agent; this Case changes nothing for it.
>   - Answer: agreed, (a).
> - **What the report may hold beyond the list of `rule-close`**
>   - Recommended: (a) Case 913 rewrites the list: the counts, the marks, the archived pages, the flags, the lint total and each read and refusal another step sends to the report; no test results and no list of files.
>   - Answer: agreed, (a).
> - **The commit command that failed once**
>   - Recommended: (a) a new Frontier item on `estimate-close-commits`; Case 913 does not cover it.
>   - Answer: agreed, (a).
> - **How the new list is checked**
>   - Recommended: (a) replace the Criterion and the purpose of `estimate-close-reports-in-twenty-lines`; it goes back to `pending`.
>   - Answer: agreed, (a).
> - **The twenty-line limit**
>   - Recommended: (a) keep twenty lines.
>   - Answer: (b) drop the limit; the person sees no point in it.
> - **How the list names the other parts**
>   - Recommended: (a) one pointer to the other steps of the frame.
>   - Answer: agreed, (a).
> - **The name of the Estimate, now that the limit is gone**
>   - Recommended: (a) rename it to `estimate-close-reports-the-run`.
>   - Answer: (a).
> - **Change**
>   - Asked: the person agreed with the fix of a pre-spec finding: name `estimate-spec-box-runs-a-conserved-spec`, and say that the exit code of the tests that `/box` shows is a line of its own beside the report, not a part of the report.
>   - Taken: `given` names that Estimate, `then` gains a `－` line on the exit code, the `method` leaves that line out of the report, and `context` says why that Criterion stands.
> - **Change**
>   - Asked: the person agreed with the fix of a pre-spec finding: name the Estimates that set the parts other steps send to the report, and add the Greps of the index check to the list of those parts.
>   - Taken: `context` names `estimate-index-check-merges`, `estimate-synthesis-clusters` and `estimate-documentation-completes` as covered by the pointer of the new list and says why each stands, and its list of parts adds each Grep of the index check with its number of lines.

> **given:**
> `rule-close`: the rule whose Render lists what the librarian's report gives.
> **＋** `.claude/agents/librarian-guppi.md`: the frame of the librarian, where that Render stands beside the steps that send parts to the report.
> **＋** `estimate-close-reports-in-twenty-lines`: its Criterion, purpose and method are replaced, and it is renamed `estimate-close-reports-the-run`.
> **＋** `.claude/skills/handoff/SKILL.md`: dispatches the librarian and shows its report unchanged.
> **＋** `.claude/skills/box/SKILL.md`: dispatches the librarian and shows its report in a session that `/box` runs.
> **＋** `estimate-spec-box-runs-a-conserved-spec`: sets the exit code of the tests that `/box` shows beside the report.

> **when:**
> The librarian's run that `/handoff` of `.claude/skills/handoff/SKILL.md` dispatches ends, and `/handoff` shows its report to the person.
> **＋** In a session that `/box` runs, `/box` of `.claude/skills/box/SKILL.md` dispatches that run and shows its report to the person instead.

> **then:**
> The report gives the pages created and updated per category, the entries marked incomplete or failed, the pages archived, the flags the run raised and the lint total.
> **＋** The report gives each part that another step of `.claude/agents/librarian-guppi.md` sends to the report.
> **－** The report holds no test result and no list of files.
> **－** No limit of lines binds the report.
> **－** The exit code of `uv run --project .guppi guppi test` that `/box` shows beside the report is a line of `/box`, not a part of the report.

> **tasks:**
> - [ ] update `rule-close`
>   - old: `Then return a report of at most twenty lines: pages created and updated per category, entries marked incomplete or failed, pages archived, the flags you raised, the lint total. Nothing else.`
>   - new: `Then return a report: pages created and updated per category, entries marked incomplete or failed, pages archived, the flags you raised, the lint total, and each part that another step of this frame sends to the report. Nothing else: no test result and no list of files (as set in case 913).`
>   - change: `the report gives each part another step of the frame sends to it, no test result and no list of files, and has no limit of lines`
> - [ ] update `estimate-close-reports-in-twenty-lines`
>   - set:
>     ```
>     status: pending
>     purpose: "Whether the librarian's report, as /handoff or /box shows it, gives the counts, the marks, the archived pages, the flags, the lint total and each part another step of its frame sends to it, with no test result and no list of files"
>     method: "by hand, after a librarian's run whose .claude/agents/librarian-guppi.md, when the run starts, holds the Render of rule-close with no limit of lines: the person's answer on whether the report that /handoff, or /box in a session that /box runs, showed after that run gave each part the Criterion names and no test result and no list of files, the exit code of guppi test that /box adds beside the report not counted as a part of it"
>     ```
>   - rename: `estimate-close-reports-the-run`
>   - change: `the Criterion replaced whole — the report gives each part its frame sends to it, no test result and no list of files, and has no limit of lines; renamed from estimate-close-reports-in-twenty-lines`
> - [ ] `uv run --project .guppi guppi render`: `.claude/agents/librarian-guppi.md`
> - [ ] read `estimate-close-reports-the-run`

> **ratification:**
> ```
> - decision[case 913][update][rule-close]{ref:rule-close}
> - decision[case 913][update][estimate-close-reports-in-twenty-lines]{ref:rule-close}
> ```
