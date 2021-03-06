# Третьяков Роман Викторович
# Факультет Geek University Python-разработки
# Основы языка Python
# Урок 1
# Задание 4:
# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

# В теоретической части преподаватель проговорился про функцию max, применимую к строкам
# Отсюда решение задачи может быть таким:
# get_num = input('Введите целое положительное число: ')
# print(f'Самая большая цифра в числе {get_num} равна {max(get_num)}')

# Если следовать строго тексту задания, то...
number = int(input('Введите целое положительное число: '))

max_digit = 0
while number != 0:
    digit = number % 10

    if digit > max_digit:
        max_digit = digit

    number = number // 10

print(f'Самая большая цифра во введенном числе равна {max_digit}')
