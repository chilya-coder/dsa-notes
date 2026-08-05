class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Space Complexity: O(n)
        # Time Complexity: O(n)
        max_length = 0

        nums_set = set(nums)
        # IMPORTANT! filter duplicates first, otherwise we will have TLE
        # 1. By the task, we don't care about input order (it has chaotic order)
        # 2. Therefore we traverse using for loop.
        # 3. The start element is the one that doesn't have a predecessor (i - 1) in the set.       
        for i in nums_set:
            if i - 1 in nums_set:
                continue
            # it's the start element
            j = i
            while j in nums_set:
                j += 1
            max_length = max(max_length, j - i)
        
        return max_length