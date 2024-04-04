board = []

def initialiseBoard(): 
    print("---CONNECT FOUR---")
    print()
    print("1 2 3 4 5 6 7 8 9")
    for i in range(7):
        digit = '-'
        row = [digit, digit, digit, digit, digit, digit, digit, digit, digit, ]
        board.append(row)

def displayBoard():

    for i in board:
        for digit in i:
            print(digit, end=' ')
        print()

initialiseBoard()
displayBoard()
player = 1

def checkHorizontal(board):
    for row in range:
        for col in range(4):
            if (board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3] != digit):
                return True
    return False

def checkDiagonal(board):
    for row in range(3):
        for col in range(4):
            

while True:
    digit = '-'

    token = 'X'
    if player % 2 == 0:
        token = 'O'

    if player % 2 == 0:
        choice = (input("Choose your column P2: "))
    elif player % 2 != 0:
        choice = (input("Choose your column P1: "))
        
    choice = int(choice)
    choice -= 1

    for i in range(6, -1, -1):
        if board[i][choice] == digit:
            board[i][choice] = token
            player += 1
            break

    
    displayBoard()







