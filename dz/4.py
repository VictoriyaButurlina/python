# Задача 1. Напишите функцию для транспонирования матрицы

def transpose_matrix(matrix):
    # Определение числа строк и столбцов в исходной матрице
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Создание пустой матрицы для транспонирования
    transposed = [[0 for _ in range(num_rows)] for _ in range(num_cols)]

    # Заполнение транспонированной матрицы
    for i in range(num_rows):
        for j in range(num_cols):
            transposed[j][i] = matrix[i][j]

    return transposed

# Пример 
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed_matrix = transpose_matrix(matrix)

# Вывод транспонированной матрицы
for row in transposed_matrix:
    print(row)

# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
# где ключ — значение переданного аргумента, а значение — имя аргумента. 
# Если ключ не хешируем, используйте его строковое представление.

def key_parameters_to_dictionary(**kwargs):
    """Функция перевода ключевых параметров в словарь."""

    new_dict = {}
    for key, value in kwargs.items():

        new_dict[hash(value) if hash(value) == value else str(value)] = key

    return new_dict


print(key_parameters_to_dictionary(course='python', homework=4, task=2))

# Задача 3. Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
#  Дополнительно сохраняйте все операции поступления и снятия средств в список.


def apply_tax(amount, tax_rate):
    return amount - amount * tax_rate

def deposit(balance, op_count, transactions):
    amount = int(input("Введите сумму для пополнения: "))
    if amount % 50 == 0:
        tax_rate = 0.10
        if op_count % 3 == 2:
            tax_rate += 0.03
        balance += apply_tax(amount, tax_rate)
        op_count += 1
        transactions.append(f"Пополнение: +{amount} у.е.")
    return balance, op_count

def withdraw(balance, op_count, transactions):
    amount = int(input("Введите сумму для снятия: "))
    if amount % 50 == 0 and amount <= balance:
        fee = min(max(amount * 0.015, 30), 600)
        balance -= amount + fee
        op_count += 1
        transactions.append(f"Снятие: -{amount} у.е. (включая комиссию {fee} у.е.)")
    return balance, op_count

def main():
    balance, op_count = 0, 0
    transactions = []

    while True:
        print(f"Баланс: {balance} у.е.")
        action = input("Действие (пополнить/снять/выйти): ")

        if action == "пополнить":
            balance, op_count = deposit(balance, op_count, transactions)
        elif action == "снять":
            balance, op_count = withdraw(balance, op_count, transactions)
        elif action == "выйти":
            print("Программа завершена.")
            break
        else:
            print("Неверное действие. Попробуйте снова.")

        if balance > 5000000:
            balance = apply_tax(balance, 0.10)

    print("Операции:")
    for transaction in transactions:
        print(transaction)

if __name__ == "__main__":
    main()