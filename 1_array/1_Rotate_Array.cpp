// Rotate Array

/*
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

Hint:
Could you do it in-place with O(1) extra space?
*/

class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        if (nums.size() < 2 || k < 1) {
            return;
        }
        
        k = k % nums.size();
        vector<int> nnew = nums; // copy reference
        
        int temp = nums[0];
        for (int i=0; i < nums.size(); i++) {
            nums[i] = nnew[(nums.size() + i - k) % nums.size()];
        }
    }
};