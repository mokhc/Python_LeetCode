# Test Program - LeetCode 1
# Trivial - How can you add value to a key in a dict?
# Runtime ~ 88.90%
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # initialize
        list = {} # dict
        ind = 0
        # loop to find value in list
        while ind < len(nums):
            if target - nums[ind] in list.keys():
                return list[target - nums[ind]], ind
            # add index as value
            list[nums[ind]] = ind
            ind += 1
