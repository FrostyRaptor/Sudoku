import random

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

def check_row(board, num, row):
    lst = board[index]
    for item in lst:
        if num != item:
            continue
        else:
            return False
    return True

def check_column(board, num, column):
    # Check column in the board
    return 0

def check_block(board, num, s_index):
    # Check 9x9 block in board
    return 0

def check_all(board, num, column, s_index):
    # Check all
    return 0

def random_board(board):
    # Ranomize the board from its default
    return 0

board = [['00', '01', '02', '03', '04', '05', '06', '07', '08'],
         ['10', '11', '12', '13', '14', '15', '16', '17', '18'],
         ['20', '21', '22', '23', '24', '25', '26', '27', '28'],
         ['30', '31', '32', '33', '34', '35', '36', '37', '38'],
         ['40', '41', '42', '43', '44', '45', '46', '47', '48'],
         ['50', '51', '52', '53', '54', '55', '56', '57', '58'],
         ['60', '61', '62', '63', '64', '65', '66', '67', '68'],
         ['70', '71', '72', '73', '74', '75', '76', '77', '78'],
         ['80', '81', '82', '83', '84', '85', '86', '87', '88']]
# board = random_board(board)

print(print_board(board))