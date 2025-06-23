# Test - LC136
# @ Author - mokhc
# Trivial - What is a bitwise operator?
from typing import List

# function 1
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # initialize
        res = 0
        # loop to find value
        for a in range(len(nums)):
            res = ~nums[a] ^ res ^ -1
        return res