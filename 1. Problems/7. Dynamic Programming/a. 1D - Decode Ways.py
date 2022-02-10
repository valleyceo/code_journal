# LC 91. Decode Ways

'''
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"

To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.

Example 1:

Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:

Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:

Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").

Constraints:

1 <= s.length <= 100
s contains only digits and may contain leading zero(s).
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        
        return self.bottomUpConst(s)
    
    @lru_cache(maxsize = None)
    def topDown(self, s: str, idx: int) -> int:
        if idx >= len(s):
            return 1
        
        if s[idx] == "0":
            return 0
        
        if idx == len(s) - 1:
            return 1
        
        count = self.topDown(s, idx + 1)
        
        if int(s[idx:idx+2]) < 27:
            count += self.topDown(s, idx + 2)
            
        return count
    
    
    def bottomUp(self, s: str) -> int:
        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1
        dp[1] = 0 if s[0] == "0" else 1
        
        for i in range(2, len(dp)):
            if s[i - 1] != "0":
                dp[i] = dp[i - 1]
                
            two_digit = int(s[i-2 : i])
            if two_digit >= 10 and two_digit <= 26:
                dp[i] += dp[i - 2]
        
        return dp[-1]
    
    def bottomUpConst(self, s: str) -> int:
        if s[0] == "0":
            return 0
        
        one_back = 1
        two_back = 1
        
        for i in range(1, len(s)):
            current = 0
            
            if s[i] != "0":
                current = one_back
            
            two_digit = int(s[i - 1 : i + 1])
            if two_digit >= 10 and two_digit <= 26:
                current += two_back
            
            two_back = one_back
            one_back = current
        
        return one_back