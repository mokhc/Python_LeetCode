# Test - LC88
# @Author - mokhc
# Trivial - What is a characteristics of a list?
from typing import List

# function 1
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # loop to get the values to the list
        for ind, x in zip(range(0, n), nums2):
            nums1[m+ind] = x
        # sort the list
        nums1.sort()