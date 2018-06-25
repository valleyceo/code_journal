// Closest Binary Search Tree Value


/*
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4
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
    int closestValue(TreeNode* root, double target) {
        if (root == NULL) return NULL;
        
        TreeNode* search_node = root;
        
        int min_val = INT_MAX;
        int max_val = INT_MIN;
        
        while (search_node) {
            if (target < search_node->val) {
                max_val = search_node->val;
                search_node = search_node->left;
            } else if (target > search_node->val) {
                min_val = search_node->val;
                search_node = search_node->right;
            } else {
                return search_node->val;
            }
        }
        
        return (abs(target-min_val) < abs(target-max_val) ? min_val : max_val);
    }
};