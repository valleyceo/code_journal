# LC 837. New 21 Game

'''
Alice plays the following game, loosely based on the card game "21".

Alice starts with 0 points and draws numbers while she has less than k points. During each draw, she gains an integer number of points randomly from the range [1, maxPts], where maxPts is an integer. Each draw is independent and the outcomes have equal probabilities.

Alice stops drawing numbers when she gets k or more points.

Return the probability that Alice has n or fewer points.

Answers within 10-5 of the actual answer are considered accepted.

Example 1:

Input: n = 10, k = 1, maxPts = 10
Output: 1.00000
Explanation: Alice gets a single card, then stops.
'''
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        return self.topDown(n, k, maxPts)

    def topDownNaive(self, n: int, k: int, maxPts: int) -> float:

        def dfs(curr):
            if curr >= k:
                return 1 if curr <= n else 0

            p = 0

            for i in range(1, maxPts + 1):
                p += dfs(curr + i)

            p /= maxPts
            return p

        return dfs(0)

    def topDown(self, n: int, k: int, maxPts: int) -> float:

        @lru_cache(None)
        def dfs(curr):
            if curr == k - 1:
                return min(n - k + 1, maxPts) / maxPts

            if curr > n:
                return 0
            elif curr >= k:
                return 1.0

            return dfs(curr + 1) - (dfs(curr + 1 + maxPts) - dfs(curr + 1)) / maxPts

        return dfs(0)

    def onePass(self, n: int, k: int, maxPts: int) -> float:

        if k == 0 or n >= k + maxPts:
            return 1

        dp = [1] + [0] * n
        maxSum = 1

        for i in range(1, n + 1):
            dp[i] = maxSum / maxPts

            if i < k:
                maxSum += dp[i]

            if i >= maxPts:
                maxSum -= dp[i - maxPts]

        return sum(dp[k:])


"""
Insight:
- When maxPts = 3:
    - dp(n)=dp(n-3)*(1/3)+dp(n-2)*(1/3)+dp(n-1)*(1/3)
    or simpler -> dp(n)=(dp(n-1)+dp(n-2)+dp(n-3)) // maxPts
"""
