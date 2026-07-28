class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        l,r = 0, len(numbers) - 1

        while r > l:
            sum = numbers[r] + numbers[l] 
            if sum == target:
                return [l + 1, r + 1]
            if sum > target:
                r -= 1
            else:
                l += 1
        return [l + 1, r + 1]
        