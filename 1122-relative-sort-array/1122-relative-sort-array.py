class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        
        counts = Counter(arr1)

        for num in arr2:
            if num in counts:
                res.extend([num] * counts.pop(num))

        for num in sorted(counts.keys()):
            res.extend([num] * counts[num])
        
        return res