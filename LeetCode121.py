# Test - LC121
# @Author - mokhc
# Trivial - What is an absolute function?
from typing import List

class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        # initializations
        prev = 0
        count = 0
        # loop to value
        for data in range(1, len(prices)):
            diff = prices[count] - prices[data]
            if prev > diff:
                prev = diff
            if diff > 0:
                data = data + 1
                count = data - 1
        return abs(prev)