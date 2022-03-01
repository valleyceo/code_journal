# Compute Enclosed Regions

'''
- Given a 2D array of either W or B entry
- Replace all Ws that cannot reach the boundary to B (i.e. all W's that is surrounded by B)
'''

# O(mn) time
def fill_surrounded_regions(board: List[List[str]]) -> None:

    n, m = len(board), len(board[0])
    q = collections.deque([(i, j) for k in range(n)
                           for i, j in ((k, 0), (k, m - 1))] +
                          [(i, j) for k in range(m)
                           for i, j in ((0, k), (n - 1, k))])
    while q:
        x, y = q.popleft()
        if 0 <= x < n and 0 <= y < m and board[x][y] == 'W':
            board[x][y] = 'T'
            q.extend([(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)])
    board[:] = [['B' if c != 'T' else 'W' for c in row] for row in board]

'''
1. Start from all edge points, BFS if they are 'W' and convert to 'T'
2. Scan the whole grid, convert all 'T' to 'W' and rest to 'B'
'''
