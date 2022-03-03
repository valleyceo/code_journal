# LC 15. 3 Sum

'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:

Input: nums = []
Output: []

Example 3:

Input: nums = [0]
Output: []

Constraints:
0 <= nums.length <= 3000
-105 <= nums[i] <= 10^5
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return self.unsortedSolution(nums)

    # O(n^2) time | O(n) space
    def sortedSolution(self, nums: List[int]) -> List[List[int]]:

        def twoSum(i):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        nums.sort()
        res = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i == 0 or nums[i-1] != nums[i]:
                twoSum(i)

        return res

    # O(n^2) time | O(n) space
    def unsortedSolution(self, nums: List[int]) -> List[List[int]]:
        res = set()
        dupCheck = set()
        seen = {}

        for i, n1 in enumerate(nums):
            if n1 not in dupCheck:
                dupCheck.add(n1)

                for j, n2 in enumerate(nums[i+1:]):
                    complement = -(n1 + n2)

                    if complement in seen and seen[complement] == i:
                        res.add(tuple(sorted([n1, n2, complement])))

                    seen[n2] = i

        return res
