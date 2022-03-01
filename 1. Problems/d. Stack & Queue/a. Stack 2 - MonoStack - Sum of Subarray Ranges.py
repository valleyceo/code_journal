# 2104. Sum of Subarray Ranges

'''
You are given an integer array nums. The range of a subarray of nums is the difference between the largest and smallest element in the subarray.

Return the sum of all subarray ranges of nums.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [1,2,3]
Output: 4
Explanation: The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0
[2], range = 2 - 2 = 0
[3], range = 3 - 3 = 0
[1,2], range = 2 - 1 = 1
[2,3], range = 3 - 2 = 1
[1,2,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.

Example 2:

Input: nums = [1,3,3]
Output: 4
Explanation: The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0
[3], range = 3 - 3 = 0
[3], range = 3 - 3 = 0
[1,3], range = 3 - 1 = 2
[3,3], range = 3 - 3 = 0
[1,3,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 2 + 0 + 2 = 4.
Example 3:

Input: nums = [4,-2,-3,4,1]
Output: 59
Explanation: The sum of all subarray ranges of nums is 59.

Constraints:
1 <= nums.length <= 1000
-109 <= nums[i] <= 109
'''

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        return self.onePass(nums)

    # O(n) time | O(n) space
    def onePass(self, nums: List[int]) -> int:
        res = 0
        inf = float('inf')

        Amin = [-inf] + nums + [-inf]
        Amax = [inf] + nums + [inf]

        stack = []
        for i, val in enumerate(Amin):
            while stack and Amin[stack[-1]] > val:
                j = stack.pop()
                k = stack[-1]
                res -= Amin[j] * (i - j) * (j - k)

            stack.append(i)

        stack = []
        for i, val in enumerate(Amax):
            while stack and Amax[stack[-1]] < val:
                j = stack.pop()
                k = stack[-1]
                res += Amax[j] * (i - j) * (j - k)

            stack.append(i)

        return res

    # O(n^2) time | O(1) space
    def twoPass(self, nums: List[int]) -> int:
        res = 0

        for i in range(len(nums)):
            minVal = nums[i]
            maxVal = nums[i]

            for j in range(i + 1, len(nums)):
                minVal = min(minVal, nums[j])
                maxVal = max(maxVal, nums[j])
                res += maxVal - minVal

        return res
