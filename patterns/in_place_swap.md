# In-place Array Swaps
This pattern is used for **in-place mutation** of arrays where elements
need to be **swapped symmetrically** from the edges toward the center.

It is NOT a filtering pattern.
It is NOT about read/write pointers.

It is about **geometry of the array**.

---

## Core idea

We reverse an array (or a subarray) by swapping elements at symmetric positions:

- left pointer moves → right
- right pointer moves ← left
- pointers converge toward the center

No extra memory is allocated.

---

## Pointer responsibilities

Unlike classic two pointers on sorted arrays:

- **left** - points to the left boundary
- **right** - points to the right boundary

Both pointers are **equal citizens**.
No read/write semantics.

---

## Canonical template

```python
def reverse(nums, l, r):
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1
```

### IMPORTANT

Do the **normalization** since we don't want to rotate an array couple of times.
**k %= len(nums)**