# O(nm) time | O(nm) space
def levenshteinDistance(self, w1, w2) -> int:
        n1 = len(w1)
        n2 = len(w2)
        dp = [[0 for _ in range(n1 + 1)] for _ in range(n2 + 1)]

        for i in range(n2 + 1):
            for j in range(n1 + 1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif w2[i-1] == w1[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])

        return dp[-1][-1]
