// Find Minimum in Rotated Sorted Array

/*
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0

*/

// my solution
class Solution {
public:
    int findMin(vector<int>& nums) {
        int min_idx = 0;
        int max_idx = nums.size()-1;
        
        while (min_idx < max_idx) {
            if (nums[min_idx] < nums[max_idx])
                return nums[min_idx];
                
            int mid = min_idx + (max_idx - min_idx) / 2;
            
            if (nums[mid] >= nums[min_idx]) {
                min_idx = mid+1;
            } else {
                max_idx = mid;
            }
        }
        return nums[min_idx];
    }
};