class Solution:
    def maxScore(self, s: str) -> int:
        zero = 0
        one = s.count("1")
        max_score = 0

        for i in s[:-1]:
            if i == "0":
                zero += 1
            elif i == "1":
                one -= 1
            max_score = max(max_score, zero + one)
        return max_score