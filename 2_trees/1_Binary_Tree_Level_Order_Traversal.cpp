// Binary Tree Level Order Traversal

/*
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> lot;
        
        if (root == NULL){
            return lot;
        }
        
        queue<TreeNode*> que;
        queue<TreeNode*> new_que;
        vector<int> list;
        
        list.push_back(root->val);
        lot.push_back(list);
        que.push(root);
        list.clear();
        
        while (!que.empty()) {
            TreeNode* temp = que.front();
            que.pop();
            
            if (temp->left){
                new_que.push(temp->left);
                list.push_back(temp->left->val);
            }
                
            if (temp->right){
                new_que.push(temp->right);
                list.push_back(temp->right->val);
            }
            
            if (que.empty() && !list.empty()){
                lot.push_back(list);
                list.clear();

                que = new_que;
                queue<TreeNode*> empty;
                swap(new_que, empty);
            }
        }
        
        return lot;
    }
};