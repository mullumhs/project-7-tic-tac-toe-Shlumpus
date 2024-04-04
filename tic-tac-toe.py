board = []

def initialiseBoard(): 

    for i in range(7):
        row = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
        board.append(row)

def displayBoard():
    for i in board:
        for digit in i:
            print(digit, end=' ')
        print()

initialiseBoard()
displayBoard()
player = 1


while True:
    
    token = 'X'
    if player % 2 == 0:
        token = 'O'
    player += 1

    choice = int(input("Choose your column: "))
    choice -= choice

    for i in range(6, -1, -1):
        if i == '-':
            board[i][choice]
    
    displayBoard()







