# LC 780. Reaching Points

'''
Given four integers sx, sy, tx, and ty, return true if it is possible to convert the point (sx, sy) to the point (tx, ty) through some operations, or false otherwise.

The allowed operation on some point (x, y) is to convert it to either (x, x + y) or (x + y, y).

Example 1:

Input: sx = 1, sy = 1, tx = 3, ty = 5
Output: true
Explanation:
One series of moves that transforms the starting point to the target is:
(1, 1) -> (1, 2)
(1, 2) -> (3, 2)
(3, 2) -> (3, 5)
Example 2:

Input: sx = 1, sy = 1, tx = 2, ty = 2
Output: false

Example 3:

Input: sx = 1, sy = 1, tx = 1, ty = 1
Output: true
'''
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        return self.backwardModulo(sx, sy, tx, ty)

    # O(tx * ty) time | O(tx * ty) space
    def recursionTLE(self, sx: int, sy: int, tx: int, ty: int) -> bool:

        @lru_cache(None)
        def recursion(sx, sy, tx, ty):

            if sx > tx or sy > ty:
                return False

            if sx == tx and sy == ty:
                return True

            if recursion(sx + sy, sy, tx, ty):
                return True

            if recursion(sx, sx + sy, tx, ty):
                return True

            return False

        return recursion(sx, sy, tx, ty)

    # O(max(tx, ty)) time | O(1) space
    def backwardTLE(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx >= sx and ty >= sy:
            if sx == tx and sy == ty:
                return True

            if tx > ty:
                tx -= ty
            else:
                ty -= tx

        return False

    # O(log(max(tx, ty))) time | O(1) space
    def backwardModulo(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx >= sx and ty >= sy:
            if tx == ty: # No case that is True
                break
            elif tx > ty:
                if ty > sy:
                    tx %= ty
                else: # ty == sy
                    return (tx - sx) % ty == 0
            else:
                if tx > sx:
                    ty %= tx
                else: # tx == sx
                    return (ty - sy) % tx == 0

        return tx == sx and ty == sy

"""
Insight:
- Work backwards, while each child has 2 case (x + y, y), (x, x + y) there is only 1 parent where max(x, y) = prev(x + y)
- Children spanning same direction can be found instantly using modulo
"""
