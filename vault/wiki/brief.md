# Brief — 2026-10-02, session 1834: rule-orchestration, the main agent's rules leave case-schema.md

## Where things stand

- Ratified (handoff): 595.1–595.21 (ledger lines 1–31). The Case was ratified twice, the second time after `/pre-spec` (21 sub-cases, 595.21 added).
- Code (handoff): `guppi/ledger.py` (the refusal message names `ratification.md`), `guppi/prespec.py` (a comment), `tests/test_ledger.py` (the asserted message). `make test` 1074 passed, 6 skipped; `make style` clean.
- Readings (handoff): ledger lines 32–39, all `passed` — `estimate-estimates-schema-checked`, `estimate-materialize-changes-a-named-part-alone`, `estimate-materialize-lifts-when-and-then`, `estimate-language-spec-prose-in-english`, `estimate-case-check-refuses-a-letter-outside-the-script`, `estimate-ledger-write-names-the-kind-of-a-user-record`, `estimate-spec-box-refuses-a-stale-spec`, `estimate-case-check-shows-only-the-checked-case`. Lesson: ledger line 40, `lesson-case-showing-ratification-fence-outside-the-blockquote`.
- Yaml: `raw/2026-10-02/1834/materialize.yaml`, 40 entries from `materialize` (31 decision lines — 4 `create`, 27 `update`; 8 `estimate`; 1 `lesson`), plus 2 added by the synthesis. 42 entries `applied`; 0 `failed`; 2 `incomplete`; `unparsed` empty. The ledger has 40 lines, each held by an entry of the yaml (lines 1 to 40). `raw/2026-10-02/1202/materialize.yaml` extended with 0 entries and not changed by this run.
- Handoff check: the nine `update` entries of 595.8–595.16 each carry `rename` and `set.target`; `log.md` records each rename and each ref rewritten. `rule-orchestration` lists the eight `estimate-orchestration-*` Estimates and `estimate-orchestration-loaded`; `rule-ratification` lists `estimate-ratification-ledger-line-form` and `estimate-ratification-loaded`; `rule-case-protocol` lists `estimate-case-protocol-loaded` and `estimate-case-protocol-case-form` only. `rule-orchestration` was written "created over placeholder"; its `deferred_by` is gone, `decision-case-424` and `decision-case-574` are superseded by 595.2 and archived, and `backlog.md` no longer names it (25 → 24 items). `rule-ratification` is `kind: MOC` with `children: [rule-atomicity]`; `rule-atomicity` has `parent: rule-ratification`; `rule-case-protocol` is `kind: Leaf`, `children: []`; `make lint` printed no orphan or `children` line. The render wrote `vault/wiki/orchestration.md` and `vault/wiki/ratification.md` (new), `vault/wiki/case-schema.md`, `.claude/skills/hi/SKILL.md`, `.claude/skills/pre-spec/SKILL.md` and `.claude/agents/case-guppi.md`; the three wiki files hold no `{{`; `CLAUDE.md` and `guppi.toml` unchanged.
- Index check: two `create` outside `estimates`, `rule-orchestration` and `rule-ratification`. Grep `^(purpose|deferred_by):` over `vault/wiki/rules/`, 87 lines. `rule-orchestration`: the index line of the same slug is its placeholder, written over by design; marked `near: rule-case-protocol`. `rule-ratification`: marked `near: rule-case-protocol`. No merge.
- Synthesis: one lesson entry. Greps `^(root_cause|deferred_by):` over `vault/wiki/lessons/`, 75 lines, and `^(pattern|deferred_by):` over `vault/wiki/insights/`, 31 lines. The lesson joined `insight-workflow-case-schema-silent-on-what-the-scripts-accept` (status `open`, kept): an `update` of the Insight with the lesson added to `children`, and an `update` of the lesson to `status: clustered`.
- `generate`: 174 pages written or changed from the 1834 yaml, 0 from the 1202 yaml.
- Pages, decisions: 22 created (595, 595.1–595.21). 2 superseded and moved by `generate` and `cleanup` to `archive/migration/2026-10-02/1834/decisions/`: 424, 574. Earlier Decision pages changed by the ref rewrites of the renames.
- Pages, rules: 2 created (`rule-orchestration` over its placeholder, `rule-ratification`); 8 updated by Cases (`rule-prespec`, `rule-internal-context`, `rule-claude-md`, `rule-compact-recall`, `rule-atomicity`, `rule-case-protocol`, `rule-case-build`, `rule-ledger-write`); `rule-plan-mode` got the children `rule-orchestration` and `rule-ratification`. Cascade: `rule-atomicity`, `rule-claude-md`, `rule-internal-context`, `rule-prespec`, `rule-skill-grill-me` built → draft; `rule-estimates-schema`, `rule-language`, `rule-materialize` draft → built.
- Pages, estimates: 2 created (`estimate-orchestration-loaded`, `estimate-ratification-loaded`); 18 updated by Cases, 9 of them renamed; 8 readings, all `passed`.
- Pages, entities: 1 updated (`entity-glossary`, 595.20). Lessons: 1 created and clustered. Insights: 1 updated (`insight-workflow-case-schema-silent-on-what-the-scripts-accept`); `insight-case-build-promise-lines-compared-by-no-check` changed by a ref rewrite.
- `cleanup` moved 2 pages. `backlog.md` and `glossary.md` changed; `sprint.md` unchanged. The run ticked 38 boxes of `raw/2026-10-02/1834/spec.md` and 7 `read` boxes of `raw/2026-10-02/1202/spec.md`; `log.md` 105 lines added.
- Archive: `guppi archive` printed no line and moved nothing; it looks only at units dated before the day of the run, so `raw/2026-10-02/1202` and `raw/2026-10-02/1834`, the session of the run, stay. No Estimate whose `method` names the archive step is `pending`.

