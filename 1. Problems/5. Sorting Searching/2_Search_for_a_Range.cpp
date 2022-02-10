// Search for a Range

/*
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
*/

// my solution
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> ans = {-1, -1};
        
        if (nums.size() == 0) {
            return ans;
        }
        
        int low, mid, high;
        low = 0;
        high = nums.size() - 1;
        
        bool found = false;
        
        while (low <= high) {
            mid = low + (high-low) / 2;
            if (nums[mid] > target) {
                high = mid-1;
            } else if (nums[mid] < target) {
                low = mid+1;
            } else {
                found = true;
                break;
            }
        }
        
        if (!found) {
            return ans;
        }
        
        int tl = mid, th = mid;
        while (tl-1 >= 0 && nums[tl-1] == target) {
            tl--;
        }
        
        while (th+1 < nums.size() && nums[th+1] == target) {
            th++;
        }
        
        ans[0] = tl;
        ans[1] = th;
        
        return ans;
    }
};