# Two Pointers

This pattern is typically used in **sorted arrays** for **in-place** optimizations.

We usually maintain two pointers with **different responsibilities**:

1p - **read pointer**: traverses the input list
2p - **write pointer**: marks the end of the valid result and overwrites input list by if statement conditions of task.

Python-specific pitfalls:
(yes, I used to be that Java person =))

-  slicing (`nums[1:]`) creates a new list with shifted indexes — they no longer match the original array
- `for x in nums` iterates over values, not indexes (unlike classic Java loops). Easily solved by using enumerate, but still.
-  be explicit about whether a variable represents an **index** or a **value**

## **Merge Sorted Array (88):**
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

## **Remove Element from the Sorted Array (27):**
Standard easy problem:
Same old one pointer for traversing input, second to fill final list (by the condition currentValue != val).

    [3,2,2,3], val = 3
    [2,2,_,_]


## **Remove Duplicates from Sorted Array (26)**
Similar to remove element, **but! the trick** here is that since we want to remove all of the duplicates, we can start traversing from **[1:]** and compare if the value on position [i] (1) is the same that last unique (unique is on position 0 in the very start, obivously).


    [0,0,1,1,1,2,2,3,3,4]
    [0,1,2,3,4,_,_,_,_,_]

## **Remove Duplicates from Sorted Array || (80)**

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