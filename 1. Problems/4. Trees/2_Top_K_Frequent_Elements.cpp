// Top K Frequent Elements

/*
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note: 
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
*/

// my solution
//https://leetcode.com/problems/top-k-frequent-elements/discuss/81760/Five-efficient-solutions-in-C++-well-explained

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> umap;
        vector<int> v;
        
        for (int n : nums) {
            umap[n]++;
        }
        
        vector<vector<int>> buckets(nums.size() + 1);
        
        for (auto& pair: umap) buckets[pair.second].push_back(pair.first);
        
        for (int i = nums.size(); i; --i) {
            for (int j = 0; j < buckets[i].size(); ++j) {
                v.push_back(buckets[i][j]);
                if (v.size() == k) return v;
            }
        }
        
        return v;
    }
};