// Maximum Product Subarray

/*
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
*/

// my solution
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int res = nums[0];
        
        for (int i = 1, imax = res, imin = res; i < nums.size(); i++) {
            
            if (nums[i] < 0) 
                swap(imax, imin);
            
            imax = max(nums[i], imax * nums[i]);
            imin = min(nums[i], imin * nums[i]);
            
            res = max(res, imax);
        }
        
        return res;
    }
};