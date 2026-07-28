class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        max_res = 0

        l, r = 0, len(heights) - 1

        while l < r:
            height = min(heights[l], heights[r])
            # width is the last coordinte minust first one
            width = r - l
            # even with edge case [2 1 1 1 1 6] - we capture 2 6 as the best
            max_res = max(max_res, height * width)
            # we move (get rid of) the worst option only
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_res