class Solution:
    def romanToInt(self, s: str) -> int:
        mappings = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

        total = 0
        prev = 0

        for char in s[::-1]:
            curr = mappings[char]
            if curr < prev:
                total -= curr
            else:
                total += curr
            prev = curr

        return total