# Test - LC66
# @Author - mokhc
# @Date - 19/11/24
# Trivial - What is the function of an index in an array?
from typing import List

# function 1
class Solution1:
    def plusOne(digits: List[int]) -> List[int]:
        # initialize
        ret = digits
        count = len(digits) - 1
        check = False
        # condition to get into the loop
        # loop to increase the count or assign value 0
        # the process starts from the last bit to the first
        while (count >= 0) :
            # condition if ret[count] != 9
            if (ret[count] != 9) :
                ret[count] = ret[count] + 1
                check = False
                break
            # else if ret[count] == 9
            else :
                ret[count] = 0
                check = True
            count = count - 1
        # condition to check if variable check == True
        # insert additional value 1
        if (check == True) :
            ret.insert(0, 1)
        return ret
    
# implementations
digits1 = [1,9]
s1 = Solution1
print(s1.plusOne(digits1))
