# a = range (0,100)
#
# for x in a:
#     # print(type(str(x)))
#     y = str(x)
#     z = type(y)
#     print(y,z)

# print('Task1')
# f_name = '0'
# s_name = '0'
# age = 0
# weight = 0
# f_name = input('Please input your first name ')
# s_name = str(input('Please input your second name '))
# age = int(input('Please input your age '))
# weight = int(input('Please input your weight '))

#
# str = "this is string example....wow!!!";
#
# sub = "i";
# print ("str.count(sub, 4, 40) : ", str.count(sub, 4, 40))
# sub = "wow";
# print ("str.count(sub) : ", str.count(sub))


# fruits = ['яблоко', 'банан', 'киви', 'апельсин']
#
# n = 0
# for fruit in fruits:
#     print (n, '{:>8}'.format(fruit))
#     n += 1
#
#
# # Задача 1
# fruits = ['яблоко', 'банан', 'киви', 'апельсин']
#
# for index, fruit in enumerate(fruits):
#      print(index, '{:>8}'.format(fruit))
####

# Задача 2

# spisok1 = [1, 2, 10, 'a', 'b', 'y']
# spisok2 = [1, 2, 20, 'a', 'b', 'z']
#
# spisok3 = set(spisok1) - set(spisok2)
# print(spisok3, type(spisok3))

# Задача 2

spisok1 = [1, 2, 10, 'a', 'b', 'y']
spisok2 = [1, 2, 20, 'a', 'b', 'z']

# spisok3 = spisok1  spisok2

# for index1,znach1 in enumerate(spisok1):
#     for index2,znach2 in enumerate(spisok2):
#         if index1 == index2:
#             spisok1.pop(index1)
# for index1,znach1 in enumerate(spisok1):
#     if znach1 in spisok2:
#         spisok1.remove(znach1)

for index1 in spisok1:
    # if spisok1[index1] in spisok2:
    #     spisok1.remove(index1)
    print (spisok1[index1])
# print (spisok1)


# n = 0

# print( '{0[0]} {0[1]}'.format(fruits))
#     # n += 1




# print("Units destroyed: {players[0]}".format(players = [1, 2, 3]))





spisok1 = [1, 2, 3, 'mark', 'alex', 'lorem']
spisok2 = [2, 4, 3, 'mark', 'alex', 'ray']
spisok3 = []

for znach in spisok1:
    if znach not in spisok2:
        spisok3.append(znach)
print(spisok3)
1


