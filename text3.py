

def data(day, mounth, year):
    lm = [1, 3, 5, 7, 8, 10, 12]
    

    if year <= 2019:

        if mounth in lm:
           
           
            if day <= 30:
                print('Такая дата существует')
            else:
                print('Неможлива дата')

        elif mounth <= 12:
           
            if mounth == 2:
                if day <= 28:
                    print('Такая дата существует')
                else:
                    print('Неможлива дата')
            elif day <= 31:
                print('Такая дата существует')
            else:
                print('Неможлива дата')
            
        else:
            print('Неможлива дата')


    else:
        print('Неможлива дата')

data(25, 5, 1953)
