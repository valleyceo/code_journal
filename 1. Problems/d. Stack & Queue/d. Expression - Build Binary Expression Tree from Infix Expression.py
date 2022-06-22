# LC 1597. Build Binary Expression Tree From Infix Expression

'''
A binary expression tree is a kind of binary tree used to represent arithmetic expressions. Each node of a binary expression tree has either zero or two children. Leaf nodes (nodes with 0 children) correspond to operands (numbers), and internal nodes (nodes with 2 children) correspond to the operators '+' (addition), '-' (subtraction), '*' (multiplication), and '/' (division).

For each internal node with operator o, the infix expression it represents is (A o B), where A is the expression the left subtree represents and B is the expression the right subtree represents.

You are given a string s, an infix expression containing operands, the operators described above, and parentheses '(' and ')'.

Return any valid binary expression tree, whose in-order traversal reproduces s after omitting the parenthesis from it.

Please note that order of operations applies in s. That is, expressions in parentheses are evaluated first, and multiplication and division happen before addition and subtraction.

Operands must also appear in the same order in both s and the in-order traversal of the tree.
'''

# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    op_levels = {"(": 0, ")": 0, "+": 1, "-": 1, "*": 2, "/": 2}
    ops = {"+", "-", "*", "/"}

    def expTree(self, s: str) -> 'Node':
        postfix = self.infix_to_postfix(s)
        tree = self.postfix_to_tree(postfix)

        return tree

    def postfix_to_tree(self, postfix: List[str]) -> 'Node':
        stack = deque()

        for c in postfix:
            if c in self.ops:
                right = stack.pop()
                left = stack.pop()

                curr_node = Node(c, left, right)
                stack.append(curr_node)
            else:
                stack.append(Node(c))

        return stack[-1]

    def infix_to_postfix(self, s: str) -> 'Node':
        stack = deque()
        postfix = []

        for i, c in enumerate(s):

            if c in self.op_levels:
                if c == "(":
                    stack.append(c)
                elif c == ")":
                    while stack and stack[-1] != "(":
                        postfix.append(stack.pop())
                    stack.pop()

                elif stack and self.op_levels[c] > self.op_levels[stack[-1]]:
                    stack.append(c)
                else:
                    while stack:
                        if stack[-1] == "(":
                            break

                        postfix.append(stack.pop())

                    stack.append(c)
            else:
                postfix.append(c)

        while stack:
            postfix.append(stack.pop())

        return postfix


"""
Note:
- Convert infix to post fix

Post fix conversion: https://leetcode.com/problems/build-binary-expression-tree-from-infix-expression/discuss/1386335/Python-O(n)-infix-greater-postfix-greater-expression-tree

Parser implementation: https://leetcode.com/problems/build-binary-expression-tree-from-infix-expression/discuss/864596/Python-Standard-parser-implementation
"""
