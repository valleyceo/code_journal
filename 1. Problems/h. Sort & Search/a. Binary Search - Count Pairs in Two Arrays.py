# 1885. Count Pairs in Two Arrays

"""
Given two integer arrays nums1 and nums2 of length n, count the pairs of indices (i, j) such that i < j and nums1[i] + nums1[j] > nums2[i] + nums2[j].

Return the number of pairs satisfying the condition.
"""

class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        return self.twoPointer(nums1, nums2)

    def binSearch(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        diff = []

        for n1, n2 in zip(nums1, nums2):
            diff.append(n2 - n1)

        diff.sort()

        def binary_search(arr, start, n):
            left = start
            right = len(arr)

            while left < right:
                mid = (left + right) // 2

                if n > arr[mid]:
                    left = mid + 1
                else:
                    right = mid

            return left

        res = 0

        for i in range(len(diff)):
            idx = binary_search(diff, i + 1, -diff[i])
            res += idx - (i + 1)

        return res

    def twoPointer(self, nums1: List[int], nums2: List[int]) -> int:
        arr = [n1 - n2 for n1, n2 in zip(nums1, nums2)]
        arr.sort()

        left = 0
        right = len(arr) - 1
        res = 0

        while left < right:
            if arr[left] + arr[right] > 0:
                res += right - left
                right -= 1
            else:
                left += 1

        return res
