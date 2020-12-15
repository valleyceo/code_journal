"""
Range Sum Query - Mutable

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.

Example:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
"""
# O(log(n)) Time complexity, O(log(n)) Space complexity
class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None
        
class NumArray:
    
    def createSegmentTree(self, nums: List[int], l: int, r: int) -> Node:
        if l > r:
            return None
        
        if l == r:
            n = Node(l, r)
            n.total = nums[l]
            return n
        
        mid = (l + r) // 2
        root = Node(l, r)
        root.left = self.createSegmentTree(nums, l, mid)
        root.right = self.createSegmentTree(nums, mid + 1, r)
        root.total = root.left.total + root.right.total
        
        return root
        
    def __init__(self, nums: List[int]):
        self.root = self.createSegmentTree(nums, 0, len(nums) - 1)

    def update(self, i: int, val: int) -> None:
        self.updateRecursive(self.root, i, val)
        return
        
    def updateRecursive(self, node: Node, idx: int, val: int) -> None:
        if node.start == node.end:
            node.total = val
            return
        
        mid = (node.start + node.end) // 2
        
        if idx <= mid:
            self.updateRecursive(node.left, idx, val)
        else:
            self.updateRecursive(node.right, idx, val)
        
        node.total = node.left.total + node.right.total
        return

    def sumRange(self, i: int, j: int) -> int:
        return self.sumRangeRecursive(self.root, i, j)
    
    def sumRangeRecursive(self, node: Node, i: int, j: int) -> int:
        if node.start == i and node.end == j:
            return node.total
        
        mid = (node.start + node.end) // 2
        
        if j <= mid:
            return self.sumRangeRecursive(node.left, i, j)
        elif i >= mid + 1:
            return self.sumRangeRecursive(node.right, i, j)
        else:
            return self.sumRangeRecursive(node.left, i, mid) + self.sumRangeRecursive(node.right, mid+1, j)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)