board = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]


def print_board(x):
    for i in range(3):
        print(x[i][0], x[i][1], x[i][2])


def over1(player, board):
    for i in range(3):
        nr = 0
        for j in range(3):
            if board[i][j] != player:
                nr = 1
                break
        if nr == 0:
            return 1
    for j in range(3):
        nr = 0
        for i in range(3):
            if board[i][j] != player:
                nr = 1
                break
        if nr == 0:
            return 1
    nr1 = 0
    for i in range(3):
        if board[i][i] != player:
            nr1 = 1
            break
    if nr1 == 0:
        return 1
    nr2 = 0
    for i in range(3):
        if board[i][2 - i] != player:
            nr2 = 1
            break
    if nr2 == 0:
        return 1
    return 0


print_board(board)
while True:
    print('Player1, pick your choice(index): ')
    i1 = int(input('index of line: '))
    j1 = int(input('index of column: '))
    while board[i1][j1] != '-':
        print('invalid position')
        i1 = int(input('index of line: '))
        j1 = int(input('index of column: '))
    board[i1][j1] = 'x'
    print_board(board)
    if over1('x', board) == 1:
        print('Player 1 wins')
        break
    stop1 = 0
    for k in range(3):
        if '-' in board[k]:
            stop1 = 1
            break
    if stop1 == 0:
        print('It\'s a tie')
        break
    print('Player2, pick your choice(index): ')
    i1 = int(input('index of line: '))
    j1 = int(input('index of column: '))
    while board[i1][j1] != '-':
        print('invalid position')
        i1 = int(input('index of line: '))
        j1 = int(input('index of column: '))
    board[i1][j1] = '0'
    print_board(board)
    if over1('0', board) == 1:
        print('Player 2 wins')
        break
