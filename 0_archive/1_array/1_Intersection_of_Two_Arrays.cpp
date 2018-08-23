// Intersection of Two Arrays

/*
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.
*/

// my solution - time: O(n1log(n1) + n2log(n2))
// **on a set, if N elements are inserted, Nlog(size+N).
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> uset;
        vector<int> res;
        
        for (auto a : nums1)
            uset.insert(a);
        
        for (auto b : nums2) {
            if (uset.find(b) != uset.end()) {
                res.push_back(b);
                uset.erase(b);
            }
        }
        
        return res;
    }
};