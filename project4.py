game = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]


def game_board(game_map, player=0, row=0, column=0, just_display=True):
    try:
        print("   0  1  2  3")
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map
    except IndexError as e:
        print('Error: Input row/column in range 0-3.', e)
    except Exception as e:
        print('Something went wrong!', e)


def win(current_game):
    for row in game:
        print(row)
        if row.count(row[0]) == len(row) and row[0] != 0:
            print('Winner!')


    # horizontal winner
    for col in range(len(game)):
        check = []

        for row in game:
            check.append(row[col])

        if check.count(check[0]) == len(check) and check[0] != 0:
            print('Winner!')


    # diagonal winner
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])

    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])

