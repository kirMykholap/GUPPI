# Handoff — 2026-09-10, Slice 3, session E

## Notes from memory

- The owner reshaped the Case mid-Plan-Mode (Cases 30 → 34): seven sections, given/when/
  then, operands **＋**/**－**, simple language, the `then` block moved to the Spec. Cases
  29–33 in the chat were in the old form; the Spec carries them in the new one.
- Two `defer` placeholders (Case 29) are the first pages the model created by `defer`.
- The owner refused reading archived lessons in synthesis (35.2) and asked for one
  Decision page per Case (31.1). Both were his own alternatives.
- `librarian-guppi` became visible to the Agent tool in the same session it was rendered,
  which contradicts the lesson of session D. Not read further; the librarian was not run.
- The gate refused `/handoff` on the dirty tree when the agent called it at the end.

## Direct instructions to the librarian

- The 2026-09-10 yaml is fully applied (77 entries, none failed). Your first run
  materializes the next session's ledger; do not touch the yamls of 2026-09-09 and
  2026-09-10 beyond what `materialize` extends.
- Two lessons on agent visibility contradict each other (see the brief). Cluster or flag.
- `[delete][old-harness]` (case 6) fails on every run of the 2026-09-09 yaml: no page,
  no category. Flag it; do not invent a route.

## What actually got done

- Everything in `raw/2026-09-10/spec.md`, Порядок работы steps 1–11, in one commit after
  this note: `feat(harness): Slice 3 — materialize, generate, cleanup, gate, the
  librarian agent, /retro and /handoff`.
- Not done: `/retro` and `/handoff` were not invoked (the session ran long); the librarian
  never ran; the readings listed in the brief wait for the next session.

---

# Handoff — 2026-09-10, Slice 3 closes, session F

## Notes from memory

- The owner picked "close Slice 3" from the Frontier and ratified both Cases at the
  first reading, without a question. No hesitation recorded.
- Case 42 carries no decision line: it only runs the built rituals. Its ten readings
  (eight of Slice 3, two of Case 43) are written by the main agent after your commit,
  so they stay uncommitted and are materialized by the next run, whatever its date.
- Case 43 changes the contract of `materialize` and `generate`: without `--date` both
  walk every `vault/raw/<date>/`. Caveat accepted in the Spec: the Render text of
  `rule-documentation` changes with this run, so `render --check` is red until
  `guppi render` is run and committed at the start of the next session.
- The two new Estimates hang by `ref` on `built` rules; the cascade drops
  `rule-materialize` and `rule-page-generation` to `draft` until their readings land.
- The brief of session E said `Materialize 2026-09-11`; the session ran on 2026-09-10,
  the same date as E, so the raw folder is shared.

## Direct instructions to the librarian

- The walk touches 2026-09-09 as well: its yaml is fully applied except
  `[delete][old-harness]` of case 6, which has no page and no category. Flag it; do
  not invent a route. Its stderr line is expected on every run.
- Two lessons on agent visibility contradict each other:
  `lesson-agents-loaded-at-session-start` (session D, a rendered agent usable only
  from the next session) and `lesson-agents-visible-in-session` (session E, the
  opposite observed). Same area, opposite claims. Synthesis: cluster or flag.
- Case 43 creates `estimate-materialize-walks-dates` and `estimate-generate-walks-dates`;
  nothing close exists in `estimates-index.md` as of this morning. Its three updates
  rewrite the How it works of `rule-materialize`, replace one sentence in
  `rule-page-generation` and one in the Render of `rule-documentation`.
- Do not change `sprint.md`. Slice 3 is not closed until the ten readings are read;
  the next session's handoff says so.
- The deferred list of the previous brief carries over with one more postponement each;
  nothing of it was touched this session.

## What actually got done

- Commit `165a261 chore(ledger): the tail of session E` (three ledger lines of 11:18:24).
- Commit `893b3d9 feat(harness): Case 43 — materialize and generate walk every date`:
  `guppi/materialize.py` (`dates_with`, `materialize_date`), `guppi/generate.py`
  (`generate_date`), six tests in `tests/test_materialize.py` and `tests/test_generate.py`,
  `make test` 132 green, the Spec of session F appended to `raw/2026-09-10/spec.md`, the
  five decision lines of Case 43.
- Not done: the pages of Case 43 (yours, now); `guppi render` of
  `.claude/agents/librarian-guppi.md` after your update of `rule-documentation` (next
  session, with a commit); the ten estimate readings of Case 42 (after your report,
  uncommitted); the close of Slice 3 in `sprint.md` (next session).

---

# Handoff — 2026-09-10, session G: the librarian's reads, generate per entry, Slice 3c

## Notes from memory

- The owner questioned the read limit of the librarian at length. The outcome, Case 44:
  the four inputs are the inputs of the run; a wiki page may be opened in three named
  cases (same-or-near not settled by an index line; the lessons of an Insight being
  written; a page a script names in an error), each named in the report with its reason;
  never session artifacts, the archive, or code; the yaml is edited only by the marks and
  the entries of index check and synthesis, a rejected entry is a flag, not a repair.
  Insights stay the librarian's product, status `open`, no ratification.
- Case 45 (a `guppi tail` script printing the unmaterialized ledger lines at `/hi`) was
  drafted in full, then deferred by the owner to Slice 3c: with `raw/` archived after the
  librarian, the tail is what lies in `raw/`, no diff needed. The draft sits in the Spec
  under Case 45 in an untagged yaml fence, unsigned.
- Case 46 records Slice 3c, raw lifecycle, in `migration-plan.md` and `sprint.md`:
  `decided_by` on pages born of a Case, `origin` as a ledger pointer elsewhere, `raw/<date>/`
  of a fully applied date archived by run stamp with its paths rewritten. The owner runs
  several sessions a day; the stamp exists for that. Nothing of it is built yet.
- Retro was reshaped in conversation: an analysis, not planning; decisions in Retro are
  always `defer`; lessons and estimates are written there; red tests mean the question
  "fix now, or revert to a patch in raw/ and defer". Recorded as `defer` of `rule-retro`
  (Case 50). The Stop hook misses a reply that ends in a Skill or ExitPlanMode call: the
  lines of Cases 48 and 49 were lost and re-emitted at Retro; `defer` of `rule-ledger-write`
  (Case 51) and `lesson-ledger-hook-misses-a-reply-ending-in-a-tool-call` carry it.
- Two readings of Slice 3 stand `failed` in this ledger (documentation-completes,
  synthesis-clusters, 11:57:07). Their criteria change by Case 44 in this same yaml, after
  the failed lines. The `passed` readings come after your run, in the tail, and the next
  session closes Slice 3. Do not close it.

## Direct instructions to the librarian

- Materialize 2026-09-10. The walk over 2026-09-09 should now pass `old-harness` with a
  stdout line (Case 48): if stderr still names it, flag it.
- The frame of Case 44 applies to this run even though `.claude/agents/librarian-guppi.md`
  will only be rendered next session: name every page you open in the report with its
  reason (same-or-near, the lessons of an Insight, a script's error); read no file under
  `guppi/` or `tests/`; do not edit the yaml beyond the marks and your own entries; an
  entry `generate` rejects stays as it is and is a flag. The marks of the yaml: `applied`
  and `failed` are set by generate; `exists` is a create whose page was on disk;
  `incomplete` lists fields the Spec block lacked; `near`, `librarian` and `merged` are
  yours, no script reads them, the brief reports them.
- Lessons in this ledger: three about generate (`replace` mapping crash, log written last,
  walk history dated by yaml), `lesson-librarian-reads-beyond-the-four-inputs`,
  `lesson-readings-after-librarian-invisible-to-next-hi`,
  `lesson-ledger-hook-misses-a-reply-ending-in-a-tool-call`. Synthesis by the rule of
  Case 44: read the Trigger and Root cause of the lessons you cluster and name them. The
  three generate lessons share an area; whether they share a root cause is your judgment.
  `lesson-librarian-reads-beyond-the-four-inputs` may pair with the two agent-visibility
  lessons only if the cause is the same; it is not — it is about the frame, not agent
  loading.
- Possible near pairs: `estimate-generate-rejects-shape-alone`,
  `estimate-generate-logs-per-entry`, `estimate-generate-dates-history-by-run`,
  `estimate-generate-passes-delete-outside-vault` against `estimate-generate-writes` and
  `estimate-generate-walks-dates` — each checks a behaviour the earlier ones do not; keep
  them as `near` at most, no merge.
- `rule-ledger-tail` (Case 45 defer) is a placeholder with a purpose only; it will be an
  orphan at lint, like `rule-work-mode`. Expected. `rule-retro` and `rule-ledger-write`
  defers have pages: History lines only.
- Rule-class files (`case-schema.md`, `index.md` §5, `migration-plan.md`) and `sprint.md`
  were edited by hand in Work Mode; their entries are `file` entries, nothing to write.
- Do not touch `sprint.md`. Do not close Slice 3.
- The brief: Slice 3 closes next session after the two `passed` readings; Case 45 is
  deferred to Slice 3c; next session's first step is `uv run guppi render` and a commit
  (the agent file lags rule-documentation by Case 44), then the readings of Case 44 and
  of the four generate estimates, then Plan Mode over Cases 50, 51, Slice 3c or 3b. The
  readings written after your commit will sit in the ledger tail; the owner adds a note
  to the brief by hand, as after session F.
- Deferred, carried with counts +1: Slice 3b Work Mode, `/grill-me`, upstream `origin`,
  `gh`, `parked/` and the old `archive/`, archive in `ask-guppi`, plus Case 45 → Slice 3c,
  Case 50 `rule-retro`, Case 51 `rule-ledger-write`.

## What actually got done

- Commit `68bb295`: render of the librarian agent file after Case 43; the tail of session
  F and the Spec of session G in raw; the owner's note in brief.md.
- Commit `3eaf5a3`: `guppi/generate.py` — an entry fails alone whatever the cause and is
  marked `failed`; `log.md` appended after each entry; History and log lines carry the
  run's date, `created` the yaml's; a delete with `category: unknown` is outside the vault,
  applied with a stdout line. Five tests in `tests/test_generate.py`, `make test` 137.
  `log.md` regained six lines of entries 78–82. `case-schema.md` pins `replace` as a list
  of pairs; `index.md` §5 gains the delete-outside-the-vault row; `migration-plan.md` and
  `sprint.md` carry Slice 3c.
- Commit `ebf943b`: the two defers of Retro.
- Readings taken: `estimate-librarian-reads-beyond-the-four-inputs` passed (13:10:37).
- Not done: the pages of Cases 44–49 (yours); the render of the Case 44 frame (next
  session); the readings of Case 44 and of the four new generate estimates (after your
  run); the close of Slice 3; Case 45, 50, 51 (deferred).

---

# Handoff — 2026-09-10, session G, second pass: after the materialize fix

## Notes from memory

- The first pass stopped at step 1: `guppi materialize` failed with `'line'`. Cause: the
  three entries you (the librarian of session F) appended at synthesis carry no `line` and
  no `case`; assemble assumed both. Fixed in commit `7dc4f7f`, one test, `make test` 138.
  The lesson `lesson-materialize-assumes-every-entry-has-a-line` is in the ledger.
- A dry run of assemble over 2026-09-10 adds 37 entries, no `unparsed`; `incomplete` on
  four: `source` of two lessons (lines 99, 100 — their source text holds a dash or a
  comma the grammar may not take), `then` of the two Retro defers (Cases 50, 51 — a
  Retro defer has no Spec block by design).

## Direct instructions to the librarian

- Everything in the document above still holds. Materialize 2026-09-10; the yaml of
  2026-09-10 now takes the whole of session G.
- Your own three synthesis entries of session F sit in the yaml without `line`; leave
  them as they are.

## What actually got done

- Commit `7dc4f7f`: `guppi/materialize.py` skips entries without `line` when matching
  the ledger and entries without `case` when grouping decisions; `tests/test_materialize.py`
  gains one test. Nothing else changed since the document above.
