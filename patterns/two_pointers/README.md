# Two Pointers

Two-pointer techniques use **two index variables** to traverse data structures efficiently.
The key distinction is **pointer responsibility**:

| Sub-Pattern | Pointer Roles | Direction | Typical Signal |
|:------------|:-------------|:----------|:---------------|
| [Fast/Slow Pointers](./fast_slow_pointers.md) | One reads, one writes | Same direction (→→) | Remove, Filter, Deduplicate, In-place |
| [Classic Two Pointers](./classic_two_pointers.md) | Both explore | Opposite directions (←→) or reverse (←←) | Sorted, Target Sum, Palindrome, Merge |
