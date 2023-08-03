import random

# Constants
ROWS = 9
COLUMNS = 9
MINES = 10

# Game Board
board = [[0 for x in range(COLUMNS)] for y in range(ROWS)]

# Place Mines randomly on the board
for i in range(MINES):
    row = random.randint(0, ROWS - 1)
    col = random.randint(0, COLUMNS - 1)
    board[row][col] = "M"

# Count the number of mines surrounding each cell
for row in range(ROWS):
    for col in range(COLUMNS):
        if board[row][col] == "M":
            continue
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (0 <= row + i < ROWS) and (0 <= col + j < COLUMNS) and (board[row + i][col + j] == "M"):
                    count += 1
        board[row][col] = count

# Print the board
for row in board:
    print(" ".join([str(x) if x != "M" else "*" for x in row]))