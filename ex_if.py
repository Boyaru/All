name = input('Введите имя: ')
age = int(input('Ваш возраст: '))
age = abs(age)

def life_progress():
    if age <= 6:
        print('Тебе в детсад')
    elif age <= 17:
        print('Тебе пора в школу')
    elif age <= 22:
        print('Тебе в шарагу')
    elif age <= 60:
        print('Иди работай, бл*ть')
    else:
        print('Умри блять')

life_progress()