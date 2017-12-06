#################################УРОК 1####################################

x = 27
x = 5.2
x = 'qwrety'
x = True
x = False
is_admin = True

some_list = [1, 3, 4, 4.4, 'qweqw', True]
some_list[0] = 100
some_tuple = (1, 2, 3, 4)

some_dict = {'name': 'Vasya', 'age': 10}
some_dict['name'] = 'Ivan'

# name = input('Введите ваше имя: ')
# print('Привет ' + name)

# age = int(input('Введите число: '))
# print(age + 1)

# print(5 > 4)
# print(5 > 10)
# print(5 == 10)
# print(5 != 10)
# print(5 >= 10)
# print(5 <= 10)

# a = 201
#
# if a <= 100:
#     print('А меньше или равна 100')
# elif a < 200:
#     print('Несмотря на то, что а больше 100, она меньше 200')
# else:
#     print('А больше 100')

# a = -1
# while True:
#     a += 1
#     if a > 10:
#         continue
#     if a % 2 > 0:
#         break
#     print(a)


a = 2
a *= 2
print(a)
#################################УРОК 2####################################
# print('qwerty' * 3)
# print('qwerty' 'asdfgh')
# a = 'asd'
# print(a * 3)
#
# a = 'qwerty'
# print(a[2::2])
# print(len(a))
#
#
# print(a.title())
# print(a.upper())
# print(a.lower())

# print('bebebe'.find('be', 1))

# name = 'Vasya'
# surname = 'Pupkin'
# age = 100
# count = 50
#
# asd = 'РџСЂРёРІРµС‚ {} {:-<{}} {}'

# result = 'Hello %s %s %i' % (name, surname, age)
# result = asd.format(name, surname, count, age)
# print(result)

# my_list = [1, 10, 40, 11, 90, 'asdas', 1 < 0]
# my_list.append('qweqweqwe')
# my_list.insert(0, ['a', 'v', 'c'])
# print(my_list)
# print(len(my_list))
# print(my_list.index(10))
# print(my_list[::2] + ['a', 'v', 'c'][1:])


# a = [[1, 2, 3, [123123]], [4, 5, 6], [7, 8, 9]]
# a[0][3][0]

# a = [1, 3, 4]
# a.append(100)
# print(a[-1])
# print(a.pop(1))
# print(a)

# admins = ('Vasya', 'Petya')
# admin = ('Vasya',)

# items = [1, 2, 3, 4, 5]
# items2 = [1, 2, 3, 4, 5]

# for index, item in enumerate(items):
#     print(item * items2)

# for x in items[::2]:
#     print(x)

# a = 'qwerty'
# for i in a:
#     print(i)

car = {'model': 'Lada', 'color': 'White', 'max_speed': 100}
# print(car['model'])
# print(car['color'])
car['color'] = 'Black'
# print(car['color'])
# car['is_sport_car'] = car['max_speed'] > 200
# print(car)

# for value in car.values():
#     print(value)
#
# print(car['model'])
# print(car['color'])
# print(car['max_speed'])

# print(car['model'][1])

# a = set(['Hello', 'Vasya', 'Hello', 2])
# b = set(['Hello', 'Vasya', 'Vasya', 1])
# print(a)
# print(len(a))
# print('Vasya' in a)
# print(a | b)
# print(type(a))

a = [1, 2, 3, 4, 5, 6, 7]

for elem in a:
    if elem % 2 == 0:
        print(elem)



for index, elem in enumerate(a):
    print(index, elem)

for elem in a:
    print(a.index(elem), elem)

#################################УРОК 3####################################
# for i in range(10):
#     print(i)

# print(abs(-100))
# print(max(['qwe', 'qweqeeee', 'qwee']))
# round(5.55555, 2)


# def car_go(car_model):
#     print('{} РѕС‚РїСЂР°РІР»СЏРµС‚СЃСЏ РІ РїСѓС‚СЊ!'.format(car_model))
#
# def car_beep():
#     print('BEEEEP!')
#
# car_go('Lada')
# car_go('Nissan')
# car_go('Ferrari')
#
# car_beep()


# def summ(a, b):
#     return a + b
#
# result = summ(1, 5)
#
# print(result)
#
#
# def get_letter(letter, mark):
#     return letter + mark
#
# print(get_letter('РїРёСЃСЊРјРѕ ', 'РјР°СЂРєР°'))


# def has_access(login):
#     if login == 'admin':
#         return True
#     return False
#
# login = input('Login:')
#
# if has_access(login):
#     print('Р’Р°Рј РїСЂРµРґРѕСЃС‚Р°РІР»РµРЅ РґРѕСЃС‚СѓРї')
# else:
#     print('Р’ РґРѕСЃС‚СѓРїРµ РѕС‚РєР°Р·Р°РЅРѕ')


