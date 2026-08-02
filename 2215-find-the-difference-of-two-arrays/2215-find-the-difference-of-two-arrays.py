class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        return [list(set(nums1) - set(nums2)), list(set(nums2) - set(nums1))]
        # res1 = set()
        # res2 = set()
        # for i in nums1:
        #     if i not in nums2_set:
        #         res1.add(i)
        
        # for j in nums2:
        #     if j not in nums1_set:
        #         res2.add(j)
        
        # return [list(res1), list(res2)]