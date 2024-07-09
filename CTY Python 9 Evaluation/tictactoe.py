# 6/30/2024


import random

player = 'X'
player2 = 'O'
winner = None
gameRunning = True
winstatus = False
board = ['-','-','-',
         '-','-','-',
         '-','-','-']
#first setup the board 
def board_(board):
    # board = ['-','-','-',
    #          '-','-','-',
    #          '-','-','-']
    #board[6] = '-'
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])
    #board[6] = '-'
    return board

print(board_(board))

#take the input
def input_(board):
    inp = int(input("Enter the position : "))
    board = board_(board)
    if inp >= 1 and inp <= 9:
        print(inp)
        if board[inp-1] == '-':
            board[inp-1] = 'X'
        #print(board)

    else:
        print('Please check the input value before playing the game')

input_(board)

#check winning situations for players
def checkHorizontal(board):
    if board[0] == board[1] == board[2] and board[0] != '-':
        print('YaY you won!!!')
        winstatus = True
        gameRunning = False
        #return True
    elif board[3] == board[4] == board[5] and board[3] != '-':
        print('yay')
        winstatus = True
        gameRunning = False
    elif board[6] == board[7] == board[8] and board[6] != '-':
        print('yay')
        winstatus = True
        gameRunning = False

def checkVertical(board):
    if board[0] == board[3] == board[6] and board[0] != '-':
        print('yay') 
        winstatus = True
        gameRunning = False
    elif board[1] == board[4] == board[7] and board[1] != '-':
        print('yay')
        winstatus = True
        gameRunning = False
    elif board[2] == board[5] == board[8] and board[2] != '-':
        print('yay')
        winstatus = True
        gameRunning = False

def checkDiagonal(board):
    if board[0] == board[4] == board[8] and board[0] != '-':
        print('yay')
        winstatus = True
        gameRunning = False

    elif board[2] == board[4] == board[6] and board[2] != '-':
        print('yay')
        winstatus = True
        gameRunning = False


def checkTie(board):
    for i in range(0,0):
        if board[i] != '-':
            print('Its a TIE')
            gameRunning = False

def switchPlayer(board):
    rand_ = random.randint(0,9)
    #board[rand_] = 'O'
    if board[rand_] != 'X' and board[rand_] == '-':
        board[rand_] = 'O'
    


while gameRunning:
    input_(board)
    checkHorizontal(board)
    checkVertical(board)
    checkDiagonal(board)
    checkTie(board)
    switchPlayer(board)
    board_(board)
