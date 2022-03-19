# LC 46. Permutations

'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:

Input: nums = [1]
Output: [[1]]
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(idx = 0) -> None:
            if idx == n:
                res.append(nums[:])

            for i in range(idx, n):
                nums[idx], nums[i] = nums[i], nums[idx]
                backtrack(idx + 1)
                nums[idx], nums[i] = nums[i], nums[idx]

        n = len(nums)
        res = []
        backtrack()
        return res
