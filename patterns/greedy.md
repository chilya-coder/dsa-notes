# Greedy algorithm

Main idea is to make a **locally optimal decision at each step**, with the guarantee
that it leads to a **globally optimal solution**.

Greedy algorithms do **not** backtrack.  
They commit to decisions immediately.

---

## Core principle

At every step:

- choose the best option **right now**
- based only on the **current state**
- without revisiting previous choices

Correctness relies on a **greedy invariant** -
a property that guarantees local optimal choices are safe.

---

## Typical greedy state

Greedy solutions usually track a **small, fixed state**, such as:

- minimum so far
- maximum so far
- current best answer
- remaining capacity / budget

No history is stored beyond what is strictly necessary.

---

## Canonical example

### Best Time to Buy and Sell Stock (121)

Key observation:

- we track the **minimum buy price so far**
- we track the **maximum profit** (`price today - minBuy`)

At each step:
- either update `minBuy` if the current price is lower
- or update `profit` if selling today is more profitable
- or do nothing

We do not actually execute a buy operation.
Instead, we keep track of the lowest price seen so far and
continuously evaluate whether selling at the current price
would yield a better profit.

### Best Time to Buy and Sell Stock 2 (122)

Very similar to the previous problem, but the greedy invariant is different.

Here we do not care about a single global optimum.
Instead, we exploit the fact that **multiple transactions are allowed**.

At each step:
- we compare neighboring prices (`i` and `i - 1`)
- if the price increased, the difference represents a guaranteed profit
- this profit is taken immediately

Effectively, we accumulate all positive price deltas.

Single pass. No backtracking.

---

