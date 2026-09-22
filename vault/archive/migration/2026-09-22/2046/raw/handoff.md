# Handoff — 2026-09-22, the conserved Spec of 1724 repaired and built

## Notes from memory

The person's own observation, and the most valuable thing said this session: the closer
`· sprint` feels inorganic. They worked out why — a session that looks at an item of the
sprint and passes over it leaves no trace anywhere but the Frontier, which dies with the
session. Before case 310.5 the defers piled up on the page, but the brief filtered them out
by 229.4, so they accumulated where nobody read them. Case 352 carries that sentence in its
`purpose`; the question stays deferred by their choice, for the next session.

They watched the form of the Cases closely and caught three faults in it that the schema
settles and no script reads: `recommend` written after `tasks`, `ratification` used as a
notes field for the agent's own caveats, and an error answered in the chat with a promise
instead of recorded as a lesson. They said plainly that they do not like that this started
happening. Four of this session's seven lessons are about that, and the last of them is
about the deeper habit: a fact asserted from a partial check — Case 348 was ratified on the
claim that every ledger line stands in `materialize.yaml`, which is false, and 349 replaced
it.

They pushed back on the ceremony twice: a full Case for a one-line repair felt
disproportionate, and the repair loop felt like a circle. The answers given were that a
ratified Case changes only by a Case, and that conserving again would only move the same
problem forward. They chose to fix everything fixable and go build.

Two caveats on decisions. `addressed_by` on the Insight is one link, not two: nothing breaks
mechanically with a list — lint checks presence and enumerated values, not the shape of a
value — but the schema says one decision wikilink, and the reopening of case 284.4 moves the
field to one decision, which would silently drop the other. And the `context` of Case 347 in
the Spec was rewritten after its ratification to cite the event log instead of the person's
premise; they were told and did not object.

## Direct instructions to the librarian

Materialize both units of 2026-09-22: `1724`, the conserved Spec, whose `carry.md` was
removed in commit `7033975`, and `2046`. The ascending order of the walk matters: 1724's
yaml must exist before 2046 is assembled, so that the `{supersedes}` lines of 2046 reach its
entries through `mark_superseded_elsewhere`.

Expect many superseded entries and few surprises from them. Of 1724: 330.2, 332.1, 332.2,
333, 334, 336, 337, 338.1, 339 and 340. Of 2046, superseded inside their own session and
gone from the Spec: 341, 342, 343, 345, 346 and 348. Their entries should be marked
`superseded_by`, none of them applied, and only their Decision pages written.

`rule-prespec` takes five `replace` pairs, from cases 325.1, 327, 331, 335 and 351, in four
different clauses of its Render. They were checked not to overlap, and the pair simulation
case 351 builds ran over this session's own plan and exited 0. If `generate` refuses one,
the entry order is the first thing to look at, not the anchor.

`insight-workflow-edit-pair-signed-from-a-grep-fragment` goes `actioned` with
`addressed_by: decision-case-351`, one link; its two `clustered` children go to the archive
by the cascade.

Two things to check after `generate` and report, both `by hand` boxes of 1724's Spec:
`rule-materialize` should stand `built`, since case 328 took the archived twelfth Estimate
out of the cascade's count; and the finding of the class `method` on
`estimate-sprint-migration-index-dissolved` should be gone, since case 329 gives it a
`method` that names `by hand`.

`guppi lint` stood at 87 findings before the run, against the 85 of the previous brief. The
two extra are from case 330.1: `is_reading` now takes `by hand` alone, and
`estimate-plan-mode-names-its-estimates` rested on the word `reading` until the `set` of the
same Case reaches it. They should clear at `generate`, with the knock-on finding on
`estimate-session-phases-in-order`.

Eleven Estimates go to `pending` with their Criterion replaced by a Case of this session.
Their readings are due next session, not now: do not take them, and list them under Readings
due by their `method`.

One knowledge lesson of this session names a gap you may meet yourself: a reading folded
into an entry the run skipped leaves no entry at all, so `materialize.yaml` is not a
complete record of the ledger — the 0014 yaml covers lines 1–51, 58 and 60 of a 64-line
ledger with `unparsed` empty. Case 349 widened the ban of your frame for exactly that: one
read of `ledger.md` is allowed, its line count and the lines the yaml does not account for,
and the read is named in your report. Nothing else of the ledger.

The session ran across midnight: its `hi` is 2026-09-22 20:46, the last commits carry
2026-09-23, and the session folder is `raw/2026-09-22/2046/`.

## What actually got done

Plan Mode produced seven live Cases — 344, 347, 349, 350, 351, 352 and 353 — repairing the
eight findings the second `ask-guppi` pass had left in the conserved Spec, plus the two
deferred items of the brief. Six more Cases were written and superseded within the session
as their own facts were checked.

Work Mode built the code of nine Cases across both Specs. In `guppi/lint.py`: `is_reading`
by `by hand` alone with `READING` gone, the predicate `names_a_form` lifted out, and the new
class `markers`. In `guppi/prespec.py`: `check_markers` for a Render written without the
page's own markers, `check_pairs` simulating the `replace` and `reword` pairs of a Spec in
entry order over copies in memory, `check_tasks` matching a reading's task line by
`generate.READ_LINE`, `check_frontier` judging by the source segment of a Frontier line, and
the check of `method` over the Estimate items of a plan. In `guppi/generate.py`:
`replace_hits` and `replace_once` lifted so one rule serves both scripts, `tick_read` over
every live Spec of `raw/`, and the cascade passing over an `archived` Estimate.

572 tests green, `make style` clean, `prespec --check` exits 0 on this session's own plan and
names the Case, the page and the anchor when one is broken on purpose. Two commits: `8e618d1`
and `7033975`.

Not done: no page of `vault/wiki/` — that is your run. Eleven readings wait for it. The two
`by hand` checks wait for it. The two items of Slice 3b, `rule-work-mode` and
`rule-subagent-guppi`, stay on the sprint page with no defer. The question of what a Frontier
closer must tell apart is deferred by case 352, now with the person's own words in its
`purpose`.
