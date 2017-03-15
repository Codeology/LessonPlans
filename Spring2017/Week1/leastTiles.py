def leastTiles(tiles):
    col_count = 0
    row_count = 0

    # columns
    for col_i in range(len(tiles[0])):
        col_count += colCount(tiles, col_i) # defined below

    # rows
    for row in tiles:
        row_count += rowCount(row) # defined below

    if col_count == row_count:
        return 0
    elif col_count > row_count:
        return 1
    else:
        return 2

# output how many paired neighbors can be smushed in a row, ignoring 0s
def rowCount(arr):
    if len(arr) > 0:
        count = 0
        prev = arr[0]
        for i in range(1, len(arr)):
            curr = arr[i]
            if curr == 0:
                continue
            if curr == prev:
                count += 1
                prev = -1
            else:
                prev = curr
        return count
    else:
        return 0

# output how many paired neighbors can be smushed in a row, ignoring 0s
def colCount(matrix, col_i):
    if len(matrix) < 0:
        return 0
    if matrix[0]:
        count = 0
        prev = matrix[0][col_i]
        for row_i in range(1, len(matrix)):
            curr = matrix[row_i][col_i]
            if curr == 0:
                continue
            if curr == prev:
                count += 1
                prev = -1
            else:
                prev = curr
        return count
    else:
        return 0
    
def test():
    # row tests
    print(rowCount([1, 1]) == 1)
    print(rowCount([0, 1]) == 0)
    print(rowCount([0, 0]) == 0)
    print(rowCount([1,0,1]) == 1)
    print(rowCount([1,1,1]) == 1)
    print(rowCount([1,0,1,1]) == 1)
    print(rowCount([1,1,1,1]) == 2)
    print(rowCount([1,0,1,2,2]) == 2)
    print(rowCount([1,2,1,2]) == 0)
    
    # col tests
    print(colCount([[0],[1],[2],[3]], 0) == 0)
    print(colCount([[0],[1],[1],[3]], 0) == 1)
    print(colCount([[0],[1],[2],[1]], 0) == 0)
    print(colCount([[1],[1],[1],[1]], 0) == 2)
    print(colCount([[1],[0],[1],[1]], 0) == 1)
    print(colCount([[1],[0],[1],[0]], 0) == 1)
    print(colCount([[1, 0],[0, 0],[1, 0],[0, 0]], 0) == 1)
    print(colCount([[1, 0],[0, 0],[1, 0],[0, 0]], 1) == 0)

    # integration
    tiles1 = [[2,4,16,8], [0,4,8,0], [0,0,0,0], [0,0,2,0]] #1
    tiles2 = [[2,16,32,8], [4,0,2,2], [2,0,2,0], [0,0,0,0]] #2
    tiles3 = [[4,16,32,8], [8,2,8,0], [2,4,2,2], [2,4,0,0]] #1
    tiles4 = [[4,4,8,8], [2,4,2,32], [0,2,8,16], [2,0,0,4]] #0
    print(leastTiles(tiles1) == 1)
    print(leastTiles(tiles2) == 2)
    print(leastTiles(tiles3) == 1)
    print(leastTiles(tiles4) == 0)

test()