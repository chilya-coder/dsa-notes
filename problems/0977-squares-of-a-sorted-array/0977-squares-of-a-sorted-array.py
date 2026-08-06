class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # [-4,-1,0,3,10]
        #  l  l  l   r  r

        # [0 1 9 16 100]


        l, r = 0, len(nums) - 1
        res = []

        while l <= r:
            if (nums[l] ** 2) > (nums[r] ** 2):
                res.append(abs(nums[l] ** 2))
                l += 1
            else:
                res.append(abs(nums[r] ** 2))
                r -= 1
        return res[::-1]