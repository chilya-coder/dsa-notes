class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # return len(nums) != len(set(nums))
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        nums_set = set()

        for num in nums:
            if num in nums_set:
                return True
            nums_set.add(num)
        return False