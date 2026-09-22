# Brief — 2026-09-22, after session 1724 of 2026-09-22 (Plan Mode only; the Spec conserved by `/carry`)

Written by `/carry` from the plan of session 1724, its `frontier.md` and `ledger.md`, and the
two `ask-guppi` passes of `/pre-spec`.

## Where things stand

- The Spec stands conserved at `vault/raw/2026-09-22/1724/spec.md` and is **not applied**.
  `vault/raw/2026-09-22/1724/carry.md` beside it tells `guppi materialize` to pass the unit by;
  the session that finishes the Spec deletes that file. No page of `vault/wiki/` was written this
  session but this brief, and no script of the librarian ran.
- The ledger holds 34 decision lines over 21 Cases. Fifteen Cases stand ratified and live in the
  Spec: 324, 325.1, 325.2, 326, 327, 328, 329, 330.1, 331, 332.2, 335, 336, 337, 338.1, 338.2, 340.
  Two are defers: 333 (`rule-documentation`), 339 (`rule-skill-hi`).
- Three Cases were superseded inside the session by findings of `/pre-spec` and left the Spec —
  330.2 by 336, 332.1 by 337, 334 by 339. Their ledger lines stay; the superseding lines carry
  `{supersedes:case N}`.
- What the Spec asks for, in one line each. 324: the hand fix of commit `94277ea` signed after the
  fact — the markers of `rule-atomicity`, the stray closing marker off `rule-case-protocol`. 325.1
  and 325.2: a rendering page without its own markers refused, by `pre-spec` on the plan and by a
  lint class `markers` on disk. 326: a reading ticks the lines of its slug in every live Spec of
  `raw/`, not in the first that holds one. 327: `pre-spec` matches a reading's task line as
  `generate` ticks it — one slug per line. 328: the cascade counts the live Estimates alone, so a
  `delete` of an Estimate no longer drags its target to `draft`. 329: the `method` of
  `estimate-sprint-migration-index-dissolved` names its reading `by hand`. 330.1: `by hand` is the
  one spelling of a reading; `READING` leaves lint. 331: `pre-spec` refuses an Estimate whose
  `method` names none of the forms, by lint's own predicate. 332.2: `pre-spec` simulates the
  `replace` and `reword` pairs of the Spec in entry order and reports an anchor that misses or is
  not unique; `insight-workflow-edit-pair-signed-from-a-grep-fragment` goes `actioned`. 335:
  `check_frontier` judges by the source segment of a Frontier line, not by the whole line. 336: the
  schema of an Estimate names the forms of `method`. 337: `reword` joins the keys of an `update` in
  `case-schema.md`, with one procedure for both forms of a pair. 338.1 and 338.2: two Criteria the
  Spec makes false, repaired. 340: a Case reads the `estimates` of the page it changes as the
  `then` block is written.
- Not done: all of it. No code, no test, no reading, no render, no page. Not one `tasks` box of the
  Spec is ticked.
- The Frontier of the session, `vault/raw/2026-09-22/1724/frontier.md`, holds sixteen Cases lines
  and four Work lines, every one closed. C3, C8 and C9 closed `· sprint` — the three Backlog notes
  of case 319 and the two items of Slice 3b stay on the sprint page, with no `defer` and no
  `deferred_by`. The four Work lines were closed `· work` before their work was done, which is the
  subject of defer 339.

## Deferred

Three items. The previous brief's list held one; the Spec's two defers join it. Neither target is
named by the sprint page.

1. `insight-workflow-edit-pair-signed-from-a-grep-fragment` — `severity` 2, standing in 2 briefs.
   Pattern: an edit pair — a `reword` or a `replace` — is signed from a grep fragment: the matched
   words are copied out as the anchor, and neither the sentence they sit in nor what an earlier
   Case of the same Spec leaves of it is read before the Case is ratified. Case 332.2 of the
   conserved Spec actions it — the procedure in `case-schema.md` by 337 and the simulation in
   `pre-spec` — but the Spec is not applied, so the page still stands `open`.
2. `rule-documentation` — defer 333. `estimate-documentation-completes` stands `failed`: the
   librarian of session 0014 read lines 52–64 of `ledger.md` while counting entries, and the
   Criterion says the frame reads no ledger. Whether the wording of the Criterion is wrong or the
   run was.
3. `rule-skill-hi` — defer 339, which supersedes 334. What a Frontier closer must tell apart:
   whether a Work line closes in a second moment of its own, whether `pre-spec` requires closed
   lines under `Cases` alone, and whether `· sprint` and `· defer case N` stay two closers or
   become one — the file living one session while the state lives on the pages.

## Flags

- **The eight findings of the second `ask-guppi` pass stand unrepaired in the conserved Spec.** The
  next session repairs them before anything else. (1) Case 337's `new` lands inside the enumeration
  of the keys of an `update`, so `change` and `rename` hang off the procedure clause; it belongs
  after the `rename` parenthesis. (2) Cases 337 and 340 both change the paragraph of the Render of
  `rule-case-protocol` whose live reading is `estimate-case-protocol-loaded` (`passed`), and neither
  names it — the rule of case 53.2, and of case 340 itself. (3) Case 340's `then` says "at the end
  of the description of an `update`" while its anchor ``it carries no `contract`.`` is mid-paragraph,
  with three sentences after it. (4) Case 336 says a page with no `method` field is counted
  `unmigrated`; `method_of` falls back to the `## Method` section, which 23 live Estimates carry, so
  such a page earns a `method` finding as well. (5) Case 336 promises no finding to any `method`
  naming one of the four forms, but for the Estimate of a MOC `check_method` demands a
  `make <target>` — the class of error that sank 330.2, repeated in its replacement. (6) Case 332.2
  names case 332.1, which left the Spec: its `－` line goes verbatim into the Criterion of
  `estimate-prespec-simulates-the-pairs`, its `addressed_by` sets `decision-case-332.2` alone while
  the `then` promises both Decisions, and the context of the parent Case 332 still promises a
  sub-case that is gone. (7) Case 338.1 moves the Criterion of `estimate-prespec-binds-a-sprint-line`
  to the source segment and leaves its `method` field in the old wording. (8) Defer 339 names
  `rule-skill-hi` alone while its questions bind `rule-prespec` too, whose closer clause 335 and
  338.1 rewrite in the same Spec.
- Commit `94277ea` changed `vault/wiki/rules/rule-atomicity.md` and `rule-case-protocol.md` by hand,
  outside a librarian's run, by the person's decision; case 324 signs it after the fact and is not
  applied. The pages on disk already hold that text.
- `uv run guppi prespec --check` on the conserved plan exits 1 with one line:
  `frontier: C6 closes a sprint item with case 329, no update of the sprint page under Case 329`.
  It is the false positive case 335 repairs — C6's source is `brief`, and the word `sprint` sits
  inside the slug `estimate-sprint-migration-index-dissolved` in its title.
- The two decision lines of case 335 were written late, at 20:35, after `/pre-spec` reported them
  missing: the reply that ratified the Case carried no `LEDGER` block and a tool call followed its
  text. They stand in the ledger now.
- `render --check`, `sprint --check` and `glossary --check` exit 0. `guppi lint` gives 85 findings,
  unchanged from the previous brief: the vault did not move this session.
- `estimate-hi-writes-frontier` could be read on the evidence of this session — the Frontier was
  written at `/hi` and closed line by line — but no reading was taken and no `estimate[…]` line
  stands in the ledger.
- The three Backlog notes of case 319 — the edge `uses` / `used_by`, the second question of the
  vault query, the lint finding on two Entities naming one `code_ref` — are still notes on the
  sprint page, not Cases.
