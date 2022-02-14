// Merge Sorted Array

/*
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
*/

// my solution
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        if (nums2.size() == 0) {
            return;
        }
        
        
        int idx1 = 0, idx2 = 0, idxm = 0;
        vector<int> merged(nums1.size(), 0);
        
        while (true) {
            //cout << nums1[idx1] << " " << nums2[idx2] << endl;
            if ((idx1 == m) && (idx2 == n)){
                break;
            }
            
            if (idx2 == n){
                merged[idxm] = nums1[idx1];
                idx1++;
            } else if (idx1 == m) {
                merged[idxm] = nums2[idx2];
                idx2++;
            } else if (nums1[idx1] >= nums2[idx2]) {
                merged[idxm] = nums2[idx2];
                idx2++;
            } else {
                merged[idxm] = nums1[idx1];
                idx1++;
            }
            //cout << idx1 << " " << idx2 << endl;
            
            idxm++;
            
        }
        
        for (int i=0; i<nums1.size(); i++) {
            nums1[i] = merged[i];
        }
        
        
        return;
    }
};