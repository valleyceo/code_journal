// Degree of an Array

/*
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
*/

// my solution - time: O(nlog(n)), space: O(n)
class Solution {
public:
    int findShortestSubArray(vector<int>& nums) {
        unordered_map<int, list<int>> umap;
        
        for (int i = 0; i < nums.size(); ++i)
            umap[nums[i]].push_back(i);
        
        int max_deg = 0;
        int min_size = INT_MAX;
        
        for (auto m : umap) {
            int deg = m.second.size();
            int size = m.second.back() - m.second.front() + 1;
            
            if (deg > max_deg || (deg == max_deg && size < min_size)) {
                max_deg = deg;
                min_size = size;
            }
        }
        return min_size;
    }
};