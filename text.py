import math

#   Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3
#  значения (с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата

def kvadrat(storona):
    p = storona * 4
    s = storona * storona
    gip2 = storona ** 2 + storona ** 2
    gip = math.sqrt(gip2)    #Импорт с библиотеки math, питется именно с math!
    print('Периметр: ' + str(p) )
    print('Площадь: ' + str(s))
    print('Диагональ: ' + str(gip))

kvadrat(5)

#   Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую 
#  время года, которому этот месяц принадлежит (зима, весна, лето или осень).

def season(number):

    z = [1, 2, 12]
    v = [3, 4, 5]
    l = [6, 7, 8]
    o = [9, 10, 11]

    if number in z:  #Если номер у списку З
        print('Это зима')
    elif number in v:   #Если номер у списку В
        print('Это весна')
    elif number in l:   #Если номер у списку Л
        print('Это лето')
    elif number in o:   #Если номер у списку О
        print('Это осень')

season(1)