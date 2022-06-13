# LC 1996. The Number of Weak Characters in the Game

'''
You are playing a game that contains multiple characters, and each of the characters has two main properties: attack and defense. You are given a 2D integer array properties where properties[i] = [attacki, defensei] represents the properties of the ith character in the game.

A character is said to be weak if any other character has both attack and defense levels strictly greater than this character's attack and defense levels. More formally, a character i is said to be weak if there exists another character j where attackj > attacki and defensej > defensei.

Return the number of weak characters.

Example:

Input: properties = [[2,2],[3,3]]
Output: 1
Explanation: The first character is weak because the second character has a strictly greater attack and defense.
'''
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        return self.sortSolution(properties)

    def naiveTLE(self, properties: List[List[int]]) -> int:
        properties.sort(reverse = True)
        res = 0

        for i, prop in enumerate(properties):
            prev = 0

            while prev < i:
                if properties[prev][0] > prop[0] and properties[prev][1] > prop[1]:
                    res += 1
                    break
                prev += 1

        return res

    # O(nlogn) time | O(n) space
    def sortSolution(self, properties: List[List[int]]) -> int:
        properties.sort(key = lambda x : (-x[0], x[1]))
        max_d = -1
        res = 0

        for i in range(1, len(properties)):
            max_d = max(max_d, properties[i-1][1])

            if properties[i][1] < max_d:
                res += 1

        return res

    # O(10**5 + n) time | O(10**5) space
    def discretized(self, properties: List[List[int]]) -> int:
        dp = [0] * (10**5 + 2)
        res = 0

        for p in properties:
            dp[p[0]] = max(dp[p[0]], p[1])

        for i in range(10**5, 0, -1):
            dp[i-1] = max(dp[i], dp[i-1])

        for p in properties:
            if p[1] < dp[p[0] + 1]:
                res += 1

        return res

"""
Insight:
- Sort descending on x[0] and ascending on x[1] (max_d)
- max_d will never be smaller on the same max_a (since it is incrementing)
- max_d is smaller only after next max_a
- Example:
    - [[6,4],[6,10],[6,20],[3,19]] -> check max_d decrease from 20 -> 19 (ans = 1)
    - [[6,4],[6,10],[6,20],[3,21]] -> if max_d does not decrease, it does not count (ans = 0)

"""
