import unittest
from typing import List
# @lc app=leetcode id=728 lang=python3
#
# [728] Self Dividing Numbers
#

# @lc code=start
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        output=[]
        for li in range(left,right+1):
            if self.isSelfDividing(li):
                output.append(li)
        return output
    
    def isSelfDividing(self, number: int) -> bool:
        for digit in str(number):
            if digit == '0' or number % int(digit) != 0:
                return False
        return True

#test

    