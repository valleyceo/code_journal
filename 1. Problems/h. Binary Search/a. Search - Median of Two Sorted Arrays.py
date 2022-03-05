# LC 4. Median of Two Sorted Arrays

'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 10^6
'''
# O(log(min(M, N))) time | O(1) space
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)

        left_size = (m + n + 1) // 2
        left = 0
        right = m
        is_even = ((m + n) % 2) == 0

        while left <= right:
            p1Idx = (left + right) // 2
            p2Idx = left_size - p1Idx

            # if partition 1 is 0 it means nothing is there on left side. (Use -INF)
            # if partition 1 is m, there is nothing on right side. (Use INF)
            p1LeftMax = float("-inf") if p1Idx == 0 else nums1[p1Idx - 1]
            p1RightMin = float("inf") if p1Idx == m else nums1[p1Idx]

            p2LeftMax = float("-inf") if p2Idx == 0 else nums2[p2Idx - 1]
            p2RightMin = float("inf") if p2Idx == n else nums2[p2Idx]

            if p1LeftMax <= p2RightMin and p2LeftMax <= p1RightMin:
                if is_even:
                    return (max(p1LeftMax, p2LeftMax) + min(p1RightMin, p2RightMin)) / 2
                else:
                    return max(p1LeftMax, p2LeftMax)

            elif p1LeftMax > p2RightMin:
                right = p1Idx - 1
            else:
                left = p1Idx + 1
