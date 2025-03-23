import random


board = ['-' for x in range(10)]

currentPlayer = 'X'
winner = None
gameIsRunning = True

# printing The Game Board

def printBoard(board):
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print("---------")
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print("---------")
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

# Taking Input from the User

def playerInput(board):
    playerinput = int(input("Enter a number 1-9: "))
    if playerinput == "":
        print("Please Enter a Number")
    if playerinput >= 1 and playerinput <= 9 and board[playerinput-1] == '-':
        board[playerinput-1] = currentPlayer
    else:
        print("Oops Player is Already There! Try Again")
        playerInput(board)



# Checking the Win or Tie

def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] != '-':
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != '-':
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != '-':
        winner = board[6]
        return True


def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] != '-':
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != '-':
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != '-':
        winner = board[2]
        return True
    



def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] != '-':
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != '-':
        winner = board[2]
        return True




def checkTie(board):
    global gameIsRunning
    if "-" not in board:
        printBoard(board)
        print("It's a Tie")
        gameIsRunning = False



def checkWin(board):
    global gameIsRunning
    if checkHorizontal(board) or checkRow(board) or checkDiagonal(board):
        printBoard(board)
        print("The Winner is " + winner)
        gameIsRunning = False



# awitch the player


def switchPlayer():
    global currentPlayer
    if currentPlayer == 'X':
        currentPlayer = 'O'
    else:
        currentPlayer = 'X'



# computer game

def computer(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == '-':
            board[position] = currentPlayer
            switchPlayer()





while gameIsRunning:
    printBoard(board) # Printing the Board
    playerInput(board) # Taking Input from the User
    switchPlayer() # Switching the Player
    computer(board) # Computer Game
    checkWin(board) # Checking the Win
    checkTie(board) # Checking the Tie


