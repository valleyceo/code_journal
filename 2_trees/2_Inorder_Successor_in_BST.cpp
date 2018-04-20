// Inorder Successor in BST


/*
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

Note: If the given node has no in-order successor in the tree, return null.
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
    TreeNode* inorderSuccessor(TreeNode* root, TreeNode* p) {
        if (p->right)
            return leftMost(p->right);
        
        TreeNode* suc = NULL;
        
        while (root) {
            if (p->val < root->val) {
                suc = root;
                root = root->left;
            } else if (p->val > root->val){
                root = root->right;
            } else {
                break;
            }
        }
        
        return suc;
    }
private:
    TreeNode* leftMost(TreeNode* node) {
        while (node->left)
            node = node->left;
        
        return node;
    }
};