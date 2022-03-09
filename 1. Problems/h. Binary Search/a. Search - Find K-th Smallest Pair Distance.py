# 719. Find K-th Smallest Pair Distance

'''
The distance of a pair of integers a and b is defined as the absolute difference between a and b.

Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.

Example 1:

Input: nums = [1,3,1], k = 1
Output: 0
Explanation: Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.
Example 2:

Input: nums = [1,1,1], k = 2
Output: 0
Example 3:

Input: nums = [1,6,1], k = 3
Output: 5
'''
# Binary search + Sliding Window
# O(NlogW + NlogN) time | O(1) space
# N is length of nums, W is nums[-1] - nums[0]
# The second NlogN is from sorting array
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def possible(guess):
            count = 0
            left = 0

            for right, x in enumerate(nums):
                while x - nums[left] > guess:
                    left += 1

                count += right - left

            return count >= k

        nums.sort()
        low = 0
        high = nums[-1] - nums[0]

        while low < high:
            mid = (low + high) // 2

            if possible(mid):
                high = mid
            else:
                low = mid + 1

        return low
