class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Time Complexity: O(n * logk) -> k elements stored in heap
        # Space Complexity: O(n + k) -> k elements stored in heap

        # most frequent = min heap (balanced binary tree)
        # calculate frequency with dict

        nums_frequency = Counter(nums)
        # [2] -> 2
        heap = []

        for num, freq in nums_frequency.items():
            heapq.heappush(heap, (freq, num))

            if len(heap) > k:
                heapq.heappop(heap) #pops the smallest element

        return [num for freq, num in heap]