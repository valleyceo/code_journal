// Contains Duplicate III

/*
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
*/

// my solution (optimal) - time: O(n * log(k)), space: O(k)
class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
        if (k < 1 || nums.size() < 2)
            return false;
        
        map<long long, int> omap;
        
        for (int i = 0; i < nums.size(); i++) {
            if (i > k) {
                omap.erase(nums[i-k-1]);
            }
            
            map<long long, int>::iterator lb = omap.lower_bound((long long)nums[i] - t);
            if (lb != omap.end() && (lb->first - nums[i]) <= t)
                return true;
            
            omap[nums[i]]++;
        }
        
        return false;
    }
};