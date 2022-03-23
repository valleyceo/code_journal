# LC 90. Subsets II

'''
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:

Input: nums = [0]
Output: [[],[0]]
'''
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        return self.maskingSolution(nums)

    def backtrackSolution(self, nums: List[int]) -> List[List[int]]:
        def backtrack(idx, path):
            if idx == N:
                res.append(path[:])
                return

            path.append(nums[idx])
            backtrack(idx + 1, path)
            path.pop()

            while idx + 1 < N and nums[idx] == nums[idx + 1]:
                idx += 1

            backtrack(idx + 1, path)

        N = len(nums)
        res = []
        nums.sort()
        backtrack(0, [])
        return res

    def maskingSolution(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        res = []
        nums.sort()

        for mask in range(1 << N):
            tmp = []

            for i in range(N):
                if (mask >> i) & 1:
                    tmp.append(nums[i])

            if tmp not in res:
                res.append(tmp)

        return res
