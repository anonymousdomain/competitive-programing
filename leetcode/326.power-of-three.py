#
# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
#

# @lc code=start
import unittest 
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==0:
            return False
        else:
            while(n%3==0):
                n/=3
        return n==1
# @lc code=end
class TestPowerOfThree(unittest.TestCase):
    def test_Power_of_three(self):
        self.assertTrue(Solution.isPowerOfThree(self=Solution,n=27),True)
        self.assertFalse(Solution.isPowerOfThree(self=Solution,n=21),True)

if __name__=='__main__':
    unittest.main()
