# Test - LC125
# @Author - mokhc
# Trivial - What is one of the elements of a while loop?

# function 1
class Solution1:
    def isPalindrome(self, s: str) -> bool:
         # initialize
        str1 = "abcdefghijklmnopqrstuvwxyz0123456789"
        s = s.casefold()
        l = 0
        r = len(s)-1
        # loop to get adjust l and r values
        while (r > l):
            while (s[l] not in str1) & (r > l):
                l+=1
            while (s[r] not in str1) & (r > l):
                r-=1
            # condition to return False
            if (s[l] != s[r]):
                return False
            l+=1
            r-=1
        # return True
        return True