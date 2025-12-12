# Problem Analysis: Merge Sorted Array (88)

## 🍀 Intuition
The core idea is that we use 2 pointers technique but **backwards**.
The main problem is that we need to ensure **all elements** from nums2 are merged into nums1 and it's done **in-place**.



## 🎯 Key Idea / Pattern
**Two Pointers (From the End / Reverse Pointers)**.
This is a variation of the Two Pointers pattern specifically designed for "in-place" merging or sorting when space needs to be utilized optimally.

We use three pointers:
* `i`: Index of the last element of `nums1` (`m - 1`).
* `j`: Index of the last element of `nums2` (`n - 1`).
* `currentIndex`: Index of the current insertion point in `nums1` (`m + n - 1`).

The time complexity is $O(m + n)$ because we only iterate through the total number of elements once. The space complexity is $O(1)$ as the merge is done in place.

## 🧠 Mistakes I Made
1.  **The Tail:** Forgetting to handle the edge case where there's `nums2 tail` requiring us to explicitly copy the remaining elements from `nums2` into the front of `nums1`.
    E.g:
    [5,6,7,0,0,0]
    [1,2,3]

    After nums1 is traversed [0,0,0,5,6,7], but there's remaining tail of [1,2,3].

## 💻 Code (Python)
```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        currentIndex = m + n - 1
        i = m - 1
        j = n - 1
        while j >= 0 and i >= 0:
            if nums2[j] > nums1[i]:
                nums1[currentIndex] = nums2[j]
                j -=1
            else:
                nums1[currentIndex] = nums1[i]
                i -= 1
            currentIndex -=1
        #merge remaining tail from nums2
        while j >= 0:
            nums1[currentIndex] = nums2[j]
            j -= 1
            currentIndex -= 1