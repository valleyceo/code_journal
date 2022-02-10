// Balanced Binary Tree

/*
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
*/

// my solution - Not optimal
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
    int height(TreeNode* node) {
        if (node == NULL)
            return 0;
        
        return 1 + max(height(node->left), height(node->right));
    }
public:
    bool isBalanced(TreeNode* root) {
        int lh, rh;
        
        if (root == NULL)
            return true;
        
        lh = height(root->left);
        rh = height(root->right);
        
        if ((abs(lh - rh) <= 1) && isBalanced(root->left) && isBalanced(root->right))
            return true;
        
        return false;
    }
};