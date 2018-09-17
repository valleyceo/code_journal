// Move Zeroes

/*
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
*/

// my solution - optimal
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int i = 0, idx = 0;

        while (idx < nums.size()){
            if (nums[idx] != 0) {
               nums[i++] = nums[idx++]; 
            } else {
                idx++;
            }
        }
        
        while (i < nums.size()) {
            nums[i++] = 0;
        }
        
        return;
    }
};


/* Note
- Time Complexity: O(n)
- Space Complexity: O(1)
*/