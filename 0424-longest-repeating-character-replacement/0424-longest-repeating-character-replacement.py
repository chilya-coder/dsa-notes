class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        # "A ABABBA" k = 2
        #  lr
        #  dict {A -> 3; B -> 3} on the 6th iteration
        #  1. A -> 1 - 1 <= k
        #  2. AA -> 2 - 2 <= k
        #  3. AAB -> 3 - 2 <= k
        #  4. AABA -> 4 - 3 <= k
        #  5. AABAB -> 5 - 3 <= k
        #  6. AABABB -> 6 - 3 <= k - false, shrink
        # --
        # "AABABBA"
        #.  lr
        #  dict {A -> 3; B -> 3}
        # ABABBA -> 6 - 3 <= k - false, shrink
        # cycle ends r = len(s)

        l = 0
        freq_map = defaultdict(int)
        max_freq = 0
        max_len = 0

        for r in range(len(s)):
            # Upd counter for char 
            freq_map[s[r]] += 1

            # Upd max frequency in the sliding window
            max_freq = max(max_freq, freq_map[s[r]])

            # If we need > k shifts, shrink (move l)
            window_len = r - l + 1
            if window_len - max_freq > k:
                freq_map[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
        return max_len