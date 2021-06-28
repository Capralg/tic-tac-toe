x_count = 0
y_count = 0
messages = ['Game not finished', 'Draw', 'X wins', 'O wins', 'Impossible']
result_message = ''
# result_message = 'Game not finished'
start = [0, 1, 2, 0, 3, 6, 0, 2]
stop = [7, 8, 9, 3, 6, 9, 9, 7]
step = [3, 3, 3, 1, 1, 1, 4, 2]
coordinate_sell = ['1, 1', '1, 2', '1, 3', '2, 1', '2, 2', '2, 3', '3, 1', '3, 2', '3, 3']
user_input = '         '
count_move = 0

def print_screen(user_input):
    print("---------")
    print("|", user_input[0], user_input[1], user_input[2], "|")
    print("|", user_input[3], user_input[4], user_input[5], "|")
    print("|", user_input[6], user_input[7], user_input[8], "|")
    print("---------")

def check_input():
    coordinates = input('Enter the coordinates:').replace(" ", "")
    if not coordinates.isdigit():
        print('You should enter numbers!')
        return check_input()
    elif coordinates[0] not in ('1', '2', '3') or coordinates[1] not in ('1', '2', '3'):
        print('Coordinates should be from 1 to 3!')
        return check_input()
    else:
        coordinates: str = coordinates[0] + ', ' + coordinates[1]
        for i in range(9):
            if coordinates == coordinate_sell[i] and user_input[i] not in (' ', '_'):
                print('This cell is occupied! Choose another one!')
                return check_input()
    return coordinates

def move(coordinates, coordinate_sell, user_input, count_move):
    if count_move % 2 == 0:
        new_user_input = ['X' if coordinates == coordinate_sell[i] else user_input[i] for i in range(9)]
        return new_user_input
    else:
        new_user_input = ['O' if coordinates == coordinate_sell[i] else user_input[i] for i in range(9)]
        return new_user_input

def check_cells(user_input, result_message):
    win_flag = 0
    o_win = 0
    x_win = 0
    not_finished = [user_input[x] for x in range(9) if user_input[x] == ' ' or user_input[x] == '_']
    x_count = [user_input[x] for x in range(9) if user_input[x] == 'X']
    o_count = [user_input[x] for x in range(9) if user_input[x] == 'O']

    # if len(not_finished) != 0:
        # result_message = messages[0]

    for x in range(8):
        x_list = [user_input[i] for i in range(start[x], stop[x], step[x]) if user_input[i] == 'X']
        if len(x_list) == 3:
            result_message = messages[2]
            x_win = 1

    for x in range(8):
        x_list = [user_input[i] for i in range(start[x], stop[x], step[x]) if user_input[i] == 'O']
        if len(x_list) == 3:
            result_message = messages[3]
            o_win = 1

    if result_message != messages[2] and result_message != messages[3] and len(not_finished) == 0:
        result_message = messages[1]

    if (o_win == 1 and x_win == 1) or (abs(len(x_count) - len(o_count)) >= 2):
        result_message = messages[4]

    #print(result_message)
    return result_message

print_screen(user_input)

while result_message == '':
    coordinates = check_input()
    user_input = move(coordinates, coordinate_sell, user_input, count_move)
    print_screen(user_input)
    result_message = check_cells(user_input, result_message)
    count_move += 1

print(result_message)
