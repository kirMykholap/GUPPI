# Handoff — 2026-10-30, the items of the brief of 2341 and four Insights of the backlog

## Notes from memory

- The person took the four backlog Insights onto the Frontier in one answer and agreed with every recommendation; Cases 923–926 were built as one batch.
- The first `/pre-spec` sent Cases 921–926 back on 11 findings of `ask-guppi` and 5 lines of the check; all were confirmed closed and ratified again. Cases 924 and 926 were ratified a third time after their new `method` texts named the Render by a case number outside a bracket.
- The `estimate-hi-takes-its-readings` Criterion of Case 921 says that only two steps open pages; the new Render states each of the two steps, not one sentence that says "only two". The reading passed on that.
- Case 925.1: the Read refusal of `ask-guppi` works only after this run renders `.claude/settings.json`; until then `grepguard` runs on `Grep` alone, so only the Grep refusal is live.

## Direct instructions to the librarian

- `rule-clean-branch` takes two updates: the `replace` pair of Case 919.2, and the `update` of Case 920.5 that carries `{supersedes:case 893.1}` and changes no text; after the run `rule-clean-branch` holds no `deferred_by`, and `decision-case-893.1` stands `superseded`.
- `rule-case-build` takes two `replace` pairs, of Cases 924 and 926, on two different sentences; render `.claude/agents/case-guppi.md` once both are applied.
- Three Insights are set `actioned` with `addressed_by`: `insight-orchestration-writes-from-its-own-reading` (`decision-case-923`), `insight-case-build-changes-a-step-without-reading-its-readers` (`decision-case-924`), `insight-case-build-claims-what-code-does-without-reading-it` (`decision-case-926`); `insight-ask-guppi-reads-a-decision-outside-its-frame` by Case 925.1 (`decision-case-925.1`).
- `rule-hook-registry` registers `guppi grepguard` on `PreToolUse` of `Read` beside `pageread`; check the rendered `.claude/settings.json` holds both hooks under the `Read` matcher.
- `estimate-clean-branch-code-holds-pointers-only-in-brackets` takes the `update` of Case 919.1 (`pending`) and then its reading of this Retro (`passed`), in that order.

## What actually got done

- Cases ratified: 919 (919.1, 919.2), 920 (920.1–920.5), 921, 922, 923, 924, 925 (925.1–925.6), 926. Frontier item C1 was put off as an item of the sprint, with no Case.
- Code: `.guppi/guppi/grepguard.py` — `before` runs on `Read` and `Grep`, and refuses by `permissionDecision: deny` a `Read` or a `Grep` of `ask-guppi` whose path is `vault/wiki/decisions/` or lies in it, the reason naming the path and `rule-search-leaves-out-decisions`; every other call keeps its behaviour, and the module docstring says so.
- Tests: `.guppi/tests/test_grepguard.py` — the refusals for `ask-guppi`, the same calls of `case-guppi`, the librarian and no `agent_type` unchanged, a `Read` of `ask-guppi` outside the folder unchanged, a `Grep` of `ask-guppi` over the wiki still excluded; `.guppi/tests/test_ship.py` — `live_code_lines` and two `live_code` tests with no mark `live`; `.guppi/tests/test_render.py` — the docstring of the `--paths` test holds its pointer in a bracket at the end.
- `uv run --project .guppi guppi test`: 1803 passed, 6 skipped, 1 deselected. `uv run --project .guppi guppi style`: clean.
- Readings: L1 and L2 at `/hi`; seven at Retro, all `passed`: `estimate-clean-branch-code-holds-pointers-only-in-brackets`, `estimate-clean-branch-tests-judge-the-live-code`, `estimate-compact-recall-reloads`, `estimate-hi-takes-its-readings`, `estimate-ratification-case-id-carries-the-sprint`, `estimate-search-leaves-out-decisions-by-the-grep-hook`, `estimate-page-read-cuts-the-history`. No lesson.

## Debt

