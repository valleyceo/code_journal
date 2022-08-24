# 303. Range Sum Query - Immutable

'''
Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
'''

class NumArray:

    def __init__(self, nums: List[int]):
        self.seg_tree = SegmentTree(nums)

    def sumRange(self, left: int, right: int) -> int:
        if not self.seg_tree:
            return 0

        return self.seg_tree.rFind(self.seg_tree.root, (left, right))

class SegmentTree:

    def __init__(self, nums):
        self.count = 0
        self.buildTree(nums)

    def buildTree(self, nums):
        if not nums:
            return None

        self.root = self.rBuildTree(nums, 0, len(nums) - 1)

    def rBuildTree(self, nums, left, right):
        if left == right:
            return Node(nums[left], (left, right))

        mid = (right + left) // 2
        new_node = Node(0, (left, right), self.rBuildTree(nums, left, mid), self.rBuildTree(nums, mid + 1, right))
        new_node.val = new_node.left.val + new_node.right.val

        return new_node

    def rFind(self, node, rng):
        if rng[0] <= node.idx_range[0] and node.idx_range[1] <= rng[1]:
            return current_node.val
        elif node.idx_range[1] < rng[0] or node.idx_range[0] > rng[1]:
            return 0
        return self.rFind(node.left, rng) + self.rFind(node.right, rng)

class Node:
    def __init__(self, val, idx_range, left = None, right = None):
        self.val = val
        self.idx_range = idx_range
        self.left = left
        self.right = right
