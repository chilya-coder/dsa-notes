class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if len(s) == 0: return 0
        g.sort()
        s.sort()

        # g = [1,2,3,7]
        # s = [1,1,3,6]
        g_idx, s_idx = 0, 0
        while g_idx < len(g) and s_idx < len(s):
            if g[g_idx] > s[s_idx]:
                s_idx += 1
            else:
                g_idx += 1
                s_idx += 1
        return g_idx
        