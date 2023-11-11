board = []

def create_board(x):
    for i in range(0,5):
        board.append(["O"] * 5)
    print board

print create_board(n)