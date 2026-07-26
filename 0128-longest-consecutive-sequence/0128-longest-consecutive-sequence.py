class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Space Complexity: O(n)
        # Time Complexity: O(n)
        max_length = 0

        nums_set = set(nums)
        # IMPORTANT! if we have a lot of duplicates in input list, use nums_set instead of nums
        for i in nums_set:
            if i - 1 in nums_set:
                continue
            # it's the start element
            j = i
            while j in nums_set:
                j += 1
            max_length = max(max_length, j - i)
        
        return max_length