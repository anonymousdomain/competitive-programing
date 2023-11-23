#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
import unittest
class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
    
    
        if len(str_x) <= 1:
            return True
    
    
        if str_x[0] == str_x[-1]:
        # Recursive call with the substring excluding the first and last characters
            return self.isPalindrome(str_x[1:-1])
        else:
            return False
# @lc code=end
class TestIsPalindrome(unittest.TestCase):
    
    def test_isPalindrome(self):
        
        self.assertTrue(Solution.isPalindrome(self=Solution,x=121),True)
        self.assertTrue(Solution.isPalindrome(self=Solution,x=-121),False)
        
if __name__=='__main__':
    unittest.main()
