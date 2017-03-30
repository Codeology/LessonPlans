# from leetcode: https://leetcode.com/problems/minesweeper/#/description

def updateBoard(board, click):
    row, col = click

    # 1. click on a mine, the game is over
    if board[row][col] == 'M':
        board[row][col] = 'X'
        return board

    adjacentMines = countMines(board, click)

    # 3. click on an empty square with at least one adjacent mine
    if adjacentMines > 0:
        board[row][col] = str(adjacentMines)
        return board

    # 2. empty squre, no adjacent mines -> DFS recursion
    else:
        board[row][col] = 'B'
        for i in [row-1, row, row+1]:
            for j in [col-1, col, col+1]:
                if i == row and j == col:
                    continue
                if legal(board, [i, j]) and unvisited(board, [i, j]):
                    updateBoard(board, [i, j])
        return board

## helper functions

# counts how many mines are surrounding the square denoted by CLICK
def countMines(board, click):
    row, col = click
    mineCount = 0

    # all 8 potential surrounding boxes are countable
    for i in [row-1, row, row+1]:
        for j in [col-1, col, col+1]:
            if i == row and j == col:
                continue
            if legal(board, [i, j]) and board[i][j] == 'M':
                mineCount += 1

    return mineCount

# returns true if this CLICK is a legal move
def legal(board, click):
    row, col = click
    height = len(board)
    width = len(board[0])

    xInBounds = row < height and row >= 0
    yInBounds = col < width and col >= 0

    return xInBounds and yInBounds

# returns true if this square has not been clicked before
def unvisited(board, click):
    return board[click[0]][click[1]] == 'E'

# [['B',  1,  'E', 'E', 'E'],
#  ['B', 'E', 'M', 'E', 'E'],
#  ['B', 'E', 'E', 'E', 'E'],
#  ['E', 'B', 'E', 'E', 'E']]


def tests():
    t1 = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']]
    o1 = [['B', '1', 'E', '1', 'B'], ['B', '1', 'M', '1', 'B'], ['B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', 'B']]
    print(updateBoard(t1, [3, 1]) == o1)


    t2 = [['B', '1', 'E', '1', 'B'], ['B', '1', 'M', '1', 'B'], ['B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', 'B']]
    o2 = [['B', '1', 'E', '1', 'B'], ['B', '1', 'X', '1', 'B'], ['B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', 'B']]
    print(updateBoard(t2, [1, 2]) == o2)

    t3 = [['E', 'E'], ['E', 'M']]
    o3 = [['E', 'E'], ['1', 'M']]
    print(updateBoard(t3, [1, 0]) == o3)

tests()