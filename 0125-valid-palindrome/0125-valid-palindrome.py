class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        new_str = re.sub(r'[\W_]', '', s)
        new_str = new_str.lower()
        arr_chr = []
        for ch in new_str:
            arr_chr.append(ch)
        # 1. convert string to array of char
        # 2. iterate from left and right to compare each char
        # 3. we need n/2 iterations if length is even number and n/2 - 1 if odd

        for i in range (0, int(len(arr_chr)/2)):
            if arr_chr[i] != arr_chr[len(arr_chr) - 1 - i]:
                return False
        return True