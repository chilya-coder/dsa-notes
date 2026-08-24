class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        pattern = Counter(s1)
        seen = defaultdict(int)
        l = 0
        for r in range(len(s2)):
            seen[s2[r]] += 1 
                # {'c' -> 1}
                # {'a' -> 2}
            if r - l + 1 > len(s1):
                seen[s2[l]] -= 1
                if seen[s2[l]] == 0:
                    del seen[s2[l]]
                l += 1
            if seen and seen == pattern:
                return True
        return False