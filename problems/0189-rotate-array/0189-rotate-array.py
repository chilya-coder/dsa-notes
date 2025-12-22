class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums) #IMPORTANT! Normalizes rotation cycles. e.g. 10%12 = only 2 rotations needed

        # rotation is classic 2 pointers:
        # tuple is used for in-place solution
        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
                r-=1

        # Step 1: Rotate full array
        # [7,6,5,4,3,2,1]
        # Step 2: Rotate k numbers
        #  l   r 
        # [5,6,7,4,3,2,1]
        # Step 3: Rotate the rest of the array from k to len(nums) - 1
        # [5,6,7,1,2,3,4]

        reverse(0, len(nums)-1)
        reverse(0, k - 1)
        reverse(k, len(nums)-1)
        