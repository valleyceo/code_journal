# LC. 360. Sort Transformed Array

'''
Given a sorted integer array nums and three integers a, b and c, apply a quadratic function of the form f(x) = ax2 + bx + c to each element nums[i] in the array, and return the array in a sorted order.

Example 1:

Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
Output: [3,9,15,33]

Example 2:

Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
Output: [-23,-5,1,7]
'''
# O(n) time | O(1) space
class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:

        def quadratic(val):
            return a*val*val + b*val + c

        n = len(nums)
        left = 0
        right = n - 1
        res = [0] * n
        idx = 0 if a <= 0 else n - 1
        di = 1 if a <= 0 else -1

        while left <= right:
            lval = quadratic(nums[left])
            rval = quadratic(nums[right])

            if (a <= 0 and lval < rval) or (a > 0 and lval > rval):
                res[idx] = lval
                left += 1
            else:
                res[idx] = rval
                right -= 1

            idx += di

        return res
