#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#

# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        maxlen=max(len(word1),len(word2))
        output=[]

        for i in range(maxlen):
            output.append(word1[i] if i < len(word1) else '')
            output.append(word2[i] if i < len(word2) else '')

        return ''.join(output)

# @lc code=end

