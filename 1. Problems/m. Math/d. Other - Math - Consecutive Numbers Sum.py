# LC 829. Consecutive Numbers Sum

'''
Given an integer n, return the number of ways you can write n as the sum of consecutive positive integers.

Example 1:

Input: n = 5
Output: 2
Explanation: 5 = 2 + 3

Example 2:

Input: n = 9
Output: 3
Explanation: 9 = 4 + 5 = 2 + 3 + 4

Example 3:

Input: n = 15
Output: 4
Explanation: 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
'''

class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        return self.consecutiveNumbersSum(n)

    # O(sqrt(n)) time | O(1) space
    def consecutiveNumbersSum(self, n: int) -> int:
        count = 0
        max_k = floor(sqrt(2*n + 1/4) - 1/2)

        for k in range(1, max_k + 1):
            if (n - k * (k + 1) // 2) % k == 0:
                count += 1

        return count


"""
Derivation:
- Solve arithmetic sequence sum formula: N = a*k + (k+1)*k/2
- Add constraint a >= 0 and solve
- k <= sqrt(2*N + 1/4) - 1/2
"""
