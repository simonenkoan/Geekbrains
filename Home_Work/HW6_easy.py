# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

import random
from pynput import keyboard


def on_press(key):
    try:
        pass
        # print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        pass
        # print('special key {0} pressed'.format(
        #     key))


class Car(object):
    def __init__(self, model, speed, color, is_police=False):
        self.model = model
        self.speed = speed
        self.color = color

    # def __str__(self):
    #     print(self.color, self.speed, self.model)

    def go(self):
        print("Наш", self.model,'начал движение со скоростью',self.speed)

    def stop(self):
        print("Наш", self.model,'остановился')

    def turn(self, turn_side=''):
        if turn_side == 'влево':
            turn_side = 'повернул налево'
        elif turn_side == 'вправо':
            turn_side = 'повернул направо'
        else:
            turn_side = 'развернулся'
        print(self.model, turn_side)


class TownCar (Car):
    def total_speed(self):
        self.speed = input('Введите максимальную скорость для городского автомобиля:')

class SportCar(Car):
    def __init__(self, model, speed, color, sound, ispolice=False):
        super().__init__(model,speed,color,sound)
        self.sound = input('Введите громкость музыки для спортивного авто(Вт):')
    def go(self):
        print("Наш", self.model,'начал движение со скоростью',self.speed, 'из машины слышится звук мощностью', self.sound)


car1 = Car('Toyota', '100', 'red', True)
car2 = TownCar('Nissan', '200', 'blue')
car3 = SportCar('Honda', '200', 'черный', False)
car2.total_speed()

garage = [car1, car2, car3]


def change_car():
    choose_car = input ('Выберите машину: (car1, car2, car3)')
    if choose_car == 'car1':
        return  car1
    elif choose_car == 'car2':
        return  car2
    elif choose_car == 'car3':
        return  car3
current_car = garage[0]
def on_release(key):
    # print('{0} released'.format(key))
    current_car = garage[int(input('Enter number 0-2: '))]
    # print(cars.model)
    if key == keyboard.Key.up:
        current_car.go()
    elif key == keyboard.Key.down:
        current_car.stop()
    elif key == keyboard.Key.left:
        current_car.turn('влево')
    elif key == keyboard.Key.right:
        current_car.turn('вправо')
    elif key == keyboard.Key.shift_r:
        current_car.turn('развернулся')
    elif key == keyboard.Key.backspace:
        current_car = change_car()
        print(current_car.model)
        # Stop listener
    else:
        pass
    return


# print(car2.model, car2.speed, car2.color)
# print(car3.model, car3.speed, car3.sound, car3.color)
print('''Нажмите на клавиатуре стрелку вперед чтобы ехать, 
        влево вправо чтобы поворачивать и назад чтобы остановиться:
        Чтобы сменить автомобиль нажмите Backspace \n''')
with keyboard.Listener( on_release=on_release ) as listener:
    listener.join()


print(" Конец программы")

