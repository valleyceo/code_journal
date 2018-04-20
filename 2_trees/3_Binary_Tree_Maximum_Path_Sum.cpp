// Binary Tree Maximum Path Sum

/*
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
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
    int max_path;
    
    int paths(TreeNode* root) {
        if (!root) return 0;
        
        int l = max(0, paths(root->left));
        int r = max(0, paths(root->right));
        max_path = max(max_path, l + r + root->val);
        
        return max(l, r) + root->val;
    }
    
    int maxPathSum(TreeNode* root) {
        max_path = INT_MIN;
        paths(root);
        
        return max_path;
    }
};