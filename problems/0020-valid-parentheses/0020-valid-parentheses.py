class Solution:
    def isValid(self, s: str) -> bool:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        if len(s) == 1: return False
        stack = []

        bracket_map = {'(':')', '{': '}', '[': ']'}

        for bracket_symbol in s:
            if bracket_symbol in bracket_map:
                stack.append(bracket_map[bracket_symbol])
            # EDGE CASE: check if stack is empty (there is no more closing bracket)
            elif len(stack) == 0 or bracket_symbol != stack.pop():
                return False
        return len(stack) == 0