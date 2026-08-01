class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        r, l = 0,0
        
        while r < len(word1) and l < len(word2):
            result.append(word1[r])
            result.append(word2[l])
            r += 1
            l += 1
        
        # while r < len(word1):
        #     result.append(word1[r])
        #     r += 1
        
        # while l < len(word2):
        #     result.append(word2[l])
        #     l += 1

        result.append(word1[r:])
        result.append(word2[l:])
        return ''.join(result)