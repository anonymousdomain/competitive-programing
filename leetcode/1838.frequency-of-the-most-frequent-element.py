#
# @lc app=leetcode id=1838 lang=python3
#
# [1838] Frequency of the Most Frequent Element
#

# @lc code=start
from typing import List
import unittest
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        n=len(nums)
        max_frq=1
        j=0
        total_diff=0
        for i in range(1,n):
            diff=nums[i]-nums[i-1]
            total_diff+=diff*(i-j)
            while total_diff>k:
                total_diff-=nums[i]-nums[j]
                j+=1
            max_frq=max(max_frq,i-j+1)
        return max_frq
# @lc code=end

class TestMaxFrequenceyOfFrequentElement(unittest.TestCase):
    def test_most_frequent_element(self):
        res=Solution.maxFrequency(self=Solution,nums=[1,4,8,13],k=5)
        self.assertEqual(res,2)
        
if __name__=='__main__':
    unittest.main()