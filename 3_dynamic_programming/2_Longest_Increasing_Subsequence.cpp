// Longest Increasing Subsequence

/*
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
*/

// my solution
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        if (nums.size() == 0)
            return 0;
        
        vector<int> dp(nums.size(), 0);
        dp[0] = 1;
        int max_ans = 1;
        
        for (int i = 1; i < dp.size(); i++) {
            int maxv = 0;
            
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) {
                    maxv = max(maxv, dp[j]);
                }
            }
            
            dp[i] = maxv + 1;
            max_ans = max(max_ans, dp[i]);
        }
        
        return max_ans;
    }
};