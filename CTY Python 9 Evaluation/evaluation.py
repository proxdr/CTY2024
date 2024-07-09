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

#def board
#print("Maze Game")
#print("--#####-")
#print("###---#-")
#print("#&--#-#-")
#print("###-#-#-")
#print("#-###-#-")
#print("#-#---##")
#print("##--##-#")
#print("#&-----#")
#print("########")

# Run the game
while gameRunning == True:
    game(board)
    userInput = input("User the WASD keys on your device to control your character: ")
    board[row][column] = '-'

#def moveRight()
    if userInput == "d":
        column += 1
#def moveLeft()
    elif userInput == "a":
        column -= 1
#def moveUp()
    elif userInput == "w":
        row -= 1
#def moveDown()
    elif userInput == "s":
        row += 1
    
    board[row][column] = 'P'

# if there is a barrier (#)
    if board[row][column] == '#':
        if userInput == "d":
            column -= 1

        elif userInput == "a":
            column += 1

        elif userInput == "w":
            row += 1

        elif userInput == "s":
            row -= 1

        board[row][column] = 'P'


# Game ending condition
    if player == board[7][1]:
        print("You Win!")
        gameRunning = False