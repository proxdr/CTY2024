print("Tic Tac Toe")

def setup(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print("-----")
    print(board[3] + '|' + board[4] + '|' + board[5])
    print("-----")
    print(board[6] + '|' + board[7] + '|' + board[8])

# Creates actual availible spaces on board
board = [' '] * 9

# Determinds if there is a win
def winCheck(board, player):
    # Vertical check
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True
    # Horizontal check
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    #Diagonal checks
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

user = 'X'
moves = 0
while True:
    setup(board)
    # Tells user x to enter their position
    userInput = int(input("Player " + user + ", enter your spot (1-9): ")) - 1

    if userInput >= 0 and userInput <= 10:
        # Play until someone wins, each turn increases the move count
        if board[userInput] == ' ':
            board[userInput] = user
            moves += 1
            if winCheck(board, user):
                setup(board)
                print("Player " + user + " wins!")
                break
            # If every spot on the board is taken and there is no win, it is a tie
            elif moves == 9:
                setup(board)
                print("It's a tie!")
                break
            # Switch between user X and O
            else:
                if user == 'X':
                    user = 'O'
                else:
                    user = 'X'
        # If the blank is taken, a message will print
        else:
            print("That spot is already taken. Try again.")
    else:
        print("Number must be 1 through 9")
