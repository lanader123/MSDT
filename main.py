"""
# Пример программы на Python
## Игра крестики-нолики
+ Игровое поле;
+ Ввод позиции;
+ Условие победы;
+ Случайный игрок;
+ Модульность игроков.
"""
import random


PLAYER_SYMBOLS = ".OX"
ROW_INDICES = "ABC"
COLUMN_INDICES = "123"


def print_game_map(gm):
    for row in gm:
        for cell in row:
            print(PLAYER_SYMBOLS[cell], end=" ")
        print()


def is_tie(gm):
    for row in gm:
        for cell in row:
            if cell == 0:
                return False
    return True


def is_completed(gm):
    assert len(gm) > 0, "Поле должно иметь хотя бы одну строку"
    assert len(gm[0]) > 0, "Поле должно иметь хотя бы одну колонку"
    for row in gm:
        first = row[0]
        if first != 0:
            for cell in row[1:]:
                if cell != first:
                    break
            else:
                return True, first

    for j in range(len(gm[0])):
        first = gm[0][j]
        if first != 0:
            for i in range(1, len(gm)):
                if gm[i][j] != first:
                    break
            else:
                return True, first

    assert len(gm) == len(gm[0]), "TODO: Пока работает только на квадратных полях"
    diag = gm[0][0]
    if diag != 0:
        for i in range(len(gm)):
            if gm[i][i] != diag:
                break
        else:
            return True, diag

    inv_diag = gm[0][len(gm) - 1]
    if inv_diag != 0:
        for i in range(len(gm)):
            if gm[i][len(gm) - i - 1] != inv_diag:
                break
        else:
            return True, inv_diag

    return is_tie(gm), 0


def random_player(gm, player):
    row_index = list(range(len(gm)))    # [0, 1, 2]
    random.shuffle(row_index)           # [1, 0, 2]
    for i in row_index:
        row = gm[i]
        empty_cells = []
        for j, cell in enumerate(row):
            if cell == 0:
                empty_cells.append(j)

        if len(empty_cells) > 0:
            player_row = i
            player_column = random.choice(empty_cells)
            return player_row, player_column


def input_player(gm, player):
    while True:
        print_game_map(gm)

        player_input = input(f"Игрок №{player}({PLAYER_SYMBOLS[player]}), введите позицию: ")
        if len(player_input) != 2:
            print("Введено неверное количество символов. Формат: A1.")
            continue
        player_row, player_column = player_input

        player_row = ROW_INDICES.find(player_row)
        if player_row == -1:
            print("Введен неверный номер ряда. Укажите букву:", ','.join(ROW_INDICES))
            continue

        player_column = COLUMN_INDICES.find(player_column)
        if player_column == -1:
            print("Введен неверный номер колонки. Укажите цифру:", ','.join(COLUMN_INDICES))
            continue

        if gm[player_row][player_column] > 0:
            print("Эта ячейка уже занята, выберите другую.")
            continue

        return player_row, player_column


# TODO: Сделать размер доски изменяемым (например, спросить пользователя перед началом игры)
game_map = []
for _ in range(3):
    temp = []
    for _ in range(3):
        temp.append(0)
    game_map.append(temp)


current_player = 1
completed, who_won = False, 0

# TODO: Сделать возможность выбора оппонента (или просто бота на бота натравить :P)
game_players = [None, input_player, random_player]

while not completed:
    player_function = game_players[current_player]
    row_index, column_index = player_function(game_map, current_player)
    game_map[row_index][column_index] = current_player

    completed, who_won = is_completed(game_map)

    if current_player == 1:
        current_player = 2
    elif current_player == 2:
        current_player = 1
    else:
        print("Неверный номер игрока")
        exit(1)


print_game_map(game_map)
if who_won != 0:
    print(f"Игрок №{who_won} победил!")
else:
    print("Игра завершилась на ничье.")
