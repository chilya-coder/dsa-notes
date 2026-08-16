class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        current, start = 0, 0
        max_len = 0
        while current < len(s):
            while s[current] in substring:
                substring.remove(s[start])
                start += 1  
            substring.add(s[current])
            max_len = max(max_len, current - start + 1)
            current += 1
        return max_len