class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Space Complexity: O(n)
        # Time Complexity: O(n)

        # assume input list nums is UNSORTED, otherwise we can solve it with 2-pointers approach O(1)
        unique_set = set()

        for i in nums:
            if i in unique_set: return True
            unique_set.add(i)
        return False
