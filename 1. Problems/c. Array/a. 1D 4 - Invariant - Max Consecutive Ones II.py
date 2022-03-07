# 487. Max Consecutive Ones II

'''
Given a binary array nums, return the maximum number of consecutive 1's in the array if you can flip at most one 0.

Example 1:

Input: nums = [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the maximum number of consecutive 1s. After flipping, the maximum number of consecutive 1s is 4.

Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 4

Constraints:

1 <= nums.length <= 10^5
nums[i] is either 0 or 1.
'''
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        prev = curr = 0
        res = 1

        for n in nums:
            if n == 1:
                curr += 1
            else:
                prev = curr + 1 if curr > 0 else 1
                curr = 0

            res = max(res, curr + prev)

        return res
