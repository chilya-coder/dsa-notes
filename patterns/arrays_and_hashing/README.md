# General Notes

1. **Syntax vs Logic:** Separate actual problem solution from Python syntax.
2. **Data State:** Is data sorted? It's crucial for choosing the correct pattern.
3. **Visualization:** Visualize data whenever possible.
4. **Lookup Time Complexity:**
    * `list`: $O(n)$
    * `set`, `dict`: $O(1)$

---

## [Contains Duplicate](problems/0217-contains-duplicate/0217-contains-duplicate.py)

1. **Unsorted Data:** We use a `set` to filter duplicates, taking $O(n)$ time to traverse all elements.
2. **If Sorted:** We could use the **2 pointers** approach and optimize Space Complexity to $O(1)$.

---

## [Valid Anagram](problems/0242-valid-anagram/0242-valid-anagram.py)

1. **Edge Case:** `if len(s) != len(t): return False`. Anagrams MUST have the same length.
2. **Definition:** Anagram is a **permutation** of characters (all characters must be present in any order).
3. **Pythonic Way to Count:**
    ```python
    Counter(s) == Counter(t)
    ```

---

## [Two Sum](problems/0001-two-sum/0001-two-sum.py)

1. **Unsorted Input:** Create a `dict` (`val -> index`) and check if the complementary value (`target - val`) exists on each iteration. Time: $O(n)$.
2. **If Sorted:** We could use the **2 pointers** approach and optimize Space Complexity to $O(1)$.

---

## [Group Anagrams](problems/0049-group-anagrams/0049-group-anagrams.py)

1. **Pattern:** Create a `{word_pattern -> list(strs)}` dict and group anagrams together.
2. **Sorting Requirement:** The word pattern (dict key) must be sorted.
3. **Python Gotcha:** `sorted(str)` returns a sorted **list**. 
4. **Hashability:** Dict keys MUST be **hashable** (immutable). We CANNOT use lists as keys.
    * *Fix 1 (Tuple):* `tuple(sorted(s))`
    * *Fix 2 (String):* `''.join(sorted(s))`

5. **Advanced Optimization ($O(L)$ instead of $O(L \log L)$):**
    We can replace word sorting with a fixed-size frequency array.

    ```python
    # Creates a list of 26 zeros: [0, 0, ..., 0]
    count = [0] * 26 
    
    for char in word:
        # Maps character ASCII code to index 0-25
        count[ord(char) - ord('a')] += 1
        
    key = tuple(count) # Tuples are hashable!
    ```

    > **How it works:** 
    > There are 26 lowercase English characters. `ord()` returns the ASCII code.
    > * `ord('a')` $\rightarrow$ 97
    > * `ord('b')` $\rightarrow$ 98
    > * Для `'d'`: `ord('d') - ord('a')` $\rightarrow$ $100 - 97 = 3$