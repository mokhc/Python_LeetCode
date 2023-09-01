# Test Program - LeetCode 9
# Trivial - How can you access the element(s) starting from the back?

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # initializations
        rev = 0
        rem = 0
        res = x
        # loop to generate the reverse number
        while (res > 0):
            rem = res % 10
            res = int(res / 10)
            rev = rev * 10 + rem
            print(rev)
        return x - rev == 0