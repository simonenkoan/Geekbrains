print("Hello Geekbrains!")

def inform():
    print("Здравствуйте,", fio)
    print("Ваш возраст, -", vozrast)
    print("Ваш вес,", weight)

while True:
    weight_good = range (50,120)
    fio = str(input ("Введите ваше ФИО: "))
    vozrast = int(input("Введите ваш возраст: "))
    weight = int(input("Введите ваш вес, кг: "))
    inform()
    if vozrast <= 30:
        if weight in weight_good:
            print("С вашим здоровьем всё в порядке")
        else:
            print ("Вам следует пройти обследование чтобы мы вам выдали рекомендации")
    elif vozrast > 30 and vozrast <=40:
        if weight not in weight_good:
            print ("Вам нужно вести здоровый образ жизни")
        else:
            print ("Вам следует пройти обследование чтобы мы вам выдали рекомендации")
    elif vozrast > 40:
        if weight not in weight_good:
            print("Вам следует обратиться к врачу")
        else:
            print ("Вам следует пройти обследование чтобы мы вам выдали рекомендации")
    else:
        pass
    1