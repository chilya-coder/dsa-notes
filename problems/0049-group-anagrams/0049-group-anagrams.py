class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Time Complexity: O(n * m * log(m)), we sort characters inside of each word, not the word itself
        # Space Complexity: O(n*m) all chars and its quantity
        # [sorted_key] -> [value1, value2, ..]

        pattern_matches = defaultdict(list)

        for word in strs:
            sorted_str = sorted(word) # list of chars, not hashable
            # ''.join(sorted_str) is also possible
            pattern_matches[tuple(sorted_str)].append(word)
        
        return list(pattern_matches.values())