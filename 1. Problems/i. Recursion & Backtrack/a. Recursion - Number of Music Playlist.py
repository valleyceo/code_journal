# LC 920. Number of Music Playlists

'''
Your music player contains n different songs. You want to listen to goal songs (not necessarily different) during your trip. To avoid boredom, you will create a playlist so that:

Every song is played at least once.
A song can only be played again only if k other songs have been played.
Given n, goal, and k, return the number of possible playlists that you can create. Since the answer can be very large, return it modulo 109 + 7.

Example 1:

Input: n = 3, goal = 3, k = 1
Output: 6
Explanation: There are 6 possible playlists: [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], and [3, 2, 1].
'''

class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        return self.bottomUpSolution(n, goal, k)

    # O(NL) time | O(NL) space
    def topDownSolution(self, songs: int, play_len: int, gap: int) -> int:
        mod = 10**9 + 7

        @lru_cache(None)
        def dp(rem_plays, rem_unique):
            if rem_plays == 0:
                return rem_unique == 0

            # use unique
            res = dp(rem_plays - 1, rem_unique - 1) * rem_unique

            # reuse same
            res += dp(rem_plays - 1, rem_unique) * max(songs - rem_unique - gap, 0)

            return res % mod

        return dp(play_len, songs)

    # O(NL) time | O(L) space
    def bottomUpSolution(self, songs: int, play_len: int, gap: int) -> int:
        mod = 10**9 + 7

        dp = [1] * (play_len - songs + 1)

        for p in range(2, songs - gap + 1):
            for i in range(1, play_len - songs + 1):
                dp[i] += dp[i - 1] * p

        res = dp[-1]

        for k in range(2, songs + 1):
            res *= k

        return res % mod
