"""
ID: derekwe1
LANG: PYTHON3
TASK: transform
"""

def initializeBoard(n):
    newBoard = []
    for r in range(n):
        row = []
        for c in range(n):
            row.append('')
        newBoard.append(row)
    return newBoard

def rotateBoard(board):
    n = len(board)
    newBoard = initializeBoard(n)

    for r in range(n):
        for c in range(n):
            newBoard[c][n-1 - r] = board[r][c]
    return newBoard

def reflectBoard(board):
    n = len(board)
    newBoard = initializeBoard(n)
    for r in range(n):
        for c in range(n):
            newBoard[r][n-1 - c] = board[r][c]
    return newBoard

# return true when both boards are equal
def equalBoard(board1, board2):
    n = len(board1)

    if (n != len(board2)):
        return False

    for r in range(n):
        for c in range(n):
            if (board1[r][c] != board2[r][c]):
                return False
    return True


with open('transform.in', 'r') as fin:
    n = int(fin.readline().strip())
    i = 0
    board = []
    newBoard = []
    while (i < n):
        board.append(fin.readline().strip())
        i += 1

    i = 0
    while (i < n):
        newBoard.append(fin.readline().strip())
        i += 1

print(board)
print(newBoard)

change = 7 
if (equalBoard(newBoard, rotateBoard(board))):
    change = 1
elif (equalBoard(newBoard, rotateBoard(rotateBoard(board)))):
    change = 2
elif (equalBoard(newBoard, rotateBoard(rotateBoard(rotateBoard(board))))):
    change = 3
elif (equalBoard(newBoard, reflectBoard(board))):
    change = 4
elif (equalBoard(newBoard, rotateBoard(reflectBoard(board))) or 
        equalBoard(newBoard, rotateBoard(rotateBoard(reflectBoard(board)))) or
        equalBoard(newBoard, rotateBoard(rotateBoard(rotateBoard(reflectBoard(board)))))):
    change = 5
elif (equalBoard(newBoard, board)):
    change = 6
else:
    change = 7

print(change)
with open('transform.out', 'w') as fout:
    fout.write(str(change) + '\n')
