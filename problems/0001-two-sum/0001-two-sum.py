class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Space Complexity: O(n)
        # Time Complexity: O(n)
        
        # Input array is UNSORTED, so we use a dict.
        # However, if the input array is SORTED, we can use two pointers to find the solution in O(n) time and O(1) space.
        val_index = dict()
        for idx, val in enumerate(nums):
            complementary = target - val
            if complementary in val_index:
                return [idx, val_index[complementary]]
            val_index[val] = idx
        return []
