## Case 473 — A reader that runs before the page it reads: the red in Work Mode is a handoff note, a refusing reader keeps the old form

> **context:**
> Some Cases change two things at once: a reader in code, and the page or governed file it reads. The reader runs from the working tree as soon as the code is written. The page lands only at the librarian's run, and the governed file at the render in that run. Between those two moments the reader refuses or goes red, and this happens by construction. Two lessons record it. After case 111.3, the Stop hook of session M refused 13 ledger lines: the reader required a stamped `hi`, and the writer of stamped lines reached `.claude/settings.json` only with the next render. That loss was stopped by the 111.6 fallback, which case 136.3 removed once the writer was live. After cases 227 and 229.1, `make lint` was red on the sprint step until the librarian's run.
> `insight-workflow-code-live-before-the-page-it-reads` is `open`, severity 2, and case 238 defers it. Its Proposal is one sentence in `rule-work-mode`. That rule is a `draft` with only a `Purpose`, and 20 Cases defer it. Naming it would take up the whole rule (case 467). So the person chose `rule-retro` for the red half, for now, and will review where it belongs when `rule-work-mode` is taken up. The person chose `rule-case-build` for the fallback half, because `case-guppi` builds every Case and reads its frame.
> The frame. The Render of `rule-retro` already says "Do not run `make lint` here" and "Red tests: fix now … the handoff still needs green". The new sentence leaves tests under that rule. `make lint` runs `render --check`, `sprint --check`, `backlog --check`, `glossary --check` and `guppi lint`. The librarian runs it after the render. A note for the handoff is already one of the four ends of a frontier item, and `rule-handoff` already writes such a note as the end of its item, so `rule-handoff` is not changed. `estimate-retro-loads` promises the readings. `estimate-retro-report-holds-each-fact-once` promises the form of the report, and its frontier already holds "what the agent noticed during Work Mode". Neither Estimate is touched. `estimate-case-build-writes-the-case` promises that `case-guppi` reads the frame and fixes each contradiction, and that stays true. The fallback is a promise of its own, on a new Estimate. Both `create` lines carry a `ref`, so no vault query was run. A Glob of `vault/**/` finds no page for either new slug.
> Not done: `rule-work-mode` stays in the backlog as it is, and no rule about tests changes.

> **problem:**
> No text says that a check which reads a page or a file the same Spec updates is expected to be red in Work Mode, so its red is taken for a finding or for debt. No text asks the author of a Case to keep a refusing reader working until its new writer is live, so a write that is refused in the gap is lost.

> **recommend:**
> Two sub-cases, one promise each. 473.1 adds a sentence to the Render of `rule-retro`: such a red, or such a refusal, is a frontier item that ends as a note for the handoff, not debt, and a red test stays under the green rule. 473.2 adds a sentence to the Render of `rule-case-build`: where the reader refuses in the gap and what it refuses is lost, the Case keeps the old form until the writer is measured live, and a later Case removes it. 473.2 also sets the Insight `actioned` and retires case 238. The rejected option was to write both halves in `rule-work-mode`, which would take up that whole rule and its 20 defers.

### Case 473.1 — A check red before the librarian's run is a note for the handoff

> **given:**
> `rule-retro` — its Render, the paragraph that keeps `make lint` out of Retro
> **＋** `.claude/skills/retro/SKILL.md` — the skill rendered from `rule-retro`
> **＋** `make lint` — the checks of the vault, which the librarian runs after the render
> **＋** `rule-handoff` — writes a note for the handoff as the end of its item, unchanged
> **＋** `estimate-retro-report-holds-each-fact-once` — the promise of the form of the report, unchanged
> **＋** `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` — the new promise

> **when:**
> The person invokes `/retro` in a session whose Spec updates a page or a governed file, and in Work Mode `make lint`, one of its steps, or a hook of the working tree that reads that page or file went red or refused.

> **then:**
> The red or the refusal is an item of the frontier, and it ends as a note for the handoff that names the check and the page or file it waits for.
> **＋** The reading of the check that counts is the `make lint` of the librarian's run, after the page is written and the file rendered.
> **－** The red is not debt: the agent does not fix it or revert it into a patch.
> **－** A red test is not such a check: it is fixed or reverted into a patch, and the handoff still needs green.

