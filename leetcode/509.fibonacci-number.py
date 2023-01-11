#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
import unittest 
class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        return self.fib(n-2)+self.fib(n-1)
# @lc code=end
class TestFib(unittest.TestCase):
    def test_fib(self):
        self.assertEqual(Solution.fib(self=Solution,n=2),1)

if __name__=='__main__':
    unittest.main()