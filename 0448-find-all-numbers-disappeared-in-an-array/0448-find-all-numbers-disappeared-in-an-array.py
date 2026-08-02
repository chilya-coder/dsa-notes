class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        res_set = set(nums)
        len_nums = len(nums)
        for idx in range(1, len_nums + 1):
            if idx not in res_set:
                res.append(idx)
        return res