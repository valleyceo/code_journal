// Minimum Depth of Binary Tree

/*
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
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

/* Note
BFS: 
- use que
- stop when NULL child is found (leaf)
- leaf is when there is no left or right node
*/
class Solution {
public:
    int minDepth(TreeNode* root) {
        if (root == NULL) return 0;
        
        queue< TreeNode* > que;
        que.push(root);
        int size, depth = 0;
        
        while (!que.empty()) {
            depth++;
            size = que.size();
            
            for (int i = 0; i < size; i++) {
                TreeNode* node = que.front();
                que.pop();
                
                if (node->left == NULL && node->right == NULL) return depth;
                if (node->left) que.push(node->left);
                if (node->right) que.push(node->right);
            }
        }
        
        return depth;
    }
};