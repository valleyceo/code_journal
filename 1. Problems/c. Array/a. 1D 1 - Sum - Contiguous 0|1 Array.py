# LC 525. Contiguous Array

'''
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.
'''
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        return self.arraySolution(nums)

    def arraySolution(self, nums: List[int]) -> int:
        arr = [-2] * (len(nums) * 2 + 1)
        arr[len(nums)] = -1

        maxLen = 0
        count = len(nums)

        for i, n in enumerate(nums):
            count += (1 if n == 1 else -1)

            if (arr[count]) >= -1:
                maxLen = max(maxLen, i - arr[count])
            else:
                arr[count] = i

        return maxLen

    # O(n) time | O(n) space
    def hashmapSolution(self, nums: List[int]) -> int:
        nmap = {}
        nmap[0] = -1

        count = 0
        maxLen = 0

        for i, n in enumerate(nums):
            count += (1 if n == 1 else -1)

            if count in nmap:
                maxLen = max(maxLen, i - nmap[count])
            else:
                nmap[count] = i

        return maxLen
