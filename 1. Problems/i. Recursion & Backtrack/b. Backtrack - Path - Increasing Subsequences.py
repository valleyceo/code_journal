# LC 491. Increasing Subsequences

'''
Given an integer array nums, return all the different possible increasing subsequences of the given array with at least two elements. You may return the answer in any order.

The given array may contain duplicates, and two equal integers should also be considered a special case of increasing sequence.

Example 1:

Input: nums = [4,6,7,7]
Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]

Example 2:

Input: nums = [4,4,3,2,1]
Output: [[4,4]]
'''
# O(2^N) time | O(N) space
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        def backtrack(idx, path):
            nonlocal res

            if len(path) >= 2:
                res.append(path[:])

            used = set()

            for i in range(idx, len(nums)):
                if path and nums[i] < path[-1]:
                    continue

                if nums[i] in used:
                    continue

                used.add(nums[i])
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        res = []
        backtrack(0, [])
        return res
