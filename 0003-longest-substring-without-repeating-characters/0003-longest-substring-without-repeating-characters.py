class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        if len(s) == 0: return 0

        l, max_res = 0, 0
        unique_chars = set()
        for r in range(len(s)):
            while s[r] in unique_chars:
                unique_chars.remove(s[l])
                l += 1
            unique_chars.add(s[r])
            max_res = max(max_res, r - l + 1)
        return max_res