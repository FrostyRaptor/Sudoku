import random

# Done
def print_board(board):
    result = ''
    num_one = 1
    num_two = 1
    for lst in board:
        for item in lst:
            if num_one % 3 != 0:
                result += item + ' '
                num_one += 1
            else:
                result += item + '  '
                num_one += 1
        result += '\n'
        if num_two % 3 != 0:
            num_two += 1
        else:
            result += '\n'
            num_two += 1
    return result

# Done
def check_row(board, num, row):
    lst = board[row]
    for item in lst:
        if num != item:
            continue
        else:
            return False
    return True

# Done
def check_column(board, num, column):
    for x in range(9):
        if board[x][column] != num:
            continue
        else:
            return False
    return True

def check_block(board, num, s_index):
    # Check 9x9 block in board
    return True

def check_all(board, num, row, column):
    if check_row(board, num, row):
        if check_column(board, num, column):
                return True
        else:
            return False
    else:
        return False

def assign_num(board, x, y):
    while True:
        num = random.randint(1,9)
        if check_all(board, num, x, y):
            return str(num)
        else:
            continue

def random_board(board):
    result = board

    for x in range(9):
        for y in range(9):
            result[x][y] = assign_num(result, x, y)

    return result

board = [['00', '01', '02', '03', '04', '05', '06', '07', '08'],
         ['10', '11', '12', '13', '14', '15', '16', '17', '18'],
         ['20', '21', '22', '23', '24', '25', '26', '27', '28'],
         ['30', '31', '32', '33', '34', '35', '36', '37', '38'],
         ['40', '41', '42', '43', '44', '45', '46', '47', '48'],
         ['50', '51', '52', '53', '54', '55', '56', '57', '58'],
         ['60', '61', '62', '63', '64', '65', '66', '67', '68'],
         ['70', '71', '72', '73', '74', '75', '76', '77', '78'],
         ['80', '81', '82', '83', '84', '85', '86', '87', '88']]
board = random_board(board)

print(print_board(board))