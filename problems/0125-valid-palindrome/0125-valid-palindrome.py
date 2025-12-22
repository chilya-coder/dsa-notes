class Solution:
    def isPalindrome(self, s: str) -> bool:
        filteredString = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        # swap approach, instead of the swap we compare

        left,right = 0, len(filteredString) - 1

        while (left < right):
            if filteredString[left] != filteredString[right]:
                return False
            left += 1
            right -= 1
        return True
        