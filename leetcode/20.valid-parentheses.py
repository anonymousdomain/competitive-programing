import unittest
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for par in s:
        
            if par in ['(','{','[']:
                stack.append(par)
            elif par in [')','}',']']:
                if not stack:
                    return False
                if par==')'and stack[-1]!='(':
                    return False
                if par=='}'and stack[-1]!='{':
                    return False
                if par==']'and stack[-1]!='[':
                    return False
                stack.pop()
        return  not stack
        
            
# @lc code=end
class TestIsValid(unittest.TestCase):
    def test_is_valid(self):
        self.assertTrue(Solution.isValid(self=Solution,s="(){}[]"))
        self.assertFalse(Solution.isValid(self=Solution,s="({}[]"))


if __name__=='__main__':
    unittest.main()
