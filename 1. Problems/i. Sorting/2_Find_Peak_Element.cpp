// Find Peak Element

/*
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

Note:
Your solution should be in logarithmic complexity.
*/

// my solution - O(N)
class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        if (nums.size() == 1) {
            return 0;
        }
        
        for (int i = 0; i < nums.size(); i++) {
            if ((i == 0 && nums[i] > nums[i+1]) ||
                (i == nums.size() - 1 && nums[i-1] < nums[i]) ||
                (nums[i-1] < nums[i] && nums[i] > nums[i+1])){
                return i;
            }
                
        }
    }
};