// Balanced Binary Tree

/*
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
*/

// my solution - optimal, space O(n), time O(n)
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
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        
        if (!root) return {};
        
        vector<vector<int>> res;
        queue<TreeNode*> que({root});
        
        while (!que.empty()) {
            vector<int> level_nodes;
            
            for (int i = que.size(); i > 0; --i) {
                TreeNode *node = que.front();
                que.pop();
                
                level_nodes.push_back(node->val);
                
                if (node->left) que.push(node->left);
                if (node->right) que.push(node->right);
            }
            
            res.insert(res.begin(), level_nodes); // insert to front of vector
        }
        
        return res;
    }
};

// alternate solution using DFS (solution)
class Solution {
public:
   vector<vector<int> > res;

  void DFS(TreeNode* root, int level)
  {
      if (root == NULL) return;
      if (level == res.size()) // The level does not exist in output
      {
          res.push_back(vector<int>()); // Create a new level
      }
      
      res[level].push_back(root->val); // Add the current value to its level
      DFS(root->left, level+1); // Go to the next level
      DFS(root->right,level+1);
  }

  vector<vector<int> > levelOrderBottom(TreeNode *root) {
      DFS(root, 0);
      return vector<vector<int> > (res.rbegin(), res.rend());
  }
};