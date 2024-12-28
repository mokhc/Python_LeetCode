# Test - LC35
# @Author - mokhc
# @Date - 31/10/24
# Trivial - What is needed to end a while loop?
from typing import List

# Pending
class Solution1:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # initialize
        sizetarget = len(nums)
        count = 0
        ret = 0
        # loop to get count
        while (count < sizetarget):
            # if target <= nums[count], assign ret with count and break
            if (target <= nums[count]):
                ret = count
                break
            # if target > nums[count] and count == sizetarget-1, assign ret with count -1 and break
            elif (target > nums[count] and count == sizetarget-1):
                ret = count + 1
                break
            # increase count by 1
            count = count + 1
        # return ret
        return ret

# implementations
nums = [1,2,3,4]
target = 3
s1 = Solution1()
print(s1.searchInsert(nums, target))
