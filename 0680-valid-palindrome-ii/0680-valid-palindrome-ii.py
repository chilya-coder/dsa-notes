class Solution:
    def isPalindrome(self, s: str) -> bool:
        r,l = len(s) - 1, 0
        print(s[l])
        print(s[r])
        while r > l:
            if s[r] != s[l]:
                return False
            r -= 1
            l += 1
        return True

    def validPalindrome(self, s: str) -> bool:
        if len(s) == 0: return False
        r,l = len(s) - 1, 0
        while l < r:
            if s[r] != s[l]:
                if self.isPalindrome(s[l:r]) == False:
                    if self.isPalindrome(s[l + 1 :r + 1]) == False:
                        return False
                    else:
                        return True
                else:
                    return True
            r -= 1
            l += 1
        return True


        