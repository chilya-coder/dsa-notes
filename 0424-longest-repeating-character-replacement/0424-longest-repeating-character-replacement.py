class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = defaultdict(int)
        l = 0
        max_substring = 0
        max_freq = 0

        for r in range(len(s)):
            # Update char frequency
            freq_map[s[r]] += 1
            max_freq = max(max_freq, max(freq_map.values()))
            while r - l + 1 - max_freq > k:
                # IMPORTANT: move l, not r
                freq_map[s[l]] -= 1
                l += 1
            max_substring = max(max_substring, r - l + 1)
        return max_substring