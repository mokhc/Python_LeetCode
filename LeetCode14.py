# Test - LC14
# @Author - mokhc
# @Date - 05/10/24
# Trivial - How can you access a specific element of a string in a string array?
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # initialize
        strs.sort(reverse=0)
        a = 0
        # loop to compare the characters of the first and last
        while a < len(strs[0]):
            # return when the character at the first string and the last does not match at a
            if strs[0][a] != strs[len(strs)-1][a]:
                # return the characters from the first to a - 1
                return strs[0][0:a]
            a += 1
        # return the first string from index 0 to length - 1
        return strs[0][0:len(strs[0])]
