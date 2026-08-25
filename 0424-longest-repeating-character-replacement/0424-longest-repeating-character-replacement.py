class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Space Complexity: O(1)
        # Time Complexity: O(n)
        l, max_length = 0, 0
        freq_map = defaultdict(int)

        for r in range(len(s)):
            freq_map[s[r]] += 1
            max_char = max(freq_map.values())
            while r - l + 1 - max_char > k:
                freq_map[s[l]] -= 1
                l += 1
            # Update max length
            max_length = max(max_length, r - l + 1)
        
        return max_length