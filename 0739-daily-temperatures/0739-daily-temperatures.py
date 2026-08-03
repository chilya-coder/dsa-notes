class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []  # Храним только индексы: [idx1, idx2, ...]

        for i, temp in enumerate(temperatures):
            # Пока стек не пуст и текущая температура строго больше температуры на вершине стека
            while stack and temperatures[stack[-1]] < temp:
                prev_idx = stack.pop()
                res[prev_idx] = i - prev_idx
            
            stack.append(i)

        return res