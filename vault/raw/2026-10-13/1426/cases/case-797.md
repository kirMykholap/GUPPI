## Case 797 — A Case is judged by the state at the moment its check or reading runs

> **context:**
> Every check of a Case file and of the Spec in Plan Mode runs the code as it stands before the Work Mode of the session changes it, and a page or a rendered file changes at the librarian's run or at the render, or earlier only by a one-off task by hand in Work Mode, such as the removal of a section that Case 796.1 makes. The instructions of `case-guppi` do not say this. So the agent can judge a Case by the state at the end of the session. `lesson-case-build-chose-a-key-its-own-session-adds` records one case: Case 787.2 used the key `drop` that Case 792 of the same session would add, and the check of the Case file refused it. `lesson-case-reading-moment-before-the-render-it-reads` has the same cause: the agent set a reading of Case 761 for a moment before the render of the file it reads. Both lessons are `clustered` under `insight-workflow-code-live-before-the-page-it-reads`, which stands `open` in the backlog.
>
> By the person's answers, Case 797.1 adds one sentence to the Render of `rule-case-build`. The sentence makes the agent judge each form a task writes, the moment of a reading and what that reading will find by the state at the moment the check or the reading runs. Where a Case needs a form that another Case of the same session adds, the agent asks the person in a round. The new Estimate `estimate-case-build-judges-by-the-state-at-the-moment` checks this, by hand, once such a Case comes. Its `method` waits for that event in the form of case 781. The insight stays `open`, because `lesson-prespec-preview-expected-before-generate-applies-the-readings` is about the main agent, and this Case does not touch the main agent.
>
> `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` is `passed`. Its last line says that the insight stands `actioned` and leaves the backlog, which has not been true since the synthesis of 2026-10-10 reopened it. Case 797.2 replaces that Criterion whole. The new Criterion copies each other line word for word and drops that line. The `purpose` of that Estimate does not name the insight, so it stands. Its `method`, a reading by hand at a Case that changes a reader and the text it reads, waits for that event but does not name it in the form of case 781, so `rule-retro` would want it read at this session's Retro, where no Case of this session fits. By the findings of `/pre-spec`, Case 797.2 sets the `method` anew in that form, with the same reading, so that Case 799 of this session counts it as waiting.
>
> The frame. The new sentence goes after the sentence on a reader that only goes red, in the paragraph on the frame of the Case. No sentence of `rule-case-build` says to judge by the end state of the session. The sentence on a reader that keeps the old form (case 473.2) covers a reader and its text that land at different moments, and the new sentence agrees with it. The other Estimates of `rule-case-build` speak of other behaviours, so their Criteria stand. Case 795 of this session changes `guppi/materialize.py` and `guppi/prespec.py`, not `rule-case-build`, and the check it changes runs at the same moment as before. A Grep `case-guppi\.md|rule-case-build` over `tests/` printed nothing, so no test reads the agent file or the page live. The new Estimate has a `ref`, so no vault query was run for it, and a Glob `vault/**/estimate-case-build-judges-by-the-state*` printed nothing, so the slug is free.

> **problem:**
> `case-guppi` can build a Case by the state at the end of the session: it can use a form that only the session's own Work Mode makes valid, or time a reading before the text it reads changes. A passed Estimate of `rule-case-build` also states that an open insight is closed.

> **recommend:**
> - **How wide should the new instruction to `case-guppi` be?**
>   - Recommended: (b) every judgment about a moment: the form a check reads, the moment of a reading and what it will find, judged by the state at that moment.
>   - Answer: agreed, (b).
> - **What should `case-guppi` do when a Case needs a form that another Case of the same session adds?**
>   - Recommended: (b) ask the person in a round, with the form the code accepts now as a possible recommended answer.
>   - Answer: agreed, (b).
> - **What should happen to the group page and to the out-of-date line about it?**
>   - Recommended: (a) remove the line from the Criterion of the Estimate and read it again; the insight stays open.
>   - Answer: agreed, (a).
> - **How should the new instruction be checked?**
>   - Recommended: (a) a new Estimate, read by hand when such a Case comes up.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: by the findings of `/pre-spec`, the new sentence names a one-off task by hand in Work Mode, such as the removal of a section in Case 796.1, as a way a page changes before the librarian's run; and the `method` of `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` names its event in the form of case 781.
>   - Taken: the sentence of Case 797.1 and `context` name such a task; Case 797.2 sets the `method` anew as `by hand, after` the first such Case, with the same reading.

### Case 797.1 — case-guppi judges a Case by the state at the moment its check or reading runs

