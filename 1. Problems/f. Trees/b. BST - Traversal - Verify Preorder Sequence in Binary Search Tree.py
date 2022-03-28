# 255. Verify Preorder Sequence in Binary Search Tree

'''
Given an array of unique integers preorder, return true if it is the correct preorder traversal sequence of a binary search tree.

Example 1:
Input: preorder = [5,2,1,3,6]
Output: true

Example 2:

Input: preorder = [5,2,6,1,3]
Output: false
'''
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        return self.constantSolution(preorder)

    # O(n) time | O(n) space
    def naiveTLE(self, preorder: List[int]) -> bool:
        def isSorted(arr: List[int]):
            if len(arr) <= 1:
                return True
            
            mid = 0

            while mid < len(arr) and arr[mid] <= arr[0]:
                mid += 1

            for i in range(mid + 1, len(arr)):
                if arr[i] <= arr[0]:
                    return False

            return isSorted(arr[1:mid]) and isSorted(arr[mid:])

        return isSorted(preorder)

    # O(n) time | O(n) space
    def stackSolution(self, preorder: List[int]) -> bool:
        stack = []
        low = float('-inf')

        for p in preorder:
            if p < low:
                return False

            while stack and p > stack[-1]:
                low = stack.pop()

            stack.append(p)

        return True

    # O(n) time | O(1) space, mutating input array
    def constantSolution(self, preorder: List[int]) -> bool:
        low = float('-inf')
        i = 0

        for p in preorder:
            if p < low:
                return False

            while i > 0 and p > preorder[i - 1]:
                low = preorder[i - 1]
                i -= 1

            preorder[i] = p
            i += 1

        return True
