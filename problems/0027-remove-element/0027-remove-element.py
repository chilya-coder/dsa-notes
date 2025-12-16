class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        currentIndex = 0
        for i in nums:
            if i != val:
                nums[currentIndex] = i
                currentIndex += 1
        return currentIndex
