class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        nums.sort()
        # [-3,0,1,2,3,3]
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                l, r = j + 1, len(nums) - 1
                while (r > l):
                    sum = nums[i] + nums[j] + nums[l] + nums[r]
                    if sum == target:
                        res.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                        r -= 1
                    elif sum < target:
                        l+=1
                    else:
                        r-=1
        return [list(quad) for quad in res]