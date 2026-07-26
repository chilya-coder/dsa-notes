class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Space Complexity: O(n)
        # Time Complexity: O(n)
        if len(s) != len(t): return False
        # return Counter(s) == Counter(t)

        char_freq = defaultdict(int)

        for c_s in s:
            char_freq[c_s] += 1
        
        for c_t in t:
            if c_t not in char_freq:
                return False

            char_freq[c_t] -= 1

            if char_freq[c_t] == 0:
                del char_freq[c_t]
        return True