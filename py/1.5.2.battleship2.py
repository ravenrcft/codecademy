board = []

for i in range(0,5):
    board.append(["O"] * 5)
print board

def print_board(board):
    for row in board:
        print row
print print_board(board)