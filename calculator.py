from colorama import init
from colorama import Fore, Back, Style
init()

print( Back.GREEN )
what = input("Виберіть дію(+,-,*,,/):")

print( Back.CYAN )
a = float( input("Введіть перше число:") )
b = float( input("Введыть друге число:") )

print( Back.YELLOW + Fore.BLACK )
if what == "+":
    c = a + b
    print("Результат:" + str(c))
elif what == "-":
    c = a - b
    print("Результат:" + str(c))
elif what == "*":
    c = a * b
    print("Результат:" + str(c))
elif what == "/":
    c = a / b
    print("Результат:" + str(c))
else:   
   print("Выбрана неверная операция!")

input()



#Здесь был текст