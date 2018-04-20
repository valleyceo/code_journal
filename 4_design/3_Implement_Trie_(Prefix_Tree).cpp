// Implement Trie (Prefix Tree)

/*
Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.
*/

// my solution
class TrieNode {
public:
    bool is_leaf;
    TrieNode* children[26];
    
    TrieNode() {
        is_leaf = false;
        memset(children, 0, sizeof(children));
    }
};

class Trie {
    TrieNode* root;
public:
    /** Initialize your data structure here. */
    Trie() {
        root = new TrieNode();
    }
    
    /** Inserts a word into the trie. */
    void insert(string s) {
        TrieNode *p = root;
        for(int i = 0; i < s.size(); ++ i)
        {
            if(p -> children[s[i] - 'a'] == NULL)
                p -> children[s[i] - 'a'] = new TrieNode();
            p = p -> children[s[i] - 'a'];
        }
        p -> is_leaf = true;
    }
    
    /** Returns if the word is in the trie. */
    bool search(string word) {
        
        TrieNode *p = find(word);
        
        return p != NULL && p->is_leaf;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        
        return find(prefix) != NULL;
    }

private:
    TrieNode* find(string key) {
        TrieNode *head = root;
        
        for (auto w : key) {
            if (head->children[w-'a'])
                head = head->children[w-'a'];
            else
                return NULL;
        }
        
        return head;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * bool param_2 = obj.search(word);
 * bool param_3 = obj.startsWith(prefix);
 */