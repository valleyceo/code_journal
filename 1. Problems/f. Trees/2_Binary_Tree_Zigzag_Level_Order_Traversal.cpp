// Binary Tree Zigzag Level Order Traversal

/*
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
*/

// my solution
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    
    vector<vector<int> > zigzagLevelOrder(TreeNode *root)  {
        vector<vector<int>> res;
        
        if (root != NULL) {
            res.push_back(vector<int>(1, root->val));
            deque<TreeNode*> q1, q2;
            vector<int> lev;
            
            q1.push_back(root);
            bool flag = false;
            
            while (true) {
                while (!q1.empty()) {
                    TreeNode* node = q1.front();
                    q1.pop_front();
                    if (node->left) {q2.push_back(node->left);}
                    if (node->right) {q2.push_back(node->right);}
                }
                
                if (q2.empty()) {return res;}
                q1 = q2;
                
                while (!q2.empty()){
                    if (flag) {
                        lev.push_back(q2.front()->val);
                        q2.pop_front();
                    } else {
                        lev.push_back(q2.back()->val);
                        q2.pop_back();
                    }
                }
                
                res.push_back(lev);
                lev.clear();
                flag = !flag;
            }
        }
        return res;
    }
};