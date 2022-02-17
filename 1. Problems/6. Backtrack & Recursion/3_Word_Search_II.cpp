// Word Search II

/*
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

For example,
Given words = ["oath","pea","eat","rain"] and board =

[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
Return ["eat","oath"].
Note:
You may assume that all inputs are consist of lowercase letters a-z.

click to show hint.

You would need to optimize your backtracking to pass the larger test. Could you stop backtracking earlier?

If the current candidate does not exist in all words' prefix, you could stop backtracking immediately. What kind of data structure could answer such query efficiently? Does a hash table work? Why or why not? How about a Trie? If you would like to learn how to implement a basic trie, please work on this problem: Implement Trie (Prefix Tree) first.
*/

// my solution
class TrieNode {
public:
    bool is_end;
    vector<TrieNode*> children;
    
    TrieNode() {
        is_end = false;
        children = vector<TrieNode*>(26, NULL);
    }
};

class Trie {
public:
    TrieNode* getRoot() {return root;}
    Trie(vector<string>& words) {
        root = new TrieNode();
        for (int i = 0; i < words.size(); ++i)
            addWord(words[i]);
    }
    
    void addWord(const string& word) {
        TrieNode* cur = root;
        
        for (int i = 0; i < word.size(); i++) {
            int idx = word[i] - 'a';
            
            if (cur->children[idx] == NULL)
                cur->children[idx] = new TrieNode();
            
            cur = cur->children[idx];
        }
        
        cur->is_end = true;
    }
    
private:
    TrieNode* root;
};

class Solution {
public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        Trie* trie = new Trie(words);
        TrieNode* root = trie->getRoot();
        set<string> res_set;
        
        for (int x=0; x < board.size(); ++x)
            for (int y=0; y < board[0].size(); ++y)
                findWords(board, x, y, root, "", res_set);
        
        // convert set to vector
        vector<string> res;
        for (auto it : res_set)
            res.push_back(it);
        
        return res;
    }

private:
    void findWords(vector<vector<char>>& board, int x, int y, TrieNode* root, string word, set<string>& result) {
        if (x < 0 || x >= board.size() || y < 0 || y >= board[0].size() || board[x][y]==' ')
            return;
        
        if (root->children[board[x][y] - 'a'] != NULL) {
            word = word + board[x][y];
            
            root = root->children[board[x][y] - 'a'];
            
            if (root->is_end)
                result.insert(word);
            
            char c = board[x][y];
            board[x][y] = ' ';
            
            findWords(board, x+1, y, root, word, result);
            findWords(board, x-1, y, root, word, result);
            findWords(board, x, y+1, root, word, result);
            findWords(board, x, y-1, root, word, result);
            board[x][y] = c;
        }
    }
};