class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        freq_map = defaultdict(int)
        l = 0
        pattern_map = Counter(s1)
        for r in range(len(s2)):
            freq_map[s2[r]] += 1
            while r - l + 1 > len(s1):
                freq_map[s2[l]] -= 1
                if freq_map[s2[l]] == 0:
                    del freq_map[s2[l]]
                l += 1
            if pattern_map == freq_map:
                return True
        return False