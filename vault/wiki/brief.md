# Brief — 2026-10-04, session 1439: the Spec of the close of a sprint and of the check of a Case against the session, conserved

## Where things stand

- Conserved Spec: `vault/raw/2026-10-04/1439/spec.md`, marked by `carry.md`, on the branch `spec/2026-10-04-1439`. It holds Cases 627 (627.1–627.5), 628 (628.1–628.12) and 629 (629.1–629.5), and under `## Deferred` the short-form Cases 630 and 631.
  - 627: the command `guppi sprint-close` — a preview, the choices `--carry` and `--archive-unread`, the close archiving the Decision pages, the actioned Insights, the lone `error` lessons, the sprint page and its Estimates; the four `estimate-sprint-close-*` read by a pytest test and the preview over the live vault; `{supersedes:case 615}` on `entity-sprint-migration`.
  - 628: the close runs in the librarian's run of a session of its own, after `guppi generate`; the readings taken in groups before it; the next session opens the next sprint first; the Backlog of a closed sprint page stays in `backlog.md`; the three Estimates of migration read in the Work Mode of the closing session; the merge of `migration` into `main` a Backlog line for the next sprint; `{supersedes:case 615}`.
  - 629: the check of an answer of `case-guppi` compares its Cases with the other Cases of the session; `case-guppi` answers again by its changed sub-cases; `context` keeps only the searches the Case rests on; `rule-case-rebuild-cost` deleted with `{supersedes:case 566}{supersedes:case 570}`.
  - 630 defers `estimate-spec-write-reaches-the-approved-spec`; 631 defers `estimate-lint-runs-every-step`.
- Not done on it: every task of 627, 628 and 629 — no code, no test, no page, no render. No `materialize` or `generate` ran; the ledger of the session, `vault/raw/2026-10-04/1439/ledger.md`, holds 49 lines, none applied.
- Code and tests: none changed in this session.

## Flags

- No reading was taken in this session; no lesson line was written.
- Cases 627 and 628 were ratified twice: after their first ratification the `Stop` hook `guppi ratified` printed "case 628.1: rule-sprint-close: writes the section Purpose that case 627.1 writes too"; 627.1 and 628.1 were built again and ratified again. Case 629.1 is the change that brings this check to the answer of `case-guppi`.
- Moments set up in this session for readings of a later `/hi`, in transcript `8b8ce20f`: the person asked a change of the ratified Case 627 while Case 628 was built, and the two came back as one batch (`estimate-orchestration-signs-a-batch-together`); the decision line of 629.2 carries two `{supersedes}` blocks for a page with two Cases in its `deferred_by` (second half of `estimate-ratification-ledger-line-form`); the next `/hi` takes this conserved Spec (`estimate-hi-takes-a-conserved-spec`).
- The readings of an Estimate this Spec updates or creates wait for the session after the one that runs it (case 428.1): among them `estimate-sprint-close-*` (W14–W17), `estimate-case-check-requires-each-question-of-the-rounds` (W3) and the three `estimate-sprint-migration-*` (W18–W20).
- The `/pre-spec` report of `ask-guppi` (10 findings, all taken into the Cases built again) is in transcript `8b8ce20f`, not in the vault.
- The context of the session passed 400 000 tokens before the Spec was approved.

## Next session

Cases:
- none

Work:
- `estimate-ask-finds`
- `estimate-ask-query-before-a-create`
- `estimate-case-check-requires-each-question-of-the-rounds`
- `estimate-case-check-sends-back-a-case-number-held-by-another-agent`
- `estimate-case-check-sends-back-a-faulty-round`
- `estimate-case-check-sends-back-a-ratified-case-in-another-shape`
- `estimate-handoff-holds-each-fact-once`
- `estimate-hi-takes-a-conserved-spec`
- `estimate-lint-runs-every-step`
- `estimate-orchestration-signs-a-batch-together`
- `estimate-ratification-ledger-line-form`
- `estimate-session-start-context`
- `estimate-spec-write-reaches-the-approved-spec`
- `estimate-sprint-close-archives-done-insights-and-lone-lessons`
- `estimate-sprint-close-archives-the-decisions`
- `estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest`
- `estimate-sprint-close-settles-unread-estimates`
- `estimate-sprint-migration-leftovers-gone`
- `estimate-sprint-migration-lint-clean`
- `estimate-sprint-migration-merges`
- the unticked boxes of the Specs of 2026-10-03 and 2026-10-04: 4 `read` of `archive/migration/2026-10-03/0115/raw/spec.md`, 5 `read` of `archive/migration/2026-10-03/0317/raw/spec.md`, 1 `read` of `raw/2026-10-04/0004/spec.md`, 3 `read` of `raw/2026-10-04/0112/spec.md`; 11 name a reading above, 2 a reading that passed in session 0112

Ask the person:
- none
