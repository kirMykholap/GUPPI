# Handoff — 2026-10-02, rule-orchestration: the main agent's rules leave case-schema.md

## Notes from memory

- The person opened `rule-orchestration` with a narrower problem: the loop after the findings of `/pre-spec` sends fixes to `case-guppi` before the person has answered the report, so the chat moves on and rounds arrive mixed. `case-guppi` recommended a Case on `rule-prespec` alone; the person chose the whole move with the loop as one part.
- The person did not first see that the design has three files, not two: they read `ratification.md` as `case-schema.md` renamed. A `/wait-what` re-pitch settled it: `case-schema.md` keeps its name and goes to `case-guppi` alone, and `ratification.md` is a third, new file.
- The move of the checks departs from the wording ratified in case 561: the nine Estimates are renamed and moved by `rename`, not written again as new pages with the old ones withdrawn. The person agreed to that when `case-guppi` asked.
- The Case was ratified twice: once as first built (20 sub-cases), then again after `/pre-spec` (21 sub-cases, placeholders restored, `purpose` of `rule-case-protocol` reworded, 595.21 added).

## Direct instructions to the librarian

- Check first the nine renames of 595.8–595.16: each `update` carries `rename` and `set.target`; the `estimates` lists of `rule-orchestration` and `rule-ratification` name the old slugs and wait for the rename in the same run to rewrite them; `rule-case-protocol` keeps `estimate-case-protocol-loaded` and `estimate-case-protocol-case-form` only.
- `rule-orchestration` is a `create` over a placeholder with `deferred_by` 424 and 574; its line carries both `{supersedes:...}` blocks, so both defers should clear and the page leave `backlog.md`.
- `rule-atomicity` moves its parent from `rule-case-protocol` (set to `kind: Leaf`, `children: []`) to the new MOC `rule-ratification`; check `make lint` prints no orphan or `children` line on the three.
- The render writes three files from the pages — `vault/wiki/orchestration.md`, `vault/wiki/ratification.md`, `vault/wiki/case-schema.md` — and `.claude/skills/hi/SKILL.md`, `.claude/skills/pre-spec/SKILL.md`, `.claude/agents/case-guppi.md`; the language placeholders `{{chat_lang}}` and `{{documentation_lang}}` stand in the Renders of 595.2 and 595.6.
- The Spec holds the Case as built again after `/pre-spec`; the ledger holds the decision lines of the first ratification and 595.21 from the second, no line twice.

## What actually got done

- Ratified: 595.1–595.21 (ledger lines 1–31).
- Code: `guppi/ledger.py` (the refusal message names `ratification.md`), `guppi/prespec.py` (a comment), `tests/test_ledger.py` (the asserted message).
- `make test`: 1074 passed, 6 skipped. `make style`: clean.
- Readings, all `passed`: ledger lines 32–39 — `estimate-estimates-schema-checked`, `estimate-materialize-changes-a-named-part-alone`, `estimate-materialize-lifts-when-and-then`, `estimate-language-spec-prose-in-english`, `estimate-case-check-refuses-a-letter-outside-the-script`, `estimate-ledger-write-names-the-kind-of-a-user-record`, `estimate-spec-box-refuses-a-stale-spec`, `estimate-case-check-shows-only-the-checked-case`.
- Lesson: ledger line 40, `lesson-case-showing-ratification-fence-outside-the-blockquote`.

## Debt

- No box of code, test or command is left unticked; no patch.
- Boxes that wait for the librarian: 58.
- `read` lines whose slug this session creates or updates: `estimate-prespec-gathers-the-answers-after-findings`, `estimate-orchestration-loaded`, `estimate-ratification-loaded`, `estimate-internal-context-loaded`, `estimate-atomicity-rendered`, `estimate-case-protocol-loaded`, `estimate-case-build-writes-the-case`, `estimate-orchestration-acknowledging-reply`, `estimate-orchestration-shows-the-frontier-after-a-closed-line`, `estimate-orchestration-defers-in-one-reply`, `estimate-orchestration-shows-the-built-case`, `estimate-orchestration-forwards-a-discussion-question`, `estimate-orchestration-asks-in-the-grill-me-shape`, `estimate-orchestration-puts-the-harness-before-plan-mode`, `estimate-orchestration-names-related-cases-in-the-dispatch`, `estimate-ratification-ledger-line-form`, `estimate-ledger-write-refuses-a-line-it-cannot-read`, `estimate-spec-capture-offers-the-fork`, `estimate-skill-grill-me-asks-in-rounds`, `estimate-claude-md-rendered`.

## Observations

- Red before the work: `make lint` exit 2 at the Baseline, 46 lines of `guppi lint` (6 `deferred`, 40 `unread: pending`). No expected red: no task changed a check that reads a page this Spec updates.
- Until the librarian renders `vault/wiki/ratification.md`, the ledger hook's refusal names a file that does not exist yet.
- After the reply that rewrote the refused lesson line, the run stopped with no condition of `where-to-stop.md`: the hook of `rule-retro-onward` had already sent the agent on once in the stretch and stayed silent, and the agent did not go on to the commit and `/handoff` by itself; the person asked, and the run went on.
- The first lesson line was refused by the ledger hook for a slug without the prefix `lesson-`; written again with it.
- The `method` of `estimate-ledger-write-names-the-kind-of-a-user-record` expects its Grep to print `guppi/ledger.py` alone; it also prints `guppi/casecheck.py`, whose hits are docstring lines only. The method is wider than its Criterion.
- The harness marked two answers of `case-guppi` as instruction-shaped (pattern `settings-json`); the match was `.claude/settings.json` named in the `given` of 595.7.
- Readings left open, their moment not come: `estimate-lint-runs-every-step` (no red backlog step at this Baseline), `estimate-case-check-refuses-text-before-a-round` (no round came after `/pre-spec`), `estimate-case-check-requires-each-question-of-the-rounds`, `estimate-plan-mode-verified` (no duplicate `create` to flag), `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` (no Expected red), `estimate-retro-runs-on-to-the-handoff` and `estimate-handoff-holds-each-fact-once` (read after this run), `estimate-ledger-write-lifts`, `estimate-retro-onward-sends-the-agent-to-the-handoff`, the `/box` and `/carry` readings, `estimate-ask-finds`, `estimate-compact-recall-reloads`, `estimate-event-log-records`, `estimate-generate-rewords`, `estimate-session-start-context`, `estimate-spec-write-reaches-the-approved-spec`, `estimate-synthesis-clusters` and the three of `entity-sprint-migration`.

## For the next session

- The close of the sprint (Slice 5) is put off again as a sprint item.
- Whether `rule-retro-onward` should send the agent on again after a reply that answers a refusal of the ledger hook at the end of Retro, or the stop seen in this session needs a rule of its own.

## Ask the person

- `estimate-context-size-shown-after-each-reply` — needs the person — after each reply of the agent in the VS Code chat, do you see one line `context: <N> tokens (<+D> since the last reply)`?
