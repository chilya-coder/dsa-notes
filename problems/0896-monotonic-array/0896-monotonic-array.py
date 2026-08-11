class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc, dec = False, False

        i, j = 0, 1

        while i < len(nums) and j < len(nums):
            if nums[i] < nums[j]:
                inc = True
            elif nums[i] > nums[j]:
                dec = True
            i += 1
            j += 1
        if inc and dec:
            return False
        return True