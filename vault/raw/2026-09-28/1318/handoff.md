# Handoff — 2026-09-28, session 1318: languages as settings, wait-what, Work Mode's /work

## Notes from memory

- The person rejected a check on the language of each chat reply ("count letters — nonsense") and chose to take the chat out of the promise instead. They want guppi usable by developers of other languages, so the language pair became settings; the questions at install stay with `rule-morph`.
- The person first read the placeholder as living in the output file; a before/after example (the placeholder stays in the `## Render` of the page, the output gets the name) answered it.
- On C5 the person asked whether a done-condition Estimate should be archived once its condition holds. Estimates have no status for that; the answer chosen was to keep it live until the close of the sprint, with a note in Slice 5 (478.2).
- On C6 the person chose to take up `rule-work-mode` with a minimum rather than defer it again; they plan a fuller Work Mode model later.
- The person asked why pre-spec always finds so many fixes. The agent's count of the ten findings: three were contradictions between sibling sub-cases of one Case, two were rules outside the frame case-guppi read, one a fact that went stale after ratification, three wordings, one a side effect on another page. The person liked the idea that case-guppi checks its own sub-cases before answering; it became the defer of Case 480.
- 19 of the 20 Decisions that 479.2 supersedes (cases 183 to 322) also defer `rule-subagent-guppi`. `generate` clears a defer only from the pages the superseding Case names, so those defers stay on `rule-subagent-guppi`, pointing at superseded Decisions. The person chose to leave them for the Case that takes that page up.
- Work Mode ran without `/work`: the skill is rendered only at this librarian's run. The baseline was taken by hand before the first change: branch `migration`, `make test` 856 passed, 2 skipped; `make lint` exit 2 with 98 findings; `make lint` after the work printed the same 98 lines.
- Git warned that `tests/test_spec.py` holds CRLF in the working copy and will get LF at the next touch.

## Direct instructions to the librarian

- `vault/wiki/rules/rule-render-harness.md` lost its `## How it works` section by the one-off migration of 476.1, done by hand in Work Mode; its text is now in the docstring of `guppi/render.py`. The `update` of 476.1 on that page carries only `set` and `change`; the missing section is intended, not a stray edit.
- Render order matters: `rule-guppi-config` (476.1) must exist before any Render with `{{documentation_lang}}` or `{{chat_lang}}` renders — 476.2, 476.4 and 477.2 hold them. The render reads the codes from the `## Render` of `rule-guppi-config`, not from `guppi.toml`. If `guppi render` stops with a placeholder error, the page of `rule-guppi-config` was not written first.
- `rule-case-build` gets three Cases (476.2, 477.1, 477.3), `rule-case-protocol` two (476.2, 477.3), `rule-retro` two (479.3, 479.4), `entity-sprint-migration` two (478.2, 479.2). The anchors were checked by pre-spec to hit once each in any order.
- 479.2 carries 20 `{supersedes:case N}` blocks on one line; every defer of `rule-work-mode` should clear.
- Cases 480 and 481 are short defers on new placeholder slugs, `rule-case-build-checks-its-sub-cases` and `rule-prespec-script-skips-code-spans`; they were put on new slugs because this Spec updates `rule-case-build` and `rule-prespec`.
- `guppi prespec --check` on this session's plan now prints `guppi.toml: missing` — the check waits for `guppi.toml`, which the render of `rule-guppi-config` writes. It is an expected red and no debt; its reading is the first pre-spec after this run.

## What actually got done

Ratified: 476.1, 476.2, 476.3, 476.4, 477.1, 477.2, 477.3, 477.4, 478.1, 478.2, 479.1, 479.2, 479.3, 479.4, 479.5, 480.

What got done:
- Commit 0af5b01: `guppi/config.py` and `tests/test_config.py` new; `guppi/render.py`, `guppi/ratified.py`, `guppi/prespec.py`, `guppi/spec.py`, `tests/test_render.py`, `tests/test_prespec.py`, `tests/test_spec.py` and `vault/wiki/rules/rule-render-harness.md` changed.
- `make test`: 876 passed, 2 skipped. `make style`: all checks passed, 64 files already formatted.
- Readings L35–L38 of `raw/2026-09-28/1318/ledger.md`.

What is not done:
- The `guppi.toml: missing` finding of pre-spec — a note, under the instructions above.
- A bug found in Work Mode: the name check of the language finding read the whole heading, `Case` included, so it would fire on every Case of a documentation language not in Latin script; fixed in `ratified.untranslated`, which now judges the name after the dash — note.
- The language finding counts the Latin slugs in the code spans of a `context` or `problem` for a documentation language of another script — defer, Case 481 (L40).
- Six Agent and SendMessage calls refused by the auto mode classifier in plan mode — lesson, L41.
- The hand edit of `rule-render-harness` in Work Mode — note, under the instructions above.
- `estimate-context-size-warns-past-the-limit`: `uv run pytest tests/test_context.py -k limit` gave 3 passed and the `UserPromptSubmit` line came exactly as its Criterion says at 406 944 tokens, but the agent cannot see the `Stop` line, and it passed the note to the person only in the Retro reply, not in its first reply after that prompt — note; the reading is not taken.
- The Retro report against `estimate-retro-report-holds-each-fact-once` — reading `failed`, L39.

49 boxes wait for the librarian.
Read in a later session, since this session creates or updates them: `estimate-guppi-config-fills-the-languages`, `estimate-language-spec-prose-in-english`, `estimate-language-followed`, `estimate-case-build-writes-a-plain-round`, `estimate-skill-wait-what-re-pitches`, `estimate-case-protocol-shows-the-built-case`, `estimate-agent-writing-followed`, `estimate-sprint-migration-file-route-gone`, `estimate-spec-capture-offers-the-fork`, `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`, `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note`, `estimate-retro-red-in-the-baseline-is-not-charged`, `estimate-permissions`.
