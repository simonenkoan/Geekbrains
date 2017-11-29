# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
# import psutil
# import shutil
import sys


spisok1 = ['dir_'+ str(i) for i in range(10)]

def make_dir(spisok):
    try:
        for i in spisok:
            os.mkdir(i)
        print('Папки успешно созданы')
    except Exception:
        print('Ошибка создания. Папки уже созданы')

def remove_dir(spisok):
    for i in spisok:
        os.rmdir(i)
    print('Все папки успешно удалены!')

def trying():
    try:
        return str(sys.argv)
    except Exception:
        print(' Это нельзя')
    finally:
        print(type(list(sys.argv)))

def help_1():
    print('''
    Commands:
    mkdir - make dir_0 to dir_9 in current dir
    removedir - del dir dir_0 to dir_9 in current dir
    help_1 - print help
    ''')

answer = ''

# while answer != 'q':
#     print('Нажмите 1 хотите создать папки и 2 если хотите удалить (доступно после создания)')
#     answer = input('(1-создать, 2-удалить, q - выйти)')
#     try:
#         if answer == '2':
#             remove_dir(spisok1)
#         elif answer == '1':
#             make_dir(spisok1)
#         else:
#             break
#     except Exception:
#         print('Чтото пошло не так')

key = sys.argv
print(key)
list1 = key


do = {
    "help_1" : help_1,
    "mkdir" : make_dir,
    "removedir" : remove_dir
}

print(do['mkdir'])

#
# if key[1] == 'help_1':
#     do['help_1']()
# elif key[1] == 'mkdir':
#     do['mkdir'](spisok1)
# elif key[1] == 'removedir':
#     do['removedir'](spisok1)
# print('"help" for info')


command = key[1]

if command:
    print('help_1 for help')
    try:
        if do.get(command):
            if command == 'help_1':
                do[command]()
            else:
                do[command](spisok1)
    except Exception:
        print('"help_1" for info')




# print ("This is the name of the script: ", sys.argv[0])
# print ("Number of arguments: ", len(sys.argv))
# print ("The arguments are: ", trying())


# print('вы вышли из программы')
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

# def proverka_file(filename_i):
#     if os.path.isfile(filename_i):
#         shutil.copy(filename_i, newFileName)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.