# access = True
#
# if access:
#     def render(name):
#         return 'Welcome, {}'.format(name)
# else:
#     def render(name):
#         return '{}, sorry. Try to enter again.'.format(name)
#
#
# print(render('РРІР°РЅ'))

# a = 5
#
# def sqrt(number):
#     my_sqrt_helper = 0.5
#     return number ** my_sqrt_helper

# def my(x):
#     return x ** 2
#
# my_func = lambda x: x ** 2
# print(my_func(2))
# print((lambda x: x ** 2)(2))

# def my_func(*args):
#     my_list = []
#     for i in args:
#         my_list.append(i ** 2)
#     return my_list
#
#
# print(my_func(1, 2, 3, 4, 5, 6))
#
# arguments = [1, 2, 3, 4, 5, 6]
# print(my_func(*arguments))


# def render_person(**kwargs):
#     # for key, value in kwargs.items():
#     #     print(key, value)
#     print('Hello {} you have {} years old'.format(kwargs['name'], kwargs['age']))
#
# render_person(name='Vasya', age=123, surname='Pupkin')


# def render_name(name='Unknown'):
#     print('Hello  {}'.format(name))
#
# render_name('asd')

# a = ['Vasya', 'Oleg', 'QQQQ']
# b = ['Pupkin', 'Ivanov']
# b.reverse()
# print(list(zip(a,b)))

# my_func = lambda x: x ** 2

# def my_func(x):
#     return x ** 2
#
# my_list = [2, 4, 6]
# print(list(map(my_func, my_list)))

# print(list(filter(lambda x: x > 0, [2, 4, 5, -6, 1, -3])))
#
#
# def my_func(list_x):
#     result = []
#     for i in list_x:
#         if i > 0:
#             result.append(i)
#     return result
#
#
# print(my_func([2, 4, 5, -6, 1, -3]))


file = open('1.txt', 'r', encoding='UTF-8')
for line in file:
    ip, access, url = line.split()
    print('ip {} has access type {} to url {}'.format(ip, access, url))
file.close()


with open('1.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        ip, access, url = line.split()
        print('ip {} has access type {} to url {}'.format(ip, access, url))


#################################УРОК 4####################################



# a = 4
# a = 4.4
# a = 'asdasd'
# b = 6
# x = [1, 2]
#
# def some_func(something):
#     something += 100
#     return something
#
# a = some_func(a)

# def some_func2(some_list):
#     some_list[0] = 100
#     some_list.append(10000)
#
# some_func(a)
# print(a)
#
# some_func(b)
# print(b)
#
# some_func2(x)
# print(x)

# import copy
#
# a = [1, 2, 3, 4, 5, [90, 91]]
# copy_a = copy.deepcopy(a)
#
# for i in copy_a:
#     if type(i) == list:
#         i[0] = 1000
#
# print(a)
# print(copy_a)

# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
# print(matrix[0][2])
# print(matrix[2][1])
#
# for line in matrix:
#     for elem in line:
#         print(elem)
#
# print(list(zip(*matrix)))

# print(False or False)
# print(bool(100000) and bool(10))
# name = input('name:')
# correct_name = name or 'Guest'
#
# print(correct_name)

# if 5 > 0:
#     print('5')
# else:
#     print('0')
#
# print(5 if 5 > 0 else 0)

# a = 10
# b = 10
# print(a is b)
#############
# c = [1, 2]
# d = [1, 2]
# print(c is d)
# a = None
#############
import random

#
# my_list = []
#
# for _ in range(10):
#     my_list.append(random.randint(-100, 100))

# my_list = [random.randint(-100, 100) for _ in range(10)]
# print(my_list)

# my_list = [i for i in range(10) if i % 2 == 0]
# print(my_list)

# names = ['Vasya', 'Olya']
# salary = [100, 200]
# my_dict = {key: value for key, value in zip(names, salary)}
# print(my_dict)
#
# my_dict = {i: i + 2 for i in [1, 2, 3, 4, 5, 6, 7, 8]}
# print(my_dict)

# import re

# some_string = 'asdasd@mail.ru'
# pattern = '[0-9_\.-a-zA-Z]+@[0-9-a-zA-Z]+\.ru|com|org'
# print(re.match(pattern, some_string))
# print(re.search(pattern, some_string))
# if some_string not in re.findall(pattern, some_string):
#     print('email is incorrect')
# else:
#     print('email is correct')
import io

a = ['2', 'asd', '23']

try:
    f = open('1.txt', 'r')
    f.write('12312')
except io.UnsupportedOperation:
    print('РћРїРµСЂР°С†РёСЏ РЅР°Рґ С„Р°Р№Р»РѕРј РЅРµ РІРѕР·РјРѕР¶РЅР°!')
else:
    print('РћС€РёР±РѕРє РЅРµС‚')
finally:
    f.close()



print(100)

#################################УРОК 5####################################
# import code2
# from code2 import summ_plus_100
# from code2 import pow
# from code2 import *

# print(code2.summ_plus_100(1))
# print(code2.pow(1, 2))

# print(summ_plus_100(1))
# print(pow(1, 2))

# import sys
# print(sys.path)


# import os
#
# print(os.name)
# print(os.getcwd())
# try:
#     os.mkdir('test_dir')
# except FileExistsError:
#     print('Такая папка уже есть!')

import os
import sys
print('sys.argv = ', sys.argv)

def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")

def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))

