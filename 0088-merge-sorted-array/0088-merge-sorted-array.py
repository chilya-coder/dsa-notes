class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        currentIndex = m + n - 1
        i = m - 1
        j = n - 1
        while j >= 0 and i >= 0:
            if nums2[j] > nums1[i]:
                nums1[currentIndex] = nums2[j]
                j -=1
            else:
                nums1[currentIndex] = nums1[i]
                i -= 1
            currentIndex -=1
        
        while j >= 0:
            nums1[currentIndex] = nums2[j]
            j -= 1
            currentIndex -= 1