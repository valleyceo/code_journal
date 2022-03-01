"""
LC 39. Combination Sum

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
Example 4:

Input: candidates = [1], target = 1
Output: [[1]]
Example 5:

Input: candidates = [1], target = 2
Output: [[1,1]]

Constraints:

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
All elements of candidates are distinct.
1 <= target <= 500
"""
# Dynamic Programming: O(nt) time, O(n^2*t) space
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for i in range(target + 1)]
        
        for n in candidates:
            for t in range(target+1):
                if n > t:
                    continue
                elif n == t:
                    dp[t].append([n])
                else:
                    for l in dp[t-n]:
                        dp[t].append(l+[n])
        
        return dp[target]

# Backtracking solution: O(2^n) time, O(n) space
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.cd = candidates
        self.res = []
        self.backtrack(0, target, [])
        return self.res
        
    def backtrack(self, idx: int, target: int, cList: List):
        if idx >= len(self.cd) or target < 0:
            return
        
        if target == 0:
            self.res.append(cList.copy())
            return
        
        cList.append(self.cd[idx])
        self.backtrack(idx, target - self.cd[idx], cList) # Use
        cList.pop()
        self.backtrack(idx + 1, target, cList) # Move