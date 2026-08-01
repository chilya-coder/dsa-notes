class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1

        while l < r:
            # if l is even
            if nums[l] % 2 == 0:
                l+= 1
                continue
            # l is not even
            else:
                # r is even
                if nums[r] % 2 == 0:
                    # we just change position
                    nums[r], nums[l] = nums[l], nums[r]
                    r-=1
                    l+=1
                # we change position of r
                else:
                    r -= 1
        return nums