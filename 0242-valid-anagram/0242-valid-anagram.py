class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # anagram is the permutation -> we need to have exact same counter of characters
        # but different order

        return Counter(s) == Counter(t)