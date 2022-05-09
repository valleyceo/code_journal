# LC 631. Design Excel Sum Formula

'''
Design the basic function of Excel and implement the function of the sum formula.

Implement the Excel class:

Excel(int height, char width) Initializes the object with the height and the width of the sheet. The sheet is an integer matrix mat of size height x width with the row index in the range [1, height] and the column index in the range ['A', width]. All the values should be zero initially.
void set(int row, char column, int val) Changes the value at mat[row][column] to be val.
int get(int row, char column) Returns the value at mat[row][column].
int sum(int row, char column, List<String> numbers) Sets the value at mat[row][column] to be the sum of cells represented by numbers and returns the value at mat[row][column]. This sum formula should exist until this cell is overlapped by another value or another sum formula. numbers[i] could be on the format:
"ColRow" that represents a single cell.
For example, "F7" represents the cell mat[7]['F'].
"ColRow1:ColRow2" that represents a range of cells. The range will always be a rectangle where "ColRow1" represent the position of the top-left cell, and "ColRow2" represents the position of the bottom-right cell.
For example, "B3:F7" represents the cells mat[i][j] for 3 <= i <= 7 and 'B' <= j <= 'F'.
Note: You could assume that there will not be any circular sum reference.

For example, mat[1]['A'] == sum(1, "B") and mat[1]['B'] == sum(1, "A").
'''
class Cell:
    def __init__(self, val = 0):
        self.val = val
        self.sumdata = defaultdict(int)

class Excel:

    def __init__(self, height: int, width: str):
        self.sheet = [[Cell() for _ in range(ord(width) - ord('A') + 1)] for _ in range(height)]

    def set(self, row: int, column: str, val: int) -> None:
        self.sheet[row-1][ord(column) - ord('A')].val = val
        self.sheet[row-1][ord(column) - ord('A')].sumdata = defaultdict(int)

    def get(self, row: int, column: str) -> int:
        cell = self.sheet[row-1][ord(column) - ord('A')]

        if not cell.sumdata:
            return cell.val

        total = 0
        for loc, count in cell.sumdata.items():
            total += self.get(loc[0], loc[1]) * count

        return total

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        self.sheet[row - 1][ord(column) - ord('A')] = self.parse(numbers)

        return self.get(row, column)

    def parse(self, string: str) -> Cell:
        cell = Cell()

        for s in string:
            sarr = s.split(":")
            s, e = (sarr[0], sarr[1]) if len(sarr) == 2 else (sarr[0], sarr[0])
            for i in range(ord(s[0]), ord(e[0]) + 1):
                for j in range(int(s[1:]), int(e[1:]) + 1):
                    cell.sumdata[(j, chr(i))] += 1

        return cell


# Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)
