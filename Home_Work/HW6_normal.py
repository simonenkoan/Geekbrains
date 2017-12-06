# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

import random
import os
import sys
import time


class Person(object):
    def __init__(self, health, damage, armor):
        self.health = health
        self.damage = damage
        self.armor = armor

    def live_or_dead(self):
        if self.health <= 0:
            print(self, 'Вася победил')

class Player(Person):
    # def level_up:
    #     level = random.randint(0,10)

    def __init__(self, health, damage, armor, level):
        super().__init__(health, damage, armor)
        self.level = random.randint(1,3)


    def _attack_from_Enemy(self):
        print('Маниак наносит удар')
        self.health = int(self.health) - (round(int(maniak.damage * maniak.special) / self.armor /self.level))
        time.sleep(0.5)
        print('Васино здоровье = {}'.format(vasya.health))


class Enemy(Person):
    def __init__(self, health, damage, armor, special):
        super().__init__(health, damage, armor)
        self.special = random.randint(2,3)
        self.damage = damage * self.special

    def _attack_from_Player(self):
        print('Вася наносит удар')
        self.health = int(self.health) - (round(int(vasya.damage * vasya.level) / self.armor))
        time.sleep(0.5)
        print('Здоровье маньяка = {}'.format(maniak.health))


vasya = Player(100, 100, 10, 1)
maniak = Enemy(100, 100, 10, 1)

print('Васино здоровье = {} , Урон = {}, Броня = {}, Разряд по самбо = {}'.format(vasya.health, vasya.damage, vasya.armor, vasya.level))
print('Здоровье маньяка = {} , у него нож и урон = {}, Броня = {}'.format(maniak.health, maniak.damage, maniak.armor))
time.sleep(5)

# class Fight():
#     while True:
#         if vasya.health > 0 and maniak.health > 0:
#             if vasya.health > 0:
#                 vasya._attack_from_Enemy()
#             else:
#                 print('Маниак победил')
#                 break
#             if maniak.health > 0:
#                 maniak._attack_from_Player()
#             else:
#                 print('Вася победил')
#                 break


# while vasya.health > 0:
#     while maniak.health > 0:
#         vasya._attack_from_Enemy()
#         maniak._attack_from_Player()
#         if vasya.health < 0:
#             print("Маньяк одолел Васю")
#             break
#             break
#         elif maniak.health <= 0:
#             print("Вася победел злобного Маньяка")
#             break


class Fight:
    def fight_begin(self):
        while vasya.health > 0 and maniak.health >0:
            if maniak.health >0:
                vasya._attack_from_Enemy()
            if vasya.health > 0:
                maniak._attack_from_Player()
        if vasya.health > 0:
            vasya.live_or_dead()
        elif maniak.health > 0:
            print('Маньяк победил', 'Васюня - ', '{}'.format(vasya.live_or_dead()))



# while vasya.health > 0 and maniak.health > 0:
#     if maniak.health >0:
#         vasya._attack_from_Enemy()
#     if vasya.health > 0:
#         maniak._attack_from_Player()
#
# if vasya.health > 0:
#     print('Вася победил')
# elif maniak.health > 0:
#     print('Маньяк победил')

fight = Fight()
fight.fight_begin()


# print('Vasya, Health = {} , Damage = {}, Armor = {}, Level = {}'.format(vasya.health, vasya.damage, vasya.armor, vasya.level))
# print('Maniak, Health = {} , Damage = {}, Armor = {}'.format(maniak.health, maniak.damage, maniak.armor))


# vasya_shvarcenegger._attack_from_Enemy()
# maniak_slabak._attack_from_Player()

