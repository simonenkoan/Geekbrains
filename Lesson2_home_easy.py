
# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

print("Задача 1. Способ 1")
fruits = ['яблоко', 'банан', 'киви', 'апельсин']
n = 0
for fruit in fruits:
    print (n, '{:>8}'.format(fruit))
    n += 1
print("")


print("Задача 1. Способ 2")
fruits = ['яблоко', 'банан', 'киви', 'апельсин']
for index, fruit in enumerate(fruits):
    print(index, '{:>8}'.format(fruit))
print("")


# Задача 2 (через множества)

print("Задача 2. Способ 1")
spisok1 = [1, 2, 10, 'a', 'b', 'y']
spisok2 = [1, 2, 20, 'a', 'b', 'z']
spisok3 = set(spisok1) - set(spisok2)
print(spisok3, type(spisok3))
print("")

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

print("Задача 2. Способ 2")
spisok1 = [1, 2, 10, 'a', 'b', 'y']
spisok2 = [1, 2, 20, 'a', 'b', 'z']
spisok3 = []
for index, znach in enumerate(spisok1):
    if znach not in spisok2:
         spisok3.append(znach)
print(spisok3)
print("")


print("Задача 2. Способ 3")
spisok1 = [1, 2, 10, 'a', 'b', 'y']
spisok2 = [1, 2, 20, 'a', 'b', 'z']
spisok3 = []
for znach in spisok1:
    if znach not in spisok2:
        spisok3.append(znach)
print(spisok3)
print("")


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

print("Задача 3.")
spisok1 = [1, 2, 10, 16, 19, 40]
spisok4 = []
for c in spisok1:
    if c % 2 == 0:
        spisok4.append(int(c/4))
    else:
        spisok4.append(c*2)
print (spisok4)
# spisok2 = [c*2 for c in spisok1 if c % 2 == 0 ]

