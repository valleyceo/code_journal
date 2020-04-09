// Leetcode 589. N-ary Tree Preorder Traversal

/*
Given an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 

Follow up:

Recursive solution is trivial, could you do it iteratively?
*/

// my solution
class Solution {
public:
    vector<int> preorder(Node* root) {
        vector<int> res;
        stack<Node*> stk;
        stk.push(root);
        
        while (!empty(stk)) {
            Node* cnode = stk.top();
            stk.pop();
            
            if (cnode == NULL)
                continue;
            
            res.emplace_back(cnode->val);
            
            for (auto it = cnode->children.rbegin(); it != cnode->children.rend(); ++it) {
                stk.push(*it);
            }
        }
        
        return res;
    }
};