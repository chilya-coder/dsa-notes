class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        # anagram is the permutation -> we need to have exact same counter of characters
        # but different order

        #return Counter(s) == Counter(t)

        s_map = Counter(s)

        for char_t in t:
            if char_t not in s_map or s_map[char_t] == 0:
                return False
            s_map[char_t] -= 1
        return True