> **given:**
> `rule-case-build`: its Render, `.claude/agents/case-guppi.md`, gains the sentence.
> **＋** `estimate-case-build-judges-by-the-state-at-the-moment`: the new check of the sentence.
> **＋** `rule-case-check`: the check of the Case file, which runs the code as it stands.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case whose task writes a form of an update or whose Estimate sets the moment of a reading, while another Case of the same session changes the code that judges that form or the page or file that reading reads.

> **then:**
> `case-guppi` judges the form, the moment of the reading and what the reading will find by the state of the code and the pages at the moment the check or the reading runs, not by the state at the end of the session.
> **＋** A task of the Case writes only a form of an update that the code accepts when the check of `rule-case-check` runs.
> **＋** Where the Case needs a form of an update that another Case of the same session adds, `case-guppi` asks the person in a round whether the Case uses a form the code accepts now or leaves that change to a Case of a later session.

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `` A reader that only goes red, such as `make lint`, keeps no old form: its red is a note for the handoff by `rule-retro`. ``
>   - new: `` A reader that only goes red, such as `make lint`, keeps no old form: its red is a note for the handoff by `rule-retro`. Each check of your file and of the Spec runs the code as it stands when it runs, in Plan Mode before the Work Mode of the session changes it, and a page or a rendered file changes at the librarian's run or the render, or earlier only by a one-off task by hand in Work Mode that a Case names: judge each form a task writes, the moment of a reading and what that reading will find by the state of the code and the pages at the moment the check or the reading runs, never by the state at the end of the session; where a Case needs a form of an update that another Case of the same session adds, ask in a round whether the Case uses a form the code accepts now or leaves that change to a Case of a later session (case 797.1). ``
>   - change: `case-guppi judges a Case by the state of the code and the pages at the moment its check or reading runs, and asks in a round when a Case needs a form another Case of the session adds (case 797.1)`
> - [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
> - [ ] create `estimate-case-build-judges-by-the-state-at-the-moment`
>   - ref: `rule-case-build`
>   - kind: `QA`
>   - purpose: `Whether case-guppi judges the forms, the moments of readings and what they will find by the state of the code and the pages at the moment the check or the reading runs, and asks the person when a Case needs a form another Case of the same session adds`
>   - method: `by hand, after case-guppi builds a Case whose form or reading depends on another Case of the same session: the Case file, or the round before it, read against the Criterion, recorded in the estimate line`
>   - tags: `[session, workflow, harness]`
> - [ ] read `estimate-case-build-judges-by-the-state-at-the-moment`

> **ratification:**
> ```
> - decision[case 797.1][update][rule-case-build]{ref:rule-case-build}
> - decision[case 797.1][create][estimate-case-build-judges-by-the-state-at-the-moment]{ref:rule-case-build}{tags:session,workflow,harness}
> ```

### Case 797.2 — The Criterion of the old-form Estimate no longer states the insight closed

> **given:**
> `estimate-case-build-keeps-the-old-form-until-the-writer-is-live`: its Criterion is replaced whole.
> **＋** `rule-case-build`: the rule whose Estimate it is.
> **＋** `rule-retro`: the rule whose handoff note takes the red of a reader that only goes red.

> **when:**
> `case-guppi` builds a Case that changes a reader in code and the text or the writer that reader reads, where the reader runs from the working tree at once and the text lands at the librarian's run or the render.

> **then:**
> Where the reader refuses in between and what it refuses is lost, such as a hook that refuses a ledger line, the `then` of the Case says that the reader accepts the old form beside the new one until a reading of the writer passes live.
> **＋** The removal of the old form is left to a Case of a later session, after that reading.
> **－** A reader that only goes red, such as `make lint`, keeps no old form: its red is a note for the handoff by `rule-retro`.

> **tasks:**
> - [ ] update `estimate-case-build-keeps-the-old-form-until-the-writer-is-live`
>   - set:
>     ```
>     status: pending
>     method: "by hand, after the first Case case-guppi builds that changes a reader in code and the text or the writer it reads: the then of that Case read against the Criterion, recorded in the estimate line"
>     ```
>   - change: `the Criterion replaced whole — the line that put the insight actioned is dropped, since the insight was reopened; the method names its event (case 797.2)`
> - [ ] read `estimate-case-build-keeps-the-old-form-until-the-writer-is-live`

> **ratification:**
> ```
> - decision[case 797.2][update][estimate-case-build-keeps-the-old-form-until-the-writer-is-live]{ref:rule-case-build}
> ```
