---
title: "The page polls only while a run is in progress, so an idle tab never learns about someone else's collection"
type: decision
status: current
authority: idle-page-polling
binding: prohibition
basis: code
sprint: S0
decided: 2026-08-05
created: 2026-08-13
sources: ["archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md", "docs/superpowers/specs/2026-08-05-collection-from-the-browser-design.md"]
tags: [htmx, collection]
---

# Polling exists only while a run does

The panel and the indicator poll the server **only while a run is in progress**:
`hx-trigger="every 3s"` arrives with the fragment and disappears with it. The spec's phrase is
«no timer of ours».

**So an open, untouched tab notices neither a run started from the terminal nor one from another
tab** — its buttons stay enabled. Slice 3 did not change this and did not try: the shell added an
indicator to both pages, but it obeys the same rule.

## Why this is accepted

Constant idle polling is a price the spec deliberately does not pay, for a cosmetic problem on one
user with one tab.

And the state is honest on **any** re-read:

- navigating between pages is a full page load and notices everything — leaving «Сбор данных» for
  «Вакансии» mid-run gives you a live indicator that counts the run out and re-requests the table
  at the end (verified live, slice 3 walk, scenario 2);
- a reload shows «Прогон запущен из терминала»;
- a press on a stale page goes to 409 and repairs the panel in the same exchange (slice 2b walk,
  scenario 7).

## Three seconds is affordable, and that was measured before it was chosen

Ten requests to the panel fragment, each way: **median 3.7 ms idle** (908 bytes) and **4.3 ms during
a run** (1112 bytes), with a maximum of 22 ms after the first cold request. **The plan's threshold
was ~150 ms**, so the interval stays at three seconds. For scale, on the same database slice 2a
measured ~4 ms of data access and 6.4 ms of page render.

The affordability argument is therefore about the *server*, and the reason polling still stops is
about the *client*: an idle tab that never stops asking is a cost with no beneficiary.

## The plan's scenario 7 over-promised, and the spec was right

The plan said a terminal run «disables the buttons in an already-open page within one poll». **It
cannot**: an idle page does not poll at all. Verified with a real CLI run against an untouched open
page — buttons stayed enabled, zero requests. No code defect; the plan's text was corrected, and
this page is the consequence it should have carried.

That is a small instance of a rule this project keeps re-learning: a plan's own words are a starting
point, not the truth ([[docstrings-drift-inside-their-own-commit]]).

See [[table-refreshes-itself]] for what the last poll carries, [[collection-runs-in-a-thread]] for
where the state actually lives, and [[one-shell-the-vacancies-and-collection-pages-and-one-poller-on-each]] for which fragment does the polling
on which page.
