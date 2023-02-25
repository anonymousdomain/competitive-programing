#
# @lc app=leetcode id=1679 lang=python3
#
# [1679] Max Number of K-Sum Pairs
#

# @lc code=start
from typing import List
import unittest

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        # [1,2,3,4]
        frq={}
        count=0
        for num in nums:
            if num<k:
                diff=k-num
                
                if diff in frq and frq[diff]>0:
                    count+=1
                    frq[diff]-=1
                    
            if num not in frq:
                frq[num]=0
                frq[num]+=1
               
        return count
# @lc code=end
class TestMaxNumberOfKSumPair(unittest.TestCase):
    def test_max_number_of_sum_pair(self):
        res=Solution.maxOperations(self=Solution,nums=[1,2,3,4],k=5)
        self.assertEqual(res,2)
        
        
if __name__=='__main__':
    unittest.main()