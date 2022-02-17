// Search in Rotated Sorted Array

/*
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
*/

// my solution
class Solution {
public:
    int search(vector<int>& nums, int target) {
        if (nums.empty()) return -1;
        
        int ri = -1;
        bool rot = false;
        
        for (int i = 0; i < nums.size()-1; i++) {
            if (nums[i] > nums[i+1]){
                ri = i+1;
                rot = true;
                break;
            }
        }
        
        if (rot) {
            sort(nums.begin(), nums.end());
        }
        
        int low, mid, high;
        low = 0;
        high = nums.size();
        
        while (low <= high) {
            mid = low + (high - low) / 2;
            
            if (nums[mid] < target) {
                low = mid + 1;
            } else if (nums[mid] > target) {
                high = mid - 1;
            } else {
                if (rot)
                    mid += ri;
                
                if (mid >= nums.size())
                    mid -= nums.size();
                
                return mid;
            }
        }
        
        return -1;
        
    }
};