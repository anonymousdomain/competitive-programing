#
# @lc app=leetcode id=1985 lang=python3
#
# [1985] Find the Kth Largest Integer in the Array
#

# @lc code=start
from typing import List
import  unittest

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums.sort(key=int,reverse=True)
        largest_number=nums[k-1]
        # [21,12,2,1]
        return largest_number
            
# @lc code=end

class TestLargestIntegerInList(unittest.TestCase):
    
    def test_largest_num_in_list(self):
        res=Solution.kthLargestNumber(self=Solution,nums=["3","6","7","10"],k=4)
        self.assertEqual(res,'3')
        
if __name__=='__main__':
    unittest.main()