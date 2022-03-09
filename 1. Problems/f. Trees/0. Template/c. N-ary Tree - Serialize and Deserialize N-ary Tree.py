# 428. Serialize and Deserialize N-ary Tree

'''
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize an N-ary tree. An N-ary tree is a rooted tree in which each node has no more than N children. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that an N-ary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following 3-ary tree

as [1 [3[5 6] 2 4]]. Note that this is just an example, you do not necessarily need to follow this format.

Or you can follow LeetCode's level order traversal serialization format, where each group of children is separated by the null value.

For example, the above tree may be serialized as [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14].

You do not necessarily need to follow the above-suggested formats, there are many more different formats that work so please be creative and come up with different approaches yourself.

Example 1:

Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Example 2:

Input: root = [1,null,3,2,4,null,5,6]
Output: [1,null,3,2,4,null,5,6]
Example 3:

Input: root = []
Output: []
'''

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if not root:
            return ""

        slist = []
        self.serializeHelper(root, slist)
        return "".join(slist)

    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        if not data:
            return None

        root_node = Node(ord(data[0]) - 48, [])
        self.deserializeHelper(data, root_node)
        return root_node

    def serializeHelper(self, node, serializedList):
        queue = deque([node, None])

        while queue:
            node = queue.popleft()

            if not node:
                serializedList.append("#")

                if queue:
                    queue.append(None)

            elif node == "C":
                serializedList.append('$')
            else:
                serializedList.append(chr(node.val + 48))

                for child in node.children:
                    queue.append(child)

                if queue[0] != None:
                    queue.append('C')

    def deserializeHelper(self, data, node):
        prevLevel = deque()
        currLevel = deque([node])
        parentNode = node

        for i in range(1, len(data)):
            if data[i] == '#':
                prevLevel = currLevel
                currLevel = deque()

                parentNode = prevLevel.popleft() if prevLevel else None
            else:
                if data[i] == '$':
                    parentNode = prevLevel.popleft() if prevLevel else None
                else:
                    childNode = Node(ord(data[i]) - 48, [])
                    currLevel.append(childNode)
                    parentNode.children.append(childNode)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
