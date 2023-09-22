from random import randint


def is_win(arrangements: list) -> bool:

    size_of_chessboard = 8
    chessboard_x = []
    chessboard_y = []

    for position in range(size_of_chessboard):

        x, y = arrangements[position]
        chessboard_x.append(x)
        chessboard_y.append(y)

    for i in range(size_of_chessboard):

        for j in range(i + 1, size_of_chessboard):

            if chessboard_x[i] == chessboard_x[j] or chessboard_y[i] == chessboard_y[j] \
                    or abs(chessboard_x[i] - chessboard_x[j]) == abs(chessboard_y[i] - chessboard_y[j]):

                return True

    return False


from random import randint

def is_win(positions):
    # Реализуйте функцию is_win, которая проверяет, является ли данное расположение ферзей успешным.
    pass

def generate_queen_arrangement(size_of_chessboard):
    while True:
        positions = []

        while len(positions) < size_of_chessboard:
            position = (randint(1, size_of_chessboard), randint(1, size_of_chessboard))

            if position not in positions:
                positions.append(position)

        if not is_win(positions):
            return positions