## Readings due

0 Estimates `failed`, 49 `pending` (the 49 `unread` lines of `make lint`). Every target named below stands `draft`. The `read` lines of `raw/2026-10-02/1834/spec.md` name no place, so each line gives the page's `method`.

- `estimate-prespec-gathers-the-answers-after-findings` — `rule-prespec` (draft) — method: by hand at the `/pre-spec` of a later session after the render whose report asks the person a question and sends findings to two or more `case-guppi`
- `estimate-orchestration-loaded` — `rule-orchestration` (draft) — method: `uv run guppi render --check`; by hand at the first `/hi` of a later session after the render, `orchestration.md` in the first turn's context, its paragraphs compared with `CLAUDE.md`, `case-schema.md` and `ratification.md`
- `estimate-ratification-loaded` — `rule-ratification` (draft) — method: `uv run guppi render --check`; by hand at the first `/hi` of a later session after the render, `ratification.md` in the first turn's context, its paragraphs compared with `CLAUDE.md`, `case-schema.md` and `orchestration.md`
- `estimate-internal-context-loaded` — `rule-internal-context` (draft) — method: one reading at the `/hi` of a session, by hand
- `estimate-atomicity-rendered` — `rule-atomicity` (draft) — method: `uv run guppi render --check` exit 0; the text between the markers of `ratification.md` read by hand after the librarian's render — this run: `guppi render --check` exit 0; `vault/wiki/ratification.md` written by the render, 2 lines naming `rule-atomicity`; `rule-ratification` `kind: MOC`, `children: [rule-atomicity]`; `make lint` printed no line on `rule-atomicity` or `rule-ratification`
- `estimate-case-protocol-loaded` — `rule-case-protocol` (draft) — method: `uv run guppi render --check`; by hand after the librarian's render, `case-schema.md`, `orchestration.md` and `ratification.md` compared paragraph by paragraph, and at the first `/hi` of a later session the first turn's context and the main agent's read calls — this run: `guppi render --check` exit 0; the render wrote `case-schema.md`, `orchestration.md` and `ratification.md`; `.claude/skills/hi/SKILL.md` holds no line naming `case-schema`
- `estimate-case-build-writes-the-case` — `rule-case-build` (draft) — method: by hand, live dispatches in a session after the render — one item with a fork, one Case with a `create` without a `ref`, one that changes a hook; tokens and seconds of each dispatch
- `estimate-orchestration-acknowledging-reply` — `rule-orchestration` (draft) — method: one reading by hand of the first acknowledging reply of a session
- `estimate-orchestration-shows-the-frontier-after-a-closed-line` — `rule-orchestration` (draft) — method: by hand in a later session, the first reply in Plan Mode after the first reply of `/hi` that closes a line of `frontier.md` with no ratification and no defer
- `estimate-orchestration-defers-in-one-reply` — `rule-orchestration` (draft) — method: by hand, the first defer the person asks for after the render that leaves no line under `## Cases` of `frontier.md` open
- `estimate-orchestration-shows-the-built-case` — `rule-orchestration` (draft) — method: by hand, the Cases of a session at its close, against the Agent, SendUserFile, Skill and SendMessage calls of the transcript
- `estimate-orchestration-forwards-a-discussion-question` — `rule-orchestration` (draft) — method: by hand in a later session, the first such question, the SendMessage call, the main agent's tool calls and the answer in the transcript
- `estimate-orchestration-asks-in-the-grill-me-shape` — `rule-orchestration` (draft) — method: by hand at the close of a later session, each question of the main agent's own read in the transcript
- `estimate-orchestration-puts-the-harness-before-plan-mode` — `rule-orchestration` (draft) — method: by hand at the close of a later session, the Agent, picker and ExitPlanMode calls of Plan Mode in the transcript
- `estimate-orchestration-names-related-cases-in-the-dispatch` — `rule-orchestration` (draft) — method: by hand at the close of a later session after the render, each Agent call to `case-guppi` read against the Cases ratified or shown before it
- `estimate-ratification-ledger-line-form` — `rule-ratification` (draft) — method: by hand, the ledger and the preview of the first session where a lesson and the Case that closes its cause stand together, and of the first Case that takes up a decision with more than one Case in its `deferred_by`
- `estimate-ledger-write-refuses-a-line-it-cannot-read` — `rule-ledger-write` (draft) — method: `uv run pytest tests/test_ledger.py`, piped payloads and a session ledger in a temp vault
- `estimate-spec-capture-offers-the-fork` — `rule-spec-capture` (draft) — method: `uv run pytest tests/test_spec.py -k 'fork or box'`; by hand, the first ExitPlanMode of a session after the render, and the first of a session that took a conserved Spec
- `estimate-skill-grill-me-asks-in-rounds` — `rule-skill-grill-me` (draft) — method: `uv run guppi render --check`; by hand, one round read in the chat in a session after the render
- `estimate-claude-md-rendered` — `rule-claude-md` (draft) — method: `uv run guppi render` and `guppi render --check` after the build, plus one reading of `CLAUDE.md` at the next session start, by hand
- `estimate-ask-finds` — `rule-ask` (draft) — method: by hand in a later session, three dispatches of `ask-guppi`, each read against the event log
- `estimate-carry-over-writes` — `rule-carry-over` (draft) — method: `uv run guppi render --check`; by hand, the first `/carry` after the fork of ExitPlanMode
- `estimate-case-check-refuses-text-before-a-round` — `rule-case-check` (draft) — method: `uv run pytest tests/test_casecheck.py -k round`; by hand in a later session, the first rounds of `case-guppi` shown before and after pre-spec
- `estimate-case-check-requires-each-question-of-the-rounds` — `rule-case-check` (draft) — method: `pytest tests/test_casecheck.py -k rounds` over a temp agent transcript; then by hand the first Case the hook sends back for a missing title
- `estimate-compact-recall-reloads` — `rule-compact-recall` (draft) — method: `pytest tests/test_recall.py` on a temp project; live, the first compaction of a working session, by hand
- `estimate-context-size-shown-after-each-reply` — `rule-context-size` (draft) — method: `uv run pytest tests/test_context.py`; the live reading by hand, the line after the replies of a session in the VS Code chat
- `estimate-end-of-work-order` — `rule-end-of-work` (draft) — method: `make test-end-of-work`, plus by hand at the close of a later session
- `estimate-event-log-records` — `rule-event-log` (draft) — method: pytest in `tests/test_event.py` and `tests/test_gate.py`; the git-ignore and timing readings once by hand; one `/hi` outside plan mode and one in it
- `estimate-generate-rewords` — `rule-page-generation` (draft) — method: `pytest tests/test_generate.py`; the live reading the librarian's run that applies the first reword — this run: the 1834 yaml holds 0 entries with `reword`; `generate` printed no `reworded` line
- `estimate-handoff-dispatches` — `rule-handoff` (draft) — method: by hand at the `/handoff` of a later session and of the first session that `/box` runs
- `estimate-handoff-holds-each-fact-once` — `rule-handoff` (draft) — method: one reading by hand at the first `/handoff` after the render, against the close of its Retro
- `estimate-hi-takes-a-conserved-spec` — `rule-skill-hi` (draft) — method: `uv run guppi render --check`; by hand, at the first session whose person takes a conserved Spec at the Frontier
- `estimate-ledger-write-lifts` — `rule-ledger-write` (draft) — method: pytest in `tests/test_ledger.py` and `tests/test_gate.py`; by hand once, the ledger of the first session whose reply that ends Retro follows a refusal of a Stop hook in the same stretch
- `estimate-lint-runs-every-step` — `rule-lint` (draft) — method: by hand, the `make lint` of the Baseline of the first `/work` of a later session whose backlog step is red
- `estimate-plan-mode-verified` — `rule-plan-mode` (draft) — method: `make test-plan-mode`; the flagging one live reading by hand
- `estimate-retro-loads` — `rule-retro` (draft) — method: one reading by hand at the first `/retro`, and one at the first `/retro` of a session that `/box` runs
- `estimate-retro-onward-sends-the-agent-to-the-handoff` — `rule-retro-onward` (draft) — method: `uv run pytest tests/test_onward.py`; by hand at the first end of Retro after the render that follows a refusal of another Stop hook in the same stretch
- `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` — `rule-retro` (draft) — method: by hand at the first `/retro` after the render in a session whose `work.md` names a check under Expected red
- `estimate-retro-runs-on-to-the-handoff` — `rule-retro` (draft) — method: by hand at the first run from `/work` to the librarian after the render
- `estimate-session-start-context` — `rule-session-start` (draft) — method: `make test-session-start`; by hand, one session opened without `/hi`, and the ledger of the next working session after its first ratification
- `estimate-spec-box-runs-a-conserved-spec` — `rule-spec-box` (draft) — method: `uv run guppi render --check`; by hand, the first session that takes a conserved Spec at the Frontier and runs it by `/box`
- `estimate-spec-write-reaches-the-approved-spec` — `rule-spec-write` (draft) — method: `uv run pytest tests/test_ratified.py -k approved_spec`; by hand, the first Case ratified in Work Mode after the change
- `estimate-sprint-migration-leftovers-gone` — `entity-sprint-migration` (draft) — method: one reading of the tree by hand at the close of the sprint
- `estimate-sprint-migration-lint-clean` — `entity-sprint-migration` (draft) — method: `make lint`, exit 0, or only unread lines on the Estimates of `entity-sprint-migration`
- `estimate-sprint-migration-merges` — `entity-sprint-migration` (draft) — method: `make test` on the last commit of `migration`, then `git log` of `main` after the merge
- `estimate-synthesis-clusters` — `rule-synthesis` (draft) — method: one reading by hand of the yaml and the report after a live librarian run whose yaml holds at least two lesson entries — this run: the 1834 yaml holds 1 lesson entry; the synthesis ran both Greps and added 2 entries marked `librarian: synthesis`
- `estimate-where-to-stop-stops-only-on-its-conditions` — `rule-where-to-stop` (draft) — method: by hand at the first run from `/work` to the librarian after the render, and at the first run of `/box`
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — `rule-work-mode` (draft) — method: `uv run guppi render --check`; by hand, in a session after the render, the first `/work` the agent calls at the fork, the first the person types and the first that `/box` calls
- `estimate-work-mode-takes-the-work-readings` — `rule-work-mode` (draft) — method: by hand at the first `/work` after the render and at the first `/work` that `/box` calls

