class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Time Complexity: O(n^2)
        # Space Complexity: O(n)
        # - 4 [-1 -1 0 1 2]
        #       l        r

        res = set()
        nums.sort()
        for idx_n, num in enumerate(nums):
            # EDGE CASE - filter duplicates
            if idx_n > 0 and num == nums[idx_n - 1]:
                continue
            l, r = idx_n + 1, len(nums) - 1 # enumerate returns tuple (index, value), + 1 works only with idx_n, not tuple
            while l < r:
                if num + nums[r] + nums[l] == 0:
                    res.add((num, nums[r], nums[l])) # only hashable values in set (no lists)
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] + num < 0:
                    l += 1
                else:
                    r -= 1
        print(res)
        return [list(item) for item in res]