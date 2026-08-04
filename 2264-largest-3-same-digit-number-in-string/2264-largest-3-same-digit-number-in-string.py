class Solution:
    def largestGoodInteger(self, num: str) -> str:
        # Space Complexity O(1)
        # Time Complexity O(n)
        l,r =0, 1
        max_digit = ""
        while r < len(num):
            if r + 1 < len(num) and num[l] == num[r] == num[r + 1]:
                if num[l] > max_digit:
                    max_digit = num[l]
            r += 1
            l += 1
        return max_digit * 3