// Product of Array Except Self

/*
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)
*/

// my solution - optimal
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        
        int n = nums.size();
        vector<int> res(n, 1);
        int from_begin = 1;
        int from_end = 1;
        
        for (int i = 0; i < n; i++) {
            res[i] *= from_begin;
            from_begin *= nums[i];
            
            res[n-1-i] *= from_end;
            from_end *= nums[n-1-i];
        }
        
        return res;
    }
};