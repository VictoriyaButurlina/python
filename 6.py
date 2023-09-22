# Задача 1. В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

# import datetime

# def is_valid_date(date_str):
#     try:
#         date = datetime.datetime.strptime(date_str, "%d.%m.%Y")
#         return date.date()
#     except ValueError:
#         return None


# def main():
#     date_str = input("Введите дату в формате dd.mm.yyyy: ")
#     date = is_valid_date(date_str)
#     if date is not None:
#         print("Дата корректна:", date)
#     else:
#         print("Дата некорректна")


# if __name__ == "__main__":
#     main()
# Задача 2. Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
#  Известно, что на доске 8×8 можно расставить 8 ферзей так, 
# чтобы они не били друг друга. 
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. 
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг 
# друга верните истину, а если бьют - ложь.
# Задача 3. Напишите функцию в шахматный модуль. 
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
from module.chess import is_win


if __name__ == '__main__':

    arrangements = [(8, 5), (4, 2), (5, 5), (4, 5), (5, 3), (3, 2), (5, 1), (5, 2)]
    print(f'''Ферзи {'бьют' if is_win(arrangements) else 'не бьют'} друг друга''')

# from module.chess import generate_queen_arrangement

# NEAD_NUMBER_OF_POSITIONS = 4
# CHESSBOARD_SIZE = 8  # Размер шахматной доски

# arrangements = [generate_queen_arrangement(CHESSBOARD_SIZE) for _ in range(NEAD_NUMBER_OF_POSITIONS)]

# for arrangement in arrangements:
#     print(arrangement)