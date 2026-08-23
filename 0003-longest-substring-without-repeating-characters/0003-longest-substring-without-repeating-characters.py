class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        l = 0
        max_substring = 0
        unique_chars = set()
        for r in range(len(s)):
            while s[r] in unique_chars:
                unique_chars.remove(s[l])
                l += 1
            unique_chars.add(s[r])
            max_substring = max(max_substring, r - l + 1)
        return max_substring