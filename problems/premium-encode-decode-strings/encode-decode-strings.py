from typing import List

class Solution:
    # Time Complexity: O(n), where n is all symbols in s
    # Space Complexity: O(n), where n is all symbols in s
    def encode(self, strs: List[str]) -> str:
        # ["Hello", "world"]
        # "5#Hello5#world
        # chars_counter# -> delimeter
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:
        # "5#Hellow5#World"
        # Parse each n# and add " " between
        decoded_list = []
        i = 0
        while i < len(s):
            word_len = 0
            while s[i] != '#':
                word_len *= 10
                word_len += int(s[i])
                i += 1
            i += 1 # skip delimeter

            word = s[i:i + word_len]
            i += word_len
            decoded_list.append(word)
        return decoded_list

if __name__ == "__main__":
    solution = Solution()
    test_strs = ["Hello", "World", "This", "is", "a", "test"]
    encoded = solution.encode(test_strs)
    print(f"Encoded: {encoded}")
    decoded = solution.decode(encoded)
    print(f"Decoded: {decoded}")