# LC 2366. Minimum Replacements to Sort the Array

'''
You are given a 0-indexed integer array nums. In one operation you can replace any element of the array with any two elements that sum to it.

For example, consider nums = [5,6,7]. In one operation, we can replace nums[1] with 2 and 4 and convert nums to [5,2,4,7].
Return the minimum number of operations to make an array that is sorted in non-decreasing order.
'''
# O(n) time | O(1) space
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        prev = nums[-1]

        for i in range(n - 2, -1, -1):
            k = ceil(nums[i] / prev)
            res += k - 1
            prev = nums[i] // k

        return res

"""
Note:
- Solve from right to left to know ceiling value
- minimum number of splits needed = ceil(curr_val / ceiling_value)
- new ceiling value = curr_val // min_num_of_splits_needed
"""
