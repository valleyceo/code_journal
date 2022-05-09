# LC 465. Optimal Account Balancing

'''
You are given an array of transactions transactions where transactions[i] = [fromi, toi, amounti] indicates that the person with ID = fromi gave amounti $ to the person with ID = toi.

Return the minimum number of transactions required to settle the debt.

Example 1:

Input: transactions = [[0,1,10],[2,0,5]]
Output: 2
Explanation:
Person #0 gave person #1 $10.
Person #2 gave person #0 $5.
Two transactions are needed. One way to settle the debt is person #1 pays person #0 and #2 $5 each.

Example 2:

Input: transactions = [[0,1,10],[1,0,1],[1,2,5],[2,0,5]]
Output: 1
Explanation:
Person #0 gave person #1 $10.
Person #1 gave person #0 $1.
Person #1 gave person #2 $5.
Person #2 gave person #0 $5.
Therefore, person #1 only need to give person #0 $4, and all debt is settled.
'''
# O(N) time | O(N) space, where N is the number of ids
class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        cache = {}

        def dfs(b):
            if not b:
                return 0

            key = tuple(b)

            if key in cache:
                return cache[key]

            min_count = float('inf')

            for i in range(1, len(b)):
                if b[i] == -b[0]:
                    return dfs(b[1:i] + b[i+1:]) + 1

                elif b[i] * b[0] < 0:
                    min_count = min(min_count, dfs(b[1:i] + [b[i] + b[0]] + b[i+1:]) + 1)

            cache[key] = min_count
            return min_count

        balance_map = defaultdict(int)

        for id1, id2, val in transactions:
            balance_map[id1] -= val
            balance_map[id2] += val

        balance = []

        for k, val in balance_map.items():
            if val != 0:
                balance.append(val)

        return dfs(balance)
