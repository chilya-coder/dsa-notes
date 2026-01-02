# Two Pointers

This pattern is typically used in **sorted arrays** for **in-place** optimizations.

We usually maintain two pointers with **different responsibilities**:

1p - **read pointer**: traverses the input list<br>
2p - **write pointer**: marks the end of the valid result and overwrites input list by if statement conditions of task.

## **[88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)**
We use **Reverse Two Pointers** technique from the **end/tail** to insert values on correct positions and not override others.

         i
    [5,6,7,0,0,0]
         j
    [1,2,3]

Don't forget to merge remaining tail of the second array to the first one.

     i
    [0,0,0,5,6,7]
         j
    [1,2,3]

Final result after merging remaining tail of nums2:

    [1,2,3,5,6,7]

## **[27. Remove Element](https://leetcode.com/problems/remove-element/)**
Standard easy problem:
Same old one pointer for traversing input, second to fill final list (by the condition currentValue != val).

    [3,2,2,3], val = 3
    [2,2,_,_]


## **[26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)**
Similar to remove element, **but! the trick** here is that since we want to remove all of the duplicates, we can start traversing from **[1:]** and compare if the value on position [i] (1) is the same that last unique (unique is on position 0 in the very start, obivously).


    [0,0,1,1,1,2,2,3,3,4]
    [0,1,2,3,4,_,_,_,_,_]

## **[80. Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)**

Variation of two pointers.
Since we know the limit of k duplicates (2 in our case), we only need to check whether the current element
is equal to the element `k` positions before (`nums[write - 2]`).


    [ valid | garbage ]
            ↑
          write

    [0,0,1,1,1,1,2,3,3]
         ↑   ↑   ↑
    [0,0,1,1,2,3,3,_,_]


### Key insight:
Two pointers are not about "two indexes".
They are about **separating responsibilities**:
one pointer reads, another defines what is valid.