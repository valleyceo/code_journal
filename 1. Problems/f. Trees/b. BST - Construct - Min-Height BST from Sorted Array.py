# Build a Minimum Height BST From a Sorted Array

'''
- Given a sorted array
- Build a BST of minimum height
'''

def build_min_height_bst_from_sorted_array(A: List[int]) -> Optional[BstNode]:
    def build_min_height_bst_from_sorted_subarray(start, end):
        if start >= end:
            return None
        mid = (start + end) // 2
        return BstNode(A[mid],
                       build_min_height_bst_from_sorted_subarray(start, mid),
                       build_min_height_bst_from_sorted_subarray(mid + 1, end))

    return build_min_height_bst_from_sorted_subarray(0, len(A))

'''
- Time complexity: O(n) - T(n)=2T(n/2)+O(1) -> T(n)=O(n), or in another words, we call O(1) for each elements
- Space complexity: O(h)
'''
