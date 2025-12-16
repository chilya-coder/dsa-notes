class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Quite interesting variation of "no more than k same items"
        # For a sorted array, comparing with nums[write - 2] ensures no more than two duplicates

        write = 0
        
        for x in nums:
            if write < 2 or x != nums[write - 2]:
                nums[write] = x
                write += 1
        return write