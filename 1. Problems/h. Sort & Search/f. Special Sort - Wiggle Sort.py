# LC 280. Wiggle Sort

'''
Given an integer array nums, reorder it such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

You may assume the input array always has a valid answer.

Example 1:

Input: nums = [3,5,2,1,6,4]
Output: [3,5,1,6,2,4]
Explanation: [1,6,2,5,3,4] is also accepted.

Example 2:

Input: nums = [6,6,5,6,3,8]
Output: [6,6,5,6,3,8]
'''
# O(n) time | O(1) space
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        small = True
        for i in range(1, len(nums)):
            if small:
                if nums[i-1] > nums[i]:
                    nums[i], nums[i-1] = nums[i-1], nums[i]
            else:
                if nums[i-1] < nums[i]:
                    nums[i], nums[i-1] = nums[i-1], nums[i]

            small ^= True
