# LC 1793. Maximum Score of a Good Subarray

'''
You are given an array of integers nums (0-indexed) and an integer k.

The score of a subarray (i, j) is defined as min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1). A good subarray is a subarray where i <= k <= j.

Return the maximum possible score of a good subarray.

Example 1:

Input: nums = [1,4,3,7,4,5], k = 3
Output: 15
Explanation: The optimal subarray is (1, 5) with a score of min(4,3,7,4,5) * (5-1+1) = 3 * 5 = 15.
Example 2:

Input: nums = [5,5,4,5,4,1,1,1], k = 0
Output: 20
Explanation: The optimal subarray is (0, 4) with a score of min(5,5,4,5,4) * (4-0+1) = 4 * 5 = 20.
'''
# O(n) time | O(1) space
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = nums[k]
        min_val = nums[k]

        left = k
        right = k

        while left > 0 or right < n - 1:
            next_left = nums[left - 1] if left > 0 else 0
            next_right = nums[right + 1] if right < n - 1 else 0

            if next_left < next_right:
                right += 1
            else:
                left -= 1

            min_val = min(min_val, nums[left], nums[right])
            res = max(res, min_val * (right - left + 1))

        return res
