#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
from typing import List
import unittest 

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red ,white,blue=0,0,0
        
        for num in nums:
            if num==0:
                red+=1
            elif num==1:
                white+=1
            else:
                blue+=1
        for i in range(red):
            nums[i]=0
        print(nums)
        for i in range(red,red+white):
            nums[i]=1
        for i in range(red+white,red+white+blue):
            nums[i]=2
        print(nums)
# @lc code=end
