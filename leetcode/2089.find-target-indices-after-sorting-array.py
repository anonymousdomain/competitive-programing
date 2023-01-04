#
# @lc app=leetcode id=2089 lang=python3
#
# [2089] Find Target Indices After Sorting Array
#

# @lc code=start
from typing import List
import unittest

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:

        nums.sort()
        index=[]
        for i in range(0,len(nums)):
            if nums[i]==target:
                
                index.append(i)
                
                
        return index
# @lc code=end
class TestTargetedIndex(unittest.TestCase):
    
    def test_targetd_index(self):
        
        rs=Solution.targetIndices(self=Solution,nums=[1,2,5,2,3],target=2)
        self.assertEqual(rs,[1,2])
        
if __name__=='__main__':
    unittest.main()