- No box is debt; no test was reverted.
- 54 boxes of `spec.md` wait for the librarian: page, render and `read` lines.
- `estimate-ask-query-before-a-create` — after a Case whose `case-guppi` proposes a `create` without a `ref`.
- `estimate-synthesis-keeps-actioned-by-the-mark` — after a librarian's run that puts a lesson with `addressed_by` under an Insight that stands `actioned`.
- `estimate-synthesis-clusters` — after a librarian's run whose `materialize.yaml` holds at least two lesson entries.
- `estimate-orchestration-states-a-subagent-fact-from-its-transcript` — after the first reply of the main agent under the new Render of `rule-orchestration` that states what a subagent did.
- `estimate-case-build-reads-the-readers-of-a-changed-step` — after the `/pre-spec` of the first session whose `case-guppi` runs on the Render of `rule-case-build` that holds the sentence on the readers of a changed step.
- `estimate-case-build-reads-the-code-it-states` — after a `/pre-spec` of a session whose Cases `case-guppi` built on the Render of `rule-case-build` this run renders.
- `estimate-search-leaves-out-decisions-refuses-ask-guppi` — after the first `/pre-spec` once this run has rendered `.claude/settings.json`; its pytest part passed at Retro.
- `estimate-search-leaves-out-decisions-in-every-agent` — after a session that runs on the rendered `.claude/rules/search-leaves-out-decisions.md` and `.claude/agents/ask-guppi.md`.
- `estimate-ask-opens-a-decision-only-for-a-finding` — after a `/pre-spec` whose `ask-guppi` runs on the rendered `.claude/agents/ask-guppi.md`.
- `estimate-ask-finds` — after a `/pre-spec` whose `ask-guppi` runs on the rendered `.claude/agents/ask-guppi.md`.

## Observations

- Red before the work, in `## Baseline` of `work.md`: `guppi check` exit 1 — `backlog.md` differs from its sources, 9 pages with `core: true` stand `draft`, and `estimate-harness-make-runs-in-both-shells: method: the Makefile has no target with`. The tenth line, `ship: .guppi/tests/test_render.py:500`, is fixed by Case 919.1; `guppi ship --check` printed nothing at Retro.
- The `method` of `estimate-clean-branch-code-holds-pointers-only-in-brackets` asks for `guppi ship --review` into an empty folder, but while a page with `core: true` stands `draft` that command prints those pages, exits 1 and writes nothing; Retro ran it with `--allow-draft`. The `method` does not name the flag.
- The four C2 checks of the handoff of session 2341 — `estimate-permissions`, `estimate-orchestration-forwards-a-discussion-question`, `estimate-case-check-sends-back-a-faulty-case`, `estimate-case-example-passes-the-check` — were already rewritten in session 1930, after the reading that listed them, and stand `passed` on their new texts; Case 922 changes none of them.
- Case 920 replaces the Criterion of three Estimates of rules with `core: true` (`rule-synthesis`, `rule-ask`, `rule-compact-recall`), and their readings wait for events, so those rules are expected to stand `draft` after this run, beside the nine already there.

## For the next session

- The milestone item of the clean branch, `rule-clean-branch` with `estimate-sprint-plugin-ci-writes-a-clean-branch`, was put off again: the owner's push of `plugin` and a tag `prod-x.y.z`, and the reading of the CI run it starts.
- Whether the `method` of `estimate-clean-branch-code-holds-pointers-only-in-brackets` should name `--allow-draft` for `guppi ship --review`.

## Ask the person

- `estimate-guppi-package-is-ready-after-the-install` — needs the person — After the agent writes a clean copy by `guppi ship --allow-draft` in the repository of GUPPI, and you, at a stop of Work Mode, add it as a catalogue, install `guppi`, type `/guppi:install` in an empty project, reopen Claude Code and type `/hi`: did the output of the install, the order of its steps, the files of the project and its `.guppi/.venv/` match the Criterion?
