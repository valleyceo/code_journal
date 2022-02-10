# LC 97. Interleaving String

'''
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Example 3:

Input: s1 = "", s2 = "", s3 = ""
Output: true

Constraints:

0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200
s1, s2, and s3 consist of lowercase English letters.

Follow up: Could you solve it using only O(s2.length) additional memory space?
'''
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        return self.bottomUp(s1, s2, s3)
        
    def topDown(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        @lru_cache(None)
        def solve(i1, i2):
            if i1 == len(s1) and i2 == len(s2):
                return True
            
            if i1 < len(s1) and s1[i1] == s3[i1 + i2]:
                if solve(i1 + 1, i2):
                    return True
                
            if i2 < len(s2) and s2[i2] == s3[i1 + i2]:
                if solve(i1, i2 + 1):
                    return True
            
            return False
        
        return solve(0, 0)
    
    def bottomUp(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        n1 = len(s1)
        n2 = len(s2)
        dp = [[False] * (n2+1) for _ in range(n1+1)]
        dp[0][0] = True
        
        for i in range(n1+1):
            for j in range(n2+1):
                print(i, j)
                if i > 0 and dp[i-1][j] and s1[i-1] == s3[i + j - 1]:
                    dp[i][j] = True
                elif j > 0 and dp[i][j-1] and s2[j-1] == s3[i + j - 1]:
                    dp[i][j] = True
        
        return dp[-1][-1]