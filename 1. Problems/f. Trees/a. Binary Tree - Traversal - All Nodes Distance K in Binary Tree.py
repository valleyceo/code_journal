# LC 863. All Nodes Distance K in Binary Tree

'''
Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.

Example 2:

Input: root = [1], target = 1, k = 3
Output: []

Constraints:

The number of nodes in the tree is in the range [1, 500].
0 <= Node.val <= 500
All the values Node.val are unique.
target is the value of one of the nodes in the tree.
0 <= k <= 1000
'''
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        return self.bestSolution(root, target.val, k)
    
    def bestSolution(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        res = []
        self.getDistantNodes(root, target, k, res)
        return res

    def getDistantNodes(self, node, target, k, res):
        if node is None:
            return -1

        if node.val == target:
            self.addSubtreeNodesAtDistK(node, 0, k, res)
            return 1

        leftDist = self.getDistantNodes(node.left, target, k, res)
        rightDist = self.getDistantNodes(node.right, target, k, res)

        if leftDist == k or rightDist == k:
            res.append(node.val)

        if leftDist != -1:
            self.addSubtreeNodesAtDistK(node.right, leftDist + 1, k, res)
            return leftDist + 1

        if rightDist != -1:
            self.addSubtreeNodesAtDistK(node.left, rightDist + 1, k, res)
            return rightDist + 1

        return -1
	
    def addSubtreeNodesAtDistK(self, node, distance, k, res):
        if node is None:
            return

        if distance == k:
            res.append(node.val)
        else:
            self.addSubtreeNodesAtDistK(node.left, distance + 1, k, res)
            self.addSubtreeNodesAtDistK(node.right, distance + 1, k, res)
        
    def GraphSolution(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def connect(parent, child):
            if parent and child:
                graph[parent.val].append(child.val)
                graph[child.val].append(parent.val)
            
            if child.left:
                connect(child, child.left)
            
            if child.right:
                connect(child, child.right)
        
        graph = defaultdict(list)
        connect(None, root)
        
        visited = set([target.val])
        que = [target.val]
        
        while que and k > 0:
            temp = []
            
            for node in que:
                visited.add(node)
                for next_node in graph[node]:
                    if next_node not in visited:
                        temp.append(next_node)
                    
            que = temp.copy()
            k -= 1
        
        return que