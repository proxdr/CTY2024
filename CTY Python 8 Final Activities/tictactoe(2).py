# 6/27/2024

print("Tic Tac Toe")
print(" | | ")
print("-----")
print(" | | ")
print("-----")
print(" | | ")

userInput = input("Enter your spot: ")
if userInput == 1:
    print("x| | ")
    print("-----")
    print(" | | ")
    print("-----")
    print(" | | ")
    
userInput = input("Enter your spot: ")
if userInput == 2:
    print(" |x| ")
    print("-----")
    print(" | | ")
    print("-----")
    print(" | | ")

userInput = input("Enter your spot: ")
if userInput == 3:
    print(" | |x")
    print("-----")
    print(" | | ")
    print("-----")
    print(" | | ")

    userInput = input("Enter your spot: ")
if userInput == 4:
    print(" | | ")
    print("-----")
    print("x| | ")
    print("-----")
    print(" | | ")

userInput = input("Enter your spot: ")
if userInput == 5:
    print(" | | ")
    print("-----")
    print(" |x| ")
    print("-----")
    print(" | | ")

userInput = input("Enter your spot: ")
if userInput == 6:
    print(" | | ")
    print("-----")
    print(" | |x")
    print("-----")
    print(" | | ")

userInput = input("Enter your spot: ")
if userInput == 1:
    print("x| | ")
    print("-----")
    print(" | | ")
    print("-----")
    print(" | | ")

    userInput = input("Enter your spot: ")
if userInput == 7:
    print(" | | ")
    print("-----")
    print(" | | ")
    print("-----")
    print("x| | ")

userInput = input("Enter your spot: ")
if userInput == 8:
    print(" | | ")
    print("-----")
    print(" | | ")
    print("-----")
    print(" |x| ")

userInput = input("Enter your spot: ")
if userInput == 9:
    print(" | | ")
    print("-----")
    print(" | | ")
    print("-----")
    print(" | |x")














print("Tic Tac Toe")

def print_board(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print("-----")
    print(board[3] + '|' + board[4] + '|' + board[5])
    print("-----")
    print(board[6] + '|' + board[7] + '|' + board[8])

# Initialize an empty board
board = [' '] * 9

# Function to check if someone has won
def check_win(board, player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

current_player = 'X'
moves = 0
while True:
    print_board(board)
    userInput = int(input(f"Player {current_player}, enter your spot (1-9): ")) - 1

    if board[userInput] == ' ':
        board[userInput] = current_player
        moves += 1
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif moves == 9:
            print_board(board)
            print("It's a tie!")
            break
        else:
            current_player = 'O' if current_player == 'X' else 'X'
    else:
        print("That spot is already taken. Try again.")