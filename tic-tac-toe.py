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
    for row in range(6):
        for col in range(8):
            if (board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3] and board[row][col] == 'X'):
                print("Player 1 WINS")
                return True
            if (board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3] and board[row][col] == 'O'):
                print("Player 2 WINS")
                return True
    return False

def checkVertical(board):
    for col in range(8):
        for row in range(4):
            if (board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col] and board[row][col] == 'X'):
                print("Player 1 WINS")
                return True
            if (board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col] and board[row][col] == 'O'):
                print("Player 2 WINS")
                return True
    return False

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

    board[3][0] == 'X'
    board[3][1] == 'X'
    board[3][2] == 'X'
    board[3][3] == 'X'

    for i in range(6, -1, -1):
        if board[i][choice] == digit:
            board[i][choice] = token
            player += 1
            break

    
    displayBoard()







