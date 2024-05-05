board = []

def initialiseBoard():
    print("---- TIC TAC TOE ----")
    print()
    for i in range(3):
        digit = "-"
        row = [digit, digit, digit]
        board.append(row)

def displayBoard():
    print("   1 2 3")
    line = 0
    for i in board:
        if line == 0:
            letter = "A"
            
        if line == 1:
            letter = "B"

        if line == 2:
            letter = "C"
        line = line + 1
        print(letter, '|', end= '')
        for column in i:
            print(column, end= '|')
        print()

def checkHorizontal():
    for row in range(2):
        if (board[row][0] == board[row][1] == board[row][2] and board[row][0] == 'X'):
            print("Player 1 WINS")
            return True
        if (board[row][0] == board[row][1] == board[row][2] and board[row][0] == 'O'):
            print("Player 2 WINS")
            return True
    return False

def checkVertical():
    for col in range(2):
        if (board[0][col] == board[1][col] == board[2][col] and board[0][col] == 'X'):
            print("Player 1 WINS")
            return True
        if (board[0][col] == board[1][col] == board[2][col] and board[0][col] == 'O'):
            print("Player 2 WINS")
            return True
    return False

def checkDiagonal():
    for row in range(2):
        for col in range(2):
            if (board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] and board[row][col] == 'X'):
                print("Player 1 WINS")
                return True
            if (board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] and board[row][col] == 'O'):
                print("Player 2 WINS")
                return True
    return False
    

initialiseBoard()
displayBoard()
player = 1

while True:
    token = 'X'
    if player % 2 == 0:
        token = 'O'

    if player % 2 == 0:
        choice2 = str((input("Choose your row P2: ")))
        choice = (input("Choose your column P2: "))
    elif player % 2 != 0:
        choice2 = str((input("Choose your row P1: ")))
        choice = (input("Choose your column P1: "))
        
    choice = int(choice)
    choice -= 1

    if choice2 == "A":
        rowline = 0
    elif choice2 == "B":
        rowline = 1
    elif choice2 == "C":
        rowline = 2

    for i in range(2, -1, -1):
        if board[rowline][choice] != token:
            board[rowline][choice] = token
            player += 1
            break

    displayBoard()
    checkHorizontal()
    checkVertical()






