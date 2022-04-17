# LC 473. Matchsticks to Square

'''
You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Return true if you can make this square and false otherwise.
'''

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        return self.dpSolution(matchsticks)

    # O(4^N) time | O(N) space
    def dfsSolution(self, matchsticks: List[int]) -> bool:
        n = len(matchsticks)
        total = sum(matchsticks)
        q_len = total // 4

        if total % 4 != 0:
            return False

        matchsticks.sort(reverse = True)
        sums = [0 for _ in range(4)]

        def dfs(idx):
            if idx == n:
                return sums[0] == sums[1] == sums[2] == q_len

            for i in range(4):
                if sums[i] + matchsticks[idx] <= q_len:
                    sums[i] += matchsticks[idx]

                    if dfs(idx + 1):
                        return True

                    sums[i] -= matchsticks[idx]

            return False

        return dfs(0)

    # O(N * 2^N) time | O(N + 2^N) space
    def dpSolution(self, nums: List[int]) -> bool:
        L = len(nums)
        perimeter = sum(nums)
        possible_side = perimeter // 4

        if perimeter % 4 != 0:
            return False

        memo = {}

        def recurse(mask, sides_done):

            total = 0

            # Find total sum of used (1 is unused, 0 is used)
            for i in range(L - 1, -1, -1):
                if not (mask & (1 << i)):
                    total += nums[L - 1 - i]

            if total > 0 and total % possible_side == 0:
                sides_done += 1

            if sides_done == 3:
                return True

            if (mask, sides_done) in memo:
                return memo[(mask, sides_done)]

            res = False

            c = int(total / possible_side)
            rem = possible_side * (c + 1) - total

            for i in range(L - 1, -1, -1):
                if nums[L - 1 - i] <= rem and mask & (1 << i):
                    if recurse(mask ^ (1 << i), sides_done):
                        res = True
                        break

            memo[(mask, sides_done)] = res
            return res

        return recurse((1 << L) - 1, 0)
