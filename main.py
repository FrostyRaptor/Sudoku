import random

def print_board(board):
    result = ''
    count = 0
    for lst in board:
        for item in lst:
            result += ' '.join(item)
            result += '  '
        count += 1
        result += '\n'
        if count % 3 != 0:
            continue
        else:
            result += '\n'
    return result

def check_row(board, num, index):
    for x in range(3):
        for y in range(3):
            if board[index][x][y] != num:
                continue
            else:
                print('Check 5')
                return False
    return True

def random_board(board):
    lst = []
    for x in range(9):
        for y in range(3):
            for z in range(3):
                while True:
                    num = random.randint(1,9)
                    if check_row(lst, num, x):
                        lst[x][y][z] = str(num)
                        break
                    else:
                        continue 
    return lst

board = [[["000", "001", "002"], ["010", "011", "012"], ["020", "021", "022"]], 
         [["100", "101", "102"], ["110", "111", "112"], ["120", "121", "122"]], 
         [["200", "201", "202"], ["210", "211", "212"], ["220", "221", "222"]], 
         [["300", "301", "302"], ["310", "311", "312"], ["320", "321", "322"]], 
         [["400", "401", "402"], ["410", "411", "412"], ["420", "421", "422"]], 
         [["500", "501", "502"], ["510", "511", "512"], ["520", "521", "522"]], 
         [["600", "601", "602"], ["610", "611", "612"], ["620", "621", "622"]], 
         [["700", "701", "702"], ["710", "711", "712"], ["720", "721", "722"]], 
         [["800", "801", "802"], ["810", "811", "812"], ["820", "821", "822"]]]
board = random_board(board)

print(print_board(board))
print('end')