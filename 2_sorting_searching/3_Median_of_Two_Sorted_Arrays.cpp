// Median of Two Sorted Arrays

/*
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
*/

// my solution
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        if (nums1.size() > nums2.size())
            nums1.swap(nums2);
        
        int size1 = nums1.size();
        int size2 = nums2.size();
        int size = size1+size2;
        
        int mid = (size - 1) / 2;
        int l = 0;
        int r = size1 - 1;
        
        while (l <= r) {
            int m1 = l + ((r-l)>>1);
            int m2 = mid - m1;
            
            if (nums1[m1] > nums2[m2])
                r = m1 - 1;
            else
                l = m1 + 1;
        }
        
        int a = max(r >= 0 ? nums1[r] : INT_MIN, mid-l >= 0 ? nums2[mid-l] : INT_MIN);
        
        if (size % 2 == 1)
            return a;
        
        int b = min(l < size1 ? nums1[l]: INT_MAX, mid-r < size2 ? nums2[mid-r] : INT_MAX);
        return (a + b) / 2.0;
    }
};