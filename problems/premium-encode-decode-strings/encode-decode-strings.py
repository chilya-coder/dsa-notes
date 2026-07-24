from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        delimeter = '#'
        encoded_string = ""

        for s in strs:
            encoded_string += str (len(s))
            encoded_string += delimeter
            encoded_string +=s

        return encoded_string

    def decode(self, s: str) -> List[str]:
        if len(s) == 0: return []
        
        decoded_string = list()
        digit = 0
        i = 0

        # 5#Hello2#Hi
        while i < len(s):
            digit = 0
            while s[i] != '#':
                digit *= 10
                digit += int(s[i])
                i += 1

            i += 1 # skip '#'
            word = s[i : i + digit]
            decoded_string.append(word)
            i += digit

        return decoded_string

if __name__ == "__main__":
    solution = Solution()
    test_strs = ["Hello", "World", "This", "is", "a", "test"]
    encoded = solution.encode(test_strs)
    print(f"Encoded: {encoded}")
    decoded = solution.decode(encoded)
    print(f"Decoded: {decoded}")