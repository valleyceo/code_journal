// 3Sum Closest

/*
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
*/

// my solution - unoptimal, time: O(n^3), space: O(1)
class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int temp_sum, diff = INT_MAX, res;
        
        for (int i = 0; i < nums.size()-2; i++) {
            for (int j = i+1; j < nums.size()-1; j++) {
                for (int k = j+1; k < nums.size(); k++) {
                    temp_sum = nums[i] + nums[j] + nums[k];
                    
                    if (abs(temp_sum - target) < diff) {
                        diff = abs(temp_sum - target);
                        res = temp_sum;
                    }
                        
                }
            }
        }
        
        return res;
    }
};

/* Note:
- brute force approach: loop over three times and find the closest value, O(n^3)
- optimize1: create hashmap of all sums and get the closest value, O(n^2 + n)
*/