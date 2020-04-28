game = [
    [7, 8, 9],
    [4, 5, 6],
    [1, 2, 3],
]


def player_input():
    marker = ""

    while not (marker == "X" or marker == "O"):
        marker = input("Player 1: Do you want to play X or O: ").upper()

    if marker == "X":
        return ("X", "O")
    else:
        return ("O", "X")


player_marker = player_input()
player1_marker = player_marker[0]
player2_marker = player_marker[1]


def print_game_board():
    for i, row in enumerate(game):
        for j, _ in enumerate(row):
            print(str(game[i][j]) + " ", end="")
        print()


def check_player_choice(player_choice):
    (x, y) = player_tile(player_choice)
    if (type(game[x][y])) is str:
        return True
    else:
        return False


def game_map():
    print_game_board()
    while True:
        player1_choice = int(input("Player 1: Pick a tile to play: "))
        while check_player_choice(player1_choice):
            player1_choice = int(input("Player 1: Pick another tile: "))

        (x, y) = player_tile(player1_choice)
        game[x][y] = player_marker[0]
        print_game_board()
        if win_con(player1_marker):
            print("Player 1 has won the game!")
            break
        elif draw_con():
            print("The game is a draw!")
            break

        player2_choice = int(input("Player 2: Pick a tile to play: "))
        while check_player_choice(player2_choice):
            player2_choice = int(input("Player 2: Pick another tile: "))

        (x, y) = player_tile(player2_choice)
        game[x][y] = player_marker[1]
        print_game_board()
        if win_con(player2_marker):
            print("Player 2 has won the game!")
            break
        elif draw_con():
            print("The game is a draw!")
            break


def player_tile(player_choice):
    # print(type(player_choice))
    if player_choice == 1:
        return (2, 0)
    elif player_choice == 2:
        return (2, 1)
    elif player_choice == 3:
        return (2, 2)
    elif player_choice == 4:
        return (1, 0)
    elif player_choice == 5:
        return (1, 1)
    elif player_choice == 6:
        return (1, 2)
    elif player_choice == 7:
        return (0, 0)
    elif player_choice == 8:
        return (0, 1)
    elif player_choice == 9:
        return (0, 2)


def win_con(player_marker):
    return (
        (
            game[0][0] == player_marker
            and game[0][1] == player_marker
            and game[0][2] == player_marker
        )
        or (  # 7 8 9 Top Row
            game[1][0] == player_marker
            and game[1][1] == player_marker
            and game[1][2] == player_marker
        )
        or (  # 4 5 6 Middle Row
            game[2][0] == player_marker
            and game[2][1] == player_marker
            and game[2][2] == player_marker
        )
        or (  # 1 2 3 Bottom Row
            game[0][0] == player_marker
            and game[1][0] == player_marker
            and game[2][0] == player_marker
        )
        or (  # 7 4 1 Left Column
            game[0][1] == player_marker
            and game[1][1] == player_marker
            and game[2][1] == player_marker
        )
        or (  # 8 5 2 Middle Column
            game[0][2] == player_marker
            and game[1][2] == player_marker
            and game[2][2] == player_marker
        )
        or (  # 9 6 3 Right Column
            game[0][0] == player_marker
            and game[1][1] == player_marker
            and game[2][2] == player_marker
        )
        or (  # 7 5 3 Diagonal
            game[0][2] == player_marker
            and game[1][1] == player_marker
            and game[2][1] == player_marker
        )
    )  # 9 5 2 Diagonal


def draw_con():
    return (
        (
            type(game[0][0]) is str
            and type(game[0][1]) is str
            and type(game[0][2]) is str
        )
        and (  # 7 8 9
            type(game[1][0]) is str
            and type(game[1][1]) is str
            and type(game[1][2]) is str
        )
        and (  # 4 5 6
            type(game[2][0]) is str
            and type(game[2][1]) is str
            and type(game[2][2]) is str
        )
    )  # 1 2 3


game_map()