def ping():
    print("pong")

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping
}


try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None
if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")



def summ_plus_100(x):
    return x + 100

def pow(x, y):
    x ** 1


#################################УРОК 6####################################
    import random

    class Person:

        def __init__(self, name, surname, email, is_service_account=False):
            self.name = name
            self.surname = surname
            self._email = email
            self._id = random.randint(10000, 99999)
            self.is_service_account = is_service_account

        def change_name(self, name):
            self.name = name

        def change_surname(self, surname):
            self.surname = surname

    user1 = Person('Vasya', 'Pupkin', '123@123.com')
    user2 = Person('NeVasya', 'NePupkin', 'Ne123@123.com')

    class Manager(Person):

        def change_email(self, person, new_email):
            person._email = new_email

    class Admin(Manager):

        def __init__(self, name, surname, email, admin_type, is_service_account=False):
            # Manager.__init__(self, name, surname, email, is_service_account)
            super().__init__(name, surname, email, is_service_account)
            self.admin_type = admin_type

        def remove_person(self, person):
            if person.is_service_account:
                result = input('Р­С‚Рѕ СЃРµСЂРІРёСЃРЅС‹Р№ Р°РєРєР°СѓРЅС‚, РІС‹ СѓРІРµСЂРµРЅС‹? y/n')
                if result == 'y' and person != self:
                    database.remove(person)
                elif person == self:
                    print('РўС‹ РІ СЃРІРѕРµРј СѓРјРµ СѓРґР°Р»СЏС‚СЊ СЃР°Рј СЃРµР±СЏ!?')
                    result = input(
                        'РќСѓ РµСЃР»Рё С‚С‹ СЃРѕРІСЃРµРј СЃСѓРјР°С€РµРґС€РёР№, С‚Рѕ РґР°Р№ СЃРѕРіР»Р°СЃРёРµ! y/n')
                    if result == 'y':
                        database.remove(self)
            else:
                database.remove(person)

    manager = Manager('Igor', 'Ivanov', 'mn@mn.com', True)
    admin = Admin('Sasha', 'Petrov', 'admin@admin.com', 'linux', True)

    print(admin.admin_type, admin._id)

    database = [user1, user2, manager, admin]

    # print(admin.is_service_account)
    # print(manager._email)
    # admin.change_email(manager, 'newemail@mail.com')
    # print(manager._email)
    #
    # for person in database:
    #     print(person.name)
    #
    # admin.remove_person(user1)
    # admin.remove_person(manager)
    # admin.remove_person(admin)
    #
    # for person in database:
    #     print(person.name)
    # -----------------------------------------------------------------------------------------
    class Vehicle:

        def go(self):
            print('РўСЂР°РЅСЃРїРѕСЂС‚РЅРѕРµ СЃСЂРµРґСЃС‚РІРѕ РЅР°С‡РёРЅР°РµС‚ РґРІРёР¶РµРЅРёРµ')

        def stop(self):
            print('РўСЂР°РЅСЃРїРѕСЂС‚РЅРѕРµ СЃСЂРµРґСЃС‚РІРѕ РѕСЃС‚Р°РЅР°РІР»РёРІР°РµС‚СЃСЏ')

    class Car(Vehicle):

        def __init__(self, car_model, car_speed):
            self._model = car_model
            self.speed = car_speed

        def _start_engine(self):
            print('Р—Р°РїСѓСЃРє РґРІРёРіР°С‚РµР»СЏ')

        def go(self):
            self._start_engine()
            print('Car {} is going with speed {}'.format(self._model, self.speed))

        def stop(self):
            print('Car {} is stopped'.format(self._model))

    class SportCar(Car):

        def __init__(self, car_model, car_speed, color='Red'):
            super().__init__(car_model, car_speed)
            self.color = color

    class Cycle(Vehicle):

        def go(self):
            print('Р’РµР»РѕСЃРёРїРµРґ РїРѕРµС…Р°Р»')

        def stop(self):
            print('Р’РµР»РѕСЃРёРїРµРґ РѕСЃС‚Р°РЅРѕРІРёР»СЃСЏ')

    semaphor_current_color = 'green'

    def semaphor(vehicle):
        if semaphor_current_color == 'green':
            vehicle.go()
        else:
            vehicle.stop()

    vehicles = [SportCar('Ferrari', 200), Cycle(), Car('Lada', 100)]

    for vehicle in vehicles:
        semaphor(vehicle)
        semaphor_current_color = 'red'


#################################УРОК 7####################################



#################################УРОК 8####################################