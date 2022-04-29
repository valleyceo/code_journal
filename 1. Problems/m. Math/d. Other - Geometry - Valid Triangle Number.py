# LC 611. Valid Triangle Number

'''
Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

Example 1:

Input: nums = [2,2,3,4]
Output: 3
Explanation: Valid combinations are:
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3

Example 2:

Input: nums = [4,2,3,4]
Output: 4
'''
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        return self.twoPointers(nums)

    # O(N^2log(N)) time | O(N) space
    def binarySearch(self, nums: List[int]) -> int:
        def search(mid, large):
            if mid == 0:
                return -1

            left = 0
            right = mid

            while left < right:
                m = (left + right) // 2

                if nums[m] + nums[mid] <= nums[large]:
                    left = m + 1
                else:
                    right = m

            return left

        nums.sort()
        res = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                x = search(i, j)

                if x >= 0:
                    res += (i - x)
        return res

    # O(N^2) time | O(N) space
    def twoPointers(self, nums: List[int]) -> int:
        nums.sort()
        res = 0

        for i in range(len(nums)-1, 1, -1):
            left = 0
            right = i - 1

            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    res += right - left
                    right -= 1
                else:
                    left += 1

        return res
