from random import randint, shuffle, seed
from copy import deepcopy
n = 20
print(n)

seed(47)

def findNextCellToFill(grid, i, j):
    for x in range(i,9):
        for y in range(j,9):
            if grid[x][y] == 0:
                    return x,y
    for x in range(0,9):
        for y in range(0,9):
            if grid[x][y] == 0:
                return x,y
    return -1,-1

def isValid(grid, i, j, e):
    rowOk = all([e != grid[i][x] for x in range(9)])
    if rowOk:
        columnOk = all([e != grid[x][j] for x in range(9)])
        if columnOk:
            # finding the top left x,y co-ordinates of the section containing the i,j cell
            secTopX, secTopY = 3 *(i//3), 3 *(j//3)
            for x in range(secTopX, secTopX+3):
                for y in range(secTopY, secTopY+3):
                    if grid[x][y] == e:
                        return False
            return True
    return False

res = []
def solveSudoku(grid, i=0, j=0):
    global res
    i,j = findNextCellToFill(grid, i, j)
    if i == -1:
        res.append(deepcopy(grid))
        return
    for e in range(1,10):
        if isValid(grid,i,j,e):
            grid[i][j] = e
            solveSudoku(grid, i, j)
            if len(res) > 2:
                return
            # Undo the current cell for backtracking
            grid[i][j] = 0


def make_board(m=3):
    """Return a random filled m**2 x m**2 Sudoku board."""
    n = m**2
    board = [[None for _ in range(n)] for _ in range(n)]

    def search(c=0):
        "Recursively search for a solution starting at position c."
        i, j = divmod(c, n)
        i0, j0 = i - i % m, j - j % m # Origin of mxm block
        numbers = list(range(1, n + 1))
        shuffle(numbers)
        for x in numbers:
            if (x not in board[i]                     # row
                and all(row[j] != x for row in board) # column
                and all(x not in row[j0:j0+m]         # block
                        for row in board[i0:i])):
                board[i][j] = x
                if c + 1 >= n**2 or search(c + 1):
                    return board
        else:
            # No number is valid in this cell: backtrack and try again.
            board[i][j] = None
            return None

    return search()

def getFormatBoard(board):
    cpyBoard = deepcopy(board)
    for i in range(9):
        for j in range(9):
            cpyBoard[i][j] = str(cpyBoard[i][j])
    rows = []
    for i in range(9):
        rows.append(''.join(cpyBoard[i]))
    return '\n'.join(rows)

# mutates board
def getBoard():
    global res
    while True:
        board = make_board()
        toRem = randint(20, 50)
        removed = 0
        while removed < toRem:
            x,y = randint(0, 8), randint(0, 8)
            if board[x][y] != 0:
                save = board[x][y]
                board[x][y] = 0
                solveSudoku(deepcopy(board))
                if (len(res) == 1):
                    removed += 1
                else:
                    board[x][y] = save
                res = []
        return getFormatBoard(board)



for _ in range(n):
    print(getBoard())
