# LC 486. Predict the Winner

'''
You are given an integer array nums. Two players are playing a game with this array: player 1 and player 2.

Player 1 and player 2 take turns, with player 1 starting first. Both players start the game with a score of 0. At each turn, the player takes one of the numbers from either end of the array (i.e., nums[0] or nums[nums.length - 1]) which reduces the size of the array by 1. The player adds the chosen number to their score. The game ends when there are no more elements in the array.

Return true if Player 1 can win the game. If the scores of both players are equal, then player 1 is still the winner, and you should also return true. You may assume that both players are playing optimally.

Example 1:

Input: nums = [1,5,2]
Output: false
Explanation: Initially, player 1 can choose between 1 and 2.
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2).
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5.
Hence, player 1 will never be the winner and you need to return false.
'''
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        return self.bottomUp1D(nums)

    def mySolution(self, nums: List[int]) -> bool:
        def canwin(psum, left, right, p1_turn):

            if right == left:
                if psum + nums[left] > 0:
                    return True
                elif p1_turn and psum + nums[left] == 0:
                    return True
                else:
                    return False

            if not canwin(-(psum + nums[right]), left, right - 1, not p1_turn):
                return True

            if not canwin(-(psum + nums[left]), left + 1, right, not p1_turn):
                return True

            return False

        return canwin(0, 0, len(nums) - 1, True)

    # O(n^2) time | O(n^2) space, memo
    def topDownSolution(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def winner(left, right):
            if left == right:
                return nums[left]

            choose_left = nums[left] - winner(left + 1, right)
            choose_right = nums[right] - winner(left, right - 1)

            return max(choose_left, choose_right)

        return winner(0, len(nums) - 1) >= 0

    # O(n^2) time | O(n^2) space
    def bottomUpSolution(self, nums: List[int]) -> bool:
        dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))]

        for l in range(len(nums) - 1, -1, -1):
            for r in range(l, len(nums)):
                if l == r:
                    dp[l][r] = nums[l]
                else:
                    lc = nums[l] - dp[l + 1][r]
                    rc = nums[r] - dp[l][r - 1]
                    dp[l][r] = max(lc, rc)

        return dp[0][len(nums) - 1] >= 0

    # O(n^2) time | O(n) space
    def bottomUp1D(self, nums: List[int]) -> bool:
        dp = [0 for _ in range(len(nums))]

        for l in range(len(nums) - 1, -1, -1):
            for r in range(l, len(nums)):
                if l == r:
                    dp[r] = nums[l]
                else:
                    lc = nums[l] - dp[r]
                    rc = nums[r] - dp[r - 1]
                    dp[r] = max(lc, rc)

        return dp[len(nums) - 1] >= 0
