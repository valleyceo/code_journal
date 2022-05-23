# LC 1567. Maximum Length of Subarray With Positive Product

'''
Given an array of integers nums, find the maximum length of a subarray where the product of all its elements is positive.

A subarray of an array is a consecutive sequence of zero or more values taken out of that array.

Return the maximum length of a subarray with positive product.

Example 1:

Input: nums = [1,-2,-3,4]
Output: 4
Explanation: The array nums already has a positive product of 24.

Example 2:

Input: nums = [0,1,-2,-3,-4]
Output: 3
Explanation: The longest subarray with positive product is [1,-2,-3] which has a product of 6.
Notice that we cannot include 0 in the subarray since that'll make the product 0 which is not positive.

Example 3:

Input: nums = [-1,-2,-3,0,1]
Output: 2
Explanation: The longest subarray with positive product is [-1,-2] or [-2,-3].
'''
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        res = 0
        zero_idx = -1
        neg_idx = -1
        count = 0

        for i, n in enumerate(nums):
            if n == 0:
                zero_idx = i
                neg_idx = i
                count = 0

            elif n < 0:
                count += 1

                if count % 2 == 0:
                    res = max(res, i - zero_idx)
                else:
                    if count == 1:
                        neg_idx = i
                    else:
                        res = max(res, i - neg_idx)
            else:
                if count % 2 == 0:
                    res = max(res, i - zero_idx)
                else:
                    res = max(res, i - neg_idx)

        return res
