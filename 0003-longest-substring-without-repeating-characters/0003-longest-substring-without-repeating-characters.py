class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        if len(s) == 0: return 0
        l = 0
        unique_substring = set()
        max_len = 0
        for r in range(len(s)):
            while s[r] in unique_substring:
                unique_substring.remove(s[l])
                l += 1
            max_len = max(max_len, r - l + 1)
            unique_substring.add(s[r])
        return max_len

        