#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
from typing import List
import unittest

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater = {}
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                greater[stack.pop()] = num
            stack.append(num)
        ans = []
        for num in nums1:
            ans.append(greater.get(num,-1))
        return ans
              
# @lc code=end
class TestNextGreaterElement(unittest.TestCase):
    
    def test_next_greate_element(self):
        
        result=Solution.nextGreaterElement(self=Solution,nums1=[4,1,2],nums2=[1,3,4,2])
        self.assertEqual(result,[-1,3,-1])
    
if __name__=='__main__':
    unittest.main()