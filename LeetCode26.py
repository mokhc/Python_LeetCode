# Test - LC26
# @Author - mokhc
# @Date - 29/08/24
# Trivial - What is meant by slicing a list?

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # assign
        nums[0:] = sorted([x for x in list(set(nums))])
        # return
        return len(nums)

