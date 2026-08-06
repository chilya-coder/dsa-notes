class Solution:
    def isPalindrome(self, left: int, right: int, s: str) -> bool:
        while right > left:
            if s[right] != s[left]:
                return False
            right -= 1
            left += 1
        return True

    def validPalindrome(self, s: str) -> bool:
        if len(s) == 0: return False
        r,l = len(s) - 1, 0
        while l < r:
            if s[r] != s[l]:
                if self.isPalindrome(l + 1, r, s) == False:
                    if self.isPalindrome(l, r - 1, s) == False:
                        return False
                    else:
                        return True
                else:
                    return True
            r -= 1
            l += 1
        return True


        