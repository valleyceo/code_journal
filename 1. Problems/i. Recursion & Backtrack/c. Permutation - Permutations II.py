# LC 47. Permutations II

'''
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
'''
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path, counter):
            if len(path) == n:
                res.append(path[:])

            for val, count in counter.items():
                if count == 0:
                    continue

                counter[val] -= 1
                path.append(val)
                backtrack(path, counter)
                path.pop()
                counter[val] += 1

        n = len(nums)
        res = []
        backtrack([], Counter(nums))
        return res
