# Test - LC67
# @Author - mokhc
# @Date - 14/12/24
# Trivial - What is the base of a binary number?

class Solution1:
    def addBinary(self, a: str, b: str) -> str:
        # initialize
        i = len(a) - 1
        j = len(b) - 1
        one = 0
        two = 0
        three = 0
        carry = 0
        ret = ""
        # loop to find the return string
        while (i >= 0 or j >= 0) :
            one = 0
            if (i >= 0) :
                one = ord(a[i]) - 48
            two = 0
            if (j >= 0) :
                two = ord(b[j]) - 48
            three = one + two + carry
            if (three == 3) :
                three = 1
                carry = 1
            elif (three == 2) :
                three = 0
                carry = 1
            elif (three == 1) :
                three = 1
                carry = 0
            elif (three == 0) :
                three = 0
                carry = 0
            ret = str(three) + ret
            i = i - 1
            j = j - 1
        # condition to add an additonal "1"
        if (carry != 0) :
            ret = "1" + ret
        # return
        return ret
    
# implementations
a = "110"
b = "111"
s1 = Solution1()
print(s1.addBinary(a, b))