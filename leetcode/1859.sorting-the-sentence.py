#
# @lc app=leetcode id=1859 lang=python3
#
# [1859] Sorting the Sentence
#

# @lc code=start
import unittest
class Solution:
    def sortSentence(self, s: str) -> str:
        words=s.split()
        sort=""
        for i in range(1,len(words)+1):
            
           for word in words:
               if word[-1]==str(i):
                   sort+=" "+word[:-1]
            
        return sort.strip()
# @lc code=end

class TestSortSentence(unittest.TestCase):

    def test_sort(self):
        
        res=Solution.sortSentence(self='',s="is2 sentence4 This1 a3")
        
        self.assertEqual(res,"This is a sentence")

if __name__=='__main__':
    unittest.main()
    
