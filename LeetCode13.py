# Test - LC13
# @Author - mokhc
# @Date - 29/08/24
# Trivial - What is unique about a dictionary?

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        lengthof = len(s)
        last = roman[s[lengthof - 1]]
        total = 0
        if lengthof > 1:
            for i in range(1, lengthof):
                if roman[s[i-1]] >= roman[s[i]]:
                    total = total + roman[s[i-1]]
                else:
                    total = total - roman[s[i-1]]
            return total + last
        else:
            return last