## Flags

- `incomplete` (`type`): line 3 `rule-orchestration`, line 5 `rule-ratification`. Both pages stand with `type: rule` on disk.
- `near`: `rule-orchestration` near `rule-case-protocol`; `rule-ratification` near `rule-case-protocol` (the index line of `rule-case-protocol` before this run named acting before ratification and ratifying without the content in view).
- `failed`: none. `unparsed`: none. Failed Estimates: none.
- `materialize`, `generate`, `cleanup`, `render`, `sprint`, `backlog`, `glossary`, `archive`: no stderr line.
- MOC candidates: none printed. Contradictions: none found.
- Stale defers, from `make lint`: `rule-subagent-guppi` deferred 31 times since case 29; `rule-case-rebuild-cost` 2 times since case 566; `rule-complaint-becomes-a-lesson` 1 time since case 504; `rule-morph` 1 time since case 239; `rule-ledger-line-withdrawn-on-re-ratification` 1 time since case 594.
- `make lint` exit 2: `guppi lint` printed 54 lines — 5 `deferred`, 49 `unread: pending`; no other step printed a line.
- Handoff observation: the `method` of `estimate-ledger-write-names-the-kind-of-a-user-record` expects its Grep to print `guppi/ledger.py` alone; it also prints `guppi/casecheck.py`, docstring lines only. The method is wider than its Criterion.
- Handoff observation: the harness marked two answers of `case-guppi` as instruction-shaped (pattern `settings-json`); the match was `.claude/settings.json` named in the `given` of 595.7.
- Handoff observation: after the reply that rewrote the refused lesson line, the run stopped with no condition of `where-to-stop.md`; the person asked, and the run went on.
- Reads outside the frame's need: none.

