# Test - LC1
# @Author - mokhc
# @Date - 28/08/24
# Trivial - How can you add value to a key in a dict?
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       # initialize
        list = {}
        ind = 0
        back = len(nums) - 1
        # loop to find value in list
        while ind < len(nums):
            if target - nums[ind] in list.keys():
                return sorted((list[target - nums[ind]], ind))
            # add index as value
            list[nums[ind]] = ind
            if target - nums[back] in list.keys():
                return sorted((list[target - nums[back]], back))
            # add index as value
            list[nums[back]] = back
            # increment
            ind+=1
            # decrement
            back-=1

