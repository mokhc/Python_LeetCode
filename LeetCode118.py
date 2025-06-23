# Test - LC118
# @Author : mokhc
# Trivial - What do you mean by a list in a list?

# function 1
class Solution1:
	def generate(self, n :int) -> list:
		# initialize
		ret = []
		ea = [1]
		# loop to insert 1s at index 0 and last index for each row
		for data in range(1, n+1):
			ret.append(ea)
			ea = [0] * data
			# insert 1 at index 0
			ea[0] = 1
			# insert 1 at last index
			ea.insert(data, 1)
		# insert the rest of the values
		for d1 in range(2, n):
			# from left to right
			for d2 in range(1, len(ret[d1])-1):
				ret[d1][d2] = ret[d1-1][d2-1] + ret[d1-1][d2]
		return ret