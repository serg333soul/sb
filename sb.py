def create_table():
    SPACE = ' '
    L_S = '0abcdefghij '
    
    f = [[i if j * i == 0 else SPACE for j in range(12)] for i in range(12)]
    f[0] = [L_S[i] for i in range(12)]

    return f

        

board = create_table()

def print_board(board):
    '''Печатаем доску в консоли'''
    for i in range(len(board) - 1):
        for j in range(len(board[i])):
            print('|'.rjust(2), str(board[i][j]).rjust(2), end=' ')
        print('')
        print('-' * 68)

print_board(board)
