#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#

# @lc code=start

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums=[str(num) for num in nums]
        nums.sort( reverse=True)
        
        largest=''.join(nums)
        
        if largest[0]=='0':
            return '0'
        
        return largest
        
# @lc code=end

