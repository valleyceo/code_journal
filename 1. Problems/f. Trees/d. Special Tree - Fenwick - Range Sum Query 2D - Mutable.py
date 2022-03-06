# LC 308. Range Sum Query 2D - Mutable

'''
Given a 2D matrix matrix, handle multiple queries of the following types:

Update the value of a cell in matrix.
Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
Implement the NumMatrix class:

NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
void update(int row, int col, int val) Updates the value of matrix[row][col] to be val.
int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
'''

# Brute force solution
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def update(self, row: int, col: int, val: int) -> None:
        self.matrix[row][col] = val

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0

        for r in range(row1, row2 + 1, 1):
            for c in range(col1, col2 + 1, 1):
                sum += self.matrix[r][c]

        return sum

# Binary Index Tree Solution
class NumMatrix(object):
    def __init__(self, matrix):
        self.tree = BinaryIndexedTree(matrix)

    def update(self, row, col, val):
        self.tree.update(row, col, val)

    def sumRegion(self, row1, col1, row2, col2):
        return (
            self.tree.sum(row2 + 1, col2 + 1) +
            self.tree.sum(row1, col1) -
            self.tree.sum(row1, col2 + 1) -
            self.tree.sum(row2 + 1, col1))

class BinaryIndexedTree(object):
    def __init__(self, matrix):
        m, n = len(matrix), len(matrix[0]) if matrix else 0

        self.matrix = matrix
        self.sums = [[0] * (n + 1) for _ in range(m + 1)]

        [operator.setitem(
            self.sums[row], col,
            self.sums[row][col] + self.matrix[i - 1][j - 1]
        )
        for row in range(1, len(self.sums))
        for col in range(1, len(self.sums[0]))
        for i in range(row + 1 - (row & -row), row + 1)
        for j in range(col + 1 - (col & -col), col + 1)]

    def update(self, row, col, val):
        i = row + 1
        while i < len(self.sums):
            j = col + 1
            while j < len(self.sums[0]):
                self.sums[i][j] += val - self.matrix[row][col]
                j += j & -j
            i += i & -i
        self.matrix[row][col] = val

    def sum(self, row, col):
        r, i = 0, row
        while i > 0:
            j = col
            while j > 0:
                r += self.sums[i][j]
                j -= j & -j
            i -= i & -i
        return r