## Next session

Cases
- The close of the sprint (Slice 5) is put off again as a sprint item (handoff, For the next session).
- Whether `rule-retro-onward` should send the agent on again after a reply that answers a refusal of the ledger hook at the end of Retro, or the stop seen in session 1834 needs a rule of its own (handoff, For the next session).

Work
- Reading `estimate-prespec-gathers-the-answers-after-findings`
- Reading `estimate-orchestration-loaded`
- Reading `estimate-ratification-loaded`
- Reading `estimate-internal-context-loaded`
- Reading `estimate-atomicity-rendered`
- Reading `estimate-case-protocol-loaded`
- Reading `estimate-case-build-writes-the-case`
- Reading `estimate-orchestration-acknowledging-reply`
- Reading `estimate-orchestration-shows-the-frontier-after-a-closed-line`
- Reading `estimate-orchestration-defers-in-one-reply`
- Reading `estimate-orchestration-shows-the-built-case`
- Reading `estimate-orchestration-forwards-a-discussion-question`
- Reading `estimate-orchestration-asks-in-the-grill-me-shape`
- Reading `estimate-orchestration-puts-the-harness-before-plan-mode`
- Reading `estimate-orchestration-names-related-cases-in-the-dispatch`
- Reading `estimate-ratification-ledger-line-form`
- Reading `estimate-ledger-write-refuses-a-line-it-cannot-read`
- Reading `estimate-spec-capture-offers-the-fork`
- Reading `estimate-skill-grill-me-asks-in-rounds`
- Reading `estimate-claude-md-rendered`
- Reading `estimate-ask-finds`
- Reading `estimate-carry-over-writes`
- Reading `estimate-case-check-refuses-text-before-a-round`
- Reading `estimate-case-check-requires-each-question-of-the-rounds`
- Reading `estimate-compact-recall-reloads`
- Reading `estimate-end-of-work-order`
- Reading `estimate-event-log-records`
- Reading `estimate-generate-rewords`
- Reading `estimate-handoff-dispatches`
- Reading `estimate-handoff-holds-each-fact-once`
- Reading `estimate-hi-takes-a-conserved-spec`
- Reading `estimate-ledger-write-lifts`
- Reading `estimate-lint-runs-every-step`
- Reading `estimate-plan-mode-verified`
- Reading `estimate-retro-loads`
- Reading `estimate-retro-onward-sends-the-agent-to-the-handoff`
- Reading `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note`
- Reading `estimate-retro-runs-on-to-the-handoff`
- Reading `estimate-session-start-context`
- Reading `estimate-spec-box-runs-a-conserved-spec`
- Reading `estimate-spec-write-reaches-the-approved-spec`
- Reading `estimate-sprint-migration-leftovers-gone`
- Reading `estimate-sprint-migration-lint-clean`
- Reading `estimate-sprint-migration-merges`
- Reading `estimate-synthesis-clusters`
- Reading `estimate-where-to-stop-stops-only-on-its-conditions`
- Reading `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`
- Reading `estimate-work-mode-takes-the-work-readings`
- Unticked box of `raw/2026-10-02/1202/spec.md` line 930: by hand, `make lint` after the librarian's run of session 1202 prints no `fence` line on `decision-case-13` — this run's `make lint` printed none.

Ask the person
- `estimate-context-size-shown-after-each-reply` — needs the person — after each reply of the agent in the VS Code chat, do you see one line `context: <N> tokens (<+D> since the last reply)`?

## Readings at the close

- `make test`: 1074 passed, 6 skipped.
- `make lint`: exit 2; 54 lines of `guppi lint` (5 `deferred`, 49 `unread`); no other step printed a line.
- Pages in `vault/wiki/`: decisions 975, rules 78, estimates 191, lessons 77, insights 30, entities 5. `vault/archive/`: 700 `.md` files after `guppi archive`.
