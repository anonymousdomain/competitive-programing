#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#

# @lc code=start
import unittest
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<1:
            return False
        else:
            while(n%4==0):
                n/=4
        return n==1
# @lc code=end
class TestisPowerOfFour(unittest.TestCase):
    def test_Power_of_four(self):
        self.assertTrue(Solution.isPowerOfFour(self=Solution,n=16),True)
        self.assertFalse(Solution.isPowerOfFour(self=Solution,n=21),True)

if __name__=='__main__':
    unittest.main()
