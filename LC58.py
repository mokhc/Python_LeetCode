# Test - LC58
# @Author - mokhc
# @Date - 13/11/24
# Trivial - How do you locate a space in a string?

class Solution1:
	def lengthOfLastWord(self, s: str) -> int:
		# initialize
		ret = ""
		lenret = 0
		count = 0
		# condition to return 0
		if (len(s) == 0) :
			return 0
		
		# split the string
		ret = s.split(" ")
		# assign count
		count = len(ret) - 1
		# while ret[count] is "", count is decrease by 1
		while (ret[count] == "") :
			count = count - 1
		
		# assign length of last word to lenret
		lenret = len(ret[count])
		# return
		return lenret
	
# implementations
s = " Hello World "
s1 = Solution1()
print(s1.lengthOfLastWord(s))