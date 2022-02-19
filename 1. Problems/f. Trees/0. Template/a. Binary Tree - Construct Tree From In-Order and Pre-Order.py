# Reconstruct a Binary Tree from Traversal Data

'''
- Given an inorder traversal sequence and a preorder traversal sequence of binary tree
- Reconstruct the tree
- Assume each node has a unique key
'''

# Time complexity: O(n)
# Space complexity: O(hashmap + search) -> O(n + h)
def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:

    node_to_inorder_idx = {data: i for i, data in enumerate(inorder)}

    # Builds the subtree with preorder[preorder_start:preorder_end] and
    # inorder[inorder_start:inorder_end].
    def binary_tree_from_preorder_inorder_helper(preorder_start, preorder_end,
                                                 inorder_start, inorder_end):
        if preorder_end <= preorder_start or inorder_end <= inorder_start:
            return None

        root_inorder_idx = node_to_inorder_idx[preorder[preorder_start]]
        left_subtree_size = root_inorder_idx - inorder_start
        return BinaryTreeNode(
            preorder[preorder_start],
            # Recursively builds the left subtree.
            binary_tree_from_preorder_inorder_helper(
                preorder_start + 1, preorder_start + 1 + left_subtree_size,
                inorder_start, root_inorder_idx),
            # Recursively builds the right subtree.
            binary_tree_from_preorder_inorder_helper(
                preorder_start + 1 + left_subtree_size, preorder_end,
                root_inorder_idx + 1, inorder_end))

    return binary_tree_from_preorder_inorder_helper(preorder_start=0,
                                                    preorder_end=len(preorder),
                                                    inorder_start=0,
                                                    inorder_end=len(inorder))

'''
- Center is the root in Inorder, Leftmost is the root in Preorder
- Visual note:
              left            right
           <--------> root <-------->
In-order:  10, 30, 40, 50, 60, 70, 90
Pre-order: 50, 30, 10, 40, 70, 60, 90
          root <-------->  <-------->
                  left        right
'''
