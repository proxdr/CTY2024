# 7/5/2024 - 7/8/2024

gameRunning = True # Allows game to run
player="P" # User
row=2
column=1

# Print board
def game(x):
    for i in range(0, len(x)):
        print(x[i])

# Game space list
board = [
    ['-','-','#','#','#','#','#','-'],
    ['#','#','#','-','-','-','#','-'],
    ['#','P','-','-','#','-','#','-'],
    ['#','#','#','-','#','-','#','-'],
    ['#','-','#','#','#','-','#','-'],
    ['#','-','#','-','-','-','#','#'],
    ['#','#','-','-','#','#','-','#'],
    ['#','&','-','-','-','-','-','#'],
    ['#','#','#','#','#','#','#','#']
]

# Run the game
while gameRunning == True:
    game(board)
    userInput = input("Use the WASD keys to control your character: ")
    board[row][column] = '-'

    if userInput == "d":
        if column + 1 < len(board[row]):
            if board[row][column + 1] == "-":
                column += 1
            elif board[row][column + 1] == "#":
                pass

    elif userInput == "a":
        if column - 1 >= 0:
            if board[row][column - 1] == "-":
                column -= 1
            elif board[row][column - 1] == "#":
                pass

    elif userInput == "w":
        if row - 1 >= 0:
            if board[row - 1][column] == "-":
                row -= 1
            elif board[row - 1][column] == "#":
                pass

    elif userInput == "s":
        if row + 1 < len(board):
            if board[row + 1][column] == "-":
                row += 1
            elif board[row + 1][column] == "#":
                pass

    board[row][column] = "P"

# Game ending condition
    if player == board[8][1]:
        print("You Win!")
        gameRunning = False