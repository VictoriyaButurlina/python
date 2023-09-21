"""
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. Функцию
hex используйте для проверки своего результата.
"""

# BASE = 16
# DATA = '0123456789ABCDEF'
#
# while True:
#     number = int(input('Введите целое число: '))
#     if number >= 0:
#         break
#
# _number = number
# result = ''
#
# while _number:
#     _num = _number % BASE
#     result = DATA[_num] + result
#     _number //= BASE
#
# print(f'Шестнадцатеричное строковое представление числа {number} - {result}')
# print(hex(number))
#
# import fractions
# import math

"""
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.  
"""

import fractions

def add_fractions(fraction1, fraction2):
  # возвращает сумму двух дробей
  return fractions.Fraction(fraction1.numerator + fraction2.numerator,
                            fraction1.denominator + fraction2.denominator)

def multiply_fractions(fraction1, fraction2):
    # возвращает произведение двух дробей
    return fractions.Fraction(fraction1.numerator * fraction2.numerator,
                              fraction1.denominator * fraction2.denominator)

def main():
    # основная функция
    fraction1 = input("Введите первую дробь: ")
    fraction2 = input("Введите вторую дробь: ")
    fraction1 = fractions.Fraction(fraction1)
    fraction2 = fractions.Fraction(fraction2)
    print("Сумма дробей:", add_fractions(fraction1, fraction2))
    print("Произведение дробей:", multiply_fractions(fraction1, fraction2))

if __name__ == "__main__":
    main()
