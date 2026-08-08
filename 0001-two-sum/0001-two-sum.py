class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Input is UNSORTED (otherwise we would use 2-pointers)
        # Space Complexity: O(n)
        # Time Complexity: O(n)
        pairs = dict()

        # [value] -> [index]

        for idx_num, num in enumerate(nums):
            if target - num in pairs:
                return [pairs[target - num], idx_num]
            pairs[num] = idx_num
        return []