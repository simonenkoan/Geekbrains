# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

# ---------->  ЗАДАНИЕ 1,2,3 ВЫПОЛНЯЕТСЯ ЧЕРЕЗ АРГУМЕНТЫ ПЕРЕДАННЫЕ ФАЙЛУ .py  <----------

import os
import shutil
import sys

# ---------->  Блок описания Функций ( имена которых вызываются через словарь DO)  <----------

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

def show_dir():
    print('Список папок в текущем каталоге:')
    for i in os.listdir():
        if not os.path.isdir(i):
            pass
        else:
           print(i)

def copy_file(filename_exec):
    if os.path.isfile(filename_exec):
        shutil.copy(filename_exec, filename_exec+'.copy')
        print('Копирование прошло успешно')
    else:
        print('Что-то пошло не так')

def help_1():
    print('''
    Commands:
    mkdir - make dir in current dir
    removedir - del dir in current dir
    help_1 - print help
    dirshow - show dir
    copy_file - copy python exec file
    ''')

# ---------->  Версия кода, где будут ждать пользователя для ввода варианта ответа  <----------
# answer = ''
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

# ---------->  Версия , где создается список непосредственно, после запуска файла  <----------
# if key[1] == 'help_1':
#     do['help_1']()
# elif key[1] == 'mkdir':
#     do['mkdir'](spisok1)
# elif key[1] == 'removedir':
#     do['removedir'](spisok1)
# print('"help" for info')

# ---------->  [Рабочая] Версия , с аргументами, передается второй аргумент после имени файла  <----------

key = sys.argv # <-----  в key записываем переданные аргументы после запуска

# <----- Создание словаря DO по ключам будут выбираться значения (которые соответствуют функциям в блоке функций)
do = {
    "help_1" : help_1,
    "mkdir" : make_dir,
    "removedir" : remove_dir,
    "dirshow" : show_dir,
    "copy_file": copy_file
}
command = 0
if len(key) > 1:
    command = key[1] # <----- Назначаем command первый элемент списка key

spisok1 = ['dir_' + str(i) for i in range(10)] # <----- Генерируем список с именами от dir_0 до dir_9

if command:
    print('help_1 for help')
    try:
        if do.get(command):
            if command == 'help_1':
                do[command]()
            elif command == 'dirshow':
                do[command]()
            elif command == 'copy_file':
                do[command](key[0])
            else:
                do[command](spisok1)
    except Exception:
        print('"help_1" for info')


if command == 0:
    help_1()