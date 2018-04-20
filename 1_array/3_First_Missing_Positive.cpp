// First Missing Positive

/*
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:
Input: [1,2,0]
Output: 3

Example 2:
Input: [3,4,-1,1]
Output: 2

Example 3:
Input: [7,8,9,11,12]
Output: 1

Note:
Your algorithm should run in O(n) time and uses constant extra space.
*/

// my solution
class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        if (nums.size() < 1)
            return nums.size() + 1;
        
        vector<bool> res(nums.size()+1, false);
        
        for (int n : nums) {
            if (n >= 0 && n <= nums.size())
                res[n] = true;
        }
        
        for (int i = 1; i < res.size(); i++) {
            if (!res[i])
                return i;
        }
        
        return nums.size() + 1;
    }
};