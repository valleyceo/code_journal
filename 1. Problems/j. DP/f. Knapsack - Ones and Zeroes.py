# LC 474. Ones and Zeroes

'''
You are given an array of binary strings strs and two integers m and n.

Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

A set x is a subset of a set y if all elements of x are also elements of y.

Example 1:

Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
{"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.

Example 2:

Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: The largest subset is {"0", "1"}, so the answer is 2.
'''
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        return self.knapsack(strs, m, n)

    # O(N!*L) time | O(1) space
    def topDownTLE(self, strs: List[str], m: int, n: int) -> int:
        @lru_cache(None)
        def helper(i, m_rem, n_rem):
            best_len = 0

            for idx in range(i, len(strs)):
                zeros = strs[idx].count('0')
                ones = strs[idx].count('1')

                if m_rem >= zeros and n_rem >= ones:
                    best_len = max(best_len, helper(idx + 1, m_rem - zeros, n_rem - ones) + 1)

            return best_len

        return helper(0, m, n)

    # O(L*m*n) time, L is the length of strs | O(m * n) space
    def knapsack(self, strs: List[str], m: int, n: int) -> int:

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for s in strs:
            zeros = s.count("0")
            ones = s.count("1")

            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones] + 1)

        return dp[-1][-1]
