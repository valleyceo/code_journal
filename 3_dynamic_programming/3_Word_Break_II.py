"""
LC 140. Word Break II

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.wset = set()
        self.minLen = sys.maxsize
        self.maxLen = 0
        self.cache = {}
        
        for word in wordDict:
            self.wset.add(word)
            self.minLen = min(self.minLen, len(word))
            self.maxLen = max(self.maxLen, len(word))
        
        return self.backtrack(s)
    
    def backtrack(self, s: str) -> List[str]:
        res = []
        if s in self.wset:
            res.append(s)
        
        if s in self.cache:
            return self.cache[s]
        
        for i in range(self.minLen, min(len(s), self.maxLen+1)):
            if s[:i] in self.wset:
                spaths = self.backtrack(s[i:])
                for path in spaths:
                    res.append(s[:i] + " " + path)
        
        self.cache[s] = res
        return res