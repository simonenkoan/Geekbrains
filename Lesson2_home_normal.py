# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

#
print("Задача 1")
import math

spisok1 = [2, -5, 8, 9, -25, 25, 4, 16, 100]
spisok2 = []

for x, y in enumerate(spisok1):
    if y > 0:
        # print(y, type(y))
        z = math.sqrt(y)
        if z ** 2 == y:
            spisok2.append(int(z))
print(spisok2)
print("")
# -------------------------------------------------------------------------------------------------------
# # Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# # Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# # Склонением пренебречь (2000 года, 2010 года)
#
print("Задача 2")
data = ['первое', 'второе', 'третье', 'четветое', 'пятое', 'шестое', 'седьмое', 'восьмое', 'девятое', 'десятое',
        'одиннадацтое', 'двенадцатое', 'тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое', 'семнадцатое', 'восемьнадцатое',
        'девятнадцатое', 'двадцатое', 'двадцать первое', 'двадцать второе', 'двадцать третье', 'двадцать четвертое',
        'двадцать пятое', 'двадцать шестое', 'двадцать седьмое', 'двадцать восьмое', 'двадцать девятое', 'тридцатое']
month = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
years = 'год'

def perevod_chisla(spisok, vvod_chisla):
    for x, y in enumerate(spisok):
        if vvod_chisla == (x + 1):
            return y

# while True:
data_input = int(input('Введите дату:'))
month_input = int(input('Введите месяц:'))
year_input = int(input('Введите год:'))
slovo_dnya = perevod_chisla(data, data_input)
slovo_mesyaca = perevod_chisla(month, month_input)
#
#             # ПЕРВЫЙ ВАРИАНТ РЕШЕНИЯ
#             # for x, y in enumerate(data):
#             #     if data_input == (x + 1):
#             #         slovo_dnya = y
#             # for x, y in enumerate(month):
#             #     if month_input == (x + 1):
#             #         slovo_mesyaca = y
print(slovo_dnya, slovo_mesyaca, year_input, years)
print("")

# -------------------------------------------------------------------------------------------------------
# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
print("Задача 3")
import random

spisok_new = []
i = 0
n = int(input("Сколько хотите элементов? Введите целое положительное число:"))
while i < n:
    y = random.randint(-100, 100)
    spisok_new.append(y)
    i += 1
print(spisok_new)
print("")

# ---------------------------------------------------------------------------------------------
# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

# A
print("Задача 4.А")
lst = [1, 2, 4, 5, 6, 2, 5, 2, 100, 200, 300, 200]
lst2 = list(set(lst))
print(lst2)
print("")

# B
print("Задача 4.Б")
lst = [1, 2, 4, 5, 6, 2, 5, 2, 100, 200, 300, 200]
lst2 = []

for y in lst:
    if lst.count(y) == 1:
        lst2.append(y)
print(lst2)
print("")
