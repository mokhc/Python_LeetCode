# Test Program - LeetCode 13
# Trivial - How can you get the value of a key?
# Runtime - 99.91%
class Solution:
    def romanToInt(self, s: str) -> int:
        # initializations
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        lengthof = len(s)
        ret = 0
        i = 1
        # loop to find return value
        while (i < lengthof):
            if roman[s[i - 1]] >= roman[s[i]]:
                ret = ret + roman[s[i - 1]]
            else:
                ret = ret - roman[s[i - 1]]
            i = i + 1
        return ret + roman[s[lengthof - 1]]
