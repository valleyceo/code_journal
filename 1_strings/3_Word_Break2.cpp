// Word Break II

/*
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
*/

// my solution - Optimal, O(MNK) where M is string length, N is number of words in dict, K is average word length
class Solution {
public:
    struct trieNode {
        bool isWord;
        unordered_map<char, trieNode*> next;

        trieNode() {
            isWord = false;
        }
    };
    
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        
        // build Trie
        trie = new trieNode();
        buildTrie(trie, wordDict);
        
        // dp
        unordered_map<int, vector<string> > umap;
        
        return wordSearch(s, 0, umap);
    }
    
    void buildTrie(trieNode* root, vector<string>& wordDict) {
        for (int i = 0; i < wordDict.size(); ++i) {
            trieNode* head = root;
            
            for (const char& c : wordDict[i]) {
                if (head->next.find(c) == head->next.end()) {
                    head->next[c] = new trieNode();
                }
                
                head = head->next[c];
            }
            head->isWord = true;
        }
    }
    
    vector<string> wordSearch(string& s, int pos, unordered_map<int, vector<string> >& memo) {
        vector<string> res;
        
        if (pos == s.length()) {
            res.push_back("");
            return res;
        }
        
        if (memo.count(pos) == 1) {
            return memo[pos];
        }
        
        trieNode* head = trie;
        
        for (int i = pos; i < s.length(); ++i) {
            if (head->next.find(s[i]) == head->next.end())
                break;
            
            head = head->next[s[i]];
            
            if (head->isWord) {
                int len = i - pos + 1;
                string temp = s.substr(pos, len);
                
                if (i < s.size() - 1) {
                    temp += " ";
                }
                auto next = wordSearch(s, i + 1, memo);
                
                for (auto& n : next) {
                    string t = temp + n;
                    res.push_back(t);
                }
            }
        }
        
        memo[pos] = res;
        return res;
    }

private:
    trieNode* trie;
};