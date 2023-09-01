# Test Program - LeetCode 14
# Trivial - How can you access a specific element of a string in a string array?
# Runtime - 100%
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # print(strs[0][0:1]) # access one element
        strs.sort(reverse=0)
        # loop to compare the first and last
        for a in range(len(strs[0])):
            if strs[0][a] != strs[0 - 1][a]:
                print("inside")
                return strs[0][0:a]
        return strs[0][0:len(strs[0])]
