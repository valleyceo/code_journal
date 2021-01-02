"""
LC 76. Minimum Window Substring

Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".

Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Example 2:

Input: s = "a", t = "a"
Output: "a"

Constraints:

1 <= s.length, t.length <= 105
s and t consist of English letters.

Follow up: Could you find an algorithm that runs in O(n) time?
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(s) < len(t):
            return ""
        
        hm = collections.Counter(t)
        comp = len(t)
        minStr = ""
        tail = 0
        
        for idx in range(len(s)):
            if hm[s[idx]] > 0:
                comp -= 1
            
            hm[s[idx]] -= 1
            
            while comp == 0:
                length = idx - tail + 1
                
                if len(minStr) == 0 or len(minStr) > length:
                    minStr = s[tail:idx+1]
                
                hm[s[tail]] += 1
                
                if hm[s[tail]] > 0:
                    comp += 1
                
                tail += 1
                
        return minStr