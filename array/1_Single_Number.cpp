// Single Number

/*
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
*/

// my solution
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int n = nums[0];
        
        for (int i = 1; i < nums.size(); i++) {
            n ^= nums[i];
        }
        
        return n;
    }
};