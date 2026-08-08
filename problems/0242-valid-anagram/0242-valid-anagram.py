class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Time Complexity: O(n)
        # Space Complexity: O(1) because 26 latin characters
        
        if len(s) != len(t): return False
        # Anagram is the permutation -> we need to have exact same counter of characters
        # but different order

        # return Counter(s) == Counter(t)

        s_map = Counter(s)

        for char_t in t:
            if char_t not in s_map or s_map[char_t] == 0:
                return False
            # avoid deleting the key from the map, just decrease the counter
            s_map[char_t] -= 1
        return True