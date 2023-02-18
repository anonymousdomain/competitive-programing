/*
 * @lc app=leetcode id=1968 lang=cpp
 *
 * [1968] Array With Elements Not Equal to Average of Neighbors
 */

class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
         sort(nums.begin(), nums.end());
        int i,temp;
        for(i=1;i<nums.size();i+=2){
                 temp=nums[i];
                 nums[i]=nums[i-1];
                 nums[i-1]=temp;
             }
             return nums;
    }
};
// @lc code=end

