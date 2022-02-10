# LC 139. Word Break

'''
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
 
Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.topDown(s, wordDict)
    
    def topDown(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache(None)
        def dp(i):
            if i < 0:
                return True
            
            for word in wordDict:
                if i - (len(word)-1) >= 0 and dp(i - len(word)):
                    if s[i - (len(word) - 1): i + 1] == word:
                        return True
            
            return False
        
        return dp(len(s) - 1)
    
    def bottomUp(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        
        for i in range(len(s)):
            for word in wordDict:
                if  i - (len(word) - 1) >= 0 and (i == len(word) - 1 or dp[i - len(word)]):
                    if s[i - (len(word) - 1) : i + 1] == word:
                        dp[i] = True
                        break
                        
        return dp[-1]