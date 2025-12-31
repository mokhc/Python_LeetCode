# Test - LC163
# @Author - mokhc
# Trivial - How do you loop through without starting from zero?
from typing import List

# function 1
class Solution1:
	def findMissingRanges(nums: List[int], lower: int, upper: int) -> List[str]:
		# initializations
		# set length
		lennums = len(nums)
		res = []
		# set blank elements in copy
		copy = (lennums + 2) * [None]
		# set the first element
		copy[0] = lower - 1;
		# set the last element
		copy[lennums + 1] = upper + 1;
		# set the rest of elements in copy
		for i in range(1, lennums + 1):
			copy[i] = nums[i - 1]
		# loop to set the missing range(s)
		i = 1
		while (i < len(copy)):
			subres = copy[i] - copy[i - 1]
			# condition if difference is 2
			if ((subres == 2) == True):
				# temp = [copy[i - 1] + 1, copy[i - 1] + 1]
				res.append([copy[i - 1] + 1, copy[i - 1] + 1])
			# condition if difference is more than 2
			elif ((subres > 2) == True):
				# temp = [copy[i - 1] + 1, copy[i] - 1]
				res.append([copy[i - 1] + 1, copy[i] - 1])
			i += 1
		return res