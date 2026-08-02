class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        p_1, p_2 = 0, 0
        start_index = 0
        while p_1 < len(haystack) and p_2 < len(needle):
            if haystack[p_1] != needle[p_2]:
                p_2 = 0
                start_index += 1
                p_1 = start_index
            else:
                if p_2 == len(needle) - 1:
                    return start_index
                p_2 += 1
                p_1 += 1
        return -1