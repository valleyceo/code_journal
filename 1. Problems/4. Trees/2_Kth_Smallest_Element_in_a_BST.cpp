// Kth Smallest Element in a BST


/*
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
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
    int smallest (TreeNode* root, int& k){
        if (!root)
            return -1;
        
        int val = smallest(root->left, k);
        
        if (!k) 
            return val;
        
        if (!--k) 
            return root->val;
        
        return smallest(root->right, k);
    }
    
    int kthSmallest(TreeNode* root, int k) {
        return smallest(root, k);
    }
};