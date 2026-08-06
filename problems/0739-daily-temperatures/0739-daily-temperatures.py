class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Space Complexity: O(n)
        # Time Complexity: O(n)

        # Pattern: Monotonic stack
        # We can add only lower value on the top of stack
        # If the value is bigger than exisiting in stack we have to update result array with the substraction (current_index - stack_top_value_index)

        #[38, 1]
        #[30,0]
        stack = []
        # We need to pre-fill all zeros
        res = [0] * len(temperatures)

        for idx, i in enumerate(temperatures):
            while stack and i > temperatures[stack[-1]]:
                prev_index = stack.pop()
                res[prev_index] = idx - prev_index
            stack.append(idx)
        return res