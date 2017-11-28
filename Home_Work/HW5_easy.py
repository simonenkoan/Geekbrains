# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import psutil
import shutil

def answer_choose():
    print("")
    print("Отлично. Выберите операцию")
    print("[1] - вывести список файлов ")
    print("[2] - вывести информацию о текущей директории ")
    print("[3] - вывести информацию о количестве CPU ")
    print("[4] - дублирование файлов в текущей дирректории")
    print("[0] - для выхода в меню")
    print("")

def proverka_file(filename_i):
    if os.path.isfile(filename_i):
        shutil.copy(filename_i, newFileName)

spisok1 = ['dir_'+ str(i) for i in range(10)]

def make_dir(spisok):
    try:
        for i in spisok:
            os.mkdir(i)
    except Exception:
        print('папка уже создана')

def remove_dir(spisok):
    for i in spisok:
        os.rmdir(i)
    print('Все папки успешно удалены!')

make_dir(spisok1)

answer = ''
while answer != 'q':
    answer = input('Хотите удалить все созданные ранее папки? (Y/N)')
    try:
        if answer == 'Y':
            remove_dir(spisok1)
    except Exception:
        print('Чтото пошло не так')

#
# while answer != "q":
#     answer = input("Давайте выполним несколько операций? Y/N")
#     if answer == 'Y':
#         answer_choose()
#         delo = ""
#         while delo != 0:
#             delo = int(input("Введите вариант:"))
#             print("")
#             if delo == 1:
#                 print("Результат:")
#                 print(os.listdir())
#                 answer_choose()
#             elif delo == 2:
#                 print("Результат:")
#                 print(os.getcwd())
#                 answer_choose()
#             elif delo == 3:
#                 print("Результат:")
#                 print(psutil.cpu_count())
#                 answer_choose()
#             elif delo == 4:
#                 print("Результат:")
#                 file_list = os.listdir()
#                 i = 0
#                 while i < len(file_list):
#                     newFileName = (file_list[i] + ".dupl")
#                     print(newFileName)
#                     # копирование
#                     proverka_file(file_list[i])
#                     i += 1
#                 answer_choose()
#             else:
#                 pass
#     elif answer == "N":
#         print("Приходдите когда будете готовы поработать")
#     else:
#         print("Кажется вы не определились. Возвращайтесть снова..")
#





# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.