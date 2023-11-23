#
# @lc app=leetcode id=1470 lang=python3
#
# [1470] Shuffle the Array
#

# @lc code=start
from typing import List
import unittest

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        list1=nums[:n]
        list2=nums[n:2*n]
        output=[]
        for i in range(len(list1)):
            output.append(list1[i])
            output.append(list2[i])
        return output
        
# @lc code=end

#test
class TestShuffle(unittest.TestCase):
    
    def test_shuffle(self):
        
        self.assertEqual(Solution.shuffle(self=Solution,n=3,nums=[2,5,1,3,4,7]),[2,3,5,4,1,7])
        self.assertEqual(Solution.shuffle(self=Solution,n=4,nums=[1,2,3,4,4,3,2,1]),[1,4,2,3,3,2,4,1])
        self.assertEqual(Solution.shuffle(self=Solution,n=2,nums=[1,1,2,2]),[1,2,1,2])
        
if __name__=='__main__':
    unittest.main()