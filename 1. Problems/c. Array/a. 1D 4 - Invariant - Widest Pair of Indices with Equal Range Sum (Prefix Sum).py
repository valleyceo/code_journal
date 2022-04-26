# LC 1983. Widest Pair of Indices With Equal Range Sum

'''
You are given two 0-indexed binary arrays nums1 and nums2. Find the widest pair of indices (i, j) such that i <= j and nums1[i] + nums1[i+1] + ... + nums1[j] == nums2[i] + nums2[i+1] + ... + nums2[j].

The widest pair of indices is the pair with the largest distance between i and j. The distance between a pair of indices is defined as j - i + 1.

Return the distance of the widest pair of indices. If no pair of indices meets the conditions, return 0.

Example 1:

Input: nums1 = [1,1,0,1], nums2 = [0,1,1,0]
Output: 3
Explanation:
If i = 1 and j = 3:
nums1[1] + nums1[2] + nums1[3] = 1 + 0 + 1 = 2.
nums2[1] + nums2[2] + nums2[3] = 1 + 1 + 0 = 2.
The distance between i and j is j - i + 1 = 3 - 1 + 1 = 3.

Example 2:

Input: nums1 = [0,1], nums2 = [1,1]
Output: 1
Explanation:
If i = 1 and j = 1:
nums1[1] = 1.
nums2[1] = 1.
The distance between i and j is j - i + 1 = 1 - 1 + 1 = 1.

Example 3:

Input: nums1 = [0], nums2 = [1]
Output: 0
Explanation:
There are no pairs of indices that meet the requirements.
'''
class Solution:
    def widestPairOfIndices(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        dp1 = [0] * n
        dp2 = [0] * n

        for i in range(n):
            if i > 0:
                dp1[i] = dp1[i-1]
                dp2[i] = dp2[i-1]

            dp1[i] += nums1[i]
            dp2[i] += nums2[i]

        diff_map = {0: -1}
        res = 0

        for i in range(n):
            diff = dp1[i] - dp2[i]

            if diff in diff_map:
                res = max(res, i - diff_map[diff])
            else:
                diff_map[diff] = i

        return res
