class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthestPoint = 0

        for i in range(len(nums)):
            #check if farthestPoint is still included in range nums[0]...i
            if i > farthestPoint:
                return False
            farthestPoint = max(farthestPoint, i + nums[i])
            if farthestPoint >= len(nums) - 1:
                return True
        return False