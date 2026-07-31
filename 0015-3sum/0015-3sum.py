class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = set()
        
        for idx, i in enumerate(nums):
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue
            l,r = idx + 1, len(nums) - 1
            while r > l:
                sum = i + nums[l] + nums[r]
                if sum == 0:
                    result.add((i, nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    r -= 1
        return [list(x) for x in result]

        