class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Intuitive in-place solution
        writePointer = 0
        maxTwoCounter = 1
        
        for x in nums[1:]:
            if nums[writePointer] == x:
                if maxTwoCounter < 2:
                    maxTwoCounter += 1
                    writePointer += 1
                    nums[writePointer] = x
            else: 
                maxTwoCounter = 1
                writePointer += 1
                nums[writePointer] = x
        return writePointer + 1