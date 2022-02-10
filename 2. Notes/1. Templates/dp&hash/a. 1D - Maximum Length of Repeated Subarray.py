# LC 718. Maximum Length of Repeated Subarray

'''
Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

Example 1:

Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].

Example 2:

Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 100
'''
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        return self.dp(nums1, nums2)
        
    def binarySearch(self, A: List[int], B: List[int]) -> int:
        def check(length):
            seen = set(tuple(A[i:i+length]) 
                       for i in range(len(A) - length + 1))
            
            return any(tuple(B[j:j+length]) in seen 
                       for j in range(len(B) - length + 1))

        lo, hi = 0, min(len(A), len(B)) + 1
        while lo < hi:
            mi = (lo + hi) // 2
            if check(mi):
                lo = mi + 1
            else:
                hi = mi
        return lo - 1
        
        
    def dp(self, nums1: List[int], nums2: List[int]) -> int:
        l1 = len(nums1)
        l2 = len(nums2)
        
        dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]
        
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
        
        return max([max(r) for r in dp])