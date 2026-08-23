class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Space Complexity: O(1)
        # Time Complexity: O(n)
        l = 0
        freq_map = defaultdict(int)
        longest_sub = 0
        max_freq = 0
        for r in range(len(s)):
            freq_map[s[r]] += 1
            # tricky part, since we care only about max frequency we ever met (we don't need to re-calculate it on every step)
            max_freq = max(max_freq, freq_map[s[r]])
            while r - l + 1 - max_freq > k: #invariant, if true - we need more flips than we currently have k
                freq_map[s[l]] -= 1
                l += 1
            longest_sub = max(longest_sub, r - l + 1)
        return longest_sub