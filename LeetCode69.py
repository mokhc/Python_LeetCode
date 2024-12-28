# Test - LC69
# @Author - mokhc
# @Date - 14/12/24
# Trivial - What is an exponent?
from math import log10

class Solution1:
    def mySqrt(self, x: int) -> int:
        # return 0 if x == 0
        if x.__eq__(0):
            return 0
        # get the return value
        res = int(pow(10, log10(x)/2))
        return res
    
# implementations
x = 4
s1a = Solution1()
print(s1a.mySqrt(x))
