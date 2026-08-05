class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Space Complexity: O(n)
        # Time Complexity: O(n)
        max_length = 0

        set_nums = set(nums)
        # IMPORTANT! filter duplicates first, otherwise we will have TLE
        # 1. By the task, we don't care about input order (it has chaotic order)
        # 2. Therefore we traverse using for loop.
        # 3. The start element is the one that doesn't have a predecessor (i - 1) in the set.       
        max_streak = 0
        for num in set_nums:
            if num - 1 not in set_nums:
                streak = 0
                current_num = num
                while current_num in set_nums:
                    streak += 1
                    current_num += 1
                max_streak = max(max_streak, streak)
        return max_streak