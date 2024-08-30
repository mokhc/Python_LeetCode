# Test - LC28
# @Author - mokhc
# @Date - 29/08/24
# Trivial - What is meant by comparing two strings?
# Pending - Submitted one on 29/08/24

class Solution1:
    def strStr(self, haystack: str, needle: str) -> int:
            return haystack.find(needle)
        
        
class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:
            return haystack.index(needle)
    

#implementations
haystack = "pooliverpool"
needle = "pool"
s1 = Solution1()
print(s1.strStr(haystack, needle))
s2 = Solution2()
print(s2.strStr(haystack, needle))