# LC 464. Can I Win

'''
In the "100 game" two players take turns adding, to a running total, any integer from 1 to 10. The player who first causes the running total to reach or exceed 100 wins.

What if we change the game so that players cannot re-use integers?

For example, two players might take turns drawing from a common pool of numbers from 1 to 15 without replacement until they reach a total >= 100.

Given two integers maxChoosableInteger and desiredTotal, return true if the first player to move can force a win, otherwise, return false. Assume both players play optimally.
'''
# O(N * 2^N) time | O(2^N) space
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        def solve(state, rem):
            if state[-1] >= rem:
                return True

            key = tuple(state)
            if key in cache:
                return cache[key]

            for i in range(len(state)):
                next_state = state[:i] + state[i + 1:]

                if not solve(next_state, rem - state[i]):
                    cache[key] = True
                    return True

            cache[key] = False
            return False

        cache = {}
        rem = maxChoosableInteger * (maxChoosableInteger + 1) // 2

        if rem < desiredTotal:
            return False

        state = [i for i in range(1, maxChoosableInteger + 1)]
        return solve(state, desiredTotal)
