# Test - LC27
# @Author - mokhc
# @Date - 29/08/24
# Trivial - What is meant by a comparison operator?

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # initialize
        currcount = 0
        # loop to get currcount
        for data in range(0, len(nums)):
            if (val != nums[data]):
                nums[currcount] = nums[data]
                currcount += 1
        return currcount
