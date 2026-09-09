---
title: "The server keeps rendering the vacancy table; no grid library is adopted"
type: decision
status: current
authority: table-rendering-approach
binding: prohibition
basis: human
sprint: S0
decided: 2026-08-12
created: 2026-08-13
sources: ["archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md", "docs/superpowers/specs/2026-08-06-shell-and-two-pages-design.md"]
tags: [htmx, architecture, frontend]
---

# The server keeps rendering the table

The owner's decision. This page exists so the question is not reopened **on a wrong ground**.

## The fact, checked by downloading the libraries and grepping them

**None of the seven** — Tabulator, AG Grid Community, Grid.js, DataTables 3, Frappe DataTable,
RevoGrid, Vaadin Grid — leaves `<table>` on the server. All of them draw rows from JSON after
initialisation, **including their free server-side modes**. There is no hybrid.

So adopting any of them means ending htmx's role on the main page and rewriting it as client-side
rendering.

## What the correct objection is, and what it is not

This **confirms** section 9 of the slice 3 spec rather than correcting it. Section 9 rejects the
libraries because they want to own the data and draw it on the client, which contradicts the
invariant that every condition goes to the database and only `PAGE_SIZE` rows come back.

Until 2026-08-06 this entry claimed section 9 rejected them for "they cannot filter on the server"
— **no document says that**, and the reference additionally pointed at the 2a spec, whose section 9
is about testing. The narrow true remark is only this: several of the libraries *can* filter on the
server, free of charge, **and it does not help**.

## Deferred on purpose, and what to weigh first when it reopens

The question was deferred deliberately on 2026-08-12 and is to be revisited **against a dressed
table rather than against an argument** — it is not ripe while the interface still wears the
palette it was prototyped in.

The owner's framing stands: a grid owning *presentation* is not a grid owning *data*, and the free
server-side modes keep the database as the only filter. The case argued against grids at the time
was stronger than the facts support. The real cost is narrower than "htmx ends": the fragment route
returns JSON instead of HTML, and the per-row status control moves from Jinja into a cell renderer.

**The cheap alternative to weigh first:** sorting is an `order_by`, so a link in a column header
buys the main thing a grid is taken for, without touching [[htmx-swap-target-invariant]], the
per-row status control, or the HTML the fragment routes return.
