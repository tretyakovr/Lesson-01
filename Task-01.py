# Третьяков Роман Викторович
# Факультет Geek University Python-разработки
# Основы языка Python
# Урок 1
# Задание 1:
# Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя
# несколько чисел и строк и сохраните в переменные, выведите на экран

var_int = 1
var_float = 2.1
var_str = 'Test string'
var_bool = True

print('var_int =', var_int, type(var_int))
print('var_float =', var_float, type(var_float))
print('var_str =', var_str, type(var_str))
print('var_bool =', var_bool, type(var_bool))

get_int = int(input('Введите целое число: '))
print('get_int = ', get_int, type(get_int))

get_float = float(input('Введите число с плавающей запятой: '))
print('get_float = ', get_float, type(get_float))

get_str = input('Введите строку: ')
print('get_str = ', get_str, type(get_str))