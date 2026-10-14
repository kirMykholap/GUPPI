---
type: rule
kind: Leaf
purpose: Prevents a Case from being written in a form the check of its file refuses because the agent that writes it saw no example of the form
status: built
enforcement: render
governs: vault/wiki/case-example.md
render_mode: full
parent: "[[rule-plan-mode]]"
estimates: []
origin: guppi
sprint: guppi
created: 2026-10-14
tags: [session, workflow, harness]
core: true
---

## Purpose

Prevents a Case from being written in a form the check of its file refuses because the agent that writes it saw no example of the form. The examples stand apart from `case-schema.md`, the Render of [[rule-case-protocol]], which `case-guppi` reads whole on every dispatch, a dispatch that answers only with rounds included. Here `case-guppi` reads them once in a dispatch, just before it first writes the file of a Case ([[rule-case-build]]). The example Case passes the check of `rule-case-check`, and the test of its Estimate runs that check over it.

## Render

<!-- rule-case-example -->
# Case — examples

`wiki/case-example.md` — the Render of `rule-case-example`: two examples of the forms that `case-schema.md` sets. `case-guppi` reads this file once in a dispatch, just before it first writes the file of a Case; the rules of the form stand in `case-schema.md`.

## The chat form, by example

The Case below is written in the chat form that `case-guppi` writes into its file. A test runs over it the check that the `SubagentStop` hook of `rule-case-check` runs over that file, and fails on any finding or note, so the example passes that check as the check stands. The limits a form must keep are those of the check, not of this paragraph: copy the form of the example, and read a finding of the check as the limit it names.

````case
## Case 1 — The cart stands before payment

> **context:**
> Until now items went straight from the catalogue to payment, and a buyer could not review an order. The person chose a cart between the two. The pair on `entity-checkout` changes the one sentence of its Purpose that names where the buyer pays; there it names the payment step, which now follows the cart. The Criterion of `estimate-checkout-orders-the-steps` speaks of the order of the steps, so Case 1.1 replaces it. A Glob `vault/**/*cart*` printed nothing, so both new slugs are free.

> **problem:**
> A buyer pays for an order without seeing it whole.

> **recommend:**
> - **Where the cart stands**
>   - Recommended: (a) between the catalogue and payment.
>   - Answer: agreed, (a).

### Case 1.1 — The cart stands before payment

> **given:**
> `entity-cart`: the new page of the cart.
> **＋** `entity-checkout`: the page of payment, which names the cart.
> **＋** `estimate-checkout-orders-the-steps`: its Criterion is replaced whole.

> **when:**
> A buyer with items in `entity-cart` opens `entity-checkout`.

> **then:**
> The buyer sees each item of the order and its price.
> **＋** The buyer pays only after the cart is shown.
> **－** An empty cart does not open `entity-checkout`.

> **tasks:**
> - [ ] create `entity-cart`
>   - type: `entity`
>   - kind: `MOC`
>   - purpose: `Lets a buyer review an order before paying`
>   - tags: `[cart, checkout]`
>   - sections.Purpose: `Until now items went straight from the catalogue to payment.`
> - [ ] update `entity-checkout`
>   - old: `` the buyer pays at `/checkout/pay` ``
>   - new: `` the buyer reviews the cart, then pays at `/checkout/pay` ``
>   - set:
>     ```
>     tags: [cart, checkout, payment]
>     ```
>   - change: `the cart precedes payment`
> - [ ] update `estimate-checkout-orders-the-steps`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the cart precedes payment`
> - [ ] read `estimate-checkout-orders-the-steps`

> **ratification:**
> ```
> - decision[case 1.1][create][entity-cart]{tags:cart,checkout}
> - decision[case 1.1][update][entity-checkout]{ref:entity-checkout}
> - decision[case 1.1][update][estimate-checkout-orders-the-steps]{ref:entity-checkout}
> ```

### Case 1.2 — The cart renders in time

> **given:**
> `estimate-cart-renders-in-time`: the new check of the time the cart takes to show.
> **＋** `entity-cart`: the page of the cart.
> **＋** `src/cart/view.py`: the view of the cart.

> **when:**
> A buyer opens the cart of `src/cart/view.py` with 10, 50 or 200 items.

> **then:**
> The cart shows all its items within 200 ms.
> **－** A cart of more than 200 items is not bound by this time.

> **tasks:**
> - [ ] create `estimate-cart-renders-in-time`
>   - ref: `entity-cart`
>   - kind: `QA`
>   - purpose: `Whether the cart shows its items within 200 ms`
>   - method: `make test-cart, which runs uv run pytest tests/test_cart_view.py -k render_time`
>   - tags: `[cart, performance]`
> - [ ] `src/cart/view.py`: the cart reads its items in one query.
> - [ ] read `estimate-cart-renders-in-time`

> **ratification:**
> ```
> - decision[case 1.2][create][estimate-cart-renders-in-time]{ref:entity-cart}{tags:cart,performance}
> ```
````

## The `then` block, by example

The block below is a `then` block of the Spec in the form that `case-schema.md` sets: a list under each decision type present, one entry per target, `slug` first.

```then
create:
  - slug: entity-cart
    type: entity
    kind: MOC
    purpose: Lets a buyer review an order before paying
    tags: [cart, checkout]
    sections:
      Purpose: |
        Until now items went straight from the catalogue to payment.
  - slug: estimate-cart-renders-in-time
    type: estimate
    ref: entity-cart
    kind: QA
    purpose: Whether the cart shows its items within 200 ms
    method: make test-cart, which runs uv run pytest tests/test_cart_view.py -k render_time
    tags: [cart, performance]
update:
  - slug: entity-checkout
    set: {tags: [cart, checkout, payment]}
    change: the cart precedes payment
  - slug: estimate-checkout-orders-the-steps
    set: {status: pending}
    change: the Criterion replaced whole — the cart precedes payment
```
<!-- /rule-case-example -->

## History

- 2026-10-14 shipped with GUPPI
