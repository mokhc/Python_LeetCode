# Test - LC168
# @Author - mokhc
# Trivial - What is meant by converting a numerical number to character?
from operator import mod

class Solution1:
    def convertToTitle(self, columnNumber: int) -> str:
        # initialize
        str1 = ""
        # loop to get the characters
        while columnNumber > 0:
            rem1 = int(mod(columnNumber, 26))
            print("rem1 :" , rem1)
            if rem1 == 0:
                rem1 = rem1 + 26
                if columnNumber == 1:
                    columnNumber = 0
                else:
                    columnNumber-=1
            str1 = chr(int(rem1 + 64)) + str1
            print("str1 :", str1)
            columnNumber = int(columnNumber / 26)
            print("col :" , columnNumber)
        # return
        return str1