# LC 1155. Number of Dice Rolls With Target Sum

'''
You have n dice and each die has k faces numbered from 1 to k.

Given three integers n, k, and target, return the number of possible ways (out of the kn total ways) to roll the dice so the sum of the face-up numbers equals target. Since the answer may be too large, return it modulo 109 + 7.

Example 1:

Input: n = 1, k = 6, target = 3
Output: 1
Explanation: You throw one die with 6 faces.
There is only one way to get a sum of 3.

Example 2:

Input: n = 2, k = 6, target = 7
Output: 6
Explanation: You throw two dice, each with 6 faces.
There are 6 ways to get a sum of 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
Example 3:

Input: n = 30, k = 30, target = 500
Output: 222616187
Explanation: The answer must be returned modulo 109 + 7.

Constraints:

1 <= n, k <= 30
1 <= target <= 1000
'''
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        return self.topDown(n, k, target)
    
    def topDown(self, n: int, k: int, target: int) -> int:
        
        @lru_cache(None)
        def search(idx: int, path: int) -> int:
            
            if idx == n and path == target:
                return 1
            
            if idx >= n or path >= target:
                return 0
            
            total = 0
            for i in range(1, k + 1):
                total += search(idx + 1, path + i)
            
            return total % mod
        
        mod = (10**9 + 7)
        return search(0, 0)