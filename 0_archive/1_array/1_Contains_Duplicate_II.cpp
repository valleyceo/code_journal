// Contains Duplicate II

/*
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:
Input: [1,2,3,1], k = 3
Output: true (0, 3)

Example 2:
Input: [1,0,1,1], k = 1
Output: true (2, 3)

Example 3:
Input: [1,2,1], k = 0
Output: false

*/

// my solution - time: O(n), space: O(n)
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        if (k < 1) return false;
        
        unordered_map<int, int> umap;
        
        for (int i = 0; i < nums.size(); i++) {
            umap[nums[i]]++;
            
            if (umap[nums[i]] == 2)
                return true;
            
            if (i >= k)
                umap[nums[i-k]]--;
        }
        
        return false;
    }
};

// alternate
// my solution (optimal) - time: O(n), space: O(k)
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        if (k < 1) return false;
        
        unordered_set<int> uset;
        
        for (int i = 0; i < nums.size(); i++) {
            if (uset.find(nums[i]) != uset.end())
                return true;
            
            uset.insert(nums[i]);
            
            if (i >= k) 
                uset.erase(nums[i-k]);
        }
        
        return false;
    }
};