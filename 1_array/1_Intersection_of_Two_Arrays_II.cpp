// Intersection of Two Arrays II

/*
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
*/

// my solution
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        if (nums1.size() > nums2.size()){
            return intersect(nums2, nums1);
        }
        
        unordered_map<int, int> umap;
        
        for (int i = 0; i < nums1.size(); i++) {
            if (umap.find(nums1[i]) == umap.end()){
                umap[nums1[i]] = 1;
            } else{
                umap[nums1[i]] += 1;
            }
        }
        
        vector<int> ans;
        for (int i = 0; i < nums2.size(); i++) {
            if (umap.find(nums2[i]) == umap.end()){
                continue;
            } else {
                if (umap[nums2[i]] > 0) {
                    ans.push_back(nums2[i]);
                    umap[nums2[i]] -= 1;
                } else {
                    continue;
                }
            }
            
            if(umap.size() == 0) {
                break;
            }
        }
        return ans;
    }
};