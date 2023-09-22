# Задача 1 Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


# import os

# def get_path_info(path):
#     path_parts = path.split(os.sep)
#     filename = path_parts[-1]
#     name, extension = os.path.splitext(filename)
#     return path, name, extension


# if __name__ == "__main__":
#     path = "C:\Windows\win.ini"
#     info = get_path_info(path)
#     print(info)

# Задача 2 ✔ Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате
# получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии

# names = ["Иван", "Петр", "Сергей"]
# rates = [1000, 2000, 3000]
# bonuses = ["10.25%", "12.5%", "15.0%"]
# result = {name: rate * float(bonus.strip('%')) / 100 for name, rate, bonus in zip(names, rates, bonuses)}

# print(result)

# Задача 3 ✔ Создайте функцию генератор чисел Фибоначчи (см. Википедию).
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


for i in fibonacci(10):
    print(i)
