class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Space Complexity: O(1)
        # Time Complexity: O(N)
        l_p, r_p = 0, len(s) - 1

        while l_p < r_p:
            # ignores left non-alphanumeric characters
            if not s[l_p].isalnum():
                l_p += 1
                continue

            if not s[r_p].isalnum():
                r_p -= 1
                continue
            
            if s[l_p].lower() != s[r_p].lower():
                return False

            l_p += 1
            r_p -= 1
        
        return True