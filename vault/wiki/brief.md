# Brief — 2026-09-30, the Spec of session 2024 conserved

## Where things stand

- The Spec of session 2024 is conserved: `vault/raw/2026-09-29/2024/spec.md`, with `carry.md` beside it. It holds Cases 526, 527 (527.1, 527.2), 528 (528.1, 528.2, 528.3, 528.5), 529, 530 (530.1, 530.2), 531 (531.1–531.15) and the short defer Case 532. 528.4 was superseded by 531.11 and left the Spec.
- Not done on it: all of it. No task of the Spec is built, no page is written, no file is rendered. Work Mode, Retro, the handoff and the librarian's run wait for the session that takes the Spec up.
- The Spec passed `/pre-spec` with no finding (`uv run guppi prespec --check`, exit 0) after one round of fixes: the findings of the first run and of `ask-guppi` went back to the `case-guppi` of each Case, and Cases 526–529 and 531 were ratified again.
- Readings of this session in `vault/raw/2026-09-29/2024/ledger.md`: `estimate-generate-ticks-the-spec` passed (L1), `estimate-glossary-terms-defined` failed (L5), `estimate-documentation-completes` failed (L24).

## Flags

- The ledger lines of the session stay unapplied while `carry.md` stands: `guppi materialize` passes the unit by, so the three readings above and the defer of Case 532 reach no page until the Spec is done.
- Case 531 changes how a session ends: from `/work` to the librarian in one turn, no stop at Retro, `handoff.md` as the report of Retro, the stops on `vault/wiki/where-to-stop.md`, and a `Stop` hook `guppi onward`. The session that builds the Spec still runs `/retro` and `/handoff` by their old text: the new text takes effect only after the librarian's render.
- Case 528.1 holds a by-hand task: `git remote remove origin`. The remote `origin` is `c:/PROJECTS/job hunt ai`; `main` tracks `origin/main`, 3 commits ahead.
- Not measured: whether an `@` import in a skill expands when the agent calls the skill (Case 531.7 relies on it; its reading checks it).
- Frontier of session 2024: the Slice 5 items C2–C6 put off `· sprint · defer`; C14 (`rule-spec-box`: `schema` and `orphan` in `make lint`) put off by Case 532. W38 (`estimate-case-protocol-defers-in-one-reply`) and W39 (`estimate-work-mode-takes-the-work-readings`) stay open: Cases 531.14 and 531.8 update those Estimates, so they are read in a later session.
- The previous brief's Readings due and Next session are not carried here (short shape); `make lint` of the finishing session lists the pending and failed Estimates again.
- The session passed 400 000 tokens in Plan Mode; the person chose to conserve.
