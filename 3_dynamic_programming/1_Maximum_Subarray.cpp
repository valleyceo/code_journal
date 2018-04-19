// Maximum Subarray

/*
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
*/

// my solution
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        if (nums.size() == 0) {
            return 0;
        }
        
        if (nums.size() == 1) {
            return nums[0];
        }
        
        int sum = 0, max_sum = INT_MIN;
        int min_i = 0, max_i = 0;
        
        for (int i = 0; i < nums.size(); i++) {
            sum += nums[i];
            
            if (sum <= nums[i]) {
                sum = nums[i];
            }
            
            if (sum > max_sum) {
                max_sum = sum;
            }
        }
        return max_sum;
    }
};