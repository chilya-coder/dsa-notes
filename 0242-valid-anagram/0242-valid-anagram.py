class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        # anagram is the permutation -> we need to have exact same counter of characters
        # but different order

        #return Counter(s) == Counter(t)

        s_map = Counter(s)

        for char_t in t:
            if char_t in s_map:
                s_map[char_t] -= 1
                if s_map[char_t] <= 0:
                    del s_map[char_t]
        print(s_map)
        return len(s_map) == 0