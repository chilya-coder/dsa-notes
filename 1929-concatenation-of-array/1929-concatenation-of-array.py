class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        ans = [0] * nums_len * 2
        for idx, num in enumerate(nums):
            ans[idx] = num
            ans[idx + nums_len] = num
        return ans