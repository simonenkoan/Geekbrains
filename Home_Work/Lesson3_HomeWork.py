# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"

def output_information(*args):
    print('{}, {} год(а), проживает в городе {}'.format(*args))

output_information(*['Василий', '21', 'Москва'])


# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

def max_number_output(*args):
    max = 0
    for i in args:
        if i > max:
            max = i
    print(max)

max_number_output(*[2000,100,1000])


# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов

def max_len_str(*args):
    max = []
    for i in args:
        if len(i) > len(max):
            max = i
    print(max)
max_len_str(*['aaa', 'vvvvvvvvvvv', 'qweqweqwe', '1', 'dddd'])


# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.


employees = ['Дмитрий', 'Сергей', 'Владислав', 'Виктор']

zp = [12000, 20000, 24000, 500000]

spisok_zarplat = {}

def zp_for_employees( names , money ):
    y = dict(zip(names, money))
    return y

nnn = zp_for_employees(employees, zp)

with open('salary.txt', 'a', encoding='UTF-8') as salary:
    for key, value in nnn.items():
        if value < 500000:
            salary.write('{} - {} \n'.format(key, value))
salary_new = []
with open('salary.txt', encoding='UTF-8') as salary:
    for line in salary:
        new_line = line.split()
        zp_minus_13 = int(new_line[2]) * 0.8
        salary_new.append([new_line[0], int(zp_minus_13)])

with open('salary_new.txt', 'a', encoding='UTF-8') as salary:
    for value in salary_new:
        salary.write('{} - {} \n'.format(value[0], value[1]))

print("Было создано два файла . Salary - где содержится информация о з.п. не учитывая тех кто получает больше 500т.р, и Salary_new где перечислены з.п. - 13%")








