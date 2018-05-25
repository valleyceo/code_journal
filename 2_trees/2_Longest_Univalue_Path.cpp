// Longest Univalue Path

/*
Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

Note: The length of path between two nodes is represented by the number of edges between them.

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output:

2
Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output:

2
Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.

* EACH node in the path is same value
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
    int traverse(TreeNode* root, int& maxlen) {
        if (root == NULL) return 0;
        
        int left = traverse(root->left, maxlen);
        int right = traverse(root->right, maxlen);
        if (!root->left || root->val != root->left->val)  left = 0;
        if (!root->right || root->val != root->right->val) right = 0;
        
        maxlen = max(maxlen, left + right);
        return max(left, right) + 1;
    }
    
    int longestUnivaluePath(TreeNode* root) {
        int maxlen = 0;
        traverse(root, maxlen);
        return maxlen;
    }
};