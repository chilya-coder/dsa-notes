class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        #Boyer–Moore majority vote algorithm for (n/2)
        candidate = None
        count = 0

        for x in nums:
            if count == 0:
                candidate = x
            count += 1 if x == candidate else -1
        return candidate

        

        
        