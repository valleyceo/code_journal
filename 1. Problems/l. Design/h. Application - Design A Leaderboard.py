# LC 1244. Design A Leaderboard

'''
Design a Leaderboard class, which has 3 functions:

addScore(playerId, score): Update the leaderboard by adding score to the given player's score. If there is no player with such id in the leaderboard, add him to the leaderboard with the given score.
top(K): Return the score sum of the top K players.
reset(playerId): Reset the score of the player with the given id to 0 (in other words erase it from the leaderboard). It is guaranteed that the player was added to the leaderboard before calling this function.
Initially, the leaderboard is empty.
'''

from sortedcontainers import SortedDict

# Time: O(logN) addScore, O(logN) reset, O(K) top | Space: O(N)
class Leaderboard:

    def __init__(self):
        self.scores = SortedDict()
        self.players = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        prev_score = 0

        if playerId in self.players:
            prev_score = self.players[playerId]
            self.scores[prev_score] -= 1

            if self.scores[prev_score] == 0:
                del self.scores[prev_score]

        new_score = score + prev_score

        if new_score not in self.scores:
            self.scores[new_score] = 0

        self.scores[new_score] += 1
        self.players[playerId] = new_score

    def top(self, K: int) -> int:
        res = 0
        rem = K

        for score, count in reversed(self.scores.items()):
            used = min(rem, count)
            res += used * score
            rem -= used

            if rem == 0:
                break

        return res

    def reset(self, playerId: int) -> None:
        if playerId not in self.players:
            return

        score = self.players[playerId]
        self.scores[score] -= 1

        if self.scores[score] == 0:
            del self.scores[score]

        del self.players[playerId]

# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
