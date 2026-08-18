class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        window = set()
        max_len = 0
        l, r = 0, 0 # left is actual start of sequence, r just reads

        while r < len(s):
            while s[r] in window: #abca -> a is alr in window
                window.remove(s[l])
                l += 1
            window.add(s[r])
            r += 1
            max_len = max(max_len, r - l)
        return max_len
