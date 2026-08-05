class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counter_st = Counter(students)
        for idx, i in enumerate(sandwiches):
            if counter_st[i] > 0:
                counter_st[i] -= 1
            else:
                return len(students) - idx
        return 0