> **tasks:**
> - [ ] update `rule-retro`
>   - old: `` Do not run `make lint` here: the vault is written after handoff, by the librarian. ``
>   - new: `` Do not run `make lint` here: the vault is written after handoff, by the librarian. A check that reads a page or a governed file this session's Spec updates — `make lint` or one of its steps, or a hook of the working tree — is red or refuses in Work Mode until the librarian's run writes the page or renders the file, and the `make lint` of that run is its reading: such a red is an item of the frontier that ends as a note for the handoff, naming the check and the page or file it waits for, and it is not debt. A red test is not such a check: it is fixed or reverted as above (case 473.1). ``
>   - change: `a check red in Work Mode because it reads a page or a file the same Spec updates is a note for the handoff, not debt; a red test stays under the green rule (case 473.1)`
> - [ ] create `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note`
>   - type: `estimate`
>   - ref: `rule-retro`
>   - kind: `QA`
>   - purpose: `Whether a check red in Work Mode because it reads a page or a governed file the same Spec updates ends at Retro as a note for the handoff, not as debt, while a red test is still fixed or reverted`
>   - method: `one reading by hand at the first /retro after the render in a session whose Spec updates a page or a governed file that make lint reads, recorded in the estimate line`
>   - tags: `[session, workflow, harness]`
> - [ ] `uv run guppi render`: `.claude/skills/retro/SKILL.md`
> - [ ] read `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` — by hand, at the first such `/retro` after the render

> **ratification:**
> ```
> - decision[case 473.1][update][rule-retro]{ref:rule-retro}
> - decision[case 473.1][create][estimate-retro-red-check-of-an-updated-page-is-a-handoff-note]{ref:rule-retro}{tags:session,workflow,harness}
> ```

### Case 473.2 — A reader that loses what it refuses keeps the old form until its writer is live

> **given:**
> `rule-case-build` — its Render, the paragraph on the frame of a Case
> **＋** `.claude/agents/case-guppi.md` — the agent rendered from `rule-case-build`
> **＋** `estimate-case-build-writes-the-case` — the promise that the frame is read and each contradiction fixed, unchanged
> **＋** `rule-retro` — the note for the handoff that a reader which only goes red gets, by 473.1
> **＋** `insight-workflow-code-live-before-the-page-it-reads` — the Insight this Case actions
> **＋** `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` — the new promise

> **when:**
> `case-guppi` builds a Case that changes a reader in code and the text or the writer that reader reads, where the reader runs from the working tree at once and the text lands at the librarian's run or the render.

> **then:**
> Where the reader refuses in between and what it refuses is lost, such as a hook that refuses a ledger line, the `then` of the Case says that the reader accepts the old form beside the new one until a reading of the writer passes live.
> **＋** The removal of the old form is left to a Case of a later session, after that reading.
> **－** A reader that only goes red, such as `make lint`, keeps no old form: its red is a note for the handoff by `rule-retro`.
> **－** `insight-workflow-code-live-before-the-page-it-reads` stands `actioned` with `addressed_by: decision-case-473.2` and leaves the backlog.

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `` Fix each in the Case, or say in `context` why it stands. ``
>   - new: `` Fix each in the Case, or say in `context` why it stands. When the Case changes a reader in code and the text or the writer it reads, the reader runs from the working tree at once and the text lands at the librarian's run or the render; where the reader refuses in between and what it refuses is lost — a hook that refuses a ledger line — `then` says that the reader accepts the old form beside the new one until a reading of the writer passes live, and a Case of a later session removes the old form (cases 111.6, 136.3, 473.2). A reader that only goes red, such as `make lint`, keeps no old form: its red is a note for the handoff by `rule-retro`. ``
>   - change: `a reader that loses what it refuses before its writer lands keeps the old form until the writer is measured live (case 473.2)`
> - [ ] update `insight-workflow-code-live-before-the-page-it-reads`
>   - set: `{status: actioned, addressed_by: decision-case-473.2}`
>   - change: `actioned: the red of a check before the librarian's run is a note for the handoff in rule-retro (case 473.1); a reader that loses what it refuses keeps the old form until its writer is measured live, in rule-case-build (case 473.2); the defer of case 238 retired`
> - [ ] create `estimate-case-build-keeps-the-old-form-until-the-writer-is-live`
>   - type: `estimate`
>   - ref: `rule-case-build`
>   - kind: `QA`
>   - purpose: `Whether a Case that changes a reader and the text it reads, where the reader loses what it refuses before the text lands, keeps the old form in its then until the writer is measured live`
>   - method: `one reading by hand at the first Case case-guppi builds after the render that changes a reader and the text or writer it reads, recorded in the estimate line`
>   - tags: `[session, workflow, harness]`
> - [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
> - [ ] read `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` — by hand, at the first such Case after the render

> **ratification:**
> ```
> - decision[case 473.2][update][rule-case-build]{ref:rule-case-build}
> - decision[case 473.2][update][insight-workflow-code-live-before-the-page-it-reads]{ref:insight-workflow-code-live-before-the-page-it-reads}{supersedes:case 238}
> - decision[case 473.2][create][estimate-case-build-keeps-the-old-form-until-the-writer-is-live]{ref:rule-case-build}{tags:session,workflow,harness}
> ```
