# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import sys
import os
import HW5_easy

# from Home_Work.HW5_easy import copy_file  #  <----- Заменить Home_Work на название своей дирректории где лежит HW5_easy
# from Home_Work.HW5_easy import show_dir   #  <----- Заменить Home_Work на название своей дирректории где лежит HW5_easy
# from Home_Work.HW5_easy import help_1     #  <----- Заменить Home_Work на название своей дирректории где лежит HW5_easy


def make_dir():
    try:
        os.mkdir(input('Введите имя папки:'))
        print('Папка успешно создана')
    except Exception:
        print('Ошибка создания. Папки уже созданы')

def remove_dir():
    try:
        y = input('Введите название папки в текущем каталоге для удаления:')
        os.rmdir(y)
    except Exception:
        print('Вы ввели несуществующее имя папки')
    else:
        print('Папка', y, 'успешно удалена!')

key = sys.argv
answer = ''

while answer != 'q':
    answer = input('Введите команду из списка. Для выхода нажмите "q":')
    try:
        if answer == 'copy_file':
            HW5_easy.copy_file(key[0])
            print(key[0],'Успешно скопирован')
        elif answer == 'dirshow':
            HW5_easy.show_dir()
        elif answer == 'help_1':
            HW5_easy.help_1()
        elif answer == 'mkdir':
            make_dir()
        elif answer == 'removedir':
            remove_dir()
        else:
            if answer != 'q':
                print('Данная команда ещё не реализована')
    except Exception:
        print('Чтото пошло не так')