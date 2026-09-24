# Handoff — 2026-09-24, session 1303: the context size in the chat, frame-guppi, the re-ratification LEDGER

## Notes from memory

- The person works in the VS Code extension: no statusline, the context indicator shows only past half of the window, and the stdout of a `UserPromptSubmit` hook is not shown to them (they did not see the `hi:` line after `/hi`). They want the size of the context and its change after every reply, mechanically; about 20 tokens a reply written by the agent is the accepted fallback if the `systemMessage` of the `Stop` hook is not shown in VS Code. That is the first live reading of the next session.
- The person worried that reading the frame of every Case costs the main agent's context. The measurement of this session: a Case cost 20–25 thousand tokens of main context, almost all of it reading; 59 past `ask-guppi` dispatches before a `create` have a median input of 205 772 tokens (Opus). Hence the narrow `frame-guppi` on Sonnet (391.1), called only before a Case that changes the behaviour of a rule or a hook (391.2). The person will judge from the numbers of the next session whether it pays; if not, it is rolled back by a Case.
- The 400 000 limit of 392.2 was proposed by the person as a figure to discuss; it is a constant in `guppi/context.py`.
- The person first thought a re-ratification would duplicate ledger lines; it does not — the ledger hook skips a line it holds. Case 390 worked live: the re-ratified 392.1 reached the Spec, the ledger kept each line once.
- The Stop hook of `rule-spec-write` refused 392.1 once (a sub-point value opening with a code span, not padded): lesson L15, schema sentence Case 393, and defer 394 for the shape the parser misreads instead of refusing.
- Pre-spec (`ask-guppi`) found 16 points although the agent had read the frames itself: lesson at Retro, marked `addressed_by:case 391.2`.
- C1, the one pass of Slice 3g, left `[-] · sprint` again. When it runs, the rewrite of `estimate-case-protocol-case-form` takes in 391.2 (what `frame-guppi` found closes `context`), and `estimate-case-protocol-loaded` takes in 390, 391.2 and 393; neither was read in this session.

## Direct instructions to the librarian

- Apply the ledger of `2026-09-24/1303` in ledger order. Cases 391.2, 392.1, 392.2 and 393 were shown and ratified again after pre-spec; their decision lines stand once, from the first ratification. The Spec in `spec.md` holds the texts as ratified last.
- In the Spec, sub-case 392.1 stands before 392.2 (moved by hand before pre-spec): 392.2 replaces text of `rule-context-size` that 392.1 creates, and 392.1 and 392.2 both add a hook to `rule-hook-registry` — apply in ledger order (392.1 lines at 14:51:00 come first in the file; 392.1's ledger lines precede 392.2's).
- `rule-case-protocol` gets three updates in ledger order: 390 (L1), 391.2 (L6), 393 (L17). `rule-hook-registry` two: 392.1, then 392.2.
- L2 replaces the Criterion of `estimate-case-protocol-acknowledging-reply` with the `when`/`then` of Case 390 and sets `pending`; L16 is the reading against that new Criterion, after it in the ledger.
- `estimate-hook-registry-rendered` (392.4) and `estimate-harness-pipeline` (392.3) are old-shape pages: the Criterion replaced whole; 392.4 sets `method`.
- The Insight `insight-workflow-case-written-without-reading-the-pages-it-changes` goes `actioned` by 391.2; the Retro lesson carries `addressed_by:case 391.2`, so it does not reopen it.
- Case 390 carries `{supersedes:case 389}`: the defer of `rule-case-protocol` leaves the brief's Deferred list.
- Renders: `case-schema.md`, `.claude/settings.json` (two new hooks: `guppi context` on `Stop`, `guppi context --prompt` on `UserPromptSubmit`), `.claude/agents/frame-guppi.md`. The code is in commit `00089c4`.

## What actually got done

- Ratified: 390, 391.1, 391.2, 392.1–392.4, 393; deferred at Retro: 394. Frontier: C2 and W3 closed `· work`, C3 → 391, C4 → 390, C5 → 392, C6 → 393, C1 `[-] · sprint`.
- Code, commit `00089c4`: `guppi/context.py` (new), `guppi/ledger.py` (`is_main`, `transcript_records`), `guppi/cli.py`; tests `tests/test_context.py` (new, 7), `tests/test_ratified.py` (+1). `make test` 624 passed, 2 skipped; `make style` clean.
- Readings in the ledger, all `passed`: `estimate-spec-write-copies-the-ratified-case`, `estimate-case-protocol-acknowledging-reply`, `estimate-spec-reconcile-shows-a-changed-case`, `estimate-generate-fails-alone`, `estimate-prespec-binds-a-sprint-line`, `estimate-rules-schema-checked`.
- Readings for the next session: `estimate-context-size-shown-after-each-reply` (the line in the VS Code chat), `estimate-context-size-warns-past-the-limit` (the first prompt past 400 000), `estimate-frame-check-finds-a-contradiction` (two live dispatches), `estimate-case-protocol-checks-its-frame` (at the close of the first session with the agent), `estimate-harness-pipeline` and `estimate-hook-registry-rendered` (after this run's render).
- Not done: the readings by hand of the brief's list — `estimate-language-followed`, `-agent-writing-followed`, `-case-protocol-ledger-line-form`, `-sprint-renders-the-backlog`, `-prespec-reconciles`, `-one-judgment-one-implementation-followed`, `-session-phases-in-order`, `-retro-report-holds-each-fact-once` — left for the size of the context (about 370 000 at Work Mode); the readings that wait for the close of the sprint or a librarian run, as before; `estimate-case-protocol-loaded` and `-case-form` left to Slice 3g.
