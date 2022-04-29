# LC 321. Create Maximum Number

'''
You are given two integer arrays nums1 and nums2 of lengths m and n respectively. nums1 and nums2 represent the digits of two numbers. You are also given an integer k.

Create the maximum number of length k <= m + n from digits of the two numbers. The relative order of the digits from the same array must be preserved.

Return an array of the k digits representing the answer.

Example 1:

Input: nums1 = [3,4,6,5], nums2 = [9,1,2,5,8,3], k = 5
Output: [9,8,6,5,3]

Example 2:

Input: nums1 = [6,7], nums2 = [6,0,4], k = 5
Output: [6,7,6,0,4]

Example 3:

Input: nums1 = [3,9], nums2 = [8,9], k = 3
Output: [9,8,9]
'''

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def maxArr(arr, k):
            res = []

            for i, v in enumerate(arr):
                while res and res[-1] < v and len(res) + len(arr) - i > k:
                    res.pop()

                if len(res) < k:
                    res.append(v)

            return res

        res = [0] * k

        for i in range(k + 1):
            if k - len(nums2) <= i <= len(nums1):
                arr1 = maxArr(nums1, i)
                arr2 = maxArr(nums2, k - i)
                cand = []
                i1 = 0
                i2 = 0

                while i1 < len(arr1) or i2 < len(arr2):
                    if arr1[i1:] >= arr2[i2:]:
                        cand.append(arr1[i1])
                        i1 += 1
                    else:
                        cand.append(arr2[i2])
                        i2 += 1

                res = max(res, cand)

        return res

"""
Insight:
- Two separate problems
    1. Given array of nums and length k, find the largest number from subsequence
    2. Given two nums and k, split distribution and merge two. Then find the largest number
        - Ex: k = 4 -> MAX(fmax(arr1, 1)-fmax(arr2,3), fmax(arr1, 2)-fmax(arr2, 2)....)
        - Merge by largest remaining string (this algorithm guarantees sequence becomes max)
"""
