#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#

# @lc code=start

from typing import List


class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x


class Solution:
    def largestNumber(self, nums):
        largest = ''.join(sorted(map(str, nums), key=LargerNumKey))

        if largest[0] == '0':
            return '0'
        else:
            return largest
        

# @lc code=end
