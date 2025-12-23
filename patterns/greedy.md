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
- either update `minBuy`
- or update `profit`
- or do nothing

Single pass. No backtracking.

---

## Greedy invariant

A greedy solution is correct only if:

> Once a choice is made, it will never be beneficial to undo it later.

Example (stock problem):

- if a lower price appears, it is **always better** to buy there
- there is no scenario where buying earlier at a higher price helps

---

## Mental model

Greedy is not about clever tricks.

It is about answering:

> *What is the minimum information I must carry forward  
> so that future decisions remain optimal?*
