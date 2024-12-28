# Test - LC70
# @Date - 24/12/24
# @Author - mokhc
# Trivial - How can you create a list?

# function 1
class Solution1:
    def climbStairs(n: int) -> int:
        # initialize
        one = 1
        two = 1
        # loop to get the return value
        for a in range(0, n):
            three = one + two
            one = two
            two = three
        # return
        return one
    
# implementations
n = 45
s1 = Solution1
print(s1.climbStairs(n))