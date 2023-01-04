#
# @lc app=leetcode id=1512 lang=python3
#
# [1512] Number of Good Pairs
#

# @lc code=start
from typing import List
import unittest
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
            count_good_pairs=0
            for i in range(len(nums)-1):
                
                for j in range(len(nums)):
                    
                    if i<j and nums[i]==nums[j]:
                        count_good_pairs+=1
            return count_good_pairs
# @lc code=end
class TestGoodPairs(unittest.TestCase):
    def test_goodpair(self):
        result=Solution.numIdenticalPairs(self=Solution,nums=[1,2,3,1,1,3])
        self.assertEqual(result,4)

if __name__=='__main__':
    
    unittest.main()