# Test Program - LeetCode 26
# Trivial - What is one of the elements of a while loop
# Class
class Solution:
    # Function
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[0:] = list(set(nums))
        return len(nums)

