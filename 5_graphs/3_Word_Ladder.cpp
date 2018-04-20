// Word Ladder

/*
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
*/

// my solution
class Solution {
public:
    void addNextWords(string word, unordered_set<string>& wordDict, queue<string>& toVisit) {
        wordDict.erase(word);
        
        for (int p = 0; p < (int)word.length(); p++) {
            char letter = word[p];
            
            for (int k = 0; k < 26; k++) {
                word[p] = 'a' + k;
                
                if (wordDict.find(word) != wordDict.end()) {
                    toVisit.push(word);
                    wordDict.erase(word);
                }
            }
            
            word[p] = letter;
        }
    }
        
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> wordDict(wordList.begin(), wordList.end());
        queue<string> toVisit;
        
        addNextWords(beginWord, wordDict, toVisit);
        int dist = 2;
        
        while (!toVisit.empty()) {
            int num = toVisit.size();
            
            for (int i = 0; i < num; i++) {
                string word = toVisit.front();
                toVisit.pop();
                
                if (word == endWord)
                    return dist;
                
                addNextWords(word, wordDict, toVisit);
            }
            dist++;
        }
        
        return 0;
    }
};