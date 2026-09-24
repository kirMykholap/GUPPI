# Brief — 2026-09-24, session 1916 conserved by `/carry`

Written by `/carry` in the short shape of `rule-brief`. The librarian did not run: the
Spec of session 1916 is ratified and its work is not done.

## Where things stand

- The conserved Spec: `vault/raw/2026-09-24/1916/spec.md`, marked by `carry.md` beside it.
  `guppi materialize` passes the unit by until the session that finishes the Spec deletes the mark.
- Its Cases, all ratified in Plan Mode of session 1916; `prespec --check` exit 0 on the plan:
  - 395 — Slice 3g of `entity-sprint-migration`: the one note cut into four.
  - 396.1–396.2 — `estimate-case-protocol-case-form` and `estimate-case-protocol-loaded` rewritten
    whole by the model of case 378.
  - 397.1–397.5 — the Estimates of `rule-materialize` of the old model; the journal `-assembles`
    split, two Estimates created.
  - 398.1–398.3 — the Estimates of `rule-page-generation` of the old model.
  - 399.1–399.5 — the journal `estimate-prespec-checks-the-plan` split, four Estimates created.
  - 400.1–400.2 — `estimate-plan-mode-names-its-estimates`; the note of the eleven leaves Slice 3g.
  - 401.1–401.8 — the journals: `estimate-lint-catches` split, four Estimates created;
    `Given:` out of `estimate-generate-ticks-the-spec` and
    `estimate-materialize-skips-a-carried-over-unit`; the note of the journals leaves Slice 3g.
  - 402 — `rule-spec-write`: a sub-point value holding a backtick only in a padded span
    (`{supersedes:case 394}`).
  - 403, 404 — defers, under `## Deferred`.
  - 405 — `rule-case-protocol`: a defer is written in the reply that asks for it.
- Not done on it — all of Work Mode:
  - the code of Case 402: `guppi/ratified.py` and `tests/test_ratified.py` with the fixture
    `SHOWING`;
  - `uv run guppi render` of `vault/wiki/case-schema.md` (402, 405) and `uv run guppi sprint`
    (395, 400.2, 401.8);
  - every `read` line of the Spec;
  - `/retro`, `/handoff` and the librarian's run.
- The one reading of the session stands in the ledger:
  `estimate-context-size-shown-after-each-reply` `passed` — `pytest tests/test_context.py`
  passed; the person saw the line in the VS Code chat.
- Frontier of 1916: C1, C2 → 395; C5 closed `· work`; C6 → 402; C7 → 400; C8 → 401;
  C11 → 405; C3 → defer 403; C4 → defer 404; C9, C10 left `[-] · sprint`; W1 and W2 open.

## Deferred

1. `rule-spec-write` — deferred by Case 394. Case 402 of the conserved Spec takes it up with
   `{supersedes:case 394}`; the defer stands until that Spec is applied.
2. `rule-frame-check` — deferred by Case 403: whether `frame-guppi` pays — the contradictions it
   finds against its tokens and time over the sessions after 1303; rolled back by a Case if it
   does not.
3. `rule-context-size` — deferred by Case 404: the limit of 400 000 tokens in
   `guppi/context.py`, proposed as a figure to discuss; judged once a session reaches it.

## Flags

What the vault does not know about session 1916:

- The person asked that these reach the next session as Cases:
  - `prespec --check` runs after each ratified Case, until it is clean. The agent fixes the
    script's findings and does not show them to the person again: the script checks the agent.
  - A `context` names no count of items: a count goes stale first and was a source of errors in
    this session. What can be counted, a script counts.
  - Translating a Case at the end of the Spec is costly: session 1916 spent a large part of its
    context on it. Consider translating each Case right after its ratification.
  - The `UserPromptSubmit` hook of `rule-context-size` orders the session closed with `/retro`
    and `/handoff` past 400 000 tokens. The person reads the mark as "take no more work" — it is
    no reason to leave Plan Mode for Retro. The text of the hook is to change; it stands next to
    defer 404.
  - The promises signed twice that `ask-guppi` found at pre-spec: the ones inside the Spec are
    fixed; one is left, `estimate-case-protocol-case-form` (396.1) against
    `estimate-prespec-checks-the-frame` — one behaviour from two sides — to be looked at.
- A candidate for a Case: a change of `given` alone after ratification — the lines of the frame
  that `prespec --check` asks for — is shown again whole by `rule-spec-reconcile`, though
  `given` enters no Estimate. In session 1916 most of the Cases shown again at pre-spec changed
  only `given`.
- In session 1916 `frame-guppi` was dispatched for Cases 402 and 405. In 402 it found the fixture
  `SHOWING` of `tests/test_ratified.py`; in 405 the one rule, the `ratification` row and the
  Frontier at Retro.
- The context of session 1916 passed 400 000 tokens at `/pre-spec`. The largest costs were
  reading the plan file whole twice and about 30 edits to translate the Cases at the end.
- The Spec of 1859 lies in the archive with 4 unticked `read` lines. `generate` does not read the
  archive, so those boxes do not tick; the Estimates themselves stand `pending` and are read as any.
