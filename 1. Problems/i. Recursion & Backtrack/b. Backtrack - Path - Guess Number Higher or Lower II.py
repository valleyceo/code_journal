# LC 375. Guess Number Higher or Lower II

'''
We are playing the Guessing Game. The game will work as follows:

I pick a number between 1 and n.
You guess a number.
If you guess the right number, you win the game.
If you guess the wrong number, then I will tell you whether the number I picked is higher or lower, and you will continue guessing.
Every time you guess a wrong number x, you will pay x dollars. If you run out of money, you lose the game.
Given a particular n, return the minimum amount of money you need to guarantee a win regardless of what number I pick.
'''
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        return self.bottomUp(n)

    # O(n^3) time | O(n^2) space
    def topDown(self, n: int) -> int:
        @lru_cache(None)
        def helper(left, right):
            if (right - left) < 1:
                return 0
            elif (right - left) == 1:
                return min(left, right)

            res = float('inf')

            for i in range(left + 1, right):
                max_val = max(i + helper(i+1, right), i + helper(left, i-1))
                res = min(res, max_val)

            return res


        return helper(1, n)

    # O(n^3) time | O(n^2) space
    def bottomUp(self, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

        for L in range(1, n+1):
            for left in range(1, n - L + 1):

                right = left + L

                if L == 1:
                    dp[left][right] = left
                    continue

                min_val = float('inf')

                for mid in range(left + 1, right):
                    max_val = max(dp[left][mid-1], dp[mid+1][right]) + mid
                    min_val = min(min_val, max_val)

                dp[left][right] = min_val

        return dp[1][-1]
