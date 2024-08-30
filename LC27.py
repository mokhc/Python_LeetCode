# Test - LC27
# @Author - mokhc
# @Date - 29/08/24
# Trivial - What is meant by a comparison operator?
# Pending - Submitted one on 29/08/24

from typing import List

class Solution1:
    def removeElement(self, nums: List[int], val: int) -> int:
        # initialize
        currcount = 0
        # loop to get currcount
        for data in range(0, len(nums)):
            if (val != nums[data]):
                nums[currcount] = nums[data]
                currcount += 1
        return currcount

class Solution2:
    def removeElement(self, nums: List[int], val: int) -> int:
        # initialize
        currcount = 0
        data = 0
        # loop to get currcount
        while data < len(nums)-1:
            if (val != nums[data]):
                nums[currcount] = nums[data]
                currcount += 1
            data = data + 1
        return currcount


nums = [1,2,3,5]
val = 2
s1 = Solution1()
print(s1.removeElement(nums, val))
s2 = Solution2()
print(s2.removeElement(nums, val))
