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
    userInput = input("User the WASD keys on your device to control your character: ")
    board[row][column] = '-'

    if userInput == "d" and board[row][column+1]=="-":
        column += 1
        board[row][column]="P"
        board[row][column-1]="-"
    if userInput == "a" and board[row][column-1]=="-":
        column -= 1
        board[row][column]="P"
        board[row][column+1]="-"
    if userInput == "w" and board[row-1][column]=="-":
        row -= 1
        board[row][column]="P"
        board[row+1][column]="-"
    if userInput == "s" and board[row+1][column]=="-":
        row += 1
        board[row][column]="P"
        board[row-1][column]="-"


    if userInput == "d" and board[row][column+1]=="#":
        column += 1
        board[row][column]="#"
        board[row][column-1]="P"
    if userInput == "a" and board[row][column-1]=="#":
        column -= 1
        board[row][column]="#"
        board[row][column+1]="P"
    if userInput == "w" and board[row-1][column]=="#":
        row -= 1
        board[row][column]="#"
        board[row+1][column]="P"
    if userInput == "s" and board[row+1][column]=="#":
        row += 1
        board[row][column]="#"
        board[row-1][column]="P"


# Game ending condition
    if player == board[7][1]:
        print("You Win!")
        gameRunning = False