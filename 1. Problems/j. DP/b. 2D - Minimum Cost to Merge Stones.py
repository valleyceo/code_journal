# LC 1000. Minimum Cost to Merge Stones

'''
There are n piles of stones arranged in a row. The ith pile has stones[i] stones.

A move consists of merging exactly k consecutive piles into one pile, and the cost of this move is equal to the total number of stones in these k piles.

Return the minimum cost to merge all piles of stones into one pile. If it is impossible, return -1.

Example 1:

Input: stones = [3,2,4,1], k = 2
Output: 20
Explanation: We start with [3, 2, 4, 1].
We merge [3, 2] for a cost of 5, and we are left with [5, 4, 1].
We merge [4, 1] for a cost of 5, and we are left with [5, 5].
We merge [5, 5] for a cost of 10, and we are left with [10].
The total cost was 20, and this is the minimum possible.
'''

class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:

        n = len(stones)
        inf = float('inf')
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        @lru_cache(None)
        def dp(i, j, m):
            if (j - i + 1 - m) % (k - 1):
                return inf

            if i == j:
                return 0 if m == 1 else inf

            if m == 1:
                return dp(i, j, k) + prefix[j + 1] - prefix[i]

            return min(dp(i, mid, 1) + dp(mid + 1, j, m - 1) for mid in range(i, j, k - 1))

        res = dp(0, n - 1, 1)
        return res if res < inf else -1

"""
Note:
- https://leetcode.com/problems/minimum-cost-to-merge-stones/discuss/247567/JavaC%2B%2BPython-DP
"""
