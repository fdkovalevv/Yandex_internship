def check_I(board, n):
    for j in range(n):
        if board[0][j] != '#' or board[n-1][j] != '#':
            return False
    for i in range(n):
        if board[i][0] != '#' or board[i][n-1] != '#':
            return False
    return True

def check_O(board, n):
    for i in range(n):
        for j in range(n):
            if board[i][j] == '#':
                value = ((0 < j < n-1) and (0 < i < n-1))
                if value:
                    internal = board[i-1][j-1] == board[i+1][j+1] == '.' and \
                               board[i-1][j+1] == board[i+1][j-1] == '.'
                    if internal:
                        return True
    return False

def check_C(board, n):
    for i in range(n):
        for j in range(n):
            if board[i][j] == '#':
                # Check if the right border is at the edge.
                if j < n - 1 and board[i][n-1] == '#':
                    return True
    return False

def check_L(board, n):
    for i in range(n):
        for j in range(n):
            if board[i][j] == '#':
                if i < n - 1 and j < n - 1 and j == n - 1:
                    return True
    return False

def check_H(board, n):
    # check for H structure
    for j in range(n):
        if board[0][j] == '#' and board[n-1][j] == '#':
            if j > 0 and board[n//2][j] == '#':
                return True
    return False

def check_P(board, n):
    for i in range(n):
        for j in range(n):
            if board[i][j] == '#':
                if (i < n-1 and j < n-1 and board[i][n-1] == '#' and
                    board[n-1][j] == '#'):
                    return True
    return False

# Основная функция
def identify_letter(n, board):
    if check_I(board, n):
        return 'I'
    if check_O(board, n):
        return 'O'
    if check_C(board, n):
        return 'C'
    if check_L(board, n):
        return 'L'
    if check_H(board, n):
        return 'H'
    if check_P(board, n):
        return 'P'
    return 'X'

# Чтение входных данных
n = int(input().strip())
board = [input().strip() for _ in range(n)]

# Вывод результата
print(identify_letter(n, board))