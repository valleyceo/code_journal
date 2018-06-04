// Intersection of Two Arrays

/*
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.
*/

// my solution
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int> umap;
        vector<int> res;
        
        for (auto a : nums1)
            umap[a] = 1;
        
        for (auto b : nums2) {
            if (umap.find(b) != umap.end()) {
                res.push_back(b);
                umap.erase(b);
            }
        }
        
        return res;
    }
};