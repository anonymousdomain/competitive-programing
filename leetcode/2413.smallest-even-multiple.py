#
# @lc app=leetcode id=2413 lang=python3
#
# [2413] Smallest Even Multiple
#

# @lc code=start
import unittest
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        multiple = 2  

        while True:
            if multiple % n == 0:
                return multiple

            multiple += 2
# @lc code=end

class TestSmallestEvenMultiple(unittest.TestCase):
    
    def test_smallest_even_multiple(self):
        
        self.assertEqual(Solution.smallestEvenMultiple(self=Solution,n=5),10)
        self.assertEqual(Solution.smallestEvenMultiple(self=Solution,n=6),6)
        
if __name__ == '__main__':
    unittest.main()