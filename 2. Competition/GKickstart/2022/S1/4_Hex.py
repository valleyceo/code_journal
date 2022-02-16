def dfs(i, j, color, connected, board, visited, n):
    if i < 0 or i >= n or j < 0 or j >= n:
        return

    if (i, j) in visited or board[i][j] != color:
        return

    visited.add((i, j))
    connected.add((i, j))
    dfs(i - 1, j + 1, color, connected, board, visited, n)
    dfs(i + 1, j    , color, connected, board, visited, n)
    dfs(i - 1, j    , color, connected, board, visited, n)
    dfs(i + 1, j - 1, color, connected, board, visited, n)
    dfs(i    , j + 1, color, connected, board, visited, n)
    dfs(i    , j - 1, color, connected, board, visited, n)

def checkRedWin(n, board):
    visited = set()
    passCount = 0

    for i in range(n):
        if (0, i) in visited or board[0][i] != "R":
            continue

        connected = set()
        dfs(0, i, 'R', connected, board, visited, n)

        # Check if it's impossible
        up = 0
        down = 0
        for i2, _ in connected:
            if i2 == 0:
                up += 1

            if i2 == n - 1:
                down += 1

        if up > 1 and down > 1:
            return "Impossible"
        elif up > 0 and down > 0:
            passCount += 1

    if passCount == 0:
        return ""
    elif passCount > 1:
        return "Impossible"
    else:
        return "Red wins"

def checkBlueWin(n, board):
    visited = set()
    passCount = 0

    for i in range(n):
        if (i, 0) in visited or board[i][0] != "B":
            continue

        connected = set()
        dfs(i, 0, 'B', connected, board, visited, n)

        # Check if it's impossible
        left = 0
        right = 0
        for _, j2 in connected:
            if j2 == 0:
                left += 1

            if j2 == n - 1:
                right += 1

        if left > 1 and right > 1:
            return "Impossible"
        elif left > 0 and right > 0:
            passCount += 1

    if passCount == 0:
        return ""
    elif passCount > 1:
        return "Impossible"
    else:
        return "Blue wins"

def game_status(n, board):

    # Check if count is correct
    rcount = 0
    bcount = 0

    for i in range(n):
        for j in range(n):
            if board[i][j] == 'R':
                rcount += 1
            elif board[i][j] == "B":
                bcount += 1

    if abs(rcount - bcount) > 1:
        return "Impossible"

    lastTurn = ""
    if rcount > bcount:
        lastTurn = "R"
    elif bcount > rcount:
        lastTurn = "B"

    # check if blue or red wins (or impossible)
    blueStatus = checkBlueWin(n, board)

    if blueStatus != "":
        if blueStatus[0] == 'B' and lastTurn == "R":
            return "Impossible"

        return blueStatus

    redStatus = checkRedWin(n, board)

    if redStatus != "":
        if redStatus[0] == 'R' and lastTurn == "B":
            return "Impossible"

        return redStatus

    return "Nobody wins"


def main():
    test_cases = int(input())
    
    for test_case in range(1, test_cases + 1, 1):
        board_size = int(input())
        board = []

        for _ in range(board_size):
            board.append(list(input().strip()))

        ans = game_status(board_size, board)
        print("Case #{}: {}".format(test_case, ans))


if __name__ == "__main__":
    main()
