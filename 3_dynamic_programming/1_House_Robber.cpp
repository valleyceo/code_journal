// House Robber

/*
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
*/

// my solution
class Solution {
public:
    int rob(vector<int>& nums) {
        int i = 0;
        int e = 0;
        
        for (int k = 0; k < nums.size(); k++) {
            int tmp = i;
            i = nums[k] + e;
            e = max(tmp, e);
        }
        
        return max(i, e);
    }
};