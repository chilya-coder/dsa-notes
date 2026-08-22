class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_chars = set()
        max_count = 0
        l = 0

        for r in range(len(s)):
            while s[r] in unique_chars:
                    unique_chars.remove(s[l])
                    l += 1
            unique_chars.add(s[r])
            max_count = max(max_count, r - l + 1)
        return max_count

        